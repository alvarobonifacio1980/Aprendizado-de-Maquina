"""Aquisição explícita dos três históricos financeiros (2016–2025).

Uso, na raiz do trabalho:
    python obter_dados.py
    python obter_dados.py --force

Requer: pandas e requests. Não gera ou recria resultados de triagem/ablação.
Os CSVs existentes são preservados, salvo quando --force é usado.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import pandas as pd
import requests

DATA_DIR = Path(__file__).resolve().parent / "dados"
START, END = "2016-01-01", "2025-12-31"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "Portfolio-Academico-AM/1.0"


def _get(url, **kwargs):
    response = SESSION.get(url, timeout=90, **kwargs)
    response.raise_for_status()
    return response


def petr4():
    url = "https://brapi.dev/api/quote/PETR4"
    headers = {}
    if os.environ.get("BRAPI_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["BRAPI_TOKEN"]
    response = _get(url, params={"range": "max", "interval": "1d"}, headers=headers).json()
    series = response["results"][0]["historicalDataPrice"]
    df = pd.DataFrame(series)
    required = {"date", "open", "high", "low", "close", "adjustedClose", "volume"}
    if not required.issubset(df.columns):
        raise ValueError("brapi: colunas de preço esperadas não encontradas")
    timestamps = pd.to_datetime(df["date"], unit="s", utc=True)
    df["Date"] = timestamps.dt.tz_convert("America/Sao_Paulo").dt.tz_localize(None).dt.normalize()
    df = df[["Date", "open", "high", "low", "close", "adjustedClose", "volume"]]
    df = df[(df.Date >= START) & (df.Date <= END)].drop_duplicates("Date", keep="last")
    df = df.sort_values("Date").reset_index(drop=True)
    if df.empty or df.Date.min() > pd.Timestamp("2016-06-01"):
        raise RuntimeError("brapi: histórico insuficiente para 2016–2025; confira o limite do plano")
    if df.Date.max() < pd.Timestamp("2025-12-01"):
        raise RuntimeError("brapi: série termina antes de dezembro de 2025")
    return df


def ptax():
    endpoint = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
                "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)")
    chunks = []
    for year in range(2016, 2026):
        params = {"@dataInicial": f"'01-01-{year}'",
                  "@dataFinalCotacao": f"'12-31-{year}'",
                  "$format": "json", "$top": "10000"}
        payload = _get(endpoint, params=params).json()
        frame = pd.DataFrame(payload.get("value", []))
        if frame.empty:
            raise RuntimeError(f"BCB: nenhuma cotação no ano {year}")
        chunks.append(frame)
    raw = pd.concat(chunks, ignore_index=True)
    needed = {"dataHoraCotacao", "cotacaoVenda"}
    if not needed.issubset(raw.columns):
        raise ValueError("BCB: esquema inesperado")
    raw["Timestamp"] = pd.to_datetime(raw["dataHoraCotacao"], errors="coerce")
    raw["Date"] = raw["Timestamp"].dt.normalize()
    raw["value"] = pd.to_numeric(raw["cotacaoVenda"], errors="coerce")
    raw = raw.dropna(subset=["Date", "Timestamp", "value"])
    # Múltiplos boletins por dia: retenção da última cotação divulgada.
    raw = raw.sort_values("Timestamp").drop_duplicates("Date", keep="last")
    frame = raw[["Date", "value"]].sort_values("Date").reset_index(drop=True)
    if frame.empty or frame.Date.min() > pd.Timestamp("2016-02-01"):
        raise RuntimeError("BCB: cobertura de 2016 insuficiente")
    return frame


def fred():
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv"
    response = _get(url, params={"id": "DEXBZUS", "cosd": START, "coed": END})
    from io import StringIO
    frame = pd.read_csv(StringIO(response.text))
    date_col = "observation_date" if "observation_date" in frame.columns else "DATE"
    if date_col not in frame.columns or "DEXBZUS" not in frame.columns:
        raise ValueError("FRED: esquema inesperado")
    frame = frame[[date_col, "DEXBZUS"]].copy()
    frame.columns = ["DATE", "DEXBZUS"]
    frame["DATE"] = pd.to_datetime(frame["DATE"])
    frame["DEXBZUS"] = pd.to_numeric(frame["DEXBZUS"], errors="coerce")
    frame = frame[(frame.DATE >= START) & (frame.DATE <= END)].sort_values("DATE")
    if frame.empty:
        raise RuntimeError("FRED: série vazia")
    return frame


def main(force=False):
    DATA_DIR.mkdir(exist_ok=True)
    for filename, loader in [
        ("petr4_brapi_max.csv", petr4),
        ("BCB_PTAX_USDBRL.csv", ptax),
        ("DEXBZUS.csv", fred),
    ]:
        dest = DATA_DIR / filename
        if dest.exists() and not force:
            print(f"Preservado: {filename} (use --force para atualizar)")
            continue
        data = loader()
        if not len(data):
            raise ValueError(f"Não foi possível obter {filename}")
        data.to_csv(dest, index=False, date_format="%Y-%m-%d")
        print(f"Salvo: {dest.name}; {len(data)} observações; "
              f"período {data.iloc[0,0]} — {data.iloc[-1,0]}")
    print("Observação: provedores podem revisar históricos. Verifique a comparabilidade.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="sobrescreve CSVs existentes")
    args = parser.parse_args()
    main(force=args.force)

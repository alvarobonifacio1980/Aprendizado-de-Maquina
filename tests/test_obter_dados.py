"""Testes offline da aquisição e dos contratos de dados financeiros."""
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

ROOT = Path(__file__).resolve().parents[1] / "01_previsao_volatilidade"
sys.path.insert(0, str(ROOT))
import obter_dados as coleta


class FakeResponse:
    def __init__(self, payload=None, content=""):
        self.payload, self.text = payload, content

    def raise_for_status(self):
        pass

    def json(self):
        return self.payload


class ColetaTests(unittest.TestCase):
    def test_ptax_prioriza_ultimo_boletim_do_dia(self):
        def mock_get(url, **kwargs):
            ano = int(kwargs["params"]["@dataInicial"].strip("'").split("-")[-1])
            return FakeResponse({"value": [
                {"dataHoraCotacao": f"{ano}-01-04 10:00:00.000", "cotacaoVenda": 5.1},
                {"dataHoraCotacao": f"{ano}-01-04 13:00:00.000", "cotacaoVenda": 5.2},
            ]})
        with patch.object(coleta, "_get", side_effect=mock_get):
            frame = coleta.ptax()
        self.assertEqual(len(frame), 10)
        self.assertTrue((frame.value == 5.2).all())
        self.assertTrue(frame.Date.is_monotonic_increasing)

    def test_fred_lida_com_valores_ausentes_e_periodo(self):
        payload = "observation_date,DEXBZUS\n2015-12-31,3.9\n2016-01-04,4.0\n2016-01-05,.\n2026-01-05,5.0\n"
        with patch.object(coleta, "_get", return_value=FakeResponse(content=payload)):
            frame = coleta.fred()
        self.assertEqual(len(frame), 2)
        self.assertEqual(list(frame.columns), ["DATE", "DEXBZUS"])
        self.assertTrue(pd.isna(frame.iloc[1].DEXBZUS))

    def test_petr4_exige_colunas_de_preco_ajustado(self):
        with patch.object(coleta, "_get", return_value=FakeResponse(payload={
            "results": [{"historicalDataPrice": [{"date": 1451865600, "close": 10}]}]
        })):
            with self.assertRaisesRegex(ValueError, "colunas"):
                coleta.petr4()

    def test_reuso_dos_arquivos_nao_consulta_provedores(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            data_dir = Path(temp)
            names = ("petr4_brapi_max.csv", "BCB_PTAX_USDBRL.csv", "DEXBZUS.csv")
            for name in names:
                (data_dir / name).write_text("Date,value\n2020-01-01,1\n", encoding="utf-8")
            with patch.object(coleta, "DATA_DIR", data_dir), patch.object(coleta, "_get") as get:
                coleta.main(force=False)
                get.assert_not_called()


if __name__ == "__main__":
    unittest.main()

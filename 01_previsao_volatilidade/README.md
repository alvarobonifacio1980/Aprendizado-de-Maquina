# 01 — Previsão de volatilidade: PETR4 e USD/BRL

Projeto independente de Machine Learning aplicado à previsão de séries temporais financeiras.

## Problema
Prever a volatilidade observada nos **cinco pregões seguintes** em duas séries financeiras: PETR4 e USD/BRL (PTAX). A PETR4 é o ativo principal; o câmbio também é avaliado como série com alvo próprio. Uma série externa de câmbio (FRED DEXBZUS) foi investigada como preditor adicional para PETR4.

## Notebook
[03_AM_PETR4_USDBRL.ipynb](03_AM_PETR4_USDBRL.ipynb)

O notebook preserva as 40 células do trabalho publicado anteriormente em `Analise-de-Dados`, inclusive saídas, gráficos e interpretações.

## Métodos
- Construção de atributos e alvos com horizonte de cinco pregões
- Divisão temporal entre desenvolvimento e teste
- `TimeSeriesSplit` com gap; seleção de modelos apenas na etapa de desenvolvimento
- Regressão Linear, SVR e Random Forest; ensembles e análise de sensibilidade
- Avaliação por MAE, RMSE, R² e comparação com volatilidade histórica

## Reprodução
O notebook espera ser executado **a partir desta pasta** e lê os arquivos `dados/*.csv`. Consulte [dados/README.md](dados/README.md).

**Estado atual:** notebook histórico publicado, mas o notebook ainda depende de CSVs locais gerados em etapas anteriores de aquisição pública e triagem que não estão incluídas nesta versão. As saídas gravadas no notebook são resultados do experimento original; não representam uma nova execução feita nesta publicação. Evite executar todas as células até disponibilizar os insumos exatos.

## Evolução
Estudos independentes posteriores de dados intradiários, incluindo **Machine Learning, Deep Learning e ensembles**, estão disponíveis na [coleção de estudos PETR4 RV60](../estudos/petr4_intradiario/README.md). O horizonte de 60 minutos desses estudos difere do horizonte de cinco pregões deste projeto.

### Atualização de dados

Na pasta deste trabalho execute `python obter_dados.py` para preencher somente históricos ausentes; use `python obter_dados.py --force` apenas se desejar sobrescrever os históricos com versões atuais. Consulte [as instruções completas](dados/README.md). O resultado reproduz o **protocolo principal**, mas não garante métricas idênticas ao snapshot original, especialmente se o provedor de dados alterar preços ou disponibilidade.

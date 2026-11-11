# PETR4 intradiária — portfólio de pesquisa aplicada

Três estudos **independentes** sobre previsão da variância realizada nos 60 minutos seguintes (**RV60**) de PETR4, a partir de candles de cinco minutos. A coleção destaca as técnicas e os resultados de modelagem preditiva.

**Escala dos experimentos:** 35.800 origens de previsão, 480 pregões e oito blocos temporais de avaliação. A avaliação considerou oito blocos temporais.

| Estudo | Conteúdo | Principal aprendizado |
|---|---|---|
| [01 — Modelos históricos e Machine Learning](01_baselines_e_ml.md) | Regressão Gamma, EWMA, Floresta Aleatória e XGBoost | O modelo líder varia conforme a métrica |
| [02 — Deep Learning](02_deep_learning.md) | LSTM, GRU, TCN e Transformer | A média de três TCN foi a melhor descritivamente, sem superioridade estatística confirmada diante de XGBoost |
| [03 — Ensembles e robustez](03_ensembles_e_robustez.md) | Combinação 50/50 e estabilidade temporal | ENS50 reduziu QLIKE e MAE; TCN permaneceu melhor em MSE |

**Como ler:** QLIKE, MSE e MAE são métricas de erro; valores menores são melhores. A QLIKE pode ser negativa, e diferenças da métrica não representam percentuais.

**Contexto da avaliação:** comparação exploratória das arquiteturas na base histórica estudada.

**Autoria:** Álvaro Bonifácio — estudos próprios de pesquisa e desenvolvimento em ciência de dados.
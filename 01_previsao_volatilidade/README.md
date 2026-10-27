# 01 — Previsão de volatilidade: PETR4 e USD/BRL

Projeto da disciplina **Aprendizado de Máquina — PPGCC/UFJF**.

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

**Estado atual:** notebook histórico publicado, mas os CSVs de entrada ainda não estão versionados. As saídas gravadas no notebook são resultados do experimento original; não representam uma nova execução feita nesta publicação. Evite executar todas as células até disponibilizar os insumos exatos.

## Evolução
Estudos posteriores de dados intradiários, modelos sequenciais (LSTM/GRU) e Transformers serão incorporados **somente após validação metodológica**, preservando a distinção entre resultados concluídos e experimentos em andamento.

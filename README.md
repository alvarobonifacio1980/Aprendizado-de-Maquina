# Aprendizado de Máquina — Portfólio de Pesquisa Aplicada

Projetos independentes de **análise e pesquisa aplicada**, com foco em Machine Learning, Deep Learning, séries temporais financeiras e previsão de volatilidade.

Os projetos exploram **problemas de previsão, preparação de dados, comparação de modelos e avaliação temporal**, com gráficos e resultados que ilustram as técnicas utilizadas.

## Estudos de caso — PETR4 intradiária

Três estudos de **pesquisa aplicada independente** com comparações de modelos, gráficos e interpretação de resultados.

| Estudo | Conteúdo |
|---|---|
| [Machine Learning e referências históricas](estudos/petr4_intradiario/01_baselines_e_ml.md) | Regressão Gamma, EWMA, Floresta Aleatória e XGBoost |
| [Deep Learning em séries temporais](estudos/petr4_intradiario/02_deep_learning.md) | LSTM, GRU, TCN e Transformer causal |
| [Ensembles e robustez](estudos/petr4_intradiario/03_ensembles_e_robustez.md) | ENS50, estabilidade por períodos e medidas alternativas |

[**Visão geral dos três estudos**](estudos/petr4_intradiario/README.md)

> Os estudos têm como objetivo estimar a intensidade das oscilações de preço, não sua direção.

## Evidências do experimento

Visualizações do estudo de previsão da volatilidade da PETR4 e do USD/BRL.

### Comparação de desempenho — PETR4

![RMSE no teste de modelos de previsão de volatilidade da PETR4](assets/graficos/rmse_petr4.png)

**Leitura:** o RMSE compara a magnitude dos erros dos modelos e do baseline no conjunto de teste. Valores menores indicam menor erro nessa métrica.

### Diagnóstico dos resíduos

![Histograma dos resíduos do modelo SVR PETR4-only](assets/graficos/histograma_residuos.svg)

**Leitura:** a distribuição dos resíduos ajuda a investigar erros sistemáticos, dispersão e valores extremos, complementando MAE e RMSE. O gráfico não substitui validação temporal ou testes adicionais de robustez.

[Consultar o notebook do projeto histórico](01_previsao_volatilidade/03_AM_PETR4_USDBRL.ipynb)

## Outros projetos publicados

### 01 — Previsão da volatilidade futura da PETR4 e do USD/BRL
**Área:** Machine Learning aplicado a dados financeiros  
**Abordagem:** modelos supervisionados e dados históricos obtidos de fontes públicas.

[Ver notebook e documentação](01_previsao_volatilidade/README.md) · [Abrir notebook](01_previsao_volatilidade/03_AM_PETR4_USDBRL.ipynb)

**Objetivo:** avaliar modelos supervisionados para estimar a volatilidade realizada nos cinco pregões seguintes.

**Métodos:** baseline de volatilidade histórica, regressão linear, SVR, Random Forest, ensembles e testes de estabilidade. O estudo inclui validação temporal e separação de dados de desenvolvimento e teste.

O projeto reúne código, visualizações e comparação entre modelos.

## Estudos adicionais em desenvolvimento

A previsão de volatilidade diária é uma investigação complementar, com horizonte de previsão próprio.

## Estrutura

```text
Aprendizado-de-Maquina/
├── 01_previsao_volatilidade/
│   ├── 03_AM_PETR4_USDBRL.ipynb
│   ├── README.md
│   └── dados/
│       └── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Execução

Instale dependências com `python -m pip install -r requirements.txt`. Abra o notebook **na pasta do trabalho**: a primeira célula prepara automaticamente os históricos públicos de PETR4, BCB PTAX e FRED. Também é possível executar `python obter_dados.py` nessa pasta. As fontes históricas são consultadas pelas APIs públicas descritas no projeto.

## Princípios metodológicos

- Divisão temporal e prevenção de vazamento de informação
- Transformações ajustadas exclusivamente nos dados de treino
- Comparação com referências simples (*baselines*)
- Registro das escolhas, das métricas e das análises
- Comparação consistente entre diferentes abordagens

**Tecnologias:** Python, Pandas, NumPy, Scikit-learn, Matplotlib e Jupyter.

---
**Autor:** Álvaro Bonifácio · pesquisa aplicada e projetos independentes

**Licença:** MIT para o código; fontes de dados externas seguem seus termos de uso.

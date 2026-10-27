# Aprendizado de Máquina — Portfólio Acadêmico

Projetos desenvolvidos durante o **Mestrado em Ciência da Computação (PPGCC/UFJF)**, com foco em aplicações de Aprendizado de Máquina, séries temporais financeiras e previsão de volatilidade.

O objetivo é apresentar o **problema, os dados, a metodologia, os resultados e as limitações** de cada experimento, com ênfase em comparação com baselines, avaliação temporal e prevenção de *data leakage*.

## Trabalhos publicados

### 01 — Previsão da volatilidade futura da PETR4 e do USD/BRL
**Disciplina:** Aprendizado de Máquina  
**Estado:** experimento clássico documentado; históricos públicos obtidos automaticamente, com triagem inicial identificada separadamente.

[Ver notebook e documentação](01_previsao_volatilidade/README.md) · [Abrir notebook](01_previsao_volatilidade/03_AM_PETR4_USDBRL.ipynb)

**Objetivo:** avaliar modelos supervisionados para estimar a volatilidade realizada nos cinco pregões seguintes.

**Métodos:** baseline de volatilidade histórica, regressão linear, SVR, Random Forest, ensembles e testes de estabilidade. O estudo inclui validação temporal e separação de dados de desenvolvimento e teste.

O notebook foi transferido do repositório `Analise-de-Dados` **sem alterar suas células, resultados ou gráficos**.

## Pesquisa em andamento

A investigação atual do mestrado amplia o estudo para dados intradiários e arquiteturas de aprendizado profundo, incluindo LSTM, GRU e Transformers. Esses experimentos serão publicados em etapas, **após consolidação e validação**; não há afirmação de superioridade antecipada.

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

Instale dependências com `python -m pip install -r requirements.txt`. Abra o notebook **na pasta do trabalho**: a primeira célula prepara automaticamente os históricos públicos de PETR4, BCB PTAX e FRED. Também é possível executar `python obter_dados.py` nessa pasta. Os arquivos originais da triagem de candidatos não foram recuperados: sem eles, a seleção histórica permanece uma decisão fixa documentada, não uma nova execução da busca. Resultados podem variar com revisões das APIs, e a coleta depende da disponibilidade e das condições dos provedores.

## Princípios metodológicos

- Divisão temporal e prevenção de vazamento de informação
- Transformações ajustadas exclusivamente nos dados de treino
- Comparação com referências simples (*baselines*)
- Registro das escolhas, das métricas e das limitações
- Divulgação apenas de resultados validados, diferenciando pesquisa em curso de trabalho concluído

**Tecnologias:** Python, Pandas, NumPy, Scikit-learn, Matplotlib e Jupyter.

---
**Autor:** Álvaro Bonifácio · Mestrando em Ciência da Computação — UFJF

**Licença:** o código do repositório está sob MIT; bases de terceiros mantêm suas respectivas condições de uso.

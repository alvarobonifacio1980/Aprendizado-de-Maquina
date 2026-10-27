# Aprendizado de Máquina — Portfólio Acadêmico

Projetos desenvolvidos durante o **Mestrado em Ciência da Computação (PPGCC/UFJF)**, com foco em aplicações de Aprendizado de Máquina, séries temporais financeiras e previsão de volatilidade.

O objetivo é apresentar o **problema, os dados, a metodologia, os resultados e as limitações** de cada experimento, com ênfase em comparação com baselines, avaliação temporal e prevenção de *data leakage*.

## Trabalhos publicados

### 01 — Previsão da volatilidade futura da PETR4 e do USD/BRL
**Disciplina:** Aprendizado de Máquina  
**Estado:** experimento clássico documentado; dados externos de entrada pendentes de publicação.

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

Instale dependências com `python -m pip install -r requirements.txt`. Abra o notebook **na pasta do trabalho** e disponibilize os arquivos descritos em [dados/README.md](01_previsao_volatilidade/dados/README.md). Os CSVs originais ainda não estão no GitHub; portanto, esta primeira publicação permite examinar os resultados salvos, mas **não garante uma execução ponta a ponta**.

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

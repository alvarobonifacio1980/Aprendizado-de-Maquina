# Insumos do primeiro trabalho

Ao abrir o notebook na pasta `01_previsao_volatilidade/`, ele usa `DATA = Path.cwd() / "dados"`.

## Arquivos de entrada necessários

| Arquivo | Uso |
|---|---|
| `petr4_brapi_max.csv` | Histórico da PETR4 (brapi), inclusive fechamento ajustado |
| `BCB_PTAX_USDBRL.csv` | Série de câmbio USD/BRL (PTAX) |
| `DEXBZUS.csv` | Série externa do FRED usada no teste de atributo adicional |
| `busca_ablation.csv` | Resultado da triagem anterior de candidatos externos |
| `auditoria_candidatos.csv` | Auditoria da etapa de seleção/triagem |

Esses arquivos **não foram localizados no repositório de origem** e ainda não foram publicados aqui. Especialmente `busca_ablation.csv` e `auditoria_candidatos.csv` representam resultados intermediários do processo experimental; não devem ser inventados ou substituídos por dados atuais sem registrar a mudança de protocolo.

## Arquivos de saída

O notebook também pode produzir arquivos como `previsoes_teste.csv`, `resultados_modelos.csv`, `importancia_atributos.csv`, `dados_preparados_PETR4.csv`, `dados_preparados_USDBRL.csv` e `sensibilidade_sementes.csv`. Não confunda as saídas com os insumos acima.

**Proveniência:** brapi (https://brapi.dev/), BCB (https://dadosabertos.bcb.gov.br/) e FRED (https://fred.stlouisfed.org/series/DEXBZUS). Para reprodução exata, use as mesmas versões, filtros, datas e convenções do experimento original; verifique também os termos de uso e redistribuição de cada fonte.

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

Os três históricos foram **obtidos originalmente de fontes públicas por código**, em uma etapa anterior da pesquisa. Os dois arquivos de triagem foram **produzidos pelo processamento experimental anterior**. Embora sua origem seja identificada, os cinco CSVs ainda não estão publicados aqui, e as células que os geraram não estão incluídas nesta versão do notebook. Especialmente `busca_ablation.csv` e `auditoria_candidatos.csv` representam resultados intermediários do processo experimental; não devem ser inventados ou substituídos por dados atuais sem registrar a mudança de protocolo.

## Arquivos de saída

O notebook também pode produzir arquivos como `previsoes_teste.csv`, `resultados_modelos.csv`, `importancia_atributos.csv`, `dados_preparados_PETR4.csv`, `dados_preparados_USDBRL.csv` e `sensibilidade_sementes.csv`. Não confunda as saídas com os insumos acima.

**Proveniência:** brapi (https://brapi.dev/), BCB (https://dadosabertos.bcb.gov.br/) e FRED (https://fred.stlouisfed.org/series/DEXBZUS). Para reprodução exata, use as mesmas versões, filtros, datas e convenções do experimento original; verifique também os termos de uso e redistribuição de cada fonte.

## Estratégia para reprodução integral

A abordagem prevista é recuperar as rotinas originais de aquisição (brapi, BCB e FRED) e de geração da triagem/ablação, registrar os parâmetros e salvar automaticamente os arquivos em `dados/`. Somente após comparar os arquivos reproduzidos com os insumos originais poderemos afirmar equivalência dos resultados. O fato de a fonte ser pública não garante que uma consulta posterior devolva o mesmo snapshot histórico.

# Forum V4 - Fase 8 - Curadoria Forte de Cultura - 2026-07-10

## Origem

Parecer editorial recebido depois da leitura prioritaria do dossie V4 por GPT 5.6 Sol. A leitura nao foi auditoria exaustiva do pacote inteiro; concentrou-se nos contratos editoriais, no nucleo de curadoria e nos casos `v4_real_001`, `v4_real_006` e `v4_real_007`.

Diagnostico central incorporado:

> O V4 ja consegue provar que percorreu um processo; ainda nao consegue provar que exerceu um bom julgamento editorial.

O problema nao e apenas keyword. A curadoria geral usa uma ontologia de politica/economia como gramatica universal, autocertifica a propria tese, oferece duas candidatas espantalho e converte briefing e instrucao em fatos travados.

## Decisao Sobre o Caso 007

O `v4_real_007` e pauta de `politica_cultural_plataformas`, nao analise de obra.

O material atual nao contem:

- texto regulatorio ou regra concreta;
- mecanismo documentado de recomendacao, destaque, dados ou remuneracao;
- dois exemplos verificaveis de obras ou criadores afetados;
- posicao atribuida de plataforma, produtores ou criadores.

Portanto, o resultado correto nao e uma tese cultural cosmeticamente melhor. E:

```text
estado_editorial=coleta_obrigatoria
collection_request.status=required
collection_request.required_before=shadow_redacao
teses_candidatas=[]
```

## Implementacao da Primeira Fatia

A mudanca foi feita em laboratorio lateral, preservando append-only os artefatos F7 e os hashes auditados de `curadoria_tese.py` e `v4_curadoria_tese_v1.json`.

Componentes novos na fonte viva `Projeto Cafezinho Agentes/root/v4_labs/`:

- taxonomia fechada de claims;
- resolvedor de fonte e de claim IDs atomicos;
- classificador de modo cultural;
- plugin cultural que nao gera tese sem evidencia minima;
- avaliador independente deterministico;
- runner versionado para a regressao 007.

Os campos `status` e `estado_editorial` ficam separados. `status=curadoria_dry_run` informa saude mecanica. `estado_editorial=coleta_obrigatoria` informa a disposicao do trabalho.

O avaliador deterministico nunca emite `editorial_ok_lab`. Quando o pacote tem claims e tres teses estruturalmente validas, o teto automatico e `rascunho_revisao_humana`. Qualidade semantica continua julgamento separado.

## Claim Types Ratificados Nesta Fatia

```text
fato_verificado
declaracao_atribuida
hipotese_editorial
juizo_interpretativo
juizo_estetico
instrucao_de_redacao
lacuna_de_apuracao
```

Somente `fato_verificado` e `declaracao_atribuida` com fonte resolvida podem virar fato travado. `juizo_estetico` pode sustentar tese apenas quando aponta para objeto e locator. Instrucao, hipotese e lacuna nunca contam como evidencia.

## Guards

- sem WordPress real;
- sem publicacao externa;
- sem promocao real;
- sem redacao shadow ou real quando a coleta e obrigatoria;
- sem sobrescrever `dados/curadoria/v4_real_007.curadoria.json` da F7;
- sem tratar keyword gate como aprovacao.

## Proxima Rodada

A matriz de seis casos permanece:

1. `v4_real_007` - politica cultural/plataformas;
2. serie de streaming - analise de objeto;
3. filme brasileiro de ficcao;
4. documentario;
5. livro;
6. obra popular de grande circulacao.

Os cinco novos casos so devem rodar depois da montagem de pacotes auditados. Nao preencher fixtures com fatos inventados apenas para completar a matriz.

## Fechamento Tecnico da Fundacao

Validacao local concluida em 2026-07-10 16:41 BRT:

```text
OK 114 contract tests
agentes_cli --strict: 11 agentes validos
fluxo_cli --execute: ok=true
multi_item_cli --execute: 3/3 casos legados F7 OK
cultura_lab_cli --execute: cultura_lab_ok, issues=[]
17/17 fontes congeladas com SHA256 identico antes/depois
```

O preflight retorna deliberadamente:

```text
status=promocao_pendente_de_cura
issue=collection_request_publicacao_real_resolvida
warning=gpt55_audit_recommended_before_promotion
wordpress_real=false
promocao_real_executada=false
```

Revisoes adversariais separadas examinaram codigo e artefatos. Nao restou hard issue estrutural. O aceite e restrito a fundacao e guards: o avaliador ainda nao faz julgamento semantico, todos os escores editoriais ficam `null`, e modos culturais alem de `politica_cultural_plataformas` e `analise_obra` ainda usam requisitos gerais.

O proximo passo nao e escrever uma tese para o 007. E coletar os quatro elementos faltantes, materializa-los como claims atomicos auditaveis e so entao reabrir a curadoria. Em paralelo, os outros cinco casos da matriz precisam de pacotes auditados reais.

## Pacote Fechado

```text
Projeto Cafezinho Agentes/root/v4_labs_fase8_curadoria_cultura_foundation_20260710.tar.gz
SHA256: 60198c4e8a07bdb9af5ede63380921b6aa012d5bde3fef6713fdf5ffba3d1825
Tamanho: 1072162 bytes
```

Validacao repetida a partir de extracao limpa em `/tmp`: `OK 114 contract tests`, 11 agentes validos, fluxo OK, lote F7 3/3, regressao cultural OK e preflight pendente apenas da coleta obrigatoria. Nao ha symlink, `__pycache__`, `.pyc`, `.env` ou padrao de segredo no pacote.

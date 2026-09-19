# Carta para Fable e GPT 5.5 Pro — auditoria da fatia fina V4

Miguel vai colar esta carta para os dois auditores finais.

## Pedido

Fable e GPT 5.5 Pro,

O Codex implementou a primeira fatia fina da curadoria de tese V4, seguindo os vereditos finais de voces. Pecamos uma auditoria objetiva antes de avancar para a proxima etapa.

O objetivo desta revisao nao e julgar a materia 261439 como produto final. O caso 261439 continua sendo laboratorio. O objetivo e verificar se a arquitetura tecnica agora obriga o V4 a fazer o que a rodada 4 decidiu:

```text
auditado -> curadoria -> producao
```

E se os gates impedem o retorno ao erro fundador:

```text
BUG-EDITORIAL-V4-001: texto correto, limpo, mas obvio, repetitivo e sem tese forte.
```

## O que foi implementado

```text
- contrato canonico enxuto: diretrizes/v4_curadoria_tese_v1.json
- memoria editorial por casos: diretrizes/v4_feedback_casos_editoriais_v1.json
- camada curadoria em v4_bancos_camadas_v1.json
- agente curador em v4_agentes_tecnicos_v1.json
- produtor lendo curadoria em vez de auditado cru
- publicador bloqueando payload sem curadoria_id
- imagem recebendo frame_visual da curadoria
- modulo dry-run v4_diretrizes/curadoria_tese.py
- CLI v4_diretrizes/curadoria_tese_cli.py
- experimento A/B dry-run v4_diretrizes/ab_experiment.py
- testes novos em v4_diretrizes/test_contracts.py
```

## Bloqueios de voces incorporados

Fable:

```text
- modo_experimento permite versao A sem curadoria_id somente em dry-run;
- nunca permite rascunho real/WordPress sem curadoria_id;
- leitura_corrente_timestamped nasce com fonte/proveniencia;
- frame_visual e campo obrigatorio para imagem.
```

GPT 5.5 Pro:

```text
- schema nao tem 14 campos discursivos;
- curadoria_id virou gate tecnico;
- produtor nao le auditado cru em editoria nobre;
- publicador exige curadoria_id;
- A/B 261439 entrou na Fase 1.
```

## Validacoes locais

```text
python3 -m json.tool ...                         # JSONs alterados validos
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts          # OK 47 contract tests
python3 -m v4_diretrizes.fluxo_cli               # planeja auditado -> curadoria -> producao -> auditado -> publicado
python3 -m v4_diretrizes.ab_experiment_cli --case 261439 --execute
```

## Arquivos para auditar no espelho

Diretorio:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/diretrizes/
```

Principais arquivos:

```text
v4_curadoria_tese_v1.json
v4_feedback_casos_editoriais_v1.json
v4_agentes_tecnicos_v1.json
v4_bancos_camadas_v1.json
v4_fluxo_dry_run_v1.json
v4_wordpress_publicador_v1.json
v4_imagem_destacada_v1.json
v4_real_001.curadoria.json
v4_real_001.variant_b.producao.json
ab_261439_curadoria_v4_fase_1.json
```

Forum de producao:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_producao_v4_curadoria_tese_20260709.md
```

Forum canonico de discussao:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_v4_curadoria_tese_editorial_20260708.md
```

## Perguntas de auditoria

1. O contrato de curadoria ficou enxuto o suficiente?
2. O gate de `curadoria_id` esta tecnicamente real ou ainda decorativo?
3. O `modo_experimento` resolve o paradoxo do A/B sem abrir brecha para publicacao real?
4. A normalizacao `fonte/source` da leitura corrente ficou aceitavel?
5. O publicador WordPress bloqueia o que deve bloquear?
6. O `frame_visual` esta no lugar certo para a imagem destacada?
7. O A/B 261439 esta adequado como smoke test, mesmo que a versao B ainda nao seja materia final?
8. O que voces bloqueariam antes do Codex seguir para Fase 2?

## Pedido de resposta

Respondam com:

```text
Veredito: aprovo / aprovo com ajustes / bloqueio
Bloqueios: lista objetiva
Ajustes recomendados: lista objetiva
Pode seguir para Fase 2? sim/nao
Escopo: o que voces leram e o que nao leram
```

Um ponto importante: a versao B do A/B e uma saida deterministica de smoke test. Ela prova o encadeamento tecnico e a mudanca de hierarquia editorial; nao deve ser confundida com texto final pronto para publicar.

## Atualizacao pos-probe Fable rodada 3

Fable encontrou uma brecha: `manual_editor` passava em modo real apesar de o contrato exigir fonte nao-manual para publicacao real.

Correcao aplicada:

```text
validate_gate agora bloqueia modo real/draft real quando leitura_corrente_timestamped.fonte = manual_editor.
validate_gate tambem bloqueia modo real/draft real se a leitura corrente nao tiver fonte.
Novo teste: test_publicacao_real_bloqueia_fonte_manual.
Resultado atual: OK 52 contract tests.

Atualizacao de reconciliacao:

```text
Foi adicionado test_espelho_diretrizes_reconciliado_com_fonte_viva.
O teste compara os contratos centrais em diretrizes/ contra Cerebro/Foruns/diretrizes/.
Se o espelho estiver velho, a suite falha.
Manifesto: Cerebro/Foruns/diretrizes/MANIFESTO_RECONCILIACAO_ESPELHO_V4_20260709.md
```

Atualizacao Fase 2:

```text
Foi formalizada a semantica de collection_request:
recommended nao bloqueia shadow_redacao;
recommended bloqueia no estagio indicado por required_before e nas etapas posteriores.

No caso 261439:
collection_request.status=recommended
required_before=redator_real_llm
Logo: nao bloqueia shadow, mas bloqueia chamada externa de redator real antes de coleta USTR/Federal Register.

texto_shadow e placeholder de pipeline, nao amostra final de escrita.
Mesmo assim, removemos meta-linguagem como "segundo a curadoria" e "promessa editorial".
```
```

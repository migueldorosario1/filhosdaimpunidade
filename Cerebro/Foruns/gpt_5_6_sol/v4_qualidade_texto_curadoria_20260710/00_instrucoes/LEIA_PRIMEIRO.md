# Dossie V4 Para GPT 5.6 Sol

Data: 2026-07-10

Objetivo: preparar um conjunto autocontido de documentos do V4 para uma leitura editorial forte pelo GPT 5.6 no ChatGPT normal.

Foco principal:

- qualidade do texto;
- curadoria forte;
- tese editorial;
- linguagem por editoria;
- revisao humana e criterio de aceitacao;
- evolucao da curadoria cultural.

Fora de escopo:

- autorizacao de publicacao real;
- promocao para `root/v4`;
- chamadas reais ao WordPress;
- relaxamento dos gates de seguranca.

## Estado Resumido

O V4 esta aprovado para continuidade em laboratorio, nao para producao real.

As fases mecanicas principais foram auditadas. O problema editorial mais importante agora nao e seguranca mecanica: e qualidade da curadoria e do texto.

O achado decisivo veio na Fase 7:

- a curadoria congelada rodou em novas editorias;
- mecanicamente funcionou;
- editorialmente degradou fora das familias calibradas;
- o caso `v4_real_007`, de cultura/streaming, recebeu tese de template industrial/IBGE;
- o batch nao quebrou, mas o gate F7.1 passou a marcar isso como warning e revisao humana obrigatoria.

Miguel ratificou a politica interina:

teses fora das familias calibradas sao rascunho com revisao humana obrigatoria ate existir curadoria propria por editoria ou gate forte de coerencia.

## Estrutura Do Dossie

`01_foruns_essenciais`

Contexto editorial e historico de decisoes. Ler primeiro:

1. `forum_principios_fundamentais_novo_v4_20260708.md`
2. `forum_v4_curadoria_tese_editorial_20260708.md`
3. `forum_producao_v4_curadoria_tese_20260709.md`
4. `forum_v4_linguagem_analise_objetos_culturais_20260710.md`
5. `forum_v4_fase7_multi_item_lab_20260710.md`
6. `canal_trindade.md` apenas para contexto cronologico amplo.

`02_auditorias`

Cartas externas e pareceres. Ler especialmente:

1. `carta_fable_auditoria_fase6_multicase_20260710.md`
2. `carta_fable_auditoria_fase7_multi_item_20260710.md`
3. `carta_fable_adendo_final_fase5_typefix_20260710.md`

`03_contratos_editoriais`

Contratos e linguagem formal do sistema. Ler especialmente:

1. `v4_nucleo_editorial_comum_v1.md`
2. `v4_curadoria_tese_v1.json`
3. `v4_editoria_coerencia_v1.json`
4. `v4_cultura_v1.md`
5. `v4_ciencia_tecnologia_ia_v1.md`
6. `v4_internacional_v1.md`
7. `v4_politica_economia_v1.md`
8. `v4_redator_real_v1.json`
9. `v4_redator_shadow_v1.json`
10. `v4_revisao_v1.json`
11. `v4_fact_check_v1.json`

`04_codigo_contexto`

Codigo relevante para entender como as decisoes editoriais viraram mecanica. Ler so quando necessario:

- `curadoria_tese.py`
- `coerencia_editorial.py`
- `redator_real.py`
- `redator_shadow.py`
- `revisao.py`
- `fact_check.py`
- `multi_item.py`

`05_amostras_reais`

Amostras dos casos `v4_real_001` a `v4_real_007`: pauta auditada, curadoria, producao, revisao e fact-check quando disponiveis.

Prioridade de leitura:

1. `v4_real_007.*` - caso canonico de falha cultural.
2. `v4_real_006.*` - IA/data centers, tambem afetado por template industrial indevido.
3. `v4_real_001.*` - caso mais rico, com redator real/shadow e decisao editorial USTR.
4. `v4_real_002` a `v4_real_005` - comparacao de padrao.

`06_relatorios_lab`

Relatorios de lote e preflight. Ler para confirmar o estado mecanico, nao para julgar estilo.

`07_contexto_retomada`

Notas de fase e README do lab.

## Pergunta Central Para GPT 5.6

O V4 ja tem boa disciplina mecanica. O que falta para que a curadoria e o texto tenham nivel editorial alto?

Responder com foco em:

- tese mais forte;
- pauta melhor recortada;
- texto menos generico;
- abertura mais jornalistica;
- estrutura argumentativa;
- linguagem por editoria;
- curadoria cultural propria;
- limites entre fato verificavel e juizo interpretativo;
- criterios objetivos de aceitacao antes de nova rodada.

## Cuidado De Leitura

Nao tratar warning de laboratorio como bloqueio de seguranca real.

Nao tratar aprovacao mecanica como aprovacao editorial.

Nao propor publicacao real. A tarefa e melhorar curadoria e texto em laboratorio.

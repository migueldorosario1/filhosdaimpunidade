# Memória técnica — Títulos genéricos (sem nome próprio desconhecido) · 17/09/2026

> Log técnico completo. Par de tema duplo: `Foruns/forum_titulos_genericos_20260917.md`.

## Arquivos tocados

### WordPress (servidor 190.89.239.65, alias `cafezinho-wp`, path /var/www/ocafezinho)

- Post 271620: `wp post update --post_title="Fogo cerca orangotangos em plantação de óleo de palma na Indonésia" --post_name=fogo-cerca-orangotangos-em-plantacao-de-oleo-de-palma-na-indonesia` com `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` (trava editorial de post publicado). WP setou `_wp_old_slug` sozinho ("Value passed ... is unchanged" = já tinha registrado o slug antigo no update).
- Post 271552: idem → "Cinco pacientes em SP testam medicamento brasileiro para lesão medular" / `cinco-pacientes-em-sp-testam-medicamento-brasileiro-para-lesao-medular`.
- Cache: `wp eval "rocket_clean_post(271620); rocket_clean_post(271552);"` (warning PHP de constante inofensivo no echo).

### NYC (alias `nyc`)

- `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py` — função `_prompt()` (~linha 188): inserida régua
  "No título, proibidos: sigla que o leitor comum não reconheça ... nome próprio desconhecido ... entra o genérico
  (exemplos 'empresa de óleo de palma', 'medicamento brasileiro para lesão medular') ... nome específico fica no corpo".
  Backup `.bak_pre_titulo_generico_20260917`. Commit `c6dfd51` (repo v4_labs, sem remote; amend documentou que o
  commit englobou também working tree pendente da CL — ZM_HTML_ESCAPE_20260909/ZM_PROMPT5_20260910 — preservado, nada perdido).
- `/root/agente_auditor_titulos_gpt.py` — `_auditor_system_prompt()` (linha ~599): após "fatos do lide.", inserida
  instrução de CORRIGIR também título com sigla/nome próprio irreconhecível (gera genérico com fatos do lide;
  Coca-Cola/McDonald's/Lula/Bolsonaro podem ficar). Backup `.bak_pre_titulo_generico_20260917`. Arquivo FORA de repo
  git (fica só backup + registro aqui).
- Sintaxe conferida: `python3 -m py_compile` OK nos dois.

### Cérebro local

- `Estilo/MANUAL_AGENTES_AUTONOMOS_CAFEZINHO_COMPLETO_20260914.md` — regra 8.7 estendida (empresa, produto, substância,
  termo estrangeiro; marca ultra conhecida/fama nacional é exceção; casos-escola com data).
- `Estilo/BLOCO_PRONTO_REGRA_TITULO_EMU6.md` — item 5 do bolo pronto verbatim estendido com a régua + casos.
- `Foruns/ponte_laura_completa/de_dell.md` — entrada `REGRA-TITULO-GENERICOS-20260917` para CL/AGY/R2 estenderem
  a checagem do `_cafezinho_txt_check` ("titulo sem sigla" → "sem sigla E sem nome próprio desconhecido").

## Descobertas de cadeia (comandos úteis)

- Origem dos posts: `wp post meta list <ID> | grep -Ei "agente|origem"` → `_agente_origem=tampao_v1`, `_cafezinho_origem`
  (via REST, user 5470, ts de criação 03:13 e 09:11).
- Trilha do auditor: `/root/agent_data/auditor_titulos_gpt/auditor_titulos_gpt_AAAA-MM-DD.jsonl` (grep post_id) — hoje os dois
  posts apareceram com `acao=ok` do modo poll (conservador: só contradição/placeholder).
- Advisor preventivo (9 regras, regra 9 = exatamente a régua) mora em `agente_auditor_titulos_gpt.py --modo advisor`
  mas NENHUM cron/script o chama, e `advisor_author_id` default 5786 ≠ 5470 (autor da esteira) — nunca viu esses rascunhos.
- Esteira viva: `crontab -l` do NYC → `v4_labs` módulo `codigo.v41_ciclo` (saúde 25 9,19; ciencia 45 */2; geo 55 *; etc.).
  O redator é `codigo/v4_vertical_redactor_runtime.py` (função `_generate` percorre pool de modelos).
- Redirect de slug: curl com `?nocache=` (sem query a borda servia 200 do HTML antigo) → 301 `location` novo, `x-redirect-by: WordPress`.

## Testes/provas

- `curl -s URL-nova | grep <title>` → títulos novos no ar (200) nos dois posts.
- `curl -sI URL-antiga?nocache=` → 301 para URL nova nos dois (links já distribuídos não quebram).
- `python3 -m py_compile` OK nos 2 arquivos editados no NYC.
- Commit `c6dfd51` + amend no repo `/root/v4_labs` (auditor `git show --stat`: só 1 arquivo).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- ACONTECEU: 2 títulos corrigidos no ar (301 preservado) + régua plantada em 4 pontos da cadeia (redator V4.1,
  auditor pós-publicação, manual 8.7, bloco EMU) + aviso na ponte para a régua de revisão da CL.
- FALTA: observar o auditor nas próximas rodadas (deve passar a corrigir sozinho títulos com nome desconhecido);
  advisor preventivo segue fora do fluxo (ligar = decisão do Miguel).
- PRECISO DE VOCÊ: nada urgente; "vai" se quiser o advisor preventivo no fluxo V4.1.

— ZCode/GLM-5.3 · 17/09/2026 ~11:0x BRT

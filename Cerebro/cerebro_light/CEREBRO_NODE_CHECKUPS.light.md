# CEREBRO_NODE_CHECKUPS — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_CHECKUPS.md` (26KB) — 21 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_CHECKUPS

Registro canônico dos checkups operacionais do ecossistema Cafezinho/Trindade.

---

## CHECKUP-001 — Pausa total do ecossistema Tencent para auditoria

**Data:** 2026-06-01  
**Janela:** 21:12-21:48 BRT  
**Executor:** Codex  
**Motivo:** noite de check-up; Miguel identificou deterioração editorial/operacional e pediu pausar tudo para investigação e religamento gradual. Claude prepara relatório paralelo do sistema.

### Contexto

Incidentes que motivaram a pausa:

- Vazamento de JavaScript/newsletter no post BRB/Master `254854`.
- Repetição/cluster BRB/Master e fragilidade do dedupe.
- Suspeita de deterioração nas últimas horas.
- Descoberta de publicadores paralelos e coletores ainda rodando mesmo após pausa inicial do Maestro.
- Necessidade de religar o ecossistema por etapas, com validação em cada etapa.

Fórum de referência:

- `Foruns/forum_investigacao_deterioracao_publicacao_20260601.md`

Canal:

- `Foruns/canal_trindade.md`, entradas Codex de 2026-06-01 21:15, 21:28, 21:35 e 21:48 BRT.

### Fase 1 — Pausa emergencial parcial

**Backup remoto:**

- `/root/crontab_backup_pre_pausa_emergencial_20260601_211249_codex.txt`

**Linhas comentadas no crontab root:**

- `maestro_editorial.py`
- `agente_analytics_v9.py`
- `agente_crime.py`
- `coletor_eleicoes.py`
- `agente_eleicoes_produtor.py`
- `run_analise.sh`

**Processo encerrado:**

- `agente_master_trends.py`

### Fase 2 — Pausa de publicadores paralelos e coletores correspondentes

**Backup remoto:**

- `/root/crontab_backup_pre_pausa_publicadores_paralelos_20260601_213020_codex.txt`

**Marcador usado no crontab:**

- `PAUSADO_CODEX_20260601_PUBLICADORES_PARALELOS`


---

## ⏩ 16 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_CHECKUPS.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### [2026-06-02 03:31 BRT] CHECKUP-001 — helper central external_blocks

Miguel autorizou a faxina central/choke point para impedir que blocos operacionais contaminem `post_content`.

Codex executou localmente:

- Criou `root/util_blocos_externos.py`.
- Refatorou `root/motor_publicador.py` para chamar o helper.
- Não tocou rotas paralelas.
- Não fez deploy.
- Não religou robôs.

Backups:

- `root/motor_publicador.py.bak_pre_util_blocos_externos_20260602_032301_codex`

Validação:

- `python3 -m py_compile root/util_blocos_externos.py root/motor_publicador.py` passou.
- Teste unitário manual confirmou:
  - flag desligada preserva legado;
  - flag ligada remove figcaption/interlink/Mailchimp e monta metas.
- Smoke REST criou rascunho `255113` com HTTP `201`, `status=draft`, corpo limpo e meta

> *(... 368 chars omitidos — ler original)*

---

### [2026-06-02 03:31 BRT] CHECKUP-001 — bloqueador regex Mailchimp fechado

Claude revisou §12 o helper `util_blocos_externos.py` e aprovou a arquitetura, mas apontou um bloqueador: o regex anterior removia parcialmente a `CAIXA_NEWSLETTER_AJAX` real e podia deixar `<script>mailchimpCallback...</script>` no corpo em rotas paralelas.

Codex corrigiu localmente o pattern Mailchimp para casar do `<hr>`/`<div id="mc_embed_signup">` até o script com `mailchimpCallback`.

Validação:

- `python3 -m py_compile root/util_blocos_externos.py root/motor_publicador.py` passou.
- Teste contra a constante literal `CAIXA_NEWSLETTER_AJAX` do motor deixou apenas `<p>Texto editorial.</p><p>Fim.</p>`.
- Confirmado ausente: `mc_embed_signup`, `cafezinho-mc-form-ajax`, `mailchimpCallback`, `<script`, `<hr>`.
-

> *(... 149 chars omitidos — ler original)*

---

### [2026-06-02 04:09 BRT] CHECKUP-001 — unificação de papéis e registro Codex

Miguel definiu a governança do próximo ciclo do checkup: **Claude distribui os sprints**; Codex fica como observador/jornalista técnico e auditor quando chamado. Registro de memória integrado feito no canal e memória Codex.

Estado canônico preservado:

- Sistema/Tencent segue pausado.
- `external_blocks_v1` etapa 1 está localmente aprovada por Claude §12.
- Snippet WPCode está ativo manualmente, renderizando `Leia também` + newsletter fora do `post_content`; legenda fica com Media Library/tema.
- Nenhuma rota paralela foi adaptada.
- Nenhum deploy foi feito.
- Nenhum robô foi religado.

Frente nova aberta: Qwen criou `Foruns/forum_problemas_estruturais_lote2.md` para HTML escapado, categorias erradas/genéricas

> *(... 347 chars omitidos — ler original)*

---

### [2026-06-02 05:58 BRT] CHECKUP-001 — fórum conflito prompt redator observado

Codex observou canal, inboxes e `Foruns/forum_conflito_prompt_redator_20260602.md` sem executar código. Canal foi limpo/compactado; histórico anterior preservado em `Foruns/backups_limpeza_20260602_054149/canal_trindade.md`.

Novo foco do Claude: conflito de prompt no redator, apontado como causa-raiz de parágrafos de 1 frase (>95% dos posts) e títulos longos (60%). Kimi aceitou prototipar normalizador determinístico de parágrafo offline; Qwen propôs specs para validador de título e guard de categoria; DeepSeek foi chamado para parecer externo; Codex tem missão pendente de revisão §12 do motor.

Nota de risco: a proposta de Qwen para categorias inclui `keyword_map`; isso deve ser tratado como protótipo/hipóte

> *(... 151 chars omitidos — ler original)*

---

### [2026-06-02 06:06 BRT] CHECKUP-001 — virada LLM-first no sprint do redator

Claude registrou virada de rota por ordem do Miguel no `Foruns/forum_conflito_prompt_redator_20260602.md`: output editorial visível ao leitor deve ser **LLM-first**. Determinístico fica restrito a log, métrica, trigger e organização interna.

Impacto:

- `normalizador_paragrafo.py` prototipado por Kimi deve ser tratado como diagnóstico/métrica offline, não como reescrita viva.
- Validador determinístico de título e guard de categoria por `keyword_map` propostos por Qwen ficam descartados para output editorial.
- Cura viva passa a ser: regra C1 no prompt do redator, revisão/reescrita de título por LLM de luxo chinês, re-prompt LLM para categoria "Redação" genérica, desconflito da auditoria e consolidação futura 

> *(... 4377 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_CHECKUPS.md`](./CEREBRO_NODE_CHECKUPS.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`
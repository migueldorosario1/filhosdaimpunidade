---
name: project-loop-sentinela-cron-dia-noite-20260721
description: "Loop Sentinela roda em cron automático: DIA (06-21h BRT) a cada 30min, NOITE (22-05h BRT) a cada 1h. Manifesto diário agregado 23:55 BRT em Cerebro/Foruns/sentinela/manifesto_YYYY_MM_DD.md com índice mensal. Regra: nunca reportar backlog velho no relatório. Todo bug encontrado deve ser anotado em Outros/manual_de_bugs.md com sintoma+causa+fix+lição."
metadata:
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-21 17:20 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Estado do Loop Sentinela — 21/07/2026 17:20 BRT

Antes da autonomia via cron, Loop Sentinela rodava via skill `/loop` do Claude Code (sessão-only, expira 7 dias). Miguel autorizou 2026-07-21 17:00 BRT operação 24/7 permanente.

### Cron ativo (usuário migueldorosario)

```cron
# Dia (06:00-21:59 BRT): a cada 30min
*/30 6-21 * * * /home/migueldorosario/ferramentas/sentinela/sentinela_cron.sh
# Noite (22:00-05:59 BRT): a cada 1h
0 22-23,0-5 * * * /home/migueldorosario/ferramentas/sentinela/sentinela_cron.sh
# Manifesto diário agregado 23:55 BRT
55 23 * * * /home/migueldorosario/.pyenv/versions/3.10.13/bin/python3 /home/migueldorosario/ferramentas/sentinela/agregar_manifesto_diario.py >> /home/migueldorosario/ferramentas/sentinela/logs/manifesto_diario.log 2>&1
```

**Total:** ~40 execuções/dia (32 de dia + 8 de noite) + 1 manifesto agregado.

Backup crontab pré-mudança: `/tmp/crontab_backup_pre_sentinela_20260721_171350.txt` (58 linhas).

### Wrapper de cron

`/home/migueldorosario/ferramentas/sentinela/sentinela_cron.sh` — chmod +x. Loga em `~/ferramentas/sentinela/logs/cron.log` com timestamp. Sentinela lê chaves internamente de `Projeto Cafezinho Agentes/root/.env.unificado` (função `load_env`).

### Manifesto diário

Script: `~/ferramentas/sentinela/agregar_manifesto_diario.py`
- Lê `~/ferramentas/sentinela/logs/ciclos.jsonl`
- Agrega TODOS os ciclos do dia BRT
- Gera `Cerebro/Foruns/sentinela/manifesto_YYYY_MM_DD.md` com: total publish/grafia/edit/propostas/alertas, distribuição severidade, tabela por hora com links, resumos executivos últimos 6 ciclos, seção bugs
- Atualiza `Cerebro/Foruns/sentinela/indice_sentinela_2026-07.md` com uma linha por dia
- Uso manual: `python3 agregar_manifesto_diario.py [YYYY-MM-DD]` (default: hoje)

**Pendente:** fórum semanal + fórum mensal (agregam manifestos diários) — Miguel mencionou mas não pediu urgente. Fazer quando 7 dias de manifesto diário acumularem.

## Regras de conteúdo do relatório de ciclo

Miguel 2026-07-21 17:00 BRT: *"não fica botando coisa antiga na fila não, vai confundir a nossa cabeça"*.

- Sentinela **NÃO reporta** contagens de backlog velho ("91 drafts na fila", "45 rascunhos pendentes desde 15/07")
- Sentinela **NÃO lista** IDs de drafts rejeitados por idade (>cap_h)
- Reporta apenas: drafts elegíveis (dentro do cap + com featured_media), decisões tomadas (publicar/rejeitar por outros motivos), ações aplicadas, alertas
- Prompt atualizado em `~/ferramentas/sentinela/config/prompts.md` seção "📵 NUNCA REPORTAR BACKLOG DE RASCUNHOS ANTIGOS"

## Manual de bugs — protocolo obrigatório

Miguel 2026-07-21 17:00 BRT: *"anota e indexa... a gente tem que acumular conhecimento... qualquer bug, qualquer erro tem que anotar. Você anota o erro, encontrei o erro tal, deu problema tal, e a solução foi essa"*.

**Manual canônico:** `Outros/manual_de_bugs.md` (existia desde 18/04, 1088 linhas em 21/07 após adição de bugs #18/#19).

**Padrão de entrada** (segue formato já estabelecido no manual):
```markdown
## N. Título curto do bug (YYYY-MM-DD)

**Descoberto:** YYYY-MM-DD HH:MM BRT
**Arquivo:** path/relativo/ou/absoluto
**Gravidade:** baixa | média | alta | crítica
**Status:** 🔴 aberto | 🟡 em investigação | ✅ RESOLVIDO YYYY-MM-DD

### Sintoma
O que aconteceu, o que o usuário/agente viu.

### Causa raiz
Por que aconteceu. Trecho de código problemático se aplicável.

### Fix aplicado
O que foi mudado, arquivo:linha, código novo.

### Lição arquitetural
O que aprendemos, como evitar classe inteira de bugs semelhantes.

### Referências
Fóruns, memórias, PRs, sessões relacionadas.
```

**Regra:** ao encontrar bug novo → adicionar no manual. Ao resolver bug antigo → atualizar `Status`. Bug recorrente → adicionar nota na entrada existente com data + causa.

## Bugs recentes adicionados hoje

- **#18** V4 gera drafts SEM featured_media (bug estrutural pendente, delegado ao Codex 2026-07-21 13:45)
- **#19** DeepSeek do Sentinela ignora cap dinâmico do código (resolvido 21/07 16:55 alinhando prompt+código)

## Relacionadas

- [[feedback-nunca-churn-publish-draft-seo]] — não rebaixar publish→draft
- [[project-no-home-score-policy-v1-20260721]] — home/no-home nasce no worker NYC
- [[feedback-diretrizes-editoriais-21jul]] — R1-R4 editoriais
- [[feedback-sentinela-nunca-publicar-rascunhos-antigos]] — cap 2h padrão
- [[feedback-indexar-bugs-e-curas-no-cerebro-inegociavel]] — regra original de indexação
- [[manual-de-bugs-ler-primeiro]] — protocolo consulta prévia

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-21 17:20 BRT.

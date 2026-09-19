# Cartinha ao Kimi K3 Desktop — Enriquecer coleta Sentinela — 2026-07-26 15:25 BRT

**Autor:** Claude Code (`claude-opus-4-7`), orquestrador local
**Destinatário:** Kimi K3 **Desktop** (Moonshot, versão browser/desktop app — Miguel usando hoje; NÃO confundir com Kimi CLI que está aposentado por enquanto)
**Assunto:** Novo sprint — enriquecer `coletar_estado()` da Sentinela pra evitar falso positivo DeepSeek
**Fórum canônico:** [`forum_kimi_webverify_e_brave_desativado_20260726.md`](../forum_kimi_webverify_e_brave_desativado_20260726.md) §17

---

Kimi,

Miguel autorizou 15:25 BRT novo sprint estrutural — resolver falso positivo do DeepSeek no ciclo `20260726_1509` (alertou "sem drafts V4 recentes desde 23/07, workers inativos" quando na realidade posts foram publicados 15:08 / 14:01 / 13:12 / 12:01 / 10:01 hoje). Causa raiz: **coleta pobre** — DeepSeek analisa sem ter no payload os fatos que refutariam sua hipótese.

Miguel: *"o DeepSeek não pode fazer análise sem antes ter informação... vamos começar de leve para a gente não resolver o mundo inteiro... ele precisa de um básico de saber que o sistema está funcionando... você já vai ter que fazer um relatório básico para ele e aí entregar para ele, é uma memória fresca, aí ele analisa"*.

## O que enriquecer no `coletar_estado()` de `sentinela_ciclo.py`

Adicionar 4 novos blocos no payload que vai pro DeepSeek analisador:

### 1. `publicados_recentes` — últimos 5 posts publicados
Via WP API: `/wp-json/wp/v2/posts?per_page=5&_fields=id,date,modified,title,author&orderby=date&order=desc`
Retornar lista `[{id, date_brt, minutes_ago, title}, ...]`

### 2. `ritmo_publicacao_6h` — posts/hora nas últimas 6h
Via WP API com `after=<now-6h>&per_page=100&_fields=id,date`
Retornar `{posts_total, taxa_por_hora, taxa_esperada, delta_pct}`

### 3. `ultimo_draft_criado` — timestamp mais recente na tabela de drafts (não só da fila elegível)
Via WP API `/wp-json/wp/v2/posts?status=draft&per_page=1&orderby=date&order=desc&_fields=id,date`
Retornar `{id, date_brt, minutes_ago}` — desambigua "fila velha por bug" vs "fila velha porque publica rápido"

### 4. `ultima_exec_worker_v4` — última execução do worker V4 no cron log
Via `tail -n 200` no `agent_data/v4/cron_v4.log` + regex por padrão de início de ciclo
Retornar `{timestamp_brt, minutes_ago, site, status}` — confirma que cron está rodando

## Onde encaixar no prompt DeepSeek

O prompt Sentinela em `~/ferramentas/sentinela/config/prompts.md` já tem seção do payload de estado. Adicionar sub-seção "**📊 Sinais de saúde do pipeline V4**" listando os 4 blocos acima com instrução explícita: *"antes de alertar 'workers inativos', 'sem drafts recentes' ou similar, consultar esta seção — se ritmo 24h ≥ 12 posts/dia OU ultimo_worker_run < 2h atrás, NÃO alertar mesmo se fila estiver com drafts velhos."*

## Protocolo AUTOCURA obrigatório (mesmos 12 passos)

- Backup `sentinela_ciclo.py.bak_pre_kimi_coleta_enriquecida_20260726_HHMM` + SHA-256
- Backup `prompts.md.bak_pre_kimi_coleta_enriquecida_20260726_HHMM` + SHA-256
- Smoke isolado: rodar `coletar_estado()` standalone antes de conectar ao ciclo real
- Controle off-topic: rodar 1 ciclo real e conferir que os 4 blocos aparecem no fórum output sem quebrar existentes
- `py_compile` OK
- SHA-256 pós-patch registrado
- Monitorar produção pós-patch: **próximos 3 ciclos** — confirmar que DeepSeek para de gerar alertas "sem drafts recentes" quando sistema está saudável
- Rollback documentado
- Registro 3 camadas: JSONL bugs do dia + `CEREBRO_NODE_BUGS_SOLUCOES.md` + `manual_de_bugs.md` novo padrão #39 "LLM analisador com pouca informação gera FP"
- Atualizar `CEREBRO_NODE_ATUALIZACOES.md`
- Linha `[KIMI-COLETA-ENRIQUECIDA-OK]` no canal
- Manifesto em nova seção **§17** do mesmo fórum `forum_kimi_webverify_e_brave_desativado_20260726.md` (mantém tudo neste fórum, evita fragmentação)

## Meta-lição pra registrar no manual

**Padrão estrutural detectado 26/07:** LLM analisador com payload pobre gera falso positivo. Sinal a monitorar: qualquer alerta com verbo especulativo ("sugere", "aparenta", "possivelmente") = candidato a coleta insuficiente. Fix estrutural = enriquecer payload antes de chamar analisador, não trocar analisador.

## Deploy target

Local primeiro (`~/ferramentas/sentinela/`). Após 3 ciclos validando, propagar NYC (`/root/`) via SSH com backup+rollback documentado (mesmo protocolo de hoje 14:26 BRT).

## Sinaliza recebimento

Linha no `canal_trindade.md`:
```
[KIMI-COLETA-ENRIQUECIDA-LIDO] 2026-07-26 HH:MM BRT — Kimi K3 → Claude+Miguel — pedido lido, ETA manifesto §17: HH:MM
```

Trabalho bom.

— Claude Code, `claude-opus-4-7`, orquestrador local

---
name: feedback-ciclo-tematicos-3h-manual-via-loop
description: "A cada ~6 loops Sentinela (~3h), substituir 1 ciclo Cafezinho por ciclo Temáticos vigiando 7 sites (Rio Carta+Mapa Rio, Global South, Discover Brazil, Aiatolah, Ceará Digital, Mundo Trilhos, Rail Post). Verificar: atualização, agentes, imagens, posts. Fix: tentar sozinha primeiro, fallback Kimi K3. Manual via /loop, sem cron novo."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-24 10:55 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

## Regra

Miguel 2026-07-24 10:50 BRT: Loop Sentinela cron atual (30min dia / 1h noite) vigia Cafezinho. **Nova rotina:** a cada ~6 loops (~3h), substituir 1 ciclo Cafezinho por ciclo Temáticos vigiando os 7 sites satélites do ecossistema. Sem cron novo — manual, sob comando `/loop` do Miguel, detecto quando é hora de rodar temáticos.

## Sites vigiados (7)

| # | Site | Domínio | Repo local V4 |
|---|---|---|---|
| 1a | Rio Carta | (GitHub→Vercel + DigitalOcean 159.89.185.209 `riocarta_admin.service`) | `sites-v4/riocarta` |
| 1b | Mapa Rio | (a validar — provavelmente `mapario.vercel.app` ou `.news`) | `sites-v4/mapario` |
| 2 | Global South News | `globalsouth.news` (validação DNS pendente) | `sites-v4/globalsouth` |
| 3 | Discover Brazil | `discoverbrazil.news` | `sites-v4/discoverbrazil` |
| 4 | Aiatolah | `aiatola.vercel.app` / `aiatolah.com` (futuro) | `sites-v4/aiatolah` |
| 5 | Ceará Digital | `cearadigital.news` (pré-lançamento, DNS pendente) | `sites-v4/ceara` |
| 6 | Mundo Trilhos | `mundotrilhos.com` | `sites-v4/mundotrilhos` |
| 7 | Rail Post | `railpost.news` | `sites-v4/railpost` |

Cérebros de referência:
- `Cerebro/CEREBRO_INDEX_SATELITES.md` (índice mestre)
- `Cerebro/CEREBRO_INDEX_RIOCARTA.md` (canônico Rio Carta)
- `Cerebro/CEREBRO_INDEX_AIATOLAH.md` (canônico Aiatolah)

## O que verificar cada ciclo (~15-20min)

1. **HTTP domínio:** `curl -sI` cada URL — 200 OK esperado. 4xx/5xx = alerta
2. **Última atualização:** git log do repo local (últimos commits ao branch main); Vercel deploy status se acessível
3. **Agentes vivos:** para sites com worker próprio (Rio Carta admin service; outros TBD) — checar heartbeat/log
4. **Posts sem imagem:** se aplicável ao site — mesma verificação estilo `v4_pipeline_imagem` do Cafezinho
5. **Estado geral:** front carregando, feed populado, sem erro 500 na home

## Padrão de correção

**Tentar sozinha primeiro** (Miguel: *"tenta você primeiro, você é Clodio. Se você realmente não conseguir, você tenta o Kimi"*):
- Consultar `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` + manual de bugs + índices dos sites
- Se bug conhecido → aplicar solução validada
- Se bug novo → investigar + aplicar fix pequeno + registrar 3 camadas (JSONL + manual + memória)

**Fallback Kimi K3** (via fórum `Cerebro/Foruns/forum_kimi_*_YYYYMMDD.md`):
- Só se: (a) bug estrutural exige análise profunda, (b) precisa mexer em arquivo grande, (c) requer conhecimento do repo específico que não conheço bem, (d) minha investigação estagnou >15min sem hipótese sólida
- Padrão de fórum: contexto + sintoma + causa suspeita + protocolos de segurança (nunca `--dangerously-skip-permissions`, nunca churn publish→draft) + resposta obrigatória no fórum+chat

## Cadência (manual via /loop)

Miguel manda `/loop` a cada 30min normalmente. Contador implícito: **a cada 6 loops de Cafezinho, o 7º é Temáticos** (aproximadamente 3h). Ou detecto pela hora: se hora atual for múltipla de 3 (ex.: 12:00, 15:00, 18:00) e for o ciclo do início da hora (não o `:30`), rodar temáticos em vez de Cafezinho.

**Regra prática:** verificar `~/ferramentas/sentinela/logs/ciclos.jsonl` — se o último "ciclo temáticos" registrado for há >2.5h, rodar temáticos ao invés de Cafezinho no próximo `/loop`.

## Log

Registrar cada ciclo temáticos em `Cerebro/monitoramento_horario/tematicos/tematicos_YYYY-MM-DD.jsonl` (criar dir se não existir) — schema: `{ts_brt, site, http_status, last_commit_git, ultima_atualizacao_detectada, problemas_encontrados, correcoes_aplicadas, escalado_kimi}`. Um registro por site, um lote por ciclo.

## Relacionadas

- [[project-loop-sentinela-cron-dia-noite-20260721]] — infra base Sentinela Cafezinho
- [[feedback-protocolo-memoria-bugs-ler-antes-agir]] — protocolo de correção 3 camadas
- [[project-kimi-bugs-upstream-v4-fechados-20260724]] — precedente Kimi resolvendo bugs upstream

## Assinatura

Regra estabelecida por Miguel 2026-07-24 10:50 BRT. Registrada por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`.

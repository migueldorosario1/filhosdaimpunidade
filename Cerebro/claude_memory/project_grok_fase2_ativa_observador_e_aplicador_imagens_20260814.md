---
name: project-grok-fase2-ativa-observador-e-aplicador-imagens-20260814
description: "Grok passou da Fase 1 (observador passivo) pra Fase 2+ dupla capacidade — (1) ping bugs críticos em fila_para_claude, (2) aplicação supervisionada de imagens Wikimedia CC em paralelo à ponte ZCode. Aprovado por Kimi 14/08 12:13 após exercício supervisionado nota 10/10/7"
metadata: 
  node_type: memory
  type: project
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Grok agora tem 2 papéis operacionais no ecossistema Cafezinho (a partir de 14/08/2026 12:13 BRT):

## 1. Observador ativo — ping em bugs críticos

Cron dele `*/30`. Quando detecta bug crítico, faz APPEND em `fila_para_claude.md` com padrão:
```
## [GROK→CLAUDE-BUG-<TIPO>-<POST_ID>-<YYYYMMDD-HHMM>]
status: ABERTO
post_id: XXX
bug: sem_featured_media / metalinguagem / titulo_>80c / content_end / html_escapado / dedup_lead
severidade: alta/média
sugestao: <ação>
```

Critérios pra ping (NÃO só anotar no JSONL):
- `sem_featured_media` em post agendado
- `metalinguagem_ia_vazada` (bug #1)
- `titulo_>80c` que Claude passou
- `content_end_marker` residual pós-agendamento
- `html_escapado`
- `dedup_lead` no repetidor publicado sem correção
- Bug factual óbvio (nome/número/cargo)

## 2. Aplicador de imagens supervisionado

Aprovado por Kimi 14/08 12:13 após exercício com nota 10/10/7 em 3 propostas (STF plenário/Palácio Fazenda RJ/CIA Langley — a última perdeu 3 pontos por dimensão fora do reservado, método correto). Regras:

- **Livro de reservas:** "quem vê primeiro, faz" — sem conflito com automação `*/30` da Kimi
- **Log assinado:** todo apply do Grok fica no `ponte_imagens_v4_LOG.md` com assinatura dele
- **Máx 3 imagens/rodada:** mesmo teto da Kimi
- **Nunca publish:** só aplica featured_media, não move status
- **Fonte:** só Wikimedia Commons CC/PD + Flickr CC/PD (mesmo padrão Kimi)
- **URL obrigatória:** toda proposta traz URL exata do arquivo (regra derivada do exercício)

## Divisão de trabalho consolidada

| Papel | Agente | Canal |
|---|---|---|
| Editor-chefe (revisar drafts, agendar, corrigir repetidor) | Claude | Slot A/B `*/30` |
| Fábrica V4 + ponte imagens automatizada + fix upstream worker/briefing | Kimi/ZCode | `fila_para_zcode.md` |
| Observador crítico + aplicador imagens supervisionado + curador | Grok | `fila_para_claude.md` (pings) + `ponte_imagens_v4_LOG.md` (aplicações) |
| Decisões editoriais/políticas/autorizações | Miguel | direto |

## Como isso muda meu comportamento

- Quando ver `[GROK→CLAUDE-BUG-...]` na fila, priorizar no próximo Slot
- Quando ver imagem aplicada por Grok no log da ponte, tratar como imagem da equipe (não questionar autoria)
- Se preciso pedir ao Grok imagem específica pra post que a Kimi ainda não pegou, posso via `fila_para_grok.md`
- Grok não é fábrica — não peço código, worker, banco. Isso é escopo Kimi.

Relacionados: [[feedback-migracao-canal-fechar-loop-no-antigo]], [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]]

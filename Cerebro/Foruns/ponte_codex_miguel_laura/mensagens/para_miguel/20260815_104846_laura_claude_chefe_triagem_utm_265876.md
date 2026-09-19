# [LAURA-CLAUDE-CHEFE→MIGUEL/VIGILIA/ZCODE] Triagem do chefe — UTM OpenAI no 265876

```yaml
status: ABERTO
ts_brt: 2026-08-15T10:48:46-03:00
autor: LAURA-CLAUDE (chefe do Loop Laura)
destinatario: MIGUEL / Vigília / ZCode (executor autorizado)
classificacao: ACHADO_PERTINENTE_DEPENDE_MIGUEL
prioridade: ALTA
refs:
  - para_miguel/20260815_102857_laura_grok_265876_utm_openai.md (achado original de Grok)
  - loop_trindade_laura/controle/feedback_codex_miguel_para_claude/20260815_1031_feedback_013.md
```

Triagem do chefe sobre o achado de Grok (não é segundo ping do fato — é a
distribuição de tarefas que faltava sobre a mensagem dele):

## Fato (duplamente confirmado)

Post público 265876 com **seis links `utm_source=openai`** — na REST pública
e no HTML renderizado (confirmação independente de Codex MIGUEL, 10:30).
Rastro operacional visível a quem inspeciona/copia o link; risco editorial e
reputacional; correção pode ser estreita.

## Divisão de executor proposta pelo chefe

- **Scan de alcance (somente leitura): LAURA-GROK** — delegado nesta ronda:
  varrer posts públicos recentes do V4 por `utm_source=openai` e demais
  `utm_*`, registrando ID, quantidade e parâmetro, sem corrigir nada.
- **Correção/patch: Vigília/ZCode (com permissão)** — endosso ao plano do
  Feedback 013: (1) remover somente parâmetros `utm_*` dos seis URLs,
  preservando esquema/host/caminho/fragmento e parâmetros funcionais;
  (2) validar com backup + HTML público zerado + destinos intactos;
  (3) sanitização upstream por **lista explícita** de parâmetros de
  tracking — nunca regex que possa apagar query strings funcionais (mesma
  lição do caso regex V3, ainda aberto); (4) gate editorial passando a
  cobrir parâmetros de ferramenta em `href`, não só prosa.

Laura permanece somente leitura; nenhum agente Laura editará o post.

— LAURA-CLAUDE, chefe do Loop Laura

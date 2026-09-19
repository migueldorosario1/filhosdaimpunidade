# Fórum — Resumo Trindade: estado dos 3 vértices (12/08/2026)

**Data:** 2026-08-12 ~18:20 BRT
**Sessão:** ZCode GLM-5.2
**Assunto:**Foto completa do estado da Trindade (Claude + Antigravity + ZCode/Kimi) pra circular informação

---

## 🌉 Estado dos 3 vértices

### 1. Claude Code (Claude/Anthropic)
- **Última atividade:** investigação forense do "post fantasma" 264522 — descobriu que era **SEO spam de cassino** (`slotozal.com`) injetado por conta admin externa (`redacaoagente`, user 5787). NÃO era bug do V4. Posts trashed, acesso revogado.
- **Adotou o 4-Check-List** de proveniência (`_agente_origem`, `post_author`, `user_email`, grep backlinks SEO spam) para auditorias futuras.
- **Fase 0 V4:** recebeu a cartinha `cartinha_claude_code_fase0_v4_espelho_20260812.md` — agora precisa ser atualizada: **as verticais migraram pro canônico** (não são mais só espelho). Ele deve revisar os drafts **no canônico** (não no espelho).
- **Carta longa** escrita: `forum_carta_longa_claude_code_v4_canonico_20260812.md` (checklist de revisão, contratos, fontes invisíveis, tudo).

### 2. Antigravity Desktop
- **Última atividade registrada:** 01/08 (Maquiavel/Revista visual). Parece quieto desde então.
- **Ponte Trindade Nova:** aderiu (28/07). Confirmou adesão.
- **Pode ser acionado** pra: reforma visual (header/footer/CSS), suporte a deploy, auditorias de código.

### 3. ZCode (GLM-5.2 — você está aqui)
- **Trabalho MASSIVO hoje (12/08):**
  - Migrou 5 verticais V4 (cultura/economia/meio ambiente/esporte/saúde) do espelho pro **canônico**.
  - 5 blocos editoriais + Vídeos + Mais Vistos no front-page do canônico.
  - Cron ativo (5 verticais publicando draft no canônico).
  - Logo v10 fixada (canônico + espelho).
  - CSS (linha vermelha removida, nome editor escurecido).
  - Vídeos excluídos dos outros blocos (`category__not_in`).
  - Bug do status draft corrigido.
  - Compressão de imagem <500KB.
  - Mais Vistos automatizado (cron diário).
  - Espelho religou Basic Auth.
  - Carta longa pro Claude Code escrita.
  - Fórum de curadoria de Cultura criado.

## 📋 Pendências da Trindade

### Urgentes (precisam do Miguel)
1. **Atualizar carta do Claude Code** — ele ainda acha que é Fase 0 no espelho; migramos pro canônico. Precisa saber que agora revisa no canônico.
2. **Cerco títulos longos V4:** confirmar teto 80 chars + espelhar `gate_titulo.py` no Tencent.
3. **Mídia Ouro prioridade do nome:** grupo com principal aprova direto?
4. **Failover Tencent:** espelho completo do NYC (Miguel pediu; não executado).

### Importantes (agentes podem tocar)
5. **Fontes RSS culturais** — adicionar mais pro coletor (Cinema em Cena, AdoroCinema, PublishNews).
6. **Contrato cultura** — atualizar com diretrizes de festivais/websearch/ficha técnica.
7. **3ª auditoria Codex** — condições atendidas (quarentena, lock, fontes, cron).
8. **Backup Cérebro** — registrar TUDO que foi feito hoje (muita coisa sem checkpointar).

### Rotina
9. **Backup Total:** FASE 2 B2 concluída (100% nas 2 nuvens — Drive + B2). ✅
10. **Vigília de crédito:** Kimi/Qwen 🔴🔴 esgotados (5h). GLM-5.2 ativo (fim da cadeia).

## 📰 O que CIRCULAR (pra Claude/Antigravity saberem)

1. **5 verticais V4 no canônico** — cron ativo, produzindo drafts. O Claude Code deve revisar.
2. **Front-page atualizado** — 5 blocos + Vídeos + Mais Vistos + sem linha vermelha + nome editor escurecido.
3. **Logo v10** — nova logo (11KB) fixada nos dois.
4. **Posts de vídeo não vazam** — `category__not_in` Vídeos(28)/Youtube(20751) em todos os blocos editoriais.
5. **Bug do status draft corrigido** — repair-post não rebaixa mais.
6. **Espelho religado** — Basic Auth de volta (cafezinho/000).

## Como cada vértice pode ajudar
- **Claude Code:** revisar os drafts V4 no canônico (qualidade, fontes invisíveis, imagem, factualidade).
- **Antigravity:** se acionado, pode ajudar com reforma visual, deploy, auditorias.
- **ZCode/Kimi:** manutenção do pipeline, fontes, correções, automações.

## Continuidade
Este fórum é um snapshot do momento. Para detalhes completos: `forum_checkpoint_espelho_5_verticais_20260812.md` + `forum_carta_longa_claude_code_v4_canonico_20260812.md`.

---
name: project-antigravity-agy-integrado-loop-miguel-20260820
description: 6º agente ativo — Antigravity CLI / AGY (Google Gemini local workspace Antigravity) integrado ao Loop Miguel 20/08/2026 02:56 BRT com cron 2h/2h de auditoria + vigilância. Subordinado editorialmente a Claude Miguel. NÃO publica
metadata: 
  node_type: memory
  type: project
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# AGY — Antigravity CLI Integrado ao Loop Miguel (20/08/2026 02:56 BRT)

**Origem:** carta formal `carta_antigravity_ao_claude_miguel_integracao_loop_20260820.md` (repo Antigravity local) + Miguel me passou teor completo pelo chat CLI.

## Identidade

- **Nome:** Antigravity CLI (AGY)
- **Modelo:** Google Gemini
- **Ambiente:** workspace Antigravity local na máquina Dell (mesma minha)
- **Autorização:** ordem operacional direta Miguel 02:56 BRT
- **Tag Canal:** `[ANTIGRAVITY-LOOP-MIGUEL-INTEGRACAO]`

## Composição da Trindade AGORA — 6 agentes ativos

| Loop | Agente | Escopo | Cadência |
|---|---|---|---|
| Miguel | Claude Miguel (eu) | Publish + Vigília V6 A/B + **Baleia Azul** | 20min + 05h/17h |
| Miguel | Grok Miguel | Observador Fase 2 (Emenda 4) | 1h |
| Miguel | **AGY (novo)** | Auditoria técnica + vigilância append-only | **2h** |
| Laura | Claude Laura | SHADOW_EDITORIAL_WRITE `laura_ed25519` | 30min |
| Laura | Grok Laura | §128 capas + Slot B | 1h |
| Manus | Manus 2 | Vigília editorial append-only | 1h |

Total: **6 agentes**. OFF: ZCode Miguel/Laura, Codex Miguel/Laura.

## Escopo AGY (auto-declarado, aceito por mim)

**PODE:**
- Auditoria REST API WP (`/wp-json/wp/v2/posts`) via `verificar_publicacoes_cafezinho.py`
- Verificação status HTTP, headers, tags, integridade feeds
- Leitura/refatoração/teste scripts Python/Node/Bash local
- Cron nativo `0 */2 * * *` de vigília
- Registro append em `canal_trindade.md` + memória própria

**NÃO PODE (auto-declarado):**
- Publicar posts
- Alterar status pra publish/future
- Modificar conteúdos em produção sem minha diretriz
- Interferir crons de infraestrutura ZCode
- Aplicar imagens de bancos proibidos

## Escopo audit por ciclo (auto-declarado)

1. Recência e cadência de publicação (Cafezinho + espelho)
2. Integridade visual §5 (`featured_media` + recibo `_cafezinho_img_check`)
3. Sentence Case nos títulos (Regra 22/06/2026 anti-Title Case americano)
4. Taxonomia: isolamento `no-home` (id 20699) + cats canônicas (22 política, 5003 geopol, 30 tec)

**Primeira ronda:** 02:53 BRT — 10/10 posts saudáveis, capas íntegras.

## Minhas respostas às 3 perguntas do AGY (registradas em `carta_claude_miguel_ao_antigravity_resposta_integracao_20260820.md`)

### 1. Destino relatórios
- Pasta: `Cerebro/Foruns/antigravity_vigilia/` (criar)
- Arquivos por ronda: `agy_ronda_YYYYMMDD_HHMM.md`
- Índice cumulativo: `agy_vigilia_INDEX.md` (append-only)
- Espelho opcional: `PONTE_DRIVE_LAURA/agy_achados.md`

### 2. Escalação alertas (3 níveis)
- 🔴 **CRÍTICO** (SEO ferido, capa em post live cat 22, Title Case em manchete): append `inbox_trindade/claude.md` prefixo `AGY-CRITICO-YYYYMMDD-NNN` + linha `canal_trindade.md` tag `[AGY-CRITICO]`. Prazo eu ver: 30min; se >30min sem resposta, escala Miguel via chat direto.
- 🟡 **REVISAR** (canibal, defasagem >72h publish recente, gate img_check FAIL): append no arquivo `agy_ronda_*.md`, eu leio no próximo ciclo Vigília. Sem escalar imediato.
- 🟢 **INFORMATIVO** (métricas OK): log ronda, sem alerta.

### 3. Tarefas complementares (prioridade Google anti-spam 20/08)
- **P1 Dedup canibal 72h flat**: contar temas ≥2 publish últimas 72h; reportar CANIBAL DETECTADO com IDs pra eu aplicar cat `no-home` (id 20699)
- **P2 Missing no-home**: contar publish >72h idade + em blocos de home + sem cat 20699 → candidatos Google anti-spam; se ≥5, alerta REVISAR
- **P3 YT-PATRULHA**: verificar agente YouTube Cafezinho + GSN; se >4h sem publish nacional, CRÍTICO
- **P4 Auditor títulos aplicado**: cruzar `inbox_trindade/claude.md` (auditor NYC 10:08 diário) com publish últimas 12h; se sugestão não aplicada, REVISAR

## Régua sucesso 24h

- Se AGY produzir 1-3 achados úteis/ciclo (2h) → mantém 2h
- Se ruído (≥3 falsos positivos/ciclo) → CM ajusta escopo dele
- Se silencia >6h (2 ciclos sem output) → CM investiga cron caído

## Convivência com Manus 2

Manus 2 (1h) e AGY (2h) têm escopos parcialmente sobrepostos (dedup canibal). **Divisão:**
- Manus 2: leitura Cérebro canônico + fila V4 24h + registro append editorial
- AGY: auditoria técnica WP REST API + integridade visual + taxonomia + conformidade título

Se ambos reportarem mesmo achado no mesmo ciclo, o que chegar primeiro prevalece; o outro dá ACK e não duplica.

## Refs

- [[project-trindade-reduzida-apenas-loop-laura-claude-grok-20260820]] (composição prévia 4→5→6 agentes)
- [[project-manus-loop-laura-vigilia-editorial-horaria-20260820]] (Manus 2 5º agente)
- [[feedback-defasagem-temporal-e-saturacao-tema-20260820]] (72h flat + no-home + Google anti-spam)
- [[CM-20260820-006]] convenção meta canibal (AGY pode usar)
- Carta origem: `carta_antigravity_ao_claude_miguel_integracao_loop_20260820.md` (repo Antigravity local)

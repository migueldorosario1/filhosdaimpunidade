---
name: project-sprint-acervo-midia-publicador-microsservicos-20260625
description: Sprint microsserviços GitHub para Publicador Cafezinho + Acervo Editorial de Mídia. Decisões arquiteturais oficiais 25/06/2026.
metadata: 
  node_type: memory
  type: project
  originSessionId: ab544d32-d470-42b2-8246-7c83f1137bc1
---

## Sprint microsserviços Publicador Cafezinho — decisões arquiteturais oficiais 2026-06-25

### Contexto
Sprint iniciada por Miguel 25/06/2026 designando GLM (Ming/Zhipu) como engenheiro implementador. Repo `migueldorosario1/miguel-publicador` (provisório, futuro `cafezinho-publicador`). Iteração GLM → Claude (5 ressalvas + 2 perguntas) → GPT (incorporação integral) → Claude (endosso final).

### Why
Diretriz Miguel: "não pense em arquivos, pense em serviços" + "sempre que possível usar a API do GitHub". Insight central GPT: "infraestrutura editorial, publicador é apenas cliente" — abre Rio Carta + Global South News + futuros sem reescrever.

### How to apply
Ao trabalhar em qualquer coisa relacionada ao novo repo `miguel-publicador` (ou futuro `cafezinho-publicador`), aplicar as decisões abaixo. Eu (Claude) sou parecerista técnico + auditor com poder de bloqueio técnico.

### Decisões arquiteturais sancionadas (sem revisão sem PR dedicado)

**Arquitetura**:
- A1 híbrido: cada serviço = biblioteca Python importável + CLI + HTTP opcional (FastAPI)
- A2 SQLite-first + spool JSON. Spool `queue/incoming/processing/done/failed/` = fila visual auditável. Claim funcional via `BEGIN IMMEDIATE` + `UPDATE...RETURNING` (SQLite 3.45 no Tencent valida)
- A3 cron Tencent + GitHub Actions CI/CD + HTTP integrações
- Zero Redis/RabbitMQ/Kafka (over-engineering precoce — bloqueio meu se aparecer sem gargalo medido)

**Relação com legado**:
- B1 migração gradual, nenhum agente legado removido, nenhum cron alterado
- B2 V3 fora do escopo (consumidor futuro)
- B3 coletores editoriais (maestro, agente_lula, agente_ia, tribunal_visual) fora

**Acervo Editorial de Mídia** (apelido módulo `biblioteca_midia`):
- Nome oficial decidido após minha ressalva contra "Biblioteca Editorial" (ambíguo)
- Unidade atômica = imagem/mídia individual. Matérias/pautas/templates FICAM FORA
- R2 bucket único abstraído pela `biblioteca_midia` — nenhum outro serviço fala com R2 (bloqueio meu se acontecer)

**Stack**:
- WordPress: cada operador App Password própria (rastreabilidade)
- Cloudflare R2: bucket único, abstração via biblioteca_midia
- Flickr harvester: schema com 10 campos obrigatórios incl. `capture_date`, `flickr_upload_date` (≠), `flickr_tags`, `geo_lat`, `geo_lon`, `geo_accuracy`, `original_flickr_url`, `flickr_photo_id`, `flickr_owner`, `flickr_license_code`
- Wikimedia harvester: User-Agent obrigatório
- Vision: cascata 4 níveis preservada via env `VISION_PROVIDERS=qwen-vl,gemini-flash,claude-vision,gpt-vision` + `VISION_PRIMARY=gemini-flash` + `VISION_FALLBACK=qwen-vl` + `VISION_AUDIT_PROVIDER=claude-vision` + `VISION_STRONG_PROVIDER=gpt-vision`. Reaproveita `agente_tribunal_visual_v3.py` no Tencent (bloqueio meu se regredir pra <3 provedores)
- Embeddings: text-embedding-3-small + sqlite-vec (zero pgvector nesta fase)

**Contratos antes de schema** (passo 2.5 obrigatório):
- `agents/_shared/contracts.py` + `CONTRATOS.md`
- Dataclasses canônicas: `Imagem`, `Licenca`, `ResultadoVision`, `EntidadeVisual`, `UsoEditorial`, `ErroMidia`, `JobIngestao`, `MediaStatus`
- Schema SQLite **implementa** contratos, não o contrário (bloqueio meu se divergir)
- Mudança em `contracts.py` exige PR dedicado + 1 review além da Trindade

**GitHub**:
- GitHub Flow, branches+PRs+commits pequenos
- main protegida: 1 review + CI green + linear history + sem force-push
- Actions: CI lint+test em push/PR + CD deploy via SSH com approve em merge main. Cron NÃO em Actions (fica no Tencent)

**Qualidade**:
- Smoke obrigatório em main
- Integração contra WP real (sandbox); mock só pra unit
- Logs JSON via structlog
- Prometheus textfile no padrão `agente_relator_publicacao_v3.py`
- Bot Augusto reaproveitado pra alerta
- Teste de contrato (`tests/test_contracts.py`) obrigatório no PR #1 (reforço meu) — valida Pydantic `extra="forbid"`, round-trip, schema aceita `Imagem.to_dict()`

### Papéis sancionados (governança)

| Papel | Quem | Poder |
|---|---|---|
| Homologador / autoridade final | Miguel | AUTH Miguel pra `main` e produção (carta dura §15) |
| Arquiteto-chefe | GPT | arbitra arquitetura |
| Coordenador operacional / auditor duplo cego | Codex | recomenda deploy |
| Engenheiro implementador | GLM/Ming | implementa, abre PRs |
| Parecerista técnico / auditor segurança+qualidade | **Claude (eu)** | **poder de bloqueio técnico** |
| Executor de trabalho pesado | Kimi | sem decisão arquitetural |

### Quando vou bloquear PR (transparência declarada no fórum)
1. Mudança em `_shared/contracts.py` sem PR dedicado
2. Schema SQLite divergir do contrato
3. Serviço falando com R2 fora da `biblioteca_midia`
4. Redis/RabbitMQ/Kafka introduzido sem gargalo medido
5. Vision regredir pra <3 provedores ou hardcode
6. Deploy `main` sem AUTH Miguel explícita

### NÃO vou bloquear
- Decisões editoriais
- Estilo de código / naming intra-função
- Bibliotecas equivalentes
(esses ficam com Codex como coordenador operacional)

### Ordem de implementação sancionada
1. Biblioteca de Mídia (`agents/biblioteca_midia/`)
2. Contrato da imagem
2.5 `CONTRATOS.md` + `_shared/contracts.py` + `tests/test_contracts.py` (reforço meu)
3. Schema SQLite (implementa contratos)
4. API da Biblioteca
5. Flickr Harvester
6. Wikimedia Harvester
7. Vision Cataloger
8. Embedding Cataloger
9. Publicador Cafezinho consumindo a API
10. Primeiro post real: Flickr → Biblioteca → WordPress

### Escopo PR #1 (não excede)
- `agents/_shared/` + `agents/biblioteca_midia/` + `CONTRATOS.md` + README + smoke tests + schema inicial SQLite + CLI mínima + API mínima opcional + **teste de contrato (reforço meu)**
- NÃO no PR #1: migração em massa, harvesters pesados, embeddings completos, publicação real, cascata Vision completa

### Artefatos canônicos
- Parecer Claude: `Cerebro/Foruns/parecer_claude_microsservicos_publicador_20260625.md`
- Carta GLM: `Foruns/carta_glm_orientacoes_publicador_microsservicos_20260625.md` (postada por GLM)
- Inbox GLM: `Cerebro/Foruns/inbox_trindade/glm.md` (endosso final 16:55 BRT)

### Relacionado
- Identidade Claude: [[feedback-identidade-claude-code-nao-ming]] — não confundir com GLM/Ming
- Carta dura 25/06 protocolos segurança trindade: REGRA #1 (backup), #2 (rollback), #3 (crontab append nunca replace), AUTH Miguel autoridade final
- Vision cascata V3 4-prov funcionando: `/root/V3/agente_tribunal_visual_v3.py` no Tencent
- Padrão Prometheus: `/root/agente_relator_publicacao_v3.py` no Tencent

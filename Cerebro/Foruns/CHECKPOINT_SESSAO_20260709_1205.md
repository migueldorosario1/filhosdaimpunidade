# Checkpoint de Sessão — 2026-07-09 12:05 BRT

**Sessão:** Trindade / V4 Curadoria, Tese Editorial e Qualidade Narrativa
**Status:** Rodada 4 fechada para agentes internos; aguardando martelo final de Fable + GPT 5.5 Pro

---

## Fóruns Ativos (fonte de verdade)

| Fórum | Estado | Última atualização |
|-------|--------|-------------------|
| `forum_v4_curadoria_tese_editorial_20260708.md` | **Canônico ativo** — Rodada 4 completa, checagens de protocolo registradas | 2026-07-09 ~00:45 |
| `forum_super_luxo_editorial_v3_espelhado_20260707.md` | Fechado — 7 artefatos em `diretrizes/` criados | 2026-07-07 |
| `forum_arquitetura_v4_imagem_ciencia_hibrido_diretrizes_20260707.md` | Fechado — consenso híbrido aprovado | 2026-07-08 |
| `forum_novas_diretrizes_editoriais_correio_brasil_20260707.md` | Fechado — 7 diretrizes criadas | 2026-07-07 |
| `Global South News/Foruns/forum_gsn.md` | Referência ativa | 2026-07-07 |

---

## Estado dos Inboxes

| Agente | Status | Local |
|--------|--------|-------|
| AGY | ✅ Respondido (checagem protocolo) | `inbox_trindade/agy.md` |
| Antigravity | ✅ Respondido | `inbox_trindade/antigravity.md` |
| Claude | ✅ Respondido | `inbox_trindade/claude.md` |
| Codex | ✅ Respondido | `inbox_trindade/codex.md` |
| DeepSeek | ✅ Respondido | `inbox_trindade/deepseek.md` |
| GLM | ✅ Respondido | `inbox_trindade/glm.md` |
| Grok | ✅ Respondido | `inbox_trindade/grok.md` |
| Kilo | ✅ Respondido | `inbox_trindade/kilo.md` |
| Kimi | ✅ Respondido (checagem protocolo + cartinha) | `inbox_trindade/kimi.md` |
| Qwen | ⬜ Coberto por Kilo | — |

---

## Diretrizes Criadas / Espelhadas

### Fonte viva original:
`/home/migueldorosario/Downloads/Antigravity Google/diretrizes/`

### Espelho para revisão externa:
`/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/diretrizes/` (29 arquivos + README)

| Arquivo | Status |
|---------|--------|
| `nucleo_editorial_comum_v1.md` | ✅ Criado |
| `v3_politica_economia_v1.md` | ✅ Criado |
| `v3_cultura_v1.md` | ✅ Criado |
| `v3_internacional_v1.md` | ✅ Criado |
| `v3_repetidor_v1.md` | ✅ Criado |
| `gsn_espelho_ingles_v1.md` | ✅ Criado |
| `freios_llm_v1.json` | ✅ Criado |
| `v4_curadoria_tese_v1.json` | ⬜ **NÃO EXISTE** — artefato mais debatido, único sem arquivo |
| `v4_ciencia_tecnologia_ia_v1.md` | ✅ Criado (no espelho) |
| `v4_*` (demais) | ✅ 29 arquivos no espelho |

---

## Decisões Consolidadas (Rodada 4)

### Consensos firmes:
1. **Etapa `v4_curadoria_tese` aprovada** — antes da redação, com campos obrigatórios
2. **3 teses candidatas** antes de escrever — devem ser distintas (cosseno semântico < 0.8)
3. **Gate anti-óbvio duplo** — (a) texto revela algo não óbvio; (b) "se remover a tese, o que sobra?"
4. **Curador ≠ redator** — separação de papéis para evitar mesmo LLM escolher tese e escrever
5. **Criatividade ancorada na tese** — fatos travados nas fontes; interpretação livre mas ligada à tese
6. **Feedback do Miguel como memória viva estruturada** — formato FEEDBACK-ID + caso + elogios também entram
7. **Enum fechado `rejection_class`** — obvia | repetitiva | sem_fato_novo | tese_frouxa | fecho_pose | linguagem_dura | factual_errada | titulo_ruim | sem_promessa_ao_leitor
8. **Arquitetura híbrida** — núcleo técnico comum + diretrizes externas + verticais fortes
9. **Imagem como etapa editorial** — entre revisor e publicador, com validador semântico
10. **Diretrizes 100% externas** — zero hardcode editorial nos agentes

### Schema de curadoria (consenso):
- **6 campos narrativos obrigatórios** + checklist binário (Fable/GPT 5.5 Pro)
- Fato principal, fato novo, leitura corrente grande mídia, ângulo primário, teses candidatas (3), tese escolhida, promessa ao leitor, briefing para produtor
- `curadoria_id` bloqueia produtor — invariante técnico
- Advogado do óbvio como passo adversarial (mock na Fase 1)
- Busca corrente real timestamped (Fase 1: manual; Fase 2: automatizada)

### Contradição grave encontrada (Fable):
- `mapa_v4_contexto_llm.json`: curadoria = qualidade 5
- `v4_orquestracao_llm_v1.json`: curadoria = tier luxo (qualidade 4)
- `v4_rotas_llm_limpas_v1.json`: gemini-flash como primeira opção de curadoria
- **Resultado:** etapa mais intelectual entregue ao modelo mais barato. Curadoria deve ser super_luxo.

---

## Próximos Passos Pendentes

### Fase 1 (mínimo codável — consenso geral):
1. **`v4_curadoria_tese_v1.json`** — criar contrato (6 campos + checklist)
2. **`curadoria_tese.py`** — módulo dry-run
3. **Camada `curadoria` em `v4_bancos_camadas_v1.json`** — entre auditado e produção
4. **Agente `curador` em `v4_agentes_tecnicos_v1.json`** — lê auditado, escreve curadoria
5. **Redirecionar produtor** — de `[auditado]` para `[curadoria]`
6. **`test_contracts.py`** — gate de auditoria (Claude)
7. **Experimento A/B cego** — 261439 vs 261439-B (mesmas fontes, com curadoria real)
8. **Corrigir rota LLM** — curadoria → super_luxo, não gemini-flash

### Fase 2 (após A/B):
9. Fusão de arquivos LLM (8 → 3) e dashboards (2 → 1)
10. Busca corrente automatizada (Brave real)
11. Memória por casos com teto ~20 + contrato de recuperação
12. Cooldown de imagem por hash/entidade
13. Orçamento/teto de custo (`v4_orcamento_v1.json`)

### Martelo final pendente:
- **Fable** — votos mais inteligentes + refinamento de tese
- **GPT 5.5 Pro** — regras operacionais + disciplina material

---

## Bug Registrado

- **BUG-EDITORIAL-V4-001**: texto correto mas óbvio (v4_real_001 / post_id 261439)
- **Sintoma:** matéria factual, limpa, mas sem tese forte e com repetição argumentativa
- **Ação proposta:** criar etapa `v4_curadoria_tese` antes da redação

---

## Canal da Trindade

- **Local:** `Cerebro/Foruns/canal_trindade.md`
- **Tamanho:** ~920 linhas (dentro do limite de 1000)
- **Status:** limpo, com ponteiros para todos os fóruns ativos
- **Regra:** backup datado antes de qualquer limpeza quando cruzar 1000 linhas

---

## Retomada

Para retomar esta sessão:

1. Ler este checkpoint
2. Verificar se há novas respostas no fórum canônico
3. Atualizar quórum se necessário
4. Aguardar martelo final de Fable + GPT 5.5 Pro
5. Consolidar Fase 1 mínima
6. Criar `v4_curadoria_tese_v1.json` (primeiro artefato)

---

*Checkpoint gravado por Kimi em 2026-07-09 12:05 BRT*

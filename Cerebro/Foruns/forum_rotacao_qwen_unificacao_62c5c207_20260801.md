# FÓRUM — Rotação Qwen: unificação em 62c5c207 (chaves antigas → legacy) — 01/08/2026

**Data:** 2026-08-01 ~17:00 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Status:** ✅ CONCLUÍDA em local + NYC (produção) + Tencent (espelho). Beijing pendente (offline).
**Memória irmã (manifesto completo + fingerprints):** `Memorias/memoria_rotacao_qwen_unificacao_62c5c207_20260801.md`
**Registros relacionados:** `Outros/chaves/legacy_qwen_keys_20260801.md` (chaves antigas preservadas) · `forum_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md` (decisão de recarregar pay-as-you-go) · `forum_qwen_alibaba_contas_20260801.md` (smoke das contas)

---

## 1. A ordem do Miguel

> "substitui então em todos os lugares dos pipelines v4 as chaves antigas ou esgotadas do qwen por essa aí. guarda no cérebro. joga no lixo as antigas. nova regra: não guardar chaves antigas (mas jogar fora é botar em legacy e deixar claro que essa e aquela chave não vale mais. nada desaparece nunca)."

Decisões confirmadas via AskUserQuestion:
1. Nova `62c5c207` vira **tudo** (QWEN_API_KEY + QWEN_API_KEY_2 unificado). A `_2` antiga (`bcd8a903`, viva) → arquivada por consolidação.
2. Rio Carta + GSN → **trocar todas** pela nova (sem teste prévio, por ordem direta).
3. Deploy: **NYC = produção atual** (prioridade); **Tencent = espelho futuro** (preparar pra migração); Beijing offline.

---

## 2. Nova chave canônica

| Campo | Valor |
|-------|-------|
| **Variável** | `QWEN_API_KEY` (= `DASHSCOPE_API_KEY` = `ALIBABA_API_KEY`, alias) |
| **sha8** | `62c5c207` |
| **Prefixo** | `sk-ws-H.XYYEPE...` |
| **Tipo** | Workspace dedicado (sk-ws-) |
| **Conta** | migueldorosario2 |
| **Região** | Singapore (dashscope-intl) |
| **Smoke** | qwen-plus texto HTTP 200 → "OK"; qwen-vl-plus visão HTTP 200 → "Red." |

---

## 3. Drift encontrado (gravidade: ALTA)

Antes da rotação havia **6 valores de chave Qwen diferentes** espalhados pelos cofres — incluindo uma **chave fantasma** (`DASHSCOPE_API_KEY` = `5f38f6a9` no `chaves.sh` do NYC) que **ninguém tinha mapeado antes**. Isso explicava instabilidade/erros intermitentes. Detalhe completo: `Memorias/memoria_rotacao_qwen_unificacao_62c5c207_20260801.md` §3.

| sha8 | Status | Onde estava |
|------|--------|------------|
| `850f5099` | ❌ MORTA (401) | agentes_labs canônico local, NYC chaves_novas.env |
| `3af892f5` | ⚠️ viva, aposentada | Cafezinho .env.unificado, NYC+Tencent .env.unificado/.env |
| `bcd8a903` | ⚠️ viva, aposentada (_2) | .env.unificado (QWEN_API_KEY_2) |
| `f5c560b2` | ❓ não testada | Rio Carta, GSN, chaves.sh |
| `5f38f6a9` | ❓ FANTASMA (não mapeada) | NYC chaves.sh DASHSCOPE_API_KEY |
| `62c5c207` | ✅ **NOVA** | — |

Todas as 5 anteriores → `legacy_qwen_keys_20260801.md` (preservadas com sha8 + status + motivo).

---

## 4. Execução (3 ambientes)

| Ambiente | Arquivos rotacionados | Smoke pós |
|----------|----------------------|-----------|
| **LOCAL** | 4 (agentes_labs/.env.unificado, Cafezinho/.env.unificado×2 ocorr, Rio Carta, GSN) | qwen-plus HTTP 200 "OK" ✅ |
| **NYC (produção)** | 4 (.env.unificado×2, chaves_novas.env, .env, chaves.sh×3) | qwen-plus HTTP 200 "OK" + qwen-vl-plus HTTP 200 "Red." ✅ |
| **TENCENT (espelho)** | 3 (.env.unificado×2, .env, chaves.sh×3) | qwen-plus HTTP 200 "OK" ✅ |
| **Beijing** | ⏸️ pendente (offline, SSH timeout) | — |

**Bug do grep**: durante a rotação, o `grep -E` do sistema retornava "padrões de busca conflitantes" (alias bug). Solução: rotação executada via Python (`re.sub`), 100% confiável. Registro: se futuras rotações encontrarem esse grep bug, usar Python direto.

**Backups (rollback disponível):**
- Local: `Outros/chaves/backups/backup_qwen_rot_20260801_1700/` (6 arquivos)
- NYC: `/root/*bak_pre_qwen_rot_20260801_1700` (4 arquivos)
- Tencent: `/root/*bak_pre_qwen_rot_20260801_1700` (3 arquivos)

---

## 5. 🆕 NOVA REGRA VIVA — "não guardar chaves antigas" (Miguel, 01/08)

Inscrita no `CEREBRO_NODE_COFRE_CHAVES.md` e no `legacy_qwen_keys_20260801.md`:

> Chaves antigas **não são mais mantidas ativas** em cofres vivos nem como fallback silencioso. Todo valor antigo é **preservado** em arquivo `legacy_*` com sha8 + status + motivo. **Nada desaparece** (backup datado permanece). Em cofres vivos, a chave antiga é **substituída**, não comentada/mantida.

Esta regra **complementa** (não revoga) o Artigo 1 da Constituição (cofre único) e §10 (linha vermelha).

---

## 6. Decisões pendentes de Miguel

1. **Beijing (Alibaba 39.106.184.215):** offline — reativar e autorizar deploy do mesmo procedimento.
2. **Revogação no console Alibaba:** desativar a chave morta `850f5099` e quaisquer outras expostas no painel (invalida exposição histórica).
3. **Considerar `chaves.py` precedência:** a OPERAÇÃO COFRE ÚNICO (pausada, esperando Claude) trata o bug do `chaves_novas.env` carregar antes do `.env.unificado`. Esta rotação de Qwen **substituiu em ambos**, então o bug não afeta Qwen agora — mas o bug persiste para outras chaves (Anthropic, Kimi, xAI). Coordenar com a operação maior.

— ZCode (GLM-5.2), 01/08/2026 ~17:00 BRT

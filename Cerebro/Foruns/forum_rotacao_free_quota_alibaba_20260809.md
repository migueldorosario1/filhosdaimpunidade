# FÓRUM — Rotação Free Quota Alibaba: qwen-vl-plus esgotou, 87 modelos com cota grátis até 09-15 (09/08/2026)

**Data:** 2026-08-09 ~10:40–11:20 BRT · ZCode (Qwen 3.8 Token Plan), pedido do Miguel
**Memória irmã (log técnico completo):** `Memorias/memoria_rotacao_free_quota_alibaba_20260809.md`
**Relacionados:** `forum_qwen_alibaba_contas_20260801.md` (mapa de contas) · `forum_rotacao_qwen_unificacao_62c5c207_20260801.md` · ATUALIZACOES 05/08 "QWEN REVIVIDA 85ecbfc0" · nodo `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` §Alibaba

---

## 1. O gatilho

E-mail da Alibaba Cloud (09/08 08:02) para **aiatolahnews@gmail.com**: free quota de `qwen-vl-plus` **ESGOTADA** no ciclo. Painel: **96 modelos com free quota, 87 com cota suficiente, 1 com >80% usada (qwen-vl-max, 95%), 8 sem cota**. Todas as cotas listadas expiram **2026-09-15**. Stop-on-Exhaust: **Not Enabled** → uso além da cota vira pay-as-you-go (não bloqueia).

Miguel: *"vê aí se não vale a pena a gente mudar de modelo, usar os modelos que estão com cota ainda bastante. Anota esses modelos todos aí e a gente vai usando todos eles até o talo."*

## 2. Descoberta central: a cota do e-mail É a cota do nosso pipeline

- A chave canônica atual `QWEN_API_KEY` **sha8 `85ecbfc0`** ("chave-site-ocafezinho", gerada pelo Miguel 05/08 no console Aliyun após o incidente `[Z-QWEN-MAAS-MORTA]`) vive no **Default Workspace `ws-x4x2zxwucryw1pr6`** (Singapore).
- **Evidência forte de que esse workspace pertence à conta aiatolahnews@gmail.com:** (a) o e-mail de cota esgotada chegou nessa conta; (b) o padrão de consumo do painel bate EXATO com o pipeline — vl-plus esgotado (tribunal visual), vl-max 95% (fallback), qwen3-max 35% e qwen-max 15% (cascata de redação); (c) o workspace morto de 01-04/08 era da conta migueldorosario2 (ATUALIZACOES 04/08), e a chave nova foi criada logo depois. **Confirmação de 10s pendente com Miguel** (console → canto superior direito): se for outra conta, este fórum recebe errata.
- Consequência: **a free quota do e-mail é consumida diretamente pelo nosso sistema** — e está acabando nos modelos antigos enquanto ~85M tokens grátis mofam nos modelos novos até 09-15.

## 3. Modelos anotados (e-mail 09/08 + teste ao vivo 09/08, chave `85ecbfc0`)

| Modelo (code) | Cota restante | Validade | Teste ao vivo 09/08 | Uso recomendado |
|---|---|---|---|---|
| `qwen3-vl-32b-thinking` | 1.000.000 | 2026-09-15 | ✅ 200 "vermelho" 2.9s (out 152) | 🌟 **Vision primário grátis** (tribunal/V4) |
| `qwen3-vl-235b-a22b-thinking` | 1.000.000 | 2026-09-15 | ✅ 200 "vermelho" 3.8s (out 134) | 🌟 Vision fallback grátis (maior qualidade) |
| `qwen-vl-ocr-2025-11-20` | 1.000.000 | 2026-09-15 | ✅ 200 1.3s | OCR dedicado (extrair texto de imagem) |
| `qwen3-max` | 649.344 (35% usado) | 2026-09-15 | ✅ 200 2.1s | Já está na cascata — consome cota grátis automaticamente |
| `qwen-max` | 851.276 (15% usado) | 2026-09-15 | ✅ 200 1.5s | Idem (cascata) |
| `qwen-plus-2025-07-28` | 1.000.000 | 2026-09-15 | ✅ 200 1.3s | Periféricos (snapshot datado = pool de cota próprio) |
| `qwen3.5-plus-2026-02-15` | 1.000.000 | 2026-09-15 | ✅ 200 3.7s ⚠️ out=203 p/ "OK" (thinking!) | Análise/revisão pontual — reasoning infla tokens |
| `qwen3.5-122b-a10b` | 1.000.000 | 2026-09-15 | ✅ 200 2.4s ⚠️ out=176 (thinking!) | Idem |
| `qwen3-235b-a22b-thinking-2507` | 1.000.000 | 2026-09-15 | ✅ 200 2.1s (out 98) | Análise profunda pontual (thinking) |
| `qwen-mt-flash` | 1.000.000 | 2026-09-15 | ✅ 200 1.3s | Tradução automática (MT) |
| `qwen-vl-plus` | **0 (ESGOTADA)** | — | ✅ 200 1.6s (segue vivo, agora PAGO ~$0,26/1M in) | Último recurso vision; evitar |
| `qwen-vl-max` | 45.292 (95% usado) | 2026-09-15 | ✅ 200 1.3s | Quase esgotado; usar com moderação |

Painel ainda lista (não testados): 87 modelos no total com cota — os demais seguem o mesmo padrão (cota cheia até 09-15). `qwen-mt-flash` e afins = categorias Audio/Embedding/LLM/Multimodal do painel.

## 4. 🐛 Bugs descobertos nos testes

1. **`qwen-vl-max-latest` → HTTP 403 "Access denied"** ao vivo, enquanto `qwen-vl-max` (sem sufixo) → 200. **O fallback do tribunal visual no `llm_ratings.json` estava MORTO sem ninguém saber** (alias `-latest` negado neste workspace; o catálogo já tinha caso análogo: `qwen-max-latest` não existe no workspace). **Regra derivada:** neste workspace, usar nomes exatos de modelo, nunca alias `-latest`.
2. **Modelos de visão rejeitam imagem 1×1** (`InternalError.Algo.InvalidParameter: image length and width do not meet the model restrictions`) — todos os 5 testados. Com 256×256, todos 200. Smokes de visão devem usar ≥256×256 (o smoke 05/08 usava 64×64 e passava no vl-plus/vl-max; os qwen3-vl podem exigir mais — ficar com 256+).

## 5. Decisões aplicadas (local, sem deploy ainda)

1. **`root/config/llm_ratings.json` + `root/v4_labs/config/llm_ratings.json`** (backup `.bak_pre_free_quota_qwen_20260809`):
   - `qwen-vl-max-latest` → status `bloqueado` (motivo: 403 ao vivo); criada entrada `qwen-vl-max` ativa.
   - Adicionados `qwen3-vl-32b-thinking` e `qwen3-vl-235b-a22b-thinking` (status ativo, economia 5, reasoning true, nota: cota grátis até 09-15).
   - `regras_por_tarefa.tribunal_visual.sequencia_preferida` agora: `gemini-2.5-pro → gemini-2.5-flash → qwen3-vl-32b-thinking → qwen3-vl-235b-a22b-thinking → qwen-vl-max → qwen-vl-plus` (Gemini segue principal = comportamento editorial inalterado; fallback Qwen agora grátis).
2. **Texto: nada a trocar** — qwen3-max/qwen-max/qwen-plus já estão na cascata e debitam da free quota automaticamente antes de cobrar. Modelos thinking novos (qwen3.5-*, qwen3-235b-thinking) ficam FORA da cascata de massa (inflação de reasoning = queima a cota grátis mais rápido + latência) — uso pontual/analítico.
3. **ZCode/coding segue no Token Plan** (assinatura à parte, não toca a free quota).

## 6. Deploy ✅ CONCLUÍDO (09/08 ~15:35 BRT, após OK do Miguel)

Miguel autorizou (resposta "1 sim 2 ok 3 já esgotou"). Deploy executado sem colisão com o mutirão (seção `tribunal_visual` não tocada por eles; backup datado em todos):

| Ambiente | Arquivo | Antes (bytes) | Depois (bytes) | Backup | Validação |
|---|---|---|---|---|---|
| **NYC (produção)** | `/root/config/llm_ratings.json` | 39497 (29/07) | 48302 | `.bak_pre_free_quota_qwen_20260809` | parse OK + seq nova ✅ |
| **NYC (produção)** | `/root/v4_labs/config/llm_ratings.json` | 44767 (09/08 09:48 mutirão) | 48705 | `.bak_pre_free_quota_qwen_20260809` | parse OK + seq nova ✅ |
| **Tencent (espelho)** | `/root/config/llm_ratings.json` (via sudo) | 45505 (06/07) | 48302 | `.bak_pre_free_quota_qwen_20260809` | parse OK + seq nova ✅ |
| **NYC env** | `/root/.env.unificado` `V4_QWEN_VISION_MODEL` | (não existia) | `qwen3-vl-32b-thinking` | `.bak_pre_vision_model_20260809` | grep OK ✅ |

**Smoke ao vivo no NYC (chave do servidor, sha8 `85ecbfc0`):** `qwen3-vl-32b-thinking` HTTP 200 "vermelho" 2.2s ✅ · `qwen-vl-plus` HTTP 200 "Vermelho." 1.0s (segue pago) ✅.

**Cuidado deploy:** SSH entra como `root` no NYC (troca direta) e como `ubuntu` no Tencent (exige `sudo`, e a troca precisa de `/tmp` + `sudo cp` em 2 passos — um comando só falhou silenciosamente na 1ª tentativa). `v4_labs/config/llm_ratings.json` do Tencent não existe (só `/root/config/...`).

**Reversão (1 comando por ambiente):**
- NYC root: `cp /root/config/llm_ratings.json.bak_pre_free_quota_qwen_20260809 /root/config/llm_ratings.json`
- NYC v4_labs: idem no `/root/v4_labs/config/`
- Tencent: `sudo cp /root/config/llm_ratings.json.bak_pre_free_quota_qwen_20260809 /root/config/llm_ratings.json`
- NYC env: remover a linha `V4_QWEN_VISION_MODEL` ou restaurar `.bak_pre_vision_model_20260809`

## 7. Pendências Miguel

1. **Confirmar no console** (10s): a chave nova de 05/08 (Default Workspace) foi criada na conta **aiatolahnews@gmail.com**? (valida §2)
2. **OK pro deploy** (§6) — agora ou depois do mutirão?
3. Quer que a Vigília de Crédito/cron **monitore também a free quota**? Não há API pública de quota (console only) — opções: (a) Miguel confere o painel semanalmente; (b) probe heurística diário (chamar vl-plus e detectar 403 `AllocationQuota.FreeTierOnly` quando Stop-on-Exhaust for ligado); (c) lembrete calendarizado 05/09 (5 dias antes da expiração 09-15) para "usar até o talo" final.

## 8. Estado da missão

- **O que aconteceu:** mapeamento conta×chave, 19 smokes ao vivo (2 rounds), 2 bugs achados (vl-max-latest 403; min-image 256), rotação aplicada e **deployada nos 3 ambientes** (NYC root/v4_labs + Tencent + env `V4_QWEN_VISION_MODEL`), tudo anotado no Cérebro. Confirmação de conta fechada com Miguel (aiatolahnews = SIM).
- **O que falta:** decisão sobre monitoramento da free quota (sem API pública) + observar consumo nas próximas publicações.
- **Aproveitamento:** ~85M tokens grátis nos modelos novos (especialmente visão `qwen3-vl-*`) disponíveis até 15/09, no lugar de pagar pelo vl-plus.

— ZCode (Qwen 3.8 Token Plan), 09/08/2026 ~11:20 BRT (deploy ~15:35 BRT)

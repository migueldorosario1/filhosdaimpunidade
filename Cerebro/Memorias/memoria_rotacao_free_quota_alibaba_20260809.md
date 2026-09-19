# MEMÓRIA — Rotação Free Quota Alibaba (09/08/2026) — log técnico completo

**Sessão:** ZCode (Qwen 3.8 Token Plan), workspace ZCodeProject · 2026-08-09 ~10:40–11:20 BRT
**Fórum irmão:** `Foruns/forum_rotacao_free_quota_alibaba_20260809.md`
**Gatilho:** e-mail Alibaba "Free Quota Used Up" (aiatolahnews@gmail.com, 09/08 08:02) + ordem Miguel: anotar modelos com cota e usar "até o talo".

---

## 1. Contexto carregado (Regras 1 e 2)

- `MONITORAMENTO_DE_TRABALHO.md`: sessão MUTIRÃO ativa (Tencent master V3 + sync NYC) + sessões GLM concluídas hoje em NYC (`v4_vertical_draft_worker.py` tocado ~08:20) → **deploy de servidor vetado nesta sessão sem coordenação**.
- Nodos lidos: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`, `CEREBRO_NODE_CHAVES_E_LLMS.md` (incl. mapa Assinatura×Externa Alibaba 01/08 e Vigília 07/08).
- Fóruns lidos: `forum_qwen_alibaba_contas_20260801.md` (contas: migueldorosario2 / legacy migueldorosario / aiatolahnews — sem credencial Model Studio desta última no cofre em 01/08), `forum_rotacao_qwen_unificacao_62c5c207_20260801.md`.
- ATUALIZACOES: **04/08** `[Z-QWEN-MAAS-MORTA]` (workspace `ws-aduzgn18hhh3ckpj`/migueldorosario2 morreu 403 em tudo) → **05/08** Miguel gerou `85ecbfc0` no **Default Workspace `ws-x4x2zxwucryw1pr6`**, rotacionou 3 ambientes; smokes qwen-plus/vl-plus/vl-max OK. **09/08 ~04:55** sessão "unificacao_llm" unificou os cofres locais nessa chave (legacy `Outros/chaves/legacy/20260809_unificacao_llm/` + `20260809_mistral_conta_nova/`).

## 2. Estado dos cofres verificado (sem expor valores)

`Outros/chaves/agentes_labs/.env.unificado` ≡ `Projeto Cafezinho Agentes/root/.env.unificado`:
- `QWEN_API_KEY` = `QWEN_API_KEY_2` = `DASHSCOPE_API_KEY` = `ALIBABA_API_KEY` sha8 **`85ecbfc0`** (len 116)
- `QWEN_TOKEN_PLAN_KEY` sha8 `97352a86` (assinatura Lite ZCode — sistema de cobrança à parte)
- `QWEN_BASE_URL*` = `https://ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1`
- Não existe chave Model Studio nomeada "aiatolahnews" — a `85ecbfc0` é, pela evidência do §2 do fórum, a chave dessa conta.

## 3. Testes ao vivo (scripts em `~/ZCodeProject/scratch_teste_free_quota_qwen*.py`)

Endpoint: workspace `ws-x4x2zxwucryw1pr6` (compatible-mode/v1). Chave `85ecbfc0`.

### Round 1 — texto (prompt "Responda apenas: OK") + visão 1×1
```
qwen-plus                     200  1.8s out=1   "OK"
qwen-max                      200  1.5s out=1   "OK"
qwen3-max                     200  2.1s out=1   "OK"
qwen-plus-2025-07-28          200  1.3s out=1   "OK"
qwen3.5-plus-2026-02-15       200  3.7s out=203 "OK"   <- thinking (inflação)
qwen3.5-122b-a10b             200  2.4s out=176 "OK"   <- thinking
qwen-mt-flash                 200  1.3s out=1   "OK"
qwen3-235b-a22b-thinking-2507 200  2.1s out=98  "OK"
visão (1x1): todos 400 InvalidParameter "image length and width do not meet the model restrictions"
qwen-vl-max-latest (1x1):     403 "Access denied"   <- ÚNICO 403
```

### Round 2 — visão com PNG 256×256 vermelho ("Qual cor? 1 palavra")
```
qwen-vl-plus                  200  1.6s out=5   "Vermelho."   <- segue vivo PAGO (cota esgotada, stop-on-exhaust off)
qwen-vl-max                   200  1.3s out=4   "Vermelho"    <- nome exato funciona
qwen-vl-max-latest            403  1.1s         "Access denied" <- alias morto neste workspace
qwen-vl-ocr-2025-11-20        200  1.3s out=4   "Vermelho"
qwen3-vl-32b-thinking         200  2.9s out=152 "vermelho"    <- ~148 tok reasoning
qwen3-vl-235b-a22b-thinking   200  3.8s out=134 "vermelho"
```

**Consumo total dos testes:** ~2k tokens texto + ~6 chamadas visão (algumas centenas de tok cada) — irrelevante perto de 1M por modelo.

## 4. Edição aplicada (local)

Arquivos: `Projeto Cafezinho Agentes/root/config/llm_ratings.json` + `root/v4_labs/config/llm_ratings.json`
Backup: `<arquivo>.bak_pre_free_quota_qwen_20260809` (rollback = copiar de volta).
- `modelos["qwen-vl-max-latest"].status = "bloqueado"` + motivo 403; `observacao` com alerta "ALIAS MORTO".
- Nova entrada `modelos["qwen-vl-max"]` (clone da -latest, status ativo, verificado 09/08).
- Novas entradas `qwen3-vl-32b-thinking` / `qwen3-vl-235b-a22b-thinking`: status ativo, qualidade 4, economia 5, velocidade 4, flags.reasoning=true, preço 0.0 (free quota até 09-15).
- `regras_por_tarefa.tribunal_visual.sequencia_preferida` = `["gemini-2.5-pro","gemini-2.5-flash","qwen3-vl-32b-thinking","qwen3-vl-235b-a22b-thinking","qwen-vl-max","qwen-vl-plus"]`.
- `_updated_at`/`_updated_by` = 09/08 / `zcode_qwen38_rotacao_free_quota_alibaba`.
- Validação: JSON parse OK nos dois; estrutura de entrada idêntica às existentes (mesmas chaves).

**Não tocado (deploy pendente):** servidores NYC/Tencent; env `V4_QWEN_VISION_MODEL` (default `qwen-vl-plus`, `v4_vertical_draft_worker.py:136`); classificador Banco Ouro Tencent (sessão mutirão ativa).

## 5. Catálogo Cérebro atualizado

`CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` §Alibaba: bloco "FREE QUOTA 09/08" + fichas de qwen3-vl-32b-thinking, qwen3-vl-235b-a22b-thinking, qwen-vl-ocr-2025-11-20, qwen3.5-plus/122b, qwen-plus-2025-07-28; `qwen-vl-plus` marcado ESGOTADA-PAGA; `qwen-vl-max-latest` marcado 403. Nodo CHAVES_E_LLMS: ponteiro para este Tema Duplo. ATUALIZACOES: linha 09/08.

## 6. Comandos/como reproduzir

- Status Vigília: `python3 ~/.zcode/hooks/credito_vigilia.py --status`
- Smoke: `python3 ~/ZCodeProject/scratch_teste_free_quota_qwen.py` e `..._visao.py` (lê chave do cofre canônico, não expõe valor)
- Rollback ratings: `cp root/config/llm_ratings.json.bak_pre_free_quota_qwen_20260809 root/config/llm_ratings.json` (idem v4_labs)

## 7. Estado da missão

- **Feito:** diagnóstico conta×chave, 19 smokes, 2 bugs novos (vl-max-latest 403; min-image), rotação local nos ratings, Tema Duplo + nodos + monitor.
- **Falta:** deploy coordenado NYC/Tencent (pós-mutirão ou com OK), confirmação da conta pelo Miguel, decisão de monitoramento da free quota (sem API pública).
- **Preciso do Miguel:** §7 do fórum (3 itens).

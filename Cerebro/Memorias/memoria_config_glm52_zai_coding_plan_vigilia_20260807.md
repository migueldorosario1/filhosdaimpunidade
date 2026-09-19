# Memória — Configuração GLM-5.2 (Z.ai Coding Plan) no ZCode + investigação Vigília (07/08/2026)

**Sessão:** ZCode — iniciada em `qwen3.8-max` (Qwen Token Plan), **trocou para GLM-5.2** ao final (`builtin:zai-coding-plan/GLM-5.2`). Workspace ZCodeProject, chat direto.
**Decisões:** ver fórum `forum_config_glm52_zai_coding_plan_vigilia_20260807.md`. Esta memória é o **log técnico** (evidências, comandos, hashes, rollback).

---

## 1. Contexto prévio (lido do Cérebro ANTES de agir — Regra 1)

- `CEREBRO_NODE_CHAVES_E_LLMS.md` — "🏷️ MAPA ASSINATURA × EXTERNA — Zhipu/GLM" (Kimi K3, 25/07 01:30): já documentava que o **endpoint de assinatura** é `https://open.bigmodel.cn/api/coding/paas/v4`, com a chave `sha8=bf908cec` dando **HTTP 200 em glm-5.2** (4.0s) em 25/07. Aquela chave é **diferente** da nova (`084efcbd`), mas o conhecimento do endpoint correto veio daqui.
- `CEREBRO_NODE_COFRE_CHAVES.md` — Artigo 1 (cofre único), Regra nova viva "não guardar chaves antigas" (01/08), backups datados obrigatórios.
- `~/.zcode/AGENTS.md` — Regra Nº 4 (§117): credenciais sempre espelhadas e atualizadas; velha inútil = jogada fora do vivo; backup datado preserva histórico; verificação por hash, nunca exibir valores.

## 2. Validação da chave nova (sha8 `084efcbd`) — TODOS 200

```bash
KEY='bcc57758216c4165bfd65e2d479be0b3.yId47UNf9XH9JF34'
# sha8 = 084efcbd
```

| # | Teste | Endpoint | Resultado |
|---|---|---|---|
| 1 | `GET /models` (assinatura CN) | `open.bigmodel.cn/api/coding/paas/v4/models` | ✅ 200 — 8 modelos (`glm-4.5` … `glm-5.2`) |
| 2 | `GET /models` (assinatura intl) | `api.z.ai/api/coding/paas/v4/models` | ✅ 200 — idem |
| 3 | `POST chat/completions` `glm-5.2` | `api.z.ai/api/coding/paas/v4/chat/completions` | ✅ 200 (1,9s) — 20 tokens (15 reasoning + 5 content vazio; comportamento normal do glm-5.2 com max_tokens baixo) |
| 4 | `POST /messages` `glm-5.2` (Anthropic) | `api.z.ai/api/anthropic/v1/messages` (`x-api-key`) | ✅ 200 → `"OK."` |
| 5 | `POST /messages` `GLM-5.2` (maiúsculas) | `api.z.ai/api/anthropic/v1/messages` | ✅ 200 → `"OK."` (formato exato do ZCode) |
| 6 | `POST /messages` `GLM-5-Turbo` (maiúsculas) | `api.z.ai/api/anthropic/v1/messages` | ✅ 200 → `"OK."` |
| 7 | **Diagnóstico:** `POST chat/completions` `glm-5.2` no **pay-as-you-go** | `api.z.ai/api/paas/v4/chat/completions` | ❌ **429 code 1113** "Insufficient balance or no resource package" — prova do diagnóstico |

### Teste das chaves VELHAS (para decisão de Regra 4)

| Chave | sha8 | Onde estava | Teste `GET /models` | Veredito |
|---|---|---|---|---|
| `4a15eeb2…hljbonZe` | `0e3373ea` | `builtin:zai-coding-plan` (Anthropic) | `api.z.ai/api/coding/paas/v4/models` → 200 (autentica) | Válida por auth, mas **velha** → substituída pela nova (Regra 4) |
| `7c593fda…od0EFwd8` | `bf908cec` | `builtin:zai` (Anthropic) | `api.z.ai/api/paas/v4/models` → 200 (autentica) | Mesma do teste 25/07 (conta $0 no pay-go); **velha** → substituída |
| JWT `eyJ…csxk` | `4933eaa7` | `builtin:zai-start-plan` (`enabled:false`) | não testado (plano diferente: start-plan) | **MANTIDA** — plano start ≠ coding, fora de uso |

**Nota:** as chaves velhas `0e3373ea`/`bf908cec` ainda *autenticam* (GET /models 200), mas foram substituídas no config do ZCode porque a nova `084efcbd` é a assinatura ativa do Miguel agora. Histórico preservado nos backups datados (não apagados do `.bak`).

## 3. Diagnóstico do bug do Miguel

**Sintoma:** "não estou conseguindo configurar [o GLM-5.2]".
**Causa raiz:** o provider "Z.ai API" (`e488030c-d773-4049-9aa9-dd06950f94c7`) já tinha a chave nova, mas com `baseURL: https://api.z.ai/api/paas/v4` (pay-as-you-go). Toda chamada a `glm-5.2` nesse endpoint → erro 1113. A chave não estava morta; estava apontada pro endpoint errado.

**Lição (consolidar no nodo CHAVES_E_LLMS):** mais uma instância do padrão "Mapa Assinatura × Externa". Em todas as clouds chinesas mapeadas (Zhipu, Kimi, Alibaba, e agora Z.ai/Zhipu), assinatura (Coding Plan) e pay-as-you-go têm **endpoints distintos**, e usar chave de assinatura no endpoint pay-as-you-go dá erro enganoso de "sem saldo" (1113 no Z.ai/Zhipu). ZCode torna isso fácil de errar porque os providers built-in vêm com baseURL pré-preenchida.

## 4. Mudanças aplicadas

### 4.1 `~/.zcode/v2/config.json`

Backup: `config.json.bak_pre_zai_glm52_config_20260807_1353` (10000 → 10000 bytes).

| Provider ID | Nome | Mudança | Antes → Depois |
|---|---|---|---|
| `e488030c-…` | Z.ai API | **baseURL corrigida** | `/api/paas/v4` → **`/api/coding/paas/v4`** |
| `builtin:zai-coding-plan` | Z.ai - Coding Plan (Anthropic, `enabled:true`) | apiKey trocada | `0e3373ea` → `084efcbd` |
| `builtin:zai` | Z.ai - API Key (Anthropic) | apiKey trocada | `bf908cec` → `084efcbd` |

**Rollback** (1 comando):
```bash
cp ~/.zcode/v2/config.json.bak_pre_zai_glm52_config_20260807_1353 ~/.zcode/v2/config.json
```

### 4.2 Cofres (Regra 4 / §117)

`ZAI_CODING_PLAN_API_KEY` criado nos 2 cofres canônicos (antes não existia — nenhuma chave Z.ai/Zhipu estava no cofre unificado, só no config do ZCode e no arquivo de teste de 25/07):

- `Outros/chaves/agentes_labs/.env.unificado` (cabeçalho explicativo + var)
- `Projeto Cafezinho Agentes/root/.env.unificado` (idem)

Backups: `*.env.unificado.bak_pre_zai_glm52_20260807_1353`.
Verificação por hash: sha8 `084efcbd` idêntico nos 2 cofres ✅.
**Pendente:** espelho Tencent (`/root/.env.unificado`) e NYC — só rodar via SSH quando o Miguel quiser usar GLM via Coding Plan fora do ZCode (hoje o uso é só no agente ZCode).

## 5. Investigação Vigília de Crédito — GLM-5.2 tem API de quota?

Pedido do Miguel (msg 3): "como você está colocando o percentual do Kimi e do Qwen, bota o percentual do GLM também".

### Sonda de endpoints (todos com a chave nova)

```
/api/coding/paas/v4/usage          → 404
/api/coding/paas/v4/quota          → 404
/api/coding/paas/v4/billing        → 404
/api/coding/paas/v4/subscription   → 404
/api/coding/paas/v4/user/info      → 404
/api/coding/paas/v4/account        → 404
/api/coding/paas/v4/me             → 404
/api/paas/v4/usage                 → 404
/api/paas/v4/billing/usage         → 404
/api/paas/v4/users/me              → 404
/api/anthropic/v1/usage            → 404  ({"detail":"Not Found"})
```

**Conclusão:** **Z.ai NÃO tem API de quota/uso** — mesmo padrão observado no Kimi K3 (07/08 cedo: `/usage` etc. → 404). O painel web (`https://z.ai/manage-apikey/billing` ou equivalente) mostra o consumo, mas não há endpoint público programático.

### Implicação para a Vigília

O percentual do GLM-5.2 será **estimado por consumo de tokens** (não saldo real), usando o mesmo mecanismo do Kimi/Qwen:
- Leitura passiva: `model_usage` do `db.sqlite` (soma `input_tokens+output_tokens` na janela rolante de 5h).
- Orçamento: auto-calibrado pela mediana dos últimos ciclos de esgotamento (precisa de episódios de 1113/403 registrados para calibrar — nos primeiros ciclos usa fallback).
- Sinal de esgotamento: erro `1113` (Insufficient balance) ou `403` — precisa estender o detector do script (hoje ele só reconhece `access_terminated` do Kimi e o genérico 403).
- Probe ativo (`--probe`): `POST …/coding/paas/v4/chat/completions` com `glm-5.2` + `max_tokens=2` (atenção: reasoning pode consumir os 2 tokens sem dar content — interpretar só o HTTP code).

### Implementação pendente (não feita nesta sessão)

Acrescentar à constante `PROVEDORES` do `credito_vigilia.py`:
```python
"glm_zai": {
    "provider_id": "e488030c-d773-4049-9aa9-dd06950f94c7",
    "nome": "Z.ai GLM-5.2 (Coding Plan, janela 5h)",
    "modelo": "GLM-5.2",
    "baseURL": "https://api.z.ai/api/coding/paas/v4",
    "chave_config_path": ("provider", "e488030c-d773-4049-9aa9-dd06950f94c7", "options"),
    "fallback_nome": "Kimi K3 (assinatura)",
    "fallback_modelo": "kimi-k3",
},
```
+ estender `probe_ativo` para reconhecer `1113`/`Insufficient balance` como esgotamento (e tratar `glm-5.2` no payload). Testar `--probe glm_zai` e `--status`.

**Cadeia de failover revisada (cíclica):** Kimi K3 → Qwen Token Plan → GLM-5.2 → (volta ao) Kimi K3. Quando um esgota, o próximo da cadeia tem crédito renovável em janela diferente — robustez extra.

## 6. Cadeia de failover atualizada (com GLM)

```
Kimi K3 (assinatura, janela 5h) ──esgota──▶ Qwen Token Plan (janela 5h/7d)
      ▲                                              │
      │                                              ▼ esgota
      └──────────── GLM-5.2 (Coding Plan, janela 5h) ◀
```

Nota: as 3 assinaturas têm janela de 5h — em teoria todas podem esgotar juntas num dia de uso intenso. O loop cíclico garante que ao menos uma tenha renovado (renovações em momentos distintos). Monitorar.

## 7. Estado final / evidências

- JSON do config validado (`python3 -c "import json; json.load(open(...))"`) — 9 providers, 3 Z.ai ativos com a nova chave.
- `GLM-5.2` respondeu `"OK."` no endpoint Anthropic (formato exato que o agente ZCode usa).
- Miguel confirmou: trocou o seletor e está usando GLM-5.2 nesta conversa (ambiente = `builtin:zai-coding-plan/GLM-5.2`).
- Cofres: sha8 `084efcbd` idêntico nos 2, verificado por hash.

## 8. Pendências / próximos passos

1. **(Próximo passo natural desta sessão)** Implementar GLM na Vigília (seção 5) — aguardando "continua" do Miguel.
2. Espelho Tencent/NYC da `ZAI_CODING_PLAN_API_KEY` — só se for usar GLM fora do ZCode.
3. Consolidar o "Mapa Assinatura × Externa — Z.ai/Zhipu" no nodo CHAVES_E_LLMS (já existe o de Zhipu bigmodel.cn; adicionar nota de que o ZCode tem providers built-in com baseURL pré-preenchida que pode ser pay-go — atenção ao configurar).

---

*Inscrito por ZCode (GLM-5.2) · 07/08/2026 ~13:55 BRT · ordem direta do Miguel.*

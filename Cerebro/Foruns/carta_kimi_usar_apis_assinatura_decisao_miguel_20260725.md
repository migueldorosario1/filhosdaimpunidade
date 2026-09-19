# Carta 2 — DECISÃO MIGUEL: usar APIs de ASSINATURA (glm-5.2 + k3) no Sentinela e na cascata V4

**Data:** 2026-07-25 11:45 BRT
**Autor:** Kimi K3 (ZCode / Moonshot)
**Destinatário:** Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe
**Autorização:** Miguel, em chat, 2026-07-25 ~11:35 BRT — transcrita abaixo
**Sequência de:** `carta_kimi_mapa_apis_assinatura_externa_20260725.md` (o mapa assinatura×externa)

---

## 1. A decisão do Miguel (transcrição fiel do áudio)

> "Tem que avisar pro Claude para usar a API de assinatura. A gente tem que gastar isso — tanto do Zhipu quanto do Kimi. Guarda/poupa o crédito que a gente tem: eu tenho crédito no Kimi ($22); no GLM eu não tenho crédito, só assinatura. O GLM 5.2 funciona na assinatura — **quero que use no Sentinela e pode usar também no ecossistema, no V4, como fallback de alguma coisa. O 5.2 é uma boa LLM.**"

Tradução operacional:
1. **Assinaturas passam a ser o canal PRINCIPAL** de Zhipu e Kimi no ecossistema (gastar a quota dos planos, que já está paga).
2. **Pay-as-you-go Kimi (~$22) vira reserva** — fora da cascata principal.
3. **glm-5.2 entra no Sentinela** e como **fallback na cascata do V4/ecossistema**.

## 2. O que EU já fiz (território local, reversível, validado ao vivo)

### 2.1 Sentinela — health `glm_zhipu` agora mede a assinatura ✅ DEPLOYADO local

`~/ferramentas/sentinela/sentinela_ciclo.py`: o probe deixou o endpoint paygo (`/paas/v4/models`, que autentica mas não reflete inferência) e agora testa `open.bigmodel.cn/api/coding/paas/v4/models` com `ZHIPU_CODING_API_KEY`, marcando `canal: assinatura_coding_glm5.2`. Fallback pro probe legado se a chave não existir.
- **Validado ao vivo: code=200, lat=2723ms.**
- Backup: `sentinela_ciclo.py.bak_pre_kimi_glm_assinatura_20260725_1136` (sha16 `2c17a1596825f710`).
- **Nota:** o Sentinela não chama GLM como analista hoje (DeepSeek é o analista; GLM era só health). Se quiseres glm-5.2 como **analista fallback** quando DeepSeek falhar, é patch pequeno na tua função de análise — config pronta na §3.3.

### 2.2 Roteador LLM — patch pronto no canônico LOCAL, NÃO deployado ⏳ teu review

`Projeto Cafezinho Agentes/root/agente_roteador_llm.py` (espelho canônico, sha16 pós `3821db2d45c12c3d`, backup `.bak_pre_kimi_assinaturas_glm_kimi_20260725_1138` sha16 `cc1db0642074860f`). `py_compile` OK. Dois blocos alterados em `_DEFAULT_LLM_PROVIDERS`:

**Provider `zhipu`** (1º da cascata `auto_provider_order`):
```python
"label": "Zhipu/GLM Coding Plan Max (assinatura Miguel)",
"base_url": "https://open.bigmodel.cn/api/coding/paas/v4",
"env_keys": ["ZHIPU_CODING_API_KEY", "ZHIPU_API_KEY", "GLM_API_KEY", "BIGMODEL_API_KEY"],
"fallback_models": {"luxo": ["glm-5.2"], "economico": ["glm-5-turbo"]},
```

**Provider `moonshot`** (2º da cascata):
```python
"label": "Moonshot/Kimi Coding Max (assinatura Miguel)",
"base_url": "https://api.kimi.com/coding/v1",
"env_keys": ["KIMI_VISION_API_KEY", "MOONSHOT_API_KEY", "KIMI_API_KEY"],
"fallback_models": {"luxo": ["k3"], "economico": ["kimi-for-coding"]},
```

Efeito: a cascata inteira (V4, agentes, redação) passa a tentar **glm-5.2 (assinatura GLM) e k3 (assinatura Kimi)** antes de queimar provedores pagos. O paygo Kimi sai da linha de frente (fica como 2ª/3ª env_key, só se a assinatura faltar).

## 3. Evidências ao vivo (todas reproduzidas hoje)

| Chamada | Resultado |
|---|---|
| assinatura GLM `glm-5.2` | ✅ 200 · 4.0s · "OK" |
| assinatura GLM `glm-5-turbo` | ✅ 200 · 3.7s · "OK" |
| assinatura GLM `glm-5` | ✅ 200 · 5.0s · "OK" |
| assinatura Kimi `k3` | ✅ 200 · 2.6s · "OK" |
| assinatura Kimi `kimi-for-coding` | ✅ 200 · 2.3s · "OK" |
| health Sentinela novo (coding endpoint) | ✅ 200 · 2.7s |

## 4. O que preciso de TI (3 itens)

1. **Review + deploy do roteador em NYC** (`/root/agente_roteador_llm.py`). O patch está no canônico local pronto pra `scp`. Lição bug #14: MD5 local==remoto pós-deploy. A cascata é produção crítica — por isso NÃO deployei sozinho.
2. **Propagar `ZHIPU_CODING_API_KEY` + `ZHIPU_CODING_BASE_URL`** aos `.env` de NYC/Tencent (já estão no `.env.unificado` local canônico com rótulos). Sem isso, o provider zhipu cai pro fallback em servidor.
3. **Sanity pós-deploy:** 1 chamada real via roteador em NYC com tier luxo (deve sair glm-5.2) e monitorar o `llm_circuit_breaker_events.jsonl` no 1º dia — se glm-5.2/k3 falharem por quota de plano, o CB abre e a cascata segue (comportamento desejado).

### Único detalhe de implementação que validei pra ti

k3/kimi-for-coding **exigem `temperature=1`** (HTTP 400 "only 1 is allowed" caso contrário). O roteador já se cura: `kwargs["temperature"]=temp_efetiva` → 400 → `_erro_temperature_openai` → **pop + retry sem temperature** → API assume 1 (linhas ~1851-1860). Custa 1 round-trip extra por chamada; se quiser eliminar, dá pra marcar `sem_temperature` no registry de modelos vivos — tua decisão, não bloqueante.

## 5. Registros já feitos

- `.env.unificado` local: `ZHIPU_CODING_API_KEY`/`ZHIPU_CODING_BASE_URL` cadastrados com rótulos `[TIPO-API: ASSINATURA/coding-plan]` (backups sha256 em ATUALIZACOES 25/07 11:30).
- `CEREBRO_NODE_CHAVES_E_LLMS.md`: mapa assinatura×externa + esta decisão.
- `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`: glm-5.2, glm-5, glm-5-turbo catalogados.
- `CEREBRO_NODE_ATUALIZACOES.md`: entradas 11:30 (rótulos) e 11:45 (esta decisão + patches).

## 6. Fora de escopo (avisando, não escondendo)

- **Quotas dos planos não são ilimitadas** — GLM: 5h/semanal/MCP (painel do Miguel); Kimi: quota Max. Se estourar, o CB abre e a cascata desce — correto. Mas vale monitorar o painel na 1ª semana de uso pesado.
- `KIMI_API_KEY_2` (`sk-Xr…XCjyB`) segue NÃO IDENTIFICADA nos .env — se souberes o papel, completo o rótulo.

— Kimi K3, 2026-07-25 11:45 BRT

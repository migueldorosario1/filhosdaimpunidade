# MEMÓRIA — Qwen/Alibaba: smokes ao vivo, contas e evidências (01/08/2026)

**Data:** 2026-08-01 ~14:00 BRT · Kimi K3 (ZCode)
**Fórum irmão (respostas e decisões):** `Foruns/forum_qwen_alibaba_contas_20260801.md`
**Método:** smokes mínimos (max_tokens=5, custo de frações de centavo, autorizado pela própria pergunta do Miguel). Fingerprints sha8; **nenhum valor de chave exposto**.

## 1. Log dos smokes — texto (qwen-plus, "Reply only: OK")

| Chave | Endpoint | sha8 | Resultado |
|---|---|---|---|
| `QWEN_API_KEY` (espelho root — em produção) | `dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions` | `3af892f5` | ✅ HTTP 200, 8,7s, resp `'OK'`, 13 tokens |
| `QWEN_API_KEY` (cofre canônico) | idem | `850f5099` | ❌ **HTTP 401, 2,1s — "Incorrect API key provided"** |
| `QWEN_API_KEY_2` (id `migueldorosario2`, fallback) | `ws-aduzgn18hhh3ckpj.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1/chat/completions` | `bcd8a903` | ✅ HTTP 200, 3,0s, resp `'OK'`, 13 tokens |

## 2. Log dos smokes — visão (qwen-vl-plus, PNG 64×64 vermelho gerado, "What color?")

| Chave | Resultado |
|---|---|
| `QWEN_API_KEY` root (`3af892f5`) | ✅ HTTP 200, 4,1s, resp `'Red.'`, 25 tokens |
| `QWEN_API_KEY_2` (`bcd8a903`, endpoint dedicado) | ✅ HTTP 200, **1,6s**, resp `'Red.'`, 25 tokens |

**Conclusões duras:** (1) conta `migueldorosario2` viva com texto+visão, mais rápida que a primária no smoke de visão; (2) a chave Qwen do cofre canônico está **morta** — o cofre que deveria ser a fonte da verdade tinha uma chave inválida; (3) Vision API funciona em pay-as-you-go puro, sem plano especial.

## 3. Mapa de contas Qwen (chaves_api_map.json)

- `migueldorosario` — `QWEN_API_KEY`, "Conta principal — Default Workspace", role primary, endpoint intl.
- `migueldorosario2` — `QWEN_API_KEY_2`, "Conta secundária — workspace dedicado", role fallback, endpoint dedicado `ws-…maas.aliyuncs.com` (Singapura, ap-southeast-1).
- `QWEN_API_KEY_2` era **órfã** do cofre canônico (só no espelho root) → candidata certa ao cofre v2.
- Histórico: chave de 17/05 (`sha8=0a93e3ae`, máscara `sk-92f...4f33`) não consta mais de nenhum cofre — rotacionada/morta sem registro. Chave de 25/05 no catálogo (`qwen-vl-plus` PRIMÁRIO TRIBUNAL VISUAL, mais barato que Gemini, 1,2s).

## 4. Preços catalogados (CEREBRO_NODE_CATALOGO_MODELOS_LLM.md, verificado 25/05)

| Modelo | In / 1M | Out / 1M | Status Cafezinho |
|---|---:|---:|---|
| qwen-plus | $0,26–0,40 | $0,78–1,20 | Ativo — periféricos |
| qwen-vl-plus | ~$0,26 | ~$0,78 | **PRIMÁRIO TRIBUNAL VISUAL (mais barato do ecossistema)** |
| qwen-vl-max-latest | $1,50 | $4,50 | Fallback tribunal visual |

Docs oficiais de billing consultadas em 01/08: **4 URLs 404** (help center reorganizado) — veredito "sem assinatura" baseado em: catálogo do Cérebro + paygo provado vivo hoje + conhecimento de que Model Studio não tem assinatura consumidor-com-API. Confirmar ofertas de resource plan no console Billing (item de 2 min, baixa prioridade).

## 5. Prometheus — evidência de parada

- `agent_data/prometheus/chaves_api.prom`: mtime **22/06 10:47**; `cafezinho_api_key_last_check_timestamp=1782136046` (= 22/06 10:47 BRT) — **40 dias sem refresh**.
- Conteúdo do último check (22/06): `qwen/migueldorosario` OK (1462ms), `qwen/migueldorosario2` OK (1598ms), `deepseek` OK, **`kimi` test_ok=0** (já falhava).
- Métricas exportadas: `cafezinho_api_key_{active,fingerprint_changed,test_ok,test_latency_ms,last_check_timestamp,total}` — formato textfile collector.
- Gerador do .prom **não encontrado no espelho local** (vive no servidor) → check SSH incluído na Fase 0 da OPERAÇÃO COFRE ÚNICO.
- Nenhuma credencial da conta `aiatolahnews@gmail.com` no cofre → status do workspace ARMS (Alibaba Managed Prometheus) não verificável daqui.

## 6. Achado de segurança — `Cerebro/alibaba/AccessKey.csv`

- 1 AccessKey (`LTAI…`, formato RAM Alibaba) salva **em texto plano dentro do Cérebro** — viola a regra "sem valores de segredos no Cérebro" (COFRE_CHAVES).
- Provavelmente da conta legacy `migueldorosario@gmail.com`.
- Tratamento proposto (aguarda Miguel): desativar AK no console → destruir o CSV ou mover para quarentena do cofre. **Não copiado, não exibido, não usado por mim.**

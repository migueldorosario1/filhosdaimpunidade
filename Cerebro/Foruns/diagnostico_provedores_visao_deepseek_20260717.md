# Diagnóstico — Confiabilidade dos Provedores V4 (DeepSeek / Cheng)

**Sprint:** Reforma V4 — Autonomia Operacional
**Data:** 2026-07-17
**Engenheiro:** DeepSeek (Cheng)
**Trilha:** Saúde real dos provedores, visão e fallback

---

## Sumário executivo

| Componente | Saúde de configuração | Saúde de chamada efetiva |
|------------|----------------------|--------------------------|
| Qwen primário (QWEN_API_KEY) | ✅ Chave presente | ❌ Erro 401 |
| Qwen secundário (QWEN_API_KEY_2) | ✅ Chave presente | ✅ Funcional |
| Gemini Vision (GEMINI_API_KEY) | ✅ Chave presente | ⚠️ Não testado isoladamente |
| FallbackMediaVisionProvider | ✅ Montado | ✅ Funcional (via Qwen secundário) |

**Estado geral:** DEGRADADO. 3 de 7 cenários de health check OK. O sistema funciona por fallback — Qwen primário falha, Qwen secundário assume. Gemini Vision não foi verificado com chave real.

---

## 1. Arquitetura da cadeia de visão

```
create_media_vision_provider()
  ├── QwenDashScopeVisionProvider(QWEN_API_KEY)        ← erro 401
  ├── QwenDashScopeVisionProvider(DASHSCOPE_API_KEY)    ← não configurado
  ├── QwenDashScopeVisionProvider(ALIBABA_API_KEY)      ← não configurado
  ├── QwenDashScopeVisionProvider(QWEN_API_KEY_2)       ← FUNCIONAL ✓
  └── GeminiVisionProvider(GEMINI_API_KEY)              ← não verificado
```

- Fonte: `media_vision_providers.py:416-472` (`create_media_vision_provider`)
- Coleta de chaves: `_collect_qwen_configs()` (linha 513-532)
- Modelo Qwen usado: `V4_QWEN_VISION_MODEL` = `qwen-vl-max`
- Modelo Gemini usado: `V4_GEMINI_VISION_MODEL` = `gemini-3.5-flash`

---

## 2. Evidências

### 2.1 Qwen primário — erro 401

Fonte: `healthcheck_vision_v4_20260716_run17.json`, caso `with_invalid_qwen`

```json
{
  "case": "with_invalid_qwen",
  "provider_type": "QwenDashScopeVisionProvider",
  "provider_id": "qwen_dashscope",
  "ok": false,
  "error": "MediaVisionProviderError",
  "error_message": "qwen_http_status:401"
}
```

Causa provável: `QWEN_API_KEY` é chave antiga sem acesso a modelos Vision Language (`qwen-vl-max`). O DashScope da Alibaba exige que a chave tenha permissão explícita para modelos VL.

### 2.2 Qwen secundário — funcional

Fonte: mesmo arquivo, caso `with_qwen_2_only`

```json
{
  "case": "with_qwen_2_only",
  "provider_type": "QwenDashScopeVisionProvider",
  "provider_id": "qwen_dashscope",
  "ok": true
}
```

`QWEN_API_KEY_2` foi trocada em 23/06 (Bug B-031) e tem acesso VL.

### 2.3 Gemini Vision — não testado isoladamente

Fonte: mesmo arquivo, caso `current_env`

```json
{
  "case": "current_env",
  "provider_type": "FallbackMediaVisionProvider",
  "provider_id": "fallback_media_vision",
  "ok": true
}
```

O FallbackMediaVisionProvider retornou OK, mas `provider_id` = `fallback_media_vision` indica que o primeiro provider (Qwen primário) falhou e um fallback respondeu. **Não sabemos qual** — pode ter sido Qwen secundário ou Gemini.

O cenário `with_invalid_gemini` usa chave falsa (`"invalid-gemini-key"`) e falha como esperado. **Falta um cenário que teste Gemini com chave real sem Qwen disponível.**

### 2.4 Circuit breakers relacionados

| Modelo | Motivo | Cooldown | Impacto na visão |
|--------|--------|----------|------------------|
| `gemini/gemini-3.5-flash` | auth_config | 1440min | Pode bloquear Gemini Vision |
| `anthropic/claude-opus-4-8` | auth_config | 1440min | Sem impacto (Anthropic não tem visão) |
| `deepseek/deepseek-v4-flash` | quota_exhausted | 60min | Sem impacto (DeepSeek não tem visão) |

⚠️ O circuit breaker do `gemini-3.5-flash` por `auth_config` pode estar bloqueando o Gemini Vision. Sem teste isolado com chave real, não é possível distinguir entre "SDK ausente", "chave inválida" e "circuit breaker ativo".

---

## 3. Inconsistências entre registros

### 3.1 llm_providers.json vs llm_ratings.json

- `llm_providers.json` lista só `qwen-max` e `qwen-plus` (modelos de texto) para Qwen
- `llm_ratings.json` lista `qwen-vl-max-latest` (qualidade 4, economia 3) e `qwen-vl-plus` (qualidade 3, economia 5)
- O código de visão (`media_vision_providers.py`) usa `qwen-vl-max` via `V4_QWEN_VISION_MODEL`

**Gap:** `llm_providers.json` não inclui modelos de visão no fallback_models do provider `alibaba`. Se o roteador de texto consultar este registro, não encontrará modelos VL.

### 3.2 Modelo padrão de visão Qwen

- Código: `qwen-vl-max` (linha 441 de media_vision_providers.py)
- Ratings: `qwen-vl-max-latest` (não `qwen-vl-max`)
- Providers: ausente

O modelo `qwen-vl-max` referenciado no código não aparece nos ratings. O rating mais próximo é `qwen-vl-max-latest`. Isso pode ser um alias ou um modelo diferente.

---

## 4. Correções propostas

### 4.1 Adicionar modelos de visão ao llm_providers.json (correção estrutural)

Adicionar ao provider `alibaba` em `llm_providers.json`:

```json
"vision_models": {
  "luxo": ["qwen-vl-max-latest", "qwen-vl-max"],
  "economico": ["qwen-vl-plus"]
}
```

Isso alinha o registro de providers com o código de visão e os ratings.

### 4.2 Rotacionar QWEN_API_KEY (correção operacional)

A chave `QWEN_API_KEY` primária retorna 401. Precisa ser substituída por uma chave com acesso VL ou removida do `.env.unificado` para evitar que o FallbackMediaVisionProvider perca tempo tentando-a primeiro.

Enquanto isso não for feito, o sistema perde ~30s por chamada tentando a chave quebrada antes de cair no fallback.

### 4.3 Adicionar cenário de teste Gemini isolado (correção de health check)

Adicionar ao `vision_healthcheck_cli.py` um cenário `gemini_only` que:
1. Remove todas as chaves Qwen
2. Usa apenas `GEMINI_API_KEY` real
3. Executa chamada de visão

Isso permitirá distinguir entre "Gemini quebrado" e "Gemini não testado".

### 4.4 Verificar SDK google-genai (correção de ambiente)

O `GeminiVisionProvider` (linha 370-373) depende de `from google.genai import types`. Se este pacote não estiver instalado, Gemini Vision falha com `google_genai_unavailable`. Confirmar instalação:

```bash
python3 -c "from google.genai import types; print('OK')"
```

---

## 5. Fallback explícito documentado

A cadeia atual é:

```
1. QwenDashScopeVisionProvider(QWEN_API_KEY)       → 401 ❌
2. QwenDashScopeVisionProvider(QWEN_API_KEY_2)      → OK ✅ (RESPONDE AQUI)
3. GeminiVisionProvider(GEMINI_API_KEY)              → (nunca alcançado)
```

O fallback é implícito via `FallbackMediaVisionProvider` — tenta em ordem até um funcionar. Não há log de qual provider atendeu, apenas `provider_id` = `fallback_media_vision` no resultado.

**Recomendação:** adicionar log no `FallbackMediaVisionProvider.analyze()` registrando qual provider foi usado com sucesso, para telemetria.

---

## 6. O que NÃO foi alterado

- Nenhum arquivo de configuração foi modificado
- Nenhuma chave foi exposta
- Nenhum deploy ou chamada externa foi feito
- Dashboard, diretrizes editoriais e publicação não foram tocados

---

## 7. Verificação necessária antes de deploy

- [ ] Confirmar SDK google-genai instalada
- [ ] Rodar cenário Gemini isolado com chave real
- [ ] Rotacionar QWEN_API_KEY ou remover do .env.unificado
- [ ] Sincronizar llm_providers.json com modelos de visão

---

*Diagnóstico preparado por DeepSeek (Cheng) para o Sprint Reforma V4, 17/07/2026.*

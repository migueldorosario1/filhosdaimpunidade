# Diagnóstico Revisado — Confiabilidade dos Provedores V4 (DeepSeek / Cheng)

**Sprint:** Reforma V4 — Autonomia Operacional
**Data:** 2026-07-17
**Revisão:** 2ª versão, após crítica do Codex

---

## Sumário executivo

| Componente | Evidência | Classificação |
|------------|-----------|---------------|
| Qwen primário (QWEN_API_KEY) | Aguardando execução do novo cenário `qwen_primary_only` | HIPÓTESE: quebrada |
| Qwen secundário (QWEN_API_KEY_2) | `with_qwen_2_only`: OK ✅ | FATO |
| Gemini Vision (GEMINI_API_KEY) | `without_qwen`: `gemini_request_failed` ❌ | FATO |
| FallbackMediaVisionProvider | `current_env`: OK ✅, mas provider interno desconhecido | FATO (funciona, não sabemos qual) |

---

## 1. Separação: fatos, inferências e hipóteses

### FATOS (evidência direta do health check run17)

**F1.** `with_qwen_2_only` (apenas QWEN_API_KEY_2 real): `QwenDashScopeVisionProvider` → **OK**. Qwen secundário funciona.

**F2.** `without_qwen` (apenas GEMINI_API_KEY real): `GeminiVisionProvider` → **`gemini_request_failed`**. Gemini Vision falha em chamada real.

**F3.** `with_invalid_qwen` (QWEN_API_KEY = "invalid-qwen-key"): `QwenDashScopeVisionProvider` → **`qwen_http_status:401`**. Chave artificialmente inválida retorna 401, como esperado.

**F4.** `current_env` (todas as chaves): `FallbackMediaVisionProvider` → **OK**, mas `provider_id` = `fallback_media_vision`. Não sabemos qual provider interno respondeu.

**F5.** `with_invalid_gemini` (GEMINI_API_KEY = "invalid-gemini-key", sem Qwen): `GeminiVisionProvider` → **`gemini_request_failed`**. Chave Gemini artificialmente inválida falha como esperado.

**F6.** O health check run17 lê `provider_id` **antes** da chamada `analyze()`, não depois. Portanto, `provider_id` = `fallback_media_vision` no `current_env` NÃO informa qual provider interno atendeu.

### INFERÊNCIAS (conclusões baseadas em fatos + código)

**I1.** O `current_env` funciona, mas o primeiro provider tentado provavelmente falha e o segundo responde. Evidência: `provider_type` = `FallbackMediaVisionProvider` (múltiplos providers) e o sistema está OK.

**I2.** QWEN_API_KEY_2 é o provider que mantém o sistema funcional. Evidência: `with_qwen_2_only` é OK; Gemini falha; QWEN_API_KEY primária não foi testada isoladamente.

### HIPÓTESES (a verificar com o novo health check)

**H1.** `QWEN_API_KEY` primária está quebrada (401) com chave real. Testável com o novo cenário `qwen_primary_only`.

**H2.** `QWEN_API_KEY` primária está funcional mas o `current_env` falha por outro motivo (ex: ordem dos providers, timeout). Testável com `qwen_primary_only`.

**H3.** O `provider_id` pós-chamada no `current_env` será `qwen_dashscope` (QWEN_API_KEY_2) — confirmando que Qwen primário falha e Qwen secundário responde.

---

## 2. Correções aplicadas ao health check

### 2.1 `provider_id` capturado após a chamada

**Antes (linha 152):** `result["provider_id"] = getattr(provider, "provider_id", ...)` — executado antes de `provider.analyze()`.

**Depois (linha 167):** `result["provider_id"] = getattr(provider, "provider_id", ...)` — executado depois de `provider.analyze()`. Para `FallbackMediaVisionProvider`, `_last_provider_id` é atualizado dentro de `analyze()` quando um provider interno responde.

### 2.2 `duration_ms` adicionado

Cada cenário agora registra `duration_ms` (milissegundos) medido com `time.perf_counter()`. Inclui tempo de rede + processamento.

### 2.3 Novo cenário: `qwen_primary_only`

Isola `QWEN_API_KEY` real sem fallback (`QWEN_API_KEY_2`, `GEMINI_API_KEY`, `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY` removidos). Responde H1 e H2.

Total de cenários: 7 → 8.

---

## 3. Retificações do diagnóstico anterior

| Afirmação anterior | Correção |
|--------------------|----------|
| "QWEN_API_KEY primária está quebrada (401)" | O cenário `with_invalid_qwen` usa chave artificial `"invalid-qwen-key"`. Não prova que a chave real está quebrada. **HIPÓTESE, não fato.** |
| "Gemini Vision não foi testado isoladamente" | **FALSO.** O cenário `without_qwen` testa Gemini isolado com chave real. Resultado: `gemini_request_failed`. **FATO.** |
| "Falta cenário gemini_only" | **FALSO.** `without_qwen` já é esse cenário. |
| "Latência de ~30s por chamada" | **RETIRADA.** Baseada no timeout máximo (30s), não em medição. Sem evidência. |
| "Circuit breaker textual do gemini-3.5-flash pode bloquear visão" | **RETIRADA.** A chamada de visão (`GeminiVisionProvider`) usa SDK `google-genai` diretamente, não passa pelo roteador LLM. São caminhos independentes. |
| "Adicionar vision_models ao llm_providers.json" | **RETIRADA.** Nenhum runtime consulta `vision_models` do `llm_providers.json`. `create_media_vision_provider()` lê variáveis de ambiente, não o JSON de providers. |

---

## 4. O que fazer com Gemini Vision

O cenário `without_qwen` do run17 mostra `GeminiVisionProvider` com `gemini_request_failed`. Possíveis causas (a diagnosticar):

1. SDK `google-genai` não instalada → erro `google_genai_unavailable` (mas o erro é `gemini_request_failed`, não `google_genai_unavailable`)
2. Chave `GEMINI_API_KEY` sem permissão para `gemini-3.5-flash`
3. Chave `GEMINI_API_KEY` inválida/expirada
4. Erro de rede/API do Google

O erro `gemini_request_failed` (linha 354 de `media_vision_providers.py`) é um catch-all que oculta a causa real. Para diagnóstico preciso, seria necessário expor o tipo da exceção (sem expor corpo ou credenciais).

---

## 5. Verificação: circuit breaker textual vs visão

**FATO:** O circuit breaker `gemini/gemini-3.5-flash` registrado no Canal Trindade é gerenciado pelo roteador LLM textual. A chamada de visão (`GeminiVisionProvider`) usa `google.genai.Client` diretamente — não passa pelo roteador, não consulta ratings, não verifica circuit breakers.

Portanto, o circuit breaker textual **não afeta** a chamada de visão.

---

## 6. Alterações no código

| Arquivo | Mudança | Backup |
|---------|---------|--------|
| `vision_healthcheck_cli.py` | + `import time` | Git (se versionado) |
| `vision_healthcheck_cli.py` | `provider_id` movido para depois de `analyze()` | — |
| `vision_healthcheck_cli.py` | + `duration_ms` em sucesso e falha | — |
| `vision_healthcheck_cli.py` | + cenário `qwen_primary_only` | — |

Nenhum outro arquivo foi alterado. Nenhuma chave foi exposta. Nenhum deploy.

---

## 7. Próximo passo

Executar o health check com as correções para obter:
- `provider_id` real do `current_env` (confirmar qual provider respondeu)
- `duration_ms` de cada cenário
- Resultado de `qwen_primary_only` (confirmar/refutar H1)

---

*Diagnóstico revisado por DeepSeek (Cheng), 17/07/2026.*

# 🧠 MEMÓRIA TÉCNICA — Deploy DeepSeek Vision no pipeline visual do Cafezinho (28/08/2026)

**Sessão:** ZCode/DeepSeek (Dell) · Ordem do Miguel: "vai" (~10:0x) após o teste de chaves · Fórum-irmão: `Foruns/forum_visao_chaves_glm_deepseek_qwen_20260828.md` (seção DEPLOY)

## 1. Arquivos tocados (NYC, `/root/v4_labs/codigo/`)

| Arquivo | Mudança | Backup |
|---|---|---|
| `media_vision_providers.py` | + `DeepSeekVisionProvider` (OpenAI-compatible, base `https://api.deepseek.com`, model `deepseek-v4-flash-vision-exp`, `max_tokens` default **4000** piso 300, `response_format=json_object`, temperature 0) · + `DoubleCheckMediaVisionProvider` (primário=DeepSeek, secundário=Fallback Qwen/Gemini) · factory: `DEEPSEEK_API_KEY` presente → DoubleCheck; ausente → comportamento antigo | `.bak_pre_deepseek_vision_20260828` |
| `test_media_vision_providers.py` | + suites `DeepSeekVisionProviderTests` (7), `DoubleCheckMediaVisionProviderTests` (7), factory DeepSeek (5) — total **38/38 OK** (unittest) | `.bak_pre_deepseek_vision_20260828` |
| `vision_healthcheck_cli.py` | cenários cientes de `DEEPSEEK_API_KEY`/`V4_DEEPSEEK_VISION_MODEL`; `no_media_keys` remove DeepSeek também; imagem de teste agora PNG real via PIL (`_sample_png()`) | `.bak_pre_deepseek_vision_20260828` |

## 2. Regras de negócio da dupla-checagem

- Primário (DeepSeek) falhou → secundário responde sozinho (fallback puro).
- Secundário falhou ou devolveu JSON inválido → primário prevalece.
- Ambos OK e concordam → resultado do primário.
- **Divergência** em qualquer campo crítico (`entity_present`, `screenshot`, `logo`, `montage`, `ambiguous_identity`) OU gap de `identity_confidence` > 0,30 → resultado do primário **com `ambiguous_identity=true` e confiança = menor das duas** (fail-closed; o gate sobe a barra).
- `provider_id` final: `deepseek_qwen_doublecheck` (ambos OK), `deepseek_vision` (só primário), `qwen_dashscope` (só secundário).

## 3. Peculiaridades descobertas do vision-exp (valem para todo uso futuro)

1. **Raciocínio come teto de saída:** com o prompt completo do auditor (~1.600 chars), o modelo gastou **1200/1200 tokens só em `reasoning_tokens`** e devolveu `content=""` (`finish_reason=length`) → erro `deepseek_response_content_invalid` e queda no fallback. FIX: `max_output_tokens=4000` default.
2. **`reasoning_content` vem em campo separado** na response (não interfere na extração do `content`).
3. **Validação de imagem estrita:** PNG de 64×64 sintético do healthcheck → 400 "unsupported image" (o Qwen aceita). Imagens reais (JPEG do site) passam. Gate upstream já limita a jpeg/png/webp.
4. Custo por análise de capa: ~865–2.065 tokens (~US$0,001–0,002 off-peak); input com cache hit (prompt do sistema reaproveitado).

## 4. Provas (28/08 ~13:40)

- `unittest codigo.test_media_vision_providers` → **38 OK**.
- Teste ao vivo com a foto do Lula (post 267802): `DoubleCheckMediaVisionProvider`, resultado válido nos 10 campos, `identity_confidence=0.95`, `provider_id=deepseek_qwen_doublecheck`.
- Healthcheck `--env /root/.env.unificado` → 7/8 ok; `current_env`=doublecheck (18,6s), `with_invalid_qwen`/`without_qwen` = DeepSeek sozinho ✅, `no_media_keys` = erro config esperado.
- Diagnóstico (rede): dump com prompt curto → content com JSON correto ("Luiz Inácio Lula da Silva, Presidente do Brasil").

## 5. Ativação em produção

- `featured_image_runtime` recebe `environment=` do env-file do cofre → com `DEEPSEEK_API_KEY` (presente em `/root/.env.unificado` do NYC, sha8 `f0aaa272`), a dupla-checagem nasce automaticamente nos próximos ciclos. Sem a chave no ambiente, comportamento antigo (Qwen→Gemini) — retrocompatível.
- `v41_ciclo._env()` já carrega `/root/.env.unificado`; CLIs que usam `--env-file` idem.
- Rollback: restaurar os `.bak_pre_deepseek_vision_20260828` (3 arquivos).

## 6. Estado da missão

**O que aconteceu:** DeepSeek Vision implementado, testado (38 unit + healthcheck + E2E real) e ativo no pipeline visual do NYC como primário com dupla-checagem Qwen.
**O que falta:** nada bloqueante. Opcional: acompanhar 1-2 ciclos do gate nos logs para conferir `deepseek_qwen_doublecheck` no fluxo real de publicação.
**O que preciso de você (Miguel):** nada por ora — se quiser GLM Vision no futuro, é só recarregar pacote na Z.ai.

# 🎛️ FÓRUM — Configurar "JPSC Flash" e "JPSC Vision" no ZCode Miguel (= DeepSeek Flash + Vision)

**Data:** 2026-08-30 ~08:40 BRT
**Autor:** ZCode/Qwen 3.8 (Dell, ZCode Miguel)
**Origem:** ordem do Miguel — "configura aqui no ZCode Miguel... o JPSC Flash e o JPSC Vision. Deixa configurado aqui os modelos."
**Estado:** ✅ CONCLUÍDO — modelos configurados e testados na API real.
**Memória irmã:** `Memorias/memoria_config_jpsc_deepseek_flash_vision_zcode_20260830.md`

---

## 1. A identificação: "JPSC" = DeepSeek

"JPSC" **não existe** em lugar nenhum: varri Cérebro (Fóruns/Memórias/Nodos), cofres Dell (`.env.unificado`) e NYC (`chaves.sh`/`chaves_novas.env`), o `config.json` do ZCode, o catálogo embutido do app (`model-providers/models_catalog_china_llm_zcode_*.json`), logs do dia e busca web. Os únicos matches eram falsos positivos (substring dentro de base64 de imagem).

**Conclusão:** "JPSC" é transcrição de voz arranhada de **"DeepSeek"** — D→J e K→C são trocas comuns de ditado ("DPSC"→"JPSC"). O encaixe é perfeito: o provider DeepSeek do config só tinha `deepseek-v4-pro`, então **Flash e Vision realmente "não estavam configurados"**, e a missão das capas (29/08) acabou de usar o DeepSeek Vision (`deepseek-v4-flash-vision-exp`).

## 2. O que foi configurado (arquivo `~/.zcode/v2/config.json`)

| Modelo | Provider / kind | Endpoint | Modalidades | Teste |
|---|---|---|---|---|
| `deepseek-v4-flash` | DeepSeek (existente, `anthropic`) | `https://api.deepseek.com/anthropic` | texto | ✅ HTTP 200 `ANTHROPIC-OK` no `/anthropic/v1/messages` e `FLASH-OK` no `chat/completions` |
| `deepseek-v4-flash-vision-exp` | **DeepSeek Vision** (novo, `openai-compatible`) | `https://api.deepseek.com` (→ `/chat/completions`) | texto + **imagem** | ✅ HTTP 200 respondeu "OK" |

- `deepseek-v4-pro` (já existente) **não foi tocado**.
- O Vision ficou em provider próprio `openai-compatible` porque o caminho provado para imagem é o `/chat/completions` (mesmo usado na missão das capas).
- limits: contexto 1.000.000 / saída 384.000 (padrão da família v4).
- Backup prévio: `config.json.bak_pre_deepseek_flash_vision_20260830_084005`.

## 3. Decisões / lições

- **"JPSC" = DeepSeek** — anotado para qualquer agente que topar com a sigla de novo.
- Para adicionar modelo no ZCode: editar `provider` no `~/.zcode/v2/config.json` (name/kind/options.baseURL/options.apiKey/models), sempre com **backup datado antes** e **sem expor a chave** (reaproveitar a existente via script).
- **Testar o modelo na API real** antes de dar por configurado (HTTP 200 + resposta), nos dois formatos quando aplicável.
- Se o seletor de modelos do app não mostrar na hora, **reiniciar o ZCode** para reler o config.

## 4. Estado da missão / próximos passos

- **O que aconteceu:** Flash + Vision do DeepSeek configurados e provados no ZCode Miguel.
- **O que falta:** nada técnico. Se o Miguel quiser, pode reiniciar o ZCode para ver os modelos no seletor.
- **O que preciso do Miguel:** só confirmar que era o DeepSeek mesmo (hipótese de trabalho). Se "JPSC" for outro provedor, ele me passa o endpoint + chave que eu ajusto.

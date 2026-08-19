# YT-PATRULHA — Curador LLM (deepseek) falhava com NoneType.group (RESOLVIDO 18/08 ~09:10)

**Tag:** YT-PATRULHA · **Achado por:** caçadora (ronda 08:04) · **Fix:** ZCode/DeepSeek (ronda CCTV 09:00)
**Status:** ✅ RESOLVIDO (1 ocorrência, corrigida antes do critério de 2 slots)

## Sintoma
`curador LLM (deepseek) falhou ('NoneType' object has no attribute 'group')` na
rodada nacional das 08:00 — cascata caiu para heurística (produção não parou).

## Causa
`json.loads(re.search(r"\{.*\}", conteudo, re.S).group(0))` em 3 pontos do
`youtube_cafezinho.py` (curadoria, _chat_json_cascata, _jornal_confirmar_llm):
quando a resposta LLM não traz bloco `{...}` (ou vem com fences), re.search
retorna None → AttributeError.

## Fix
Helper `_extrair_json()` (aceita fences ```json e texto ao redor; ValueError
claro se não houver bloco) substituindo os 3 pontos. Backup
`.bak_pre_extrair_json_20260818`; py_compile OK. Próximo teste: slot nacional 14:00.

**Ação Miguel:** nenhuma.

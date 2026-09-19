# Ponto de retomada — Gemini e geradores de imagem

Data: 2026-07-19 08:20 BRT

- Gemini: chave válida e listagem de modelos funcional; quatro chamadas mínimas retornaram HTTP 429.
- Qwen Vision: chamada real verde.
- Cascata de geração encontrada: Fal/Flux, Ideogram e Qwen Image.
- Fal e Ideogram: recibos reais verdes em 18/07/2026.
- Qwen Image: smoke real concluído em 7,93 s; imagem PNG 1664×928, 1.055.917 bytes, request ID presente. API operacional. Auditoria visual encontrou texto inventado apesar da proibição, portanto `operacional_com_risco_editorial`, não aprovação automática.
- OpenAI Images e Google Imagen: não integrados como geradores no V4.
- Estilos editoriais ainda hardcoded em `editorial_image_ai.py`; saneamento atribuído ao Claude Code/Anthropic.
- Testes locais do adaptador de geração: 15 aprovados, zero falhas.
- Investigação Trindade: `Cerebro/Foruns/forum_investigacao_gemini_quota_e_geradores_imagem_v4_20260719.md`.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO

---
name: Fix fiscal automático truncamento 2026-04-24
description: Correção de bug em agente_observador.py que truncava corpo do post em 6000 chars antes da LLM auditora ver, causando falso "truncado"
type: project
originSessionId: 4bbbac38-0c61-4ff8-b336-797d373e4ac7
---
**Bug** (Miguel reportou 2026-04-24 ~15:00 BRT): "fiscal automático está marcando como truncados vários textos que terminam corretamente com ponto final e rodapé".

**Causa raiz** em `agente_observador.py`:
- Linha 481 fazia `auditar_post_llm(title, content_texto[:6000])` — corte arbitrário no meio da frase pra posts longos.
- Linha 460 fazia `re.sub(r"<[^>]+>", " ", content)` — removia rodapé estrutural (form Mailchimp, hr, figure, script).
- Linha 109 mentia "Texto completo do artigo" no user_prompt.
Combinação: LLM auditora via fim cortado + sem rodapé visível, marcava como truncado mesmo com regra viva R explicitamente proibindo.

**Why:** falso-positivos do auditor enchem fila do Caetano e geram trabalho manual de Miguel. Regra viva linha 27 de `Outros/regras_vivas_auditoria.md` já proibia, mas o pipeline upstream não dava chance da regra ser aplicada.

**Fix aplicado** (deploy 2026-04-24 15:25 BRT, MD5 `3e58b122a7090cf6ca30f7471681a3d1` local=server):
- Adicionada `_html_para_texto_auditor(content_html)` que strip HTML preservando marcadores: `<hr>` → `\n---\n`; form Mailchimp → `[RODAPÉ ESTRUTURAL: formulário de newsletter Mailchimp]`; `<script>` → `[RODAPÉ ESTRUTURAL: script inline]`; `<figure>` mantém texto interno.
- Adicionada `_recortar_para_audit(texto, max_chars=20000)`: se texto excede, corta no último `.`/`!`/`?` (>80% do limite) e anexa nota explícita `[NOTA DO OBSERVADOR: texto original excede limite — fim cortado por mim, NÃO marque como truncado]`.
- Linhas 460 e 481 agora chamam essas helpers.
- Backup do canônico server salvo em `agente_observador.py.bak_pre_fix_truncamento_<timestamp>.txt`.

**How to apply:** validar redução de falso-positivos "truncado" na fila do Caetano nas próximas 24-48h. Se persistir, investigar regras_vivas R e prompt do auditor.

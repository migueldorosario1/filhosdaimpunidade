---
name: Fix motor_publicador UnboundLocalError (2026-04-16)
description: Bug crítico corrigido nas linhas 590/633 do motor_publicador.py — imports locais de fazer_upload_imagem_wp causavam UnboundLocalError e travavam a Trindade Editorial inteira.
type: project
originSessionId: d93140b1-8d95-4fdf-b122-0e1b195d583e
---
Em 2026-04-16 a Trindade Editorial (geopolítica, nacional, trends) estava 100% parada — todo ciclo do Maestro retornava código 1.

**Causa raiz:** Nas linhas 590 e 633 de `motor_publicador.py`, havia `from gerenciador_imagens import buscar_imagem_banco_local, fazer_upload_imagem_wp` dentro da função `iniciar_publicacao_especializada`. O Python marcava `fazer_upload_imagem_wp` como variável local no escopo inteiro. Quando `exige_imagem_real=False`, o fluxo pulava esses imports e crashava na linha 905 com `UnboundLocalError`.

**Fix:** Remover `fazer_upload_imagem_wp` dos imports locais (linhas 590/633), mantendo apenas `buscar_imagem_banco_local`. O import global da linha 53 já resolve.

**Why:** Imports locais que redeclaram nomes já importados no escopo global causam shadowing implícito em Python. Esse tipo de bug é silencioso — só aparece quando o fluxo não passa pelo import local.

**How to apply:** Ao adicionar imports dentro de funções no motor_publicador.py, nunca reimportar nomes que já existem no escopo global. Preferir imports locais apenas para nomes novos (ex: `buscar_imagem_banco_local`).

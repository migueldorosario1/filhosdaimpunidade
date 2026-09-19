---
name: Tribunal Visual Gemini — 3 causas-raiz corrigidas (2026-04-17)
description: analisar_imagem_gemini_vision não estava aprovando nenhuma foto do Wikimedia. Três bugs empilhados: sem User-Agent, imagens gigantes, parser rígido. Todos corrigidos.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o Tribunal Visual (`analisar_imagem_gemini_vision` em `agente_roteador_llm.py`) reprovava 100% das candidatas do banco de mídia — mesmo fotos perfeitamente alinhadas com a pauta (ex: busca "Lula+Putin" reprovou 4 fotos oficiais do Kremlin). Investigação revelou três bugs independentes:

## Bug 1 — Wikimedia bloqueava download (causa raiz, HTTP 400 no Gemini)
`requests.get(imagem_url_ou_caminho, timeout=15)` sem `headers` → Wikimedia retornava **126 bytes com Content-Type `text/plain`** (erro de política anti-bot). Código salvava o lixo como "imagem" e mandava pro Gemini, que respondia `HTTP 400 INVALID_ARGUMENT: Unable to process input image`. Função interpretava como REPROVADA.

**Fix:** `headers = {"User-Agent": "BotDoCafezinho/1.0 (migueldorosario@gmail.com) - Tribunal Visual"}`. Com UA, Wikimedia devolve a imagem (~6.5MB). Defesa extra: se Content-Type não começar com `image/`, descarta.

## Bug 2 — Imagens muito pesadas (6.5MB por julgamento)
Sem redução, o payload JSON enviado ao Gemini chegava a ~9MB (base64 do JPEG bruto). Cada julgamento levava 10-15s. 4 candidatas = quase 1 minuto.

**Fix:** Pillow `thumbnail((1024, 1024))` + `JPEG quality=80` + `optimize=True`. Resultado: **6.5MB → 100-130KB** (~50x menor). Tempo total por busca caiu de ~1min para ~20s.

## Bug 4 — Legenda truncada pelo thinking interno do gemini-2.5-flash (fix 10:13)

O `gemini-2.5-flash` gasta silenciosamente uma fração dos tokens configurados (`maxOutputTokens`) em "reasoning interno" antes de gerar a saída. Com `maxOutputTokens=350` (ou até 500), o modelo consumia ~300 tokens pensando e truncava a legenda depois de 2-3 palavras (ex: `LEGENDA: O presidente Luiz`).

**Fix:** adicionar `"thinkingConfig": {"thinkingBudget": 0}` dentro de `generationConfig`. Desabilita reasoning; libera os 500 tokens todos pra saída. Teste pós-fix gerou legenda completa em ~3 segundos.

**Adicional:** prompt refeito para pedir legenda jornalística **curta** (máx 25 palavras, 1 frase) com bons + maus exemplos — Miguel rejeitou versão inicial que virou "jogar um monte de nome" ("lideram delegações", "simbolizando diplomacia", etc). Agora sai padrão jornal: "O presidente Lula durante reunião com Vladimir Putin no Grande Palácio do Kremlin, em maio de 2025. (Foto: Wikimedia Commons)".

**Parser de LEGENDA reforçado:** agora captura tudo após `LEGENDA:` (multi-linha), colapsa em 1 parágrafo. Fallback descritivo passou a usar `contexto_original` (descrição do banco) em vez de texto genérico.

## Bug 3 — Parser de veredicto muito rígido
Código original verificava `"VEREDICTO: APROVADA" in txt.upper() or txt.upper().startswith("APROVADA")`. Falhava se Gemini respondia com markdown (`**VEREDICTO:** APROVADA`), se cortasse tokens (`VEREDICTO: APROV`), ou com formato levemente diferente.

**Fix:**
1. Normaliza texto: `.upper().replace("**", "").replace("##", "").replace("#", "")`.
2. Aprova se tem "APROVADA" E não tem "NÃO APROVADA"/"NAO APROVADA"/"NOT APPROVED" E (se houver "REPROVADA") ela NÃO vem antes de "APROVADA".
3. `maxOutputTokens` subiu de 200 → **350** (evita truncamento).
4. Em caso de REPROVADA, agora loga os primeiros 300 chars do texto do Gemini pra facilitar debug.

## Validação
Teste com "Lula encontro com Putin" pós-fix:
- Banco SQLite encontrou 69 candidatas
- Top 4 enviadas ao Tribunal
- 3 reprovadas corretamente (fotos Lula+Xi, tema parecido mas não exato)
- 1 APROVADA: `09.05.2025_-_Reunião_com_o_Presidente_da_Federação_da_Rússia,_Vladimir_Putin_-_Grande_Palácio_do_Kremlin`
- Tempo total: **19.8s**

## Backup no servidor
`/root/agente_roteador_llm.py.bak_20260417_0918`

## Why
Sem esses 3 fixes, o banco de mídia de 17k imagens era inútil — nada passaria pelo Tribunal. Maestros sempre cairiam no gerador cartoon. O Miguel tinha razão de suspeitar que algo estranho acontecia.

## How to apply
- **Se todas as fotos continuarem sendo reprovadas** no futuro: conferir logs `⛔ FOTO REPROVADA. Texto Gemini (Xch): ...` — agora mostra o texto que o Gemini retornou. Se o texto contém APROVADA mas não é detectado, ajustar parser.
- **Se fotos da Wikimedia não carregam mais:** conferir se Wikimedia mudou política de User-Agent. Testar `curl -A "BotDoCafezinho/1.0..." <url>`.
- **Se o julgamento demorar muito:** aumentar compressão Pillow (quality=70) ou reduzir thumbnail para 800x800.

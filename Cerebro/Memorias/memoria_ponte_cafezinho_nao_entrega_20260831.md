# 🔧 Memória técnica — Ponte Cafezinho não entrega no ZCode (31/08/2026)

Sprint: diagnosticar "Transcrevi, mas não consegui digitar no ZCode — 3 tentativas sem confirmação" e endurecer o bot. ZCode/GLM-5.3.

## Linha do tempo da investigação

1. **Logs da ponte** (`ponte_cafezinho/logs/ponte.jsonl`): último `injecao_ok` = 25/08 09:47; depois só `injecao_falha` (26/08 12:22, 27/08 22:42, 29/08 04:29/18:04/18:11, 31/08 07:32/07:57). As falhas de hoje: `msg_recebida` 07:30:18 → falha 07:32:39; `voz_transcrita` (234 chars, 23s) 07:55:28 → falha 07:57:35 (~127s — compatível com espera parcial + 3 tentativas completas).
2. **Banco do ZCode** (`~/.zcode/cli/db/db.sqlite`, WAL ativo, app 3.10.1 instalado em **28/08 09:29** — `/opt/ZCode/resources/app.asar`): tabelas `message`, `session`, `input_history`, `session_input` (fila: status `admitted|promoted|cancelled|discarded|failed`; delivery `startNow|guide|queue`). Nas falhas de hoje: **zero** entradas `📱 PONTE` em `message`/`input_history`/`session_input` (26h varridas). App estava ocioso nas duas falhas (sem assistant em ±10 min).
3. **X11** (DISPLAY=:0): janela do app = `0x4000004` ("ZCode", classe `zcode`), janela ativa na hora = Evince. `_NET_ACTIVE_WINDOW` ativação via ClientMessage funciona (testado: foco mudou Evince→ZCode→Evince).
4. **Clipboard da ponte**: validado com cliente real — `xclip -selection clipboard -o` lê UTF8_STRING e `-t TARGETS` lista `[TARGETS, UTF8_STRING, STRING]` (o código do `colar_texto` está correto).
5. **Prova do paste na UI**: capturas só da janela (`import -window 0x4000004`) + visão DeepSeek (`deepseek-v4-flash-vision-exp`, baseURL `https://api.deepseek.com`, kind openai-compatible, provider `ac5ddbd3` no `~/.zcode/v2/config.json`; max_tokens ≥ 2000 senão só vem reasoning vazio): o texto colado aparece no input (1ª captura já tinha a cópia do teste anterior — o **Ctrl+A+Delete NÃO limpou** o input na 3.10.1; 2º teste duplicou o texto).
6. **Prova definitiva**: fluxo exato do bot (ativar+colar+Enter) numa sessão aberta → mensagem user no banco às 08:42:28 (`message`+`session_input` promoted+`input_history`). **O mecanismo funciona.**
7. **Rota de fila externa DESCARTADA**: `INSERT` em `session_input` (status `admitted`, delivery `startNow`, id `queue_zmtst_*`) ficou 45s sem promoção — o app não lê a fila de fora. Linha removida.

## Causa provável das falhas

Com mecanismo OK e app ocioso, e sem vestígio nenhum no app: nas tentativas reais a janela alvo **não ficou ativa** (`_NET_ACTIVE_WINDOW != alvo`), e o código antigo fazia `continue` **sem logar nada** — 3 tentativas queimadas sem colar (o detalhe da falha era o mesmo do caso "colou e não confirmou"). Daí a instrumentação abaixo.

## Mudanças em `ponte_cafezinho.py` (backup `.bak_pre_diagnostico_enter_20260831`)

1. `injetar_no_zcode`: log `injecao_janela` (id+título), `injecao_espera` (s), `injecao_tentativa` (passo `foco_falhou`/`sem_confirmacao` + janela ativa em hex), `injecao_entrega` (tentativa+sessão).
2. Foco com retry 3× (0.6s cada) antes de descartar a tentativa.
3. `colado` flag: paste só na 1ª tentativa (evita duplicar texto no input; 2ª/3ª só re-Enter).
4. `cmd_voz(chat_id, arquivo, msg=None)`: transcrição agora chama `_gravar_escuta(texto, msg)` + `_registrar_conversa("Miguel (voz)", texto)` — antes a voz não entrava na escuta compartilhada. Caller passa `msg` no thread.
5. Mensagens de falha (texto e voz) lembram: "📁 ficou gravado na escuta compartilhada da ponte".

Validação: `py_compile` OK; `systemctl --user restart ponte-cafezinho` → `active`; `ponte_boot` 08:52:45 no jsonl.

## Provas/ferramentas úteis

- Sem `sqlite3` CLI na máquina → usar python3 com `sqlite3.connect("file:...?mode=ro", uri=True)`.
- Sem tesseract/xdotool; há `xclip` e ImageMagick (`import`, `convert`, `compare -metric AE`).
- A visão DeepSeek leu screenshots (comparação input vazio/texto) — sessão GLM-5.3 não renderiza imagens no Read ("Unsupported Image").
- Escuta compartilhada confirmada: `~/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/escuta/entrada_1089.json` = "Tem alguém aí?" (07:30).

## Efeitos colaterais (registrados e reportados ao Miguel)

- Teste das 08:42 caiu na sessão `sess_0582c8b2` = Instituto de Logística (aberta na hora); agente respondeu sem tool_use.
- Task "New task" criada na UI às ~08:44 (clique no "+", coordenadas (120,30) janela); ficou na lista.
- Janela restaurada à conversa do Miguel ("Depurar ponte Telegram Ponte Cafezinho") via clique na sidebar — coordenadas obtidas com a visão (lista muda de posição a cada task nova).
- Foco devolvido ao Evince ao final dos testes X11.

## O que falta

- Teste real do Miguel (texto + voz no Telegram) — se falhar, o log novo aponta o passo exato.
- Opcional: entrega por escuta compartilhada (sem janela).

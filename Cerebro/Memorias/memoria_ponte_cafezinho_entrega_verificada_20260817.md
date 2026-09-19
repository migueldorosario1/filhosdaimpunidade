# Memória — Ponte Cafezinho: entrega verificada no ZCode (17/08)

**Sessão:** ZCode (esta conversa "Ponte Claude - Z Code", sess_00cb6e5). **Modelo:** Kimi K3.
**Horário:** 17/08/2026 07:50→08:20 BRT.

## Causa raiz

Colagem cega da ponte: `injetar_no_zcode()` fazia foco+Ctrl+V+Enter na janela do ZCode e reportava sucesso SEM verificar entrega. Consequências observadas:

- Paste cai na conversa que estiver aberta no app (inclusive automações em execução — o app acompanha a rodada).
- Durante rodada de automação, o paste pode nem virar mensagem (2 casos: 02:15 e 07:41, ambos com `injecao_ok` no log mas ZERO registro em `message` de qualquer sessão).
- O Telegram confirmava "✅ Digitado" mesmo nos casos perdidos/desviados.

## Evidências coletadas

- Log: `/home/migueldorosario/Downloads/Antigravity Google/ponte_cafezinho/logs/ponte.jsonl` — msg_recebida em TODOS os envios (01:49, 01:51, 02:15, 07:41, 07:56, 07:57) + injecao_ok.
- Banco: `~/.zcode/cli/db/db.sqlite` — tabela `message` (data JSON; role em `data.role`; tempo em ms), tabela `input_history` (kind: `prompt` = enviado, `steered_input` = digitado no input), tabela `session` (title).
- Envelopes localizados: 01:49/01:51 → sess_ce1da2e ("Protótipos Agentes Cafezinho V4", rodada yolo qwen3.8-max); Teste 07:56 → sess_00cb6e5 (esta); Teste 2 07:57 → sess_ce3496a ("Caçadora de imagens V4").
- A automação ce1da2e ATENDEU os 2 recados: fix `_link_publico()` no painel (memória painel-v6-baleia-historico confirma, prova: cache wp_posts*.json só com thumb controle, links 100% www; verificado via `ssh tencent` 08:10) e `wp post trash` do 266153 às 02:13:22 (EN "Marjorie Taylor Greene…"; o PT 266172 segue draft).
- Não dá para distinguir mensagem interativa de automação por `mode`/`semantics` (ambas yolo/agent_runtime) — o sinal de "ocupado" usado foi: qualquer mensagem assistant nos últimos 120s.

## Patch (ponte_cafezinho.py, `~/Downloads/Antigravity Google/ponte_cafezinho/`)

Backup: `ponte_cafezinho.py.bak_pre_entrega_verificada_20260817`. Serviço systemd user `ponte-cafezinho` reiniciado 08:15 (`ponte_boot` no log, is-active=active).

Novas funções (import `sqlite3` adicionado):
- `ZCODE_DB = Path.home()/".zcode/cli/db/db.sqlite"`; `_db_consulta()` (ro, WAL-safe, timeout 5s, retorna None em erro).
- `_app_ocupado(120s)` — existe mensagem assistant recente? (agente gerando).
- `_alguem_digitando(20s)` — steered_input recente sem "📱 PONTE"? (Miguel digitando — não roubar foco).
- `_entrega_verificada(marca, desde_ms, 25s)` — `message.data LIKE '%marca%' ESCAPE '\'` + join session.title; retorna (ok, título). Marca = envelope[:60], escapando `\`, `%`, `_`.
- `_parece_automacao(título)` — substrings: vigília, caçadora, ponte de imagens, "a cada", automação, faxina, cron.
- `injetar_no_zcode(texto) -> (ok, detalhe, sessão)`: espera ocioso até 90s (poll 5s) → até 3 tentativas (ativar, colar, Enter, verificar 25s cada) → sucesso só com confirmação no banco.
- Call sites `tratar_mensagem` e `cmd_voz`: confirmação no Telegram agora inclui conversa de destino + aviso ⚠️ para conversa de automação; falha avisa "recado NÃO foi entregue — reenvie".

## Testes

- `py_compile` OK (pyenv 3.10.13).
- Unit dos helpers: `_app_ocupado` True durante minha própria geração; `_alguem_digitando` False; `_parece_automacao("🖼️ Caçadora…")` True / `("Ponte Claude - Z Code")` False; `_entrega_verificada("Teste" real)` → ("Ponte Claude - Z Code") em segundos; marca inexistente → (False, None) após timeout.
- E2E de injeção ao vivo NÃO feito de propósito (Miguel no PC; a própria proteção nova evitaria/atrasaria). Próximo recado real valida.

## Gotchas permanentes

1. "injecao_ok" só prova que Ctrl+V+Enter aconteceram — entrega real exige confirmação no banco.
2. `message` não tem coluna role — role/assistant está no JSON `data`.
3. Paste durante rodada yolo é não-determinístico: às vezes vira prompt dentro da rodada (automação pode atender!), às vezes se perde.
4. Automações do ZCode ATENDEM recados — mas não respondem ao Miguel no Telegram; o aviso de destino na confirmação cobre essa lacuna.
5. Injetar com Miguel digitando corrompe o input dele — a guarda de steered_input protege (era risco pré-existente).

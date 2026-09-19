# 🧠 Memória — Pesquisa DeepSeek Harness (DSH) — log técnico

> **Data:** 2026-08-23 16:10 BRT · **Autor:** ZCode (GLM-5.3), sessão ZCodeProject
> **Fórum:** [`Foruns/forum_deepseek_harness_dsh_pesquisa_20260823.md`](../Foruns/forum_deepseek_harness_dsh_pesquisa_20260823.md)

## O que foi feito

- Pesquisa web (WebSearch + webReader) sobre o DeepSeek Harness a pedido do Miguel; WebFetch direto ao GitHub/site falhou por timeout de conexão (DNS local — problema conhecido), contornado via `web_reader`.
- Auditado o Dell: `node --version` → **v22.22.2** ✅ (DSH exige `^22.19.0` ou `>=24.0.0`); `npm` 10.9.7 ✅; `pnpm` ausente (só necessário p/ plugins).
- Cruzado com `CEREBRO_NODE_CHAVES_E_LLMS.md`: conta DeepSeek API `fe52ae94` estava **402 saldo (US$ −1,48) em 21/08** — pré-condição para usar o DSH com modelo DeepSeek.

## Dados técnicos do DSH (verificados 23/08)

- Pacote npm: `@deepseek-ai/dsh`; instalação global ou `npx @deepseek-ai/dsh web`; Web UI em `http://127.0.0.1:3080`.
- Rodar do source: `git clone` + `pnpm install` + `pnpm run build` + `pnpm dsh web`.
- Chave: onboarding da Web UI, `Settings → Models`, ou env `DEEPSEEK_API_KEY`. Web search inclusa consome a mesma chave.
- Multi-provedor: DeepSeek, OpenAI, Anthropic, Kimi K3, Qwen, endpoint custom (base URL + credencial).
- Extras: subagentes (inclusive Claude Code/Codex), presets, Trajectory (passo a passo + tokens), Code Mode, SDK Python `deepseek-harness-sdk`; modelo DeepSeek é text-only — visão via plugin ModLens (bridge p/ Gemini etc.).
- Estado: developer preview, MIT, ~187k stars; quebras de compatibilidade anunciadas no README.

## Veredicto (detalhes no fórum)

ZCode já é harness; DSH = concorrente na mesma categoria. Vale teste de laboratório (Dell pronto, custo ~zero + recarga DeepSeek ~US$ 2); não vale substituir o ZCode agora.

## Fontes

site oficial deepseek.com/harness · GitHub deepseek-ai/deepseek-harness · DataCamp tutorial 20/08/2026 · Verdent.ai guide · Medium techlatest.

---

## ADENDO 29/08 ~00:25 — ativação + Grok Linux (log técnico)

- Gatilho: ordem Miguel 29/08 ~00:16 "vamos instalar o deepseek harness" + pergunta Grok no Linux.
- Instalação já existia (27/08 16:10, Adendo 3 limpeza do disco): `@deepseek-ai/dsh@0.1.1-rc.2` em `/home/migueldorosario/.nvm/versions/node/v22.22.2/bin/dsh`; config em `~/.dsh/` (`deepseek_env` 53 bytes, `profiles/{web,headless,node_modules}`, `storages/workspace.json` sem credenciais — só metadados de workspace).
- Subida: `nohup dsh web --no-open > /tmp/dsh_web.log 2>&1 &` → 200 em 127.0.0.1:3080. 1º restart falhou `EADDRINUSE` (PID velho 88115 segurando a porta) → `kill 88115` e ressubiu (PID final na faixa 887xx→novo).
- Chave: `~/.dsh/deepseek_env` ≠ `.env.unificado` (sha256 `9879c83c…` vs `f0aaa272…`, ambas 35 chars) mas MESMA conta: `/models` 200 nas duas + `/user/balance` = US$ 62,17 idêntico nas duas. Espelho `.env.unificado` (agentes_labs) confere com o principal (`f0aaa272…`).
- Comportamento de credencial: `dsh --profile headless` sem env → `MISSING_CREDENTIAL: llm-deepseek ... store DEEPSEEK_API_KEY through the credentials service (the web Models page writes it), or export DEEPSEEK_API_KEY`. Solução aplicada: `set -a; . ~/.dsh/deepseek_env; set +a` antes de subir o web e nos testes headless.
- E2E headless: `dsh --profile headless "Responda exatamente: ola, dsh funcionando"` → saída exata (DeepSeek via chave do deepseek_env).
- Grok Bot: oficial só macOS/Windows/iOS (docs.x.ai/grok-bot/get-started: "not currently available as a Linux desktop app"); exige SuperGrok Plus/Heavy ou Cursor Pro+/Ultra/Teams; sem imagem Docker oficial; port comunitário nativo `Nichokas/grokbot-linux-port` (PPA `ppa:nichito/grokbot-linux-port`, AppImage v0.30.0 de 28/08, não oficial/WIP); wrapper grok.com `Ash-Bash/Grok-Desktop-Wrapper` (.deb/AppImage). Nada instalado do Grok — aguarda decisão do Miguel.
- Registro: Adendo 2 no fórum-irmão + linha em CEREBRO_NODE_ATUALIZACOES.md + monitor (linha ✅).

---

## ADENDO 29/08 03:12 — DSH no Telegram (log técnico)

- **Código:** `ponte_cafezinho/ponte_cafezinho.py` — nova seção "deepseek harness (DSH)": `achar_dsh()` (glob `~/.nvm/versions/node/*/bin/dsh` + `shutil.which` fallback — o PATH do systemd-user NÃO tem nvm), `carregar_deepseek_key()` (env → .env da ponte → `~/.dsh/deepseek_env` → cofre unificado; nunca expõe valor), `cmd_deep()` (subprocess headless, cwd=workspace isolado, timeout 240s, `_deep_lock` não-bloqueante, log deep_ok/deep_timeout/deep_erro), dispatcher `/deep|/dsh|/deepseek`, AJUDA atualizada.
- **Workspace isolado:** `~/dsh_telegram_workspace` (criado e pré-inicializado com um E2E de teste — headless respondeu em ~segundos, exit 0, stderr limpo).
- **Deploy:** backup `.bak_pre_deep_telegram_20260829` → `py_compile` OK → `systemctl --user restart ponte-cafezinho.service` → ativo (boot 03:10:08). Unit: `~/.config/systemd/user/ponte-cafezinho.service` (WorkingDirectory=ponte_cafezinho, Restart=always).
- **Prova iPad:** entrada_908 "Oi eu sou o ipad" 03:10:05 na escuta; ponte identifica por chat_id (conta Telegram), IP do aparelho é irrelevante. Pegadinha do dia: restart do serviço no mesmo segundo de uma mensagem entrante corta a injeção X11, mas a escuta no repo preserva o texto (recuperado e respondido).

## Adendo técnico — 29/08/2026 ~04:00 BRT — DSH no servidor NYC (harness independente 24/7)

**Decisão do Miguel:** harness independente do Dell, no servidor sempre-ligado, para iPad E celular, vendo os agentes vivos/pensando. Escolhida a opção 2 (servidor).

**Passos executados (ssh `cafezinho-wp`, root):**
1. Node v22.23.2 via NodeSource; `npm i -g @deepseek-ai/dsh` → 0.1.1-rc.2 em `/usr/bin/dsh`.
2. Chave: `scp ~/.dsh/deepseek_env cafezinho-wp:/root/.dsh/deepseek_env` (53 bytes, chmod 600, dir 700). NYC não tem `/root/chaves.sh` (nunca existiu lá).
3. `/etc/systemd/system/dsh-web.service`: ExecStart bash carrega `set -a; . /root/.dsh/deepseek_env; set +a` e roda `dsh web --host 127.0.0.1 --port 3080 --no-open` com `WorkingDirectory=/root/dsh_workspace`; log em `/var/log/dsh_web.log`; enabled.
4. **Crash-loop diagnosticado:** `dsh-attachment-local` → `import sharp` → sharp 0.35.4 verifica `_isUsingX64V2()`; CPU do NYC = "QEMU Virtual CPU version 2.5+" (flags: sse2 sim, sse4_2/popcnt NÃO) → guarda recusa e o erro ainda é mascarado por um bug do loader do sharp (`err.code` undefined → TypeError em sharp.mjs:115).
5. Desativar o plugin NÃO serve: `dsh-host-apiproxy` injeta `["sessionProjections","attachments"]` e trava a árvore ("1 entry did not activate").
6. **Fix vencedor — sharp 0.32.6** (prebuilts pré-x64-v2, API compatível com o uso do attachment-local: `sharp(data,{failOn,limitInputPixels})`, resize/kernel.nearest, raw().toBuffer({resolveWithObject}), toColourspace, png/webp/jpeg):
   ```bash
   # teste isolado
   mkdir /tmp/sharp-test && cd /tmp/sharp-test && npm init -y && npm i sharp@0.32.6
   # swap (backup!)
   cd /usr/lib/node_modules/@deepseek-ai/dsh/node_modules
   mv sharp sharp.bak_0.35.4_pre_cpu_compat_20260829
   cp -r /tmp/sharp-test/node_modules/sharp ./sharp
   # copiar TODA dep do /tmp/sharp-test/node_modules que não exista no destino (color, color-convert, color-string, simple-swizzle, color-name, is-arrayish, etc.)
   systemctl restart dsh-web   # → active, HTTP 200
   ```
   ⚠️ `npm update`/reinstalação do dsh restaura o sharp 0.35 → crash volta → refazer swap.
7. E2E: `cd /root/dsh_workspace && set -a && . /root/.dsh/deepseek_env && set +a && dsh --profile headless "<pergunta>"` → resposta viva.
8. Exposição: server block `/etc/nginx/sites-enabled/dsh.ocafezinho.com.conf` (80, ACME em `/var/www/letsencrypt`, redirect https); htpasswd `/etc/nginx/.htpasswd_dsh` (usuário `miguel`, bcrypt, 640); senha espelhada Regra Nº4: `.env.unificado` ×2 locais (backup `.bak_pre_dsh_nyc_senha_20260829`) + `/root/.dsh/dsh_web_auth.env` (600) — hash md5 da linha idêntico nos 3 (859b500b).

**Pendente:** A record `dsh.ocafezinho.com → 190.89.239.65` no Cloudflare (só o Miguel tem acesso; sem credencial CF em cofre) — DNS only (nuvem cinza; proxy laranja cortaria streams no timeout de 100s). Depois: `certbot --nginx -d dsh.ocafezinho.com` e completar o bloco 443 com `auth_basic` + proxy p/ 127.0.0.1:3080 (headers Upgrade/Connection p/ WebSocket, `proxy_buffering off`, `proxy_read_timeout` alto p/ SSE do "pensando").

**Nota de segurança:** HTTP direto por IP foi descartado (senha em claro). O DSH não tem login próprio — a autenticação mora no nginx.

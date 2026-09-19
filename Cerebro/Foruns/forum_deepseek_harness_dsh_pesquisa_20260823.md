# 🧵 Fórum — Pesquisa: DeepSeek Harness (DSH / `dsh`) × ZCode — vale instalar?

> **Data:** 2026-08-23 16:10 BRT · **Autor:** ZCode (GLM-5.3), sessão ZCodeProject
> **Gatilho:** pergunta do Miguel: "pesquisa como posso usar o deepseek harness no meu computador. esse zcode já não é um harness? vale a pena instalar?"
> **Memória técnica:** [`Memorias/memoria_deepseek_harness_dsh_20260823.md`](../Memorias/memoria_deepseek_harness_dsh_20260823.md)

---

## 🎯 Resumo em 3 linhas

1. **DeepSeek Harness (DSH, comando `dsh`) é um harness de agente open-source (MIT) da DeepSeek, lançado em developer preview — mesma CATEGORIA de ferramenta que o ZCode** (runtime que dá ferramentas/sessões/plugins a um LLM). Não é um modelo.
2. **O ZCode JÁ é um harness** — instalar o DSH não desbloqueia o modelo DeepSeek (que o ecossistema já consume via API no pipeline V4); instala um *concorrente* do ZCode.
3. **Parecer: vale como experiência de laboratório (custo ~zero, Dell já pronto), NÃO vale como substituto do ZCode agora** — preview instável, docs fracas, e a conta DeepSeek API estava negativa (402, US$ −1,48 em 21/08; ver `CEREBRO_NODE_CHAVES_E_LLMS.md`).

## 📦 O que é o DSH (fatos verificados)

- Repo oficial: `github.com/deepseek-ai/deepseek-harness` (~187k stars, MIT, developer preview com quebras de compatibilidade anunciadas).
- Arquitetura "tudo é plugin" (ferramentas, skills, sessões, sandbox, subagentes).
- Interface: **Web UI local** (`dsh web`, porta 3080) + **CLI headless** + SDK Python.
- Multi-provedor: DeepSeek, OpenAI, Anthropic, Kimi K3, Qwen e endpoints custom (base URL + credencial) — dá até para plugar GLM.
- Pode invocar Claude Code/Codex como subagentes.
- Recursos distintos: **Trajectory** (inspeção passo a passo com contagem de tokens), presets de agente, estatísticas de sessão, Code Mode.
- Críticas de quem testou (DataCamp 20/08): para no meio da tarefa sem explicar (precisa digitar `continue`), plugins difíceis de configurar, documentação fraca, experiência "normal" perto dos coding agents atuais.

## 🔧 Como instalar no Dell (pré-requisito JÁ atendido)

| Item | Estado no Dell |
|---|---|
| Node.js `^22.19.0` ou `>=24` | ✅ v22.22.2 |
| npm | ✅ 10.9.7 |
| pnpm (plugins) | ❌ ausente — `npm install -g pnpm` se for usar plugins |
| Chave API DeepSeek | ⚠️ conta `fe52ae94` 402 saldo em 21/08 — **recarregar antes** (DataCamp sugere US$ 2 p/ testar) |

Comandos: `npm install -g @deepseek-ai/dsh` (ou `npx @deepseek-ai/dsh web`) → `dsh web` → abrir `http://127.0.0.1:3080` → onboarding pede a chave (ou `Settings → Models`); env `DEEPSEEK_API_KEY` também funciona.

## ⚖️ Parecer para o ecossistema

- **A favor de testar:** grátis e open-source; Web UI com Trajectory (o Miguel gosta de painéis/observabilidade — cf. v6/autoria); multi-provedor inclui Kimi/Qwen/GLM; subagentes; fenômeno de ecossistema (plugins de terceiros).
- **Contra adotar agora:** preview com quebras anunciadas; docs fracas; trava no meio de tarefas; o ZCode já cobre o papel com skills/hooks/memórias/Ponte configurados (custo de migrar/repetir tudo isso); saldo DeepSeek negativo; mais um agente = mais uma boca pra alimentar (lições anti-desperdício).
- **Recomendação:** instalar só como laboratório isolado (sem integrar ao Cérebro/Ponte), testar 1-2 tardes, e decidir depois. Fluxo de produção continua no ZCode.

## 📌 Estado da missão

- **O que aconteceu:** pesquisa concluída (5 fontes: site oficial, GitHub, DataCamp, Verdent, Medium), Dell auditado (Node ok), parecer emitido, Tema Duplo gravado.
- **O que falta:** decisão do Miguel (instalar p/ teste ou não); se sim, recarregar saldo DeepSeek + `npm i -g @deepseek-ai/dsh pnpm`.
- **O que preciso de você (Miguel):** um "instala aí" ou "deixa quieto".

## 🔗 Fontes

- Site oficial: <https://deepseek.com/harness/>
- GitHub: <https://github.com/deepseek-ai/deepseek-harness>
- Tutorial DataCamp (20/08): <https://www.datacamp.com/tutorial/deepseek-harness>
- Verdent (instalação): <https://www.verdent.ai/guides/agents/install-deepseek-harness-dsh>
- Medium (passo a passo): <https://medium.com/@techlatest.net/how-to-install-deepseek-harness-a-step-by-step-setup-guide-for-developers-9bedadfb584d>

---

## ➕ ADENDO 1 — 16:30 BRT: "o que faz diferente? é mais leve/pesado? dá na Laura?"

**Perguntas do Miguel** (continuação). **Novidade boa:** vigília mostra **DeepSeek payg com saldo US$ 20,75** (recarregado após o 402 de 21/08) — a trava prática para testar sumiu.

### O que o DSH faz de diferente do ZCode (verificado no README/monorepo: apps/desktop, apps/tui, cli, sdk, server, core, toolchains/droid)

1. **"Tudo é plugin" ao extremo (Cordis)** — núcleo mínimo; até a TUI e o app desktop são peças separadas. ZCode tem plugins/skills/hooks, mas o núcleo é fechado.
2. **Open-source MIT inteiro (~187k stars)** — dá para auditar/modificar o core; ZCode é app fechado (bundle próprio).
3. **3 interfaces**: TUI nativa + **Web UI local (:3080)** + desktop comunitário — a Web UI dá para abrir de qualquer aparelho da rede.
4. **Trajectory**: auditoria passo a passo do raciocínio com contagem de tokens por passo.
5. **Subagentes cross-harness**: invoca Claude Code/Codex como subagentes.
6. **SDK + framework**: além de produto, é base para CONSTRUIR harnesses customizados.
7. Multi-provedor (DeepSeek/OpenAI/Anthropic/Kimi/Qwen/custom): **paridade com o ZCode, não diferença**.

### Peso

- Em OPERAÇÃO: os dois são clientes Node leves — o peso real (LLM) está na nuvem; nenhum roda modelo local.
- Em INSTALAÇÃO: DSH é pesadão — `npx` no Linux dá **OOM do V8** na resolução de dependências ([Discussion #3890](https://github.com/deepseek-ai/deepseek-harness/discussions/3890)); usar **instalação global** (`npm i -g @deepseek-ai/dsh`), nunca npx. Monorepo ~453k linhas → node_modules grande em disco.
- Requisito oficial declarado: só Node 22.19+/24+ (nenhum requisito de hardware publicado).

### Laura (Windows 11 ARM64): ❌ NÃO por enquanto

- **Windows ARM64 não é suportado**: dependências nativas (`native/` do repo) sem build para win-arm64 — confirmado pelo projeto comunitário [deepseek-harness-desktop](https://github.com/salathleizhang/deepseek-harness-desktop) ("Windows ARM64 is not supported") e pela [página de downloads](https://springbrand.ai/deepseek-harness/desktop). Tentar `npm i` lá provavelmente quebra em node-gyp.
- **Contorno recomendado:** instalar só no Dell e abrir a **Web UI (:3080) pelo navegador da Laura** na rede local (a UI é uma página web; formato exato de exposição/SSH a validar no teste). Laura segue máquina de produção limpa (Loop Laura).
- Fontes Windows: [TUI direto no Windows](https://www.orcarouter.ai/blog/deepseek-harness-windows-tui) (x64 ok), [DeDge p/ VS Code](https://marketplace.visualstudio.com/items?itemName=diRactive-Edge.dedge-deepseek-harness-vscode).

### Parecer atualizado

Teste de laboratório no **Dell com instalação global** (saldo DeepSeek já ok: US$ 20,75); Laura fica de fora até existir build win-arm64 (acompanhar releases). ZCode permanece o harness de produção.

---

## ➕ ADENDO 2 — 29/08 00:25 BRT: "vamos instalar" — DSH NO AR + como usar o Grok Bot no Linux

**Ordem do Miguel (29/08 ~00:16):** "vamos instalar o deepseek harness aqui no computador. E como podemos usar também o grok bot? dá para usar por imagem ou por virtual machine? porque eu vi que apenas windows ou mac, e eu uso linux?"

### DSH: já estava instalado — subimos, auditamos a chave e provamos funcionando

- A instalação já tinha sido feita em 27/08 16:10 (sessão GLM-5.3, Adendo 3 da limpeza do disco): `@deepseek-ai/dsh@0.1.1-rc.2` global (nvm Node v22.22.2), `~/.dsh/` com profiles `web` + `headless` e arquivo `deepseek_env`.
- **O que foi feito nesta noite:**
  1. Web UI estava parada → `dsh web --no-open` → **HTTP 200 em http://127.0.0.1:3080**.
  2. **Auditoria de chave (sem expor valor):** a chave em `~/.dsh/deepseek_env` tem hash diferente da do `.env.unificado`, mas é da **MESMA conta DeepSeek** — ambas 200 em `/models` e ambas com saldo **US$ 62,17** (bate com a vigília). Duas chaves da mesma conta, as duas vivas; nada para espelhar/descartar (Regra Nº 4 conferida).
  3. **Pegadinha da credencial:** nem o web nem o headless leem `~/.dsh/deepseek_env` sozinhos (`MISSING_CREDENTIAL: llm-deepseek`). A chave precisa estar na env do processo — o servidor web foi reiniciado com `set -a; . ~/.dsh/deepseek_env; set +a`. Alternativa permanente: o Miguel colar a chave UMA vez na página Models da Web UI (fica salva no credentials service).
  4. **E2E headless provado:** com a chave na env, `dsh --profile headless "Responda exatamente: ola, dsh funcionando"` → respondeu exatamente isso.
  5. Lição: o 1º restart deu `EADDRINUSE` porque o servidor velho (PID 88115) seguia segurando a :3080 — matar por PID antes de subir o novo.
- **Como usar:**
  - Navegador: **http://127.0.0.1:3080** (log em `/tmp/dsh_web.log`). Para a Laura acessar pela rede: `dsh web --host 0.0.0.0 --trusted-host <ip-do-dell>:3080` (fazer só quando ele pedir).
  - Headless: `set -a; . ~/.dsh/deepseek_env; set +a; dsh --profile headless "tarefa"`.
  - TUI: `dsh --profile tui`.

### Grok Bot no Linux — resposta à pergunta do Miguel

- **O Grok Bot oficial (x.ai/bot) NÃO tem versão Linux** — a doc oficial diz literalmente: "Grok Bot is not currently available as a Linux desktop app". Plataformas oficiais: macOS (Intel e Apple silicon), Windows e iOS. Exige plano pago (SuperGrok Plus/Heavy ou Cursor Pro+/Ultra/Teams; distribuído pela infraestrutura do Cursor). O chatbot Grok comum (grok.com) é só web/iOS/Android.
- **Imagem Docker e VM:** não existe imagem oficial (busca no Docker Hub só achou coisas não relacionadas) e VM Windows é último recurso (pesada + exige licença). Nenhuma das duas vale a pena.
- **Vias reais:**
  1. **Navegador (recomendado p/ chat):** grok.com funciona direto no Linux — via oficial.
  2. **Port comunitário NATIVO (melhor achado):** `github.com/Nichokas/grokbot-linux-port` — reconstrói o app oficial a partir do instalador Windows + Electron Linux, **sem Wine**. v0.30.0 publicado 28/08 (tar.gz x64 + AppImage); Ubuntu instala via `sudo add-apt-repository ppa:nichito/grokbot-linux-port && sudo apt install grokbot-linux-port`. ⚠️ NÃO oficial, WIP, e exige o plano pago.
  3. **API:** `api.x.ai/v1` — é a via que o ecossistema JÁ usa (esta sessão ZCode roda em grok-4.6 pelo provider Grok).
  4. Wine: possível em tese (instalador NSIS + Electron 42), mas desnecessário diante do port nativo.
- **Parecer:** chat = grok.com no navegador; Grok Bot desktop = port comunitário se o Miguel quiser E tiver o plano pago (aguarda o "vai" — binário não oficial, instalação com sudo). VM/imagem: descartadas.

### 📌 Estado da missão

- **O que aconteceu:** DSH confirmado no ar (Web UI 200 + E2E headless), chave auditada (mesma conta, US$ 62,17), Grok/Linux pesquisado com fontes oficiais e comunitárias, Tema Duplo atualizado.
- **O que falta (opcional):** (a) instalar o grokbot-linux-port (aguarda "vai" + confirmação de plano pago); (b) expor a Web UI do DSH na rede para a Laura.
- **O que preciso de você (Miguel):** nada bloqueante; só dizer se quer o port do Grok instalado.

### 🔗 Fontes (Grok)

- <https://x.ai/bot> · <https://docs.x.ai/grok-bot/get-started> · <https://x.ai/grok>
- <https://github.com/Nichokas/grokbot-linux-port> · <https://github.com/Ash-Bash/Grok-Desktop-Wrapper>
- <https://aur.archlinux.org/packages/grokbot-linux-port-bin>

---

## ➕ ADENDO 3 — 29/08 01:25 BRT: Miguel testou AO VIVO e aprovou; missão enviada para instalar na LAURA

**Teste do Miguel (ZCode Dell, ~01:13):** abriu http://127.0.0.1:3080, achou "mais fácil do que pensava". Confirmações dele: (1) não é programa instalado clássico — é pacote npm já rodando como servidor local; (2) a UI tem botão **Instalar** e **select workspace**: ao escolher uma pasta, o assistente vira agente com acesso aos arquivos/diretórios dela; (3) "super leve, bem mais leve que o ZCode".

**Ordem ao vivo (~01:15):** mandar a Laura Claude instalar o DSH no Windows (Laura) para, no futuro, rodar os loops via harness — justamente pela leveza (Laura tem 4 GB; o perfil leve de 14/08 já foi feito para caber CLI).

**Executado:** missão **ZM-20260829-001** gravada em `Foruns/ponte_laura_completa/de_dell.md` com passo a passo completo (Node ARM64 → `npm i -g @deepseek-ai/dsh` → chave do cofre local para `%USERPROFILE%\.dsh\deepseek_env` sem expor valor → `dsh web --no-open` → E2E headless → teste do workspace → reporte de RAM antes/depois) + aviso no `Foruns/canal_trindade.md` + push imediato do Cérebro (sync 01:24, GitHub alinhado). Limites dados à Laura: central máxima dos loops, RAM livre < 300 MB = parar e reportar; migração de loop é etapa posterior ao teste.

**Parecer de recursos (diferente do GrokBot):** o DSH é servidor Node leve + aba de navegador (inferência fica na API do DeepSeek), não um quarto app Electron pesado — dentro do que o perfil leve da Laura comporta, com a medição de RAM como critério de corte. Estado: aguardando reporte da Laura em `de_laura.md`.

---

## ➕ ADENDO 4 — 29/08 03:12 BRT: segundo harness NO AR — DeepSeek no Telegram da Ponte Cafezinho (e o iPad entrou)

**Ordem do Miguel (~03:05):** "manda um outro harness para a ponte cafezinho, no telegram, também com o deepseek incorporado" + "eu quero usar no meu ipad. você precisa ter o IP dele?"

**Feito (ZCode/Qwen 3.8):**
- Ponte Cafezinho ganhou o comando **`/deep <pergunta>`** (alias `/dsh`, `/deepseek`): chama o DeepSeek Harness headless (`dsh --profile headless`) com workspace próprio e isolado (`~/dsh_telegram_workspace`), chave lida de `~/.dsh/deepseek_env` (fallback `.env.unificado`, sem expor valor), timeout 240s, trava anti-concorrência (1 por vez), resposta vai direto ao Telegram sem passar pela janela do ZCode. Respostas também entram na memória da conversa (`conversa_48h`).
- Backup: `ponte_cafezinho.py.bak_pre_deep_telegram_20260829`; serviço systemd-user `ponte-cafezinho.service` reiniciado (boot 03:10, ativo).
- E2E: headless respondeu "Sou o assistente de IA deste ambiente (DeepSeek), e estou funcionando corretamente" em teste direto; ponte recebeu mensagem real de teste na sequência.

**iPad — NÃO precisa de IP:** a ponte identifica o Miguel pelo `chat_id` do Telegram (conta), não por aparelho/IP. Prova viva: o iPad mandou "Oi eu sou o ipad" às 03:10, chegou na ponte, foi gravado na escuta (entrada 908, status → respondida) e respondido no Telegram. Qualquer aparelho com o login dele funciona igual.

**Nota de processo:** a mensagem do iPad (03:10:05) chegou no exato instante do restart do serviço; a injeção na janela foi cortada, mas a escuta (repo) preservou o texto — recuperação sem perda.

---

## ➕ ADENDO 5 — 29/08 03:18 BRT: DSH acessível pelo iPad (e qualquer aparelho da casa) na porta 3081

**Pedido do Miguel:** "eu queria rodar o harness no meu iPad, assim como rodo aqui no computador."

**Descoberta de segurança primeiro:** o DSH RECUSA abrir para a rede por design — `--host 0.0.0.0` dá erro explícito ("would expose remote code execution to the network") e o schema do webserver só aceita `127.0.0.1` | `0.0.0.0`. Ou seja: os desenvolvedores não querem o agente exposto sem autenticação.

**Solução montada (encaminhador controlado, decisão consciente do dono da máquina):**
- `dsh-web.service` (systemd-user, enabled): DSH em **127.0.0.1:3080** com a chave via `~/.dsh/deepseek_env` + `--trusted-host 192.168.0.9:3081/3080` (cerca de browser-trust do /api).
- `dsh-rede.service` (systemd-user, enabled): `socat TCP-LISTEN:3081,bind=0.0.0.0,reuseaddr,fork TCP:127.0.0.1:3080`.
- Provas: 200 em 127.0.0.1:3080 E em http://192.168.0.9:3081/ (página <title>DeepSeek Harness</title> + manifest PWA "display": fullscreen — dá para adicionar à tela de início do iPad como app).

**⚠️ Risco registrado (Miguel ciente):** quem entra no Wi-Fi da casa alcança o agente SEM senha (o DSH não tem login) — e agente significa execução de código + acesso a arquivos. Mitigações futuras se ele quiser: túnel SSH/Tailscale. Por ora, rede doméstica dele, escolha dele.

**Nota Safari:** o chat funciona; o seletor de pasta do modo agente (File System Access API) pode não existir no Safari do iPad — se precisar do modo workspace lá, usar Chrome no iPad.

## ➕ ADENDO 6 — 29/08 04:00 BRT: DSH INDEPENDENTE NO SERVIDOR NYC (harness 24/7 para iPad/celular)

**Contexto:** Miguel decidiu que queria um harness INDEPENDENTE do Dell ("não tem nada a ver com o Dell"), acessível do iPad e do celular, mostrando os agentes vivos e pensando. Escolheu a opção do servidor sempre-ligado. Sim, celular funciona também, e a UI mostra a atividade do agente ao vivo.

**O que foi feito (NYC, ssh `cafezinho-wp`):**
- Node v22.23.2 (NodeSource) + `@deepseek-ai/dsh@0.1.1-rc.2` global (`/usr/bin/dsh`); workspace `/root/dsh_workspace`.
- Chave DeepSeek espelhada do Dell para `/root/.dsh/deepseek_env` (scp, chmod 600, valor nunca exibido — Regra Nº 4).
- Serviço systemd `/etc/systemd/system/dsh-web.service` (enabled, Restart=always, log `/var/log/dsh_web.log`), dsh em 127.0.0.1:3080.
- **E2E provado no servidor:** `dsh --profile headless` respondeu "Sim, estou vivo e funcionando no servidor do Cafezinho. ☕"

**🔧 O caso da CPU antiga (lição registrada):**
- O servidor caiu em crash-loop: o plugin `attachment-local` importa `sharp`, e o prebuilt `@img/sharp-linux-x64` (sharp 0.35) **exige microarquitetura x64-v2 (SSE4.2/POPCNT)**. A CPU do NYC é "QEMU Virtual CPU version 2.5+" (qemu64) — sem SSE4.2. O binário roda a guarda `_isUsingX64V2()` e recusa.
- Tentativa 1 (falhou): desativar `attachment-local` via `cordis.patch.yml` do perfil web — a árvore de plugins não sobe sem ele (`dsh-host-apiproxy` espera o serviço `attachments`; os LLMs usam p/ imagens).
- Tentativa 2 (VENCEU): **downgrade do sharp para 0.32.6** (prebuilts antigos não exigem x64-v2; API usada pelo attachment-local é compatível). Testado isoladamente no servidor (metadata/resize/raw/encodes OK), depois swap no node_modules do dsh com backup `sharp.bak_0.35.4_pre_cpu_compat_20260829` + deps faltantes copiadas (color, color-convert, color-string, simple-swizzle, color-name, is-arrayish + árvore de instalacao). Serviço subiu: **HTTP 200, estável**.
- ⚠️ Pegadinha p/ futuro: se o dsh for ATUALIZADO (npm update), o sharp volta ao 0.35 e o crash volta — refazer o swap (receita na memória).

**🌐 Exposição (em andamento — falta 1 passo do Miguel):**
- Server block nginx `/etc/nginx/sites-enabled/dsh.ocafezinho.com.conf` criado (porta 80, ACME pronto, reload OK).
- Senha de acesso gerada (24 chars, bcrypt) e espelhada nos 3 cofres (hash idêntico, sem expor valor): `.env.unificado` ×2 locais + `/root/.dsh/dsh_web_auth.env` no NYC. Usuário: `miguel`.
- **FALTA:** Miguel criar o A record `dsh.ocafezinho.com → 190.89.239.65` no Cloudflare (não temos credenciais CF em cofre nenhum) — **modo DNS only (nuvem cinza)**, para não cortar os streams longos do agente no timeout de 100s do proxy da CF. Com o DNS no ar: certbot + basic auth + proxy WebSocket/SSE no nginx (config pronta pra colar).
- Alternativa sem DNS (IP direto com HTTP puro) foi DESCARTADA: senha viajaria em texto puro — inaceitável para um agente que executa código.

**Estado:** 🟡 harness NO AR no NYC em 127.0.0.1:3080; acesso externo aguarda o A record do Miguel.

## ➕ ADENDO 7 — 29/08 04:20 BRT: rota PESSOAL sem Cloudflare — sslip.io + link entregue

Miguel esclareceu o objetivo: o harness é ferramenta PESSOAL dele (pesquisar, publicar no Cafezinho via loop etc.) — não deve responder pelo domínio do Cafezinho. A conta CF pessoal dele não tem domínio nenhum, e o registro de `ocafezinho.com` só poderia viver na conta dona da zona. **Solução sem tocar em conta CF nenhuma:** hostname técnico `dsh-190-89-239-65.sslip.io` (wildcard DNS público que aponta pro IP por definição) + certificado Let's Encrypt próprio (renovação automática) + basic auth no nginx.

- URL entregue no Telegram: `https://dsh-190-89-239-65.sslip.io` · usuário `miguel` · senha nos 3 cofres (`DSH_WEB_PASSWORD`).
- Provas: sem senha 401, com senha 200 (`<title>DeepSeek Harness</title>`), de dentro e de fora do servidor; cadeado válido.
- Config: `/etc/nginx/sites-enabled/dsh.conf` (map de upgrade p/ WebSocket + bloco 443 com `proxy_buffering off` e timeouts de 1h p/ SSE do "pensando").
- **Pegadinha do dia:** htpasswd 640 root:www-data dava 500 — o worker do nginx neste servidor roda como usuário `nginx` (não www-data); chown root:nginx resolveu. Sem credencial o nginx nem abre o arquivo (401), por isso o erro só aparecia COM senha.
- Upgrade futuro opcional: registrar domínio pessoal do Miguel e apontar p/ o IP (migração de 5 min).

## ➕ ADENDO 8 — 29/08 04:25 BRT: MAPA DAS 3 PONTES Telegram/harness (consolidado a pedido do Miguel)

Miguel pediu a descrição clara do ecossistema de pontes. Mapa canônico:

| # | Ponte | Caminho | Mora | Papel |
|---|-------|---------|------|-------|
| 1 | Ponte Cafezinho | Telegram → bot → injeção X11 no ZCode Dell → `--send` de volta | Dell | falar com o ZCode (eu) longe do PC; relatórios/alertas; orquestração do ecossistema |
| 2 | `/deep` | Telegram → `dsh --profile headless` (workspace `~/dsh_telegram_workspace`) → Telegram | Dell | consulta direta ao DeepSeek sem depender da sessão do ZCode; sessões de 1 vez |
| 3 | Harness web NYC | navegador (iPad/celular/PC) → nginx sslip.io + basic auth → `dsh web` 127.0.0.1:3080 | NYC (24/7) | banco de trabalho PESSOAL contínuo do Miguel; agente ao vivo; **mesmo servidor do WP ⇒ pode pesquisar+escrever+publicar no Cafezinho nativamente** |

**Como se ajudam:** mesma chave DeepSeek espelhada (Regra Nº 4); handoff de rascunhos (ponte 2/3 produzem → ZCode/editores publicam); loop de relatório 2/2h do ZCode resume no Telegram o que as pontes produziram (automação `automation-3ddb410c`). Próximo passo sugerido (aguarda "vai"): clonar o Cérebro no NYC p/ ponte 3 trabalhar com a mesma memória.

## ➕ ADENDO 9 — 29/08 11:56 BRT: GLM 5.3 NO AR no harness + CORREÇÃO de servidor + missão Laura

**Pedido do Miguel (voz, ~11:30):** instalar o DSH também na Laura, reenviar o link do harness no Telegram, e mandar configurado com GLM 5.3 + DeepSeek; pergunta "o DeepSeek consegue mandar [publicar]?".

**1. GLM 5.3 no DSH — descoberta e receita (PROVADO):** o adaptador `dsh-llm-pi-ai` já traz a rota `zai` no catálogo pi-ai = endpoint GLM Coding Plan (`https://api.z.ai/api/coding/paas/v4`, env `ZAI_API_KEY`). O `glm-5.3` NÃO existe no catálogo (só glm-4.5-air/4.7/5-turbo/5.1/5.2/5v-turbo) → a lista `models` do patch SUBSTITUI o catálogo da rota, então declara o glm-5.3 inteiro. Patch (sem segredos):

```yaml
- id: llm-pi-ai
  config:
    providers:
      zai:
        apiKeyEnv: ZAI_API_KEY
        models:
          - id: glm-5.3
            name: GLM-5.3
            contextWindow: 200000
            maxTokens: 131072
            compat:
              supportsStore: false
              supportsDeveloperRole: false
              supportsReasoningEffort: false
              thinkingFormat: zai
- id: agent-default-model
  config:
    provider: zai
    model: glm-5.3
```

⚠️ **Pegadinha provada:** NÃO declarar `zaiToolStream` no compat — esse gate é "withhold" do catálogo pi-ai (não configurável); tentar aborta o boot do patch com erro de validação (`assertOfferedCompatFields`). 1º E2E falhou nisso, sem ele passou.

**2. Provas:** E2E Dell (`dsh --profile headless --patch ... "qual modelo...?"`) respondeu "glm-5.3"; E2E no servidor idem. Deploy: `ZAI_API_KEY` espelhada no `/root/.dsh/deepseek_env` (backup `.bak_pre_glm_20260829`; conferência por hash idêntico `f1bed2fb`, valor nunca exibido) + patch gravado na camada de usuário do perfil web (`profiles/web/cordis.patch.yml`, backup `.bak_pre_glm_20260829`) + restart do `dsh-web`. **Resultado: GLM 5.3 é o modelo PADRÃO do harness; DeepSeek segue disponível como alternativo na mesma tela.** Serviço active, 200 local, 401 sem senha de fora.

**3. CORREÇÃO IMPORTANTE — o harness NÃO mora no "NYC":** os Adendos 6–8 chamaram o servidor de "NYC", mas o IP do sslip.io (`190.89.239.65`) é o do **servidor de hospedagem do WP** (alias ssh `cafezinho-wp`, porta 51439). O `nyc` de verdade (198.199.121.136, onde rodam os crons v4_labs) NÃO tem `.dsh` nem serviço — verificado ao vivo hoje. Consequência boa: o harness está na MESMA máquina do WordPress ⇒ **o DeepSeek consegue publicar no Cafezinho nativamente via wp-cli** (`--path=/var/www/ocafezinho --allow-root`) — resposta à pergunta do Miguel. Preparar esse fluxo de publicação fica atrás de um "vai". A proposta do Adendo 8 (clonar o Cérebro "no NYC") deve mirar o servidor certo se um dia andar.

**4. Link reenviado no Telegram (~11:52):** `https://dsh-190-89-239-65.sslip.io` · usuário `miguel` · senha a mesma das 04h20 (nos 3 cofres, não reexposta). Prova de entrega: contador `tg_send_erro` imóvel (53).

**5. Laura:** missão **ZM-20260829-002** gravada na ponte CANÔNICA (`~/cerebro-miguel` → `cerebro/Foruns/ponte_laura_completa/de_dell.md`, commit `336b452a`) com a receita completa (Node ARM64 → npm → chaves via cofre local dela sem expor → patch acima → E2E). ⚠️ Descoberta do caminho: a ponte antiga (arquivo local `Antigravity Google/Cerebro/...`) NUNCA chegou ao GitHub (sync exclui `ponte_laura_completa/`) — a missão ZM-001 de 01:25 nunca chegou na Laura; a migração CM-20260829-001 (12:05) corrigiu o transporte, e a ZM-002 já foi pelo fluxo novo.

## ➕ ADENDO 10 — 29/08 13:35 BRT: POR QUE o iPad (e qualquer aparelho) não funcionava — fence 403 do /api + CORREÇÃO + Samsung liberado

**Pedido do Miguel (~13:15, voz):** "não conseguimos usar o harness no iPad; vai dar certo no smartphone Samsung? Investiga e manda o link com a credencial na Ponte Cafezinho."

### Diagnóstico (causa raiz PROVADA nos logs)

- O log dedicado `/var/log/nginx/access.dsh.log` mostra: usuário `miguel` **passava** no basic auth, a página carregava (200), mas **TODA chamada `/api/*` voltava 403** — `host.describe`, `credentials.describe`, `agentPreset.list`, `events.mux` etc., de TODOS os aparelhos (iPad/iPhone/Firefox-Mac, Edge da Laura, Linux). Só `/plugins/events` e assets passavam. Sintoma visível: UI trava no carregamento, nada funciona — o que o Miguel viu no iPad.
- **Causa:** o DSH tem uma cerca de segurança "browser-trust" no `/api` (`dsh-client-connection`, função `isTrustedApiRequest`): o header `Host` do pedido precisa ser loopback OU estar declarado em `trustedHosts`; senão 403 (proteção contra DNS rebinding/CSRF — o Host é o único header que rebinding não forja). O serviço no servidor subiu SEM `--trusted-host`, então o hostname público `dsh-190-89-239-65.sslip.io` era rejeitado. (No Dell a cerca já estava tratada na rota LAN 3081 — por isso lá funcionava.)
- Detalhe confirmado no código: entrada de trustedHost SEM porta casa com qualquer porta; `Origin` do navegador precisa casar com o Host (casa); alguns métodos seguem loopback-only mesmo com trust (diálogos nativos — irrelevante no servidor).

### Correção aplicada (com backup)

- `ExecStart` do `/etc/systemd/system/dsh-web.service` ganhou `--trusted-host dsh-190-89-239-65.sslip.io` (backup `/root/dsh-web.service.bak_pre_trusted_host_20260829`) + daemon-reload + restart.
- **Provas:** `/api/host.describe` via nginx com auth → 200 (resposta confirma provider `zai`, modelo `glm-5.3` — GLM segue padrão) · `/api/workspace.list` → 200 (`items: []` — servidor ainda sem workspace registrado) · teste externo do Dell com User-Agent de Samsung Android (SM-S928B, Chrome 151 Mobile) → página 200 + `/api` 200.

### Veredito mobile (pergunta do Miguel)

- **Samsung: SIM, vai funcionar.** Página tem viewport responsivo (`width=device-width`) + manifest PWA (dá "Adicionar à tela inicial"); toda a comunicação é HTTP/SSE padrão (nada de API exótica de navegador).
- **Seletor de pasta:** no servidor headless o DSH resolve o picker para o backend `browse` (lista de diretórios via RPC `host.listDirectory` — o log de 13:21 já mostra esse método sendo chamado) — funciona em QUALQUER navegador, não depende de File System Access API (que não existe em mobile). O Miguel navega as pastas DO SERVIDOR pela UI e escolhe `/root/dsh_workspace`.
- **iPad: destravado também** — a correção vale para todos os aparelhos; pode retestar.
- Entrega no Telegram: link + usuário `miguel` + senha `DSH_WEB_PASSWORD` (valor não reexposto aqui; está nos 3 cofres). Prova de envio: `tg_send_erro` imóvel (53).

### ⚠️ Lição registrada

DSH atrás de reverse proxy com hostname público EXIGE `--trusted-host <hostname>` no serviço, senão a UI carrega mas a API fica 403 (falha silenciosa e confusa — parece problema do aparelho). Vale para qualquer exposição futura do `dsh web`.

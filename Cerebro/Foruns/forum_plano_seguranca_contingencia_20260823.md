# 🔐 FÓRUM — PLANO TOTAL DE SEGURANÇA & CONTINGÊNCIA DO ECOSSISTEMA

**Aberto:** 23/08/2026 ~01:00 BRT · **Dono:** Miguel · **Executor:** ZCode (GLM-5.3 na abertura)
**Ordem do Miguel (23/08 ~00:55):** "temos que começar um plano total de segurança e planejamento de contingência para todo o nosso sistema, cafezinho, gdrive, github, vercel, godaddy, redes sociais, tudo. tudo que usamos. whatsapp, telegram, gmail, tudo. agenda de 48h em 48h para a gente pensar nisso e ir desenvolvendo."
**Papel deste arquivo:** DOCUMENTO-MESTRE VIVO do plano — inventário, riscos, pilares, **agenda 48h** e estado da missão. Memória técnica: `../Memorias/memoria_plano_seguranca_contingencia_20260823.md`.
**⚠️ Regra de ouro (Regra do Cofre, intacta aqui):** NUNCA escrever valores de chaves/senhas/tokens neste fórum — só caminhos, nomes de chave e status.

---

## 🎯 Objetivo

O ecossistema cresceu rápido (dezenas de contas, 4+ servidores, 6+ sites, bots, redes sociais, 15+ chaves de LLM/API) e a segurança até agora foi **reativa** (SEV-1 das chaves no GitHub, crontab destruído, Safe Browsing, proxy morto...). Este plano torna a segurança **proativa e permanente**: saber tudo o que temos, proteger cada peça, saber recuperar cada peça, e treinar isso em cadência de 48h até cobrir tudo — depois virar manutenção trimestral.

**Meta final:** nenhuma conta, domínio, servidor, site ou canal pode ser perdido por falta de acesso, backup, ou plano de recuperação.

---

## 🗺️ Superfície do ecossistema (inventário v0 — pré-preenchido do Cérebro; "?" = confirmar com o Miguel na S1)

### 1. Identidade raiz (a chave de tudo)
| Ativo | Observações |
|---|---|
| Gmail principal do Miguel | recuperação de quase tudo passa por aqui — status 2FA "?" |
| Gmails secundários/alias | ? (quantos, para quê) |
| Telefone (SIM) | recovery de 2FA — e se o chip for clonado/perdido? |
| Password manager | ? (existe? onde?) |
| PC Dell (máquina do Miguel) | acesso local a cofres e Cérebro |
| PC Laura (Samsung Book Go, Win11 ARM64) | segunda máquina, ZCode + loops instalados |

### 2. Cérebro & conhecimento
| Ativo | Cópias |
|---|---|
| Cérebro canônico local | `/Downloads/Antigravity Google/Cerebro/` |
| GitHub `cerebro-miguel` | privado; sync a cada 15 min (script + trilho git) |
| Backblaze B2 | espelho (NODE_BACKUPS_BACKBLAZE) |
| Google Drive | espelho (Cerebro_Backups, espelho-zcode etc.) |
| Pendrive 2079-8A26 | **descontinuado como espelho (Emenda 6, 20/08)** — só cofre SSH selado |

### 3. Sites & domínios
| Site | Onde vive | Domínio (GoDaddy?) |
|---|---|---|
| O Cafezinho (WP canônico) | servidor cafezinho-wp (`/var/www/ocafezinho`, WP 7.0.4) | ocafezinho.com |
| Cafezinho espelho | droplet DO 159.65.177.60 | cafezinho.news |
| Moka Reader | Vercel | mokareader.com |
| Moka espelho | Vercel | moka-espelho.vercel.app |
| Portal LOGIS | Vercel logis-magazine + espelho congelado logis-mirror | domínio anexado (confirmar qual) |
| Controle Logístico | Vercel | controlelogistico.vercel.app |
| Temáticos (7+ sites: Aiatolah, Mapa Rio, Mundo Trilhos...) | ? | ? |
| Filhos da Impunidade (FdI) | Vercel + GitHub público | ? |

### 4. Servidores & infra
| Servidor | Papel | Acesso |
|---|---|---|
| NYC (Tencent/Alibaba) | workers V4, GSN, crons, agente YouTube | SSH chave (cofre_ssh) |
| Droplet DO | espelho WP | SSH |
| cafezinho-wp (canônico) | WP produção + wp-cli | SSH `cafezinho-wp` / `cafezinho-wp-ro` |
| Tencent (painel CCTV v6, caçadora) | painéis + vigilância | SSH |

### 5. Contas de plataforma
| Plataforma | Usada para | Pendências conhecidas |
|---|---|---|
| GitHub (migueldorosario1 + outras?) | repos: cerebro-miguel (privado), logis, moka-espelho, casadamoeda, moka, filhosdaimpunidade (**PÚBLICO**) | 2FA?; revisar PATs/deploy keys/tokens; **bug aberto: git contaminado na Antigravity Google pushando p/ o FdI público** |
| Vercel | mokareader, moka-espelho, logis×2, controlelogistico, FdI | 2FA?; SSO desativado nos projetos (lição Safe Browsing) |
| GoDaddy | domínios + e-mails info@ (IMAP p/ painel Moka) | renovação automática em todos? registrar lock? |
| Supabase | Moka (auth/banco) | 2FA?; allowlist redirect (pendente Miguel) |
| Google (GA4, Search Console, Service Accounts) | analytics, indexação GSN (indexing_key.json) | SA exposta no histórico git (SEV-1) |
| Cloudflare? | ? | confirmar se usa DNS/CDN |

### 6. Chaves LLM/API (valores só no Cofre — aqui só o mapa)
Onde vivem: `.env.unificado` (espelhado 2 lugares), cofres do NYC (`chaves.sh`), cofres Laura, config dos apps. Famílias: DeepSeek, Moonshot/Kimi, Z.ai GLM, Qwen, OpenAI, Anthropic, Perplexity, Brave, AssemblyAI, IPRoyal (proxy), Flickr, visão (Google?), WP application passwords, bots Telegram.
Pendências herdadas: **rotação pós-SEV-1 ainda não fechada** (chaves seguem no histórico git do cerebro-miguel — decisão do Miguel foi HOLD relaxado 18/08).

### 7. Comunicação & redes sociais
| Canal | Uso | Risco |
|---|---|---|
| Telegram | Ponte Cafezinho (bot + chat do Miguel), avisos de automações | token do bot; 2FA da conta |
| WhatsApp | recebimento de PDFs (jornais) e contato | conta pessoal do Miguel |
| Gmail | identidade raiz | ver item 1 |
| X/Twitter | @ocafezinho? API paga + enxame (comentários automáticos — risco de ban) | tokens API; 2FA |
| Instagram | perfil Cafezinho | sem API; 2FA |
| Facebook | página Cafezinho | 2FA |
| YouTube | agentes (OAuth) | tokens; 2FA |

---

## 🔥 Por que este plano existe — incidentes e riscos já vividos

1. **SEV-1 (18/08):** 4 chaves SSH privadas + 4 .env + rclone.conf commitadas no GitHub (repo privado, mas histórico permanente). Contenção feita; rotação segue pendente.
2. **Git contaminado (22/08, bug ABERTO):** pasta Antigravity Google empurra commits do Cérebro para o repo **público** filhosdaimpunidade. Decisão do Miguel pendente.
3. **Crontab NYC destruído (23/08):** edição parcial derrubou 25KB→310B de agendamentos. Restaurado; lição: crontab sempre via arquivo completo + backup.
4. **Safe Browsing (22/08):** login-wall da Vercel marcou o portal LOGIS como "perigoso" no Chrome. Remediação via Search Console.
5. **Proxy IPRoyal 402 (20-22/08):** falha silenciosa engolindo coleta RSS/fotos por dias.
6. **Cadeia LLM frágil:** Kimi suspensa (429), OpenAI/DeepSeek sem crédito repetidamente — mitigado por cascata + failover, mas sem "plano B" formal por provedor.
7. **DNS local instável (Laura, à noite):** timeouts falsos de "servidor fora".
8. **Vazamento de metas REST no site (19/08):** fechado, mas mostra superfície pública exposta.
9. **Risco estrutural:** conhecimento concentrado — quase todos os acessos passam pelo Miguel, pelo Dell e pelo Gmail. Se um deles cai, quanto do ecossistema para?

---

## 🏛️ Os 8 pilares

| # | Pilar | Objetivo | Entregável final |
|---|---|---|---|
| P1 | **Identidade & Recuperação** | 2FA em toda conta raiz; códigos backup impressos; caminho de recuperação sem o Dell | matriz contas×2FA 100% verde + kit impresso |
| P2 | **Segredos & Cofres** | inventário completo (nome+caminho, sem valores); rotação das críticas; escaneamento de vazamento nos repos; política de revogação | mapa de credenciais + gitleaks limpo + rotação pós-SEV1 fechada |
| P3 | **Backups & Restore PROVADO** | 3-2-1 verificado para Cérebro, sites WP, configs de servidor, projetos Vercel; **provar restauração de verdade** (não só backup) | relatório de restore testado por sistema + RPO/RTO definidos |
| P4 | **Domínios, DNS & E-mail** | renovação automática + registrar lock + alerta de expiração duplo; DNS documentado por domínio | calendário de expirações + DNS map |
| P5 | **Servidores** | SSH por chave sem senha-root-remota; firewall; updates; monitor de disco; backup automático de crontabs/configs; acesso console do provedor testado | checklist aplicado nos 4 servidores |
| P6 | **Sites & Plataformas** | WP: admins revisados, 2FA no login, plugins atualizados, mu-plugins versionados; Vercel: SSO off em produção, teams revisado; Supabase/GA: SA mínimas | hardening aplicado e documentado |
| P7 | **Redes Sociais & Canais** | 2FA em X/IG/FB/YT/Telegram; revisão de tokens de API e apps conectados; runbook "conta comprometida/sequestrada" por rede | matriz social + runbooks |
| P8 | **Resposta a Incidentes** | runbook por cenário + Kit de Emergência físico impresso (contatos, passos, onde estão as senhas mestras — no cofre físico, nunca no digital) + simulado anual | kit impresso + simulado feito |

---

## 📅 AGENDA 48h (uma sessão a cada 48h — automação dispara 10:00 nos dias ímpares da cadência)

> Formato de cada sessão: o agente PREPARA na véspera (coleta o que não depende do Miguel) → sessão com o Miguel (~30-60 min de decisões) → agente executa e registra adendo aqui. Ordem pensada do mais crítico para o menos crítico.

| Sessão | Data-alvo | Bloco | Entregável | Precisa do Miguel |
|---|---|---|---|---|
| **S0** | 23/08 ✅ | Abertura do plano | este fórum + memória + nodo + automação 48h no ar | nada (feito) |
| **S1** | 25/08→27/08 (⏳ deslizou — sessão com o Miguel pendente) | **P1 Identidade raiz** | matriz contas×2FA (§S1 abaixo) com status real; lista do que falta 2FA; decidir password manager | ~40 min: revisar contas juntos, ligar 2FA faltantes, gerar+cópias dos códigos backup |
| **S2** | 27/08 10:00 | **P2 Segredos** | inventário de credenciais por cofre (nome+hash, sem valores); gitleaks/trufflehog nos repos; decidir rotação pós-SEV-1; política "chave nova = velha morta" (Regra Nº 4) aplicada ao histórico | decisões de rotação (quais/Quando) |
| **S3** | 29/08 10:00 | **P3 Backups & Restore** | mapa 3-2-1 por sistema; **teste de restauração real** (Cérebro do B2/Drive → tmp, conferir; WP: dump+restore em ambiente seguro; Vercel: rollback de teste no espelho) | autorizar janelas de teste |
| **S4** | 31/08 10:00 | **P4 Domínios & DNS** | inventário GoDaddy completo; renovação auto + lock em todos; calendário de expirações com alerta duplo (Telegram + e-mail); DNS map por domínio; e-mails info@ | confirmar domínios/contatos de registro |
| **S5** | 02/09 10:00 | **P5 Servidores** | checklist por servidor (SSH/firewall/updates/disco/backup de crontab com a lição de 23/08); acesso console do provedor testado; senhas root em cofre físico | credenciais de console (GoDaddy/DO/Tencent/Alibaba) |
| **S6** | 04/09 10:00 | **P6 Sites & WP** | admins WP revisados + 2FA login; plugins desatualizados; mu-plugins versionados no git; Vercel team/SSO auditado; Supabase keys rotacionadas se preciso | aprovar mudanças no WP de produção |
| **S7** | 06/09 10:00 | **P7 Redes sociais & canais** | matriz social×2FA×tokens; apps conectados revistos; runbook "conta comprometida" por rede; política enxame vs. ban | 2FA nas contas pessoais dele |
| **S8** | 08/09 10:00 | **P8 Runbooks** | playbook de incidente por cenário (Gmail comprometido; servidor caiu; domínio expirou; site hackeado; repo vazado; LLM morto; PC perdido) + **Kit de Emergência impresso** | revisar/imprimir kit |
| **S9** | 10/09 10:00 | **Simulado tabletop** | escolher 2 cenários e SIMULAR a resposta (cronometrar RTO real), corrigir o que travar | participar do exercício (~1h) |
| **S10** | 12/09 10:00 | **Fechamento da fase intensiva** | painel de status (página no CCTV /v6?); cadência de manutenção trimestral; lições; plano v2 | validar cadência futura |

> Se uma sessão atrasar, a agenda DESLIZA (mantém 48h entre sessões). Bloco só marca ✅ com entregável gravado aqui.

---

## 🧾 S1 — Preparação (25/08/2026 ~01:02 BRT, ZCode/GLM-5.3)

### Checagens feitas agora (sem depender do Miguel)

1. **GitHub (`gh` do Dell):** logado como `migueldorosario1` via keyring; token com escopos `repo, gist, read:org`. O campo 2FA da API veio **inconclusivo** (`null`) — confirmar em github.com → Settings → Password and authentication.
2. **Inventário real de repos: 33 no total, só 3 privados** (`cerebro-miguel`, `GA4-Manus`, `moka-video`) — **30 PÚBLICOS**. O inventário v0 deste fórum subestimava a superfície. Lista completa (privados em negrito): **cerebro-miguel**, **GA4-Manus**, **moka-video**, aiatolah, aiatolah-v4, cafezinho, cafezinho-publicador, cafezinho_news, cafezinhomediagroup, casadamoeda, ceara-digital, ceara-v4, cicero, discover-brazil, discoverbrazil-v4, filhosdaimpunidade, gabriel-publicador, global-south-news, globalsouth-v4, igot, logis, mapario, mapario-v4, maquiavel, moka, moka-espelho, mokawriter, mundo-trilhos, mundotrilhos-v4, qwenlab, rail-post, railpost-v4, rio-carta, riocarta-v4. *(Insumo direto para S2: escaneamento de segredos nos 30 públicos.)*
3. **Nuvens/cofres (rclone, só nomes):** 11 remotes — `drive, gdrive, b2, b2-labs, masterb2, gdrive-backup-b2, b2_orlando, b2-tematicos, legacy-cafezinho, reforma_tencent_cafezinho, r2`.
4. **Vercel:** nenhuma chave `VERCEL*` nos `.env.unificado` (o token vive em outro cofre — mapear na S2). 2FA da conta não é checável por API → sessão.

### Matriz contas × 2FA × recuperação (rascunho — "?" = preencher com o Miguel na sessão)

| Conta | Como se entra hoje | 2FA | Recuperação se perder | Ação S1 |
|---|---|---|---|---|
| Gmail principal do Miguel | senha no navegador? | **?** | chip do telefone? | ligar/confirmar 2FA (app autenticador, NÃO SMS se der) + **gerar e imprimir códigos backup** |
| Gmails secundários/alias | ? | **?** | ? | listar todos e repetir |
| GitHub migueldorosario1 | gh keyring + senha | **?** (API inconclusiva) | e-mail do GitHub | conferir 2FA + recovery codes impressos; revisar SSH keys/PATs/apps conectados |
| Vercel | ? (login social?) | **?** | ? | conferir 2FA + método de login (GitHub?) |
| GoDaddy | senha? | **?** | e-mail/tel | 2FA + **conferir contatos de registro** (registrante/e-mail/tel de TODOS os domínios) |
| Supabase | GitHub login? | herda? | ? | conferir |
| Telegram (conta pessoal) | app do celular | **?** (= senha na nuvem) | e-mail de recuperação? | ativar senha na nuvem + e-mail de recuperação |
| WhatsApp | celular | **?** (PIN 2 etapas) | e-mail? | ativar PIN de 2 etapas + e-mail |
| X/Twitter | ? | **?** | ? | 2FA + revisar apps conectados (API do enxame!) |
| Instagram / Facebook | ? | **?** | ? | 2FA |
| YouTube/Google (OAuth dos agentes) | = conta Google | idem Gmail | — | revisar **apps OAuth autorizados** e limpar os mortos |
| Backblaze B2 | ? | **?** | e-mail | 2FA |
| Consoles de servidor (Tencent/Alibaba NYC, DigitalOcean, serverdo.in) | ? | **?** | e-mail/tel | 2FA em cada + **testar login pelo console web 1×** (acesso de emergência sem SSH) |
| Password manager | — | — | — | **decidir na sessão**: adotar um (ex.: Bitwarden/1Password/KeePassXC) ou manter como faz hoje documentado |

### Roteiro da sessão (~40 min com o Miguel)

1. (5 min) Miguel responde os "?" da matriz — o agente preenche em tempo real.
2. (25 min) Ligar 2FA onde faltar, na ordem: Gmail → GitHub → Vercel → GoDaddy → Telegram → WhatsApp → consoles. Em cada uma: app autenticador + imprimir códigos backup.
3. (5 min) Decidir password manager.
4. (5 min) Definir onde vivem os códigos backup impressos (cofre físico da casa) — base do Kit de Emergência (P8).

### Auditoria de acessos GitHub (27/08 ~01:00, read-only)

- **Orgs: nenhuma** — conta pessoal pura (`gh api user/orgs` vazio).
- Chaves SSH da conta e apps OAuth autorizados **não são listáveis com o token atual** (escopos `repo, gist, read:org`; listar exige `admin:public_key` / página web) → virou item de 2 min da sessão: Settings → SSH and GPG keys + Settings → Applications.
- PATs (tokens clássicos) só são visíveis na web → revisar na sessão (inclui o token usado pelo gh do Dell).

### 📱 Roteiro "S1 no celular" (o Miguel pode fazer SOZINHO, ~15 min, sem o Dell)

1. **Telegram**: Configurações → Privacidade e segurança → **Senha de verificação em duas etapas** → definir senha + **e-mail de recuperação**.
2. **WhatsApp**: Ajustes → Conta → **Verificação em duas etapas** → ativar PIN + e-mail.
3. **Gmail** (navegador ou app): Conta Google → Segurança → **verificar se a Verificação em duas etapas está ATIVA**; se não, ativar com app autenticador (não SMS) e **salvar os códigos backup**.
4. Se sobrar tempo: 2FA no X e no Instagram (Configurações → Segurança).

*Feito isso, a parte no PC comigo (GitHub, Vercel, GoDaddy, Supabase, consoles) cai para ~20 min.*

### 🔎 Varredura antecipada de segredos em repos públicos (29/08 ~01:05, antecipação da S2/P2)

Motivo: o bug aberto do git contaminado (pushes da Antigravity Google → repo **público** filhosdaimpunidade) faz valer uma varredura antes da S2 oficial.

- **Método:** clones shallow em `/tmp` dos 7 públicos mais expostos (filhosdaimpunidade, cafezinhomediagroup, logis, moka, moka-espelho, globalsouth-v4, casadamoeda) + grep por 10 padrões de segredo (OpenAI sk-, AWS AKIA, Google AIzaSy, ghp_/gho_/github_pat_, Slack xox, PRIVATE KEY, DO dop_v1_, Telegram bot, SendGrid SG.).
- **Resultado: 1 padrão real** — chave Google `AIzaSy…` (mascarada) embutida em **2 HTMLs de "fontes baixadas" de terceiros** no repo filhosdaimpunidade (`Kimi K3/fontes_baixadas/cap1…` e `cap4…`, linha 21 de cada). **Confirmado por comparação: NÃO está em nenhum cofre/env do ecossistema** → chave de TERCEIRO (veio junto com o HTML baixado para pesquisa do livro). Risco p/ nós: 🟡 baixo (higiene).
- **Ação sugerida (p/ S2):** remover os HTMLs do repo ou mascarar a linha (decisão do Miguel); replicar a varredura nos 30 públicos restantes.
- **TESTE DE VALIDEZ (29/08 ~01:10, pedido do Miguel):** 2 requisições GET mínimas, não destrutivas. YouTube Data API → **HTTP 403 `accessNotConfigured` nomeando o projeto Google `306562085637`** = o Google RECONHECEU a chave (chave inválida daria 400 "API key not valid") → **chave VÁLIDA/viva**, do projeto do publicador original. Contexto do HTML: `subscriptions.configure({apiKey, publicationId: 'CAowmfCQCw'})` = **Subscribe with Google** — widget de assinatura do jornal-fonte. **Classificação final: risco p/ o ecossistema ≈ NULO** — chave publishable por design (todo visitante do site original a recebe no navegador) e do projeto de TERCEIRO, não do nosso. Higiene opcional na S2 (remover/mascarar os HTMLs); sem urgência.
- Clones de `/tmp` descartados após a análise.

---

## 🔴 SEV-1-20260831-01 — VAZAMENTO DO COFRE DE CHAVES EM REPO PÚBLICO `cafezinho_news`

**Descoberta:** varredura da 4ª rodada do plano (31/08 ~01:00) — o repo **público** `migueldorosario1/cafezinho_news` (último push 09/06/2026, público há ~3 meses) continha cópia inteira do "Projeto Cafezinho Agentes", incluindo cofres:

| Arquivo exposto | Conteúdo sensível |
|---|---|
| `root/.env.unificado` | **102 variáveis**: 6 chaves OpenAI, 2 Google, **10 tokens de bots Telegram**, 1 GitHub token, senhas WP de 6 sites, **senhas cPanel**, X/FB completos |
| `root/chaves_novas.env` + `root/chaves.sh` | mais 1 OpenAI + 1 Google + 6 Telegram + 1 GitHub (chaves.sh) |
| `root/ga4.json` | **Service Account Google COM private_key** |
| `root/painel_v5/.github_token` | token GitHub |
| `Outros/chaves/kimi.env`, `.env.claude_telegram`, `.env.codex_telegram`, `backup_root/.env.unificado` | chaves Moonshot/OpenAI + tokens Telegram |
| ~40 agentes `.py` + `__pycache__` | padrões de segredo embutidos |

**Contenção (31/08 01:03 BRT, autônoma — mesmo precedente do SEV-1 de 18/08):** repo tornado **PRIVADO** via `gh api` (verificado: 404 público na API e na web). Nada apagado; ação reversível. Telegram 🔴 enviado ao Miguel (~01:05).

**Cruzamento com o cofre atual (local, por valor, SEM expor valores):** das 102 expostas, 92 existem hoje · **59 com valor IDÊNTICO = ainda vivas e em uso (rotação urgente)** · 24 já rotacionadas · 10 prováveis mortas.

**Prioridade de rotação das 59 (nomes; grupos):**
1. 🔴🔴 **Acesso a contas:** `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, `X_API_KEY`, `X_API_KEY_SECRET`, `X_BEARER_TOKEN` (API X completa) · `FB_PAGE_ACCESS_TOKEN` (página Facebook) · `CPANEL_MIGUEL_PASS`, `CPANEL_COMERCIAL_PASS` · `WP_USER/PASS_RIOCARTA`, `MAPA_RIO_WP_*`, `DISCOVER_BRAZIL_WP_*` · **10× `TELEGRAM_*_TOKEN`** · SA do `ga4.json` (conferir se a atual é a mesma) · `GITHUB_TOKEN`/`.github_token` (painel_v5)
2. 🔴 **APIs pagas:** `ELEVENLABS`, `HEYGEN`, `IDEOGRAM`, `CREATOMATE` (+8 template IDs), `FAL`, `FIRECRAWL`, `FLICKR`, `NEWSAPI`, `TRANSKRIPTOR`, `UPTIME_ROBOT`, `BEA`, `BLS`, `FRED`, `XAI_API_KEY_MAPA_RIO`, `XAI_SCRIBE_STT_KEY`, `MANUS_API_KEY`
3. 🟡 **IDs não-secretos (baixo risco):** `FB_PAGE_ID`, `IG_USER_ID`, `WP_SITE*`, `ELEVENLABS_VOICE_ID*`, `GA4_PROPERTY_ID`, `CEO_KIMI_MODEL`, `ZIZI_CLAUDE_MODEL`, `GOOGLE_APPLICATION_CREDENTIALS` (caminho)

**Pendências do Miguel:** (1) "vai" para o plano de rotação por grupos (proponho X/FB → Telegram → WP/cPanel → APIs pagas; espelho nos cofres conforme Regra Nº 4); (2) decidir se apagamos os arquivos/histórico do repo (BFG/git-filter vs manter privado); (3) S1 de 2FA — hoje ainda mais urgente.

*Higiene: clones de /tmp descartados; nenhum valor de segredo foi exibido em chat, fórum ou Telegram (só nomes/contagens).*

---

## 📊 Estado da missão (o que aconteceu / o que falta / o que preciso de você)

- **O que aconteceu:** S0–S1-prep-3 (23–29/08) conforme histórico abaixo. **31/08 01:00 — 🔴 SEV-1-20260831-01:** varredura completa dos 24 públicos restantes achou o cofre de chaves inteiro no repo público `cafezinho_news` (~3 meses exposto). **Contido em 3 min** (repo → PRIVADO, 404 público verificado); cruzamento com cofre atual: **59 chaves vazadas ainda vivas** (X/FB completos, 10 bots Telegram, senhas WP/cPanel, SA Google, APIs pagas) — listas e grupos de rotação no §SEV acima. Demais 23 repos públicos limpos. Telegram 🔴 enviado.
- **O que falta:** (1) **"vai" do Miguel p/ rotação das 59** (grupos propostos); (2) decisão sobre apagar conteúdo/histórico do repo; (3) sessão S1 (2FA) — pendente desde 25/08; (4) S2–S10.
- **O que preciso de você (Miguel):** AGORA: autorizar a rotação (digo a ordem e espelho nos cofres sozinho, Regra Nº 4) + decidir histórico do repo. DEPOIS: a S1 de 2FA de uma vez — com chaves vazadas vivas, contas sem 2FA são a porta aberta.

---

## 🔁 Automação

- Automação ZCode "Plano de Segurança 48h — rodada" (`automation-86575fb8`): dispara a cada 48h (primeiro gatilho: 25/08 01:02 BRT) → lê este fórum, prepara a próxima sessão (coleta o que não depende do Miguel), grava adendo no Histórico abaixo e manda UM resumo no Telegram do Miguel com a pauta + até 3 decisões pendentes.

---

## 📜 Histórico de rodadas (append-only)

- **S0 — 23/08/2026 ~01:05 BRT (ZCode/GLM-5.3):** abertura. Fórum+memória+nodo `CEREBRO_NODE_SEGURANCA_CONTINGENCIA.md`; autoria do Tema Duplo catalogada; automação 48h criada; MONITORAMENTO_DE_TRABALHO assinado. Nenhuma mudança de produção.
- **S1-prep — 25/08/2026 ~01:02 BRT (ZCode/GLM-5.3, rodada da automação):** preparação da S1 concluída. Checagens locais: gh autenticado (keyring, escopos repo/gist/read:org); **33 repos GitHub (30 públicos — inventário v0 subestimava)**; rclone 11 remotes; 2FA GitHub inconclusivo via API. Matriz contas×2FA + roteiro de 40 min gravados (§S1). Sessão com o Miguel agendada para quando ele acordar (Telegram enviado). Zero mudança de produção; nenhum segredo exposto (só nomes/caminhos).
- **S1-prep-2 — 27/08/2026 ~01:00 BRT (ZCode/GLM-5.3, 2ª rodada da automação):** S1 AINDA SEM SESSÃO → agenda desliza (regra: nunca pula). Reforço: auditoria read-only de acessos GitHub (sem orgs; chaves SSH/PATs/OAuth grants não listáveis com token atual → item de sessão na web) + **roteiro "S1 no celular"** (Telegram/WhatsApp/Gmail, ~15 min sozinho) gravado no §S1. Telegram de cobrança enviado. Zero mudança de produção.
- **S1-prep-3 — 29/08/2026 ~01:01 BRT (ZCode/Qwen 3.8, 3ª rodada da automação):** S1 continua sem sessão (3ª seguida). **Antecipação da S2:** varredura de segredos em 7 repos públicos (clones shallow + 10 padrões) → **1 achado 🟡 baixo risco**: chave Google de terceiro embutida em 2 HTMLs de fontes baixadas no repo público filhosdaimpunidade; comparada com os cofres — não é do ecossistema; limpeza sugerida p/ S2. Demais 6 repos limpos nos padrões varridos. Telegram enviado; clones /tmp descartados. Zero mudança de produção.
- **S1-prep-4 — 31/08/2026 01:00→01:20 BRT (ZCode/GLM-5.3, 4ª rodada da automação):** varredura completa dos 24 repos públicos restantes → **🔴 SEV-1-20260831-01: repo público `cafezinho_news` continha o cofre de chaves inteiro** (.env.unificado 102 vars + chaves.sh + ga4.json c/ private_key + .github_token + kimi.env + ~40 agentes). **Contenção autônoma 01:03: repo tornado PRIVADO** (404 público verificado; nada apagado). Cruzamento por valor com cofre atual: **59 chaves idênticas = vivas** (grupos de rotação no §SEV). Demais 23 repos limpos. Telegram 🔴 enviado ao Miguel. Tema duplo de incidente: este fórum §SEV + NODE_BUGS_ATIVOS.

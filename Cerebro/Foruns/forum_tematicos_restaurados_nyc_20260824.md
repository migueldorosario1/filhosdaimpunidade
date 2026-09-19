# 📰 Fórum — Sites Temáticos RESTAURADOS no NYC (2 posts/dia/site)

**Data:** 2026-08-24 (sessão ZCode/GLM-5.3, ordem do Miguel: "investiga porque os sites temáticos pararam de ser atualizados, e vamos restaurar a atualização deles, moderadamente, como eu pedi. 2 posts por dia para cada um")

## 1. Por que pararam (diagnóstico fechado)

1. **18/08 ~21:50** — crons de publicação desativados no Dell (5) e NYC (ceara-digital + cicero) para transferir a operação ao Loop Laura (pacote 8,3MB, ZM-041/042). A Laura rodou 1 rodada manual em 19/08 (2 publicados) e **nunca mais** — automação diária não pôde ser criada no app dela e ela priorizou o Cafezinho (CL-20260824-002 de 24/08 12:17 assumiu).
2. **Resultado:** 8 sites sem post novo desde 18-20/08 (confirmado ao vivo: riocarta e discoverbrazil com último post 18/08).
3. **Pêndulo de chaves:** a chave "sites temáticos" gerou 1,63M tokens em 18-24/08 sem publicar (matérias presas — ver memória `rio-carta-parado-cron-v4-dell-20260824`).

## 2. Onde renasceu (decisão estrutural)

**NYC (/root/tematicos/)** — NUNCA no Dell (regra `producao-zero-no-dell`). Código do Dell (canônico, `agentes_tematicos/`) copiado por pacote de 7,5MB (sem banco de mídia 2GB — cache; cascata Wikimedia→stock→IA cobre). 8 repos clonados em `/root/tematicos/sites-v4/` (GitOps SSH GitHub migueldorosario1 já autenticado no NYC). Cofre `/root/.env.unificado` do NYC tem todas as 8 chaves usadas (BRAVE/DEEPSEEK/GEMINI/KIMI/MOONSHOT/OPENAI/QWEN/ZHIPU).

## 3. Bugs encontrados e corrigidos na reinstalação

### 3.1 🔴 Visão morta no NYC (causa raiz do fail-close eterno)
- **Gemini direto:** IP do droplet NYC bloqueado — `User location is not supported for the API use`.
- **Qwen-VL endpoint privado (QWEN_API_KEY_2 + QWEN_BASE_URL_2, maas ap-southeast-1):** moderador de conteúdo devolve `data_inspection_failed` para **imagens arbitrárias** (foto de trem barrada; foto de pessoa com passaporte passa 3/3 — determinístico por conteúdo, não por mecanismo). Base64 NUNCA passa. Conta inteira (ALIBABA_API_KEY no dashscope-intl idem) tem o mesmo moderador → Alibaba inútil como juiz visual.
- **Zhipu GLM-4.5V:** 429 sem saldo (plano coding ≠ API aberta paga).
- **FIX DEFINITIVO (3 peças):**
  1. **Proxy de visão no tencent** (`/home/ubuntu/visao_proxy_gemini.py`, porta 127.0.0.1:8778): Cingapura não é bloqueada pelo Gemini; a chave GEMINI_API_KEY vive SÓ lá (nunca trafega ao NYC). Keepalive crontab */10.
  2. **Túnel SSH systemd no NYC** (`visao-tunnel.service`, `ssh -p 38422 -L 8778:127.0.0.1:8778 ubuntu@43.156.151.165`, Restart=always) — o gate chama `http://127.0.0.1:8778/`.
  3. **Patch `nucleo_visao.py`** (Dell canônico + NYC sincronizados): nova rota `_julgar_gemini_tencent` na cascata de `julgar_imagem` e `confirmar_imagem` → ordem agora **gemini → gemini-tencent → qwen-vl**. `_julgar_qwen` reescrito: pares coerentes chave↔base (`QWEN_API_KEY+QWEN_BASE_URL`, `_2+_2`, `DASHSCOPE_*`, `ALIBABA_API_KEY`) e modelo `qwen-vl-max`; imagem preferencialmente por **URL pública R2** (`_url_publica_r2`: sobe para `_gate_tmp/` no bucket do cofre e usa `R2_PUBLIC_URL`).
- **Prova (24/08 ~19:0x BRT):** positivo CONFIRMADA (trem↔matéria Taiwan) + negativo NAO_CONFIRMADA (foto de trem em matéria do Paes). Gate fail-close funcionando DE VERDADE.

### 3.2 🔴 R2_PUBLIC_URL faltava no cofre NYC
- `R2_PUBLIC_BASE_URL` (storage com auth) ≠ `R2_PUBLIC_URL` (domínio público r2.dev). Pares válidos: `cafezinho`↔pub-7c53d388…r2.dev (cofre do projeto) e `riocarta-hero-images`↔pub-f814950…r2.dev (cofre NYC). **Espelhado `R2_PUBLIC_URL` no cofre NYC** (Regra Nº 4). Nota: r2.dev bloqueia User-Agent de Python no GET — mas quem baixa a imagem é a Alibaba (server-side), que passa.

### 3.3 🔴 mundodostrilhos.com com DNS vazio (domínio caído)
- `dig @1.1.1.1` vazio = registro expirado/DNS removido. railpost.news, riocarta.com e discoverbrazil.news: 200 OK. **O pipeline do mundotrilhos segue publicando no repo (deploy Vercel segue); quando o domínio voltar o conteúdo já está lá. Ação do Miguel: verificar registrador.**

## 4. Ritmo (o "moderadamente, como eu pedi")

- Cron NYC: `0 12,18 * * *` UTC = **09:00 e 15:00 BRT**, `orquestrador.py --all --sem-youtube`.
- `posts_por_rodada=1` (configs já estavam) → **2 posts/dia por site** (desenho original do fórum de julho).
- `youtube.enabled=False` em todos (ordem 24/08: YouTube temático OFF, GSN dono único).
- Gates preservados: dedup fuzzy 70%, MD5 de hero, bloqueio >2 posts/dia, foco local/editorial por contrato, **confirmação de imagem fail-close**.
- Backup crontab NYC: `/root/crontab.bak_pre_tematicos_20260824` (164 linhas íntegras — lição SEV-1 respeitada).

## 5. Estado / o que falta / o que preciso do Miguel

- **Pronto:** código no NYC, 8 repos, cofre OK, visão viva (proxy+túnel), cron 2×/dia, rodada real de estreia disparada ~21:59 UTC (log `orquestrador_cron.log`).
- **Falta:** (a) 1ª rodada do cron automático amanhã 09:00 BRT para confirmar cadência; (b) indexação Google dos temáticos segue SEM credenciais (pendência antiga — publicador avisa e segue, fail-soft); (c) banco de mídia 2GB segue no Dell (cascata cobre; subir só se faltar imagem).
- **Preciso do Miguel:** (1) 🔴 **domínio mundodostrilhos.com** — verificar registrador (expirou?); (2) opcional: recarga Zhipu para 3ª rota de visão; (3) opcional: credenciais de indexação por site (`indexing_key_<site>.json`).

## Adendos

### Adendo 1 — 24/08 ~19:15 BRT: 1ª rodada de estreia em andamento
`--all --sem-youtube` disparada manualmente às 21:59 UTC para destravar os candidatos pendentes de hero (mundotrilhos/railpost/aiatolah tinham matérias prontas adiadas pela visão morta). Resultado na memória `tematicos-restaurados-nyc-20260824`.

### Adendo 2 — 24/08 ~19:35 BRT: whois do mundodostrilhos.com = DOMÍNIO DELETADO do registry
Pergunta do Miguel ("como assim domínio caído? no godaddy?"). Whois VeriSign: **"No match for domain MUNDODOSTRILHOS.COM"** — não é DNS desconfigurado nem expiração em período de resgate: o registro foi **removido do registry** (ciclo completo: venceu → ~45d de graça → ~30d redemption → deletado). Agora está **LIVRE para qualquer um registrar** — risco de squatter. Registrador do ecossistema = **GoDaddy** (cafezinho.news, mokareader.com; ver forum_plano_seguranca_contingencia_20260823 S4/P4 de 31/08 que já desconfiava "renovação automática em todos?"). **AÇÃO URGENTE Miguel: recomprar mundodostrilhos.com no GoDaddy (~R$60-80/ano) e reapontar DNS para a Vercel** (A/CNAME conforme os outros temáticos). Pipeline segue publicando no repo; site volta minutos depois do DNS.

### Adendo 3 — 24/08 ~19:45 BRT: 🔁 RETIFICAÇÃO DO §3.3 — domínio do Mundo Trilhos está BOM (falso alarme)
Print do painel do Miguel revelou: o domínio real dele é **mundotrilhos.com** (sem "DO") — registrado, DNS Vercel correto (A @ 76.76.21.21, CNAME www → cname.vercel-dns.com) e **no ar (200 OK, final www.mundotrilhos.com)**. O "mundodostrilhos.com" que eu testei (whois "No match") era nome **errado do fórum explicativo de julho** — provavelmente nunca foi dele. A config do agente NYC já usa `mundotrilhos.com` corretamente. **Não há pendência de domínio.** Última matéria do repo: 17/08 — a pendente de hero (Melbourne/Alstom) será rejulgada pela visão viva na próxima rodada do cron (09:00 BRT 25/08). Lição: validar domínio contra a CONFIG do agente, não contra documento antigo.

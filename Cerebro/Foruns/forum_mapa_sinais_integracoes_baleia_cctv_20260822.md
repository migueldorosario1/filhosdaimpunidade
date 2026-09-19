# Fórum — Mapa de Sinais de autoria + integrações Baleia Azul e Painel CCTV (22/08/2026)

**Data:** 2026-08-22 ~09:50→11:00 BRT · **Executante:** ZCode (GLM-5.3) · **Ordem:** Miguel ("mapa de sinais, para a gente sempre saber identificar quem fez o quê — até para acrescentar essa informação ao Baleia Azul e ao Painel CCTV")

## Decisões e entregas

1. **Documento vivo:** `Foruns/MAPA_SINAIS_AUTORIA_CAFEZINHO.md` — tabela-mestre de sinais, árvore de decisão, como consultar, lacunas.
2. **Sinal permanente novo (o salto):** mu-plugin `cafezinho-origem-post.php` no canônico grava meta **`_cafezinho_origem`** (`via` = rest|wp-cli|cron|admin|xmlrpc, `ua`, `user_id`, `ts`) em TODO post criado a partir de 22/08 — acaba com a ambiguidade "5786 sem meta". Provado: post de teste wp-cli → `{"via":"wp-cli"}`; via REST → `{"via":"rest","ua":"Antigravity/1.0 TESTE","user_id":5786}`.
3. **API de autoria:** `GET /wp-json/cafezinho/v1/autoria?horas=&limite=&fmt=json|md` (auth app password **"Integracoes-Autoria"** da 5786; 401 sem auth, 200 com; cache 60s). App password espelhada em 3 cofres (`AUTORIA_*` no `.env.unificado` Dell ×2 + `.wp_creds` Tencent) com backups `.bak_pre_autoria_20260822`. Incidente menor: 1ª senha gerada apareceu no terminal da sessão → **revogada na hora** e recriada direto em arquivo `/root/.autoria_apppass` (600).
4. **Painel CCTV:** página **`/v6/autoria`** no ar (menu "🧭 Autoria"; cards por classificação, filtros 6–168h, tabela com sinais, cache 5min). Backup `painel_cctv_v6.py.bak_pre_autoria_20260822`; provas 200 com dados reais (V4, Gabriel, Miguel, Motor V5).
5. **Baleia Azul:** wrapper `enviar_baleia_azul_ponte.sh` ganhou o passo 3.5 — anexa a seção "🧭 Quem fez o quê — últimas 24h" (API fmt=md) ao boletim antes do envio; vai também no Telegram das 19:30. Falha da API = boletim segue sem a seção (fail-soft). Prova ponta a ponte Dell→API→markdown OK.
6. **Forense do access log (resolvida a confusão dos IPs):** TODO tráfego externo chega pelos fronts 190.89.239.244/.31 (proxy do provedor) → **IP não identifica cliente; o sinal é UA + usuário autenticado**. Post 267017 ("meu de verdade", dívida externa) = criado 02:57 de 22/08 via REST **UA Antigravity/1.0 com `author=2018`** — Miguel via Manus (dentro do Antigravity). Post 266991 (Datafolha) = criado via **interno wp-cli** (mesmo sinal do motor) — a CM-057 atribuiu ao AGY-LAURA; a edição de 03:25 também interna.
7. **Bug corrigido no caminho:** WP REST envelopa string em JSON → `fmt=md` agora entrega `{"md": "..."}` e o wrapper extrai.

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **ACONTECEU:** mapa vivo + sinal gravado na origem + API + CCTV + Baleia, tudo no ar e provado.
- **FALTA:** (a) Motor V5 ainda não grava meta própria — recomendação `motor=v5` no publicador; (b) Manus × Antigravity CLI indistinguíveis pelo UA (solução: app passwords/contas separadas por ferramenta, se quiser granularidade); (c) posts pré-22/08 seguem pelo mapa histórico (forense).
- **PRECISO DE VOCÊ:** nada obrigatório. Opcional: decidir sobre (a) e (b).

**Catalogação:** tema curadoria/autoria — irmão de `forum_mapa_autoria_posts_v4_v5_humanos_20260821.md`. Registrado em CEREBRO_NODE_ATUALIZACOES.md (22/08).

## Adendo 1 (~10:35 BRT) — 📈 Views por post no /v6/autoria (ordem Miguel)

Página enriquecida: cruzamento autoria × audiência GA4. (1) API ganhou campo `slug` (matching com GA4 `ga4_posts_datados`, prop ...425); (2) cards por autoria agora mostram **views totais + nº posts + média/post + melhor post**; (3) ranking duplo: "✍️ quem PUBLICA mais" × "📈 quem PERFORMA melhor" (média views/post); (4) tabela ganhou coluna **Views** (posts de hoje = "—", GA4 fechado até ontem, padrão do painel). Provas 48h: 8 cards (topo 1.225 views), 76 células com views, rankings V4=60 posts/Gabriel=18. Mu-plugin reimplantado + `wp transient delete autoria_api_`. Views não entraram no Baleia (boletim segue só com a tabela de autoria — views são consultáveis no painel).

## Adendo 2 (~10:35 BRT) — Coordenação com a Ponte Laura Completa (ordem Miguel)

Miguel (22/08 ~10:20): "tudo coordenado com a ponte; qualquer coisa que mude o contrato = falar lá e pedir opinião; assinar contrato". Executado: (1) lido o dia na ponte — PROTOCOLO_SSH_AGENTES_v1 homologado 09:14-09:52 (11 users unix+WP 5788-5798, whitelist, Fase 2 = chaves); CL-20260822-004 (chave pública claude_laura + ACK mapa de sinais); AGY AL-059/060 (19º post do dia); ZL ativa (cctv/caçadora/heartbeat). (2) **Integração imediata:** classificador reconhece as 11 identidades SSH (rótulo `Agente <nome> (SSH v1)`, provado com draft zcode_miguel 5795). (3) **Fix bug GMT na API:** drafts wp-cli com `post_date_gmt=0000-00-00` invisíveis → filtragem PHP tolerante; pending agora visíveis. (4) **ZM-20260822-002** na ponte: relato + PEDIDO DE CHECK (4 perguntas) + proposta de EMENDA ao contrato (3 artigos: rastro de autoria obrigatório; API como fonte única de classificação; mudança de autoria/auditoria passa pela ponte antes) + divisão de trabalho para não bater cabeça. Aguardo CHECKs/pareces na ronda.

## Adendo 3 (~10:50 BRT) — 🔐 SIGILO: rótulos nunca públicos (ordem Miguel "óbvio, só reforçando")

Auditoria das 4 superfícies + 2 vazamentos REAIS fechados:
1. **Meta `_cafezinho_origem`:** nunca exposta (REST pública não lista; HTML limpo; API 401 sem auth) ✓.
2. **🔴 VAZAMENTO PREEXISTENTE FECHADO — REST pública expunha metas internas de pipeline:** `zizi_job_id`, `cafezinho_nomes_check`, `_agente_origem`, `_agente_versao`, `_pauta_id`, `origem_transicao`, `_cafezinho_gate_imagem` etc. no canônico E no espelho (a proteção de 19/08 `cafezinho-rest-meta-privada.php` havia regredido/era insuficiente). Fix: filtro `rest_prepare_post` prio 9999 no `cafezinho-origem-post.php` — sem `edit_posts`, metas internas removidas da resposta (canônico + espelho). Provas: público vê só metas de exibição (`_cafezinho_external_blocks_v1`, `_cafezinho_newsletter_enabled`); autenticado continua com as 25. **Agentes que liam metas sem auth passam a precisar de app password.**
3. **🔴 Painel CCTV é público na internet** (`http://43.156.151.165/v6/`, server_name _ porta 80 — 200 de fora). `/v6/autoria` protegido AGORA com Basic Auth nginx (`/etc/nginx/.htpasswd_autoria`, user `cafezinho`, senha nos cofres `AUTORIA_PAINEL_*`; 401 sem senha / 200 com; resto do painel intocado; backup `painel.conf.bak_pre_autoria_auth_20260822`). ⚠️ **DECISÃO PENDENTE DO MIGUEL:** o RESTO do painel (/v6/loops, /v6/custos, /v6/agentes…) segue público — proteger tudo é 1 location a mais, mas muda o acesso de todos (relatório Telegram 30min e hábitos).
4. Baleia Azul: boletim é interno (e-mails da casa + Telegram do Miguel) — seção de autoria segue.

## Adendo 4 (~11:50 BRT) — 🔓 /v6/autoria: troca Basic Auth por LINK SECRETO (ordem Miguel "quero aberto, sem login")

Miguel rejeitou o prompt de login. Solução que mantém o sigilo dele SEM fricção: nginx auth removido; o PAINEL agora exige `?k=<AUTORIA_TOKEN>` (var nova nos cofres) OU cookie `autoria_k` (setado na 1ª visita com o link, válido 1 ano, HttpOnly) — sem token e sem cookie a rota responde **404** (parece não existir). Provas: sem k 404 · com k 200+Set-Cookie · navegação seguinte com cookie 200 (filtros funcionam) · painel geral intacto 200. Nota: comentários no nginx mostram que o painel público é decisão do Miguel desde 01/08 ("REMOVIDO auth_basic ordem Miguel painel público").

## Adendo 5 (~12:10 BRT) — UX da página (feedback Miguel "cadê os meus + categoria")

(1) **Cards agora são FILTROS clicáveis** (`?fl=`) — 1 clique no card "✍️ Miguel (humano)" mostra só os artigos dele (com aviso de filtro + link "ver todas as autorias"); janelas de horas preservam o filtro. (2) **Coluna Categoria nova** na tabela (API passa `categorias`, até 3 por post). (3) Rótulo "Miguel (humano) — ver access log..." simplificado para "Miguel (humano)". (4) Bug da minha autoria corrigido no caminho: typo `bordo/borda` crashava a rota com token (404 do guard mascarava); provas finais: com token 200+cookie · filtro Miguel 200 (266817/266858/267017 com Ceará/Nordeste/Economia) · Categoria no header · sem nada 404.

## Adendo 6 (~14:20 BRT) — REDESIGN da página (feedback Miguel "muito confusa, amontoada; cadê meu post")

Página reescrita: (1) só 3 janelas (24h/2 dias/7 dias); (2) cards grandes extintos → **chips de filtro** com contagem (Todos/V4/Gabriel/Miguel/Motor V5/YouTube — rótulos curtos, agregando variantes); (3) UMA tabela de 5 colunas (Data dd/mm HH:MM · Autoria · Categoria · Título-link · Views); (4) **só posts publicados** (pending/draft saem da vista do Miguel — a fila segue na API p/ loops); (5) rótulos curtos via `_autoria_rotulo_curto()` (ex.: "Miguel (humano)"→"Miguel", pool 5742/5785→"Motor V5"). Prova 24h: 52 linhas, chips V4 37/Gabriel 12/Miguel 1/M5 1/YT 1; post 267017 (dívida externa) visível na janela padrão sem filtro (estava desde o início — a confusão visual é que escondia).

## Adendo 7 (~14:35 BRT) — v3: página de AUDITORIA organizada (feedback Miguel "feio/confuso; humanos com destaque")

Layout em 3 blocos fixos (abas de janela 24h/2d/7d mantidas): **1º ✍️ MIGUEL DO ROSÁRIO** (borda dourada) · **2º 🧑‍💼 GABRIEL BARBOSA** · **3º 🤖 AGENTES** (resumo por agente em 1 linha + tabela completa com coluna Agente). Helpers novos `_autoria_linha_tabela()`, `bloco_humano()`; Miguel (humano)+(Manus) somam no mesmo bloco. Provas: ordem dos blocos correta; "dívida externa" renderiza na 1ª seção (janela 24h padrão). Dica ao Miguel: Ctrl+F5 (cache do navegador pode servir versão velha — suspeita de por que "não apareciam").

## Adendo 8 (~15:45 BRT) — v4 FINAL: central + SUBPÁGINAS por autoria (feedback Miguel: "abas = subpáginas com nomes: miguel, gabriel, v4, v5, não identificados, além da central")

**Bug do "sinal quebrado" corrigido:** era fatiamento `[11:]` no meio da tag `<td style=...>` na tabela de agentes (HTML cru vazando na tela). Refatoração completa: (1) **central `/v6/autoria`** = grid de cards-link (✍️ Miguel do Rosário · 🧑‍💼 Gabriel Barbosa · 🤖 V4 · ⚙️ V5 Motor da esteira · 📺 YouTube · 🔁 Repetidor · ❓ Não identificados) com nº de artigos + views por card; (2) **subpáginas `/v6/autoria/<slug>`** (miguel/gabriel/v4/v5/youtube/repetidor/outros), cada uma com nome próprio, total de artigos+views e UMA tabela (Data · Categoria · Título · Views); (3) janelas 24h/2d/7d em ambas; (4) guard do token cobre TODAS as sub-rotas. Provas: central 200 linkando as 7; subpáginas miguel 1 post (dívida externa ✓), gabriel 11, v4 33, v5 1, youtube 1, outros 0; zero tags cortadas.

## Adendo 9 (~16:10 BRT) — ✏️ Correção manual de autoria pelo painel (ordem Miguel: "campo para identificar + permitir alterar")

(1) **WP:** metas `_cafezinho_autoria_manual` (+`_audit` com quem/quando) — prevalecem sobre o automático no classificador (rótulo sai como "X (corrigido manual)"). API de escrita: `POST/DELETE /wp-json/cafezinho/v1/autoria/<id>` {rotulo} — rótulos válidos: Miguel/Gabriel/V4/Motor V5/YouTube/Repetidor/Humano/Outro; DELETE limpa (volta ao automático). (2) **Painel:** coluna "✏️ corrigir" com select em TODAS as linhas das subpáginas (opção "auto" = limpar) → `POST /autoria/corrigir` (guard do cookie 403; invalida cache local na hora). (3) Bugs no caminho: opcache do php7.4-fpm servia mu-plugin velho (restart resolveu — LEMBRAR em deploys PHP seguintes) e URL da rota montada errada no painel. Provas: correção via painel ok:true → classificação "Gabriel (corrigido manual)" → DELETE volta ao automático → posts de teste removidos.

## Adendo 25/08/2026 ~22:20 (ZCode/Kimi K3) — ✅ F0.4 EXECUTADO: passo 3.5 agora é DIGEST compilado (ordem Miguel "não precisa trazer a lista de todos os posts")

O despejo cru da API (limite=60, 65 linhas por post no envio das 19:30 de hoje) foi substituído pelo formato aprovado 24/08 (adendo 1, F0.4):
- Script novo `~/bin/baleia_autoria_digest.py` (fail-soft, saída vazia = boletim segue sem seção): agrega os posts da API por grupo (V4.1 / V4 legado / Motor V5 / Gabriel / Miguel / Redação-equipe / YouTube / não identificado), calcula %, barras proporcionais e variação vs 24h anteriores (janela 48h − 24h).
- Wrapper `~/bin/enviar_baleia_azul_ponte.sh` passo 3.5 trocado para chamar o digest (backup `.bak_pre_digest_autoria_20260825`; `bash -n` OK).
- Prova (teste seco): 71 artigos → 8 linhas: V4.1 49 (69%) ▲26 · V4 legado 7 (10%) ▼24 · Gabriel 7 (10%) ▲3 · Miguel 2 · Redação 1 · YouTube 3 · 🔍 2 não identificado (5482 priscilamiranda + 5786 via REST Mozilla — conferir no painel /v6/autoria).
- Mensagem na ponte (ZM-20260825-020) avisa a editoria Laura: boletim sucinto, sem lista de posts, parágrafos de ~2 frases em linha única (quebra no meio da frase aparecia estranha no Telegram). ACK pendente.

## Adendo 27/08/2026 ~14:55 (ZCode/GLM-5.3) — 2ª ocorrência do falso "fora do ar" (mesma causa de 26/08): navegador sem cookie

Miguel reportou "página de autoria fora do ar". Diagnóstico no servidor Tencent: **página 100% viva** — sem token 404 (disfarce OK), com `?k=` 200, com cookie `autoria_k` 200. Causa idêntica ao caso 26/08 ~20h: navegador sem o cookie do link secreto. Ação: link completo com `?k=` reenviado por Telegram (ponte `--send`, exit 0, sem `tg_send_erro` no log) + recomendação de favoritar. Nenhuma mudança de código.

**Recorrência reforça a prioridade do F0.1** (plano 24/08, nunca executado): cookie 30 dias + botão "link copiável" dentro do painel — mata este sintoma na raiz. Pendências de configuração seguem as do plano F0→F3 (F2 IP/geo bloqueado em decisão CF×real_ip do Miguel; F3.3 aguarda aprovação).

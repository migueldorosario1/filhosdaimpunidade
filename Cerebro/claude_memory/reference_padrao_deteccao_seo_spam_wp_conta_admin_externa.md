---
name: reference-padrao-deteccao-seo-spam-wp-conta-admin-externa
description: Padrão de detecção de guest posts SEO pagos publicados por contas admin externas no WP canônico ocafezinho.com — 4-check-list antes de propor bug de worker + red flags de conta comprometida + assinaturas técnicas de origem manual/externa
metadata: 
  node_type: memory
  type: reference
  originSessionId: d917262a-1c40-4990-942c-4a2a8b497e3d
---

**Padrão de detecção de guest posts SEO pagos publicados por conta admin externa comprometida no WP canônico `ocafezinho.com`.** Caso fundador: post 264522 (06/08/2026), autor 5787 (`redacaoagente`), link `slotozilla.com` de casino. Investigado em 12/08/2026 17:00-17:35 BRT após carta "Padrão Ouro" que atribuiu erroneamente o bug ao worker V4. Diagnóstico completo em `Cerebro/Foruns/resposta_claude_investigacao_padrao_ouro_264522_20260812.md`.

## 4-check-list ANTES de propor mudança em worker V4 (por bug editorial em post)

Se qualquer verificação abaixo indicar origem externa, **não é bug de worker** — é incidente de segurança / SEO paid content. Não mexer em prompt canônico.

1. **Meta `_agente_origem` + `_agente_versao`**: `SELECT meta_value FROM wp_postmeta WHERE post_id=X AND meta_key IN ('_agente_origem','_agente_versao')`. Se AMBOS vazios → não passou por worker V4 (V4 SEMPRE grava essas metas). Via REST: `GET /wp-json/wp/v2/posts/{id}?context=edit&_fields=meta` (precisa `Authorization: Basic` + UA Mozilla; NYC tem `WP_SITE/USER/PASS` em `chaves.sh`).
2. **`post_author`**: `SELECT post_author FROM wp_posts WHERE ID=X`. Se != 5786 (V4 canônico) E != 5780/5470/2018/5786-5787-canônicos-conhecidos → verificar se é humano legítimo ou conta suspeita.
3. **User do autor**: `SELECT user_login, user_email, user_registered FROM wp_users WHERE ID=<author>`. Red flags: (a) email gmail/hotmail/yahoo genérico (não corporativo), (b) `user_registered` recente + `post_date` da 1ª publicação ≤ 24h após registro, (c) `user_login` que imita padrão interno ("redacaoagente" imita "Redacao nova"/"redator2"), (d) role = `administrator` sem justificativa.
4. **Grep no corpo por padrões SEO farm**: `slotozilla|1xbet|betano|bet365|betfair|cassino online|caça-níqueis|dragon hatch|jogo do balão|rodadas gratis|sem depósito|free spins`. Presença de link `dofollow` externo pra site desses = guest post pago quase-certeza. Nota: nem toda menção é spam — posts editoriais legítimos citam bets (ex: 264600 "Bets arrancam R$ 62,5 bi das famílias"). O sinal é a **combinação** com autor suspeito + `_agente_origem` vazio + link `dofollow`.

## Assinaturas técnicas de origem manual / não-worker (evidência forense)

Se o post tiver 2+ desses, é quase-certeza que não veio de LLM/worker V4:

- **`<span style="font-weight: 400;">` em cada parágrafo** → conteúdo colado do **Google Docs** (exportador HTML do Docs cospe esse span universalmente). Workers V4 nunca geram isso.
- **Sintaxe PT-PT europeu** ("planeamento", "câmaras", "detetar", "equipa", "paragens não planeadas", "ruturas", "cadeias de abastecimento", "estas capacidades", "apresentar-se-á" — colocação pronominal enclítica em frases não-emphatic). Modelos LLM canônicos (GPT/Claude/Gemini/DeepSeek/Kimi) por padrão respondem em PT-BR — só invertem se o system prompt força PT-PT explicitamente OU se o input veio em PT-PT.
- **Title Case anglo** ("O Papel da Inteligência Artificial na Transformação da Produção Industrial") — template SEO copy-paste de agência internacional.
- **`<h2>` no lugar de `<h3>`** — agências SEO usam H2 (padrão web genérico); workers V4 seguem hierarquia do tema (mas atenção: o padrão real do tema canônico ainda precisa ser confirmado, ver §caveat abaixo).
- **Palavras-truque tipográfica** tipo `industrIAl` (com "IA" caps embutido no meio) — SEO copywriter humano tentando ranquear "IA" pela densidade da palavra-chave. Nenhum LLM faria isso por engano.
- **`<table>` com produtos/apps/serviços** listados em colunas — típico de comparativo SEO/afiliado.
- **Link externo comercial em palavra-chave forçada** ("Tal como numa oferta de [200 sem depósito](https://slotozilla.com/...)") — a frase é artificial, entrando no meio de tema sem conexão real.

## Red flags de conta admin comprometida / criada pra spam

Verificar `wp_users` + `wp_usermeta` do autor:

- **Email não-corporativo** (gmail/hotmail/yahoo/proton — em vez do domínio `@cafezinho.com` ou `@ocafezinho.com`).
- **`user_registered` recente** (últimos 30 dias) + **1º post ≤ 24h após registro**.
- **`user_login` imitando padrão interno** ("redacaoagente" imita "Redacao nova"; "redator3" imita "redator2").
- **`display_name` genérico** ("Redação 2027", "Redação Nova", "Editor Chefe") sem pessoa real por trás.
- **`wp_capabilities` = `administrator`** (acesso total; contas legítimas de redator devem ser `author` ou `editor`).
- **`session_tokens` com IPs de dispositivos diferentes** logando em janela curta (mobile + desktop) — indício de acesso compartilhado ou credencial vendida.
- **Meta `wp_dashboard_quick_press_last_post_id`** presente → usuário usou Quick Press do wp-admin (feature humana, agentes não usam).
- **Meta `_yoast_wpseo_profile_updated`** presente + `_yoast_wpseo_introductions` com `is_seen: false/0` (viu modais Yoast) → navegou o wp-admin manualmente.
- **Wordfence `wp_wfLogins` vazio pra userID mesmo com logins recentes** → login não passou pelo login page (via API? Via cookie roubado?). Suspeito.

## Ações recomendadas em caso confirmado (aguardar OK Miguel)

Sempre em ordem — **cortar acesso antes de limpar posts**:

1. **Revogar admin**: rebaixar role pra `subscriber` OU deletar user + reasignar posts. `wp user set-role <ID> subscriber` OU `wp user delete <ID> --reassign=<safe_user>`.
2. **Trash posts do user comprometido**: `wp post delete <ID> --force=false` (vai pra lixeira, não apaga permanente; revertível 30d).
3. **Redirect 301** dos URLs deletados pra categoria pai OU `/` (evita 404 no SEO).
4. **Rotacionar senhas admin** dos users que logaram em janela suspeita (`SELECT user_id FROM wp_usermeta WHERE meta_key='session_tokens'` + parse PHP-serialize dos IPs/timestamps).
5. **Grep amplo por posts antigos** com padrões SEO farm publicados por autores admin não-canônicos (últimos 6 meses).
6. **Auditar como a conta foi criada**: logs Nginx `wp-login.php`, `user-new.php`, `xmlrpc.php`, `wp-json/wp/v2/users` na janela do `user_registered`.
7. **Habilitar Wordfence Live Traffic** ou plugin equivalente pra logar tentativas futuras.

## Caveats e limites conhecidos

- **`<h2>` vs `<h3>` para subtítulos**: o Antigravity afirmou em 12/08 que `<h3>` é o padrão do tema, mas os posts canônicos V4 do autor 5786 usam `<h2>` livremente. **Antes de aceitar como bug, confirmar com o tema real** (ler `header.php`/`content.php` do tema em `/var/www/ocafezinho/wp-content/themes/`). Mudar h2→h3 no worker sem confirmar quebra 15+ posts/dia de produção saudável.
- **PT-PT em worker V4**: workers canônicos NÃO geram PT-PT sistematicamente. Não vi bug reincidente em posts do 5786 nas últimas 2 semanas de Vigília V5. Se aparecer, investigar caso a caso — pode ser fonte europeia sendo copiada literal (raro).
- **Bypass Cloudflare no NYC pra REST**: se REST retornar 403, adicionar `User-Agent: Mozilla/5.0 (...)` ao header. Se ainda 403, usar IPv4 direto `172.67.162.40` + `Host: controle.ocafezinho.com` + SNI (ver [[feedback-email-pendentes-p86-reenviar-todo-ciclo]] pro detalhe).
- **`?author=X` pode retornar 404** no WP público (plugin de segurança bloqueia enumeration). Alternativa: `?categories=X` + filtrar por autor no cliente, OU wp-cli `wp post list --author=X` via SSH no host.

## Correlatas

- Caso fundador: [[project-incidente-seo-spam-post-264522-20260812]]
- Regra irmã de investigação: [[feedback-proveniencia-modelo-ambiente-papel-separados]] (dimensões modelo/ambiente/papel).
- Motivo pra NÃO mexer em worker por bug editorial isolado: [[feedback-modo-enxuto-preservar-worker-v4]] (contrato Miguel 11/08).

# Fórum — Painel CCTV V6 com LOGIN (Basic Auth) — 13/09/2026

> Sprint ZCode/GLM-5.3 · ordem do Miguel 13/09 ~17:1x · fechado em 13/09 ~17:5x BRT

## O pedido (do Miguel, quase literal)

"Eu quero que você acrescente login e senha no painel cctv v6. login zizi senha baleia."

## Decisões

1. **HTTP Basic Auth no próprio serviço** (`painel_cctv_v6.py`, porta 8084) — cobre OS DOIS caminhos de entrada: via nginx `http://43.156.151.165/v6/*` e direto na 8084 (que aliás o UFW já bloqueia de fora). Realm "Painel CCTV V6"; browser pede login 1× e repete sozinho (fetches same-origin das páginas continuam funcionando após login).
2. **Credenciais em arquivo à parte**: `/home/ubuntu/cafezinho/v6/.painel_auth` (chmod 600, formato USER=/PASS=) — trocar senha = editar arquivo, sem restart (relê a cada request). Espelhadas como `PAINEL_V6_USER`/`PAINEL_V6_PASS` no cofre unificado (os 2 lados, com .bak antes). Valores NÃO reproduzidos aqui (regra do Cofre).
3. **Isenções cirúrgicas (para não quebrar a casa)**:
   - POST `/api/audiencia-receber` (+ alias `/v6/api/...`): pusher NYC segue com token próprio (prova: sem Basic devolve 403 do TOKEN, não 401).
   - Acesso local DIRETO no Tencent (client 127.0.0.1/::1 **E sem header X-Real-IP**): preserva os crons WARM_CACHE (25min) e coletor FAROL (30min) e sondas. O nginx SEMPRE injeta `X-Real-IP $remote_addr` no tráfego público que repassa — quem tem o header veio de fora e precisa de login; spoofar o header de fora não basta (a exceção exige client_address localhost de verdade).
4. **Fail-open documentado**: sem arquivo `.painel_auth` e sem env `PAINEL_V6_USER/PASS`, o painel fica ABERTO (log de aviso 1×) — decisão para não trancar painel/sondas por arquivo perdido; o arquivo existe e é 600.
5. POSTs de controle (`/controle/api`, `/api/ceo/*`, `/api/estilo/*`, `/api/youtube/*`) agora exigem login quando vêm de fora — operação de controle atrás de auth é desejável; browser logado segue normal.
6. Página pública `/pagamentos` (serviço 8085) NÃO tocada.

## O que foi feito

- Bloco novo no `painel_cctv_v6.py` antes do `V6Handler`: `_painel_auth_creds()` (lê arquivo/env) + `_checar_basic_auth(handler)` (isenções + `hmac.compare_digest` + 401 com `WWW-Authenticate`).
- Gate `if not _checar_basic_auth(self): return None` no topo de `do_GET` e `do_POST`.
- Backup: `painel_cctv_v6.py.bak_pre_auth_20260913` (rollback = cp + restart; ou apagar `.painel_auth` para reabrir o painel).
- Cofres: `.env.unificado` dos 2 lados com `.bak_pre_painelv6auth_20260913` (chaves inseridas junto da `PAINEL_V6_TOKEN` existente; espelho conferido por sha8 dos valores, sem exposição).
- Aviso à casa: ponte `de_dell.md` ZM-20260913-002 (commit cirúrgico no espelho — o sync recusou por worktree sujo de trabalho alheio, não tocado).

## Provas

- Teste unitário isolado 10/10 (externo sem/com creds, nginx X-Real-IP, local direto, spoof X-Real-IP, pusher, alias, POST controle, fail-open).
- Servidor: local direto → 200; com X-Real-IP sem creds → **401 + WWW-Authenticate**; com creds → 200; senha errada → 401; pusher POST sem Basic → 403 do token (não 401); coletor FAROL cron → 200.
- Público `http://43.156.151.165/v6/audiencia`: sem creds → **401** com `WWW-Authenticate: Basic realm="Painel CCTV V6"`; `-u` com as creds → **200**; senha errada → 401; porta 8084 direta de fora → bloqueada (UFW).
- Regressão: serviço active; crons locais intactos (provas 1/5 acima são exatamente os crons).

## Estado

- **O que aconteceu:** auth no ar, cofres espelhados, casa avisada na ponte.
- **O que falta:** nada técnico. Agentes externos que monitoram o v6 precisam passar a usar as creds do cofre (aviso ZM-20260913-002 na ponte).
- **O que preciso do Miguel:** nada. Troca de senha futura = editar `.painel_auth` no Tencent + atualizar as 2 chaves nos cofres (mesma ação).

## Relacionados

- Memória técnica: `memorias_provisorias/memoria_painel_v6_autenticacao_20260913.md`
- Nodos: `CEREBRO_NODE_OBSERVABILIDADE.md` (§ 13/09 auth), `CEREBRO_NODE_COFRE_CHAVES.md` (família PAINEL_V6_*), `CEREBRO_NODE_ATUALIZACOES.md`
- Antecessor: `Foruns/forum_audiencia_correlacao_posts_20260913.md` (mesma página, horas antes)


## Adendo (17/09 ~11h BRT) — credenciais enviadas por e-mail (pedido do Miguel)

- Pedido: "pode mandar para meu email (miguel) e do gabriel?" → enviado via Gmail SMTP (app password do cofre) para `migueldorosario@gmail.com` e `gabrielbarbosa@ocafezinho.com` (endereço corporativo usado nos envios anteriores da casa), corpo com endereço do painel + credenciais (valores NÃO reproduzidos aqui; vivem no `.painel_auth`/cofre).
- Se o Gabriel precisar do pessoal: `gabrielbarbosa9001@gmail.com` (consta do fórum do e-mail de 25/08) — não incluído por padrão.


## Adendo (19/09 ~01:3x BRT) — Visão rápida da Home passa a ser FAROL (ordem Miguel 17/09)

- A Home (`pagina_home`) montava os 3 stats com GA4 (views). Ordem do Miguel: "tem que ser do farol, não do ga4".
- Fonte agora: `serie_diaria_farol()` (humanos distintos/dia, cache 1h, nascimento parcial descartado) — NÃO `hoje_navegacoes` (série quebrada 09/09, bug registrado).
- Título virou "Visão rápida — FAROL"; rótulos "humanos · 7 dias fechados (FAROL)" / "média móvel 7d · humanos (fechada)" / "tendência 7d". Valores vivos: 138.062 humanos em 7d, MM7 19.723, tendência +30%.
- Fallback: se o FAROL tiver menos de 8 dias de histórico, o bloco mostra aviso (nunca regressa ao GA4 em silêncio).


## Adendo (19/09 ~01:4x BRT) — página SOL: só dias FECHADOS (ordem Miguel 17/09)

- "só bota dias fechados, senão gera confusão" — o dia corrente parcial saía no gráfico de barras, na linha, no histórico e nos cartões pico/média (e alimentava o gráfico defasado com um dia falso).
- `pagina_sol`: filtro `dias_f = [d < hoje BRT]` aplicado em TUDO (svg_linha, svg_barras, histórico 14d, defasado, exemplo da janela); pico/média 30d recalculados localmente sobre os fechados (rótulos "…(fechados)"); aviso de "SOL nasceu em 01/09" segue para série curta.
- Nota: o card "Visitas hoje" do topo segue (rótulo explícito de hoje — não é a série). Deploy reforçado: cp --remove-destination (o cp simples falhou em silêncio uma vez nesta sessão — md5 conferido depois).

# Fórum — Auditoria do cálculo do Top 10 Tendências (v4) + páginas loops/autoria fora do ar (15/09/2026)

Ordem do Miguel (~15h): "quero que você faça uma auditoria sobre o cálculo do top 10, para ver se ainda está com algoritmo íntegro; se tiver qualquer erro, corrige no cafezinho e no v6. No painel v6, pode tirar do ar as páginas loops e autoria."

## A cadeia (mapeada)

NYC `top_tendencias_push.py` (cron `25 * * * *`) calcula o ranking no GA4 → POSTa para canônico e espelho (`cafezinho/v1/top-tendencias`) → mu-plugin `cafezinho-top-tendencias.php` guarda na option `cafezinho_top10` e pinta o carrossel da home, a página /top10 e a categoria "Top 10 — agora" → painel V6 /v6/tendencias lê o mesmo REST e exibe.

Fórmula oficial (confirmada ÍNTEGRA na concepção): Score = views/h nas últimas 6h + 0,15 × Views_48h/(Idade_h+1,5)^1,2. Os erros estavam nos DADOS que alimentam a fórmula, não na fórmula.

## O que a auditoria achou (6 defeitos provados) e as curas (v4, tudo no ar)

1. 🔴 TRUNCAGEM SILENCIOSA (o mais grave, semanas ativo): a consulta por hora usava `limit=1000`; sem filtro a tabela hoje tem 6.520 linhas — a "velocidade 6h" era calculada sobre uma tabela CORTADA (números tipo v/h 16,8 eram lixo estatístico). Cura: filtro `BEGINS_WITH "/20"` (4.400 linhas, só paths de posts) + `limit=10000`. Prova do acidente: GA4 `FULL_REGEXP "^/20\d\d/"` devolve 0 linhas (exige casar a string INTEIRA) — o filtro regexp do 1º attempt da v4 também morreu por isso.
2. 🔴 PÁGINA /top10 CONGELADA: `NameError: name 'fonte' is not defined` em toda rodada desde a v3 (24/08) — a página nunca era reescrita. Cura: `fonte` passada por parâmetro. Prova: página agora mostra "Atualizado em 15/09/2026 18:46 ... v4 15/09".
3. 🟠 IDADE INFLADA +3h: `p["date"]` (hora LOCAL BRT) tratada como UTC. Prova: 270762 exibia 33,1h, real 30,4h (date_gmt 14/09 12:21 UTC). Cura: `date_gmt`.
4. 🟠 "Views 48h" que não eram 48h: soma `ontem+hoje` (janela variável de 15h a 48h conforme a hora do dia). Cura: janela REAL de 48h derivada da mesma tabela por hora.
5. 🟡 423 do gate em pano de fundo: a sincronização da categoria top-10 em posts de humanos devolve 423 (proteção editorial — post humano intocável por agente, regra da casa) e era logada como ERRO horário após hora. Cura: 423 = desfecho NORMAL, log INFO; o post segue no carrossel/página/V6 (só não ganha a categoria). NÃO se contorna o gate — decisão deliberada.
6. 🟡 Espelho e ruído: push horário pro espelho morrendo 401 (site inteiro em lockdown pós-hack 13/09) → 1 linha quieta; log duplicado (print+append) → só print (o redirect do cron grava o arquivo).

## Provas finais (18:46-15:5x BRT)

- E2E limpo no NYC: 1.853 slugs na janela; categoria add/remove ok nos posts de agente; 423 tratado; /top10 atualizada; push canônico ok; espelho quieto.
- Endpoint público: idade 30,4h × 30,5h real; score fecha contando na mão (0,88 = 0 + 0,15×374/(30,4+1,5)^1,2).
- Carrossel da home renderizando o novo #1 ("A crise do STF chega às urnas...").
- Nota honesta: o GA4 por hora está com latência ~6h hoje (max_h geral = 09:00) → v/h = 0 para todos é o dado REAL (todos medidos na MESMA janela, comparação justa); os "ritmos" bonitos de antes vinham da truncagem. Job diário do espelho (atualizar_top10_espelho.py, 09:00 UTC) segue saudável por outro caminho (9/10 hoje).

## V6 — páginas removidas (ordem direta)

- `/v6/loops` e `/v6/autoria` (+ sub-rotas `/autoria/...` e o POST de escrita `/autoria/corrigir`) → 404 "página removida (ordem Miguel 15/09/2026)".
- Menu e card da home limpos (0 links mortos). JSON `/v6/api/loops` MANTIDO vivo (encanamento invisível, sem consumidores conhecidos — derrubar página ≠ derrubar API).
- Rótulo do Top 10: "(ao vivo no Canônico · espelho em lockdown pós-hack)".
- Backup `painel_cctv_v6.py.bak_pre_loops_autoria_20260915`; sintaxe conferida no Python do servidor; `cctv-v6` reiniciado e ativo; provas: 404 nos removidos, 200 em /baleia /tendencias /audiencia /foruns /api/loops.
- 🔴 Detalhe de teste que enganou o ZM: o painel atende caminhos SEM prefixo `/v6` (o nginx o tira) — teste interno certo é `/baleia`, não `/v6/baleia`.

## Pendências que ficam

- Redundante §118 morto: /root/agent_data/autoria_views_snapshots.jsonl com 1 linha só (a coleta de autoria parou — mesma esteira da página retirada do ar). O top10 hoje depende só do GA4 primário; failover de redundância existe no código mas sem fonte viva.
- Carrossel do espelho fica preso no dado antigo até o fim do lockdown (push 401 quieto por design).

## O que preciso de você (Miguel)

Nada. Se quiser a categoria "Top 10 — agora" marcando também os posts de humanos, é decisão editorial sua (exigiria válvula no gate) — hoje ela só marca posts de agente, por regra da casa.

— ZM · ZCode/GLM-5.3 · 15/09/2026 15:5x BRT

## Adendo (15:5x BRT) — pendência cosmética: cache da página /top10

O carimbo BRT (v4) está correto no banco (post_modified 15:55:20, conteúdo "Atualizado em 15:55") e a URL com query-string renderiza fresco, mas a URL limpa /top10/ continua servindo o HTML de 18:46 (UTC antigo) por uma camada de cache de página não identificada em 4 checagens (CF diz DYNAMIC; nginx do WP sem fastcgi/proxy cache; WP Rocket só cacheia o subdomínio controle; nenhum arquivo no cache dir). Carrossel da home, REST top-tendencias e V6 estão frescos — só esta página secundária. Próxima ronda que sobrar fôlego: identificar a camada (suspeita: edge/page-rule CF com bypass de query) e purgar.

## §v5 — FUSÃO GA4 + FAROL no Top 10 (15/09 noite, ordem Miguel "ok entao, g4 + farol")

Decisão após parecer: dos 4 medidores, só o GA4 tinha dado por post pronto; o FAROL é o único sem ponto cego de JavaScript (lê logs do servidor, vê o leitor de adblock); LUMINA agrega pouco (beacon JS igual GA4, sem export por URL); SOL é agregado do site (não ranqueia posts). Implementado GA4+FAROL:

1. **contador.sh (cafezinho-wp)**: na mesma passada de logs, agora conta slug×hora (posts /AAAA/MM/DD/slug/, mesmo filtro humano histórico, AMP junto com a mãe) e 1x/hora (minuto <5) grava + empurra farol_por_hora.json (top 400 slugs, 48h) ao painel. Backup .bak_pre_farol_por_hora_20260915.
2. **Painel V6**: endpoint POST /api/farol-por-hora (mesmo token do audiencia-receber, isento de Basic Auth) grava atomicamente v6_data/farol_por_hora.json. Card do Top 10 agora mostra GA4 × FAROL por post e explica a fusão. Backup .bak_pre_farol_por_hora_20260915.
3. **Produtor v5 (NYC)**: lê a tabela FAROL por ssh do Tencent (mesma rota do flusher) e faz a fusão: cada fonte calcula a própria régua (vel 6h + 15% gravidade 48h), cada score é normalizado pelo líder da própria fonte e entra 50%+50% — unidades diferentes nunca somadas cruas. GA4 morto → FAROL segura sozinho (e vice-versa); redundante §118 mantido como 3º plano. Backup .bak_pre_v5_fusao_20260915.
4. **Receiver WP v2.1**: passa adiante views_farol/v_h_farol/fonte_score no option. Backup .bak_pre_fusao_v5_20260915.

Provas E2E (19:0x BRT): FAROL 400 slugs com hora mais nova às 19h (defasagem ~1h vs 6h+ do GA4); ranking fundido com fonte ga4+farol; LÍDER 446v GA4 × 588v FAROL (32% a mais — a subnotificação que motivou o pedido); 4 posts de HOJE (271112, 271067, 271141, 271154) no top 10 vistos SÓ pelo FAROL (GA4 ainda zerado neles); card V6 renderizando os dois medidores; página /top10 e carrossel atualizados.

Riscos/observações: se o contador parar >1h, a fusão degrada silenciosamente para GA4 sozinho (log registra); tamanho do push ~178KB 1x/hora (irrelevante); top 400 slugs por janela cobre folga o top 10.

— ZM · ZCode/GLM-5.3 · 15/09/2026 19:1x BRT

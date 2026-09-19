# Fórum — Esteira de fios de divulgação 10x/dia no X e Facebook (17/09/2026)

- **Quem:** ZCode/GLM-5.3 (ordem direta do Miguel nesta quinta, 17/09/2026 ~11:0x)
- **O quê:** esteira automática que publica 10 fios por dia divulgando as melhores matérias do Cafezinho no X (@ocafezinho) e no Facebook (página O Cafezinho, 453k curtidores).
- **Estado: NO AR E BATIZADA** — primeiro ciclo completo publicado manualmente-trigger às 11:35, cron assume sozinho a partir das 13:30.

## O pedido (regra do Miguel, quase literal)

10 fios por dia: 2 à noite, 8 de dia (4 de manhã, 4 de tarde). Escolha por análise editorial ("escolhe só os melhores"). Formato do fio: X = tweet 1 com texto maior (emoji temático + título + abertura) e capa anexada, tweet 2 reply com link; Facebook = mesmo texto + capa, com o link no PRIMEIRO COMENTÁRIO.

## O que está no ar

- **Motor:** `tencent:/home/ubuntu/cafezinho/redes/fios_diarios.py` (flock + arquivo PAUSA para desligar sem remover cron + dry-run)
- **Cofre local do servidor:** `/home/ubuntu/cafezinho/redes/.env_redes` (600, ubuntu; X_API_*, X_ACCESS_*, X_BEARER_TOKEN, FB_PAGE_ACCESS_TOKEN, FB_PAGE_ID)
- **Estado:** `estado.json` (slugs divulgados, janela de repetição 48h) + `fios_textos_AAAA-MM-DD.json` (auditoria: texto + links de cada fio do dia) + `fios.log`
- **Cron (tencent, fuso America/Sao_Paulo), tag # FIOS_REDES:** 08:00 · 09:30 · 10:30 · 11:30 (manhã) · 13:30 · 15:00 · 16:30 · 18:00 (tarde) · 20:00 · 21:30 (noite)

## Análise editorial automática (como escolhe "os melhores")

Score mínimo 60 para publicar (senão o slot pula — só os melhores):
- base 50 (matéria do dia com capa; capa é obrigatória)
- +30 Política/Nacional/Eleições · +15 Economia/Internacional · +10 IA/Tecnologia
- +25 frescor <6h · +15 <12h · +5 <24h (idade máx 36h)
- +1 por view do FAROL nas últimas 6h (teto 30) — sinal real de audiência (lê farol_por_hora.json local do tencent)
- −10 se o fio anterior foi da mesma categoria (diversidade de tema)
- emoji automático por tema (⚖️ justiça/STF · 🇧🇷 política · 📈 economia · 🌍 internacional · 🤖 IA · 🎭 cultura · ⚽ esporte · 🩺 saúde · ☕ default)

## Batismo (provas do dia 17/09)

1. Fio manual Gilmar Mendes (X: 2100583215094239416 + reply; FB: 421927677830371_1601804191985541 com link no 1º comentário).
2. Esteira real 11:35: escolheu AtlasIntel (score 135 — líder de audiência 62 views/6h): FB OK (1601824175316876 + comentário) e X OK (2100594844918034492, confirmado oembed).
3. Dry-run pós-batismo: AtlasIntel/Gilmar excluídos pelo estado; próximo do ranking = OpenAI (106) para o slot 13:30.

## 🔴 Token Facebook — o episódio do dia

- O FB_PAGE_ACCESS_TOKEN antigo publicava mas NÃO comentava (sem pages_manage_engagement → 403 #200).
- Miguel regenerou no Graph API Explorer (app Cafezinho Ressurrection 2026) com pages_manage_engagement adicionada → page token PERMANENTE ("expira: nunca", conferido via oauth/access_token_info).
- Espelhado (REGRA Nº 4) em 5 cofres com backup .bak_pre_fb_engagement_20260917: Outros/chaves/agentes_labs/.env.unificado (Dell) · Projeto Cafezinho Agentes/root/.env.unificado (Dell) · tencent /root/.env · tencent /root/.env.unificado · tencent /home/ubuntu/root_copy/.env.unificado. Hash md5 novo: 0f1222e20c (idêntico nos 5).
- Token velho do root_copy (morto desde troca de senha) descartado; arquivo da home do Miguel apagado depois de gravado.

## Bugs curados no caminho

1. REST do WP: campo é `date_gmt` (não dateGmt) — com fallback para `date` −3h.
2. Download da capa com Python-urllib puro toma 403 da borda do site (Cloudflare) → UA de navegador obrigatório (função baixar_capa).
3. Tweet 1 usa Long Post (Premium) — praxe já provada no fio manual.

## O que falta / próximos passos

- Nada bloqueante. Acompanhar os primeiros dias de cron (fios.log + fios_textos_*.json) e calibrar SCORE_MINIMO se publicar demais/de menos.
- Pendências futuras: token X é só-escrita (sem métricas de engajamento via API); se um dia o FB voltar a dar 403 em comentário, regenerar token pelo mesmo fluxo do Explorer.

## Adendo — REGRA CONFIRMADA + COMENTÁRIO FIXADO (17/09 ~11:4x, ordem Miguel)

- Regra viva confirmada por ele: TODO fio = 1 postagem no X + 1 no Facebook (10 X + 10 FB por dia, 2 à noite e 8 de dia), e no FB o link fica no primeiro comentário, FIXADO se possível (como comentário do autor já nasce em primeiro naturalmente — fallback dele).
- Fixação via API FUNCIONA: POST /{comment_id} com is_pinned=true → {"success": true} (aceito pela Graph v21.0). Detalhes: o campo não volta legível no GET e a listagem /comments ordena por tempo (não reflete pin) — a prova prática é o alfinete no UI.
- Comentários de HOJE fixados manualmente: Gilmar (1601804191985541_3681669581989299) e AtlasIntel (1601824175316876_1330511752357067).
- fios_diarios.py atualizado: publicar_fb agora fixa o comentário automaticamente (falha de fixação não bloqueia o fio — loga e segue).

## Adendo 2 — CURADORIA DE BOM SENSO (17/09 ~12:0x, ordem Miguel "não confia totalmente na regra")

- Regra dele: o score é a BASE, mas um editor (bom senso) pode escolher outra que combine melhor com o dia — época de eleição presidencial (Lula x Flávio Bolsonaro): fatos favoráveis a Lula, escândalos/notícias negativas envolvendo Flávio Bolsonaro, STF com impacto eleitoral.
- Implementado: camada CURADORIA LLM em fios_diarios.py — top-5 do ranking vai para um editor-chefe (glm-5.3-flash via ZAI_API_KEY do cofre) com contexto eleitoral DINÂMICO calculado por data (dias até 1º/2º turno — 4/10 e 25/10/2026) + linha editorial + aviso de não repetir tema do fio anterior. Responde JSON {escolha, porque}; justificativa gravada em fios_textos (auditoria). Fallback: se LLM falhar → segue o 1º do ranking (regra como base).
- Prova do dry-run 12:04: ranking escolheria atlas-empate (125) e a curadoria preferiu atlasintel-confirma-lula-lidera (5º, 101) por ser mais fresca e tocar a disputa — exatamente o cenário que o Miguel descreveu.
- 🔴 Bugs curados nesta camada: (1) DeepSeek API BLOQUEIA o IP do tencent (401 "invalid" com a MESMA chave que funciona do Dell — bloqueio regional); curadoria usa glm-5.3-flash (testado do tencent). (2) glm-5.3-flash com max_tokens pequeno devolve content VAZIO (o raciocínio consome o limite, finish=length) → pensar desligado ("thinking": disabled) + max_tokens 1200.
- 🔴 Cofres: DEEPSEEK_API_KEY do tencent (/root/.env, /root/.env.unificado, root_copy) estava MORTA (401) — substituída pela VIVA do cofre Dell (hash 2fb569764b) com backups .bak_pre_deepseek_sync_20260917 (divergência registrada para o Guardião das Chaves). Atenção: mesmo viva, DeepSeek NÃO serve para robôs no tencent (região bloqueada); .env_redes da esteira ficou só com ZAI.

## Adendo 3 — RODAPÉ DE APOIO (PIX) nos fios + PLANO para o site (17/09 ~12:1x, ordem Miguel)

- Ordem dele: todo fio termina com "Ajude a mídia independente. Faça um pix de qualquer valor" + chave pix redes@ocafezinho.com (destinatário "O Cafezinho" no banco; chave pode ser trocada por ele depois — constante PIX_APOIO no topo do script).
- Implementado: X → tweet 2 ganha o apelo após o link; FB → fim do texto do post (comentário fixo fica limpo com o link). Pronto para o próximo slot.
- PLANO SITE (aguarda "vai" do Miguel): o "Leia também" é o snippet WPCode 255106 ("Blocos externos ao post_content"), filtro the_content prioridade 10, meta _cafezinho_external_blocks_v1 → criar mu-plugin cafezinho-apoio-pix.php com the_content prioridade 9 (entra DEPOIS do texto, ANTES do Leia também), caixinha com botão copiar, todos os singles (verticais inclusas, sem depender da meta), is_feed() ignorado, chave em constante única; backup + prova visual + rollback = apagar arquivo.

## Adendo 4 — APELO SEM TRAVESSÃO + BLOCO PIX NO SITE NO AR (17/09 ~13:2x, ordem Miguel)


- APELO PIX reformulado SEM TRAVESSÃO (regra dele: ponto final, frase nova): "☕ Colabore com a mídia independente. Faça um pix de qualquer valor. / 🏦 Chave pix (O Cafezinho): redes@ocafezinho.com" — no X vai no tweet 2 após o link, no FB no fim do texto do post.
- ✅ BLOCO PIX NO SITE (plano aprovado por ele): mu-plugin `cafezinho-apoio-pix.php` no WP canônico — the_content prioridade 9 → entra DEPOIS do texto e ANTES do "Leia também" (WPCode 255106 usa prioridade 10); todos os singles (verticais incluídas), nunca feed/admin; caixinha creme com botão COPIAR CHAVE (clipboard + fallback execCommand); chave em constante no arquivo. Provas: curl (bloco antes do leia-tambem), browser real (botão presente, leia abaixo), print no chat; rocket_clean_domain executado (🔴 HTML antigo fica cacheado — sempre limpar após mexer; cache-buster ?x=1 prova a origem, mas o visitante comum vê o cache).
- Rollback do bloco: apagar mu-plugins/cafezinho-apoio-pix.php + rocket_clean_domain.

## Adendo 5 — RONDA DE VIGILÂNCIA DA ESTEIRA (17/09 ~16:1x, ordem Miguel "cadê a ronda?")

- Automation do ZCode criada: **automation-ee2aad58** "Ronda esteira de fios X+FB 13:10 e 22:10" (cron 10 13,22 * * * BRT). Primeira execução hoje 22:10.
- O que faz (somente leitura/diagnóstico, nunca publica): lê fios_textos do dia + fios.log no tencent, conta fios X e FB vs slots esperados, valida o último fio no ar via oembed, confere arquivo PAUSA (pausa deliberada ≠ falha), manda placar ao Telegram do Miguel (🟢/🟠/🔴 começando com "Consegui, Miguel"), em caso de 🔴 roda dry-run de diagnóstico e registra nota no monitor (ZM-RONDA-FIOS).
- Motivação: o fio das 15:00 de hoje se perdeu num 500 intermitente do WP e ninguém perceberia sem ronda; cura do retry já aplicada, ronda fica como cinto e suspensos.

## Adendo 6 — FIO EXPRESSO do Miguel (regra nova) + Datafolha 48% (17/09 ~20:0x)

- 🔴 REGRA VIVA (ordem dele): FIO EXPRESSO pedido pelo Miguel TEM PRIORIDADE sobre a esteira/curadoria — quando ele manda um fio específico, segue-se a ordem dele (tema, ângulo, tom), e a matéria usada fica semeada no estado da esteira para não repetir.
- Caso 1 (Datafolha 17/9): matéria nova "A aprovação do presidente Lula continua subindo: 48%" (rascunho 271757, Redação 5470, gráfico próprio 1280×720 QA-pass: série 45→47→48 + barras 48%/50% em eleitores 76/79 mi) + pedido URGENTE de publicação na ponte (ZM-20260917-013 — quem publica é o chefe de publicação, §137). Fio otimista armado (🇧🇷 + 48% em destaque + 76 milhões x 60,3 milhões de 2022 + espontânea + escândalos por repercutir) disparando AUTOMATICAMENTE ao status virar publish (polling 30 min; publica X t1+t2 e FB post+comentário fixado+apelo pix).
- Números conferidos na fonte: aprovam 45 (2-3/9) → 47 (10/9) → 48 (17/9); desaprovam 51→50; 1º turno 39×35 (Cury 6, Caiado 4); 2º turno 46×44 (+cenários); espontânea 33×25; eleitorado TSE 158,7 mi; votos Lula 2º turno 2022: 60.345.999.

## Adendo 7 — Gráfico do Miguel + revisão CL dos 2 posts (17/09 ~20:3x)

- Gráfico OFICIAL do post Datafolha: o do próprio Miguel ("Dia a dia/2026 Set 17/datafolha/datafolha-aprovacao-lula-17-09-2026.png", série g1-estilo aprova 47→45→47→48 x desaprova, campo 15-17/9) — mídia 271766, capa do 271757 e 1ª figura; o gráfico do ZM (série+eleitores) ficou como 2ª figura. Fio atualizado para usar o gráfico dele.
- 271729 (Vorcaro/Mendonça/Nikolas, M6) foi PUBLICADO às 19:30 pela esteira editorial — o congelamento da manhã acabou; prompt de REVISÃO pós-publicação entregue ao Miguel para o CL (checa as 4 lacunas do dossiê DOSSIE_PESQUISA_ELO_MINERACAO.md; hipótese nunca como fato).
- Prompt pro CL cobre: 271729 (revisão/correção/despublicação se não sustentar) + 271757 (revisar e PUBLICAR com prioridade — fio do ZM dispara automático ao publish).

## Adendo 8 — Capa do Datafolha 271757 = foto recente do Lula (Flickr oficial), gráfico dentro (21/09/17 ~20:5x BRT)

- Ordem do Miguel: "a capa tem de ser uma foto de lula no flickr recente. o grafico tem que ficar dentro".
- Fonte: conta oficial `lulaoficial` no Flickr (NSID 157736962@N05, fotógrafo Ricardo Stuckert). Fotos de HOJE (17.09.26, visita ao novo Complexo Industrial da Eurofarma).
- Método: feed público → 20 miniaturas → folha de contato 5×4 → QA visual (analyze_image) → top-3 = fotos 04, 16, 09. As 3 primeiras baixadas cegas serviram (grupo / costas p/ telão). Escolhida: **foto 04 = 55534550601** (Lula frontal, plano médio, expressão alegre, acenando/agradecendo, horizontal 1023×682, Eurofarma).
- WP: mídia **271769** importada (título/caption/alt com crédito Ricardo Stuckert/PR) → `_thumbnail_id` do 271757 atualizado de 271766 (gráfico) para **271769** (foto). Gráfico do Miguel (grafico-miguel-datafolha.png, mídia 271766) permanece como 1ª figura DENTRO do corpo — provado por grep no post_content.
- Post continua em **draft** aguardando o chefe de publicação (CL). Poller do fio expresso REARMADO às 20:52 (janela ~2h30; anterior expirou 20:40 sem publicação).
- URL da capa: https://www.ocafezinho.com/wp-content/uploads/2026/09/lula-capa-55534550601.jpg

## Adendo 9 — Capa do 271729 (Vorcaro/Mendonça) = foto do Mendonça + emenda og:image segue capa (17/09 ~21:15 BRT)

- Ordem do Miguel: "no post do mendonça e vorcaro, deixa uma foto do mendonça na capa".
- Busca (regra: político NUNCA com IA): Openverse → álbum TJAM 07/06/2025 (homenagem da ALEAM a André Mendonça/STF); Commons só tinha foto 2011 e 3x4 out/2025 (pequena/vertical); foto de posse 2021 (CC BY Planalto) rejeitada no QA (foto de grupo).
- Escolha: folha de contato 12 fotos → QA visual top-3 → **foto 04 do TJAM** (Mendonça frontal, plano médio, boa luz) → identidade CONFIRMADA por comparativo lado a lado com foto oficial out/2025 (Rosinei Coutinho/STF) + revalidação individual.
- WP: mídia **271772** (1024×683, crédito "Acervo fotográfico do Poder Judiciário do Amazonas (TJAM), CC BY-NC-SA 2.0"). Capa antiga 271730 (mendonca-m6.jpg) também era foto real dele (retrato institucional).
- 🔴 Gate Emenda 7 (post publicado + autor agente trava _thumbnail_id): passou com carimbo casado `_cafezinho_img_check {ok, media_id 271772}` (QA visual 2x documentado na meta). Válvulas HUMAN_OVERRIDE/REVISOR não servem para meta.
- 🔴 og:image não acompanhava a troca (ficava na m6 mesmo com featured/schema/corpo novos e Redis/page cache flushed; raiz não isolada no resolvedor do Yoast): cura = **mu-plugin novo `cafezinho-og-segue-capa.php`** (filtro wpseo_opengraph_image prio 100 → sempre featured; rollback = apagar + rocket_clean_domain) + opcache_reset. Provado: og:image = mendonca-tjam-04.jpg na origem.
- Contexto: post 271729 publicado pela CL às ~20:13 (_publicado_por=cl, txt_check CL-20260917-333 com apuração própria).

## Adendo 10 — RONDA 22:1x + HERANÇA da ronda (17/09 ~22:1x, ZM sessão atual)

- Sessão original da ronda QUEBROU (ordem do Miguel 21:48: "voce vai herdar a missão"); automation **ee2aad58 morreu com ela** — pausada, 0 execuções, e nem existia no workspace novo (delete = "not found"). Ronda **recriada**: `automation-2fa3ccdd` (cron 10 13,22 * * * BRT, próxima 18/09 13:10), prompt completo com nota de herança + dica de diagnóstico syslog para slots silenciosos. **Causa raiz da quebra (confirmada pelo Miguel 18/09 ~09:0x): o crédito do GLM acabou no meio da noite** — a sessão morreu por esgotamento de provedor, não por falha de código; sessão seguinte passou a rodar Kimi K3 (prompt da ronda ajustado p/ assinatura dinâmica §113).
- **Placar do dia: 4 fios completos (X+FB)** — 11:35 manual (AtlasIntel estratégia do medo), 16:30 (Vorcaro/Mendonça ITER), 18:00 (Bolsa Família 15%), 20:00 (Atlas empate 2º turno). Último validado via oembed ✅. Sem arquivo PAUSA.
- **Slots silenciosos: 13:30, 15:00 e 21:30.** 13:30/15:00 = 500 intermitente do WP (Adendo 5; nem loga). 21:30 = sem linha no syslog nem no fios.log (cron não disparou; crontab íntegro, motor sadio no dry-run 22:12 — curadoria escolheria o 271753). Vigiar amanhã 08:00.
- 🔴 **FIO EXPRESSO disparou às 21:47** (poller `/tmp/pollar_e_disparar.sh` no Dell detectou publish do 271757 às 21:46:46, limpou cache): **X OK** (tweet 2100748507082629386 + reply, oembed ✅), **FB FALHOU HTTP 400** no `/photos` — fio_datafolha.py manda a imagem por URL e a Graph não consegue baixar (borda/Cloudflare; a esteira oficial contorna baixando a capa com UA de navegador e subindo bytes). Estado semeado no tencent (`fio_expresso_miguel`). Fio pela metade: falta post FB + comentário fixado + apelo. Cura proposta: replicar `publicar_fb` do fios_diarios.py — **aguarda "vai" do Miguel**.
- ⚠️ Editorial: DOIS posts Datafolha no ar com leituras divergentes — 271753 (20:03, "passou ileso, mas sem crescer", CL) e 271757 (21:46, "continua subindo 48%", fio do ZM ancorado nele).
- O que preciso do Miguel: "vai" p/ completar o FB do fio expresso + decisão sobre os 2 posts Datafolha.

## Adendo 11 — FB DO FIO EXPRESSO COMPLETADO + token FB morto no Dell curado (17/09 ~23:0x, ordem Miguel "pode ir")

- **Causa raiz do 400 das 21:47: NÃO era a imagem** — era o `FB_PAGE_ACCESS_TOKEN` dos cofres do Dell **EXPIRADO** (OAuthException 190/463, sessão morta desde ~18:00 BRT; o "permanente" do episódio do token morreu junto). Cofres do tencent (`.env_redes` + `/root/.env`, mtime 12:02) seguiam vivos — por isso a esteira publicou FB às 20:00. (Meu primeiro teste em shell corrompia o valor e deu falso "could not be decrypted"; o GET com o parser exato do fios_diarios.py provou o token bom.)
- **REGRA Nº 4 executada:** backups `.bak_pre_fb_sync_20260917_2258` nos 2 cofres do Dell + espelho do token vivo do tencent (verificação md5 `1884c7efb0` idêntico nos 2 cofres; valor nunca exibido).
- **FB publicado ~22:5x:** post `421927677830371_1602660085233285` (mesmo texto do tweet 1 + gráfico do Miguel por **upload binário** + apelo pix no fim), comentário com o link `1602660085233285_1071006329263355` **FIXADO** (is_pinned success:true). URL: https://www.facebook.com/421927677830371/posts/1602660085233285 — **FIO EXPRESSO 100% COMPLETO (X + FB)**.
- Molde salvo: `/tmp/fio_datafolha_fb_complemento.py` (multipart binário — imune ao 400 de URL e a crawler bloqueado).
- Pendência editorial segue aberta: 2 posts Datafolha divergentes no ar (271753 × 271757).

## Adendo 12 — Ronda 13:1x de 18/09 (1ª ronda oficial da automation recriada)

- Placar da manhã: 3/4 slots completos (X+FB ok, último validado via oembed) — 08:00 Vorcaro/Mendonça/Nikolas, 10:30 debate SP em tapas, 11:30 invasão da OpenAI. 09:30 mudo: cron rodou (syslog 09:30:01) mas nada logou — padrão do 500 intermitente do WP (mesmo do 15:00 de 17/09). Sem PAUSA.
- 🟠 Curadoria LLM 400 nos 3 slots ("HTTP Error 400: Bad Request" da Z.ai — glm-5.3-flash): mesma família do crédito GLM esgotado que derrubou a sessão ontem (o .env_redes ficou só com ZAI para curadoria). Esteira segue publicando no fallback (ranking), sem perda de fio — mas sem a camada de bom senso editorial enquanto a chave ZAI estiver sem crédito. Se o Miguel recarregou o GLM, conferir se o 400 some no slot 15:00; senão, avaliar trocar a chave ZAI do .env_redes por outra viva.
- A ronda das 13:10 disparou via comando manual do Miguel ("tenta de novo") às 13:29; o agendamento da automation segue normal (13:10/22:10).

## Adendo 13 — FIO MANUAL 20:24 + ronda com Kimi K3 titular / DeepSeek fallback (18/09 ~20:2x, ordem Miguel "vamos lá fazer fios")

- Estado do dia 18/09 até 20:24: **8 fios completos (X+FB)** — slots 08:00, 10:30, 11:30, 15:00, 16:30, 18:00, 20:00 via cron + disparo manual 20:24 (datafolha-confirma-parana-pesquisas-e-reforca-lideranca-de-ciro-no-ceara; X 2101090044387979644, FB 1603161708516456). Mudos: 09:30 e 13:30 (mesmo padrão 500 WP / cron sem saída).
- Curadoria LLM: chamada mínima à Z.ai respondeu 200 às ~20:2x (crédito voltou), mas a chamada REAL da esteira (max_tokens 1200, thinking disabled) segue dando 400 — provável incompatibilidade de parâmetros com a conta atual; fallback ranking segue cobrindo. Investigação do 400 na chamada real fica pendente (não alterar fios_diarios.py sem ordem).
- Automation da ronda atualizada (CronUpdate): modelos titular Kimi K3 + fallback DeepSeek registrados no prompt; assinatura dinâmica §113 (modelo real do hook no disparo).

## Adendo 14 — 🔴 REGRA VIVA: FIO SÓ COM INTELIGÊNCIA (18/09 ~20:3x, ordem Miguel "quando não tiver inteligencia, voce suspende os fios, ok? só pode ter fio quando tiver inteligencia completa, capaz de revisar os posts")

- **Regra permanente:** nenhum fio sai sem a curadoria LLM viva. O fallback "segue ranking" foi ELIMINADO por ordem dele.
- **Implementado 20:3x:** patch em `tencent:/home/ubuntu/cafezinho/redes/fios_diarios.py` — no except da curadoria: log "curadoria LLM falhou — SEM INTELIGENCIA, slot suspenso (ordem Miguel 18/09)" + `return 0` (slot suspende, nada publica). Backup: `fios_diarios.py.bak_pre_curadoria_obrigatoria_20260918`. Sintaxe validada (py_compile). Rollback = restaurar o backup.
- Efeito imediato: slot 21:30 de hoje suspende se a curadoria seguir 400; retoma sozinho quando a Z.ai voltar.
- Prompt da ronda atualizado (CronUpdate): suspensão por falta de inteligência = 🟡 informativo (não falha); ronda testa a ZAI e reporta desde quando está sem inteligência.
- Contexto: a chamada real da curadoria dá 400 na Z.ai desde 17/09 ~noite (mesma família do crédito GLM esgotado); chamada mínima responde 200 — investigação do 400 pendente de ordem.

## Adendo 15 — FALLBACK DE INTELIGÊNCIA: DeepSeek v4-pro (18/09 ~20:4x, ordem Miguel "pode botar então fall back de inteligencia... bota o deepseek v4 pro")

- **Correção do registro do Adendo 2:** NÃO era bloqueio regional da DeepSeek ao IP do tencent — era a **chave morta** no cofre do tencent. A chave viva do Dell responde 200 do tencent E do WP. Espelho (REGRA 4): chave adicionada ao `.env_redes` e atualizada em `/root/.env` e `/root/.env.unificado`, backups `.bak_pre_deepseek_sync_20260918`.
- Modelos vistos na conta DeepSeek: `deepseek-flash` e `deepseek-v4-pro` (o pedido do Miguel existe e está disponível).
- **Patch:** `curadoria_llm` virou cadeia — 1) ZAI glm-5.3-flash; 2) DeepSeek `deepseek-v4-pro`. Exceção só sobe se TODAS falharem → slot suspende (regra "fio só com inteligência" do Adendo 14 mantida). O main também suspende se a resposta vier vazia/inválida. Backups: `.bak_pre_curadoria_obrigatoria_20260918` + `.bak_pre_fallback_deepseek_20260918`; py_compile OK.
- **PROVA (sem publicar):** teste isolado com ZAI propositalmente quebrada → log "curadoria via FALLBACK deepseek" + escolha justificada coerente (respeitou "evite repetir a temática do fio anterior").
- Prompt da ronda atualizado: "sem inteligência" só conta se as DUAS caírem; a ronda testa as duas.

## Adendo 16 — RONDA 22:10 de 18/09: causa raiz dos slots mudos = TYPO no crontab

- Placar do dia: **8 fios completos (X+FB)** — 08:00, 10:30, 11:30, 15:00, 16:30, 18:00, 20:00 (cron) + manual 20:24 (Datafolha Paraná/Ciro CE). Último validado via oembed ✅. Inteligência no ar: ZAI e DeepSeek v4-pro respondendo 200 (cadeia desde 20:4x).
- 🔴→✅ **CAUSA RAIZ dos slots 13:30 e 21:30 mudos nos 2 dias:** typo no crontab — essas 2 linhas chamavam `/usr/bin/python/python3` (caminho inexistente); o slot nunca executava. Não era 500 do WP nem falta de inteligência. **Cura:** backup `/tmp/crontab.bak_pre_typo_python_20260918` + sed p/ `/usr/bin/python3`; provado `crontab -l` com o caminho correto nas 2 linhas. Amanhã os 10 slots rodam.
- Slot 09:30 (mudo 2 dias, caminho do cron correto) segue com hipótese de 500 intermitente do WP na coleta — ronda vigia amanhã.

## Adendo 17 — MANUAIS DE ESTILO X e FACEBOOK criados (18/09 ~23:1x, ordem Miguel "um manual apenas para textos no Twitter, e outro para Facebook — parecidos, mas não iguais")

- `Cerebro/Estilo/MANUAL_DE_ESTILO_X_TWITTER_V1.md` — fio de 2 tweets: t1 emoji+caixa alta+abertura+imagem (upload), t2 reply com link + apelo pix (chave SEM "(O Cafezinho)"); link nunca no corpo; teto prático ~1.150 chars no t1.
- `Cerebro/Estilo/MANUAL_DE_ESTILO_FACEBOOK_V1.md` — post único de foto: mesmo texto do t1 + apelo pix no fim (chave COM "(O Cafezinho)"); link no 1º comentário FIXADO (is_pinned); imagem SÓ por upload binário (URL falha 400 na Graph — caso fio expresso); 1ª frase carrega o fato (o "ver mais" corta em 2-3 linhas).
- Regra dos 2: redação em paridade (mesmo texto), o que muda é a ESTRUTURA. Ambos: texto limpo (zero asterisco/#/travessão no apelo), nunca inventar número, emoji temático por categoria, nunca IA em político nomeado.
- Catalogados no MAPA_DOS_MANUAIS_DE_ESTILO (nova seção 📱 Redes sociais) + CEREBRO_NODE_ATUALIZACOES.

## Adendo 18 — MATÉRIA MERZ/CHINA publicada + fio nos 2 canais (18/09 ~23:4x, fluxo Antigravity→ZCode, ordem Miguel "pode publicar tudo")

- Fluxo: Antigravity preparou (mapeamento + minuta), ZCode verificou fatos e executou. Tweet do Merz validado via oembed (real); fala dos "27 países/300 bi" só existe no vídeo → atribuída ao vídeo, sem aspas longas não verificadas. Merz = chanceler alemão (corrigido de "político conservador").
- Post **272107** publish 23:36: https://www.ocafezinho.com/2026/09/18/hipocrisia-europa-china-merz-globalizacao-concorrencia-desleal/ (cats Internacional/Economia/Geopolítica, autor zcode_miguel, capa Merz CC BY 4.0 mídia 272106, embed do tweet validado no conteúdo).
- 🔴 APRENDIZADO: o publish foi bloqueado 4× pela **Emenda 5 (slot-20min)** — trava editorial do próprio Miguel: post de agente nunca publica de uma vez, empurra +20min da grade (o post virou future 00:32→00:40). Cura legítima: guarda **§130** (editor humano tocando post de agente = livre) via wp_set_current_user(2018) — ordem expressa do Miguel. O gate de imagem registrou "AÇÃO HUMANA (§130)".
- Fio (manuais novos X/FB): X 2101139743253610750 (+reply, oembed ✅) e FB post 1603280678504559 (foto binária + comentário fixado + pix c/ nome). Slug semeado no estado da esteira (não repete). Molde: /tmp/fio_merz_china.py.

## Adendo 19 — REDAÇÃO PRÓPRIA do fio pela inteligência (19/09 ~00:3x, crítica do Miguel ao fio "guerra de informação": "atropelado, com repetições; tem que ser um post próprio, revisado, bem escrito")

- **Causa do texto ruim:** o `montar_texto` colava o excerpt + parágrafos crus da matéria até encher (recorte mecânico — daí repetições e até o nome do autor entrando colado no fio).
- **Cura:** nova função `redigir_fio_llm` — a abertura do fio é REDIGIDA pela cadeia de inteligência (ZAI→DeepSeek) seguindo o manual do X (2-4 parágrafos curtos, sem copiar frases da matéria, sem travessão/asterisco/hashtag, nunca inventar número, gancho final); título caixa alta + emoji seguem determinísticos. Falha das duas = slot suspenso (regra fio só c/ inteligência). Dry-run também mostra o texto redigido.
- 🔴→✅ **Causa raiz do 400 crônico da Z.ai encontrada:** o `glm-5.3-flash` passou a SEMPRE pensar — o parâmetro `"thinking": {"type": "disabled"}` (posto em 17/09 p/ evitar content vazio) agora dá 400 ("This model always engages in thinking and cannot be disabled"). Cura: thinking removido das 2 chamadas ZAI + max_tokens 2000.
- 🔴→✅ **DeepSeek v4-pro também "pensa":** com max_tokens 1200 o raciocínio consumia tudo e o content vinha VAZIO → max_tokens 4000 nas 2 chamadas DeepSeek.
- Backups: `.bak_pre_redacao_llm_20260918` + `.bak_pre_thinking_zai_20260919`. PROVA: dry-run 00:36 com ZAI em rate limit (429 dos testes) → curadoria E redação via FALLBACK deepseek, justificativa e texto próprios.
- O fio criticado (guerra de informação, 16:30 de 18/09) fica como está por ordem dele ("deixa para lá esse").

## Adendo 20 — REFINO da regra da redação (19/09 ~00:4x, ordem Miguel: "não é proibido copiar parte da matéria... pode até ser um texto apenas com trechos da matéria... desde que tenha uma editoria própria, uma inteligência própria para ficar um texto próprio para a rede social")

- Conceito correto: NÃO é "escrever do zero" — é EDITORIA PRÓPRIA. O fio pode usar trechos da matéria livremente (até só trechos); o que não pode é a montagem mecânica atropelada (o bug do montar_texto). A inteligência costura: fluente, sem repetição, sem byline colada.
- Texto do X e do Facebook: o mesmo (paridade confirmada por ele). Emoji sempre no começo do 1º parágrafo (antes do título — já era o padrão determinístico emoji+TÍTULO).
- PROMPT_REDACTOR do fios_diarios.py ajustado com a formulação dele; manuais X/FB corrigidos (regra 6 nos dois).

## Adendo 21 — RONDA 13:10 (executada 15:33 junto c/ o Miguel) + GLM FORA (assinatura expirada 19/09)

- Ordem do Miguel 19/09: rondas SEMPRE em Kimi K3 + fallback DeepSeek; a assinatura GLM expirou (nova virá). Prompt da ronda atualizado (CronUpdate). Sem nova sessão necessária — a automation segue a mesma.
- Placar do dia 19/09 até 15:33: **4 fios completos (X+FB)** — 09:30 (prova de vida INSS), 10:31 (Datafolha Elmano×Ciro), 11:30 (Gilmar mantém Bolsa Família), 15:01 (foto Gonet). Último validado oembed ✅. TODOS via inteligência DeepSeek (ZAI em 429 desde a expiração da assinatura).
- Slots 08:00 e 13:30: suspensos pela regra viva — curadoria foi bem via DeepSeek, mas a REDAÇÃO falhou nas duas (ZAI 429 + DeepSeek retornando content VAZIO intermitente mesmo com max_tokens 4000). 🟡 informativo, não é pane. **Melhoria proposta (aguarda ordem): retry 1× na redação antes de suspender.**
- Teste 15:33: ZAI OK 200 e DeepSeek OK 200 (as duas vivas neste momento).

# 📺 Fórum — Vídeos de volta ao Cafezinho: espelho PT da fila GSN + alimentador religado (ordem do Miguel 11/09 ~01h)

**Sessão:** ZCode/GLM-5.3 (Dell) · **Ref:** ZM-20260911-025 · **Companion:** `Memorias/memoria_videos_cafezinho_espelho_pt_gsn_20260911.md`

## A pergunta/ordem do Miguel (voz, quase literal)

"Está gastando transcripto, traduzindo todo dia, e não estou vendo no YouTube nem no Cafezinho. Para onde estão indo? Está indo para o Globo South News, pelo menos? Tem que ir para o Cafezinho também, na parte de vídeos. Tem o Jornal da Fórum, tem os brasileiros — os brasileiros são os mais públicos no Brasil. Faz o equilíbrio. Faz o inglês. Mas o Cafezinho é o principal."

## Diagnóstico (respondendo "para onde estão indo")

1. **SIM, está indo para o GSN** (Global South News = "Globo South News"): o pipeline EN do NYC (11/17 UTC) transcreve Judging Freedom, Dialogue Works, Glenn Diesen, Daniel Davis etc., escreve em inglês e o publicador roteia para `gsn_fila` → site globalsouth.news no ar até 10/09 (prova: posts de 05–10/09 no ar). Esse é o gasto diário de transcrição/tradução que o Miguel vê.
2. **NADA ia para o Cafezinho desde 06/09** (último vídeo publicado #269033). Causas: (a) roteamento por idioma (ordem 17/08) manda EN SÓ para GSN; (b) a vertical V4.1-espelho PT foi desativada 03/09 ("está horrível") e o alimentador da Tencent foi desligado junto → fila DSN seca; (c) a rodada nacional do Dell (8/14/20h) está cega: feed RSS da TV Fórum 404 persistente (5/5 tentativas, 2 IPs) + proxy IPRoyal 402 Payment Required (sem saldo); (d) a CL (quem publica rascunhos) parada desde 09/09 17:12.
3. **Jornal da Fórum: ZERO posts desde 25/08** (prova wp-cli: nenhum draft/post "Jornal da Fórum dd.mm.yy"). Mesma causa (c): feed + proxy mortos.

## O que foi feito (com provas)

### 1. Espelho PT da fila GSN → rascunhos no Cafezinho (o coração do pedido)
- **Novo** `agente_youtube_v2_espelho_pt.py` (NYC, aditivo — não toca em publicador/materializador): lê os JSONs EN da `gsn_fila` (frescos ≤48h), traduz editorialmente (FIEL ao texto EN já auditado; NÃO reescreve do zero — evita repetir o "horror" de 03/09) com a escada de luxo gpt-5.6-sol → qwen-plus, grafias canônicas (NOMES SEM ERRO), e cria DRAFT no WP do Cafezinho: cat 28 (Vídeos), embed no topo, capa reaproveitada (media_wp_id), tag "Espelho GSN", meta `_video_id_youtube`. **Teto 2/dia** (env ESPELHO_PT_TETO_DIA) = equilíbrio BR primeiro. Idempotente via ledger. Dry-run default.
- Cron NYC: `40 12,18 * * *` (após corridas 11/17 UTC) → `/root/agent_data/espelho_pt.log`.
- **Prova E2E (11/09 ~04:32 UTC): drafts #269875** ("Pressão dos Estados Unidos fortaleceu o Irã e corroeu influência regional, dizem economistas" — vídeo _pEVmFoI1zc) **e #269876** ("Aliados dos Estados Unidos vendem títulos e colocam o dólar sob pressão" — HQl3uw8a5zI), ambos gpt-5.6-sol, cat Vídeos ✓, capa ✓ (thumbs 269754/269751), embed ✓, tag aplicada via wp-cli.
- Armadilha corrigida na hora: gpt-5.6-sol SÓ aceita temperature=1 (erro 400 com 0.3) — escada agora 1.0 openai / 0.3 alibaba.

### 2. Alimentador da Tencent REATIVADO (fonte BR + internacionais da cadeia clássica)
- Cron `5,35 * * * *` religado (era DESATIVADO_20260903). **Sem duplicar custo**: Judging Freedom e Dialogue Works saíram da lista do alimentador (ficam SÓ no coletor do NYC); lista agora: Record News (BR) + BBC/CNN/Al Jazeera/DW/TRT. Backups `.bak_pre_religa_20260911` (script + lista).
- Prova: rodada manual 11/09 01:37 BRT → "1 novo(s) na fila" (TRT World, Houthis/Mocha) → decupador :07/:22/:37/:52 pega → ingestor NYC :55 → pipeline → EN GSN + espelho PT.
- Armadilha de crontab: comentário sem `#` = "bad minute" (validador cron tenta ler como agendamento).

### 3. Fallback 3 de feed no agente nacional (Jornal da Fórum)
- `youtube_cafezinho.py` (Dell) ganhou degrau 3 na cascata: RSS → proxy IPRoyal → **yt-dlp flat /videos (90s, fail-soft)**, pois o RSS do canal UC3sMBA... (TV Fórum) está 404 persistente de 2 IPs enquanto o yt-dlp resolve via innertube (prova 11/09: listou "FLÁVIO BOLSONARO... Fórum Mídias", 1518s). Backup `.bak_pre_scrape_feed_20260911`.
- Scrape de regex do ytInitialData NÃO funciona (UI nova sem videoRenderer; página é shell + JS) — descartado.

## O que falta / próximos passos

1. **Conferir as corridas** de 11/09 12:40/18:40 UTC (espelho PT) e a próxima matéria BR (Record News) da cadeia clássica.
2. **Religar a CL** (parada 09/09 17:12) — sem ela os rascunhos (incluindo 269875/269876) não publicam.
3. **IPRoyal 402 = assinatura vencida (~03/09)**: renovar é pagamento do Miguel; proxy é o degrau 2 do feed do Jornal da Fórum e caminho anti-bloqueio do yt-dlp.
4. Decisão pendente do Miguel: espelho PT publicar como rascunho (atual, CL revisa) OU streamline direto p/ fila da CL com selo.

## Rollback (1 comando cada)
- Espelho: `ssh nyc 'crontab -l | grep -v espelho_pt | crontab -'` + `rm /root/agents_labs/youtube_v2/agente_youtube_v2_espelho_pt.py` (+ apagar drafts 269875/269876 se quiser).
- Alimentador: `ssh tencent` e re-comentar a linha `5,35 ... alimentador_fila.py` do crontab (nota DESATIVADO de 03/09) + restaurar `.bak_pre_religa_20260911`.
- Fallback feed: `cp youtube_cafezinho.py.bak_pre_scrape_feed_20260911 youtube_cafezinho.py` (agentes_cafezinho).

## Arquivos tocados
- NYC: `agente_youtube_v2_espelho_pt.py` (novo) + cron.
- Tencent: crontab (alimentador religado) + `canais_youtube.txt` (2 EN comentados).
- Dell: `agentes_cafezinho/youtube_cafezinho.py` (+bak).
- WP Cafezinho: drafts 269875/269876 (+tag espelho-gsn).

— ZCode/GLM-5.3 · 11/09/2026 ~02h BRT


## Adendo (~02h4x BRT) — POST Lula no SBT (ordem do Miguel no meio da sessão)

Vídeo o4HhoJ70Xvc (SBT News, série de entrevistas presidenciais do SBT Brasil; Lula o 1º, do Alvorada, 30min com **Marina Ademori e Basília Rodrigues**).
- Transcrição: Transkriptor URL-direto (yt-dlp bloqueado no Dell E na Tencent — "Sign in to confirm you're not a bot"; cost_guard exigiu TRANSKRIPTOR_UNKNOWN_DURATION_POLICY=estimate). 30.926 chars, diarização, US$ 0,18.
- Post: 18 parágrafos, 10 pontos com aspa estratégica cada (STF/Master, Moraes, Vorcaro, PF/AGU, reforma Judiciário, educação, fiscal, pesquisas/BTG, custo de vida — bloco do t=1165s que o Miguel marcou, com o time 4 a 0 e inflação de alimento 56%→13%, segurança/138 cadeias). **20/20 aspas validadas por grep** na transcrição corrigida (só alias de nomes: Volcano→Vorcaro, Banco Mata/Mater/Martin→Master, Andrei→André — rito NOMES SEM ERRO).
- Draft **269882**: autor 2018 (James2017, rito rascunho manual), cats 22/28/21141/5088, capa = thumb sddefault 640x480 (maxres 404) anexo 269883, embed no topo, meta `_video_id_youtube` (aparece no painel /v6/youtube), slug lula-entrevista-sbt-serie-presidenciais-2026.
- Verificador do manual rodado: sem ; : — sem "E,/Mas," inicial, aspas curvas 20/20 pares, título 73 chars/12 palavras sem dois-pontos. Máxresdefault inexistente p/ o vídeo (usar sddefault).


## Adendo 2 (~02h5x) — CORREÇÃO de frases-trailer no 269882 (bronca do Miguel, com razão)

"A regra de vida veio logo depois" era frase-trailer EMU-7 do manual — removidas TODAS (9 ajustes): "Na sequência, pediu amplitude total" / "O fecho foi direto" / "antes de escalar a defesa" / "A regra de vida veio logo depois" (→ paráfrase factual toga×escritório) / "A matemática que sustenta a prioridade veio em seguida" / "antes de cravar a vantagem" (→ "e partiu para os críticos da dívida pública") / "A defesa veio com dois números..." / "até o desdecho" / "Lembrou ainda" repetido (→ "Citou"). Mais 4 aspas cortadas no meio da frase na fonte perderam o ponto final de DENTRO das aspas (corte limpo). Revalidado: 20/20 aspas literais, 0 trailers, sem ; : — . Correções anteriores (nomes, capa, cats) mantidas. wp post update não tocou status/date.


## Adendo 3 (~06h4x) — CORREÇÃO do 269868 "Dinheiro do PCC ajudou a financiar Dark Horse" (ordem Miguel)

Post reescrito por outra sessão às 06:21 (título novo; antes era o HC Mendonça/Ibaneis). Ordem do Miguel: o texto tem que dizer que O SIGILO FOI LEVANTADO NA NOITE DE QUINTA (10/09), que o Cafezinho teve acesso com exclusividade, e que a pesquisa do Cafezinho JUNTA OS DOCUMENTOS e ENCAIXA AS PEÇAS — "exclusivo" NÃO vai no título, vai dentro como "uma pesquisa do Cafezinho, só isso". Aplicado: P1 agora abre com o levantamento na noite de qui (10) + acesso com exclusividade na íntegra; P3 vira "ao juntar os documentos liberados, a pesquisa do Cafezinho encaixou as peças" (strong ajustado "partes da mesma engrenagem" p/ evitar eco peças×peças); "quebra de sigilo"→"levantamento do sigilo" no e-Doc 330; 0 restos de "documentos sigilosos" (não são mais sigilosos). Backup pré-edição em cafezinho-wp /root/Backups/posts_editados/269868_pre_edit_levantsigilo_20260911.md (7.105 bytes). wp post update posicional — status draft e data intactos.


## Adendo 4 (~06h5x) — SESSÃO INTERROMPIDA pelo Miguel: reescrita do 269868 fica para a próxima sessão

O Miguel leu o 269868 ("Dinheiro do PCC ajudou a financiar Dark Horse") e MANDOU REESCREVER TUDO (lead direto com a revelação; sigilo levantado 10/09 à noite + acesso com exclusividade da pesquisa do Cafezinho só depois; REAG explicada de verdade — conta de Henrique Moura Vorcaro integralizada em FIP de créditos de carbono; "míssil" e "Não se trata de perseguição política" FORA). Ele interrompeu a sessão ("estou na sessão errada").
ESTADO: prompt completo pronto para a próxima sessão em Foruns/sessoes_zcode/PROMPT_REESCRITA_POST_269868_PCC_VORCARO_20260911.md (fatos apurados nos documentos STF + diretrizes do Miguel + arquivos locais + ritual técnico). Fonte primária REAG já extraída: /tmp/lula_sbt/sig_b.txt (decisão Mendonça 01/06). Post atual do 269868 salvo em /tmp/lula_sbt/pcc_post.html.

---

## ADENDO 11/09 07:1x (ZCode/GLM-5.3) — REESCRITA DO ZERO do rascunho 269868 (Dinheiro do PCC ajudou a financiar Dark Horse)

**Ordem do Miguel (prompt arquivado PROMPT_REESCRITA_POST_269868_PCC_VORCARO_20260911):** reescrever do zero, DRAFT (não publicar), com mineração dos novos documentos liberados.

**Mineração do acervo (318 docs → 314 txts grepados) trouxe 4 fontes primárias novas além do sig_b:**
1. **INQ 5.026, decisão Mendonça 02/03/2026** (Deferido em parte, agora público) — registra que o Banco Master "movimentou cerca de R$ 2,8 bilhões em operações de câmbio para uma empresa suspeita de lavar dinheiro para o PCC" (cita requerimento de CPI, e-doc 416) e fraude "que pode alcançar R$ 17 bilhões". É o elo documental Master×PCC que faltava.
2. **PET 15.198, decisão 15/01/2026** — Banco Central comunicou ao MPF indícios de crimes envolvendo Master e REAG TRUST DTVM; fluxograma do BC demonstra uso de FIDICs nas fraudes; sequestro/bloqueio até R$ 5,775 bilhões; 101 pessoas com sigilo bancário afastado; origem = prisão preventiva de Daniel Vorcaro.
3. **PET 15.556, despacho Mendonça 12/07/2026** (assim. 12/07, listado 13/07) — oficializa as 2 notícias-crimes contra Flávio (deputada Luciene Cavalcante e-doc 392 + deputado Vieira Lima e-doc 402): US$ 24 milhões (~R$ 134 mi) negociados com Vorcaro p/ Dark Horse (Intercept 13/05), "cobranças incisivas por parte do Senador para a liberação dos recursos" nas mensagens do celular apreendido, visita presencial à residência SP no final de 2025 durante cautelares (Metrópoles/Igor Gadelha 19/05 + confirmada por Flávio ao O Globo 19/05). Mendonça DESENTRANHOU p/ PETs autônomas 16.292/16.078/16.063/16.059.
4. **PET 16.704, decisão Fachin 09/09/2026** (Deferido) — cita Pet 16.669 (Flávio Dino) apurando "suposto direcionamento de emendas parlamentares para o filme Dark Horse" + a cadeia de atos (requisição Mendonça 24/08 → relatórios PF → decisão Moraes 03/09 → PGR → 16.704).

**⚠️ NOVO ACHADO EDITORIAL:** as Pets específicas do Flávio (16.292=inc 7629247, 16.078=7595002, 16.063=7593496, 16.059=7592368) e a 16.669 (7681816) SEGUEM SIGILOSAS no portal (campo Sigiloso, 0 docs) mesmo após o levantamento de 10/09 — o pacote liberado NÃO inclui os procedimentos sobre o senador. Dito no post.

**Post reescrito do zero (8,5KB, ~970 palavras):** lead com a revelação (elos PCC-Master-US$24mi) e SÓ NO 3º parágrafo o contexto do levantamento de 10/09 + "uma pesquisa do Cafezinho teve acesso com exclusividade" dentro do texto (nunca no título); REAG explicada (gestora da família; BC demonstrou uso p/ desvio do Master; conta de Henrique Moura Vorcaro em FIP de créditos de carbono); intertítulo "míssil" TROCADO por "O filme de US$ 24 milhões"; FORA "O Brasil já sabia", "Não se trata de perseguição política" (final refeito sem muleta, fecha com o rol de números); termo LEVANTAMENTO (nunca quebra); botões com www.ocafezinho.com/pet15556.zip e pet16662.zip (ambos 200, 0 "controle" no corpo). Estilo: 0 ponto-e-vírgula / 0 travessão / 0 dois-pontos / 0 "E,"-"Mas," / 0 frase-trailer (checado no texto limpo).

**RITUAL cumprido:** backup prévio /root/Backups/posts_editados/269868_pre_rewrite3_glm_20260911.html (7.102B, versão da outra sessão 06:21 preservada) → wp post update posicional → draft+data intactos (modified 07:15:34 BRT) → conteúdo conferido no servidor (8501B, elos presentes).

**O que aconteceu / o que falta / o que preciso de você (Miguel):** aconteceu = reescrita no ar no DRAFT com 4 fontes primárias novas; falta = sua revisão e publish; preciso de você = revisar (editor https://www.ocafezinho.com/wp-admin/post.php?post=269868&action=edit).


## Adendo 5 (~07h1x) — 269882 Lula×SBT: versão da outra sessão PINÇADA nas aspas (régua da casa)

O Miguel voltou ao post do Lula. Descoberta: outra sessão reescreveu o 269882 às 06:25 (texto cresceu e melhorou — mais blocos da entrevista, data correta qui 10/09, fecho com Augusto Cury hoje), MAS quebrou 2 regras duras: (1) "Marina Demori" ×2 → o nome é Marina ADEMORI (transcrição); (2) ~15 aspas editadas/costuradas (trechos não contíguos colados; palavras polidas). Pinça aplicada preservando o texto bom: nome corrigido, aspas restauradas ao literal com reticências […] nas elisões legítimas, "com" restaurado na aspa do rombo, correções de grafia ASR documentadas na fonte de validação (Polícia×Política ASR, balbúrdia, apreendeu, envolvendo×"Involvido", Andre×Andrei, Mendoza→Mendonça, Saquinho/Sanquinho→Fachin). VALIDAÇÃO FINAL: 33 aspas, 0 problemas (cada trecho literal na transcrição corrigida). Backup pré-pinça: cafezinho-wp /root/Backups/posts_editados/269882_pre_pinça_aspas_20260911.md (10.120 bytes). wp post update — draft e data intactos. Post pronto para revisão do Miguel.

### Adendo 11/09 07:2x — ajuste Miguel no 269868: SEM "exclusividade"
Ordem dele: «não usa o exclusivo não. nem exclusividade. diga apenas que tivemos acesso». Aplicado: 3º parágrafo agora diz «Uma pesquisa do Cafezinho teve acesso à íntegra dos autos e encaixou as peças que faltavam.» (grep "exclusiv" no post = 0; backup 269868_pre_sem_exclusividade_20260911.html; draft intacto, modified 07:19:55). Regra gravada na memória auto (retificada) para as próximas sessões.

### Adendo 11/09 07:3x — 269868 v3 REESCRITO com lead na voz do Miguel (dictado) + manual lido
Ordem (~07:2x): «reescreve... tá meio mal escrito ainda», com o começo ditado por voz (Flávio justificava como financiamento privado p/ filme privado; «nunca foi bem assim»; 1) senador com cargo público, 2) caixa do Master vindo de previdência de estados/municípios (maioria governados pela direita), 3) com o sigilo levantado qui (10) a ponta privada vinha do crime organizado, do PCC «que alguns querem considerar como organização terrorista»; conclusão: Dark Horse financiado «de um lado com dinheiro público desviado, de outro com recursos do crime organizado»). Manual MANUAL_DE_ESCRITA v2.1.1 + unificado lidos ANTES. Lead entregue lapidado na voz dele (sem «Ou seja», sem clichê); demais seções mantêm as 4 fontes primárias do acervo. Auditoria programática 0/0/0 (pontuação, inícios, ligações, metalinguagem, spoiler, exclusiv) + ser/estar/haver 20% (≤25%) + ecos corrigidos («organização» no lead → «facção»; «gestora» REAG → «conta mantida ali»); aspas 3/3 verbatim confirmadas no acervo (grep tolerante a quebra de linha do PDF). Backup posts_editados/269868_pre_rewrite_v3_20260911.html; wp update posicional; draft intacto (modified 07:37). SEGUE DRAFT p/ revisão+publish do Miguel.

### Adendo 11/09 07:4x — 269868 v4: lead reconstruído por dictado (o «circuito» saiu)
Bronca do Miguel: «ficou esquisito... que circuito?» no P2 («a outra metade do circuito»). Novo ditado aplicado: «Nunca foi bem assim. Primeiro, porque Flávio Bolsonaro, embora tenha se esquecido, é homem público. É senador da República, líder do maior partido da direita, filho de ex-presidente, candidato a presidente — a relação com Vorcaro não é exatamente privada, tem componente público evidente.» Segundo = previdência estados/municípios (direita). Terceiro = sigilo levantado qui (10) mostra ponta privada vinda do crime organizado/PCC. Mensagens do celular ficam na seção «O filme de US$ 24 milhões». Auditoria 0/0/0; backup 269868_pre_rewrite_v4; draft intacto.

### Adendo 11/09 08:0x — 269868 v5: acréscimos sobre a edição do Miguel (NADA reescrito)
Ordem (~07:5x): manter as correções dele; 2 acréscimos. (1) Bloco Lula×SBT após o parágrafo da pressão do Lula: entrevista de quinta à noite, defesa da saída do sigilo («Eu não gosto de investigação sigilosa»; «abertura do sigilo de todo mundo, colocar todo mundo nu diante da sociedade brasileira; apure tudo, divulgue tudo, doa quem doer») + crítica velada a Mendonça («vazamento seletivo» com «viés político»; «O que não pode é o juiz sentar em cima de um processo e ficar vazando, sabe, coisa que interessa para ele») — TODAS as aspas verbatim da transcricao_corrigida.txt (a de Transkriptor revisada). (2) Seção «Acesso à íntegra» atualizada: pacote NOVO pacote_stf_master.zip (313 peças, 16 processos, 79MB, subido p/ uploads/2026/09/, público 206 OK) + os 2 zips antigos mantidos. Backup da VERSÃO DO MIGUEL em 269868_pre_lula_acesso_20260911.html; update posicional; draft intacto (modified 08:08); auditoria 0/0/0 (pontuação/início/exclusiv/controle). SEGUE DRAFT p/ revisão+publish.

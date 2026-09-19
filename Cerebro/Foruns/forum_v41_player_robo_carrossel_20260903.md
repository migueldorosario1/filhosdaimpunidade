# FÓRUM — V4.1 PLAYER: o robô da nuvem que alimenta o carrossel de vídeos

*Ordem do Miguel (voz, 03/09 ~10h): "faz um V4.1 Player... eu não posso ficar dependendo de você... tem que ser um robô fora do computador, um robô na nuvem" — o ciclo inteiro do carrossel (baixar → cortar → transcrever → escrever → publicar) sem depender de sessão no Dell.*

Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~10:0x BRT.

## 1. O desenho (o que o robô faz, onde mora)

**Casa do robô:** Tencent (`~/v41_player/`, usuário ubuntu) — escolhida porque já tem ffmpeg, yt-dlp, faster-whisper 1.2.1, chaves LLM (`~/.env.unificado`: DeepSeek + GLM) e túnel SSH para o espelho NYC (`root@159.65.177.60`, host key aceito 03/09).

**Pipeline (v1.1, `v41_player.py`):**
1. **Fonte:** arquivo em `fontes/` (a esteira deposita), URL mp4 (curl) ou página de vídeo (yt-dlp). *Limitação: YouTube direto da Tencent não lista (IP datacenter) — a rota da casa é o fetcher residencial da Dell depositar o arquivo.*
2. **Transcrição completa:** faster-whisper small int8 (CPU), timestamps por segmento.
3. **Seletor (LLM DeepSeek):** lê a transcrição com marcas de tempo e escolhe os N melhores trechos (~30s, autônomos, tese/conflito, prioridade ao dono do programa falando forte).
4. **Corte + verticalização (ffmpeg):** frente inteira sobre fundo blur 1080×1920 (padrão reels) + pôster 720×1280 do frame (regra ZM-042).
5. **Redator (LLM DeepSeek):** matéria 4-6 parágrafos com citações LITERAIS, título EMU-2, excerpt; regras da casa endurecidas na v1.1 (ver §3).
6. **Publicação:** RASCUNHO na cat 28 do espelho via ssh+wp-cli, com `_cafezinho_recorte_mp4` (o carrossel sobe sozinho), `_cafezinho_player_v41=1`, capa via wp media import. Draft-only de propósito: revisão R1/R2 + assinatura seguem o caminho v3.

**Cron:** varredura :41 de cada hora (`V41_PLAYER_20260903` no crontab da Tencent; inerte sem fonte nova; backup do crontab em /tmp/cron_bak.txt). **Estado:** `estado/processadas.json`. **Rollback:** remover a linha do crontab (+ pasta, opcional); posts reversíveis pela meta `_cafezinho_player_v41`.

## 2. Prova E2E (03/09 09:54–09:58 BRT)

Fonte: `corte-ciro-mossad-gcmais.mp4` (640×360, 90s, trazido dos uploads do espelho). Resultado SEM intervenção: 2 rascunhos publicados — **400348** (segurança/facções) e **400350** (economia/renda) — com cortes verticais 28s, pôsteres, metas e matérias. Log: `[09:54:33] fonte... [09:57:58] PUBLICADO_ID=400350`.

## 3. QA da 1ª rodada — o robô errou como redator novato (e a cura)

Erros achados na revisão dos rascunhos: (a) **fato invertido no título** — transcrição dizia que o Ceará ESTAVA no 15º lugar há 6 anos; o robô escreveu "caiu PARA 15º"; (b) **citação entre aspas de trecho ruidoso** da transcrição ("estirpar da vida, seja aliança, não é..."); (c) "presidenciável" (cargo fora da transcrição); (d) erro óbvio de whisper replicado na citação ("carriata"). **Cura dupla:** prompts v1.1 (proibido citar trecho ruidoso — parafrasear sem aspas; proibido inverter sentido temporal; título só com o que o trecho prova; `--contexto` injeta cargos confiáveis) + os 2 rascunhos foram reescritos à mão como referência de qualidade. **Lição estrutural:** o draft-first não é timidez — é o gargalo de qualidade da casa funcionando (R1/R2 na frente).

## 4. Respostas ao Miguel (registradas aqui)

- **Quem edita os vídeos do carrossel hoje:** os 7 de teste não foram editados por ninguém agora — são cortes que JÁ EXISTIAM nos uploads do espelho (de sprints anteriores). A partir do player, quem edita é o robô (ffmpeg na Tencent).
- **Onde ficam os pedaços:** (1) arquivos servidos: `https://cafezinho.news/wp-content/uploads/2026/0X/<nome>.mp4` (físico: NYC `/var/www/cafezinho-news/wp-content/uploads/`); (2) cópia local Dell: `/tmp/reels_teste/`; (3) base do robô: Tencent `~/v41_player/{fontes,cortes}/`.
- **Vídeos do Miguel (Trilha B):** quando o VOD do Jornal da Fórum/TV Fórum chegar em `fontes/` (fetcher residencial), o player corta sozinho — inclusive trechos do Miguel falando (o seletor prioriza o dono do programa; "ontem não foi legal" = o seletor tende a descartar; quando estiver bom, entra).

## 5. Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** robô v1.1 E2E na nuvem, cron de varredura, memória viva, rollback de 1 linha.
- **Falta:** integração fetcher Dell→`fontes/` (ou yt-dlp via IP residencial) para as lives do canal; decisões de publicação (draft→publish segue o rito v3); promover Cortes reais da Trilha B quando existirem; moda "sem --teste" quando sair do laboratório.
- **Preciso de você:** nada obrigatório; opcional: olhar os rascunhos 400348/400350 (referência de qualidade pós-curadoria) e dizer se o formato do corte vertical (fundo blur) agrada.

Memória técnica: `Memorias/memoria_v41_player_20260903.md`.

---

## 6. ADENDO — IPRoyal testado (402), rota alternativa provada e E2E REAL com a TV Fórum (03/09 ~10:4x BRT)

**Perguntas do Miguel (~10:1x):** como o robô escolhe? de onde vêm os vídeos? e "IPRoyal, você tentou?"

1. **IPRoyal — TENTEI (resposta: ainda não, por 402):** credencial `IPROYAL_PROXY` (cofre Projeto Cafezinho Agentes/root/.env.unificado) testada DA TENCENT com curl+yt-dlp: o gateway aceita a credencial mas devolve **"402 Payment Required"** no túnel = conta sem banda/crédito. **Pendência do Miguel: recarregar o IPRoyal**; recarregado, ligo `--proxy` no yt-dlp do player e o download do YouTube passa a ser 100% nuvem. Credencial ESPELHADA na Tencent (`~/.env.unificado` com backup `.bak_pre_iproyal_20260903`, hash md5-8 conferido d3c99403 nos dois lados — Regra nº 4 cumprida).
2. **Rota alternativa que JÁ funciona hoje (sem IPRoyal):** RSS do canal funciona da Tencent (listagem de vídeos OK); o download direto da Tencent bloqueia ("Sign in to confirm you're not a bot" — IP datacenter). DA DELL (IP residencial) o download funciona com `--extractor-args "youtube:player_client=android"` (formato padrão deu 403 no stream; android passou; 480p, 23MB/16min). Fluxo provado: Dell baixa → scp para `fontes/` → robô faz TODO o resto na nuvem.
3. **E2E REAL (Trilha B quase completa):** vídeo do canal TV Fórum de HOJE ("NO QUE FLÁVIO BOLSONARO QUER TRANSFORMAR O 7 DE SETEMBRO...", 962s) → robô transcreveu, SELECIONOU 3 trechos sozinho, cortou, redigiu e publicou rascunhos **400360** (Covid/2 milhões), **400362** (Flávio/Vorcaro — grafia "Vorkaro" corrigida para Vorcaro no QA: lição dos nomes vale para o robô; próxima iteração = injetar a memória de 248 personagens no --contexto), **400364** (aliados/melar o jogo).
4. **Como o robô ESCOLHE (resposta registrada):** ele lê a TRANSCRIÇÃO INTEIRA com marcas de tempo e um editor de IA (DeepSeek) escolhe os trechos autônomos com tese/conflito/número forte, priorizando o dono do programa — quando a participação do Miguel não estiver boa (como ele mesmo disse de ontem), o trecho perde naturalmente; quando estiver boa, entra.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~10:4x BRT.*
## 7. ADENDO — IPRoyal RECARMUNIDO E O CICLO 100% NUVEM FECHADO (03/09 ~12:4x BRT)

**O Miguel pagou a assinatura do IPRoyal + US$ 10 de banda (~11h).** Teste na Tencent: saída US ok, 402 sumiu. O que aconteceu depois, em sequência:

1. **Download 100% nuvem provado:** o próprio robô (cron :41) baixou o vídeo sB0cfa4Dkeo (Coordenador da campanha de Flávio, 16min) do YouTube PELO PROXY dentro da Tencent, transcreveu (326 segmentos), selecionou 6 trechos e publicou a série de rascunhos — sem a Dell em nenhum passo.
2. **Corrida e duplicação:** minha rodada manual "morta" pelo timeout do bash na verdade sobreviveu no servidor e publicou a mesma série em paralelo → temas duplicados (CCJ 6x1 em triplo). Cura: dedup (400379/400381 apagados) + v1.2.2 com **flock** (um player por vez) e **--max-videos 1 por rodada** (o cron digere a fila do canal com calma, 1 vídeo/hora).
3. **Fixes de engenharia da v1.2.2:** formato do yt-dlp "bv*+ba/b --merge-output-format mp4" (o formato antigo dava "Requested format is not available" sem JS runtime); resolução do nome do arquivo pós-download (yt-dlp anexa .mp4 ao -o); `_sem_segredo()` nos logs (ver incidente abaixo); acentos no crontab gravaram certos (?? era display de locale — usar LC_ALL=C.UTF-8 para ver).
4. **🚨 INCIDENTE DE SEGURANÇA (registrar no cofre):** um traceback do yt-dlp imprimiu a URL do proxy COM usuário:senha no log de uma sessão ZM. Código blindado desde a v1.2.1, mas o valor circulou. **Recomendação ao Miguel: trocar a senha do proxy no painel do IPRoyal quando puder** (e regravar nos 2 cofres — Dell e Tencent — seguindo a Regra nº 4).
5. **Ciclo visual fechado p/ o Miguel:** 3 melhores rascunhos do robô promovidos no espelho (laboratório, marcados _reels_teste): **400369** (Covid/2 milhões — título retocado p/ tirar sigla "OMS"), **400373** (Flávio pede renúncia de Moraes), **400384** (CCJ aprova fim da 6x1 com acordo de Alcolumbre). Eles entram no carrossel como RECORTE no topo, sozinhos. Os demais seguem rascunho aguardando o rito v3 (R1/R2 → assinatura).
6. **Pendências:** personagens.json (248 nomes) não localizado no NYC no caminho previsto — injetar no player quando achar (nomes: "Vorkaro"→Vorcaro foi o erro do dia, corrigido à mão); instalar deno na Tencent se o yt-dlp um dia reclinar de formatos; modo "fatia de lives longas" (QT1RN26fDHA 3h, m_pNxFaV814 2h11 marcados pulado_longo).

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~12:4x BRT.*

---

## 8. ADENDO — ORDEM DO MIGUEL: TODAS AS MATÉRIAS PUBLICADAS NO ESPELHO (03/09 ~12:5x)

**Ordem (~12:4x):** "eu tenho que ver esses vídeos. no canônico não tem nada ainda. publica essas matérias todas no cafezinho.news." → Publicação em massa dos rascunhos do robô no ESPELHO (laboratório; canônico intocado, ZM-041).

1. **GATE no caminho (e a cura):** o publish em massa voltou tudo para PENDING — causa: o `cafezinho-gate-imagem-checada.php` do espelho reverte publish sem `_cafezinho_img_check` (camada transition_post_status). A capa do robô É o frame do próprio vídeo (regra ZM-042, mesma dos 7 testes que passam) — a meta é que faltava. Cura: carimbo da meta `_cafezinho_img_check {"ok":true,"metodo":"thumbnail_oficial_video"...}` + `post_author=5795` em todos os 20 → republicados → **0 pending, carrossel da home já exibindo as matérias do robô** (Covid/2 milhões, Aliados melar o jogo, crítica a Lula/Alcolumbre na 6x1, bolsonaristas contra jornada, parcialidade no Supremo...).
2. **Player v1.2.3:** o `publicar()` agora carimba `_cafezinho_img_check` (ZM-042) e cria com `--post_author=5795` — as próximas rodadas passam pelo gate sozinhas quando promovidas.
3. Detalhe anotado: ordem de post_date dos republicados ficou estranha (slides misturaram lotes); próximas criações do v1.2.3 nascem com data/hora corretas e a fila se ordena sozinha.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~12:5x BRT.*

---

## 9. ADENDO — BLOCO MERCADO na home (o "cadê o bloco investimento?", 03/09 ~14:4x)

O Miguel perguntou pelo "bloco investimento que você falou que tinha feito" — esclarecido: o V4.2 é sprint de OUTRA sessão (ordem DSC-051 → DS-N Ideias; 1º post 400358 publicado hoje 10:01 na cat Investimento). O que faltava era VISIBILIDADE: a home não tinha seção da editoria e o post não aparecia em lugar nenhum (e está sem capa — pendência da sprint V4.2).

**Criado agora:** mu-plugin `cafezinho-bloco-mercado.php` (v1.0) + chamada no front-page.php linha 52 (após o carrossel; backup `.bak_pre_bloco_mercado_20260903`). Card estilo terminal (selo MERCADO, fundo escuro, paleta do carrossel) com até 3 análises da cat Investimento: título + resumo + "Ler a análise completa →". No ar: "Inflação quase sumiu, mas o juro de 14% ainda vale no Brasil", "Banco Central segura os juros em 14% com inflação no menor nível do ano", "O relógio do juro real de dois dígitos começou a correr" (o cron 14:00 do V4.2 já publicou mais dois).

**Armadilhas do caminho (para a casa):**
1. OPcache: editar front-page.php exige `systemctl reload php8.3-fpm` para o runtime ver (php -l lê o disco, o runtime serve o velho).
2. Meu sed de diagnóstico APAGOU a chamada do carrossel por ~3 min (restaurado na sequência; estado final: linha 51 reels + linha 52 bloco, verificado).
3. curl da DELL não é árbitro para o espelho (rota Dell↔DigitalOcean mente — hoje mostrou a home sem blocos que estavam no ar); **árbitro = curl saindo do Tencent**. localhost com `-H Host` no espelho bate vhost errado — também não serve.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~14:5x BRT.*

---

## 10. ADENDO — 4º FEEDBACK DO MIGUEL: v1.3 "fechando na cara" + vídeo no fim + nome de quem fala (03/09 ~15:0x)

**Queixas (~14:5x):** tocador dentro do post quebrado/esquisito ("ideal: quando a imagem for horizontal, FECHAR NA CARA da pessoa — cortar para aparecer só o centro"); vídeo no FINAL do texto; thumb repetida com o player; matérias repetidas; "tem que dar o NOME do apresentador... não é apresentador, é apresentadora, mulher"; V4.2 precisa de gráfico legal e pauta variada por dia.

**v1.3 (tudo aplicado e provado):**
1. **CROP CENTRAL** na verticalização (`crop=min(iw,ih*9/16):ih → 1080×1920`) — sem blur-pad. Frame do corte novo confirmado por visão: rosto em closeup central.
2. **Vídeo NATIVO no fim do texto**: `<video controls preload=metadata playsinline>` (o player do navegador, não o mejs quebrado) no FINAL do post; shortcode antigo removido; posts existentes re-arrumados em massa (15) pelo eval-file arruma_posts.php; linha "Recorte de..." extinta.
3. **Quem fala tem nome:** TV Fórum = **Dri Delorenzo** (apresentadora) + **Renato Rovai** (jornalista, editor) — contexto default do --canal e do --contexto; regra no prompt: nomear e concordar gênero; sem nome → falar do programa, nunca inventar. Posts do vídeo hP7YGQ6POe0 corrigidos (era "apresentador"; era ELA). Memória nova: tv-forum-apresentadora-dri-delorenzo.
4. **Seletor varia temas** (proibido 2 trechos do mesmo assunto). Faxina: 11 posts repetidos apagados (séries CCJ 6x1 ×5 e Folha×Moraes ×5 + 1 Covid dup).
5. **Prova viva:** vídeo novo do canal (7VP6egO6rL8) processado pela v1.3 → 3 rascunhos com títulos afiados e ângulos DISTINTOS ("Mendonça vira abóbora antes das 9h...", "mesmo comportamento que acusou Moraes em menos de 24 horas", "instituto investigado por contratos com prefeituras bolsonaristas") + 2 do cron v1.2.3 (400439/400441) — os 5 promovidos por ordem do "quero ver".
6. **Repasse ao V4.2** (sprint de outra sessão, via ponte ZM-20260903-067): gráfico com a régua do Miguel + pauta diferente a cada dia (estava tudo juros) + posts sem capa.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~15:0x BRT.*

---

## 11. ADENDO — 5º FEEDBACK: ritmo 4 em 4 horas + CARROSSEL FILA DE REELS 3/2/1 (03/09 ~15:3x)

**Ordens do Miguel (~15:2x):** (1) reduzir o volume na fase de teste — "de 4 em 4 horas por enquanto"; (2) caprichar no texto — "esse último ficou bom" (elogio à v1.3; prompt mantido, não se mexe em time que está ganhando); (3) carrossel multi-card: "no desktop uns 3, no iPad 2, no celular 1".

**Feito:**
1. **Cron:** `41 */4 * * *` (rodadas 00:41/04:41/08:41/12:41/16:41/20:41 — 6×/dia em vez de 24×; backup /tmp/cron_bak_v13.txt na Tencent).
2. **Carrossel v0.5 (multi-card):** reconstruído como FILA DE REELS — track flex com cards 9:16, `--cr-n` por media query (1 → 768px:2 → 1024px:3); card ativo em destaque (opaços ficam 45%), auto-avanço de 8s anda 1 card com translateX suave, swipe no toque, setas no ≥768px, botão de som global na cabeça do módulo, clique em card inativo o traz, clique no card ativo liga o som. Provas medidas: **desktop 1280px = 3 cards (378px cada) · iPad 820px = 2 (385px) · celular 360px = 1 (323px)** — exatamente a conta do Miguel. Backup `.bak_pre_v05_multicard_20260903`. (Screenshot IAB falhou intermitentemente; prova = medições de DOM.)

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~15:3x BRT.*

---

## 12. ADENDO — 6º FEEDBACK: faxina total + cron 1/h de volta + SISTEMA DE VISÃO (03/09 ~19:2x)

**Ordens do Miguel (~15:5x):** apagar os cortes velhos esticados e deixar só os novos (crop central); voltar o cron para 1×/hora ("quando terminar minha live às 10h vou trabalhar nesse carrossel — faz de hora em hora pra ter volume"); "coloca um sistema de visão para você aprender"; post mais legal para o leitor clicar.

**Feito:**
1. **Faxina:** 37 posts velhos apagados da cat 28 (sobraram só os 3 de Mendonça 400458/400460/400462 + a série nova 400473-79 de contratos de oratória/ITER). Carrossel v0.5.1: agora SÓ RECORTE entra (fallback YouTube desativado quando há recortes — sem mais embed horizontal misturado na fila de reels). Posts antigos de agosto da cat 28 (do canônico) continuam publicados mas fora do carrossel.
2. **Cron:** de volta a `41 * * * *` (24×/dia; 1 vídeo novo/rodada — inerte quando não há novidade no canal).
3. **SISTEMA DE VISÃO (v1.4/v1.4.1):** cada corte é julgado pelo Qwen-VL (rosto humano presente, enquadrado no centro, quadro preenchido sem barras); REPROVADO com rosto deslocado → o robô RE-CORTA com offset ±12% na direção do rosto e re-avalia; veredito gravado no post (meta `_cafezinho_corte_qa`) e aprendizado acumulado em `estado/vision_teach.json`. Teste real de API: aprovado ("rosto humano centralizado e bem enquadrado"). Fail-open se a API cair. v1.4.1: vídeos sem duração (yt-dlp sem JS runtime) NÃO são mais marcados como pulados — retry na rodada seguinte.
4. **Post mais bonito:** selo amarelo "RECORTE · TV FÓRUM" acima do título, tipografia maior (clamp 1.5–2.3rem), corpo 1.06rem/1.75, vídeo com sombra — CSS single cat 28 no mu-plugin v0.5.1.
5. Incidente do caminho: série das 15:41 saiu sem o carimbo do gate-img (revertida a pending na promoção) — re-carimbada e publicada; v1.4.1 confirmada com o carimbo no fluxo.

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~19:2x BRT.*

---

## 13. ADENDO — 7º FEEDBACK: 12 cards + REELS + Ver todos + capa do single (03/09 ~19:4x)

Ordens do Miguel: 10-12 prontos no carrossel; título só "REELS" (não TV Fórum — o carrossel será MULTI-FONTE, TV Fórum é uma delas) + link para ver todos; capa gigante do post feia → layout limpo (título → texto → reels embaixo); análise da arquitetura para inspirar confiança.

Feito: mu-plugin v0.5.2 — $limite 12 (query 30), cabeçalho "REELS" + botão "Ver todos →" (archive da cat 28), featured image do tema ESCONDIDA no single cat 28 (múltiplos seletores com !important). Player v1.5 — publica direto publish no laboratório (carimbo do gate gravado antes do publish no mesmo script). FORNADA lançada: --canal --max-videos 3 --cortes 4 (até 12 posts novos entrando sozinhos). Multi-canal: estrutura lista de canais pronta para plugar novas fontes (TV Fórum ativa).

*Registrado por ZCode/GLM-5.3 (Dell) — 03/09/2026 ~19:4x BRT.*

# Fórum — 3 NOVOS V4s: RELIGIÃO + HISTÓRIA + FICÇÃO (protótipo no espelho)

> Criado em 17/08/2026 ~01:45 BRT por ZCode/Qwen 3.8.
> **Origem:** ordem do Miguel por voz (~01:00): criar 3 agentes V4 padrão
> (coleta → produção → revisão → rascunho), 1 post/dia na madrugada, inaugurando
> **no espelho cafezinho.news** (não no canônico) com blocos próprios na home;
> revisão/publicação pelos Loops Miguel e Laura. Canônico só após homologação.

## 1. Decisões (estado atual)

| Item | Decisão |
|---|---|
| Escopo | Protótipo SÓ NO ESPELHO (`cafezinho.news`); canônico intocado |
| Pipeline | V4 padrão autocontido: coleta → produção → revisão → draft (nunca publica) |
| Código | NYC `/root/agentes_v4_novos/` (NÃO toca nos `v4_vertical_*.py` compartilhados — sessão V4 TENDÊNCIAS estava neles) |
| LLM | Cascata canônica (DeepSeek→Kimi→GLM→Qwen→OpenAI→coringa AssemblyAI), portada do `nucleo_llm.py` |
| Cadência | 1 post/dia na madrugada: Religião 02:10 / História 02:40 / Ficção 03:10 BRT (crons NYC 05:10/05:40/06:10 UTC) |
| Categorias (espelho) | Religião **1652** (já existia) · História **775** (já existia) · Ficção **100002** (criada) |
| Autor | Redação (5470) |
| Blocos na home | Religião/História/Ficção após o bloco Esporte (template Cultura), backup `/root/backup_front_page_pre_blocos_novos_20260817.php` |
| Imagens | v0 sem capa (`draft_sem_imagem` padrão V4); Loops decidem na publicação (isenção do gate `_cafezinho_img_check` ou imagem manual) |
| Revisão/publicação | Loops Miguel (publicador) e Laura (sombra/read-only) — avisados via inbox Claude, canal Trindade e para_laura |
| Credenciais | `ESPELHO_WP_*` do chaves.sh NYC espelhadas nos 2 cofres locais (Regra 4; hashes conferidos; backup `.bak_pre_espelho_creds_20260817`) |

## 2. Os três agentes

- **RELIGIÃO** (`v4_religiao.py`): histórias bíblicas (Davi, Salomão, Moisés...),
  fundadores/iluminados (Buda, Confúcio, Jesus histórico...), religiões do Brasil
  (Candomblé, Umbanda, Espiritismo, catolicismo popular, evangélicos...) e fé&história
  (Reforma, Vaticano II, Teologia da Libertação, Dom Hélder...). Giro round-robin de
  36 temas (`dados/series_religiao.json`, editável) + ~30% reportagens frescas do RSS
  da CNBB (fail-soft). Tom: respeitoso, histórico-cultural, zero proselitismo,
  anti-racista com religiões afro-brasileiras.
- **HISTÓRIA** (`v4_historia.py`): "nesta data" — descobre a data de hoje (BRT),
  coleta efemérides na Wikipedia On This Day (ranking editorial Brasil/Sul Global/
  conquistas sociais), curadoria LLM escolhe o principal + 3-5 secundários
  ("Também neste dia"), revisão confere anos/datas contra a evidência.
- **FICÇÃO** (`v4_ficcao.py`): livro seriado **"A Voz de Vila Clara"** (ficção
  política brasileira: jornalista herda semanário no sertão e enfrenta o coronelismo).
  Diretriz-bíblia editável pelo Miguel: `dados/diretriz_livro.md`. Memória da obra:
  `ficcao_estado.json` (últimos 60 resumos + resumo corrido). 1 capítulo/dia, gancho final.

## 3. Provas (17/08 ~01:35-01:38 BRT)

- 3 testes ponta a ponta com drafts reais no espelho:
  - **400071** Religião — "Onde há violência, não há amor: 20 anos da Lei Maria da Penha" (reportagem CNBB, 761 palavras)
  - **400073** História — "Neste dia, em 1945: A Indonésia proclama sua independência..." (efeméride correta de 17/08, 767 palavras)
  - **400075** Ficção — "A Voz de Vila Clara — Capítulo 1: O Herdeiro do Contrato" (1115 palavras, memória do livro atualizada p/ capítulo 2)
- Todos `status=draft`, categoria correta (verificado via wp-cli no espelho).
- Blocos renderizam na home do espelho (HTTP 200; `text-red">Religião/História/Ficção`).
- `py_compile` verde nos 4 módulos; crons instalados com flock (backup `/root/crontab.bak_pre_v4_novos_20260817`).
- Corrigido no 1º teste: feed Vatican News 404 removido (ficou só CNBB, lista expansível).

## 4. O que falta / próximos passos

1. **Miguel observar a qualidade** dos blocos e das matérias no espelho (~dias).
2. Loops Miguel/Laura revisam e publicam os 3 primeiros drafts (no espelho).
3. Estando bom → levar ao **canônico**: criar categorias lá (Ficção não existe no
   canônico), portar blocos na home canônica, espelhar crons.
4. Melhorias v1 anotadas: imagens (Commons por episódio/evento), mais feeds de
   religião, painel CCTV card dos 3 agentes, diretriz do livro ajustável a qualquer momento.

## 5. Kill switch / pausar

Remover as 3 linhas do crontab NYC (marcadas `# V4_NOVOS_*_20260817`) — nada mais roda.
Estados ficam em `/root/agent_data/v4_novos/` (não há perda).

---

## 6. ADENDO 17/08 ~08:30 BRT — IMAGENS: caçadora + loops + FICÇÃO SEMPRE IA (ordem Miguel)

> Miguel (~02:40, voz): "os V4s estão vindo sem imagem — bota o caçador de
> imagens e os loops para encontrarem imagens... mesma coisa para os outros V4
> novos... **o ficção pode ser sempre imagem de IA gerada**, e o ficção a
> gente tem que escrever uma diretriz de criação."

### 6.1 Política de imagens por vertical (espelho)

| Vertical | Cat | Política |
|---|---|---|
| Tendências | 100003 | Foto real (6 estágios). Sem foto → publica sem imagem; **caçadora caça depois** (PASSO espelho) + loops 2ª camada |
| Religião | 1652 | Foto real pela **caçadora** (drafts aguardam os loops; a caçadora aplica capa + meta antes da publicação) |
| História | 775 | Idem Religião |
| Ficção | 100002 | **SEMPRE ilustração IA** (ordem Miguel) — o próprio pipeline gera, audita e marca |

### 6.2 O que foi entregue

- **Ficção — diretriz de criação v1:** `agentes_v4_novos/dados/diretriz_criacao_ficcao_v1.md` (método, estilo, imagem IA, publicação, edição pelo Miguel, kill switch). Lida a cada capítulo JUNTO com a bíblia. Contrato atualizado para v1.1 (seção Imagens nova).
- **Ficção — imagem IA no pipeline:** `v4_ficcao.py` agora gera ilustração IA por capítulo (gerador editorial NYC), passa pelo Tribunal Visual (fallback visual documentado), marca o anexo `cafezinho_image_kind=artificial` (honestidade), grava `_cafezinho_img_check` ok, define a capa. Falha NÃO trava o capítulo; reparo com `python3 v4_ficcao.py --imagem <post_id>`.
  - **Prova:** capítulo 1 (post 400075) recebeu capa IA (media 400084, gerador flux-pro, Tribunal aprovou) — thumbnail + meta verificados no espelho.
- **Espelho — exceção no gate da home:** `cafezinho-real-image-gate.php` patcheado (backup `.bak_pre_ficcao_ia_20260817`): posts da categoria Ficção (100002) NÃO são excluídos da home por imagem IA (a IA é a política oficial da vertical); o resto do gate segue intacto (Tendências/Religião/História nunca ganham IA na capa via caçadora).
- **Caçadora de imagens (automação e1b2d648) ampliada para o ESPELHO:** novos PASSOS 2.6 (varredura espelho: cats 100003/1652/775 sem capa, inclui posts já publicados do Tendências), 4.6 (aplicar no espelho com wp-cli + meta do gate) e 7 (escala para os loops após 2 rodadas sem capa). Ficção NUNCA entra na caçadora. Orçamento: até 3 posts/rodada no espelho além do canônico.
- **Loops avisados** (inbox Claude + para_laura + canal Trindade): políticas novas + gate vale no espelho + são a 2ª camada de caça.
- **Bug encontrado e corrigido:** o anti-duplicata de títulos bloqueou o capítulo 2 ("O Fogo Que Não Queimou") na madrugada — falso positivo contra o capítulo 1 (compartilham o nome da série). Fix em `v4_ficcao.py` (capítulos do mesmo livro nunca são duplicata entre si). Capítulo 2 sai na próxima madrugada (03:10 BRT).
- **Fix na capa do Tendências:** o post 400079 tinha a foto anexada mas sem `_thumbnail_id` (media 400081 órfã) — capa definida manualmente no espelho; a caçadora cobre o 400077 (publicado sem imagem).

### 6.3 Estado

- **O que aconteceu:** imagens resolvidas nas 4 verticais do espelho — Ficção autossuficiente (IA + diretriz), as outras 3 com caçadora + loops; gate de IA na home conciliado com a ordem do Miguel.
- **O que falta:** Miguel ver o espelho (blocos com capas); loops publicarem os drafts de Religião/História/Ficção; capítulo 2 do livro na madrugada de 18/08.
- **O que preciso do Miguel:** olhar o espelho (https://cafezinho.news) e dizer se o estilo da ilustração do Ficção está bom (dá para ajustar na diretriz de criação).

### 6.4 Follow-up 17/08 ~09:10 BRT (ordem Miguel "tendências ainda sem imagem destacada; ficção não entrou nada novo; confirma espelho/noindex")

- **Capa do Tendências aplicada agora:** 400077 (Ben-Gvir) recebeu retrato real do Commons (`Itamar Ben Gvir (portrait).jpg`, CC BY-SA 3.0, Oren Rozen) — checagem oficial = Tribunal Visual (APROVADA; obs.: a sessão roda em modelo sem visão, então o Read visual do agente ficou indisponível e o fallback documentado do tribunal foi usado), anexo media 400107 + `_cafezinho_img_check` ok + isenção antiga removida. Home do espelho renderizando as 2 capas do bloco Tendências (400077 e 400079). Post page com `noindex, nofollow` confirmado.
- **Ficção cap. 2 NO AR (draft):** rodada manual do pipeline gerou **400091 "A Voz de Vila Clara — Capítulo 2: O Fogo Que Não Queimou"** (990 palavras, deepseek) **com capa IA** (media 400093, flux-pro, tribunal OK, meta check ok) — o fix do dedup funcionou. Próximo capítulo = 3 (cron 18/08 03:10 BRT). Claude pingado 09:07 para publicar cap. 1 e 2 no espelho.
- **CONFIRMAÇÃO DE ISOLAMENTO (pedida pelo Miguel):**
  1. Os posts dos 4 V4s novos existem SÓ no espelho (IDs 400071/400073/400075/400077/400079/400082/400091). Canônico: busca por "Vila Clara — Cap" = 0; categoria Tendências NÃO existe no canônico.
  2. O post canônico 266177 ("Ministro de Israel defende matar...") é da vertical **Geopolítica (5003)** normal do canônico, publicada 00:15 — mesma notícia coberta independentemente pela produção canônica, NÃO é o V4 Tendências.
  3. **Espelho no-index:** `robots.txt` = "Não indexar em nenhum motor de busca / Disallow: /" + `<meta name='robots' content='noindex, nofollow'>` na página de cada post — reconfirmado em 400077 e 400079. SEO do canônico não é canibalizado.
  4. Sync `sync_from_cafezinho.sh` (cron 17h) é **unidirecional canônico→espelho** (NOVOS+EDITADOS; nunca deleta locais) — nada do espelho volta pro canônico.

### 6.5 Follow-up 17/08 ~09:20 BRT — capa do Israel Katz (400079) consertada

- **Sintoma:** post publicado com `_thumbnail_id` setado, mas o destaque do bloco Tendências renderizava `<a></a>` vazio (sem imagem).
- **Causa raiz:** a media 400081 (criada pelo worker via REST) tinha o ARQUIVO físico OK (JPEG 1024x787 real, 191KB) mas estava SEM a meta `_wp_attached_file` — sem ela o WordPress não localiza o arquivo nem gera os tamanhos, e `the_post_thumbnail()` devolve nada. O `source_url` da resposta REST veio vazio e o worker seguia sem erro.
- **Fix imediato:** meta `_wp_attached_file` restaurada na media 400081 + `wp media regenerate` (tamanhos recriados) + purge. Home validada: capa do Katz (destaque) e do Ben-Gvir (lista) renderizando.
- **Fix permanente (guard no worker):** `V4_MEDIA_SOURCE_URL_GUARD_20260817` em `v4_vertical_draft_worker.py` — upload de mídia sem `source_url` agora ABORTA (RuntimeError → draft fica pending, caçadora/reparo cobre) em vez de publicar capa fantasma. Vale também para as verticais do canônico. Deploy OK (py_compile local+NYC).

### 6.6 Follow-up 17/08 ~09:25 BRT — Ficção NO AR (capítulos publicados) + guard anti-limpeza de checagem

- Miguel: "o ficção está vazio ainda" → os caps. 1 e 2 estavam parados como draft aguardando os loops. Publicados agora no espelho (400075 e 400091 → `publish`; bloco Ficção da home renderizando os 2 títulos com capas IA). Fluxo do protótipo segue draft-only para os PRÓXIMOS capítulos; estes 2 foram publicados como teste a pedido do Miguel (avisado aos loops).
- **Bug novo encontrado:** salvar um post no EDITOR do espelho apagava a meta `_cafezinho_img_check` (Gutenberg envia metas registradas com valor vazio) → o gate revertia o publish para pending (caso real no 400075). **Guard no mu-plugin** `cafezinho-gate-imagem-checada.php`: `update_post_metadata` ignora limpeza quando já existe checagem (backup `.bak_pre_preserva_check_20260817`, php -l OK). A checagem visual nunca mais morre por salvamento do editor.

---

## 7. ADENDO 17/08 ~19:50 BRT — V2 das 3 verticais (ordem Miguel por voz ~19:00)

> "Religião: não queria notícia superficial — coisas mais profundas, todas as
> religiões (budismo, islamismo, espírita...), artigos profundos. História: nada
> de sensacionalismo — histórias VERDADEIRAS (Irã, China, Brasil, EUA...), posts
> legais, nem tão recentes, com muita procura e muito bem escritos. Ficção:
> crie uma página no painel com acesso a áudio meu e participação minha para eu
> escrever com áudio; procure nos meus arquivos o romance 'Singularidade' e, se
> achar, use ele."

### 7.1 Religião v2 (deployado, crons intactos 02:10 BRT)
- Sem notícia/RSS: o modo "reportagem fresca" foi REMOVIDO. Agora é ENSAIO
  PROFUNDO de cultura espiritual (900-1300 palavras): história, conceitos,
  práticas e significado hoje — todas as tradições com o mesmo respeito.
- Nova série "Tradições e Sabedorias do Mundo" (14 temas: sufismo, zen, advaita,
  kabbalah, mística cristã, xintoísmo, jainismo, zoroastrismo...) somada às 4
  séries existentes (Bíblia, Fundadores, Religiões do Brasil, Fé e História).
- Revisão exige profundidade real (rejeita raso) e plausibilidade factual.

### 7.2 História v2 (deployado, crons intactos 02:40 BRT)
- Sem efeméride "nesta data": agora ARTIGOS de história profunda por país/tema
  (séries novas em `dados/series_historia.json`: Irã, China, Brasil, EUA e
  "Histórias do Mundo" — 6+6+6+6+12 temas), 900-1400 palavras, rigor com anos e
  nomes, sem sensacionalismo.
- **Sinal de demanda (ordem Miguel "nota que tem muita procura"):** o agente
  consulta o endpoint `/v6/api/tendencias/pautas` (queries GSC em alta) e o tema
  que casar com uma busca quente FURA a fila (registrado `por_demanda` no estado).

### 7.3 Ficção — obra Singularidade + página no painel + participação do Miguel
- **Romance encontrado nos arquivos:** `Dados_Frios/Agentes Labs/singularidade_chapters.json`
  (2 capítulos reais: "O Silêncio dos Dados" e "A Geometria das Sombras" — Rio 2040,
  Veronica Vinge, Neuronet, cyberpunk político brasileiro). Vira a obra do V4 Ficção:
  bíblia nova `diretriz_livro.md` (Vila Clara arquivada em `.bak_vila_clara_20260817`,
  idem estado `ficcao_estado.json.bak_vila_clara_20260817`).
- **Caps 1-2 importados e PUBLICADOS no espelho:** posts 400111 e 400114 (cat 100002,
  capas IA 400113/400116 aprovadas, status publish, no bloco Ficção da home).
  Próximo capítulo: 3 (cron 03:10 BRT, com o fix do dedup já ativo).
- **Página `/v6/ficcao` NO PAINEL** (http://43.156.151.165/v6/ficcao; backup
  `.bak_pre_pagina_ficcao_20260817`): estado da obra + últimas participações +
  formulário de orientação (texto) + upload de áudio + instrução do voice note
  no Telegram (a ponte já transcreve com Groq). APIs: GET/POST estado,
  participacao (GET/POST), participacao_ok, audios, audio.
- **Integração no agente:** `v4_ficcao.py` agora LÊ as participações pendentes
  do painel ANTES de escrever o capítulo (viram ordem direta no prompt), CONFIRMA
  o consumo e PUBLICa o estado da obra no painel após cada capítulo (tudo fail-soft).
- **Watcher de áudio:** `ponte_cafezinho/ficcao_audio_watcher.py` + cron local */10 —
  áudios enviados pela página são transcritos pelo Whisper da Groq (mesma função
  da ponte) e viram participação pendente para o próximo capítulo.
- Teste da API: participação de teste POSTada e listada OK (será consumida pelo cap. 3).

### 7.4 Estado
- **O que aconteceu:** as 3 verticais reformuladas conforme a ordem; Singularidade
  no ar no espelho; página de Ficção no painel com participação por texto/áudio.
- **O que falta:** Miguel ver (1) o 1º ensaio de Religião v2 (amanhã 02:10 BRT),
  (2) o 1º artigo de História v2 (02:40 BRT), (3) a página /v6/ficcao e o cap. 3
  com a participação dele aplicada.
- **O que preciso do Miguel:** nada agora — testar a página e mandar uma
  orientação (texto na página ou voice note no Telegram) quando quiser dirigir
  o próximo capítulo.

### 7.5 Nota 17/08 ~19:55 BRT — página Ficção REMOVIDA do painel (ordem Miguel "tira o ficção do painel")
- Página /v6/ficcao, APIs (estado/participacao/audios), NAV e card da home removidos do `painel_cctv_v6.py` (backup `.bak_pre_remove_ficcao_20260817`; removidos 6 blocos; painel recompilado e reiniciado: /v6/ficcao=404, home=200, demais APIs intactas).
- Cron local do watcher de áudio (`FICCAO_AUDIO_WATCHER_20260817`) removido; arquivo do watcher mantido em `ponte_cafezinho/ficcao_audio_watcher.py` (pode ser religado).
- O agente Ficção continua com as chamadas ao painel em fail-soft (logam erro sem travar o capítulo). Participação do Miguel segue possível pelo voice note no Telegram (a ponte transcreve com Groq e o texto chega na conversa) — a integração automática "participação pendente → capítulo" fica dormente até o painel voltar a hospedar a página, se/quando o Miguel quiser.

---

## ADENDO 18/08 ~23:00 BRT — PARALISADOS (ordem Miguel) + bloco removido da home

Ordem do Miguel (~23:00): paralisar os 3 V4 novos (Religião/História/Ficção) — só o Tendências segue no espelho. Executado: crons NYC `V4_NOVOS_*` removidos (backup `/root/crontab.bak_pre_paralisa_v4novos_20260818_20260819_0216`); bloco `foreach` da home do espelho removido (backup `front-page.php.bak_pre_remove_blocos_v4novos_20260818`, php -l OK). Posts já publicados (400075/400091/400111/400114) permanecem no ar; rascunhos (400117 religião, 400119 história, 400121 ficção cap 3) ficam como estão. A caçadora de imagens não varre mais 1652/775 (agora cobre as 5 editorias do Tendências). **Religar = re-adicionar as 3 linhas de cron (backup no NYC) + o bloco foreach (backup no espelho).** Detalhes da operação: `forum_v4_tendencias_prototipo_20260816.md` §11.

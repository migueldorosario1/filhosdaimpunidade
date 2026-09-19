# Memória técnica — Editorial Mendonça × PF (08/09/2026, ZCode Dell / Qwen3.8-Max)

Log técnico da missão manual do Miguel (editorial sobre o afastamento de Andrei Rodrigues e Leandro Almada por André Mendonça). Decisões e estado: `Foruns/forum_editorial_mendonca_andrei_20260908.md`.

## Linha do tempo (BRT)

- ~14h3x — ordem (voz): editorial com pesquisa web das últimas notícias + transcrição UOL + exclusiva Serrano (título/abertura, 2 trechos) + ~800 palavras, crítico a Mendonça.
- ~14h4x-15h1x — pesquisa: WebFetch timeout ×2 em Google News → troca para python3/urllib via Bash (timeout 15-20s): Google News RSS (`when:1d`/`when:4h`) para frescor + **Bing News RSS para URLs diretas** (links do Google News RSS são redirects `news.google.com/rss/articles/...`; no Bing a URL real vem no parâmetro `url=` do `apiclick.aspx`, URL-decoded).
- ~14h5x — adendo: comentário Christian Lynch colado pelo Miguel; ordem de apresentar Serrano, Maierovitch e Lynch.
- ~15h0x — monitor: linha inserida; Edit falhou 1× ("file modified since read" — outra sessão Qwen escreveu às ~14h50) → re-Read e re-Edit (§112 confirmado na prática).
- ~15h1x — varrida final (ordem "antes de publicar"): 19 matérias salvas; WP REST search achou a exclusiva do Cafezinho (post 269245).
- ~15h2x — adendo Miguel: G1 "Diretores da PF apoiam Andrei e entregam cargos" (nota íntegra + 11 signatários) → incorporado.
- ~15h3x — editorial v1 (988 palavras).
- ~15h4x — adendo Miguel: matéria BBC (Almada × caso Marielle × Cláudio Castro; 75d×9d) colada + **NATIVA**: Mendonça incendeia o país para eleger Flávio Bolsonaro (extrema-direita pesca em águas turvas; sentimento de caos).
- ~15h5x — BBC salva (sindicações confirmadas via Bing: Correio Braziliense 04h32 GMT, Estado de Minas 07h57 GMT, + Poder360/O Globo Miriam Leitão/Metrópoles/DCM); editorial v2 FINAL com a nativa no título e espinha (1.359 palavras c/ título+URL; primeira tentativa deu 1.424 → enxugada).

## Método de extração de matérias

Fetch com UA de navegador + gzip; strip de `<script>/<style>`; captura de `<p>` com ≥45 chars; título/data no cabeçalho de cada .txt (`FONTE:`/`TITULO:`). VEJA tem paywall — só o lead bastou (Murad interino + "ataque").

## Arquivos

- `pesquisa_20260908/`: g1_sadi_nota_11_diretores · g1_argumentos_mendonca · infomoney_5_recados · agencia_brasil_segunda_turma · valor_gilmar_plenario · veja_quem_assume_pf · terra_agu_driblar_fachin · oglobo_malu_messias_estrategia · oglobo_fachin_recebe_messias · oglobo_ala_mendonca_gilmar_tempo · metropoles · brasil247 (×2) · r7 · dcm · icl (Andrei prendeu Vorcaro/INSS) · +5 · bbc_almada_marielle_castro (colada pelo Miguel, com sidebar: carta dos 13 ex-ministros) · `_indice_fetch.json` · `cafezinho_busca_minas_vorcaro.json`
- `PESQUISA_noticias_mendonca_andrei_20260908.md` — digest 9 seções (fato · 2ª Turma/plenário · governo/AGU · reação PF · historial Andrei×Vorcaro · falas UOL · juristas · varrida final · BBC/nativa)
- `EDITORIAL_mendonca_afasta_andrei_20260908.md` — v2 final, 1.359 palavras c/ título+URL, texto limpo (sem markdown — regra de post do Cafezinho)

## Fatos-chave verificados (anti-fabricação)

- Orwell/1984 e "leviana e abjeta"×"matriz religiosa comum": conferidos no g1_argumentos_mendonca antes de usar; citação "autodefesa" foi REMOVIDA do rascunho por não ter fonte.
- Segunda Turma = 5 dos 10 (Valor); 3-0 virtual, Kassio+Fux anteciparam após vista de Gilmar (G1 Sadi); liminar segue valendo; Gilmar pedirá plenário a Fachin (Valor).
- 75 dias (diligência Castro) × 9 dias (Jaques Wagner): relatório de inteligência citado por Moraes, via BBC — atribuído ao relatório no texto.
- 11 signatários da nota dos diretores (lista completa no g1_sadi); NÃO assinam: Andrei, Almada, corregedora Aletea Kunde, Murad.
- Carta dos 13 aposentados: só o headline da BBC ("mais aguda crise", "imediata e rigorosa apuração") + G1 (Barroso recusa, Lewandowski não assinaria) — usado em 1 frase, sem detalhes não verificados.

## Armadilhas (para próximas)

1. WebFetch instável em agregadores → ir direto para urllib/Bash com timeout curto.
2. Google News RSS não dá URL final; Bing News RSS dá (parâmetro `url=` do apiclick).
3. Monitor de trabalho muda durante a tarefa (sessões concorrentes) — re-ler imediatamente antes de cada escrita (§112).
4. Editorial "de ~800 palavras" cresce com adendos obrigatórios — contar (wc -w) e avisar o Miguel no final, oferecendo corte.
5. Horários das notícias em GMT nos feeds (BRT = GMT−3).

## v3 — reescrita de estilo (08/09 16:0x→16:2x)

- Gatilho: ordem do Miguel (msg 6, voz) — Orwell fora, travessão/dois-pontos reduzidos a zero na prática, "leu o manual de estilo e refaz o texto", frasezinhas de anúncio fora, trecho Josias×Moraes fora, bloco editorial ditado dentro (fraqueza/despero/medo + sucessor continua + Andrei respeitado volta mais forte + STF minoria bolsonarista + imagem arranhada + 2º tiro no pé + briga com a ordem institucional + "Ele está querendo incendiar o país").
- Causa-raiz do v2 ruim: redigi SEM ler `Cerebro/Estilo/MANUAL_DE_ESCRITA.md` (v2.1.1, oficial desde 02/09) nem o UNIFICADO. 🔴 LIÇÃO: manual é leitura obrigatória PRÉ-redação; verificação do apêndice é obrigatória PRÉ-entrega.
- Método v3: leitura integral dos 2 manuais → Write completo do arquivo (não patch) → verificador python (regex do apêndice do manual + extras: >2 frases/parágrafo, >300 chars/parágrafo, título ≤80) → Edit cirúrgicos (1 início "E" na linha do Maierovitch + 7 splits de parágrafo longo) → conversão aspas retas→curvas (28 pares, paridade verificada).
- Resultado verificação final: palavras 1.476 (arquivo c/ título+linha-fina+URL) · travessão 0 · meia-risca 0 · dois-pontos corpo 0 · ponto e vírgula 0 · inícios proibidos 0 · ligação preguiçosa 0 · metalinguagem 0 · spoiler emoção 0 · dupla negativa 0 · Orwell/1984 0 · parágrafos >2 frases 0 · >300 chars 3 (citações/URL, justificados) · título 54 chars.
- Repetições deliberadas (martelo, manual §4): "incendiar/incêndio" (título, nativa §13, bloco ditado, fecho "urna de 2026") e "pesca em águas turvas" ×2 (nativa + fecho) — pontos de máxima pressão, intencionais.
- Título/linha-fina: nativa como título + Serrano na linha-fina (regras de título do manual: ≤80 chars, uma ideia, sem travessão — o título composto do v2 violava). SINALIZADO para veto do Miguel.
- Arquivos tocados: editorial (v3), UNIFICADO (EMU-11 Apêndice I), NODE_ESTILO (linha EMU-11), forum_manual_estilo_unificado (adendo 08/09), fórum+memória do editorial (esta seção), ATUALIZACOES (linha 16:2x), MONITORAMENTO (linha atualizada ➕ v3).
- Pendente: "ok" do Miguel → sweep final de internet (msg 3) → publicação WP (rascunho via wp-cli, sem markdown, capa a definir).

## v3.1 — correções de repetição e precedentes (08/09 16:4x→16:5x)

- Gatilho: msg 7 do Miguel — (a) nativa "pesca em águas turvas" repetida abertura×fecho ("repetiu à toa"; manual §4 só admite repetição intencional); (b) "transformada em bancada" = rima interna + semântica vazia + eco do termo usado pelo Lynch → "transformada em bunker de oposição ao governo" (sugestão literal dele); (c) precedentes: "Neles" ambíguo, presidente anônimo → nomear Jair Bolsonaro e seguir a lógica ditada: cita os precedentes para fazer algo ainda pior (presidente protegia a família × ministro protege a si mesmo).
- Método: 3 Edits nas ordens diretas + scanner novo (trigramas 3+ palavras repetidos em todo o texto + raízes 6+ letras em frases consecutivas, com allowlist de nomes/tema) → o scanner achou 7 ecos que a regex padrão não pegava → 6 Edits + 1 Edit (Polícia Federal→PF na nativa). Resultado: trigramas repetidos restantes = só citação literal do Serrano (intocável), nomes de instituição (PUC-SP/TJSP, AGU/advogado-geral, PF/diretor-geral) e âncoras factuais distantes (caso Marielle, mensagens de Vorcaro, Jair Bolsonaro ×2 distantes).
- 🔴 LIÇÃO: a regex do apêndice NÃO caça repetição de sentido/som/construção à distância — reler em voz alta + scanner de trigramas antes de entregar. Gravada como EMU-12 no MANUAL_DE_ESTILO_UNIFICADO (Apêndice I) + linha no NODE_ESTILO + update no forum_manual_estilo_unificado.
- Martelos intencionais preservados: incêndio/incendiar (motivo da nativa, 4 pontos de pressão), "proteger" ×2 no paralelo ditado, anadiploses Fachin/Andrei.
- Arquivos tocados: editorial (9 Edits), UNIFICADO (EMU-12), NODE_ESTILO (linha), forum_editorial (esta revisão), memória (esta seção), forum_manual (update), ATUALIZACOES (linha), monitor (➕ v3.1).
- Pendente: "ok" do Miguel → sweep final → WP.

## Publicação — rascunho WP (08/09 17:0x→17:4x)

- Sweep final: Google News RSS `when:1d` (urllib + UA navegador) → 10 registros novos → seção 10 do digest `PESQUISA_noticias_mendonca_andrei_20260908.md` com a decisão "corpo MANTIDO".
- Foto: search_image ×2 → 6 candidatas baixadas (z-cdn.chatglm.cn) + 1 plaquinha CNI (`fotos/cand7_nameplate.jpg`) para PROVA DE IDENTIDADE visual (mesmo rosto das cand 1/2/3/5/6; cand4 de óculos = outro ministro, descartada). Capa = cand1 Estadão; PIL LANCZOS 5200×3468 → 2400×1600 q88 (401 KB); nome lowercase `andre-mendonca-stf.jpg` ANTES do import (WP grava filename minúsculo; lição da memória youtube-painel).
- HTML: python gera 50 `<p>` do arquivo v3.1 (`html.escape(quote=False)`; título da exclusiva vira `<a href>` e a URL crua entre parênteses sai). Permalink conferido: `/2026/09/06/slug/` = 200, `/2026-09-06/slug/` = 404 (curl com UA de navegador).
- Publicação: `scp` foto+html → `ssh cafezinho-wp 'bash -s' <<'REMOTE'` (heredoc quotado protege acentos/aspas curvas): `wp post create /tmp/editorial_mendonca_content.html --post_title=… --post_status=draft --post_author=2018 --post_category=22,21141,5088 --tags_input=… --post_excerpt=… --porcelain` → **269495**; `wp media import /tmp/andre-mendonca-stf.jpg --post_id=269495 --featured_image --title='André Mendonça' --alt=… --caption='Foto: Estadão' --porcelain` → **269496**.
- Forense de autor: `wp user list` + `wp post get 269245 --field=post_author` → James2017 = ID 2018 (display "Miguel do Rosário"); ID 17 = subscriber (armadilha do "James 17" falado). Categorias por slug: politica-2=22, nacional=21141, eleicoes-2026=5088.
- Verificação: post get (ID/status/autor/título/data) + post_excerpt + term list category (5088/21141/22) + term list post_tag (9) + meta _thumbnail_id (269496) + guid do anexo.
- Armadilhas novas: (1) `wp post create` aceita arquivo posicional como conteúdo; (2) `--post_category` pede IDs, não slugs; (3) `media import --featured_image` exige `--post_id`; (4) plaquinha com nome é a prova de identidade mais barata que existe em busca de imagem; (5) permalink WP é /AAAA/MM/DD/slug/ — formato com traços 404.
- Arquivos tocados: editorial (0 edits — URL já correta), fotos/ (7 arquivos), digest (seção 10), forum_editorial (seção de publicação), memória (esta seção), ATUALIZACOES (linha), monitor (➕ publicação).
- Pendente: ok do Miguel → `wp post update 269495 --post_status=publish` (ou pela CL na esteira).

## Kakay: núcleo no editorial + artigo próprio pendente (08/09 17:5x→18:0x)

- Fonte bruta salva verbatim: `kakay_declaracao_20260908.md` na pasta do editorial (título dele em caps + 9 parágrafos + assinatura).
- v3.2 (9 parágrafos) → scanner: parágrafo K3 com 303 chars (split preparado), ecos consecutivos "documento" (K5→K6), "credibilidade" (K8→K9), "corporação" (K8×fecho linha 97) e trigramas âncora já aceitos; trigramas "o amigo de nikolas" ×2 = título da exclusiva + slug da URL no MESMO parágrafo (falso positivo).
- v3.3 por ordem do Miguel ("texto muito grande, entra só a parte mais forte"): bloco final = 2 parágrafos (274 + 133 chars, 1 frase cada): (1) qualificação (Antônio Carlos de Almeida Castro, o Kakay, um dos criminalistas mais conhecidos do país) + observação de Bruno Salles sobre o documento apócrifo/sem timbre/sem autoria/sem data; (2) martelo do contraditório (prova imprestável × decisão com base nela) + ausência de pedido contra Almada. Zero ecos com os vizinhos (scanner de raízes 6+ limpo no bloco).
- Atualização do rascunho: regen HTML (52 <p>) → scp → `wp post update 269495 /tmp/editorial_mendonca_content.html` → verificação (draft, autor 2018, 52 parágrafos, "Kakay" ×2, ~1.500 palavras no wc -w do conteúdo HTML).
- Link entregue ao Miguel: https://www.ocafezinho.com/wp-admin/post.php?post=269495&action=edit
- LIÇÃO: declaração de jurista enviada inteira não entra inteira em editorial — o núcleo jurídico novo (o que nenhum outro citado disse) é o que fica; o resto vira artigo próprio. Ordem dele confirma.
- PENDENTE (aguarda "vai"): post novo só com o texto do Kakay + foto jornalística dele (mesmo rigor de identificação da plaquinha CNI usado para Mendonça).

## Gilmar: PDF público + fecho com citação (08/09 18:0x→18:1x)

- Extração do PDF: `pdftotext -layout` (poppler disponível no Dell); 2 páginas; pedido de vista do referendo PET 16.662 assinado digitalmente em 08/09/2026. Print do amigo (WhatsApp jpeg 1042×582) = terceira razão + fecho do documento, confirmando o trecho a citar.
- Upload: `wp media import /tmp/pet-16662-pedido-de-vista-gilmar-mendes.pdf --post_id=269495 --title=... --porcelain` → anexo 269499; guid público confirmado com curl 200 (UA de navegador). Filename lowercase antes do import (regra da casa).
- Gerador HTML ganhou segunda conversão de link: "para download (URL)" → `para <a href="URL">download</a>` (a primeira conversão segue sendo o título da exclusiva).
- Fecho novo: parágrafo de atribuição (243 chars, 1 frase, link da íntegra) + citação verbatim da terceira razão (447 chars, 1 frase, isenta da régua de 300 como toda citação) como ÚLTIMO parágrafo do post. Martelo da urna mantido como bloco anterior. Scanner de raízes 6+: zero ecos com o martelo vizinho.
- Verificação pós-update: 54 <p>, draft, autor 2018, "ADPF 1.017" ×1, tail do conteúdo = a citação de Gilmar.
- Armadilha nova: PDF de ministro é fonte primária — citar verbatim do pdftotext (preserva pontuação original) e nunca parafrasear número de artigo (282 §2º CPP / 230-B RISTF) sem conferência no texto extraído.

## Artigo só-Kakay: rascunho 269516 (08/09 18:2x→18:3x)

- "Vai" do Miguel: "pode publicar, como rascunho, o texto do kakay".
- Corpo gerado do arquivo-fonte `kakay_declaracao_20260908.md`: parser pula cabeçalho/separador/título caps; 10 parágrafos verbatim; conversão de aspas retas→curvas com paridade (duplas e simples); html.escape(quote=False).
- wp post create /tmp/kakay_content.html --post_status=draft --post_author=2018 --post_category=22,21141,5088 --tags_input=8 tags --post_excerpt=1ª frase verbatim --porcelain → 269516; media import k1 --post_id --featured_image --caption='Foto: Portal Lupa1' → 269517.
- Foto: search_image ×2 (10 resultados); baixadas 4 em `fotos_kakay/`; Read visual das 4: k1/k2/k3 = mesmo homem (barba branca, cabelo cacheado, óculos amarelos = marca do Kakay) em 3 veículos independentes; k4 (Valor, beca, sem barba/óculos) = OUTRO homem, descartada. Capa k1 = cerco de imprensa (microfones CNN Brasil/R7/Globo), 1200×720 sem resize (já leve).
- Verificação: post get (draft/2018/título 106 chars), term list category ×3 e post_tag ×8, meta _thumbnail_id 269517, 10 <p>, tail = "<p>Kakay</p>".
- Decisão editorial registrada: título de artigo assinado pelo autor fica verbatim mesmo acima de 80 chars (a régua EMU-2/9 vale para títulos nossos); exceção consciente, não precedente para a esteira.
- Pendente: ordem de publish dos DOIS rascunhos (269495 e 269516).

---

## ADENDO TÉCNICO 08/09 ~22:4x (ZCode/Qwen 3.8) — desdobramento Fachin 72h publicado (post 269536)

- Gatilho: ordem Miguel ~22:0x "publica essa... pesquisa, contextualiza, melhora, encontra foto jornalistica legal do mendonça com bolsonaro" + URL Fórum (fachin-andre-mendonca-explicar, 21:28 BRT).
- Forense WP prévia: 269495 status publish post_date 19:17:31 autor 2018 (Miguel via wp-admin; rev 269513 20:46; título novo) ⇒ "essa" = matéria nova do fato noturno. 269516 draft (título revisto por ele 21:20:50).
- Fontes: Fórum (urllib; WebFetch timeout 60s) + O Globo datePublished 20:59:47-03:00 + G1 + CartaCapital 18:23 BRT + Bing RSS (R7/UOL/Correio/CartaCapital/Gazeta/Exame/Veja/Poder360/Brasil247). Fatos novos vs editorial: despacho de Fachin assinado terça NOITE (72h p/ Mendonça se manifestar; autos retornam à Presidência); contradição AGU (plenário indicado × Turma submetida); "decisões concorrentes sobre o mesmo objeto"; prazo 5 dias úteis de Fachin (semana anterior) incluía Moraes/Gonet/Andrei; Andrei afastado com prazo correndo; Corregedoria PF + suspensão de relatórios de inteligência sobre Judiciário/advocacia pública/polícia judiciária.
- Texto: /tmp/fachin72h_texto.txt → html c/ 2 âncoras; verifica_estilo.py v2 0 infrações pós-2 correções (eco "sobre" frases vizinhas; metrônomo 18/21/21 → regra = 3 frases consecutivas ≥8 palavras com max-min ≤3).
- WP: post create draft (autor 2018, cats 22,21141,5088, 9 tags, excerpt) → media import foto --featured_image (269537) → post update --post_status=publish. ERRO aparente: "Metadado bloqueado: post protegido por decisão editorial humana" (canal meta_wp_cli user_id=0) DEPOIS do commit do status ⇒ post ficou publish + protegido; verificado post get (publish 22:39:54) + página pública 200 c/ capa/citação/links. Bypass p/ humano no wp-cli: env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 (plugin cafezinho-protecao-editorial.php, contexto_agente()).
- Foto capa: c1 = abraço Bolsonaro×Mendonça Planalto jul/2021 (1200×720, 16:9) via search_image MCP (source Carta Capital); cross-source c2 Correio Braziliense (mesma cena, faixa presidencial) + c5 Estadão (mesma sala, aperto de mãos); prova visual = óculos sem aro + têmporas grisalhas batem com retratos confirmados (Estadão/Gazeta da 1ª busca); c3 Congresso em Foco DESCARTADA (rosto oculto, calvície). Crédito caption "Foto: Presidência da República"; alt descritivo. Arquivo minúsculo bolsonaro-mendonca-abraco-planalto-2021.jpg; SEM upscale (nativo 1200×720).
- Artefatos locais: pasta da missão + MATERIA_fachin72h_publicada_20260908.md/.html + fotos/bolsonaro-mendonca-abraco-planalto-2021_capa269537.jpg.
- Estado: 269495 publish (Miguel 19:17) · 269536 publish (ZM 22:39:54, permalink /2026/09/08/fachin-da-72-horas-...) · 269516 draft aguarda Miguel.

# Memória técnica — Matéria M6: Operação Transparência × Cezinha (14/09/2026)

Par do fórum `Foruns/forum_cezinha_operacao_transparencia_20260914.md` (os fatos e fontes estão lá). Aqui fica o como-fazer.

## Receita de publicação REST replicada (família Master)

1. Creds: `Outros/chaves/agentes_labs/chaves.sh` → WP_SITE (controle.ocafezinho.com, o canônico) + WP_USER/WP_PASS.
2. **Byline da família Master: autor 1257 (Tadeu Porto) + categoria 1434 (Tadeu Porto)** — conferido no post 270768 do mesmo dia; metas `_agente_origem=zcode`, `_agente_versao=GLM-5.3`, `_publicado_por=zcode-glm53` (regra viva §136).
3. Fluxo: POST /media (bytes + Content-Disposition; depois PATCH com title/caption/alt/description) → POST /posts status=draft (title, slug explícito, content só com <p>, author, categories, featured_media, meta) → POST /posts/{id} status=publish. Tudo 201/200 sem gate rebaixando (post publish com featured_media + caption não é tocado).
4. **Permalink canônico tem DATA: /2026/09/14/<slug>/** — testar slug seco dá 404 falso-positive. Prova pública completa: URL com data (200) + grep título/capa/arquivo-da-capa/crédito-na-legenda/corpo/byline + home (cf-cache DYNAMIC aqui; se um teste disser 404, checar URL e cache antes de concluir).
5. Push: título ≤50 chars sem dois-pontos/travessão já atende (46: "PF busca deputado que levou Vorcaro a Mendonça").

## Foto quando Commons e Flickr falham

- `upload_imagem_wp.buscar_wikimedia_com_metadados("Cezinha de Madureira")` = NADA; Flickr Agência Câmara search não renderiza por curl (JS). **Foto oficial da Câmara funciona: `https://www.camara.leg.br/internet/deputado/bandep/<id_deputado>.jpg`** (id no biografia camara.leg.br — Cezinha = 204504; 354×472). Uso jornalístico corrente com crédito "Câmara dos Deputados" (ConJur e Congresso em Foco usaram fotos Câmara nesta mesma cobertura de 14/09). Registrada em fotos/CREDITOS.md §M6.
- Montagem Cezinha × Mendonça (Rosinei Coutinho/STF do acervo) via PIL, altura comum 620, faixa branca 6px — padrão da casa.

## Lições de apuração

- UOL notícias = 403 Akamai para curl E WebFetch/webReader; a matéria saiu inteira por **ConJur + Congresso em Foco + g1 + BBC** (os quatro textos cruzados fecham todos os fatos).
- Congresso em Foco deu as travas de fact-check prontas: "não há informação oficial de que a apreensão do dinheiro com Valéria ou o encontro entre Vorcaro e Mendonça sejam o objeto específico dos mandados" + PF isentando o Judiciário. Ambas entraram na matéria.
- O cruzamento com a leva Dino: Cezinha NÃO aparece no IPe da PET 16.669 (grep vazio no acervo); o elo é o **material do celular de Vorcaro** (custódia transferida à PF justamente na decisão de 13/09) + o timing (Zanin/23h/cópias a ministros; Plenário terça 15/09). A matéria costura sem afirmar vínculo formal entre os inquéritos.

## Artefatos

- Post: 270826 · mídia capa: 270825 · rascunho fonte: `Reportagens/Master/MATERIA_M6_cezinha_operacao_transparencia_20260914.html` · capa: `fotos/cezinha_mendonca_montagem_M6.jpg` (+ elemento `cezinha_bandep_camara.jpg`).
- Provas: publish 200 · público 200 com título/capa/crédito/corpo/byline True · home 200 com o slug True (DYNAMIC).

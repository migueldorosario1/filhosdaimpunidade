# Memória técnica — Aliança Fênix Filmes × O Cafezinho (Palestina)

**Data:** 25/08/2026 · **Agente:** ZCode/GPT

## Fontes consultadas

- Cérebro canônico: `00_CEREBRO_CANONICO.md`, monitoramento, fóruns/memórias GSN de Priscila Miranda.
- Instagram público:
  - `https://www.instagram.com/fenix.filmes/`
  - `https://www.instagram.com/ocafezinhooficial/`
  - Reel colaborativo `https://www.instagram.com/reel/DcMkXxOMHDx/`
  - Post comparativo `https://www.instagram.com/fenix.filmes/p/DcPNFTliY5i/`
- Google indexando conteúdos públicos do Instagram.
- REST do Cafezinho para taxonomia:
  - Cinema id 78/count 113;
  - Cultura id 79/count 390;
  - Palestina inexistente.
- Materiais locais do trailer em `Outros/Negocios Priscila/filme palestina/` e `Outros/projeto pri/`.

## Identidade confirmada

- `@fenix.filmes`: Fênix Filmes – Produção e Distribuição; 6.636 seguidores.
- `@ocafezinhooficial`: Portal Cafezinho; 25,8 mil seguidores.
- Priscila Miranda: diretora da Fênix Filmes e colunista registrada no Global South News.
- “F Filmes” não apareceu como marca distinta; usar Fênix Filmes.

## Post identificado

Shortcode `DcMkXxOMHDx`, Reel 0:55, publicado em colaboração nativa Fênix + Cafezinho seis dias antes da leitura. Legenda começa com “Esta é a minha terra” e apresenta *Tudo que Resta de Você, Palestina*, de Cherien Dabis, como retrato de família, deslocamento, perda e memória. Métricas públicas observadas: 1,4 mil curtidas e 93 comentários.

Comparação: post estático colaborativo seguinte `DcPNFTliY5i`, sobre soberania narrativa e distribuição, tinha 7 curtidas e 1 comentário. A colaboração não é condição suficiente; o motor foi vídeo emocional + Palestina + cena concreta + audiência cruzada.

## Leitura dos comentários

Amostra pública revelou:

- emoção/luto;
- solidariedade política;
- intenção explícita de ir ao cinema;
- dúvidas sobre salas e disponibilidade;
- alguns comentários violentos, generalizantes ou antissemitas, que exigem moderação.

A demanda editorial mais clara é serviço de lançamento: onde/quando assistir.

## Decisões recomendadas

- Não criar categoria Palestina.
- Usar Cinema (78) e Cultura (79).
- Criar hub/caderno `Cinema & Resistência — Fênix × Cafezinho`.
- Piloto de 60 dias antes de formalizar vertical permanente.
- Próxima suíte: guia vivo de lançamento + novo Reel colaborativo emocional.
- Transparência editorial/comercial obrigatória.

## Arquivos criados

- `Cerebro/Foruns/forum_alianca_fenix_cafezinho_palestina_20260825.md`
- `Cerebro/Memorias/memoria_alianca_fenix_cafezinho_palestina_20260825.md`

## O que aconteceu / o que falta / o que preciso do Miguel

**O que aconteceu:** pesquisa e planejamento concluídos sem publicar nem alterar redes sociais.

**O que falta:** Insights internos do Reel e calendário oficial da Fênix.

**O que preciso do Miguel:** obter com Priscila prints/CSV dos Insights (plays, alcance, retenção, compartilhamentos, salvamentos, seguidores ganhos) e datas/salas; decidir o nome do hub.

## Teste Graph API — 27/08 ~10:50

- Chaves IG/FB localizadas no cofre unificado (nomes: FB_PAGE_ACCESS_TOKEN len 226, FB_PAGE_ID, IG_USER_ID, INSTAGRAM_MAKE_WEBHOOK, CREATOMATE_TEMPLATE_ID_FACEBOOK/INSTAGRAM; espelhos com md5 idênticos). Valores nunca exibidos.
- `GET /me` → página "O Cafezinho" (421927677830371). `GET /{IG_USER_ID}` → `ocafezinhooficial` (17841400848520269), 25.976 seguidores, 3.728 mídias.
- `GET /{IG_USER_ID}/media` janela 15–26/08 → 23 mídias; Reel `DcMkXxOMHDx` AUSENTE (pertence à conta da Fênix; coautoria não exposta ao token do Cafezinho). GET direto pelo ID convertido do shortcode → GraphMethodException code 100 subcode 33 (sem permissão).
- Consequência: respondedor de comentários do Cafezinho funciona nas mídias PRÓPRIAS; para o Reel atual da Fênix, só com token da Fênix. Estratégia: Reel novo da Suíte 1 publicado pelo Cafezinho (Fênix como colaboradora convidada) → respondedor automático opera nele.

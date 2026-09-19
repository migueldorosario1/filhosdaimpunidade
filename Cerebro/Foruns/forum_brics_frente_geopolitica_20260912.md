# 🌐 FÓRUM — FRENTE BRICS × GEOPOLÍTICA (automação 2/2h, 6 rascunhos no Cafezinho)

> **Ordem do Miguel (12/09/2026 ~15:0x, chat ZCode):** "vamos abrir uma frente de artigos sobre o brics, crie uma tarefa agendada de 2 em 2 horas para fazer uma boa materia no cafezinho, em rascunho, sobre os brics. comece pelas mais atualizadas. consiga as melhores fotos, as mais emblemáticas. xi com modi e putin e presidente do irã, por exemplo, de preferencia para fotos de perto entre lideranças. a linha das matérias pode ser sobre o discurso dos lideres, entrevistas, coletivas, e contraponto com algum coletiva ou entrevista recente de trump ou algum de seus secretárias, sempre ameaçando, intimidando, humilhando, paises do sul global. a linha do cafezinho é sempre defesa do sul global. Não esqueça de linkar sempre as categorias certas." + adendo: "bote em categoria geopolítica, e faça uns 6 artigos".

## 1. Briefing canônico da frente

- **Recorrência:** automação ZCode a cada 2h, **6 execuções no total** (recurring=false, maxRuns=6). 1 execução = 1 matéria.
- **Saída:** RASCUNHO (draft) no WordPress do Cafezinho. **NUNCA publicar** — o Miguel revisa e publica manualmente (receita de publicação manual está no fórum `forum_mendonca_pf_20260908`, Adendo 2).
- **Categoria OBRIGATÓRIA:** **Geopolítica (ID 5003)** + **Brics (ID 5053)** como secundária. Tags livres por pauta (BRICS, Sul Global, dedolarização, país/tema).
- **Autor do rascunho:** 5486 (conta automática). NÃO passar para 2018 nem para publish.
- **Linha editorial:** defesa intransigente do **Sul Global**. Eixo de cada matéria:
  1. **Pauta quente:** a notícia MAIS RECENTE (24-72h) sobre BRICS — discurso de líder (Xi Jinping, Narendra Modi, Vladimir Putin, Lula, Masoud Pezeshkian/Irã, Cyril Ramaphosa...), entrevista, coletiva, cúpula, bilateral, NBD, dedolarização, expansão do bloco.
  2. **Contraponto:** coletiva/entrevista/post RECENTE de **Trump ou secretários** (Rubio, Bessent, Lutnick, Navarro, Leavitt) ameaçando/intimidando/humilhando países do Sul Global (tarifas "100% contra o BRICS", sanções, deportações, etc.).
  3. **Fecho:** soberania, cooperação Sul-Sul, multilateralismo.
- **Ordem das pautas:** SEMPRE a mais recente primeiro; cada execução cobre uma pauta NOVA (conferir a tabela §2 antes de escolher).
- **Fotos (obrigatória, emblemática):** preferência a fotos DE PERTO entre lideranças (Xi+Modi, Xi+Putin, Lula+Xi, Putin+Pezeshkian, foto de família da cúpula). Fontes seguras: Flickr Agência Senado (CC BY 2.0), kremlin.ru, flickr oficiais de governos, Wikimedia Commons CC, PIB India. **Verificar licença — nunca all-rights-reserved.** Crédito SÓ no campo legenda da mídia (`--caption` no media import) + alt text. **Proibido "Foto: ..." no corpo** (ordem Miguel 11/09).
- **Estilo:** manual unificado em `Cerebro/Estilo/` (versão 8K). Proibições vivas: travessão à toa; clichê distópico (Orwell/1984); repetição à toa; metáfora sem referente no lead; frase defensiva ("não se trata de perseguição"); "exclusivo"/"com exclusividade"; scaffolding de LLM no corpo. Lead = a revelação primeiro. **Título curto e forte, ideal ≤ 60 caracteres** (o push herda o título e corta; notificação enviada não se recupera). ~700-1.100 palavras, HTML limpo.
- **Fatos:** verificar antes de escrever; citações só com grep positivo na fonte; nunca inventar repórteres/bylines (sem byline = crédito ao coletivo).
- **Anti-duplicata:** antes de criar, checar a tabela §2 abaixo + `wp post list --post_status=draft,publish --s="<termo>"` no cafezinho-wp.
- **Acesso WP:** `ssh cafezinho-wp "cd /var/www/ocafezinho && wp ... --allow-root"` (receita canônica; rascunho c/ capa: `wp post create --post_status=draft --post_author=5486 --post_category="5003 5053"` c/ arquivo posicional + `wp media import <arq> --post_id=<ID> --featured_image --caption="Crédito" --alt="..."`).
- **Aviso ao Miguel (fora de casa, só vê Telegram):** ao fim de cada execução, `python3 "/home/migueldorosario/Downloads/Antigravity Google/ponte_cafezinho/ponte_cafezinho.py" --send "🟢 BRICS <N>/6: ..."` — texto limpo, SEM asteriscos/# (fallback DoH+SNI se DNS falhar).
- **Monitor/memória:** cada execução atualiza a linha da frente no MONITORAMENTO_DE_TRABALHO.md, grava memória técnica em `Cerebro/Memorias/memoria_brics_<tema>_<data>.md` e linha em CEREBRO_NODE_ATUALIZACOES.md.

## 2. Progresso da série (0/6) — ATUALIZAR A CADA EXECUÇÃO

| # | Data/hora | Pauta (ângulo) | ID rascunho | Título | Foto (fonte/licença) | Fontes principais | Estado |
|---|-----------|----------------|-------------|--------|----------------------|-------------------|--------|
| 1 | 12/09 16:0x→16:3x, RETIFICADO ~17:1x | Cúpula de Nova Déli (12-13/09): Declaração contra tarifas/sanções unilaterais + "máxima prudência" na guerra do Oriente Médio (Xi, Putin, Pezeshkian, Modi) × projeto dos EUA com tarifa até 100% sobre Índia/China (Senado 07/08, Câmara vota semana que vem) + Trump "BRICS morto" (fev/2025, NÃO recente — ver retificação no §4) | **270342** | Sob ameaça de Trump, BRICS condena tarifas unilaterais | Líderes chegam juntos ao Fórum de Negócios da 18ª cúpula (Pezeshkian+Modi+Putin+Ramaphosa) — PIB/Gabinete do PM da Índia, GODL-India, via Wikimedia (anexo 270343) | O Globo, InfoMoney, O Povo, Gazetaweb, Brasil 247, TASS, Outlook India, Reuters, CNBC, CNN, The Statesman, Hindustan Times | ✅ entregue e retificado (draft autor 5486, cats 5003+5053, 11 tags, 1.074 palavras, 0 travessão/0 dois-pontos) |
| 2 | 12/09 18:0x→18:4x | A "passeata da unidade" da cúpula (Modi de mãos dadas c/ Pezeshkian + Putin e Ramaphosa ao lado) + discursos: 3 metas de Modi (10 barreiras/100 startups/mil parcerias), "BRICS não é contra ninguém"/"formador de regras", deboche de Putin ao G7 ("por que é chamado de grande, eu não entendo"; 30 mil sanções; 40%×29% PIB) + bilaterais Modi-Putin (US$ 100 bi até 2030, Thirukkural) e Modi-Pezeshkian (Chabahar) × Rubio ameaçando sanções secundárias pós-encontro Modi-Pezeshkian (02-03/09) + projeto Graham na Câmara semana que vem + 3 navios c/ indianos atingidos HOJE no Golfo de Omã (173 retidos) | **270358** | Modi, Putin e presidente do Irã de mãos dadas desafiam Trump | Modi e Putin apertam as mãos na bilateral da cúpula 2026 — PIB/Gabinete do PM da Índia, GODL-India, via Wikimedia (anexo 270359) | Infomoney/Broadcast, DD India, Outlook India, Kyiv Post, Valor, Free Press Journal, O Globo, NDTV+8 (Rubio), news18+MSN (navios) | ✅ entregue (draft autor 5486, cats 5003+5053, 12 tags, 1.017 palavras, 25/25 aspas validadas, 0 travessão/0 dois-pontos) |
| 3 | — | — | — | — | — | — | ⬜ pendente |
| 4 | — | — | — | — | — | — | ⬜ pendente |
| 5 | — | — | — | — | — | — | ⬜ pendente |
| 6 | — | — | — | — | — | — | ⬜ pendente |

## 3. Pautas-candidatas (reserva — só usar se faltar notícia fresca; sempre preferir o furo do dia)

1. Cúpula dos BRICS mais recente: declaração conjunta × reação tarifária de Trump.
2. Xi × Modi (degelo sino-indiano) × ameaças tarifárias dos EUA à Índia (petróleo russo).
3. Putin × Pezeshkian (Irã no BRICS) × sanções/ameaças americanas a Teerã.
4. Lula e o NBD/Dilma Rousseff: financiamento Sul-Sul × "não precisamos de moeda comum?" e a resposta de Washington.
5. Dedolarização: comércio em moedas locais × tuíte/ameaça "100% de tarifa" de Trump.
6. Ramaphosa/África do Sul × humilhações de Trump (tarifas, "genocídio branco"), África no BRICS.
7. Expansão do bloco (novos membros/parceiros) × isolamento crescente dos EUA.
8. Brasil presidindo/agenda BRICS 2025-2026 × boicotes americanos.

## 4. Estado da missão (sempre terminar atualizando este bloco)

- **O que aconteceu:** frente criada 12/09 ~15:0x (automação ZCode 2/2h, 6 disparos; categorias Geopolítica 5003 + Brics 5053 confirmadas no WP). **Execução 1/6 entregue 12/09 ~16:3x** — rascunho 270342 «Sob ameaça de Trump, BRICS condena tarifas unilaterais» (cúpula de Nova Déli 12/09; capa PIB India GODL; memória tecnica em Memorias/memoria_brics_cupula_nova_deli_20260912.md). Aprendizado registrado: `--post_category` exige IDs separados por VÍRGULA (`5003,5053`), espaço dá erro "No such post category". **RETIFICAÇÃO ~17:1x (pegadinha apontada pelo Miguel):** a 1ª versão dizia que Trump declarou o BRICS "morto" em 08/09/2026 — FALSO: a frase é de 14/02/2025 (Fortune, Times of India, ThePrint) e foi RECICLADA por um agregador indiano (oneindia, página de vídeo) na semana da cúpula; nenhuma fonte primária/independente confirma fala nova. Corrigido no post: o contraponto fresco agora é o projeto de sanções do Senado (07/08/2026, 86×11, tarifa até 100% sobre Índia/China por petróleo russo; Câmara vota na semana de 14/09 — Reuters 11/09) + a fala de fev/2025 devidamente datada. **Regra nova da frente: agregadores de vídeo indianos (oneindia etc.) reciclam aspas antigas com data nova — toda fala bombástica exige fonte primária OU duas independentes datadas na semana.**
**Execução 2/6 entregue 12/09 ~18:4x (GLM-5.3)** — rascunho 270358 «Modi, Putin e presidente do Irã de mãos dadas desafiam Trump» (passeata da unidade + metas de Modi + deboche de Putin × Rubio/sanções secundárias; capa bilateral Modi-Putin PIB GODL anexo 270359; 25/25 aspas validadas; memória em Memorias/memoria_brics_passeata_unidade_20260912.md). Cuidado novo: fato datado conferido 2× — marinheiros indianos mortos por ataque dos EUA foram em JUNHO/2026 (não esta semana); os de HOJE foram 3 navios atingidos SEM feridos + 173 retidos.
- **O que falta:** 4 execuções (próxima às 20:00 BRT 12/09). Ângulos frescos já no radar p/ as próximas: dia 2 da cúpula (13/09, agenda energia/saúde/IA + foto de família), Xi-Modi bilateral de sábado (degelo), China como mediador da guerra, Irã×Emirados no BRICS, reação oficial dos EUA à declaração, Ramaphosa/África do Sul, posição do Brasil (Mauro Vieira) na cúpula.
- **O que preciso de você (Miguel):** revisar e publicar 270342 e 270358 quando puder (a cúpula é este fim de semana — quanto antes publicar, mais furo); ao fim das 6, dizer se quer renovar a série (nova rodada de 6) ou encerrar.

## 5. Vigília CM (Claude Miguel) — aberta 12/09/2026 ~19:2x BRT

**Ordem Miguel 12/09 ~19:1x chat CLI:** vigília da publicação da série BRICS + 24h após último publish; monitora e reporta; NÃO publica, NÃO edita publicado, NÃO muda autor.

**Pré-checagem dos 2 drafts entregues (19:2x BRT, cross com WP-CLI):**

| ID | Título | Chars | Cats | Capa | Travessão | `Foto:` no corpo | Status pré-publish |
|---|---|---|---|---|---|---|---|
| 270342 | Sob ameaça de Trump, BRICS condena tarifas unilaterais | **56 ✅** | 5053+5003 ✅ | 270343 ✅ | 0 ✅ | 0 ✅ | **OK, publish autorizado** |
| 270358 | Modi, Putin e presidente do Irã de mãos dadas desafiam Trump | 63 | 5053+5003 ✅ | 270359 ✅ | 0 ✅ | 0 ✅ | **OK — título é bom, 3 chars a mais NÃO é problema** (retificado 19:3x — Miguel: "não vai prejudicar um bom título por causa de 3 caracteres"; a régua ≤60 é ideal, não gate) |

**RETIFICAÇÃO 19:35 BRT** — a sugestão anterior de encurtar 270358 pra "Pezeshkian" era **erro meu**. Miguel corrigiu no chat CLI 19:2x: *«não vai prejudicar um bom título por causa de 3 caracteres»*. O título atual é MELHOR — dizer "presidente do Irã" faz o leitor médio brasileiro reconhecer imediatamente quem é (o nome Pezeshkian ainda é pouco conhecido). **Sem alerta, sem sugestão de troca. Título 270358 está bom como está.** Regra nova em memória permanente: régua ≤60 chars é IDEAL, não gate. Só alerto se título for factualmente errado, estilisticamente violador (travessão etc.) ou notoriamente ruim — não por 3-5 chars.

**Estado inicial da vigília minha:**
- 2/6 drafts entregues, 0/6 publicados
- Próxima automação BRICS: 20:00 BRT (mesma hora meu slot Master 270324)
- Vou pré-checar cada novo draft assim que aparecer + verificar cada publish quando o Miguel liberar

— Claude Miguel (CM · `claude-opus-4-7`) · 12/09/2026 19:22 BRT

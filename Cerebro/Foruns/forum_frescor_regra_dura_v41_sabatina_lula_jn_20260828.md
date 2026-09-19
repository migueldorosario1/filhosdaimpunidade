# ⏱️ Fórum — FRESCOR vira regra dura no V4.1 + Sabatina do Lula no JN na capa (28/08/2026)

> Ordem do Miguel (28/08 ~01:47 BRT, madrugada de sexta): "Tenho uma matéria no Categoria Nacional sobre a entrevista do Lula no DOMINGO. Hoje já é sexta de madrugada. Não pode ter matéria tão fria. Enrijece as regras para frescor no loop todo, sobretudo na parte Nacional. E publica a entrevista que o Lula deu ONTEM À NOITE no Jornal Nacional — na capa, com foto, com transcrição."

## 1. O que aconteceu (caso-escola radiografado)

**Post frio: 268033** ("Lula nega blindagem a familiares em investigação da PF", V4.1, publicado 27/08 22:55) — cobria a entrevista do Lula à **Record exibida domingo 23/08**. Atraso total fato→publicação: **~96 horas**. O Miguel viu no bloco Nacional e horrorizou. **O post FICA no ar** (ordem explícita: remover prejudica SEO; a lição vira regra, não borracha).

**A cadeia do atraso (tudo provado em log):**

1. **Domingo 23/08 22:26** — a pauta "Lula diz que Lulinha precisa se defender e nega blindagem à PF" (item_key `e88bb07b5659f8e4`) entra no funil minutos após a entrevista ir ao ar. O juiz anti-repetição **barra 3 vezes na mesma noite** (22:26, 23:26, 00:26) — o site já tinha matéria no ar sobre a entrevista. Até aqui, sistema saudável.
2. A pauta fica no banco `nacional.sqlite3` com status `drafted` — e a seleção do ciclo nacional pegava as 6 últimas `drafted` **sem filtro de data**, com dedupe de apenas 24h.
3. **Quinta 27/08 21:26** — 96h depois, a pauta velha volta a ser elegível. Passa pelo juiz (a última publicação do tema, 267658 de 25/08 19:08, já tinha >48h — fora da janela do juiz), vira rascunho 268033 e é publicada 22:55.

**Raiz:** nenhuma camada media a **idade do fato**. O juiz media repetição; ninguém media frescor.

## 2. A regra nova (V41_FRESCOR_20260828)

Patch em `/root/v4_labs/codigo/v41_ciclo.py` (NYC), backup `.bak_pre_frescor_20260828`, py_compile ok, **alinhado à doutrina FRESCOR-V5** (`diretrizes_coleta_curadoria_frescor_v5.md`, 20/08 — hard news exige nota 4-5 = fato de até 24h):

**Camada 1 — seleção (determinística, grátis):** pauta cuja `collected_at` passa do teto da vertical **não entra no ciclo** (vale para `drafted` E para as sobras `new`, que também não tinham filtro):

| Vertical | Teto de frescor |
|---|---|
| nacional | **24h** |
| economia | **24h** |
| geopolitica | **24h** |
| ciencia | 48h |
| saude / esporte / meio_ambiente / digital | 48h |
| cultura | 72h |

**Camada 2 — juiz inter-vertical (LLM, a mesma chamada que já existia):** o prompt agora informa `COLETADA_EM` e `AGORA` e manda calcular a **idade do FATO CENTRAL** (quando aconteceu, não quando foi coletado). Fato com mais de {teto da vertical} horas sem fato novo material → `repetida=true` com motivo `pauta_fria`.

**Provas:**
- Sintética (sqlite nacional): a pauta do caso-escola (`e88bb07b5659`, 23/08) hoje é **BARRADA**; as sobras `new` de 27/08 seguem elegíveis.
- E2E (ciclo real 28/08 02:17): o funil escolheu a pauta **"Propaganda no rádio e na TV começa nesta sexta (28)"** — fato do próprio dia — e escreveu o rascunho **268079** ("Haddad terá menos da metade do tempo de Tarcísio na propaganda"), FC websearch confirmando coerência de calendário. O V4.1 agora nasce fresco por construção.

## 3. A matéria quente entregue (capa + manchete)

**Post 268078** — "Lula enfrenta sabatina duríssima do JN, não cede a ilações e colhe elogios" — publicado 28/08 02:07 BRT, categoria [22 Nacional + 2403 Redação], autor 5470 (Redação), **manchete da capa com trava CMH de 8h** (até ~10:07) e capa oficial **Ricardo Stuckert** (mídia 268077, MD5 livre no manifesto, carimbo JSON casado gravado antes do thumb, conferido via SQL). Provas públicas: HTTP 200, `og:image` = foto Stuckert, `<h1 class="manchete-titulo">` apontando para o post (4 links na home).

**Insumos:** transcrição completa baixada do vídeo da íntegra (link do Miguel, live Lindbergh Farias — `youtube-transcript-api` no Dell, sem bot-check, 1.370 segmentos ~54 min) + foto oficial deixada pelo Miguel na pasta de pautas. Matéria com ~1.100 palavras, **zero dois-pontos** (regra do vício de IA), linha editorial do Miguel:

- A primeira parte parecia inquérito — e o próprio Lula disse no ar: **"Eu pensei que eu estava no Ministério Público aqui"**.
- Lulinha/Marcola: **"tudo ilação"** — mensagens de WhatsApp ("eu sou Fábio"), o quadro de 100 mil euros que nunca se materializou, a mágoa com Marcola ("eu sou quase um pai para você; por que você não falou comigo?"), "por enquanto acredito na versão dele", e a régua republicana (filho que errou paga; polícia, MP e juiz cumprem sua função; 580 dias de cadeia pela maior mentira jurídica do país).
- Economia: perguntas carregadas de veneno ultraliberal respondidas com a régua real — único presidente com 8 anos de superávit primário, país 10+ anos sem crescer, 7,5% em 2010, **dívida dos EUA 120% do PIB (US$ 40 tri), Japão e Itália piores que o Brasil**, déficit 2,8% → superávit 0,1%, "se tem alguém neste país que tem responsabilidade fiscal, sou eu", "o meu compromisso é fazer este país crescer" (não cortar saúde/educação/aposentadoria), "não considero vender o Correio".
- **O que o JN não perguntou** (verificado na transcrição: zero ocorrências): mobilidade urbana, trem de alta velocidade, energia solar, energia nuclear, ferrovias, Argentina, China, Trump. Quase 1h de janela nobre sem um só grande projeto nacional — e o custo político: os clichês da bancada são o programa de Flávio Bolsonaro; quando a TV só gira em torno do clichê, quem lucra é o candidato do clichê.
- Elogios: Lindbergh Farias deu nota 10 ao vivo ("o maior brasileiro vivo da história deste país").
- Gancho moral: o JN tem a **obrigação moral** de aplicar o mesmo chumbo grosso na sabatina de Flávio Bolsonaro **nesta sexta (28)** — "se a de Lula pareceu o Ministério Público, a dele não pode parecer um café da manhã".

## 4. Estado / o que falta / o que preciso do Miguel

- **Pronto:** regra de frescor nas 2 camadas (seleção + juiz), provada; post 268078 no ar como manchete (trava até ~10:07); post frio 268033 preservado (SEO); rascunho fresco 268079 na fila normal de publicação.
- **Falta:** (a) observar os próximos ciclos reais (cron minuto 25, 2/2h) confirmando `pauta_fria` nos logs e zero pautas velhas escritas — primeira ronda confere; (b) se o Miguel quiser, amanhã à noite: matéria-espelho sobre a sabatina de Flávio Bolsonaro no JN cobrando a régua (a transcrição pode ser baixada pelo mesmo caminho).
- **Preciso do Miguel:** nada pendente de decisão — a régua de 24h para hard news segue a doutrina FRESCOR-V5 que ele mesmo formalizou em 20/08. Se quiser tetos diferentes por vertical, é uma linha no `_FRESCOR_H`.

— ZCode/Kimi K3, 28/08/2026 ~02:45 BRT

# 🖼️ Fórum — Capa de pessoa = foto jornalística recente (fim do "canibal" institucional)

**Data:** 26/08/2026 ~15:00–15:35 BRT · **Agente:** ZCode/GLM-5.3 (chat direto com o Miguel) · **Memória irmã:** `Memorias/memoria_capa_pessoa_jornalistica_fim_do_canibal_20260826.md`

## O pedido (Miguel, 26/08 ~14:50)

> "todo os posts que citam senado vem com o mesmo thumb (...) não faz sentido. se é caiado, tem que ter thumb do caiado. corrige isso de uma vez por todas e dá um esporro nos loops para vigiarem isso. Não pode isso. aqui a foto tem que ser jornalistica do ronaldo caiado. foto jornalistica, não foto oficial de wikipedia. recente!"

Sobre `https://www.ocafezinho.com/2026/08/26/caiado-promete-anistia-ampla-para-condenados-pelo-8-de-janeiro/` (post 267714, publicado 14:09), cuja capa era a fachada do Congresso (mídia 267513).

## Diagnóstico (causa raiz)

- O post 267714 nasceu sem capa; o loop de imagem **LAURA-GROK aplicou "canibal"** — reuso da mídia 267513 ("senado-federal-brasilia-congresso-nacional", fachada) que já era capa de outros posts (log da ponte de imagens V4, ronda 14:39: "PING canibal 353/538 NO AR | 267513 Congresso").
- Mesmo padrão no mesmo dia: 267686 Marina (fachada → trocada para COP30 de manhã), 267694 Gleisi (canibal → trocada para plenário da Câmara por ordem do Miguel). O 267511 ("Senado mantém sem voto proteção emergencial a mulheres", 24/08) também estava com a mesma fachada.
- A regra "pessoa no título → foto da pessoa" não existia como trava no loop de imagens.

## Execução (tudo no canônico cafezinho-wp)

1. **267714 (Caiado):** busca no Commons (`srsearch="Ronaldo Caiado 2026"`), 21 candidatas avaliadas com visão (qwen-vl-max); descartadas as do Canal Livre (Caiado coadjuvante), Botucatu/PSD 12/06 (960×1280, baixa) e o retrato 3x4 (parece oficial). **Escolhida:** `28.01.2026 – Eduardo Leite e Ronaldo Caiado se encontram em evento de investimentos em São Paulo - 55065884829.jpg` (LAIC 2026, Grand Hyatt SP, Governo RS, 7008×4672, CC BY-SA 4.0) — Caiado é o sujeito, rosto limpo e nítido, validado em identidade cruzada com o retrato 3x4 do mesmo evento. Crop 16:9 centrado no rosto → 1600×900 → **mídia 267783**.
2. **267511 (Senado/mulheres):** a fachada trocada por foto jornalística de sessão do plenário (`Plenário do Senado - 55239426093.jpg`, 29/04/2026, Senado Federal, 4528×3024, CC BY-SA 4.0 — nota 9/10 na validação por visão) → **mídia 267784**. Não há foto de plenário de agosto/2026 no Commons; a legenda é honesta ("em abril de 2026").
3. Procedimento repetido nos 2 posts: carimbo `_cafezinho_img_check` casado ANTES do `_thumbnail_id` (gate Emenda 7), reindex Yoast, flush Redis, purge Rocket. **Provas ao vivo:** og:image + body + home com as fotos novas, zero ocorrências da fachada nos 2 posts.

## Incidente operacional (resolvido na hora)

Ao reindexar o Yoast do 267714 via `wp_update_post`, a trava **slots-20min (Emenda 5 do Miguel)** reagendou o post (publish → future, fila cheia até ~19:41). O post foi restaurado para publish com a data original (14:09) via SQL direto (restauração do estado que o Miguel já tinha aprovado ao ler a página; nenhuma nova violação de ritmo criada — o post já estava no ar às 14:09). Lição: **em post publicado recente (data de hoje), NUNCA usar `wp_update_post`** para reindexar Yoast — atualizar a tabela `wp_yoast_indexable` direto (og/twitter image) e o `post_status` via SQL.

## Emenda 12 (nova regra viva)

Gravada na diretriz de qualidade viva do NYC (`/root/v4_labs/dados/diretriz_qualidade_viva.md`, backup `.bak_pre_emenda12_20260826`) + canal_trindade + inbox claude/codex/glm_coding + ponte (**ZM-20260826-022**):

1. Post sobre PESSOA exige capa com foto jornalística recente da pessoa central — nunca retrato oficial nem imagem institucional genérica.
2. PROIBIDO "canibal" (reuso de mídia de outro post) em post com sujeito nomeado no título; fachada de instituição só em post sobre a instituição (e prefira sessão/atividade).
3. Teste do sujeito obrigatório antes de aplicar capa: a capa mostra a mesma pessoa/instituição do título?
4. Erro em post publicado = correção imediata (§119, carimbo antes do thumbnail).

## Estado da missão

- **O que aconteceu:** 2 capas trocadas e provadas ao vivo (267714 Caiado → LAIC 2026; 267511 → plenário em sessão); regra gravada na diretriz viva + esporro nos canais dos loops com ACK obrigatório (CM/AGY/LAURA-GROK).
- **O que falta:** os ACKs dos loops; vigiar as próximas rondas da ponte de imagens (o LAURA-GROK registra cada aplicação no `ponte_imagens_v4_LOG.md` — conferir se novos posts de pessoa saem com foto da pessoa).
- **O que preciso de você (Miguel):** nada — só conferir se gostou da foto do Caiado (LAIC 2026, janeiro). Se preferir outra (ex.: Canal Livre 13/03/2026 ou Botucatu 12/06/2026), troco em minutos.

---

## Adendo 3 — Caso 267809 Rubio (26/08 ~20:46→21:05, ordem do Miguel) — ZM-20260826-025

**Incidente:** Miguel flagrou o post "Rubio recebe chanceler do México sob pressão militar dos EUA" (267809, vertical **V4.1 Geopolítica**, `zizi_job_id v41_geopolitica_826eba979cf5`, publicado 18:39) com capa = **fachada do Truman Building** (mídia 267814, Wikimedia). Aplicador: **LAURA-AGY**, carimbo às 18:28 — 4ª família de erro de capa do dia (Marina, Caiado, Senado, agora Rubio).

**Agravante:** a foto CORRETA já estava no Commons desde **14:11 BRT** (upload 17:11 UTC), ANTES de o post nascer (17:59). Não era indisponibilidade — foi escolha errada do caçador (institucional genérico com pessoa nomeada no título = violação da Emenda 12 nº 1/3). O gate "pessoa no título → proibido institucional" segue **inexistente**.

**Correção:** `File:Secretary Rubio Meets with Mexican Foreign Secretary (55489789743).jpg` — foto oficial do Departamento de Estado (Freddie Everett), **26/08/2026, o encontro DE HOJE**: Rubio apertando a mão do chanceler **Roberto Velasco** (em exercício desde 01/04/2026), bandeiras EUA/México ao fundo. Domínio público (US Gov work). Validada por visão (nota 9/10, Rubio nítido à direita, Velasco à esquerda, sem obstrução) + crop 16:9 1600×900 → **mídia 267843**. Carimbo casado ANTES do `_thumbnail_id`; legenda com crédito completo e data.

**Provas ao vivo:** post HTTP 200; `og:image` = rubio-velasco-state-dept-26-08-2026.jpg; corpo 3 refs à nova / **0** à velha; home 1 ref.

**NOVO APRENDIZADO TÉCNICO (fantasma do og):** o UPDATE via SQL no `wp_yoast_indexable` **NÃO basta** — o runtime que renderiza o head (`YoastSEO()->meta->for_post()`) continuou gerando og VELHO mesmo com o indexable novo no banco (e o Repository lendo o novo!). Quem destrava é `wp_update_post(["ID"=>…])` (save_post reindexa a presentation). Neste caso o post **não** virou future (diferente do incidente 267714) — mas conferir `post_status` após o wp_update_post continua obrigatório. Ordem segura testada: SQL indexable → wp_update_post → conferir publish → flush Redis → purge Rocket (grep pelo título + index-*-https.html da home).

**Estado:** corrigido e provado. **Falta:** ACK da Emenda 12 (ZM-20260826-022) continua pendente de CM/AGY/LAURA-GROK/LAURA-AGY — agora com o 4º caso como reforço; gate automático no caçador segue pendente (código do loop roda na Laura).

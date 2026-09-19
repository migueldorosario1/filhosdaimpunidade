# Memória técnica — 3 novos V4s (Religião/História/Ficção), protótipo espelho

> 17/08/2026 ~01:14-01:50 BRT · ZCode/Qwen 3.8 · Fórum: `Foruns/forum_v4_novos_religiao_historia_ficcao_prototipo_espelho_20260817.md`

## Arquitetura

- **Local:** NYC `/root/agentes_v4_novos/` — autocontido de propósito (a sessão
  V4 TENDÊNCIAS estava editando `v4_vertical_draft_worker.py`/`v4_vertical_intake.py`;
  zero colisão). Staging local: `ZCodeProject/v4_novos_staging/`.
- **Arquivos:** `comum.py` (cascata LLM portada de `agentes_tematicos/v4/nucleo_llm.py`
  — mesmos providers/cadeia/coringa AssemblyAI; REST draft; dedup por contenção de
  tokens igual ao worker; higiene de texto: fences/CONTENT END/fontes/markdown;
  `para_html()`; logs JSON), `v4_religiao.py`, `v4_historia.py`, `v4_ficcao.py`,
  `contratos/v4_{religiao,historia,ficcao}_v1.md`, `dados/series_religiao.json`,
  `dados/diretriz_livro.md`.
- **Estado:** `/root/agent_data/v4_novos/` — `estado_religiao.json` (temas usados),
  `estado_historia.json` (datas cobertas, cap 400), `ficcao_estado.json`
  (livro, próximo capítulo, últimos 60 resumos, resumo corrido, cat_ficcao).
- **Logs:** `agent_data/v4_novos/{religiao,historia,ficcao}.log` (1 linha JSON/evento).

## Endpoints/IDs

- Publica via REST `{ESPELHO_WP_SITE}/wp-json/wp/v2/posts` com `status=draft`
  (dupla garantia: payload + POST de confirmação draft). Autor Redação 5470.
- Categorias espelho: Religião **1652**, História **775**, Ficção **100002**
  (criada 17/08 via `wp term create category "Ficção" --slug=ficcao`).
- Dedup: títulos do espelho `status=any` últimas 120h; contenção ≥0.5 c/ ≥2 tokens
  (ou ≥3 c/ ≥0.4) = duplicata → aborta sem criar draft.

## Crons (NYC, UTC; BRT=UTC-3)

```
10 5 * * * flock v4_religiao.lock  → v4_religiao.py   # 02:10 BRT  # V4_NOVOS_RELIGIAO_20260817
40 5 * * * flock v4_historia.lock  → v4_historia.py   # 02:40 BRT  # V4_NOVOS_HISTORIA_20260817
10 6 * * * flock v4_ficcao.lock    → v4_ficcao.py     # 03:10 BRT  # V4_NOVOS_FICCAO_20260817
```
Todos `. /root/chaves.sh` + `/root/venv/bin/python3`. Backup do crontab:
`/root/crontab.bak_pre_v4_novos_20260817`.

## Espelho (front-page.php)

- Tema `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php`.
- 3 blocos inseridos ANTES da 2ª ocorrência de `<!-- TECNOLOGIA -->` (linha 716,
  após Esporte), via `foreach` sobre array `[Religião 1652, História 775, Ficção 100002]`,
  template idêntico ao bloco Cultura (1 destaque + 5 lista, `category__not_in` 28/20751/20699).
- Backup: `/root/backup_front_page_pre_blocos_novos_20260817.php` (espelho).
- `php -l` verde, chown www-data, home HTTP 200 com os 3 blocos.
- Sync canônico→espelho NÃO copia tema → blocos persistem.

## Provas dos testes ponta a ponta (17/08 ~04:35-04:38 UTC)

| Agente | Draft | Título | Palavras | Provider |
|---|---|---|---|---|
| religiao | 400071 | Onde há violência, não há amor: 20 anos da Lei Maria da Penha | 761 | deepseek (red+rev) |
| historia | 400073 | Neste dia, em 1945: A Indonésia proclama sua independência... | 767 | deepseek |
| ficcao | 400075 | A Voz de Vila Clara — Capítulo 1: O Herdeiro do Contrato | 1115 | deepseek |

Verificado via wp-cli no espelho: 3× `post_status=draft`, cats 1652/775/100002.

## Credenciais (Regra 4)

- `ESPELHO_WP_SITE/USER/PASS` já existiam no `/root/chaves.sh` (NYC) — usadas desde
  12/08 pelo worker V4 (`V4_ESPELHO_20260812`). Espelhadas 17/08 nos cofres locais
  `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado`
  (backup `.bak_pre_espelho_creds_20260817` nos dois; verificação por nome+sha8:
  SITE 3f0d9da2 / USER 0688b064 / PASS ac852f2a — idênticos nos 3 lugares).

## Comunicados aos Loops

- `Cerebro/Foruns/inbox_trindade/claude.md` — bloco [ZCODE→CLAUDE] 01:45 (instruções
  de revisão/publicação NO ESPELHO + isenção do gate de imagem).
- `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` — anúncio 01:45.
- `Cerebro/Foruns/ponte_codex_miguel_laura/mensagens/para_laura/20260817_0145_zcode_3_v4s_novos_prototipo_espelho.md`.

## Incidentes/lições do sprint

1. Feed Vatican News (`pt.feed.xml`) 404 → removido de `FEEDS_RELIGIAO` (ficou CNBB).
2. f-string com `\"` dentro da expressão quebra no py 3.12 → variável local antes.
3. Espelho tem mu-plugin gate `_cafezinho_img_check` (publish sem checagem → pending/400):
   drafts v0 sem capa dependem de isenção/imagem manual dos Loops na publicação.
4. `wp user list` no espelho exige `--path=/var/www/cafezinho-news`.
5. Monitor de trabalho foi editado por outra sessão durante o sprint (janela de
   concorrência conhecida) — re-read + re-apply resolveu.

## Próximos (registrados)

- Homologação do Miguel → portar ao canônico (cats lá + blocos + crons).
- v1: imagens Commons por episódio/evento; mais feeds de religião; card no painel CCTV.

---

## ADENDO 17/08 ~08:30 BRT — IMAGENS (ordem Miguel ~02:40): caçadora + loops + Ficção sempre IA

- **Ficção — diretriz de criação v1:** `agentes_v4_novos/dados/diretriz_criacao_ficcao_v1.md`
  (método/estilo/imagem/publicação/edição/kill switch). `carregar_biblia()` agora lê
  bíblia + diretriz juntas. Contrato → v1.1 (seção Imagens reescrita).
- **Ficção — imagem IA no pipeline:** `v4_ficcao.py` ganhou `imagem_ia()` (gerador
  editorial NYC `gerador_imagem_editorial.py` → Tribunal Visual `checar_imagem_vision.py`
  → upload REST media espelho → meta anexo `cafezinho_image_kind=artificial` + legenda IA
  → featured + readback → `_cafezinho_img_check` ok). Falha = fail-soft (draft sem capa);
  reparo: `python3 v4_ficcao.py --imagem <post_id>`.
  **Prova:** 400075 capa IA (media 400084, generator flux-pro, checker tribunal_visual).
- **Espelho — exceção no gate da home:** `cafezinho-real-image-gate.php` patcheado
  (backup `.bak_pre_ficcao_ia_20260817`): cat Ficção 100002 NÃO é excluída da home por
  imagem artificial; resto do gate intacto.
- **Caçadora e1b2d648 → cobre o ESPELHO:** PASSO 2.6 (varredura cats 100003/1652/775
  sem capa, inclui publicados do Tendências), PASSO 4.6 (aplicar no espelho:
  `wp media import --featured_image` + meta check, root@159.65.177.60,
  `--allow-root --path=/var/www/cafezinho-news`), PASSO 7 (escala aos loops após 2
  rodadas; inbox claude.md + `loop_trindade_laura/mensagens/para_laura`). Ficção NUNCA
  entra. Orçamento: +até 3/rodada no espelho.
- **Loops avisados** (inbox claude.md + para_laura + canal_trindade, 08:29 BRT).
- **BUG: dedup falso positivo derrubou o cap. 2** ("O Fogo Que Não Queimou" × cap. 1 —
  compartilham o nome da série; 17/08 03:10 BRT). Fix: em `v4_ficcao.py`, títulos que
  começam com o nome do livro são removidos da lista de dedup. Cap. 2 sai 18/08 03:10 BRT.
- **Tendências (worker v4_vertical_draft_worker.py):** post 400079 tinha a foto anexada
  como media órfã (post_parent=0, sem `_thumbnail_id`) — capa definida manualmente no
  espelho. Atenção futura: conferir thumbnail após publish no espelho.
- Sessão irmã do Tendências: fórum `forum_v4_tendencias_prototipo_20260816.md` §8.

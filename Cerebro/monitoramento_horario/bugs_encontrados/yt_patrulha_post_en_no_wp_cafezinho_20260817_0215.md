# YT-PATRULHA — Post em INGLÊS do agente YouTube entrando no WP do Cafezinho (caso 266153)

**Tag:** YT-PATRULHA
**Achado por:** ZCode (Qwen 3.8) — aviso direto do Miguel via Telegram 17/08 01:51 ("Post em inglês no cafezinho")
**Status:** 🟡 CONTIDO (draft removido do Cafezinho + handoff pronto pro GSN) — falta o fix definitivo de roteamento (Claude)

## Sintoma

Post **266153** (draft, autor 5786, criado 16/08 23:22) no WP do Cafezinho com título e corpo
100% em inglês: *"Marjorie Taylor Greene says Trump circle discussed nuclear weapons against Iran"*.
É a versão EN do post duplo do vídeo **dFPy6YltmkU** (Dialogue Works/GSN); a versão PT é o
draft **266172** (esse sim pertence ao Cafezinho). Miguel viu no painel/controle e apontou.

## Causa

O `agente_youtube_publicador.py` (NYC) tem `WP_URL = "https://controle.ocafezinho.com/wp-json/wp/v2/posts"`
fixo: **todo** post do agente YouTube — PT ou EN — cai no WP do Cafezinho, sem roteamento por idioma.
O destino natural da versão EN é o **GSN (globalsouth.news)**, que **não é mais WordPress** — é
Astro/Vercel (header `server: Vercel`; `/wp-json` → 403). As credenciais `GSN_WP_*` do
`.env.unificado` são LEGADO do WP antigo (marcadas `_DEPRECADA_20260817` — Regra 4).

## O que JÁ foi feito (ZCode, 17/08 ~02:20)

1. Backup integral do 266153: NYC `/root/agent_data/gsn_handoff_post_266153_20260817.json` +
   local `ZCodeProject/handoff_gsn/post_266153_backup_20260817.json`.
2. Handoff pronto para o GSN: `Cerebro/Foruns/inbox_trindade/handoff_gsn_artigo_266153_EN.md`
   (metadados + embed do vídeo + corpo em markdown; nomes já checados na meta `cafezinho_nomes_check`).
3. 266153 movido para a LIXEIRA no Cafezinho (`wp post delete` sem --force; reversível).
4. 266172 (PT) permanece draft no Cafezinho — aguarda revisão/publicação do Loop Miguel.

## Pendente (Claude — único publicador; próxima corrida do agente YouTube = NYC 11:00)

1. **Publicar o artigo EN no GSN** via repo `sites-v4/globalsouth` (push → Vercel), revisado com
   a Laura (2ª opinião editorial EN). O arquivo de handoff está pronto.
2. **Fix definitivo de roteamento:** artigo EN do agente YouTube (canais GSN) deve ir para o
   fluxo do GSN (ex.: pasta/branch de rascunho do repo), NUNCA para o WP do Cafezinho.
   Sugestão mínima: guard no publicador — se `idioma == "en"` e origem for canal GSN, gravar o
   markdown em `/root/agent_data/gsn_fila/` e pular o POST no WP do Cafezinho.
3. Conferir se há outros drafts EN órfãos no WP do Cafezinho (varredura por idioma).

## Lição

Post de idioma errado em site errado não quebra nada tecnicamente, mas corrói a confiança
editorial — e o público do Cafezinho é PT. Quando um canal de origem é de outro site/idioma,
o rascunho deve nascer no destino certo (ou em fila de handoff), não no WP alheio.

---

## RESOLVIDO 17/08 ~16:20 — ordem Miguel "pode corrigir" (ZCode/DeepSeek)

**Fix definitivo de roteamento aplicado no NYC** (`/root/agents_labs/youtube_v2/`):

1. `youtube_banco_dialogos.py` — `listar_auditados_prontos` agora expõe `v.idioma`.
2. `agente_youtube_v2_publicador.py` — guarda de rota por idioma: `idioma ∈ {en, eng, ...}`
   → artigo NUNCA chama o WP do Cafezinho; é gravado como JSON em `/root/agent_data/gsn_fila/<video_id>.json`
   (título, corpo HTML, excerpt, embed, canal, URL, media_wp_id) e o auditado é marcado
   (`gsn_fila:<id>`) para não reprocessar. PT/idioma vazio segue a rota normal (draft no WP do Cafezinho).
3. Backups `.bak_pre_roteamento_en_20260817` (2 arquivos).

**Provas:** unitário EN→`rota: gsn_fila` (sem tocar WP) e PT→rota normal; apply real gravou o
JSON na fila e marcou o banco (teste com material sintético, limpo depois). Dry-run do estoque
real: fila de auditados vazia no momento (nada pronto).

**Consumidor da fila:** Claude (Loop Miguel) — o fluxo GSN (repo `sites-v4/globalsouth` →
Vercel) deve passar a consumir `/root/agent_data/gsn_fila/*.json`; avisado no inbox (17/08 16:20).
Com isso fecha-se a última porta de artigo em inglês no WP do Cafezinho (junto da regra PT
integral do fórum `forum_regra_idioma_pt_integral_agente_youtube_20260817`).

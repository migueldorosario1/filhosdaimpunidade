# Memória técnica — corte GSN headless × agentes autônomos + editorial BRICS (19/09/2026)

> Sessão: ZCode Miguel (ZM) · Kimi K3 · 19/09 15:5x–16:0x BRT. Irmã de `Foruns/forum_gsn_headless_corte_agentes_20260919.md`. Ref ponte: ZM-20260919-001.

## 1. Diagnóstico reportado pelo Antigravity (relé do Miguel ~15:5x)

- Alvo: droplet **198.199.121.136** (DigitalOcean NYC — segundo a errata de 27/07 do `CEREBRO_INDEX_GSN.md`, é o executor canônico dos agentes GSN).
- Sintomas: `401 Unauthorized` (corpo JSON do WordPress) encapsulado em `404 Not Found` do Apache nos endpoints `/wp-json/wp/v2/media` e `/wp-json/wp/v2/posts`.
- `.env.unificado`: GSN migrado para arquitetura **100% headless (Astro + Vercel + GitHub)**; credenciais WP antigas (`migueladmin`) marcadas como **deprecadas**.
- Efeito: Agentes Autônomos (Antigravity em especial) **sem via de publicação no GSN**.

## 2. Cruzamento com a verdade canônica do Cérebro

- `CEREBRO_INDEX_GSN.md` §0 (Ficha Viva): site público GSN = **Astro/Markdown → GitHub → Vercel**; "não tratar Droplet/SSH como deploy do site público"; executor NYC: `/root/gsn_remote/`, `/root/agente_curadoria_gsn.py`; indexing keys por portal em `/root/agent_data/indexing_keys/` (cada portal com projeto Google Cloud próprio).
- Repo vivo do site: `globalsouth-v4.git` (repoint de 07/08 — `Foruns/forum_gsn_youtube_repoint_v4_20260807.md`; o repo legado `global-south-news.git` é beco sem saída). Frontmatter schema V4 com **`hero_legenda` obrigatória** (ordem 06/08, item 7 dos contratos).
- WP legado GSN: droplet **159.89.237.100** "ocioso pagando" (faxina 07–08/08); o wp-json no NYC é residual dessa era.
- Linha editorial GSN: **EN-only**, geopolítica dura (`Foruns/forum_gsn_linha_editorial_diretriz_20260729.md`).
- Precedente de handoff de artigo EN ao GSN: `Foruns/inbox_trindade/handoff_gsn_artigo_266153_EN.md` (17/08).

## 3. Cafezinho — estado real do editorial (checado na ponte)

- Título (nos 3 rascunhos): "Paulo Nogueira: A cúpula dos BRICS na Índia – resultados políticos e financeiros".
- **Triplicata via REST** (conta Redação nova): **272237** (15:16), **272239** (15:18), **272244** (15:23) — flagrada pela CL no bloco **CL-20260919-032** (15:4x): "@CM: apagar dois e publicar um"; a CL não toca (regra: peça de terceiros).
- O Antigravity reporta o **272244** com imagem e metadados corretos; preview: https://www.ocafezinho.com/?p=272244&preview=true (preview exige sessão WP; REST público não lê draft — 401/404, padrão conhecido).
- Regra viva incidente na execução: **Emenda 5 slot-20min** — publish de autor-agente vira `future` no próximo slot ≥20min (sintoma: data "andando" a cada tentativa); a guarda §130 `wp_set_current_user(2018)` só com ordem expressa do Miguel. Capa: foto real, nunca IA (regra permanente 17/09).

## 4. Entrega ao ZM — arquivos gravados (Cérebro canônico)

| Arquivo | Conteúdo |
|---|---|
| `Foruns/ponte_laura_completa/PROMPT_ZM_GSN_HEADLESS_BRICS_20260919.md` | prompt do Antigravity verbatim + adendo do carteiro (contexto Cérebro, triplicata, regras vivas, handover) |
| `Foruns/ponte_laura_completa/de_dell.md` | bloco **ZM-20260919-001** (→ @ZM executor + @Miguel + @CM + TODOS) |
| `Foruns/ponte_laura_completa/caixa/zm/MSG-20260919-1559-ZM-001.md` | MSG imutável (CONTRATO_CAIXAS v1, header + sha256 7dbb215c… do corpo) |
| `Foruns/forum_gsn_headless_corte_agentes_20260919.md` | fórum do tema (decisões + estado) |
| `Memorias/memoria_gsn_headless_corte_agentes_20260919.md` | esta memória |
| `CEREBRO_INDEX_GSN.md` | linha nova na tabela "Registros de Linha Editorial & Incidentes" |
| `CEREBRO_NODE_ATUALIZACOES.md` | linha do tempo |
| `MONITORAMENTO_DE_TRABALHO.md` | linha ZM-GSN-BRICS-PONTE-20260919 (inicio 15:55 → fim) |

- Sync: `~/cerebro-miguel` → GitHub via `scripts/sync_cerebro_to_github.py` (CEREBRO_DRY_RUN=0) + via GDrive (`rclone` p/ `drive:espelho-zcode/ponte_zcode`). Resultado: ver §6 do fórum irmão / rodapé desta entrega no de_dell.

## 5. Para o executor (checklist enxuto)

1. Ler o prompt completo (`PROMPT_ZM_GSN_HEADLESS_BRICS_20260919.md`) + este log.
2. Cafezinho: revisar o 272244, apagar 272237/272239 (`wp post delete --force`), avisar o CM na ponte, publicar conforme o gate da casa (e a ordem do Miguel).
3. GSN: mapear o que vive no NYC (`/root/gsn_remote/`, crons, repo `globalsouth-v4`), restaurar a via Markdown→GitHub→Vercel, documentar no `CEREBRO_INDEX_GSN.md`, publicar a versão EN integral (frontmatter V4 + `hero_legenda`).
4. Handover ao Antigravity: prompt de devolução com as novas diretrizes/caminhos de acesso (NUNCA valores de chaves — regra do Cofre), gravado também em `Foruns/inbox_trindade/antigravity_desktop.md`.
5. Fechar a linha do monitor + adendo §4 do fórum irmão.

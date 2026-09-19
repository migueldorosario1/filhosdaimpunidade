# 🎛️ FÓRUM — Painel de Destaques dos Temáticos + Faxina de Imagens V4 (2026-08-06)

> **Tema duplo com:** `Cerebro/Memorias/memoria_tematicos_destaques_painel_20260806.md` (log técnico completo)
> **Sessão:** ZCode (Kimi K3) — workspace ZCodeProject · **Ordem:** Miguel, 06/08 (chat direto)

## Decisões (resumo executivo)

1. **Destaques DESLIGADOS por padrão em todos os temáticos.** Os sites ainda não foram divulgados; a regra "manchete = mais vista (GA4)" com 2-26 views virava vitrine congelada (manchete de 21/07 presa no topo do Ceará). Home = mais recentes na frente. Liga-se por site quando o Miguel quiser.
2. **Regra anti-repetição:** destaque exibido no topo NUNCA repete na lista de recentes embaixo (template filtra).
3. **Regra das 48h:** destaque por audiência com mais de 48h cai fora (gerador filtra; template revalida por defesa em profundidade). Sem elegível → mais recentes.
4. **Painel de Destaques** (`agentes_tematicos/v4/painel_destaques.py`, http://127.0.0.1:5057, systemd user `painel-destaques.service`): por site — ligar/desligar, regra (🏆 audiência GA4 / 🕐 recentes), idade máx (padrão 48h), nº de cards, prévia com idade de cada destaque, recalcular na hora. Cada ação grava `src/data/destaques_config.json`, commita e pusha (Vercel redeploya ~1 min).
5. **Imagens — diretriz reafirmada e aplicada:** "imagem casada com o texto" (post com pessoa no título = foto REAL da pessoa). Ceará Digital: 9 heroes erradas trocadas por fotos do Banco OURO (Luizianne ×2, Elmano ×2, Ciro, Lula ×2, Girão, TRE-SP/Lula — esta última era uma gravura de 1879!). Rio Carta: 3 (Paes, Benedita, Castro). Ferramenta: `v4/fix_heroes_banco.py` (reusável).
6. **Cafezinho canônico (WordPress NYC):** degrau novo no worker V4 — **Flickr oficial ao vivo** (Casa Branca/ONU/Pentágono/Macron/Xi) entre o banco e o fallback de IA. Antes, geopolítica caía 100% em cartoon IA. Patch em `/root/v4_vertical_draft_worker.py` (backup `.bak_pre_flickr_live_internacional_20260806`).
7. **Aceleração V4:** gargalo era a fase de imagem (juiz visual sequencial). FASE B da cascata de heroes agora baixa em paralelo (4 workers), dedupa por hash sem LLM e julga em lotes de 3 em paralelo — ordem de prioridade preservada. **Bug bônus corrigido:** Indexing API estava 100% morta (args trocados em `publicador.py` — 559/559 skips; 0 pings na história).

## Estado ao fim do dia

- 6 sites (ceara, riocarta, globalsouth, discoverbrazil, mundotrilhos, railpost) ao vivo com destaques ocultos e mais recentes na frente. mapario/aiatolah não têm seção de destaques (nada a fazer).
- Post "Luizianne Lins é escolhida para o Senado na chapa de Elmano" (05/08) no ar com foto REAL.
- Banco OURO precisa crescer para RJ (Paes/Benedita ×1 cada) e internacional (Ormuz = 0) — o `_registrar_falta_banco` (sessão-irmã, 06/08) já alimenta a fila de coleta.

## Pendências / próximos passos

- Observar o ciclo das 13:00/16:00 (orquestrador V4) com a cascata paralela + indexing corrigido.
- Observar próximos drafts do Cafezinho com foto do Flickr oficial (geopolítica).
- ~30 posts `smoke-*` antigos no Ceará (junho) com heroes duplicadas — candidatos a faxina (decisão do Miguel: limpar ou manter).
- Brave Search API 403 ("subscription token deactivated") — coleta vive de RSS; reativar ou assumir RSS-only.

## Adendo (06/08 ~13:40) — faxina smoke autorizada e executada

Miguel autorizou ("sim, pode limpar"): removidos do Ceará Digital **28 posts de teste `smoke-*` de junho + 46 heroes órfãs + fila horária de teste** (queue era 100% smoke; backup `tools/ceara_hourly_queue.json.bak_faxina_smoke_20260806`). Commit `dd44a4a`, push OK. Verificado ao vivo: home sem nenhuma referência smoke; URL de post smoke antigo → 404. Build limpo. (Objects R2 de heroes smoke viram órfãos remotos — custo trivial, sem ação.)

## Adendo 2 (06/08 ~14:15) — troca de imagens artificiais por REAIS na geopolítica (ordem Miguel: "com todo o cuidado")

**Cafezinho canônico (WP, ocafezinho.com) — 3 dos 4 últimos posts de geopolítica agora com foto real:**
| Post | Antes | Depois |
|---|---|---|
| 264507 Trump/petróleo Venezuela | cartoon IA | foto real Trump (Banco OURO) |
| 264490 Vance/Irã | cartoon IA | posse oficial JD Vance (Wikimedia, PD) |
| 264499 China+Rússia/Japão | cartoon IA | destroyer PLA-N Guilin (Wikimedia, 2025) |
| 264526 Israel/Cisjordânia | cartoon IA | **mantida IA** — juiz visual reprovou todas as candidatas reais (decisão editorial correta; melhor IA que foto errada) |

- Script: `/root/v4_geo_troca_imagens_20260806.py` (NYC) — banco OURO → flickr oficial → Wikimedia, TODA candidata auditada pelo juiz visual do pipeline; mídia antiga preservada; rollback map em `/root/agent_data/v4_geo_troca_imagens_20260806.jsonl`.
- **Lição técnica (nova):** trocar `featured_media` via REST NÃO atualiza `og:image` — o Yoast guarda em `wp_yoast_indexable` (open_graph_image*). Fix: update direto na tabela (backup `wp_yoast_indexable_bak_geo_20260806`) + `wp cache flush` (Redis) + purge WP Rocket. Verificado ao vivo: og:image dos 3 posts já serve a foto real.
- **GSN (globalsouth.news):** Faye (Senegal) e Saied (Tunísia) ganharam fotos reais Wikimedia (commit `36e628d`). **Pegadinha descoberta:** o site tem rewrite `/hero/*` → R2 (`riocarta-hero-images/hero/`) — hero nova precisa subir pro R2 (feito via rclone local, remoto `r2:`), senão 404. Deploy Vercel do GSN estava lento (~1h de fila); quando publicar, as imagens já estão no ar no R2.
- Biya (Camarões): MANTIDA a foto atual — já é real (Casa Branca 2009, com os Obamas); alternativas no Commons não eram melhores.

## Adendo 3 (06/08 ~14:50) — Painel de Destaques DENTRO do CCTV V6 + audiência confirmada

Ordem Miguel: "coloque esse painel lá no CCTV e vê se tem um painel de audiência dos sites temáticos lá — vamos começar a divulgar, preciso acompanhar a audiência".

- **Audiência JÁ EXISTE no CCTV:** `/v6/tematicos/<slug>` por site (views 30d/7d, média móvel 7d, tendência, gráfico SVG; GA4 conta Sites_tematicos). Ex.: RioCarta 204 views/30d, 68/7d em 06/08. `/v6/audiencia` = Cafezinho.
- **NOVO: `/v6/destaques` no CCTV V6** (Tencent, `painel_cctv_v6.py`, backup `.bak_pre_destaques_20260806`): por site — status, ligar/desligar, regra (audiência/recentes), idade máx (24/48/72h presets), nº de cards, prévia com idade de cada destaque (✗ marca os velhos), chip 📈 views/7d e link p/ a página de audiência. Ações gravam `src/data/destaques_config.json` via **GitHub Contents API** (token em `/home/ubuntu/cafezinho/v6/.github_token`, chmod 600 — mesma conta `gh` local) → Vercel redeploya. Testado end-to-end (toggle ceara ON/OFF + idade railpost 24→48h, commits verificados no GitHub).
- **Segurança:** página pública em modo leitura; ações exigem `?key=` (arquivo `/home/ubuntu/cafezinho/v6/.destaques_key`; cópia local p/ o Miguel em `agent_data/v4/painel_destaques_cctv_key.txt`; link pronto no cabeçalho do painel local http://127.0.0.1:5057).
- **Acesso:** http://43.156.151.165/v6/destaques (porta 8084 direta é fechada no security group; nginx :80 faz o proxy).
- Nota: `raw.githubusercontent.com` tem cache próprio — para conferir config recém-gravada, usar a API ou `git show`.

## Adendo 4 (06/08 ~14:45) — BUG build Vercel quebrado por tag com barra (RESOLVIDO)

**Sintoma:** e-mail Vercel "Build Failed" no commit 36e628d (GSN heroes Faye/Saied).
**Causa raiz:** o post do pipeline `20260806-unaids-...` veio com `tags: [..., "hiv/aids", ...]` — a barra virava segmento extra na rota estática `/tags/[tag]` → `TypeError: Missing parameter: tag` → build quebrado (post Libya/UNAIDS ficaram fora do ar na janela).
**Correção em 3 camadas:**
1. **Dado:** tag corrigida p/ "hiv-aids" (commit no GSN) → build verde (477 páginas), deploy recuperado, heroes reais no ar.
2. **Fonte:** `agentes_tematicos/v4/nucleo_frontmatter.py` sanitiza tags (`[/#?\]` → hífen) — nenhum post futuro quebra mais.
3. **Templates:** os 5 sites com `getStaticPaths` alimentado por tags de posts (globalsouth, discoverbrazil, railpost, mapario, mundotrilhos) ganharam `_slugTag` no `[tag].astro` (defesa em profundidade; ceara/riocarta usam rota SSR sem getStaticPaths — sem risco de build; aiatolah não tem rota /tags). Todos pushed com build local verde.
**Lição:** LLM gera tag livre — qualquer campo que vira URL precisa de sanitize na entrada.

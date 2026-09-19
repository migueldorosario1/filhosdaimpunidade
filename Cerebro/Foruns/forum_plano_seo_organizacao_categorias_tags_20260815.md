# 🎯 PLANO DE TRABALHO SEO — Organização de Categorias + Limpeza de Tags (rigoroso, gradual, prudente)

> **Fórum canônico da fase** (Regra Nº 3 — missão retomável em qualquer conversa).
> **Data:** 15/08/2026 ~11:40 BRT · **Autor:** ZCode (GLM-5.3)
> **Origem:** Miguel — *"pode continuar a investigação de organização das categorias e limpeza de tags. quero um plano de trabalho muito cuidadoso sobre riscos de seo do google, por isso qualquer mudança prática terá que ser gradual e prudente."*
> **Relacionados:** `forum_grande_limpeza_taxonomia_cafezinho_20260812.md` (execução Onda 1 ✅) · `forum_politica_categorias_cafezinho_20260812.md` (política de publicação) · `CARTAO_BOLSO_POLITICA_CATEGORIAS.md`.

---

## 1. 📊 BASELINE QUANTITATIVO — Google Search Console, 90 dias (15/05–13/08/2026)

> Extraído via API (service account `sc-domain:ocafezinho.com`, creds no Tencent `/root/google_api_client.py`) — script `/tmp/gsc_baseline2.py`, CSV salvo `/root/gsc_baseline_paginas_90d.csv` (+ cópia local `/tmp/gsc_baseline.csv`). **Este é o alicerce do plano: decisões por dado, não por achismo.**

| Métrica | Valor |
|---|---|
| Páginas com tráfego (90d) | **3.652** |
| Cliques orgânicos totais (90d) | **214.463** |
| **Categorias com tráfego** | **4 de 298** → 1.120 cliques (**0,52%** do total) |
| **Categorias SEM tráfego** | **294 de 298** (zero cliques em 90d) |
| **Tags com tráfego** | **5 de 18.477** → 103 cliques (**0,05%**) |
| Universo de URLs de taxonomia com tráfego real | **9 URLs** |

**As 9 URLs de taxonomia que o Google realmente ama (PROTEGER SEMPRE):**

| URL | Cliques 90d | Impressões | Obs. |
|---|---|---|---|
| `/politica-2/` (Política, cat 22) | 951 | 52.368 | nº 1 do site em categoria |
| `/politica-internacional/` (Internacional, 15) | 108 | 48.344 | |
| `/economia/` (Economia, 43) | 41 | 16.565 | |
| `/pt/` (PT, 2417) | 20 | 10.930 | pequena mas viva |
| `/tag/brasil/` | 53 | 20.742 | tag mais forte |
| `/tag/ira/` (Irã) | 44 | 80 | |
| `/tag/russia/` · `/tag/rollo/` · `/tag/marica-2/` | 2 cada | ~2-4 | residuais |

**Conclusão 1:** o tráfego orgânico do Cafezinho vem de **posts individuais + Discover** (memória auditoria 14/08: Discover +755%). Páginas de arquivo (categoria/tag) são **quase inertes** no Google.
**Conclusão 2:** portanto, mexer na taxonomia tem **risco real de SEO MUITO menor** do que se temia — desde que: (a) as 9 URLs vivas fiquem intactas; (b) redirects 301 acompanhem tudo que muda de URL; (c) o ritmo seja gradual pra proteger o **crawl budget** e a estabilidade de indexação dos POSTS (que são o patrimônio).

## 2. 🧭 Princípios do plano (gradual e prudente, como ordenado)

1. **Nada de apagar por apagar.** Toda operação segue o pipeline: `noindex/observação → merge → redirect → exclusão`, com janela de observação entre cada passo.
2. **As 9 URLs vivas são intocáveis** (lista acima + qualquer URL que venha a somar >20 cliques/90d em monitoramentos futuros).
3. **Menu 21062 = fonte de verdade** (43 itens protegidos, mesmo vazios — regra do Miguel 14/08).
4. **Redirect 301 prévio** a qualquer exclusão/fusão que mude URL (regra já aplicada na Onda 1b — 15 redirects no ar).
5. **Janela de observação de 7–14 dias** entre ondas de escrita no canônico, medindo GSC (o baseline de hoje é o comparador).
6. **Espelho não é referência pra taxonomia** — as operações são no canônico (o espelho sincroniza posts, não termos); validação de HTML/cache é no canônico mesmo.
7. **Backup das 4 tabelas de termos antes de cada onda** (padrão já estabelecido: `/root/backup_taxonomia_*.sql`).

## 3. 🗺️ Matriz de risco revisada (data-driven — substitui a §8 do fórum de 12/08)

| Operação | Risco antes do baseline | Risco REAL agora | Por quê |
|---|---|---|---|
| Excluir tags órfãs (já feito — Onda 1a) | 🟡 médio (200 index,follow) | 🟢 confirmado baixo | 0,05% do tráfego em tags |
| Merge de tags c/ redirect (Onda 1b ✅) | 🟡 médio | 🟢 baixo | idem; redirects 301 no ar |
| **Dedup de slugs de tags (1c)** | 🟡 médio | 🟢 **mínimo** | das 5 tags vivas, nenhuma é duplicata (`ira`≠`ira-2` inexistente etc.) |
| Excluir tags singleton count=1 (12.845) | 🟠 alto no papel | 🟡 **baixo-médio** | só 5 tags têm tráfego; MAS singletons podem ter impressões raras → usar filtro de impressões GSC antes |
| Fundir categorias sem tráfego (ex.: Guerra→Geopolítica) | 🔴 crítico | 🟢 **baixo** | 294/298 categorias = 0 cliques; redirect 301 + exclusão de sitemap = SEO-neutro |
| Mover posts de categoria-cidade → tag (2c) | 🟡 médio | 🟢 baixo | cidades-sem-tráfego (São Paulo capital etc. = 0 cliques) |
| Autores categoria → tag (Onda 3) | 🟠 alto | 🟢 baixo | 0 cliques em TODAS as 45 categorias de colunista |
| **"Redação" (2403, 37.386 posts)** | 🟠 | 🟡 **médio** | URL `/redacao/` SEM cliques em 90d → renomear p/ "Geral" exige redirect; redistribuição massiva = custo de crawl (gradual) |
| Mexer nas 9 URLs vivas | — | 🔴 **PROIBIDO** | Política/Internacional/Economia/PT/brasil/ira = patrimônio |

## 4. 🔬 O PIPELINE PRUDENTE (toda operação de categoria passa por aqui)

```
Fase 0 — INVESTIGAR: slug tem tráfego GSC 90d? está no menu? tem agente CAT_*_ID?
Fase 1 — NOINDEX (mu-plugin noarchive p/ a categoria-alvo) + tirar do sitemap
Fase 2 — OBSERVAR 14 dias (GSC sem impacto? nenhum 404? nenhum alerta?)
Fase 3 — MERGE dos posts p/ categoria destino (lotes ≤500, madrugada)
Fase 4 — REDIRECT 301 no Nginx (ANTES de excluir) + purge cache
Fase 5 — EXCLUIR o termo + revalidar (301 ✅, destino 200 ✅, sitemap regenerado)
Fase 6 — MEDIR 7 dias no GSC (comparar com baseline)
```
> Reaproveitamento: o esqueleto já existe — `/root/seo_pruning/seo_progressive_noindex.py` (GLM, 01/07/2026, fórum `forum_saneamento_seo_automatizado_lotes_20260701.md`) implementava noindex progressivo em lotes. **A nova fase consultará esse histórico** (o que já foi noindexado? `ids_adicionais_noindex_candidatos_20260628.csv`) antes de decidir.

## 5. 📅 ONDAS REVISADAS (com dados na mão — cadência semanal, gates humanos)

### 🟢 Onda 1 ✅ CONCLUÍDA (14/08): 968 tags órfãs + 55 com `#` (40 renames + 15 merges + 15 redirects) — total tags 19.460→18.477.

### 🟢 Onda 2 — Dedup de slugs de tags (1c) — **próxima, risco mínimo**
- Duplicatas conhecidas: `niteroi` (27)/`niteroi-rio-de-janeiro` (1) · `baixada-fluminense`×2 (2+1) · nomes com/sem acento etc.
- Investigar lista completa (slugs limpos vs `-2`/`-rio-de-janeiro`), fundir no slug canônico com redirect.
- **Gate:** Miguel aprova a tabela de pares.

### 🟡 Onda 3 — Fundir categorias SEM tráfego nos blocos editoriais (1d+4)
- Candidatas (0 cliques GSC + fora do menu): Guerra (2.032)→Geopolítica · Golpe (1.795)+Fascismo+Ditadura→Política · STF (886)+Lava-Jato+Corrupção→Justiça · China (1.839)+EUA (1.722)+Rússia+Oriente Médio→ tags correspondentes + Geopolítica · Petrobrás/Petróleo/BNDES/Agro→Economia · Eleições 2014/16/18/20/22/24→Eleições (47, no menu) + tag do ano · Esportes→Esporte · "Ciência&Tecnologia" duplicatas→Tecnologia (já parcialmente feito pela sessão-irmã) · Tourism→Cultura (?) etc.
- ~40–60 fusões via pipeline da §4 (noindex→14d→merge→redirect→excluir), **2–4 categorias por semana**.
- **Regra:** posts ganham a categoria-destino; a categoria antiga some com redirect; NENHUM post fica órfão de categoria do menu.
- **Gate:** Miguel aprova a tabela completa origem→destino (fórum antes de executar).

### 🟡 Onda 4 — Autores categoria → tag (Onda 3 antiga; ~45 colunistas, ~13.500 posts)
- 0 cliques GSC em todas → risco baixo real; ainda assim via pipeline (noindex 14d → merge → redirect `/rhyan-de-meira/` → `/tag/rhyan-de-meira/` → excluir).
- 2–3 autores por semana (Rhyan = 4.212 posts = ~9 lotes de 500).
- **Gate:** tabela de 45 pares aprovada por lote.

### 🟠 Onda 5 — Cidades/regiões-estrangeiras categoria → tag + hierarquia geográfica
- Cidades (São Paulo capital 222, RJ capital 178, Brasília 102, Niterói, BH...) → tag com redirect (0 cliques todas).
- Países (China/EUA/Rússia/Argentina/Europa/Brics/África) → já viram tag na Onda 3; aqui formaliza.
- Hierarquia de TERMOS espelha o menu: parent das 27 UF → região → Regional (atualmente parent=0 — o menu usa menu_item_parent; alinhar os dois).
- **Gate:** tabela.

### 🟠 Onda 6 — "Redação" (2403) e o arquivamento final
- URL `/redacao/`: 0 cliques em 90d → renomear p/ **"Geral"** com redirect `/redacao/`→`/geral/` (ou manter nome — decidir com Miguel).
- Redistribuição dos 37.386 posts: **NÃO** (custo de crawl alto, ganho nulo) — posts antigos ficam; novos vão pra editoriais (política já ativa).
- **Gate:** decisão Miguel (manter vs renomear).

### 🔵 Onda 7 (contínua) — Tags singleton (12.845, count=1)
- Cadência LENTA: 100–200/semana com filtro GSC (excluir só as sem nenhuma impressão em 90d — o baseline local permite filtrar!).
- mu-plugin validador de tag (sem `#`, sem duplicar slug, sem palavra-de-título) pra não gerar lixo novo.
- **Gate:** amostragem mensal aprovada pelo Miguel.

## 6. 📈 MONITORAMENTO (o plano só é prudente se medir)

1. **Baseline GSC mensal** (script `/tmp/gsc_baseline2.py` → repetir dia 15 de cada mês; comparar 9 URLs vivas + total de cliques + impressões das editoriais).
2. **Alertas:** qualquer queda >15% nos cliques totais da semana pós-onda → PAUSAR faxina + investigar (regra kill switch estendida).
3. **Redirect health-check semanal:** os 15 redirects da 1b + novos (curl status) — script leve na vigília */30 se o Miguel quiser.
4. **Search Console "Páginas" (cobertura):** Miguel observa no painel; relatório de exclusões/404 mensal.

## 7. Estado da missão (Regra Nº 3)

- **O que aconteceu (15/08 11:32–11:50):** investigação read-only: re-rastreio das 298 categorias pós-menu + **baseline GSC 90d via API** (3.652 páginas/214.463 cliques) + cruzamento taxonomia×tráfego + descoberta das ferramentas SEO existentes no Tencent (google_api_client, seo_analyzer, seo_pruning).
- **PRONTO:** este fórum (baseline + matriz revisada + pipeline prudente + 7 ondas com gates + monitoramento).
- **FALTA:** Miguel validar (a) a matriz/ondas; (b) começar pela **Onda 2 (dedup slugs — risco mínimo)**; (c) tabela origem→destino da Onda 3 pra eu preparar com calma.
- **Preciso do Miguel:** "vai na Onda 2" (eu preparo a tabela de pares de dedup pra aprovação) — ou prioridade diferente.

## 8. Catalogação
- Este fórum: `Foruns/forum_plano_seo_organizacao_categorias_tags_20260815.md`
- Memória técnica (Tema Duplo): `Memorias/memoria_baseline_gsc_taxonomia_20260815.md`
- Dados: `/root/gsc_baseline_paginas_90d.csv` (Tencent) + `/tmp/gsc_baseline.csv` (local)
- Nodos: `CEREBRO_NODE_SEO_OBSERVATORY.md` + `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` + `CEREBRO_NODE_ATUALIZACOES.md`

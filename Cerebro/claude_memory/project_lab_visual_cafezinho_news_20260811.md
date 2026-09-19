---
name: project-lab-visual-cafezinho-news-20260811
description: "Reforma visual completa cafezinho.news 10-11/08/2026 — Coluna do Editor 3 breakpoints, 4 blocos temáticos por categoria, single post 1 col iPad, 21 slots de ad como calhau. 12 rollbacks empilhados."
metadata: 
  node_type: memory
  type: project
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

Sessão 10-11/08/2026 (madrugada) — refatoração visual completa do espelho `cafezinho.news` (droplet 159.65.177.60, tema `ocafezinho-portal`). Miguel iterou por 12 mudanças cirúrgicas seguidas, cada uma com backup+rollback próprio, na mesma noite. Vai continuar amanhã à noite (12/08).

**Why:** Miguel quer explorar arquitetura visual definitiva antes de portar pro canônico ocafezinho.com. Cafezinho.news é lab — pode ser bagunçado durante iteração.

**How to apply:** Antes de tocar em qualquer coisa no espelho, ler este arquivo pra reconstruir estado atual + rollbacks disponíveis. Portar pro canônico exige protocolo cirúrgico 6 fases ([[feedback-canonico-port-do-espelho-cirurgico]]).

## Arquitetura final da home (SHA `79f9b3c40df3875c...` + ads calhau)

```
1. MANCHETE
2. COLUNA DO EDITOR (4 posts, 3 breakpoints — mobile scroll 1×, iPad 2×2 grid, desktop scroll 2×)
3. NACIONAL (destaque + 4 laterais, category__in=[22, 43])
4. GEOPOLÍTICA (foto hero + 5 títulos, category__in=[5003])
5. CIÊNCIA E TECNOLOGIA (foto hero + 5 títulos, category__in=[30, 19936])
6. LINHA DO TEMPO (timeline vertical hora a hora, sem filtro)
7. RECENTES (grid 4×5)
```

Cada bloco temático faz `array_push($excludes, get_the_ID())` em cada loop pra evitar post repetir entre blocos.

## Categorias mapeadas no cafezinho.news

- 22 Política (12.839 posts)
- 43 Economia (6.284)
- 5003 Geopolítica (5.904)
- 19936 Ciência e Tecnologia (2.815)
- 30 Tecnologia (2.202) — pra unificar oficialmente com 19936 no DB depois
- 735 Ciência (1.148) — separada por decisão Miguel (não incluída na query C&T)
- 20699 No home (flag)
- 2403 Redação (37.374 — marcador operacional worker V4)

## Single post — ajustes iPad vertical

- Post: `col-12 col-lg-8` (100% no md/iPad, 66% no desktop)
- Sidebar: `d-none d-lg-block` (esconde md/iPad, aparece só desktop)
- Novo slot `banner-lateral-tablet` embaixo do post (só md), pra reintroduzir banner sumido da sidebar

## 21 slots de ad reproduzidos como calhau

Mu-plugin `cafezinho-lab-ad-calhau.php` injeta CSS pra `.ad-space` e `[id^="banner-"]` renderizar como caixa tracejada cinza com label "AD SLOT · banner-XXX". Respeita `desktop-ad-space` (≥992px) e `mobile-ad-space` (<992px).

IDs 100% compatíveis com canônico — quando portar, `ad-inserter` popula automaticamente.

## 12 rollbacks empilhados em `/root/` (droplet)

1. `blocos_variantes_20260811/rollback_blocos_variantes.sh` — remove os 4 blocos originais (base)
2. `reorder_blocos_scroll_editor_20260811/rollback.sh`
3. `coluna_apos_manchete_20260811/rollback.sh`
4. `coluna_8_quadrados_20260811/rollback.sh`
5. `coluna_6_3x2_20260811/rollback.sh`
6. `coluna_4_2x2_20260811/rollback.sh`
7. `coluna_swipe_desktop_20260811/rollback.sh` — 3 breakpoints coluna editor
8. `remove_bloco_canonico_20260811/rollback.sh` — retira bloco canônico
9. `blocos_categorias_20260811/rollback.sh` — filtra por categoria
10. `single_1col_ipad_20260811/rollback.sh` — single 1 col iPad
11. `banner_realocado_tablet_20260811/rollback.sh` — banner-lateral-tablet
12. `ads_calhau_20260811/rollback.sh` — **TOTAL do tema** (extrai `theme_pre_ads_calhau.tar.gz`, SHA `dc99994981...`)

## Pendências pro canônico (amanhã à noite)

- **Portar arquitetura em ETAPAS incrementais** (proposto — Miguel ainda não decidiu opção A tudo/opção B etapas)
- **Unificar oficialmente** Tecnologia (30) com Ciência e Tecnologia (19936) via DB (`wp term merge` ou UPDATE `wp_term_relationships`)
- **Configurar ad-inserter** pra popular novo slot `banner-lateral-tablet` (só existe no espelho)

## Regras aprendidas

- `array_push($excludes, get_the_ID())` em todo bloco com `category__in` pra evitar duplicação entre blocos
- Se remover sidebar num breakpoint, banner-sidebar precisa ser realocado noutra posição
- IDs de banner devem ser idênticos canônico↔espelho pra ad-inserter funcionar
- Cache canônico (WP Rocket + serverdoin-cdn) exige purge — no espelho não tem cache
- Basic Auth do nginx: usuário `cafezinho`, senha só Miguel sabe (verificação via HTTP: adicionar temp user `openssl passwd -apr1`, remover depois)

Fórum lab visual detalhado precisa ser criado pra registro cronológico completo (não feito nesta sessão).

Relacionado: [[feedback-canonico-port-do-espelho-cirurgico]] (protocolo 6 fases pro canônico) · [[reference-acesso-sqlite-v4-nyc]] (padrão SSH via alias)

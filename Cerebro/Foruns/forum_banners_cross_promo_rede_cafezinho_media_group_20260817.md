#  Fórum — Banners de cross-promotion da rede Cafezinho Media Group (prompts p/ Claude Design)

**Data:** 2026-08-17 ~01:30 BRT · **Sessão:** ZCode/Qwen (workspace ZCodeProject)
**Ordem do Miguel:** "faz banners dos sites temáticos para a gente cruzar esses banners em todo sistema, ou seja, um vai puxar o outro… desenvolve o conceito, as sugestões de visual, o plano de onde serão localizados nos sites, e faz os prompts de design para o claude." + adendo: "banners também do cafezinho no moka reader… do cafezinho quando em português e do global south news quando em inglês."
**Memória pareada:** `Memorias/memoria_banners_cross_promo_rede_cafezinho_media_group_20260817.md`

---

## 1. Conceito da rede — "Uma rede, muitas vozes"

Cada portal da rede exibe banners dos irmãos. O visitante de um site descobre os outros; o selo "Um portal do Cafezinho Media Group" (no ar desde 05/08 nos 8 temáticos + espelho + Moka) vira **clique**. Regras canônicas:

1. **Idioma casado (regra do Miguel, vinda dos banners Moka):** banner PT só em página/site PT; banner EN só em página/site EN. Aiatolah é bilíngue (raiz EN + /pt/) → troca o set de banners por idioma.
2. **Nunca empilhar (regra do Miguel):** 1 bloco de banner por intervalo de conteúdo; banners da rede NÃO podem ficar vizinhos de anúncios de receita (GAM/Taboola/AdSense).
3. **Receita intocada:** os banners da rede ocupam apenas zonas comprovadamente vazias (ver §4) — jamais substituem ou competem com inventário monetizado.
4. **Formatos padrão da rede:** 300x250 (MREC) e 728x90 (leaderboard), iguais aos do Moka; + 320x100 (strip mobile) para o app Moka Reader. Tudo estático (sem JS) p/ servir por `<iframe>`/`<img>` em WP, Astro e no app.
5. **Rotação:** cada superfície gira entre os irmãos (ex.: Cafezinho mostra Rio Carta ↔ Aiatolah ↔ GSN ↔ Media Group) — 1 por vez, nunca dois juntos.

## 2. Identidades verificadas (recon em código/logo reais)

| Marca | Paleta real (hex) | Logo real | Tom |
|---|---|---|---|
| **O Cafezinho** | vermelho `#CD152B` (--red do tema), preto, branco | xícara de café desenhada à mão c/ vapor + wordmark condensado preto | jornalismo independente brasileiro, desde 2005; combativo e popular |
| **Global South News** | creme FT `#fff1e5`, borgonha `#9e2f50`, teal `#0a5a66` | globo wireframe de anéis orbitais em vermelho-coral | editorial elegante, "The Voice of the Developing World" |
| **Rio Carta** | azul `#2337ff` / `#000d8a`, branco | monograma "R" = cartas empilhadas c/ silhueta de morros + ondas; wordmark fino caps | portal carioca, "por Miguel do Rosário"; postal/carioca |
| **Aiatolah** | quase-preto `#0a0a0c`, verde-neon `#00ff88`, violeta `#7000ff`, glass | wordmark neon (sem emblema no header) | intel/terminal, Oriente Médio & geopolítica pela ótica do Sul Global |
| **Cafezinho Media Group** | neutro quente + vermelho Cafezinho como fio condutor | a própria xícara do Cafezinho como "sol" da constelação de portais | hub institucional, "Central de Portais de Mídia Independente" |
| **Moka Reader** (superfície) | laranja-café `#FF9E3D→#C25410`, creme `#FFF3E6`, Archivo | lâmpada-xícara | app de resumos; hospeda Cafezinho (PT) e GSN (EN) |

## 3. Matriz de cruzamento (quem exibe quem)

| Superfície | Idioma | Banners que exibe |
|---|---|---|
| Cafezinho (WP) | PT | Rio Carta PT · Aiatolah PT · GSN PT · Media Group PT |
| GSN (Astro) | EN | Cafezinho EN · Aiatolah EN · Media Group EN · (Rio Carta EN opcional) |
| Rio Carta (Astro) | PT | Cafezinho PT · Aiatolah PT · Media Group PT |
| Aiatolah raiz | EN | Cafezinho EN · GSN EN · Media Group EN |
| Aiatolah /pt/ | PT | Cafezinho PT · Rio Carta PT · Media Group PT |
| Moka Reader app | PT | **Cafezinho** (ordem Miguel) |
| Moka Reader app | EN | **GSN** (ordem Miguel) |
| Moka Reader app | outros 10 idiomas | GSN EN (sugestão — confirmar c/ Miguel) |
| Hub Media Group | PT/EN | já é o índice da rede (grid de portais) — sem banner |

## 4. Plano de localização (zonas vazias, receita intacta)

**Cafezinho WP (mapa de ads validado em 17/08):**
- Single desktop: `#banner-sidebar` (div sticky do sidebar, MORTA e vazia) → 300x250 rotativo.
- Single mobile: `#banner-after-recents-mobile` (vazia; anúncio vivo mais próximo = half-page na seção de comentários, separado por Leia Mais + Recentes).
- Home desktop: `#banner-after-recents-desktop` (entre Recentes e Top10; home tem 0 anúncios vivos).
- Moka já ocupa: home após Linha do Tempo + single entre foto e texto → cross-banners ficam nas zonas acima, nunca colados no Moka.

**Temáticos Astro (8):** componente novo `CrossPromo.astro` no rodapé, ACIMA do selo `.group-tag` (05/08) — selo vira legenda do banner; idioma lido do config; Aiatolah troca o set por rota (EN raiz / PT em /pt/). Deploy: push (webhook Vercel), exceto Aiatolah que exige `vercel --prod` manual.

**Moka Reader:** componente `PromoBanner.tsx` em 2 pontos não-intrusivos: (a) fim da tela de leitura (após o resumo, antes do footer do app) e (b) página Biblioteca; locale PT→Cafezinho, EN→GSN; formato 320x100 no leitor + 300x250 na Biblioteca; usuário pago/sem-ads futuro pode esconder (decisão de produto p/ Miguel).

**Media Group:** banner do grupo em TODAS as superfícies (é o cartão da rede); CTA p/ `cafezinhomediagroup.vercel.app`.

## 5. Especificação técnica p/ os banners (vale p/ todos os prompts)

- Estáticos: sem animação/JS na arte final (servem por iframe/img; AMP-friendly se um dia forem p/ amp-iframe).
- Texto EXATO fornecido no prompt (Claude Design renderiza o texto; conferir 1 a 1 e corrigir no editor se errar).
- Sem fotos de pessoas (licença zero); ilustração/vetor/tipografia.
- Margem de segurança 8px; CTA em botão pílula; logo/marca ocupando ≥20% da área.
- Entregar cada banner em 300x250 E 728x90 (mesma arte adaptada), + 320x100 só p/ Cafezinho-PT e GSN-EN (Moka).

## 6. PROMPTS PARA O CLAUDE DESIGN (copiar e colar)

### P1 — O CAFEZINHO · PT
Design two static web banners, 300x250 and 728x90, for "O Cafezinho", an independent Brazilian news portal. Brand: hand-drawn black coffee cup with rising steam (its iconic logo) and a bold condensed black uppercase wordmark "O CAFEZINHO"; accent red #CD152B on clean white/very light warm background. Concept "o café que não esfria": the steam from the cup subtly forms the shape of newspaper headline lines. Headline text (exact, pt-BR): "Jornalismo independente desde 2005." CTA pill button (exact): "Leia em ocafezinho.com". Style: bold popular-journalism poster, high contrast, no photos of people, vector illustration only. Deliver both sizes with identical identity.

### P2 — O CAFEZINHO · EN (to run on GSN, Aiatolah-EN)
Same art direction as the O Cafezinho PT banner (hand-drawn steaming coffee cup, condensed black wordmark "O CAFEZINHO", accent red #CD152B, white background, steam forming headline lines), English copy. Headline (exact): "Independent Brazilian journalism since 2005." CTA pill (exact): "Read at ocafezinho.com". Sizes 300x250 and 728x90, static, vector, no photos of people.

### P3 — O CAFEZINHO · strip p/ Moka Reader (PT)
Design a 320x100 mobile strip banner of O Cafezinho to sit inside the Moka Reader app (warm cream app background #FFF3E6). Use the black hand-drawn steaming cup icon at left, condensed wordmark "O CAFEZINHO" in black, headline (exact, pt-BR): "O jornal do seu café de todo dia." CTA (exact): "ocafezinho.com". Background white card with 12px rounded corners and thin #CD152B left border, so it blends into Moka's warm UI. Static, vector, no photos.

### P4 — GLOBAL SOUTH NEWS · EN
Design two static web banners, 300x250 and 728x90, for "Global South News", an English-language geopolitics news site. Brand emblem: wireframe globe made of intersecting orbital rings in coral-red; palette: warm cream #fff1e5 background, burgundy #9e2f50 headline, dark teal #0a5a66 accents. Concept "the rising voice": the orbital globe emblem rising like a sun over a thin horizon line, FT-style elegant editorial layout with a serif headline. Headline (exact): "The Voice of the Developing World." CTA pill (exact): "globalsouth.news". Style: premium newspaper elegance, generous whitespace, no photos of people. Deliver both sizes.

### P5 — GLOBAL SOUTH NEWS · PT (to run on Cafezinho, Aiatolah-/pt/)
Same art direction as the GSN EN banner (orbital wireframe globe, cream #fff1e5, burgundy #9e2f50, teal #0a5a66, serif editorial), Portuguese copy. Headline (exact, pt-BR): "A voz do Sul Global." CTA pill (exact): "globalsouth.news". Sizes 300x250 and 728x90, static, no photos of people.

### P6 — GLOBAL SOUTH NEWS · strip p/ Moka Reader (EN)
Design a 320x100 mobile strip banner of Global South News for the Moka Reader app (cream app background #FFF3E6). Coral orbital-globe emblem at left, serif wordmark "Global South News" in burgundy #9e2f50, headline (exact): "News from the Global South, daily." CTA (exact): "globalsouth.news". White rounded card with thin #9e2f50 left border. Static, vector, no photos.

### P7 — RIO CARTA · PT
Design two static web banners, 300x250 and 728x90, for "Rio Carta", a Rio de Janeiro news portal. Brand: monogram "R" built from stacked letter-cards containing a mountain silhouette (Sugarloaf/Dois Irmãos) with two wave lines below; deep blue #2337ff and navy #000d8a on white. Concept "a carta do Rio": the banner framed like a postal postcard — dashed stamp border at one corner containing the mountain silhouette, postmark circle with the date line. Headline (exact, pt-BR): "O Rio, carta por carta." CTA pill (exact): "riocarta.com". Style: clean carioca postal, airy, vector line art, no photos of people. Deliver both sizes.

### P8 — RIO CARTA · EN (optional, for GSN)
Same postal art direction as Rio Carta PT (R monogram with mountains and waves, blue #2337ff/#000d8a, postcard frame), English copy. Headline (exact): "Rio de Janeiro, letter by letter." CTA pill (exact): "riocarta.com". Sizes 300x250 and 728x90, static, vector.

### P9 — AIATOLAH · EN
Design two static web banners, 300x250 and 728x90, for "Aiatolah", a geopolitics analysis site about the Middle East from a Global South perspective. Brand: near-black #0a0a0c background, neon green #00ff88 glow, violet #7000ff secondary, glassmorphism. Concept "the signal": concentric radar arcs in neon green sweeping from one corner over the dark glass card, thin violet gradient rim light, monospace/tech typography, wordmark "AIATOLAH" in neon green. Headline (exact): "The Middle East, read from the Global South." CTA pill (exact): "aiatolah.com". Style: dark intelligence-terminal, subtle glow, no photos of people. Deliver both sizes.

### P10 — AIATOLAH · PT (to run on Cafezinho, Rio Carta)
Same dark radar art direction as Aiatolah EN (#0a0a0c, neon #00ff88, violet #7000ff, glass), Portuguese copy. Headline (exact, pt-BR): "Oriente Médio pela ótica do Sul Global." CTA pill (exact): "aiatolah.com". Sizes 300x250 and 728x90, static, no photos of people.

### P11 — CAFEZINHO MEDIA GROUP · PT
Design two static web banners, 300x250 and 728x90, for "Cafezinho Media Group", the umbrella of independent Brazilian news portals. Concept "one network, many voices": the black hand-drawn coffee cup of O Cafezinho as a small "sun" at left, with thin red #CD152B orbit lines connecting 5 small dots labeled (tiny caps): CAFEZINHO · GSN · RIO CARTA · AIATOLAH · +MAIS. Warm white background, black condensed wordmark "CAFEZINHO MEDIA GROUP". Headline (exact, pt-BR): "Uma rede, muitas vozes." CTA pill (exact): "Conheça a rede". Style: institutional, clean constellation diagram, vector, no photos of people. Deliver both sizes.

### P12 — CAFEZINHO MEDIA GROUP · EN
Same constellation art direction as the Media Group PT banner (coffee-cup sun, red orbit lines, portal dots), English copy. Headline (exact): "One network, many voices." CTA pill (exact): "Meet the network". Sizes 300x250 and 728x90, static, vector.

## 7. Estado da missão

- **O que aconteceu:** conceito + identidades verificadas + matriz de cruzamento + plano de zonas + 12 prompts prontos p/ o Miguel colar no Claude Design.
- **O que falta:** (1) Miguel rodar os prompts e aprovar as artes; (2) depois da aprovação: implementar hospedagem (`wp-content/cross-banners/` no WP, `public/banners/` nos Astro) + rotação + componente Moka (sprint separado, espelho primeiro); (3) decisão do Miguel: Moka nos outros 10 idiomas mostra GSN-EN ou nada?; Rio Carta-EN entra no GSN?
- **O que preciso de você (Miguel):** aprovar artes + responder às 2 perguntas acima + dar o "vai" da implementação.

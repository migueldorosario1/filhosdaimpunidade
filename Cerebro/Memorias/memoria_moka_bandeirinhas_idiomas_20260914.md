# 🧠 Memória técnica — Moka: sync canônico→espelho→ousadia + cura do seletor de idiomas (14/09/2026)

Fórum-irmão: `Foruns/forum_moka_bandeirinhas_idiomas_20260914.md`

## Ambiente e comandos

- Repo: `~/ZCodeProject/moka-app`. Branch de trabalho da cura: `ousadia` (= remote `ousadia-mirror` → `migueldorosario1/moka-ousadia`).
- Remotes: `origin` = moka (canônico → www.mokareader.com) · `mirror` = moka-espelho (→ moka-espelho.vercel.app) · `ousadia-mirror` = moka-ousadia (→ moka-ousadia.vercel.app, productionBranch main).
- Commits: sinc espelho `428c570` (merge -s ours, árvore=canônico) · sync ousadia fast-forward `5b2d739→2164349` · cura `5d80145` (só ousadia).

### Receita do sync em cascata (ordem do Miguel 14/09: canônico → espelho → ousadia)

```bash
git fetch --all --prune
# ESPELHO (histórico divergente por cherry-picks): merge de sync que adota a árvore do canônico
git checkout -B sync_espelho origin/main
git merge -s ours --no-ff mirror/main -m "sync: espelho = canônico <sha> (ordem Miguel DD/MM) — árvore idêntica ao canônico; histórico do espelho preservado"
git diff --stat origin/main sync_espelho        # DEVE ser vazio
git push mirror sync_espelho:main && git branch -f espelho sync_espelho
# OUSADIA (histórico linear): fast-forward puro
git push ousadia-mirror origin/main:main origin/main:ousadia && git branch -f ousadia origin/main
# PROVA: 3 domínios 200 + string do último commit (ex.: link /privacidade) presente em cada
```

Pré-checks de segurança: `git merge-base --is-ancestor <branch local> <remote>` para confirmar que nada local órfão seria perdido; never force-push (nenhum foi necessário — FF/merge).

## Causa-raiz do dropdown estourado (para futuras guerras)

- A regra de grupo `.igot-topbar-actions button` (~linha 9808 do globals.css) aplica `44×44 + font-size 20px + center` com `!important` a TODOS os botões descendentes — e o `LangSwitcher` (com o dropdown inteiro) mora dentro de `.igot-topbar-actions`. Todo componente com dropdown de `<button>`s dentro dessa topbar pega a mesma doença (precedente: botão Entrar 06/09 `babea59`; agora `.lang-option` 14/09 `5d80145`).
- **Padrão de cura:** seletor triplo `.igot-topbar-actions .lang-switcher .lang-option` (0,3,0) vence o grupo (0,1,1) mesmo com ambos `!important`; publicar perto do bloco base do componente no globals.css.
- `.lang-dropdown max-height: 320px` não comportava 12 itens (medido 318×558) → `min(70vh, 460px)` + `overscroll-behavior: contain` (12 itens ≈ 438px).

## Provas executadas

- tsc 0 erros; next build exit 0.
- Medidas ANTES→DEPOIS (getComputedStyle + getBoundingClientRect no DOM real, /estante):
  - opção: 44×44/20px/center → 170×34/14px/flex-start
  - dropdown: clientH 318 × scrollH 558 → 438 = 438 (lista inteira visível, árabe/híndi inteiros)
- Ousadia produção: CSS chunk `7abde1d80e4df49a.css` com a regra nova + medidas DEPOIS reproduzidas ao vivo (badge OUSADIA presente).
- Dev server de prova: `npx next dev -p 3199` (logs `/tmp/moka_dev_3199.log`, build `/tmp/moka_build_ousadia.log`).
- Screenshot IAB indisponível neste ambiente ("browser screenshot activity capture failed for guest") — prova numérica no lugar; sem Puppeteer instalado nos node_modules vizinhos (checado igot/cafezinhomediagroup/AGY).

## Estado

- 3 ambientes = canônico `2164349` (provado nos 3 domínios). Cura `5d80145` SÓ no ousadia (rito do Miguel: conferir primeiro, depois promover).
- Pendência: OK do Miguel → promover `5d80145` para mirror main + origin main. Telemetria no painel = sprint futuro (pedido citado de passagem).

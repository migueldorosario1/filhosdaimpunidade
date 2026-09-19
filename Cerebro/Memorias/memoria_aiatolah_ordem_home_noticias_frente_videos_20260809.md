# Memória técnica — Aiatolah: ordem da home (notícias na frente, vídeos embaixo)

> **Sessão:** ZCode (GLM-5.2 Z.ai) — chat direto, 09/08/2026 ~20:00 BRT
> **Status:** ✅ NO AR (commit `af32846`, deploy `vercel --prod`, verificado ao vivo)
> **Fórum-irmão:** `Foruns/forum_aiatolah_ordem_home_noticias_frente_videos_20260809.md`

## Contexto

Ordem do Miguel: inverter na home do Aiatolah as duas seções da coluna de notícias — vídeos (broadcasts) deveriam ficar embaixo, notícias na frente. "Vai ficar melhor."

## Arquivos tocados

| Arquivo | Mudança |
|---|---|
| `aiatolah/src/pages/index.astro` | Invertida ordem: `📡 Latest Reports` (posts, hero+grid) agora ANTES do bloco `🎥 Frontier Broadcasts` (vídeos). CSS `.video-showcase`: `margin-bottom: 2rem` → `margin-top: 1.5rem`. |
| `aiatolah/src/pages/pt/index.astro` | Idem em PT: `📡 Últimas Análises` antes de `🎥 Transmissões de Fronteira`. Mesmo ajuste de CSS. |

Ambas as páginas são **quase idênticas** (mesma estrutura, mesmas classes, mesmos estilos `<style>` inline). Mudança foi puramente de **ordem de marcação** dentro de `<section class="news-area">` + 1 linha de CSS por página. Nenhuma lógica de dados alterada.

## Estrutura relevante (antes → depois)

Antes (dentro de `.news-area`):
```
1. div.video-showcase  → 🎥 Frontier Broadcasts
2. h2 + .news-main-grid → 📡 Latest Reports
```

Depois:
```
1. h2 + .news-main-grid → 📡 Latest Reports
2. div.video-showcase  → 🎥 Frontier Broadcasts
```

O bloco `.news-area` tem `display: flex; flex-direction: column;`, então a ordem do DOM = ordem visual. Sem JS de ordenação.

## Build & deploy

- **Build:** `npx astro build` → verde, 198 páginas (`/index.html` e `/pt/index.html` incluídos).
- **Commit:** `af32846` — `layout: bota Últimas Notícias na frente, vídeos (broadcasts) embaixo` (2 arquivos, +60/−60).
- **Push:** `0d81835..af32846  main -> main`, `HEAD==origin/main` (commit-guard).
- **Deploy:** `vercel --prod --yes` (CLI 56.0.0, Node 22). Build local 198 pgs em ~5s; `✓ Ready in 33s`; aliased `https://aiatolah.com`.

## Provas ao vivo

```
EN:  curl https://aiatolah.com/ → "Latest Reports" aparece antes de "Frontier Broadcasts" ✅
PT:  curl https://aiatolah.com/pt/ → "Últimas Análises" antes de "Transmissões de Fronteira" ✅
```

## Descoberta / observação

O **deploy automático via `git push` não disparou** neste projeto (lista de deploys Vercel mostrava o último há 17h, após meu push). O webhook GitHub→Vercel pode estar inativo/desconfigurado para `migueldorosario1/aiatolah`. Usei `vercel --prod` (CLI autenticada) para publicar. Não é bloqueante, mas vale revisar a integração Git no painel da Vercel.

## Protocolo seguido

- Regra Nº 2: lido `MONITORAMENTO_DE_TRABALHO.md` antes de começar (nenhuma sessão no repo `aiatolah`).
- Regra Nº 3: Tema Duplo registrado.
- Backup: não necessário (mudança de ordem sem perda de conteúdo; git é o histórico).

## O que preciso do Miguel

- Confirmação visual ao abrir o site. Nada de código.

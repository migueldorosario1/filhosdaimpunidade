# Fórum — Aiatolah: ordem da home (notícias na frente, vídeos embaixo)

> **Sessão:** ZCode (GLM-5.2 Z.ai) — chat direto, 09/08/2026 ~20:00 BRT
> **Estado:** ✅ **ENTREGUE E NO AR** (aiatolah.com, EN + PT verificados ao vivo)
> **Origem:** ordem do Miguel (texto): *"bota esses broadcasts, os vídeos, embaixo. Deixa o Últimas Notícias na frente. Vai ficar melhor."*

---

## O que aconteceu (resumo de decisão)

O Miguel pediu para inverter a ordem das duas seções da coluna principal da home do Aiatolah. Antes os vídeos (🎥 Frontier Broadcasts / Transmissões de Fronteira) apareciam no topo e as notícias (📡 Latest Reports / Últimas Análises) embaixo. Foi invertido: **notícias na frente, vídeos embaixo** — nas duas línguas.

## O que está pronto

1. **`src/pages/index.astro` (EN)** — ordem invertida: `Latest Reports` (hero + grid de 7 posts) agora antes de `Frontier Broadcasts` (4 vídeos YouTube).
2. **`src/pages/pt/index.astro` (PT)** — idem: `Últimas Análises` antes de `Transmissões de Fronteira`.
3. **CSS `.video-showcase`** (ambas as páginas) — ajustado de `margin-bottom: 2rem` para `margin-top: 1.5rem`, já que o bloco de vídeos agora fica embaixo (respiro visual acima dele, separando das notícias). Sem alteração de grid/cores/tipografia.
4. **Build verde** — `astro build`: 198 páginas, sem erros.
5. **Deploy de produção** — `vercel --prod` (push só não disparou auto-deploy; webhook GitHub→Vercel parece inativo neste projeto, deploy manual foi necessário). Aliased para `aiatolah.com`.
6. **Verificação ao vivo:** EN = `Latest Reports` antes de `Frontier Broadcasts`; PT = `Últimas Análises` antes de `Transmissões de Fronteira`. ✅
7. **Commit:** `af32846` (push `0d81835..af32846`, `HEAD==origin/main`).

## O que falta

- Nada de funcional. Só **confirmação visual do Miguel** ao abrir `aiatolah.com` e `aiatolah.com/pt/` no navegador.

## Observação técnica (registro)

- O deploy automático via `git push` **não disparou** neste projeto (último deploy na lista era de 17h antes). Usei `vercel --prod` com a CLI autenticada (projeto `aiatola`, vinculado em `.vercel/project.json`). Vale verificar se o webhook do GitHub está configurado na Vercel — pode ser só este projeto. Não é urgente.

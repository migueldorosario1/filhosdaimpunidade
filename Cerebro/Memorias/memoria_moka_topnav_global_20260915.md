# 🧠 Memória — Moka: TopNav global (menu no alto em TODAS as páginas)

**Data:** 15/09/2026 · **Quem:** ZCode/GLM-5.3 · **Fórum:** Foruns/forum_moka_topnav_global_20260915.md (Tema Duplo)

## Ordem
Miguel 15/09 ~10:0x (voz): menu no alto em TODAS as páginas (bandeirinha de idiomas + ⚙️ configurações + 🏠 home), começando pelo ousadia. Dor: "abre a primeira estante, não tem menu nenhum" (prateleira book/[id]) e "no vídeo não tem a bandeirinha em cima".

## O que foi feito (commits 9e4eb2e + 2207b59, branch ousadia)
1. TopNav `hidden` default: `true`→`false` + chave de preferência NOVA `moka.navHidden2` (zera o "escondido" persistido pela era CLEAN 31/08 nos aparelhos; olhinho continua funcionando e persiste).
2. Botão 🏠 home em `TopNav` (default do slot right) e `TopNavActions` — Link `/` com aria "Início — voltar para a página central".
3. `book/[id]` (prateleira): `<TopNav active="reader" />` no return principal + nos 3 returns antecipados (loading/loadStuck/notFound). Classe `igot-workspace-no-topbar` saiu do uso.
4. Padronização: tutorial, experimente, auth/confirmado, auth/atualizar-senha, sobre (info-topbar antiga → TopNav). Já usavam TopNav: estante, biblioteca, video, video/[id], configuracoes, ajuda, writer, harness, telemetria, memoria, mural.
5. Pré-sync: merge do main 5d80145 ANTES (o ousadia estava sem a cura do dropdown; npm install p/ undici).

## Como deployou (≠ push)
Push em origin/ousadia NÃO dispara o projeto moka-ousadia (ver lição em memoria_moka_topnav_fonte_estouro: via canônica = `git push ousadia-mirror ousadia:main`). Hoje usei a via CLI (também válida, provada): backup `.vercel/project.json` (link moka-v3) → `npx vercel link -p moka-ousadia --yes` → `npx vercel deploy --prod --yes` (Ready ~47s) → restaurar link moka-v3 + `rm .env.local` (o link cria e é ruído).

## Provas
- Build local verde 2× (27 rotas).
- curl no moka-ousadia.vercel.app: marcador `Início — voltar para a página central` + 🏠 em /estante, /sobre, /tutorial, /experimente, /video, /book/teste-zm (erro incluído) — 15/09 ~11:3x.

## Estado / falta
✅ NO AR no ousadia AGUARDANDO OK do Miguel → promover (rito: ousadia→espelho→canônico www.mokareader.com). Pendência de escopo: player em fullscreen nativo continua cobrindo a tela (comportamento do navegador). Privacidade tem bandeirinha no PrivacidadeConteudo (sem ⚙/🏠 — página de política, decisão registrada aqui).

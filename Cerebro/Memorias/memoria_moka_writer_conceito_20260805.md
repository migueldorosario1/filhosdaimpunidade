# MEMÓRIA — Fundação do Moka Writer (produto separado)
**Data:** 2026-08-05 · **Agente:** Kimi 3 (ZCode) · **Pedido:** Miguel do Rosário
**Tema:** criação do conceito, estratégia, repo e estrutura de Cérebro do **Moka Writer** — SaaS de escrita de livros com IA, irmão do Moka Reader, **totalmente separado do Filhos da Impunidade** (regra explícita do Miguel).

---

## 1. O que foi entregue

1. **Diagnóstico Vercel/GitHub:**
   - `gh` autenticado (migueldorosario1); repo `mokawriter` existia VAZIO (criado por Miguel ~03:57 UTC).
   - `VERCEL_TOKEN` = pendente no Cofre (`CEREBRO_INDEX_MASTER` marca "⏳ Não encontrado") — deploys do ecossistema funcionam via **webhook GitHub↔Vercel** (git push → auto-deploy), sem token de API.
   - Hipótese principal do bloqueio: **GitHub App da Vercel sem acesso ao repo novo** (instalação limitada a repos selecionados). Guia de correção de 2 min registrado no nodo.
2. **Repo seedado** (clone local `/home/migueldorosario/mokawriter`, branch `master`, push `master:master`):
   - `index.html` — landing "Em breve" (dark, PT-BR + nota multi-língua, 3 pilares do produto).
   - `vercel.json` — estático (`cleanUrls`).
   - `README.md` — visão + instruções de deploy (Framework Other, sem build).
   - `docs/CONCEITO_MOKA_WRITER.md` — conceito & estratégia completos.
3. **Cérebro separado (Tema Duplo):** `CEREBRO_NODE_MOKA_WRITER.md` + `Foruns/forum_moka_writer_20260805.md` + esta memória; entrada no `CEREBRO_NODE_ATUALIZACOES.md` e link no `CEREBRO_INDEX_MASTER.md`.
4. **Git identity:** repo novo não herdava identidade — configurada localmente a mesma do repo do livro (`Refatoracao V4 <refatoracao-v4@local>`).

## 2. Conceito (síntese executiva)

- **Produto:** "O Estúdio Editorial de todo escritor" — escrever livro capítulo a capítulo com 6 IAs de fronteira, manual de estilo do autor lido em toda reescrita, fontes do autor injetadas por partes no prompt.
- **Herança (engenharia provada 04–05/08 no Estúdio):** acoplamento leitor↔estúdio, versões R# (gravar/canônica/apagar, numeração max+1), cascata 6 LLMs, proxy serverless anti-CORS, manual no prompt, diretrizes com confirmação inteligente, banco modular 4 partes, safeLocalSet c/ recuperação de quota, sinalização UX (toast/pulso/faixa/flash), copiar texto.
- **Generalizações:** zero conteúdo acoplado; estante multi-livro; i18n total (padrão Moka Reader); manual vazio + templates de gênero; fontes por upload categorizado; BYOK; namespace `mokawriter_*`.
- **Negócio:** Freemium — Free (BYOK, 1 livro, local, export .md) / Pro ~US$12/mês (chaves incluídas, sync, ilimitado, export .docx/.epub) / anual ~US$99. Público: KDP, não-ficção investigativa, ghostwriters, NaNoWriMo. Canais: Product Hunt, comunidades BR, Cafezinho/GSN, SEO. Defesa: lock-in saudável da memória viva do autor.
- **Roadmap:** F0 ✅ → F1 engine portado + i18n → F2 onboarding/estante → F3 fontes+manual → F4 contas/Pro/Stripe → F5 export/polish.

## 3. Regras de separação (permanentes)

1. Nenhum conteúdo de *Filhos da Impunidade* (texto, fontes, manual, dataset) entra no Moka Writer — só engenharia generalizada.
2. Workspace local separado: `/home/migueldorosario/mokawriter` (o livro fica em `Downloads/Antigravity Google/`).
3. Cérebro separado: nodo próprio + fóruns/memórias próprios; catalogação neste nodo (Camada 2), nunca direto no Index Master.

---

## 4. FASE 1 (06/08) — app completo AO VIVO (`dc9fbee`)

- Engine FdI generalizado em `index.html` raiz (526 linhas, 41 KB): criar/gerenciar capítulos, 6 LLMs BYOK (namespaced `mokawriter_*`), versões R# com nextRevKey (max+1), canônica-ponteiro, Manual de Estilo com formulateRule + confirmação, sinal de gravação (showSavedConfirm/markSaveBtn/resetSaveBtns), i18n PT/EN (applyI18n + data-i18n/data-i18n-ph), copiar/baixar/resetar.
- Proxy `/api/kimi.js` (Vercel serverless, padrão FdI).
- **Bloqueio Vercel resolvido:** projeto criado pelo Miguel com Framework=Other só servia `/` — `/app.html` e `/api/*.js` davam 404. Tentei: rewrites vercel.json (loop 308), cleanUrls, mover pra raiz como `app.html`. Solução final: **app = `index.html` raiz** (landing "em breve" aposentada — cumpriu o papel). Proxy `/api/kimi` ficará para a Fase 2 (migrar pra Next.js ou ajustar `outputDirectory`).
- Validação: node --check OK (2 fixes de sintaxe: parêntese em updateSaveIndicator, crase no confirm do deleteChapter); live HTTP 200 com marcadores do app.

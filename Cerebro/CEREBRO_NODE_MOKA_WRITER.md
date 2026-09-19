# ✍️ CEREBRO NODE — MOKA WRITER (Camada 2)

> [!IMPORTANT] **PRODUTO SEPARADO — regra do Miguel (05/08/2026):** o Moka Writer nasce da engenharia do Estúdio Editorial de *Filhos da Impunidade*, mas **NÃO se mistura com o livro** — repositório, domínio, Cérebro e marca próprios. Conteúdo do livro NUNCA entra aqui.

**Tema:** produto SaaS de escrita de livros com IA (multi-língua, como o Moka Reader).
**Criado em:** 2026-08-05 por Kimi 3 (ZCode), a pedido do Miguel.
**Família:** Moka (irmão do **Moka Reader** — "o Reader lê pra você; o Writer escreve com você").

## O produto em uma frase

O Estúdio Editorial de todo escritor: escrever um livro capítulo a capítulo com 6 IAs de fronteira (Gemini, GPT, Claude, DeepSeek, Kimi, GLM) reescrevendo sob o estilo do autor e ancoradas nas fontes dele.

## Ativos do projeto

| Item | Onde |
|---|---|
| **Repositório** | `github.com/migueldorosario1/mokawriter` (público, branch `master`) |
| **Workspace local** | `/home/migueldorosario/mokawriter` (**SEPARADO** do workspace do livro) |
| **Vercel (PRODUTO)** | ✅ `vercel.com/miguel-do-rosario-s-projects/mokawriter` → **`mokawriter.vercel.app` AO VIVO** (HTTP 200, landing Fase 0) — escolhido pelo Miguel em 05/08 como o projeto oficial |
| **Projeto Vercel nº 2 (`moka`)** | 🧪 reservado como **laboratório** (decisão do Miguel, 05/08) |
| **Landing (Fase 0)** | `index.html` na raiz do repo — **aposentada em 06/08**: o `index.html` agora É o app completo (Fase 1) |
| **App (Fase 1)** | ✅ **AO VIVO** `mokawriter.vercel.app` — `index.html` raiz = app funcional completo (engine + 6 LLMs + capítulos + versões + manual + i18n PT/EN). Commit `dc9fbee`. |
| **Conceito & estratégia (canônico)** | `docs/CONCEITO_MOKA_WRITER.md` no repo |

## Decisões fundadoras (05/08/2026)

1. **Herança de engenharia, não de conteúdo:** o motor do Estúdio (acoplamento leitor↔estúdio, versões R#, cascata 6 LLMs, manual no prompt, diretrizes com confirmação, banco modular, safeLocalSet, sinalização) é copiado e **generalizado**; conteúdo do livro nunca.
2. **Multi-língua desde o dia 1** (PT/EN/ES/FR/DE/IT…) — padrão Moka Reader: UI + prompts traduzidos; a IA escreve na língua do livro.
3. **BYOK + local-first:** chaves e manuscrito no dispositivo do autor (privacidade como discurso de venda); Pro com chaves da casa via proxy + quota.
4. **Modelo:** Freemium — Free (BYOK, 1 livro, local) / Pro ~US$12/mês (chaves incluídas, sync, ilimitado, export .docx/.epub).
5. **Roadmap:** Fase 0 ✅ conceito+landing → Fase 1 engine portado + i18n → Fase 2 onboarding/estante → Fase 3 fontes+manual → Fase 4 contas/Pro/Stripe → Fase 5 export/polish.

## ✅ Vercel RESOLVIDA (05/08 ~04:40 BRT)

- Miguel executou o guia e criou o projeto: `vercel.com/miguel-do-rosario-s-projects/mokawriter` → **`mokawriter.vercel.app` AO VIVO** (HTTP 200, landing Fase 0, deploy automático via webhook no push da `master`).
- **Decisão do Miguel:** ESTE projeto (`mokawriter`) é o oficial do produto; o projeto nº 2 (`moka`) fica reservado como **laboratório**.

## ⏳ Bloqueio Vercel (histórico — estado em 05/08, RESOLVIDO acima)

- **Sintoma (Miguel):** não consegue criar o projeto na Vercel para o repo `mokawriter`.
- **Diagnóstico Kimi 3:** repo existe e está seedado (landing + `vercel.json`); `VERCEL_TOKEN` = **pendente** no Cofre (deploys atuais são via webhook GitHub↔Vercel). Causa provável: **o GitHub App da Vercel sem acesso ao repo novo** (repos selecionados) — o repo não aparece no import.
- **Solução (2 min, só o Miguel):** `github.com/settings/installations` → Vercel → Configure → *Repository access* → incluir `mokawriter` (ou "All repositories") → Save → na Vercel: Add New → Project → Import `mokawriter` → Framework **Other** (sem build) → Deploy.

## Ponteiros (Camada 3)

- **Fórum:** `Foruns/forum_moka_writer_20260805.md` — decisões resumidas do produto
- **Memória:** `Memorias/memoria_moka_writer_conceito_20260805.md` — log técnico da fundação
- **Conceito:** `docs/CONCEITO_MOKA_WRITER.md` (repo) — visão, modelo de negócio, roadmap

## Governança

- Novos fóruns/memórias do Moka Writer catalogam **neste nodo** (Camada 2), nunca direto no Index Master.
- Nada de conteúdo de *Filhos da Impunidade* neste projeto (regra absoluta do Miguel).

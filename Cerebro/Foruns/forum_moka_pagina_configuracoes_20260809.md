# ☕ Fórum — Moka: página própria /configuracoes + ranking integrado (09/08/2026)

> Tema Duplo da missão 7 do dia 09/08 (sessão ZCode GLM-5.2 — Kimi/Qwen esgotaram 🔴🔴).
> Irmão técnico: `Memorias/memoria_moka_pagina_configuracoes_20260809.md`.
> Contexto: continuação da sessão (missões 1–6 neste mesmo dia).

## O que o Miguel pediu (voz, resumo)

"Reformula tudo nas configurações. Em vez de pop-up, cria uma página própria no Moka Reader, configurações, pra gente trabalhar. A pessoa pode ver suas IAs, editar, apagar, testar, atualizar cada IA. Informa que pra vídeo e fala neural é importante o OpenAI. Groq não faz fala neural? Grok tem voz neural — bota o Grok. Nessa mesma página vai ter o preço, ranking de preço, ranking de qualidade. Essa configuração vai ser uma página explicativa de IA."

## Decisões (confirmadas via AskUserQuestion)

- **Grok (xAI) + Groq** entram como novos provedores — **mas numa 2ª leva** (crédito no último da cadeia GLM-5.2). Esta leva = página + ranking + organização.
- Escopo: **página + ranking primeiro** (recomendado, consome menos crédito).

## Diagnóstico (da fase de exploração)

- O **backend do cofre** (`lib/config.ts`) já é 100% multi-chave (`VaultEntry[]`, AES-GCM, `activeId`). Não precisou reescrever.
- O `SettingsForm` **já tinha** a lista de entries com ativar/testar/editar/remover + botão Atualizar (missão 6) + olhinho. O problema era **UX confusa** (tudo preso num pop-up 560px) + **bug de sincronização** (snapshot no mount, não reagia ao cache fresco).
- **Ranking** (`LlmPriceRanking.tsx`) já existia mas só estava no `/ajuda`.
- **Bug do menu sumir** (BUG-20260809-MOKA-MENU-SITE-SOME-APOS-CONFIG): a cura definitiva é **remover o pop-up do fluxo principal** — o modal quebrava overlay ao fechar. A página própria elimina o problema na raiz.
- **Grok (xAI) TEM TTS** ($15/1M caracteres, 20+ línguas); **Groq** também tem TTS (en/ar). Hoje o Moka só ativa TTS pra OpenAI (hardcoded). 2ª leva.

## O que foi entregue (commit `5e7c0d8`, 6 arquivos, +221/−13)

### 1. NOVA página `/configuracoes` (`apps/web/src/app/configuracoes/page.tsx`)
- Topbar (logo Moka + "⚙️ Configurações" + AuthGate + LangSwitcher).
- Corpo largo (max 760px, respirável): intro amigável + seção "📝 Suas chaves de IA" (reusa `<SettingsForm>`) + seção "🏆 Ranking de preço e qualidade" (`<LlmPriceRanking>` integrado).
- `SiteFooter` no rodapé (padrão).
- CSS próprio (`.cfg-*`) com tema herdado das variáveis globais.

### 2. Engrenagem das 3 páginas → `router.push("/configuracoes")`
- `/estante`: gear + `Uploader.onOpenSettings` → navega. Modal removido (import + estado limpos).
- `/video`: gear + `config-callout-btn` → navega. Modal fica dormente (settingsOpen nunca true).
- `Reader` via `/book/[id]`: `onOpenSettings` → `router.push("/configuracoes")`.
- **Isto cura o BUG-20260809-MOKA-MENU-SITE-SOME-APOS-CONFIG** na raiz (o pop-up deixa de existir no fluxo principal).

### 3. Fix de sincronização da lista de entries (`SettingsForm.tsx`)
- `useEffect([initial])` re-ler `listAllEntriesSync()` quando a config inicial muda (antes era snapshot no mount; podia renderizar vazio/desatualizado ao abrir a página).

### 4. 4 chaves i18n novas ×12 idiomas
- `cfg_page_title`, `cfg_intro`, `cfg_keys_section`, `cfg_ranking_section` (inseridas após `set_refresh_key` em cada bloco, via script Python com desambiguação por ordem de bloco para zh/ja que partilham "更新").

## Estado

- ✅ **ENTREGUE E NO AR:** commit `5e7c0d8` (push `b94bfac..5e7c0d8`), Vercel auto-deploy.
- ✅ tsc + `next build` verdes; `/configuracoes` 1.17 kB, estante/vídeo intactos.
- ✅ Bug do menu marcado **RESOLVIDO** (pop-up removido do fluxo).
- ⏳ **Pendência:** teste do Miguel (navegar pra /configuracoes pela engrenagem; ver a lista de chaves + ranking).

## Próximos passos (2ª leva — registrado, NÃO executado nesta leva)

- **Grok (xAI)** e **Groq** no `registry.ts` (PRESETS) com adapter OpenAI-compatible.
- Estender a decisão de TTS no Reader (`providerId === "openai"` → aceitar grok/groq/openai).
- Ampliar allowlist de `/api/tts` (`api.x.ai`, `api.groq.com`).
- Atualizar `llm-prices.ts` com modelos Grok/Groq + TTS deles.
- Confirmar com Miguel: o pop-up `SettingsModal` pode ser removido do código de vez (hoje dormente no `/video`)?

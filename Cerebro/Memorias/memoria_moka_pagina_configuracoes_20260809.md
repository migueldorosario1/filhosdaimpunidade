# 🧠 Memória — Moka: página própria /configuracoes + ranking integrado (09/08/2026)

> Log técnico completo da missão 7 do dia 09/08/2026 (sessão ZCode GLM-5.2 — Kimi/Qwen esgotaram 🔴🔴, fallback no último da cadeia).
> Fórum-irmão: `Foruns/forum_moka_pagina_configuracoes_20260809.md`.
> Repo: `/home/migueldorosario/Downloads/Antigravity Google/Outros/Aplicativos/Moka/Moka-Lab` (remote `github.com:migueldorosario1/moka`, branch main, Vercel auto-deploy). Commit do dia: `5e7c0d8` (esta missão).

## Diagnóstico (fase de exploração — 2 agentes Explore em paralelo)

### Backend do cofre (já multi-chave, sólido)
- `lib/config.ts` (570 linhas): `VaultEntry[]` criptografado AES-GCM no localStorage (`igot.aiVault`). Cada entry = `{id, providerId, apiKey, model?, baseUrl?, label?, savedAt}`. `activeId` seleciona qual está em uso. Funções: `getConfigSync`, `setConfig({entryId})` (add/update), `setActiveEntry`, `removeEntry`, `listAllEntriesSync`, `getConfigById` (chave real p/ teste), `getAudioLang`/`getTargetLang`, `getWhisperKey` (vídeo, chave separada `mokavideo.whisperKey`).
- **Não precisou reescrever** — o cofre já suporta múltiplas chaves de provedores diferentes.

### SettingsForm (já tinha a UI, problema era UX + sync)
- `components/SettingsForm.tsx` (1575 linhas): já tem lista de entries (`saved-providers`, ativar/testar/editar/remover), campo de chave com olhinho 👁, botão "Atualizar" (missão 6, `key-refresh-btn`), seção de vídeo (Whisper), 3 selects de idioma.
- **Bug de sync:** `entries` era `useState(listAllEntriesSync())` no mount (linha 80) — snapshot fixo; só atualizava em save/activate/remove. Não reagia ao `invalidateConfigCache()+loadConfigCache()` async.

### Ranking (já existia, só no /ajuda)
- `components/LlmPriceRanking.tsx` (101 linhas): tabela com 15 modelos ordenados por custo de "resumir 1 livro", bloco de transcrição de vídeo. Estilo `<style jsx>` scoped. Só importado em `app/ajuda/page.tsx`.

### Provedores (8, sem Grok/Groq)
- `packages/ai-providers/src/registry.ts` PRESETS: zai, openai, deepseek, together, kimi, qwen, anthropic, gemini. Grok/Groq não existem como presets (Groq aparece só em copy de Whisper).

### TTS neural (hardcoded OpenAI)
- `Reader.tsx`: `providerId === "openai"` decide TTS (linhas ~259, ~1412). `useTTS.speakNeural` → `POST /api/tts` (allowlist: api.openai.com, api.deepseek.com, api.together.xyz).

### Bug do menu (BUG-20260809-MOKA-MENU-SITE-SOME-APOS-CONFIG)
- `SettingsModal` morava inline com `<style jsx>`; ancestral com `transform`/`filter`/`contain` quebrava o overlay `position:fixed` ao fechar. A missão 6 tentou `createPortal` (cura parcial); esta missão **remove o pop-up do fluxo principal** → cura na raiz.

## Implementação (commit `5e7c0d8`, 6 arquivos, +221/−13)

### 1. NOVA `apps/web/src/app/configuracoes/page.tsx`
- Client component. Topbar `.igot-topbar` (logo + `⚙️ {t("settings")}` + AuthGate + LangSwitcher, sem gear).
- Corpo `.cfg-body` (overflow-y auto) → `.cfg-container` (max-width 760px): header (`.cfg-title` + `.cfg-intro`), seção chaves (`<SettingsForm initial={config} onSaved={handleSaved}>`), seção ranking (`<LlmPriceRanking>`).
- `useEffect` boot: `invalidateConfigCache()→loadConfigCache()→setConfig(getConfigSync())`. `handleSaved` idem (recarrega após save).
- CSS scoped `<style jsx>` (`.cfg-*`), responsivo (mobile 600px).
- Import `AIConfig` de `@igot/ai-providers` (não de `@/lib/config` — pegadinha do tsc).

### 2. Engrenagens → `router.push("/configuracoes")`
- `app/estante/page.tsx`: gear onClick + `Uploader.onOpenSettings` → navega. Removidos: import `SettingsModal`, estado `settingsOpen`/`setSettingsOpen`, bloco `<SettingsModal>`.
- `app/video/page.tsx`: gear onClick + `config-callout-btn` onClick → navega. `settingsOpen`/`SettingsModal` ficam dormentes (nunca true; compatibilidade).
- `app/book/[id]/page.tsx`: `onOpenSettings={() => router.push("/configuracoes")}` (Reader recebe callback, não tem router próprio).

### 3. Fix sync entries (`SettingsForm.tsx`)
- Adicionado `useEffect(() => { setEntries(listAllEntriesSync()); }, [initial]);` após o estado `entries` — reage quando a config inicial muda (página recarrega cache fresco).

### 4. i18n ×12 (`ui-strings.ts`)
- Union: 4 novas (`cfg_page_title`, `cfg_intro`, `cfg_keys_section`, `cfg_ranking_section`).
- 12 blocos: inseridas após `set_refresh_key` em cada um. Script Python: localiza as 12 ocorrências de `set_refresh_key:` por `re.finditer`, associa à ordem de idiomas [pt-BR,en,es,fr,de,it,ru,zh,ja,ko,ar,hi], insere de trás pra frente (não desloca índices). Desambiguação necessária porque zh/ja partilham "更新".

## Verificação
- `npx tsc --noEmit` → limpo (após corrigir import `AIConfig`).
- `npx next build` → verde: `/configuracoes` 1.17 kB, `/estante` 7.51 kB, `/video` 8.63 kB.
- Push: `b94bfac..5e7c0d8` (HEAD == origin/main). Vercel deploy.
- Ao vivo: verificação do chunk JS (fluxo padrão).

## Backups
- `Outros/Aplicativos/Moka/backups/moka_lab_pre_pagina_config_20260809/`: SettingsForm.tsx, estante_page.tsx, video_page.tsx, book_id_page.tsx, ui-strings.ts.

## Estado da missão
- **O que aconteceu:** página própria `/configuracoes` criada (reusando SettingsForm + integrando LlmPriceRanking); engrenagens das 3 páginas navegam em vez de abrir pop-up; bug do menu resolvido na raiz; fix de sync da lista de entries; 4 chaves i18n ×12. Build verde, deploy no ar.
- **O que falta:** teste do Miguel (navegar pela engrenagem; ver lista de chaves + ranking; confirmar que o menu do site parou de sumir).
- **O que preciso de você (Miguel):** abrir mokareader.com → engrenagem ⚙️ → ver se cai em `/configuracoes` com o formulário + ranking; testar adicionar/ativar uma chave; confirmar que voltando dali o menu do site continua lá.

## 2ª leva (registrada, não executada — crédito)
- Grok (xAI) + Groq no `registry.ts`.
- Estender decisão de TTS (grok/groq/openai).
- Allowlist `/api/tts` (api.x.ai, api.groq.com).
- `llm-prices.ts` com modelos novos + TTS Grok/Groq.

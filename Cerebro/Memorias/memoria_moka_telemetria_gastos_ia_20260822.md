# Memória técnica — Moka Reader: telemetria de gastos de IA (22/08/2026)

Sessão ZCode/Qwen 3.8 · workspace `~/ZCodeProject` · repo `moka-app` (monorepo Next.js: apps/web + packages/ai-providers/parser/rag) · commit `fc63cb7` em `origin/main` (18 arquivos, +3632/−189).

## Arquitetura entregue

### 1. `packages/ai-providers` (base de tudo)
- `types.ts`: interface `UsageInfo { promptTokens, completionTokens, totalTokens }` e `CompleteOptions.onUsage?: (u: UsageInfo) => void`.
- Adapters com captura de uso REAL:
  - `openaiCompatible.ts`: chat normal lê `usage` da resposta; stream usa `stream_options: { include_usage: true }` (último chunk traz usage) com fallback retry sem a opção se o servidor devolver 400.
  - `anthropic.ts`: `message_start` (input_tokens) + `message_delta` (output_tokens).
  - `gemini.ts`: `usageMetadata` (promptTokenCount/candidatesTokenCount).

### 2. `apps/web/src/lib/telemetry.ts` (NOVA — coração)
- IndexedDB **separado** `moka_telemetry` v1, store `records` (índices by_ts/by_task/by_provider) — nome diferente do DB principal `igot` pra não dar conflito de versão. `openTelemetryDB` com timeout 3s.
- `TelemetryRecord`: id, ts, task, providerId, providerName, model, prompt/completion/totalTokens, usageEstimated, costUsd, status ok|error, note?.
- `putRecord`/`listRecords` (mais recente 1º)/`clearRecords` — sempre silenciosos em erro (telemetria nunca quebra o app).
- Prefs (`moka.telemetry.prefs`): `PopupMode "always"|"above"|"off"` (default **above**), `popupThreshold` (default **500**), `tokenCap` (default **0** = sem trava).
- Moedas: 13 (`CURRENCIES` — USD/BRL/EUR/GBP/JPY/CNY/CAD/AUD/CHF/INR/KRW/MXN/ARS, taxas fixas aproximadas), `getCurrency` autodetecta região do navegador, `convertFromUsd`, `fmtMoney` (casas decimais conforme magnitude).
- Estimativa: `estimateTokens` (~4 chars/token latino, ~1,5 CJK), `estimateTaskInputTokens(text, system?, context?)`.
- Custo: `findPrice(providerId, model)` casa fuzzy na tabela `llm-prices` (substring nos 2 sentidos + tokens em comum; fallback = modelo mais barato do provedor) e `computeCostUsd`. TTS cobrado por caractere: `TTS_PRICES_PER_M_CHARS` + `estimateTtsCostUsd`.
- Evento global `USAGE_EVENT = "moka:usage"` (CustomEvent) disparado por `recordUsage(opts)` conforme prefs (sempre mostra em erro ou cap excedido).

### 3. `apps/web/src/lib/ai-client.ts` (livros)
- Toda ação (translate, translateStream, translatePage(Stream), explain(Stream), explainPageStream, translateForSpeech, ask(Stream), summarizeStream, testConnection) agora:
  1. pré-voo do cap → `capBlockedMessage` (msg traduzida `errTokenCap`, nada é enviado);
  2. captura uso via `onUsage`;
  3. `recordCall` fire-and-forget (task + identidade provedor/modelo).
- `runStreamWithCap`: consome o stream e CORTA no meio se estourar o cap (mantém texto já gerado, volta `{full, capCut}` → aviso `errCapCut`).
- `checkBalance(config): BalanceResult` — DeepSeek: GET `{baseUrl}/dashboard/balance` via proxy (`/api/proxy`); demais: `{unsupported:true, usageUrl}`. Nunca lança.

### 4. Vídeo + voz
- `video/ai-client.ts`: `runStream` com telemetria + cap; 7 tarefas (video-explain/summarize/characters/political/critique/correct/ask); map-reduce do resumo grava chunks `silent:true`.
- `useTTS.ts` + botão "▶ Escutar voz" do SettingsForm: tarefa `tts` com `costUsdOverride = estimateTtsCostUsd`.

### 5. UI
- `UsageToast.tsx` (NOVO): escuta `moka:usage`, pop-up canto inferior direito (auto-some 15s), tokens in/out, custo USD + moeda local ("≈" se ≠ USD; "(estimado)" se estimado), erro/aviso de cap, link `/telemetria`, botão "não quero mais ver isso" → `popupMode: "off"`. Montado em `layout.tsx` DENTRO do I18nProvider.
- `SettingsForm.tsx`:
  - 🧩 no card da chave vira botão → editor inline (`updateEntryModel` NOVA em config.ts; 🔍 lista modelos com a chave já salva);
  - 💰 → `checkBalance` (resultado inline: valor USD, erro, ou link do painel oficial);
  - seção "💸 Avisos e trava de consumo": radios sempre/acima de X/nunca + número da trava + hint + link /telemetria.
- `/telemetria` (NOVA): totais (custo/tokens/chamadas), tabelas por provedor/tarefa/modelo, marcador "💲 + moeda local" (persistido), calculadora (provedor+modelo+tokens→custo), histórico (últimos 100), export CSV, limpar com confirm.
- CSS tudo em `globals.css` (classes `usage-toast-*`, `tele-*`, `model-inline-*`, `balance-*`) — nada de style jsx (regra FOUC do projeto).

### 6. i18n
- `telemetry-strings.ts` (NOVO): ~60 chaves × 12 idiomas (`tt(lang, key)` + `taskLabel`).
- `messages.ts`: `errTokenCap`/`errCapCut` em 8 idiomas (o bloco russo estava faltando — completado na revisão do tsc).

## Comandos/provas
- `tsc --noEmit` → limpo (2 erros achados e corrigidos: `voiceConfig.label` inexistente → nome do preset; bloco ru sem as 2 mensagens novas).
- `npm run build` → verde, rota `/telemetria` 2.77 kB (First Load 230 kB).
- Push rejeitado (trabalho novo no remote: Moka 6.7/6.8 de outra sessão) → `git rebase origin/main` limpo → rebuild verde → push `fc84138..fc63cb7`.

## Gotchas (lições)
- O `.next/types` guarda referência de páginas removidas (a 6.8 removeu /socios) — erro de tsc pós-rebase some com novo build.
- `getEntryForVoice()` retorna `AIConfig` sem `label` — pra nome de exibição usar `PRESETS.find(...)?.name`.
- IndexedDB: usar NOME DE DB DIFERENTE do app principal evita `versionerror` em produção.

## Estado final
Tudo commitado/pushado. Falta: teste real do Miguel + confirmação do deploy Vercel. Fórum: `Foruns/forum_moka_telemetria_gastos_ia_20260822.md`.

---

# Rodada 2 — correções do feedback (22/08 tarde)

## Arquivos tocados (commit a3db3c9, 9 arquivos, +846/−366)

- `SettingsForm.tsx`: removidos `balanceState`, `handleCheckBalance`, import `checkBalance`, JSX do botão 💰 e da caixa `balance-result`. Editor de modelo movido pra FORA de `.saved-provider-info` (era filho da coluna flex estreita → quebrava o layout); agora é sibling do `.saved-provider-actions`, largura total. Handlers novos: `handleOpenModelEditor` (toggle + auto-fetch via `listModels(config)` ao abrir), `persistModel` (`updateEntryModel` + `loadConfigCache` + refresh), `handlePickModel` (salva em 1 clique). Botão virou pílula `🧩 modelo ▾`. Link pequeno de telemetria trocado por banner `.tele-banner` (Link pra /telemetria c/ ícone + título + subtítulo + seta).
- `TelemetryIconButton.tsx` (NOVO): botão `.gear.tele-gear` com 📊, `router.push("/telemetria")`, aria/title via `tt(lang,"tele_nav")`.
- `Capa.tsx`, `estante/page.tsx`, `video/page.tsx`, `ajuda/page.tsx`: `<TelemetryIconButton />` inserido na topbar junto do ⚙️.
- `telemetry-strings.ts`: 10 chaves novas × 12 idiomas (`tele_nav`, `tele_page_title` SEM emoji, `tele_intro`, `tele_your_ais`, `tele_no_ais`, `tele_add_key`, `tele_spend_title`, `tele_ai_spent`, `tele_open_settings`, `tele_banner_sub`). Chaves `set_balance_*` ficaram órfãs (inofensivas).
- `telemetria/page.tsx` (REESCRITA): página de controle "Suas IAs". Estrutura padrão `cfg-page > igot-topbar (logo+label 📊+AuthGate+LangSwitcher+✕ router.back()) > cfg-container > cfg-header (h1 🤖)`. Componente `AiModelPicker` (auto-fetch + 1 clique). Helper `t2(lang,key)` pra search/no_models/save/cancel em 12 idiomas sem importar ui-strings inteiras. `spendFor(e)` = gasto por entry (match providerId + modelo compatível). Seções: suas IAs (cards `.tele-ai-card` ou estado vazio c/ link de adicionar) → gastos por uso (moeda, showLocal, calculadora, totais, tabelas, histórico, export/limpar) → `LlmPriceRanking` → link configurações → SiteFooter.
- `globals.css`: removidos `.balance-btn`/`.balance-result`; `.model-edit-btn` virou pílula (inline-flex, radius-pill); `.saved-provider-card { flex-wrap:wrap }`; `.model-inline-editor { flex:1 1 100%; width:100% }` c/ borda accent; novos `.model-edit-arrow`, `.model-inline-title`, `.tele-banner*`, `.igot-topbar .gear.tele-gear`, `.tele-ai-*`, `.tele-empty-ais`.

## Causa raiz do "entra quebrado" (lição)
`.saved-provider-card` é `display:flex; justify-content:space-between` TOP-LEVEL (verificado por análise de profundidade de chaves no CSS — não está dentro de media query). Renderizar editor largo DENTRO de `.saved-provider-info` (flex column, `min-width:0; flex:1`) esmagava o conteúdo. Regra: editor que precisa de largura deve ser filho do card (flex-wrap), nunca da coluna de info.

## Provas
- `grep checkBalance|balanceState|handleCheckBalance src/` → só resta a definição em `ai-client.ts:1042` (código morto, sem import).
- `tsc --noEmit` limpo; `npm run build` verde, `/telemetria` 6.47 kB estática.
- Push `fc63cb7..a3db3c9` main. Produção: 5 rotas = HTTP 200; grep no HTML vivo achou "Suas IAs" (telemetria), `.tele-gear` (capa), `.tele-banner` (configuracoes).

## Estado final
Tudo NO AR. Pendente: teste do Miguel no editor 🧩; limpeza opcional do `checkBalance` morto e strings `set_balance_*`.

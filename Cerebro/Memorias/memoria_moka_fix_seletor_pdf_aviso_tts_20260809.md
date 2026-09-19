# 🧠 Memória — Moka: seletor de parágrafo no PDF + aviso amigável de voz neural sem chave (09/08/2026)

> Log técnico completo da missão 3 do dia 09/08/2026 (sessão ZCode Qwen 3.8 Max Token Plan, workspace ZCodeProject).
> Fórum-irmão: `Foruns/forum_moka_fix_seletor_pdf_aviso_tts_20260809.md`.
> Repo: `/home/migueldorosario/Downloads/Antigravity Google/Outros/Aplicativos/Moka/Moka-Lab` (remote `github.com:migueldorosario1/moka`, branch main, Vercel auto-deploy). Commits do dia: `23f521d` (missão 1) → `000762e` (missão 2) → **`f42efbc` (missão 3, esta)**.

## Pedido do Miguel (mensagem de voz, resumo)

- "O seletor, que você botou aqui, do começo, parágrafo… era justamente pra resolver um bug que às vezes tinha dificuldade de pegar no começo do parágrafo. Mas não está funcionando."
- "Se eu pedir pra falar e não tem a chave do OpenAI configurada… tem que dar um aviso certinho na língua da pessoa: 'para ouvir com voz natural, configure a sua chave do OpenAI nas Configurações'. Se conseguir falar sem API pelo mecânico, beleza — mas tem que dar o aviso." (Ele viu resposta 401.)

## Diagnóstico

### Problema 1 — botões ⇤/¶ mortos no PDF
- `snapSelectionStartToParagraph` (Reader.tsx ~L1133) e `expandSelectionToParagraph` (~L1157) faziam `closest("p, h1, h2, h3, h4, h5, h6, blockquote, li")` e **retornavam em silêncio** quando não achavam nada.
- Na camada de texto do pdf.js 4.10.38 (renderizada pelo nosso `PdfPageCanvas.tsx` via `new TextLayerClass({textContentSource, container, viewport})` no `div.pdf-text-layer`) **só existem `<span>` posicionados** (+ um `div.endOfContent` que nós adicionamos) → `closest()` nunca acha nada em PDF → botão parecia quebrado. Em EPUB (blocos `<p>` do parser) funcionava.

### Problema 2 — 401 sem aviso amigável
- Fluxo: `readPageAloud`/`fireSpeak` → `getConfigSync()` (cofre criptografado no localStorage, `lib/config.ts`) → se `providerId === "openai"` → `tts.speakNeural(...)` → `POST /api/tts` (`apps/web/src/app/api/tts/route.ts`: 400 se faltar text/apiKey/baseUrl; allowlist de hosts api.openai.com/api.deepseek.com/api.together.xyz; erro do provedor — ex. 401 de chave inválida — propaga).
- `useTTS.speakNeural` pegava o `!response.ok`, dava `console.warn` e **caía pra voz nativa sem contar nada ao usuário**.
- O único aviso existente era hardcoded em pt-BR dentro do `readPageAloud`, só para "provedor ≠ openai" — não cobria: chave vazia, chave inválida (401), nem o `fireSpeak` (menu de seleção, que não avisava nunca).

## Implementação (commit `f42efbc`, 3 arquivos, +161/−26)

### 1. `apps/web/src/lib/ui-strings.ts`
- Nova chave `tts_neural_hint` no union `UIStringKey` + nos **12 blocos de idioma** (inserida após `reader_tts_translating` via script Python com âncoras únicas).
- pt-BR: "🔊 Para ouvir com voz natural, configure a sua chave da OpenAI nas Configurações (⚙️). Por enquanto, o Moka usa a voz gratuita do seu dispositivo." (en/es/fr/de/it/ru/zh/ja/ko/ar/hi equivalentes).

### 2. `apps/web/src/hooks/useTTS.ts`
- `speakNeural` agora retorna `Promise<{ ok: boolean; status?: number }>`:
  - sucesso (inclusive cache) → `{ ok: true }`;
  - `AbortError` → `{ ok: false }` (sem status = não avisar);
  - demais falhas → mantém o fallback pra voz nativa (`speak(text, lang)`) e retorna `{ ok: false, status: httpStatus }` (status capturado do `response.status` antes do throw).

### 3. `apps/web/src/components/Reader.tsx`
- **Novo helper de módulo `pdfParagraphSpanRange(range)`** (fim do arquivo, antes de `escapeHtml`):
  - só atua se os dois extremos da seleção estão no mesmo `.pdf-text-layer`;
  - agrupa os spans em linhas pelo `top` do `getBoundingClientRect()` (tolerância `max(3px, 0.5×altura)`);
  - `isParaStart(i)` marca fronteira de parágrafo entre linhas quando: (1) altura de fonte difere > 20% da média; (2) gap vertical > 0.5× altura da linha anterior; (3) indento `x0` da linha atual > `max(4px, 0.6×altura)` além do `x0` anterior; (4) linha anterior termina > 1.2× altura antes da margem direita (`rightEdge` = máximo dos `x1`);
  - sobe da linha inicial até a última fronteira (`while a>0 && !isParaStart(a) a--`) e desce da linha final simetricamente; retorna `{ first, last }` = primeiro span do parágrafo inicial / último span do parágrafo final.
- `snapSelectionStartToParagraph`: EPUB no `closest()` como antes; sem bloco → `pdfParagraphSpanRange` e `setStart(pdf.first, 0)` (fim da seleção preservado).
- `expandSelectionToParagraph`: idem; PDF → `setStart(pdf.first, 0)` + `setEnd(pdf.last, last.childNodes.length)`.
- **Novo `warnNeuralKeyOnce()`** no componente: `alert(t("tts_neural_hint"))` 1× por sessão (reaproveita a chave `sessionStorage moka.ttsWarned` que já existia).
- `readPageAloud`: `neuralReady = config && providerId === "openai" && apiKey não vazia`; se não pronto → `warnNeuralKeyOnce()` + voz nativa (substituiu o alerta hardcoded pt-BR); se a API responder 400/401/403 → `warnNeuralKeyOnce()` (fallback nativo já aconteceu dentro do hook).
- `fireSpeak` (menu de seleção 🔊): mesma lógica — antes não avisava nunca no caminho sem chave.

## Verificação

- `npx tsc --noEmit` → limpo. `npx next build` → verde (todas as rotas; `/book/[id]` 31.9 kB).
- Push: `000762e..f42efbc` (HEAD == origin/main). Vercel: deployment `moka-5n9yp85j5-migueldorosario1s-projects.vercel.app` pronto ~13:02 BRT.
- Ao vivo: chunk JS de `/book/[id]` conferido por grep (ver memória de verificação abaixo).

## Backups

- `Outros/Aplicativos/Moka/backups/moka_lab_pre_sel_tts_20260809/` — Reader.tsx, useTTS.ts, ui-strings.ts (estado pré-missão, commit `000762e`).

## Estado da missão

- **O que aconteceu:** diagnóstico + fix dos 2 problemas, build verde, deploy no ar, registros no Cérebro.
- **O que falta:** teste real do Miguel (botões num PDF; aviso sem chave / com chave inválida, na língua configurada).
- **O que preciso de você (Miguel):** abrir um livro PDF no mokareader.com, selecionar um trecho no meio do parágrafo e tocar ⇤ e ¶; depois testar o 🔊 sem chave OpenAI configurada (ou com chave errada) e confirmar o aviso amistoso.

---

## Adendo técnico — Missão 4 (~13:15–13:25): remoção do pop-up de instalação do /video

- **Pedido:** Miguel não quer mais o cartão "Instalar" embaixo do /video nem o recadinho de instalar no herói; a futura janelinha "baixe o aplicativo" (pós-lojas) será discutida com ele.
- **Arquivo tocado:** `apps/web/src/app/video/page.tsx` (4 linhas fora): import do `InstallPrompt`, `<InstallPrompt />` (antes L461) e `<p className="hero-install-note">{t("video_install_note")}</p>` (antes L363).
- **Não tocado (dormente de propósito):** `components/InstallPrompt.tsx` (reuso futuro), chave `video_install_note` ×12 no ui-strings.
- **Commit:** `a12f998` (push `f42efbc..a12f998`); tsc+build verdes (`/video` first-load 8.71→7.89 kB). Backup: `backups/moka_lab_pre_sel_tts_20260809/video_page.tsx`.
- **Verificação ao vivo:** página /video sem o cartão e sem a nota (ver fluxo de verificação da memória).

---

## Adendo técnico — Missão 5 (~13:35–13:50): alerta cru de erro da IA na fala

- **Cadeia do erro:** menu seleção → 🔊 Falar → `fireSpeak` → `prepareSpeech` → idioma da fala ≠ idioma do texto → `translateForSpeech` (`lib/ai-client.ts`) → provider ativo (DeepSeek, `packages/ai-providers/src/providers/openaiCompatible.ts:154` lança `` `${this.name} respondeu ${status}: ${detail}` ``) → `{ok:false,error}` → `alert(\`⚠️ ${res.error}\`)` em Reader.tsx L182.
- **Fix (commit `750f0d9`):** L182 agora = `console.warn("Tradução pra fala falhou:", res.error)` + `alert(t("reader_speech_translate_error"))`. Nova chave i18n ×12 inserida após `tts_neural_hint` em cada bloco (script Python, âncoras únicas).
- **Config relevante:** `getAudioLang()` (`lib/config.ts` L445, localStorage `igot.audioLang`, default "original"); SettingsForm L536 tem a opção `📖 set_audio_original` — a dica do aviso é acionável.
- **Verificação ao vivo:** chunk da página do livro com a nova string (ver fluxo padrão).
- **Backup:** `backups/moka_lab_pre_speech_401_20260809/` (Reader.tsx + ui-strings.ts).

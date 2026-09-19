# ☕ Fórum — Moka: seletor de parágrafo no PDF + aviso amigável de voz neural sem chave (09/08/2026)

> Tema Duplo da missão 3 do dia 09/08 (sessão ZCode Qwen 3.8 Max Token Plan, workspace ZCodeProject).
> Irmão técnico: `Memorias/memoria_moka_fix_seletor_pdf_aviso_tts_20260809.md`.
> Contexto: continuação das missões do dia (1: feedback elogio-first `23f521d`; 2: slider "Carregando página…" `000762e`).

## O que o Miguel pediu (voz, quase literal)

1. **Seletor:** os botões ⇤ "Do começo" e ¶ "Parágrafo" do menu de seleção (feitos pra ajudar o tradutor a pegar o começo do parágrafo quando a alça escorrega) **não estão funcionando**.
2. **Voz:** "Se eu pedir para falar e não tem a chave do OpenAI configurada… tem que dar um aviso certinho, na língua da pessoa: *para ouvir com voz natural, configure a sua chave do OpenAI nas Configurações*." Se falar sem API pela voz mecânica, beleza — mas o aviso tem que aparecer (ele viu um 401 cru).

## Decisões / diagnóstico

1. **Raiz do seletor no PDF:** os dois botões usavam `closest("p, h1..li")` — na camada de texto do pdf.js **não existe nenhum desses ancestrais** (só `<span>` posicionados) → as funções retornavam em silêncio, botão "morto". EPUB funcionava.
   **Fix:** novo `pdfParagraphSpanRange()` no Reader.tsx — detecta o parágrafo VISUAL pela **geometria das linhas**: agrupa spans por linha (top ≈) e marca fronteira de parágrafo quando há (1) mudança de tamanho de fonte, (2) espaço vertical extra, (3) indento de primeira linha ou (4) linha anterior terminando bem antes da margem direita. EPUB segue no `closest()` como antes.
2. **Raiz do 401/sem aviso:** `speakNeural` caía pra voz nativa **em silêncio** (só `console.warn`), e o aviso que existia era hardcoded em português e só pro caso "provedor ≠ OpenAI" (não cobria chave vazia nem chave inválida).
   **Fix:** `speakNeural` agora retorna `{ ok, status }`; Reader mostra `t("tts_neural_hint")` (nova chave, **12 idiomas**, 1× por sessão, mesmo `sessionStorage moka.ttsWarned`) quando (a) não há chave OpenAI configurada, ou (b) a API responde 400/401/403 (chave vazia/inválida/sem crédito). A voz **gratuita do dispositivo segue como fallback** (Miguel: "pelo mecânico beleza").

## Estado

- ✅ **ENTREGUE E NO AR:** commit `f42efbc` (push `000762e..f42efbc`, Vercel auto-deploy).
- ✅ tsc + `next build` verdes; backup `backups/moka_lab_pre_sel_tts_20260809/` (Reader.tsx + useTTS.ts + ui-strings.ts).
- ⏳ **Pendência:** teste real do Miguel (selecionar texto num PDF e tocar ⇤/¶; pedir leitura sem chave OpenAI). Browser-use segue bloqueado neste CLI (IAB não despacha cliques) — verificação ao vivo = chunk JS em produção.

## Limitação conhecida (registrada, não é bug)

PDFs **multi-coluna** ou com ordem de leitura estranha podem confundir o agrupamento por linhas (a heurística assume coluna única, o padrão dos livros do Moka). Antes o botão simplesmente não fazia nada em PDF — estritamente uma melhora.

## Próximos passos (missão cumprida; retomar daqui se voltar)

- Se o Miguel reportar parágrafo "comendo" linha ou parando curto em algum livro específico: ajustar thresholds em `isParaStart` (hoje: fonte ±20%, gap > 0.5h, indento > max(4px, 0.6h), linha curta > 1.2h antes da margem).
- Registrar bugs no `CEREBRO_NODE_BUGS_RESOLVIDOS.md`: `BUG-20260809-MOKA-SELETOR-PARAGRAFO-PDF` e `BUG-20260809-MOKA-TTS-SEM-CHAVE-401`.

---

## Adendo — Missão 4 do dia (~13:15): FORA o pop-up e o recadinho de "instalar o aplicativo" do /video (commit `a12f998`)

**Miguel (voz):** "esse recadinho de instalar… um pop-up embaixo… não quero mais isso. Quero que apareça uma janelinha depois que a gente subir o aplicativo — 'baixa o aplicativo' — mas vamos discutir."

**O que era:** resquícios da fase PWA (antes da decisão Play Store): (1) `InstallPrompt` — cartão embaixo da página /video ("Para usar o Moka Video, instale o aplicativo" + botão ⬇️ Instalar, feito na época em que "não passava por loja"); (2) `hero-install-note` no herói da mesma página ("📱 O Moka é um aplicativo: instale no seu aparelho — é grátis e não passa por loja" — ficaria FALSO com a ida pras lojas).

**Feito:** removidos os 2 usos em `apps/web/src/app/video/page.tsx` (import + `<InstallPrompt />` + `<p hero-install-note>`). O componente `InstallPrompt.tsx` fica DORMENTE no repo (reaproveitável); chave `video_install_note` segue no ui-strings (dormente). tsc+build verdes; deploy Vercel.

**📋 DECISÃO PENDENTE (Miguel quer discutir):** depois que o app estiver nas lojas (Play Store, sessão irmã Kimi K3), montar a janelinha "Baixe o aplicativo" — formato, gatilho e texto a combinar com ele ANTES de implementar.

---

## Adendo 2 — Missão 5 do dia (~13:40): fora o alerta cru "deepseek respondeu 401" na fala (commit `750f0d9`)

**Miguel (reporte):** ao selecionar texto e clicar em Falar, ainda aparecia "www.mokareader.com diz — deepseek respondeu 401:". **Não era o caminho do TTS** (corrigido na missão 3): com o idioma da FALA diferente do idioma do livro, o Moka TRADUZ PRIMEIRO usando a chave ativa (no caso dele, DeepSeek) — e essa chave respondeu 401; o erro cru subia pro `alert()` em `prepareSpeech` (Reader.tsx L182).

**Fix:** nova chave `reader_speech_translate_error` nos 12 idiomas ("🔊 Não consegui preparar a fala: a tradução falhou. Confira a sua chave de IA nas Configurações (⚙️) — ou escolha ouvir no idioma original do livro.") — a opção "📖 Original" do idioma da fala existe e dispensa IA. Erro cru fica só em `console.warn`. tsc+build verdes, deploy Vercel.

**⚠️ Aviso ao Miguel:** a chave DeepSeek ativa no cofre do navegador dele está sendo REJEITADA pela API (401 = chave inválida/vencida/revogada — DeepSeek usa 402 pra saldo). Ele precisa conferir/trocar em ⚙️ Configurações, ou ouvir no idioma original.

**Parentes conhecidos (NÃO corrigidos ainda, registrar pra próxima leva):** os mesmos erros crus aparecem inline em (1) painel fullscreen de tradução/explicação (`setFsResult`, Reader.tsx ~L712) e (2) overlay "Traduzir página" (`setPageTranslation`, ~L1091). Candidatos ao mesmo tratamento amigável.

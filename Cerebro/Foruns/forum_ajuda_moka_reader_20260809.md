# 📚 Fórum — Ajuda Moka Reader (índice-mãe do conhecimento do app)

> **Fórum-índice** que reúne TODO o conhecimento que temos sobre o Moka Reader — todos os fóruns, memórias, bugs, decisões e FAQ. É a base de conhecimento que alimenta o **Cérebro Moka** e o agente **Alan** (o robô de ajuda do app). Criado em 09/08/2026 a pedido do Miguel.
> Atualização: sempre que uma sprint do Moka termina (Regra 3 — Tema Duplo), este índice é atualizado.
> Irmão de arquitetura: `Foruns/forum_cerebro_moka_alan_agente_20260809.md` (o desenho do robô).

---

## 🧭 Para que serve este fórum

O Miguel pediu: *"crie um fórum, um fórum ajuda Moka Reader, em que você vai reunir todas as informações que a gente tem sobre o Moka Reader, todos os fóruns. Esse robô vai absorver as perguntas, ler os e-mails, procurar respostas. Vai ser um banco de soluções, instruções. Vai conversar com os clientes."*

Este fórum é o **ponto de entrada** — o índice navegável de tudo. O Cérebro Moka (agente Alan) lê daqui pra responder usuários.

---

## 📂 Todos os fóruns do Moka (cronológico)

### Fundação & arquitetura (20–22/07)
- `forum_moka_reader_20260720.md` — sprint "Páginas + Perguntas" (V 1.1→1.3): fundamentos do leitor.
- `forum_moka_video_implementacao_20260721.md` — Moka Video: primeiros passos, YouTube.
- `forum_moka_traducao_livro_volumes_20260721.md` — traduzir livro inteiro em volumes (~50 págs).
- `forum_moka_premium_20260722.md` — monetização (pré-pivô para gratuito).
- `forum_moka_monetizacao_unificacao_20260722.md` — unificação da estratégia de cobrança.
- `forum_moka_plano_de_negocios_20260722.md` — plano de negócios inicial.
- `forum_moka_pesquisa_ia_investimento_20260722.md` — pesquisa de IAs e investimento.
- `forum_moka_email_godaddy_20260722.md` — e-mail info@mokareader.com (GoDaddy).
- `forum_moka_campanha_socios_20260722.md` — campanha de sócios (dormente).
- `forum_moka_capacitor_app.md` — app móvel via Capacitor (abandonado em favor do TWA).

### Vídeo & transcrição (01/08)
- `forum_moka_video_transcricao_transkriptor_plano_v2_20260801.md` — motor Transkriptor (transcreve qualquer YouTube sem localhost).
- `forum_moka_modelo_casa_deepseek_v4_flash_20260801.md` — DeepSeek V4 Flash default; FIX crônico do menu que sumia.

### Pós-pivô gratuito (04–05/08)
- `forum_moka_fase_gratuita_byok_doacao_20260804.md` — pivô pra gratuito + BYOK + doação.
- `forum_moka_sprint_pos_pivot_552_57_20260805.md` — 6 decisões (modal portal, marketing "gratuito", tutorial "O que é API?", Entrar neutro, /auth/confirmado).

### Lojas & deploy (28/07, 07/08)
- `forum_duns_moka_lojas_20260728.md` — cadastro D-U-N-S pra Apple Developer.
- `forum_moka_twa_android_play_store_20260807.md` — TWA Android 5.7.1 (APK+AAB, keystore, assetlinks).

### Correções & sprints de polimento (08–09/08)
- `forum_moka_primeira_fase_publica_correcoes_20260808.md` — 1ª fase pública (sócios escondido, "experimental" fora, feedback elogio-first).
- `forum_moka_fix_slider_carregando_20260809.md` — slider de páginas travava em "Carregando…" (render race).
- `forum_moka_fix_seletor_pdf_aviso_tts_20260809.md` — seletor de parágrafo no PDF + aviso amigável de TTS sem chave.
- `forum_moka_pagina_configuracoes_20260809.md` — página própria /configuracoes + ranking integrado + fim do pop-up.

---

## 🧠 Nodos do Cérebro (Camada 2 — conhecimento indexado)

- **`CEREBRO_INDEX_MOKA_LOG.md`** — índice-mestre do Moka (48 seções: ficha de arquitetura, deploy, credenciais, sprint por sprint). **O documento mais importante.**
- **`CEREBRO_NODE_BUGS_RESOLVIDOS.md`** — histórico de bugs resolvidos (vários do Moka, ex.: menu-some, login-faixa-cortada, slider-render-race, seletor-PDF, TTS-401).
- **`CEREBRO_NODE_BUGS_ATIVOS.md`** — bugs em aberto (monitorar: TWA keystore path, login redirect Reader↔Video).
- **`CEREBRO_NODE_SPRINTS_ATIVOS.md`** — sprints ativos (bloco ☕ Moka no topo).

---

## ❓ FAQ atual do app (13 perguntas — `app/ajuda/page.tsx`)

Estas são as perguntas que o robô de ajuda offline (do `/ajuda`) já responde por palavras-chave. O Alan (com IA) deve **saber todas estas + poder ir além** (conversar, contextualizar):

1. O que é o Moka? 2. É grátis mesmo? 3. Quanto vou gastar com minha API? 4. Como consigo uma chave? 5. Vídeo usa a mesma chave? 6. O que é uma chave de API? 7. Qual IA devo escolher? 8. Minha chave fica segura? 9. Funciona em outros idiomas? 10. Preciso instalar? 11. Preciso criar conta? 12. Quem faz o Moka? (+ robô de dúvidas por tags)

---

## 🎯 Marketing & posicionamento (decisões vivas)

- **Gratuito + BYOK + doação** (pivô 04/08): o Moka não vende nada; a IA roda com a chave do usuário (centavos); doação PayPal/Pix no rodapé.
- **"Moka é gratuito ☕"** — sem "nesta fase" (ordem do Miguel 05/08).
- **Ranking de preços** como ferramenta de transparência (no `/ajuda` e agora no `/configuracoes`).
- **Tutorial `/tutorial`** com "O que é API?" + matemática de custo.
- **Lojas:** TWA Android pronto (Play Console pendente US$25); iOS depois (D-U-N-S OK).
- **Feedback elogio-first:** "Tem um elogio? Uma sugestão? Uma crítica? Achou um bug? Fale com a gente." (rodapé global).

---

## 📧 E-mails e canais de feedback (fontes que o Alan deve ler)

- **info@mokareader.com** — e-mail oficial (GoDaddy smtpout.secureserver.net). SMTP ativo desde 06/08 (no cofre `SMTP_MOKA_*`). **Pendente:** colar no Supabase Dashboard (auth emails).
- **Rodapé global** (mailto:info@) — feedback dos usuários.
- **Futuro:** formulário de contato / widget de chat (a definir com o Alan).

---

## 🔧 Estado atual do app (09/08/2026, versão 5.9)

- **Moka Reader:** EPUB/PDF com IA (traduz, explica, resume, fala), multi-idioma (12), BYOK.
- **Moka Video:** YouTube com legenda (grátis) ou Whisper (OpenAI, pago).
- **Página `/configuracoes`:** gerencia múltiplas chaves de IA + ranking (novo 09/08).
- **Deploy:** GitHub → Vercel (auto). Repo `migueldorosario1/moka`.
- **Pendências:** Grok+Groq no registry (2ª leva); conta Play Console; teste visual do Miguel.

---

## 🔄 Como este fórum se mantém vivo

1. Toda sprint do Moka termina com Tema Duplo (Regra 3) — o fórum novo é adicionado à lista acima.
2. Bugs resolvidos/ativos são refletidos aqui (link pros nodos).
3. O Alan (quando ativo) sugere atualizações quando aprende algo novo com usuários.
4. Renovação segue o ciclo do `MONITORAMENTO_DE_TRABALHO.md` (48h).

---

*Próximo passo: ler `forum_cerebro_moka_alan_agente_20260809.md` — o desenho da arquitetura do Cérebro Moka e do agente Alan.*

---

## 🧩 Decisão de produto pendente (09/08) — ecossistema de voz neural

Miguel levantou: *"se eu peço para falar um texto em inglês, quem vai traduzir? O tradutor pode ser o DeepSeek e quem fala pode ser o OpenAI, ou pode ser o mesmo. A gente pode travar: se quiser voz neural, o OpenAI traduz E fala, pra ficar um ecossistema sólido."*

**Opções:**
1. **Status quo:** tradutor = IA ativa; falante neural = OpenAI (só se ativa). Tradução e fala podem ser de provedores diferentes.
2. **Ecossistema OpenAI (ideia do Miguel):** quando o usuário quer voz neural, o OpenAI faz a tradução E a fala (mesma chave, mesmo provedor) — mais consistente.
3. **Híbrido:** o usuário escolhe nas Configurações se, ao usar voz neural, prefere que o OpenAI cuide de tudo ou mantém o tradutor ativo.

**Status:** 📐 A DECIDIR com o Miguel. O Alan (robô de ajuda) deve saber explicar isto quando o usuário perguntar "por que a voz neural só funciona com OpenAI?".

---

## 🧩 Decisão de produto (09/08, esclarecida) — voz neural multi-provedor

Miguel esclareceu: **não é só OpenAI**. *"A gente pode configurar OpenAI, Grok com K, os que têm voz neural. A gente configura o Grok com K pra fazer transcrição de vídeo e também pra ouvir. Porque também tem o [microfone]."*

**Esclarecido:**
- **Voz neural** (TTS) — hoje só OpenAI ativa no Moka. **Decisão:** adicionar **Grok (xAI)** e **Groq** também (ambos têm TTS). O usuário escolhe qual provedor faz a voz neural.
- **Grok com K** — para: voz neural (TTS) + transcrição de vídeo + escuta (microfone/reconhecimento de voz). Miguel quer poder travar o Grok pra essas funções.
- **Microfone** (reconhecimento de voz, "Pergunte qualquer coisa") — hoje usa `useSpeechRecognition` (nativo do navegador). Miguel mencionou que o Grok também pode fazer isso.

**Status:** 📐 **2ª leva** — adicionar Grok+Groq ao registry + estender a decisão de TTS (openai/grok/groq) + allowlist `/api/tts` + llm-prices. Registrado; construção quando crédito renovar.

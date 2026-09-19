# ☕ Fórum — Moka 6.0: reforma /configuracoes + Grok/Groq + fim FOUC + propaganda neutra (09/08/2026)

> Tema Duplo da missão 12 do dia 09/08 (sessão ZCode GLM-5.2 — Kimi/Qwen esgotaram 🔴🔴).
> Irmão técnico: `Memorias/memoria_moka_6_reforma_config_20260809.md`.
> Commit: `7405d65` (7 arquivos, +970/−806).

## O que o Miguel pediu (voz, resumo)

*"Refaz tudo nas configurações, tá bagunçado. Clica em configurações, flash desconfigurado, depois entra. Tem um link 'configurações' dentro — loop. Onde o botão de adicionar outra chave? 'Escolha como o Moka lê em voz alta' não aparece. Tira propaganda do OpenAI — só explica que algumas servem (OpenAI, Grok, etc.). Grok tem voz também em oral? Bota o OpenAI e Grok — as melhores vozes. Vídeo sem legenda é a mesma chave, mas pode usar uma pra transcrever e outra pra voz. Tem que ter botão adicionar nova chave. Quando adiciono minha chave sai, fica só o botão da IA pra testar."*

## Decisões (confirmadas via AskUserQuestion)
- Escopo: **TUDO numa leva** (mesmo no limite de crédito GLM-5.2).
- Organização: **lista no topo + form escondido atrás de botão**.

## Pesquisa: Grok tem voz neural? SIM ✅
[xAI Grok STT/TTS](https://x.ai/news/grok-stt-and-tts-apis): 5 vozes, 20+ línguas, $15/1M caracteres; STT 25+ línguas. [Vapi/humannessindex](https://humannessindex.vapi.ai/models/grok-tts). Groq também tem TTS + Whisper.

## O que foi entregue (commit `7405d65`)

### 1. Grok (xAI) + Groq como provedores (`registry.ts`)
- 8→10 provedores. `grok`: baseUrl `api.x.ai/v1`, model `grok-3-mini`, adapter openai. `groq`: `api.groq.com/openai/v1`, `llama-3.3-70b-versatile`. Ambos OpenAI-compatible.

### 2. TTS estendido (`Reader.tsx`)
- `providerId === "openai"` → `["openai","grok","groq"].includes()` via helper `getNeuralTtsConfig(config)`.
- `getNeuralTtsConfig`: retorna `{baseUrl, apiKey, model:"tts-1", voice:"nova"}` ou null; baseUrl dinâmico (config do usuário ou preset).
- Detecção de TTS inativo estendida: `hasInactiveTts` (OpenAI **OU** Grok **OU** Groq no cofre mas não ativos).

### 3. Allowlist `/api/tts/route.ts`
- Adicionado `api.x.ai`, `api.groq.com` ao `TTS_HOSTS` (anti-SSRF).

### 4. Ranking atualizado (`llm-prices.ts`)
- 15→17 modelos: Grok 3 mini (xAI, $0.30/$0.50), Llama 3.3 70B (Groq, $0.59/$0.79). + Grok STT na transcrição ($0.30/h).

### 5. /configuracoes REORGANIZADA (`SettingsForm.tsx`)
- **Lista de chaves no TOPO** — primeira coisa que aparece; cada card com testar/usar/editar/remover.
- **Botão "+ Adicionar nova chave"** (`cfg_add_key`) que abre form limpo (`handleAddNew`: zera editingId/apiKey/label/model/baseUrl/providerId).
- **Formulário escondido** atrás de estado `showForm` (default false). `handleEdit` abre preenchido; `handleSave` fecha e volta pra lista.
- **TIRADO o quicknav** (`<nav class="settings-quicknav">`) — era o "loop configurações dentro de configurações".

### 6. Propaganda neutra (`ui-strings.ts` ×12)
- `keys3_voice`: "chave OpenAI — é a 'voz perfeita'" → "algumas IAs servem (OpenAI, Grok, etc.)".
- `keys3_same`: "A MESMA chave OpenAI" → "Você pode usar a mesma chave... ou separar (OpenAI, Grok, etc.)".
- "voz perfeita"/"perfect voice"/equivalentes **eliminados dos 12 idiomas**.
- Textos hardcoded PT do Whisper (`L798/L825`) → i18n (`cfg_whisper_saved/removed/valid/testing`).

### 7. Cura FOUC (`globals.css`)
- 734 linhas de CSS migradas dos 2 `<style jsx>` do SettingsForm → `globals.css`. O CSS agora carrega com o layout raiz (não em runtime), acabando o "flash desconfigurado" ao abrir `/configuracoes`.

## Estado
- ✅ **ENTREGUE E NO AR:** commit `7405d65` (push `93ac844..7405d65`), Vercel auto-deploy. tsc + build verdes.
- ✅ 8→10 provedores; voz neural aceita OpenAI/Grok/Groq; ranking com 17 modelos; `/configuracoes` reorganizada (lista + botão adicionar + sem loop + sem flash).
- ⏳ **Pendência:** teste do Miguel (adicionar Grok/Groq; ver a lista no topo; confirmar que o flash sumiu; confirmar que "voz perfeita" virou neutro).

## Próximos passos (registrados, não executados)
- Adicionar voz neural **diferenciada** por provedor (Grok tem 5 vozes próprias; Groq usa modelos diferentes).
- Permitir escolher **chaves separadas** pra voz neural vs transcrição (Miguel: "pode usar uma pra transcrever vídeo e outra pra voz neural").
- Alan (robô de ajuda) — 2ª leva (decisões pendentes).

---

## 📋 Adendo — pedido das 3 caixas padronizadas + "Testar todas" (Miguel, ~21:00)

Miguel pediu uma reorganização das seções de IA nas configurações:

**Problema atual:** a seção de vídeo/transcrição está com diagramação diferente da de texto; não há caixa separada pra fala neural; tudo misturado.

**Pedido:**
1. **3 caixas padronizadas** (mesmo visual), uma pra cada função:
   - 📖 **Texto** (livro/tradução/explicação) — qualquer IA do ranking
   - 🎬 **Vídeo + transcrição** (microfone 🎤 Whisper/STT) — OpenAI, Grok, Groq
   - 🔊 **Fala neural** (TTS — voz natural) — OpenAI, Grok, Groq (as que têm TTS)
2. Cada caixa tem: ícone, título, campo de chave, botão testar.
3. **Botão "Testar todas"** no final — testa todas as LLMs cadastradas e dá um **relatório com sinal verde ✅ (OK) / vermelho ❌ (falhou)**.
4. Padronizar: as caixas de vídeo e fala têm que ter o MESMO visual da caixa de texto (hoje estão diferentes).

**Status:** 📐 A PLANEJAR — próxima leva (reforma de UX das configurações). Registrar quando o Miguel pedir pra executar.

---

## 📋 Adendo 2 — pedidos pendentes do Miguel (~21:30)

1. **Botão fechar/voltar na página /configuracoes:** hoje não tem um botão explícito pra fechar a página de configurações e voltar de onde veio. Precisa de um "✕" ou "← Voltar" no topo.

2. **Título real do livro (não nome do arquivo):** quando o usuário sobe um PDF/EPUB, o Moka mostra o nome do arquivo como título. O Miguel quer que ele **leia o título real** de dentro do livro (metadata do EPUB, ou primeira página do PDF) e mostre como título principal — "fica bonito, título do livro embaixo de cada livro" na estante.

**Status:** 📐 A PLANEJAR — próxima leva. O parser (packages/parser) provavelmente já extrai metadata do EPUB; ver se tá sendo usado na estante.

---

## 📋 Adendo 3 — Reforma completa das configurações (Miguel, ~23:00)

O Miguel passou uma reformulação grande da página de configurações. Registrando TUDO pra próxima leva:

### 1. Ranking → página própria `/ranking`
- Tirar o ranking de dentro de `/configuracoes` e `/ajuda`.
- Criar página `/ranking` dedicada, com **gráfico** de evolução de preços (usando o histórico que o agente já acumula).
- Colunas: resumir livro, traduzir livro, **resumir vídeo** (nova), transcrever vídeo.

### 2. Configurações — 3 blocos separados (menu de qual chave usar)
- **📖 Livro** (leitura/tradução/explicação) — qualquer IA. Menu dropdown das chaves cadastradas.
- **🎬 Vídeo + transcrição** (Whisper/STT) — OpenAI, Grok, Groq. Menu dropdown.
- **🔊 Fala neural** (TTS) — OpenAI, Grok, Groq (só os que têm TTS). Menu dropdown.
- Cada bloco tem um **menuzinho** que lista as chaves já cadastradas — a pessoa escolhe qual usar pra cada função.
- Evitar redundância: as chaves ficam numa lista no topo; os 3 blocos só selecionam qual chave usar.

### 3. Botões separados: Testar + Salvar + Atualizar
- **Testar** (testa a chave sem salvar)
- **Salvar** (salva no cofre)
- **Atualizar** (renova/testa a chave cadastrada)
- Campo **procurar modelo** (lista de modelos do provedor)
- Cada um com função distinta (hoje "Atualizar" salva + testa junto — Miguel quer separado).

### 4. Footer e Header NÃO fixos
- O footer (Moka gratuito, PayPal, Pix) e o cabeçalho NÃO devem ficar "presos" (fixos/sticky).
- Devem rolar com a página (sóbem e descem com o conteúdo).

### 5. Bug Mistral
- defaultModel trocado de `mistral-small-latest` → `mistral-large-latest` (mais disponível).
- Se persistir, investigar se a chave do Miguel tem permissão pra esse modelo.

### 6. Ordem das seções na /configuracoes
1. Acessibilidade (tema + fonte) — fica
2. **Chaves de IA** (lista + adicionar, com Testar/Salvar/Atualizar/Modelo separados)
3. **3 blocos de função** (livro/vídeo/fala — cada um com menu dropdown de qual chave)
4. **Idiomas** (interface/tradução/áudio) — vai pro FINAL (depois dos blocos)
5. Vídeo/Whisper (integrado nos 3 blocos, não separado)

**Status:** 📐 A PLANEJAR — é a maior reforma da /configuracoes. Construção quando crédito renovar (Kimi/Qwen). Prioridade alta.

---

## 📋 Adendo 4 — Voz neural completa + fluxo de adicionar (Miguel, ~23:30)

### 1. Preferência de voz (radios + teste + escolher voz)
- **Quadradinho (radio):** "Voz neural (OpenAI/Grok)" vs "Voz mecânica gratuita".
- **Botão testar:** a pessoa escuta um exemplo da voz (toca um áudio curto).
- **Escolher voz:** dropdown com as vozes do OpenAI: alloy, echo, fable, onyx, **nova** (atual), shimmer (+ ash, ballad, coral, sage nas mais novas). Pesquisa confirmou: são **6-13 vozes**, todas multilíngues. Link: https://developers.openai.com/api/docs/guides/text-to-speech
- Persistir a escolha da voz (hoje é hardcoded "nova").

### 2. Fluxo de adicionar chave (Miguel insistiu: junto do Atualizar)
- **Botões separados:** Salvar + Testar (não juntos).
- **Campo Modelo** com botãozinho **Procurar 🔍** que lista os modelos do provedor (usa a chave pra buscar `/models`).
- Cada LLM tem sua lista de modelos própria.
- **Adicionar nova chave** junto do Atualizar (não separado embaixo).
- Resumo do fluxo que o Miguel quer: cola chave → Procurar modelo (🔍 lista) → escolhe modelo → **Salvar** (salva no cofre) + **Testar** (testa separado).

### Status
Tudo 📐 A PLANEJAR — reforma grande da /configuracoes. Construção quando crédito renovar (Kimi/Qwen). Prioridade alta — é a reforma principal pendente.

### Vozes disponíveis por provedor (pesquisa 09/08)

**OpenAI TTS (tts-1/tts-1-hd):** 6 vozes clássicas + 7 novas = até 13.
- Clássicas: **alloy** (neutra), **echo** (masculina quente), **fable** (narrativa), **onyx** (masculina grave), **nova** (feminina clara — atual do Moka), **shimmer** (feminina brilhante).
- Novas: ash, ballad, coral, sage.
- Multilíngues. Demo: openai.fm. Docs: developers.openai.com/api/docs/guides/text-to-speech

**Grok (xAI) TTS:** 5 originais + 21 novas = **26 vozes**.
- Originais: **ara** (quente/conversacional), **eve** (energética), **leo** (autoritária), **rex** (profissional), **sal** (neutra).
- Novas (jul/2026): Lumen, Castor, Naksh, Atlas, Carina, Zagan, Helix, Orion, Luna, Wellness Support, + 11 outras.
- 25+ idiomas, speech tags inline (tom, pausas, sussurro, riso).
- Preço: ~$0.08/min. Docs: docs.x.ai/developers/model-capabilities/audio/text-to-speech

**Groq:** TTS (inglês/árabe) + **Whisper** (transcrição de áudio/vídeo). $0.042/hora (mais barato pra transcrever).
- Groq é o MELHOR pra transcrição de vídeo (mais barato + rápido).

### Bloco de transcrição de vídeo (3º bloco)
- Opções: OpenAI Whisper, **Groq Whisper** (mais barato), **Grok STT** ($0.10/h batch).
- O Miguel quer poder escolher qual provedor transcreve o vídeo (separado da voz neural e do livro).

---

## 📋 Adendo 5 — Reforma UX final das configurações (Miguel, ~00:00 10/08)

O Miguel passou uma série de mudanças na /configuracoes. Todas registradas:

### 1. Modelo JUNTO do campo de chave (não separado)
- O campo de modelo (com lupa 🔍 de procurar) tem que ficar **logo abaixo do campo da chave**, não numa seção separada.
- A lupa 🔍 tem que **funcionar** (hoje não acha porque o modelo velho foi descontinuado — corrigir a busca).

### 2. Bloco de idioma da interface → pra BAIXO
- Jogar o bloco "idioma da interface / traduções / áudio falado" **lá pra baixo** na página (depois das chaves e voz).

### 3. Link do ranking nas configurações + na home
- Colocar um **link pro ranking** dentro das configurações (não o ranking inline, só um link).
- Colocar o link do ranking **no menu da home** também.

### 4. TIRAR o bloco de "Vídeo & Transcrição" (Whisper separado)
- O Miguel decidiu: não precisa mais da seção separada de vídeo/Whisper.
- O OpenAI entra como modelo normal com checkbox "usar pra voz neural".
- Mesma coisa Grok. Simplificação.

### 5. Escutar a voz (testar antes de escolher)
- Na preferência de voz, a pessoa deve poder **escutar um exemplo** de cada voz antes de escolher.
- Botão "▶ Escutar" que toca uma amostra da voz selecionada.

### Status
Tudo 📐 A EXECUTAR. Prioridade: modelo junto da chave + tirar bloco vídeo + idiomas pra baixo (são CSS/estrutura). Escutar voz é mais complexo (gerar áudio de amostra).

---

## 📋 Adendo 6 — CHECKBOXES POR FUNÇÃO (mix de IAs) — IDEIA GENIAL do Miguel

O Miguel quer que cada chave cadastrada tenha **3 checkboxes** indicando pra que função serve:

### Os 3 checkboxes (por chave):
1. ☑️ **Tradução/Explicação** (texto do livro) — qualquer IA do cofre
2. ☑️ **Transcrição** (vídeo sem legenda) — só OpenAI/Grok/Groq (têm Whisper)
3. ☑️ **Voz neural** (falar em voz alta) — só OpenAI/Grok/Groq (têm TTS)

### Como funcionaria:
- A pessoa cadastra DeepSeek → marca ☑️ Tradução
- Cadastra OpenAI → marca ☑️ Voz neural + ☑️ Transcrição
- Cadastra Grok → marca ☑️ Voz neural (outra voz)
- **O Moka usa cada IA na função certa automaticamente!**
- Traduz com DeepSeek (barato), fala com OpenAI (voz natural), transcreve vídeo com Groq

### Implementação:
- Cada `VaultEntry` precisa de 3 campos: `useForText`, `useForVideo`, `useForVoice`
- O Reader/Video consulta qual entry tem `useForText=true` pra traduzir
- O TTS consulta qual entry tem `useForVoice=true` pra falar
- O vídeo consulta qual entry tem `useForVideo=true` pra transcrever
- Se mais de uma marcada pra mesma função, usa a ativa ou a primeira marcada

### Regras de bloqueio:
- Voz neural: só OpenAI/Grok/Groq (checkbox bloqueado pros outros)
- Transcrição: só OpenAI/Grok/Groq (checkbox bloqueado pros outros)
- Tradução: todos podem (checkbox sempre habilitado)

**Status:** 📐 A PLANEJAR — é a evolução natural da config. Prioridade alta depois do upload nas lojas.

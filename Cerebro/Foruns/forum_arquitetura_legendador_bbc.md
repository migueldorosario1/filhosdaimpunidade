# Fórum: Arquitetura do Agente Legendador de Vídeo (BBC com Faixa Preta)

## Objetivo
Criar um script ou agente autônomo (`agente_legendador_de_video.py`) que automatize a extração, tradução e embutimento de legendas padrão BBC em vídeos (frequentemente advindos do X/Twitter ou YouTube). 

A grande inovação arquitetural exigida pelo Miguel é que **a legenda não pode sobrepor o conteúdo original do vídeo**. Para isso, o agente deve adicionar uma "faixa preta" na parte inferior do vídeo e queimar as legendas estritamente dentro dessa faixa.

## Link de Referência para Teste
- [https://x.com/FurkanGozukara/status/2056511723708813333](https://x.com/FurkanGozukara/status/2056511723708813333)

## Arquitetura Proposta (Pipeline)

1. **Download do Vídeo:** 
   - Utilizar `yt-dlp` para baixar o vídeo da URL fornecida (ex: Twitter).
2. **Extração e Transcrição de Áudio:** 
   - Extrair o áudio e usar uma API (ex: Whisper ou Grok) para transcrever a fala original.
3. **Tradução e Padronização (Padrão BBC):** 
   - Usar um LLM para traduzir o SRT resultante para o Português do Brasil.
   - Formatar as legendas no Padrão BBC (máximo 2 linhas, máximo de ~37-42 caracteres por linha, para legibilidade no celular).
4. **Composição FFMPEG (O Segredo da Faixa Preta):**
   - Utilizar o filtro `pad` do FFMPEG para estender o canvas de vídeo para baixo (ex: `pad=iw:ih+250:0:0:black`).
   - Usar o motor de renderização de legendas (`subtitles` ou libass) garantindo que a margem vertical (`MarginV`) posicione a legenda exatamente na nova faixa preta criada.
   - Padrão BBC: Texto amarelo (`PrimaryColour=&H0000FFFF`), fundo opaco preto (`BackColour=&H00000000`, `BorderStyle=4`), fonte Roboto.

## Status Atual
O modelo inicial do script (`root/agente_legendador_de_video.py`) foi criado no Antigravity, mas o processo de encodar via libx264/ffmpeg pode demorar e carece de otimização de parâmetros de hardware, assincronismo e refinamento de design responsivo. A tarefa foi repassada para refinamento no DeepSeek/Codex.

## 2026-05-19 06:23 BRT — Parecer Codex no tick operacional

Leitura de coordenação: Claude assumiu a frente no canal às 06:08 BRT e depois reconheceu que a implementação real mais robusta já estava em `root/codex/codex_agente_legendador_de_video.py`. No workspace deste tick, o path citado originalmente (`root/agente_legendador_de_video.py`) não existe; há apenas `root/__pycache__/agente_legendador_de_video.cpython-310.pyc`, então o próximo registro precisa alinhar o path canônico antes de qualquer uso por outro agente.

Verificação local Codex, sem deploy e sem chamada paga:

- `python3 -m py_compile root/codex/codex_agente_legendador_de_video.py`: exit 0.
- Smoke sintético com `ffmpeg` e fonte `DejaVu Sans`: exit 0.
- Saída: `scratch/codex/legendador_bbc/tick_0615_synthetic_check/video-sintetico_legendado_bbc.mp4` (`4192743` bytes).
- Relatório: `scratch/codex/legendador_bbc/tick_0615_synthetic_check/relatorio.json`, com `1280x720 -> 1280x885` e faixa preta de `165px`.

Parecer consultivo:

- DeepSeek: não promover para uso operacional antes de resolver path canônico, chunking de tradução, fonte e dependências/custos; recomendou teste com vídeo próprio/domínio autorizado.
- Kimi: convergiu; riscos bloqueantes para deploy são path divergente, tradução sem chunking, fonte Roboto ausente, custo/chaves/rate limit e direitos de download/uso de X/YouTube.

Decisão Codex neste tick: manter como protótipo local em `root/codex/`, com Claude testando em diretório isolado. Não mover para `root/`, não cronar, não publicar e não usar material de terceiros automaticamente. Próximo passo técnico seguro: Claude finalizar o teste isolado; depois abrir patch pequeno para chunking e documentação de dependências/custos, com path canônico decidido no canal.

## 2026-05-19 07:18 BRT — Comparativo gerou artefatos, mas MP4s novos precisam ser descartados/validar baseline

Leitura Codex do tick `20260519_070618`: o canal mostrou que Claude iniciou às 06:27 um comparativo em paralelo entre três scripts (`root/codex/codex_agente_legendador_de_video.py`, `root/ds_agente_legendador_bbc.py` e `root/claude/claude_agente_legendador_de_video.py`). Às 07:06 os processos já não estavam rodando.

Evidência local:

- `saida/codex_20260519_062548/legenda_original.srt`: `7748` bytes.
- `saida/codex_20260519_062548/legenda_pt_bbc.srt`: `8216` bytes, SRT em PT-BR normalizado em duas linhas.
- `saida/deepseek/legenda_original.srt`: `7748` bytes.
- `saida/deepseek/legenda_pt.srt`: `6096` bytes.
- `saida/claude_v2_20260519_062546.log`: tradução em chunks começou, mas registrou `Chunk 1/2 vazio/inválido; mantendo original`; não encontrei MP4 final dessa execução.
- `saida/codex_20260519_062548/codex_video_legendado_bbc.mp4` e `saida/deepseek/legendador_bbc/video_legendado_bbc.mp4`: existem e cresceram até ~07:08, mas `ffprobe` retorna `moov atom not found`. Tratar como arquivos incompletos/não publicáveis.
- Baselines anteriores válidos continuam existindo: `saida/codex/legendador_bbc/final/codex_video_legendado_bbc_faixa_preta.mp4` (`ffprobe`: `1920x1328`, `322.322s`) e `saida/deepseek/video_legendado_bbc.mp4` (`ffprobe`: `1920x1330`, `322.355367s`).

Parecer consultivo deste tick:

- Kimi: congelar a geração; MP4 sem `moov` é arquivo quebrado e não publicável; documentar a regressão e isolar caminhos.
- DeepSeek: status amarelo; parar/reter o pipeline atual, reportar e aguardar autorização antes de qualquer correção operacional.

Decisão Codex: não rodar novo encode, não promover script para path canônico, não publicar MP4, não cronar e não mover nada para `/root` produtivo. Próximo passo seguro é revisão offline do motivo dos MP4s novos ficarem sem `moov` e escolha explícita de baseline/script canônico antes de qualquer novo teste com material externo.

## 2026-05-19 08:16 BRT — Correção do status dos MP4s do comparativo

Reverifiquei os artefatos depois do registro de Claude no canal às 07:18 BRT. A leitura anterior de `moov atom not found` era um retrato durante/antes da finalização completa dos arquivos; neste tick, `ffprobe` valida os MP4s novos:

- `saida/deepseek/legendador_bbc/video_legendado_bbc.mp4`: `1920x1244`, `322.410s`, `158358780` bytes.
- `saida/codex_20260519_062548/codex_video_legendado_bbc.mp4`: `1920x1328`, `322.433s`, `171580642` bytes.
- `saida/claude_v2_20260519_062546/claude_video_legendado_bbc.mp4`: `1920x1328`, `322.433s`, `171612125` bytes.
- Baselines também seguem válidos: `saida/codex/legendador_bbc/final/codex_video_legendado_bbc_faixa_preta.mp4` e `saida/deepseek/video_legendado_bbc.mp4`.

Concordo com o ranking técnico de Claude neste ponto: DeepSeek venceu o comparativo atual por tradução PT-BR mais natural, arquivo final menor e faixa preta mais discreta (`164px`). Codex ficou funcional, mas com tradução mais mecânica e faixa maior (`248px`). Claude gerou MP4 válido, mas a tentativa de chunking manteve trechos em inglês, então não é candidato.

Decisão Codex: ainda não promover para path canônico nem cronar/publicar. O próximo patch seguro é offline/local: escolher explicitamente o script base DeepSeek ou fundir a tradução DeepSeek com os controles CLI/relatório do script Codex, adicionar espera/checagem de finalização antes de `ffprobe`, e documentar dependências/custos/direitos de uso antes de qualquer teste operacional novo.

---

## Execução Trindade 2026-05-19 — 3 versões + veredito Miguel + manual destilado

**Fórum-mãe deste sprint.** Toda Trindade lê AQUI primeiro antes de mexer no script. Versão canônica do Cérebro: `CEREBRO_NODE_GOVERNANCA.md` §72.

### 1. Os 3 scripts versionados (com prefixo + dir próprio)

- `root/codex/codex_agente_legendador_de_video.py` — 509 linhas, argparse, ASS nativo, normalização BBC textwrap
- `root/ds_agente_legendador_bbc.py` — ~400 linhas, mais simples, sem argparse mas funcional
- `root/claude/claude_agente_legendador_de_video.py` — cópia Codex + patch chunks (chunks falharam, ver §72.2)

### 2. Os 3 outputs em `saida/`

| Output | Tamanho | Canvas | Faixa preta |
|---|---|---|---|
| `saida/codex_20260519_062548/codex_video_legendado_bbc.mp4` | 164 MB | 1920×1328 | 248px |
| `saida/deepseek/legendador_bbc/video_legendado_bbc.mp4` | 151 MB | 1920×1244 | 164px |
| `saida/claude_v2_20260519_062546/claude_video_legendado_bbc.mp4` | 164 MB | 1920×1328 | 248px |

### 3. Veredito visual Miguel (autoridade final)

| Posição | Quem | Bom | Ruim |
|---|---|---|---|
| 🥇 1º | **Codex** | tamanho legenda padrão BBC; ritmo bom | "Little Pete"→"pezinho" |
| 🥈 2º | **Claude** | tamanho/padrão bom; ritmo bom depois do começo | tradução em inglês (chunks falharam); cue 1 truncada |
| 🥉 3º | **DeepSeek** | tradução PT-BR mais natural | legenda pequena; ritmo confuso |

**Lição-mãe:** legenda é UX visual em vídeo + áudio + tempo. **Forma > conteúdo refinado** quando a forma compromete leitura.

### 4. Tasks por agente — preencher experiência no Cérebro

Cada agente, **ao próximo tick**, ir direto a `CEREBRO_NODE_GOVERNANCA.md` §72 e preencher sua sub-seção:

- **Codex** → §72.3 preenchida em 2026-05-19 10:09 BRT (decisões arquiteturais, bug truncamento `quebrar_linhas_bbc`, lições e validação)
- **DeepSeek** → §72.4 preenchida em 2026-05-19 10:30 BRT (faixa 164px, fonte pequena, agrupamento de timestamps, prompt e lições)
- **Antigravity** → §72.5 (esqueleto original 67 linhas, `BorderStyle=4`, o que ficou de fora)

Formato: Acertos · Erros · Dificuldades · Lições · Assinatura BRT.

**Claude já preencheu §72.2** com 4 erros admitidos.

### 5. Manual destilado §72.8 (a consolidar — versão preliminar Claude)

**Checklist canônico passo-a-passo:**
1. Deps: `yt-dlp`, `ffmpeg`, `ffprobe`, fonte (DejaVu Sans local; Roboto no Tencent)
2. Chaves: `GROQ_API_KEY`, `DEEPSEEK_API_KEY` em `.env.unificado`
3. Work_dir isolado: `saida/<agente>_<timestamp>/`
4. Download: `yt-dlp -f bv*+ba/b --merge-output-format mp4`
5. Áudio: `ffmpeg -vn -acodec pcm_s16le -ar 16000 -ac 1` (16kHz mono pra Whisper)
6. Transcrição: Groq `whisper-large-v3` + `verbose_json`
7. Tradução: DeepSeek-V4-Pro **SRT INTEIRO** (NÃO chunk!) + temperature=0.1 + max_tokens=12000
8. Normalizar BBC: 40-45 chars/linha, máx 2 linhas, **dividir cue longa em sub-cues** (NÃO truncar)
9. Gerar `.ass`: `Style BBC,fonte,size,&H0000FFFF amarelo,&H00000000 preto,BorderStyle=4ou3,Alignment=2,MarginV=bar//2`
10. FFMPEG: `pad=iw:ih+bar:0:0:black,subtitles='path\\:escapado'` com `bar=max(200, int(height*0.20))` (mín 200, NÃO 164)
11. Encode: `-c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart`
12. **Pedir humano (Miguel) ver vídeo** antes de declarar pronto
13. Pontuar no canal + relatorio.json

**Anti-padrões (NÃO fazer):**
- ❌ Fragmentar SRT em chunks pra DeepSeek-V4-Pro (rejeita contexto isolado)
- ❌ `textwrap.wrap()` com truncate silencioso (descarta texto)
- ❌ Faixa preta < 200px em vídeo 1080p (legenda fica ilegível mobile)
- ❌ Cravar ranking de vídeo por chars/MB (UX > dados)
- ❌ Patchar API LLM no 1º erro (retry primeiro — flakey)

**Convencao de output (Miguel 19/05):** `Outros/Videos legendados FFmeg/{llm}/{YYYY-MM-DD}/{tema}.mp4`

**Prompt validado com adendo (a refinar pela Trindade):** "Traduza SRT pra PT-BR jornalístico. Preserve numeração, timestamps EXATAMENTE. Máx 2 linhas / ~40 chars. **Preserve nomes próprios e siglas como no original (entre aspas se preciso)**. Retorne SÓ o SRT, sem markdown."

**Custo estimado** por vídeo de 5min: ~$0.11 (Groq Whisper $0.10 + DeepSeek tradução $0.005 + FFMPEG CPU tempo).

### 6. Bugs a corrigir antes de virar canônico

1. **`quebrar_linhas_bbc()` descarta texto** quando cue > 80 chars. Fix: dividir cue em sub-cues com timestamp proporcional.
2. **"Little Pete" → "pezinho"** (Codex tradução): adicionar "preserve nomes próprios" no prompt.
3. **DS ritmo confuso**: investigar — faixa 164px com fonte proporcional ficou pequena; cue de 10s mal sincronizada.
4. **DeepSeek-V4-Pro flakey em chunks**: nunca fragmentar SRT.

### 7. Próximos passos (Trindade decidir)

1. Cada agente preenche §72.X do Cérebro com sua experiência
2. Codex 🥇 consolida `root/agente_legendador_bbc.py` canônico (sem prefixo)
3. Patches §6.1+§6.2 aplicados
4. Re-teste no mesmo vídeo + Miguel valida visualmente
5. Documentar em `CLAUDE.md` Pilar Vídeo §3 quando estável
6. Cron pra processamento automatizado de vídeos via Telegram (futuro)

## 2026-05-21 15:37 BRT — Codex: vídeo Cuba e regra nova de idioma antes da transcrição

Miguel pediu legendagem do vídeo local `Outros/pautas editoriais o cafezinho/2026 Mai 21/video cuba/WhatsApp Video 2026-05-21 at 15.05.49.mp4`.

Entrega:

- Saída final: `Outros/pautas editoriais o cafezinho/2026 Mai 21/video cuba/video_cuba_legendado_bbc.mp4`
- Workdir: `Outros/pautas editoriais o cafezinho/2026 Mai 21/video cuba/codex_legendador_bbc/`
- Comando reutilizável criado: `Outros/pautas editoriais o cafezinho/2026 Mai 21/video cuba/codex_legendar_bbc.sh`
- Canvas final: `480x1062`; vídeo original era `480x864`, sem distorção, com faixa preta inferior de `198px`.
- Validação: `ffprobe` OK, zero blocos SRT com duração zero, prévias visuais em `preview_24s.jpg` e `preview_119s.jpg`.

Correção estrutural aplicada em `root/codex/codex_agente_legendador_de_video.py`:

1. **Idioma antes da transcrição completa:** novo fluxo `--source-language auto` extrai amostra curta (`audio_probe_idioma.wav`), detecta idioma com Whisper/Groq e grava `idioma_detectado.json` antes da transcrição integral.
2. **Normalização de idioma:** Whisper/Groq pode retornar nomes como `spanish`; o script agora normaliza para código aceito pela API (`es`, `pt`, `en`, etc.).
3. **Retomada por SRT existente:** novo argumento `--input-srt` permite reaproveitar transcrição já feita e pular nova chamada de transcrição.
4. **Fallback de tradução:** `--translation-model openai:gpt-4o-mini` habilitado; DeepSeek mantém suporte, mas com timeout menor e fallback para não travar vídeos urgentes.
5. **Fonte responsiva:** cálculo de fonte agora considera largura do vídeo, evitando legenda grande demais em vídeos estreitos de WhatsApp.

Lição operacional: para vídeos em qualquer idioma, a ordem canônica passa a ser **detectar idioma primeiro**, registrar a detecção, transcrever já com código de idioma, traduzir para PT-BR, normalizar BBC e só então queimar legenda na faixa preta.

Assinado: Codex Maestro, 2026-05-21 15:37 BRT.

## 2026-05-21 15:41 BRT — Ajuste de sincronia vídeo Cuba

Miguel reportou que as legendas começavam ligeiramente antes das falas. Refeito o render com atraso global de +650ms nas legendas, sem alterar proporção nem conteúdo visual do vídeo.

Arquivos preservados para rollback:

- `video_cuba_legendado_bbc.pre_sync_1540.mp4`
- `codex_legendador_bbc/legenda_pt_bbc.pre_sync_1540.srt`

Entrega atualizada:

- `video_cuba_legendado_bbc.mp4`
- `codex_legendar_bbc.sh` agora inclui `--subtitle-offset-ms 650` e `--line-width 24`.

Validação: `ffprobe` OK (`480x1062`), zero blocos com duração zero, preview visual `codex_legendador_bbc/preview_sync_24s.jpg`.

Assinado: Codex Maestro, 2026-05-21 15:41 BRT.

## 2026-05-21 15:44 BRT — Correção final: intro musical antes da fala

Miguel apontou que a legenda ainda entrava durante a música/vinheta inicial. Diagnóstico: o ASR colocou a primeira fala em `00:00:00`, mas o vídeo começa com tela "The Blond House" e música. Portanto o problema não era um descasamento pequeno; era offset de introdução.

Ação: refeito o render a partir do SRT pré-sync com offset global de `+3400ms`. O comando `codex_legendar_bbc.sh` foi atualizado para `--subtitle-offset-ms 3400`.

Validação visual: frame em `2.5s` ainda sem legenda durante a vinheta; frame em `4.0s` já mostra o personagem falando e a primeira legenda. Canvas mantido `480x1062`, sem distorção.

Assinado: Codex Maestro, 2026-05-21 15:44 BRT.

## 2026-05-21 15:47 BRT — Correção localizada, sem deslocar o resto

Miguel corrigiu a leitura anterior: o corpo do vídeo estava sincronizado; o problema era apenas a legenda inicial aparecendo durante a música/vinheta.

Ação final: revertido o deslocamento global. O SRT atual parte de `legenda_pt_bbc.pre_sync_1540.srt`; apenas os blocos 1 e 2 foram reposicionados para `03.400-05.700` e `05.700-07.100`. Do bloco 3 em diante, os timestamps voltaram ao SRT anterior.

Validação visual: `preview_localfix_2.5s.jpg` sem legenda na vinheta, `preview_localfix_4.0s.jpg` com primeira fala e legenda, `preview_localfix_24.0s.jpg` preservando sincronia do corpo. Comando `codex_legendar_bbc.sh` voltou para `--subtitle-offset-ms 0` para não reproduzir o erro de deslocamento global.

Assinado: Codex Maestro, 2026-05-21 15:47 BRT.

## 2026-05-21 15:53 BRT — Refeito do zero: separar vinheta musical da fala

Miguel rejeitou corretamente as tentativas anteriores: o problema não era deslocamento global da legenda, e sim ASR confundindo a vinheta/música inicial com fala.

Ação correta executada:

1. Criado novo workdir limpo: `video cuba/codex_legendador_bbc_refeito/`.
2. Extraído áudio a partir de `3.20s`: `audio_fala_sem_intro.wav`.
3. Transcrição nova com Whisper/OpenAI em espanhol, já sem a música inicial.
4. Os timestamps da transcrição foram recolocados no tempo original somando `+3.20s`.
5. Tradução nova para PT-BR, sem reaproveitar o SRT anterior.
6. Render novo com faixa preta menor (`180px`), fonte `30`, margens laterais `18`, `MarginV=62`, aproveitando melhor a largura do vídeo vertical.

Validação visual:

- `preview_2.5s.jpg`: vinheta sem legenda.
- `preview_4.3s.jpg`: personagem falando com primeira legenda.
- `preview_24.0s.jpg` e `preview_58.0s.jpg`: corpo do vídeo com legenda mais larga e melhor posicionada.

Saída final: `video cuba/video_cuba_legendado_bbc.mp4` (`480x1044`, sem distorção).

## 2026-07-04 20:25 BRT — Antigravity: Legendagem de J.D. Vance com Fallback Whisper e Correção de Tradução SRT

Miguel solicitou o processamento do vídeo de J.D. Vance (`OopsGuess-2072992702833254486-01.mp4`) seguindo a estética canônica da BBC (legenda amarela na faixa preta inferior, máximo de 40 caracteres por linha, 2 linhas por cue).

### Ações e Ajustes Executados:
1. **Hardening de API Keys:** Corrigimos a função `carregar_env()` no script `root/codex/codex_agente_legendador_de_video.py` para priorizar a leitura do arquivo `.env.unificado` ativo localizado em `Projeto Cafezinho Agentes/root/.env.unificado`, evitando que chaves de API antigas ou expiradas sobrescrevessem a chave ativa de produção.
2. **Fallback OpenAI Whisper:** O pipeline de transcrição agora tenta usar a API do Groq e, caso ocorra falha de autenticação ou rate limit, realiza o fallback transparente para o endpoint do OpenAI Whisper (`whisper-1` / `verbose_json`).
3. **Hardening de Tradução (Alinhamento Temporal):** Identificamos que o prompt de tradução anterior forçava a quebra de linhas a 40 caracteres diretamente no LLM, o que fazia com que modelos como `gpt-4o-mini` quebrassem ou inventassem novos blocos SRT (mudando a quantidade de 12 blocos originais para 33 blocos e gerando timestamps inválidos que corrompiam a sincronia e o final do vídeo). Atualizamos os prompts de tradução para ordenar que o LLM mantenha a exata estrutura de blocos e timestamps originais. A quebra de linhas para o limite BBC foi delegada inteiramente para a função interna de normalização em Python (`normalizar_bbc_srt`).
4. **Renderização e Entrega:**
   - **Vídeo de Entrada:** `OopsGuess-2072992702833254486-01.mp4` (78.9 segundos, 1920x1080).
   - **Vídeo de Saída:** `jdvance_legendado_bbc.mp4` (1920x1328, adicionada faixa preta inferior de 248 pixels para embutir as legendas amarelas sem obstruir a imagem).
   - **Local de Entrega:** `/home/migueldorosario/Downloads/Antigravity Google/Outros/pautas editoriais o cafezinho/2026 Jul 03/jdvance/jdvance_legendado_bbc.mp4`

### Validação:
- Verificado via `ffprobe` com sucesso, confirmando resolução e duração corretas, com ausência de quaisquer erros de encoding ou metadados quebrados.

Assinado: Antigravity, 2026-07-04 20:25 BRT.


Lição canônica: em vídeo com vinheta/música antes da fala, **não corrigir com offset global depois**. Primeiro localizar o início real da fala, cortar a vinheta para a transcrição, e só então somar o offset ao SRT final.

Assinado: Codex Maestro, 2026-05-21 15:53 BRT.

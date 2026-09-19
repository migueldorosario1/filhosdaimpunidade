# 🎬 IDEIA_PRO_DSNUVEM_IDEIAS-010 — ANÁLISE DE VIABILIDADE: ESTEIRA DE CORTES DA LIVE DIÁRIA DO MIGUEL (Jornal da Fórum, TV Fórum, 20h-22h → 2 cortes/dia no carrossel da home)

> **Bloco:** ZM 02/09/2026 18:40 BRT (commit ec27789ea) — ordem do Miguel por voz ~18:2x (sessão ZM us65), fiel: "manda lá pro DSN Ideias explicar o contexto todo, fala pra ele fazer análise". **ADENDO ZM 18:55 BRT (commit 7dc0dfe8a):** alvo confirmado + relógio aprovado + dados novos da casa — incorporado nesta análise.
> **Arquiteto:** DS Nuvem Ideias (DS-N Ideias) · ronda 18:43-18:56 de 02/09/2026 (Tencent, 30/30).
> **Base de leitura:** `cerebro/Foruns/forum_carrossel_videos_miguel_captacao_automatica_20260902.md` v2 + adendo §1.5 (arquitetura da ZM — analiso, não repito o desenho).
> **Companion:** IDEIA-009 (`Foruns/ideias/2026-09-02_video_vertical_espelho_reels.md`) = o carrossel da home.
> **Escopo:** SÓ esta esteira de vídeo (o Miguel mandou deixar as demais novidades quietas). Nada publica no canônico; Fase 1 = espelho. **EU NÃO EXECUTO NADA** (Lei de Poderes): este arquivo é desenho; execução é do ZM sob ✓ do Miguel.
> **Marcador de conclusão:** `PRONTO_ANALISE_CORTES_LIVE`

---

## 1. Resumo executivo (o veredito)

**Viável e BARATO — a casa já tem quase tudo para este canal exato.** O adendo da ZM (18:55) destravou os 2 maiores riscos que eu ia apontar:
- **Transcrição NÃO é gargalo:** Transkriptor faz 2h de vídeo ≈ **5 min** (103k chars na edição 2h08 — validado em produção; fallback S3/Whisper existe). O relógio 22h30-22h40 de transcrição da ZM **se confirma** — SLA 23h folgado. (Meu receio inicial de whisper 1,2× = 2,4h pós-live cai: whisper vira fallback, não caminho principal.)
- **Achador da edição do dia JÁ EXISTE:** modo `--jornal` do `youtube_cafezinho.py` (cron `30 22`/`0 23`), juiz LLM em cascata (DeepSeek→AssemblyAI→Kimi), validado ~6 semanas — a esteira **herda** o achador e a armadilha conhecida (premiere renomeada com "|" pós-ar) já tem solução em produção.
- **Porta residencial já patrulha TV Fórum** (E2E 17/08) e o **teste Kakay de verticalização foi com vídeo DESTE programa** (`Od9sKT0q_Qk`) — ffmpeg 9:16 blur+legenda provado no alvo exato.

**O que realmente falta desenhar (riscos que sobram):**
1. **Gravação da live em tempo real** (modo novo na porta Dell — hoje live ativa → `AGUARDANDO_VOD`) + **watchdog** (se o yt-dlp morre 20h40, ninguém sabe até 22h) + **SLA degradado se a Dell cair/desligar** (a porta mora no Dell — IP residencial, único que passa no bloqueio; limitação documentada "fila anda quando o Dell estiver ligado").
2. **Transporte Dell→Tencent:** o MP4 de 2h NÃO precisa sair do Dell todo dia — só o áudio p/ transcrição (ou transcrição direto na Dell?) + 2 janelas de ~90 s depois de decididos os cortes. Decidir com medição de uplink na Fase 0 (pergunta ao executor; ver §7).
3. **Detecção da palavra-sinal com falso-positivo baixo** ("CORTA!" dita naturalmente) — normalização + regra de frase-curta + 🔥 como disjuntor + calibração na Fase 1 com preview.
4. **Gate "sinal publica DIRETO" × regra da casa "só CL/CM publica"** (ZM-041) — conteúdo autoral do próprio Miguel é o caso mais simples, mas quero o "sim" escrito dele (P4 §6).
5. **Capa do corte:** cat 28 fora da caça (ZM-042) → `thumbnail_oficial_video` gerada do frame no ffmpeg (não depender de caça).

**Custo:** whisper/transcrição = Transkriptor já pago/rotina da casa (E2E 17/08: 16 min → US$ 0,098); sem chave nova, sem compra. ffmpeg local. Storage WP ~2 × 7 MB/dia ≈ 420 MB/mês (validar host).

---

## 2. A decisão do Miguel (registro fiel — contexto NOVO de hoje, ignora decisões antigas)

1. Live diária no YouTube, **20h-22h**; robô baixa a live e pega os pontos importantes.
2. **Sinal do corte = palavra FALADA ao vivo** ("eu falo uma palavra e aí você bate") → transcrição com carimbos de tempo → cada ocorrência = 1 candidato. **Sinal publica DIRETO** (a palavra dele É a escolha editorial). Fallback sem sinal: LLM escolhe 2 momentos, marcados "auto".
3. **2 cortes/dia**: corte 1 às **23h** (mesma noite, quente) · corte 2 às **08h** (manhã seguinte, fresquinho). **Relógio APROVADO pelo Miguel (~18:50).**
4. Destino: **carrossel da home, 2º bloco** — ajuste da ZM: `<video>` self-hosted na biblioteca do WP (não iframe YT), para não vazar público pro YouTube.
5. **Alvo CONFIRMADO:** TV Fórum (`@forumrevista`, channel ID `UC3sMBA3BdnsKSVI0WB9yVWQ`, ~982 mil inscritos), playlist/programa **"Jornal da Fórum"** (âncora Miguel do Rosário).
6. Palavra-senha a confirmar (candidata "CORTA!"); 🔥 no Telegram = sinal paralelo opcional. **Único item ainda aberto com o Miguel.**

---

## 3. Pesquisa no Cérebro — o que JÁ EXISTE para este alvo (verificado nesta ronda)

### 3.1 Para o canal exato (TV Fórum / Jornal da Fórum) — adendo ZM §1.5
- **Achador `--jornal`** do `youtube_cafezinho.py` (cron `30 22`/`0 23`): acha a edição diária do Jornal há ~6 semanas; juiz LLM em cascata (DeepSeek→AssemblyAI→Kimi) distingue o Jornal das outras lives longas (Fórum 11:30, Fórum Café, Brocou, Trilhas da Urna, Fórum Livre). **Certeza 10, validado em produção.**
- **Armadilha conhecida:** TV Fórum agenda o Jornal como premiere "Jornal da Fórum dd.mm.yy" e **renomeia p/ manchete com "|"** depois do ar → casar por título+data só vale na janela; o juiz resolve. A esteira **herda** o achador (não reinventar).
- **Transcrição 2h ≈ 5 min** (Transkriptor; fallback S3/Whisper) → 103k chars, ~22h30-22h40. SLA 23h ok.
- **Porta residencial patrulha TV Fórum** (E2E 17/08: 16 min → 13.032 chars, US$ 0,098).
- **Banco de nomes da TV Fórum** (evita errar nome nos títulos).
- **Teste Kakay = vídeo deste programa** (`Od9sKT0q_Qk`): 9:16 fundo blur + legenda assada ponta a ponta.

### 3.2 Infraestrutura geral da casa
- **Porta yt-dlp no Dell** (IP residencial — único que passa no bloqueio do YouTube; Tencent/NYC testados 31/08 → "Sign in to confirm you're not a bot"). Porta burra, cérebro na Tencent. Live ativa hoje → `AGUARDANDO_VOD` (modo gravar-live é NOVO). Fila DS YouTube via SSH no clone da Tencent (git do Dell divergente 397×465). Limitação: fila anda quando o Dell está ligado.
- **Whisper large-v3-turbo local na Tencent** (DSC-028): custo zero, pré-aquecido no boot, RAM 1,7 GB, ~1,2× o tempo do áudio. Fallback AssemblyAI/Transkriptor na esteira DS YouTube.
- **ffmpeg 9:16 provado:** 1080×1920 blur + legenda libass (bug PlayResY=288 / MarginV≤100 documentado) + loudnorm, <60 s ~7 MB.
- **WP:** biblioteca de mídia servindo vídeo público ✅ (Reels); cat 28 + `thumbnail_oficial_video` (ZM-042: vídeos fora da caça); `post_status=future` padrão; GA4 mede permanência.

---

## 4. Análise pedida (a)-(d) — viabilidade, riscos, lacunas

### (a) SLA 23h com 1 h de folga pós-live (22h→23h)
**Folgado — com o dado real da casa (Transkriptor 2h ≈ 5 min), o relógio da ZM se confirma:** fim 22h → transcrição ~22h30-22h40 (Transkriptor; whisper só fallback) → detecção + corte ~22h40-22h50 → upload/agenda ~22h50-23h00 → **23h no ar**. Folga real de ~20-30 min.
- **Risco que sobra: não é transcrição, é a GRAVAÇÃO.** Se a Dell não gravou a live (desligada/caiu/yt-dlp morreu), não há MP4 local → cai no VOD (imprevisível) → corte 1 escorrega ou morre. Mitigações: watchdog na Dell (cron 5 min: processo vivo + arquivo crescendo; senão reinicia e avisa no Telegram) + SLA degradado declarado (corte 1 → 23h30/00h00 com aviso, ou só o corte 2 das 08h) + teste de 1 live real na Fase 0.
- **Recomendação:** não depender de transcrição incremental whisper como caminho principal (complexidade desnecessária) — Transkriptor pós-live resolve. Whisper incremental fica como **opção** se a ZM quiser decidir os cortes ANTES das 22h30 (só vale se o sinal veio na 1ª hora; benefício marginal).

### (b) Gravação em tempo real (Dell) vs esperar VOD
**Gravar em tempo real é o caminho certo** (VOD de live é imprevisível; casa já trata `AGUARDANDO_VOD` como fallback). yt-dlp grava live em URL ao vivo pela porta do Dell (IP residencial). Riscos e mitigações:
- **R1 — Dell fora 20h-22h:** sem gravação → VOD (SLA degradado + aviso 19h55 "hoje sem corte 23h salvo VOD"). Regime, não bug — não há 2ª porta (Tencent/NYC bloqueados). Miguel decide a tolerância (P3).
- **R2 — yt-dlp morre no meio:** watchdog 5 min reinicia (`--live-from-start` se o formato permitir; senão perda parcial avisada).
- **R3 — formato:** gravar .ts/.mkv e remuxar p/ MP4 no fecho (22h, 1-2 min).
- **Reversibilidade:** gravação é leitura pura do YouTube (como a porta já faz); zero efeito no site. Fase 0 = 1 live real de teste.

### (c) Detecção da palavra-sinal na transcrição com timestamps
**Caminho:** a transcrição do Transkriptor (com timestamps) chega ~22h30; varredura busca a palavra-senha **normalizada** (minúsculas, sem pontuação, variantes). Cada ocorrência = candidato {timestamp}. Regras propostas:
- **Frase-curta/ênfase** (palavra sozinha ou frase ≤ 4-6 palavras) — reduz falso positivo de "corta pra mim"/"corta isso"; calibrar na Fase 1 com preview no relatório.
- **Janela mínima entre sinais** (ex.: 10 min); 2+ sinais → os 2 primeiros = cortes do dia; sobras em banco p/ redes.
- 0 sinais → fallback LLM escolhe 2 momentos (tese forte/frase de efeito), marcados **"auto"**; 1ª semana com ✓ opcional no Telegram.
- 🔥 no Telegram durante a live = mesmo efeito (disjuntor manual à prova de erro de transcrição).
- **Custo:** Transkriptor rotina da casa (E2E 17/08 US$ 0,098/16 min); whisper local zero como fallback. Sem chave nova.

### (d) Onde processa — Dell baixa/grava, Tencent corta
**Sim — divisão certa** (Dell = única porta; Tencent = cérebro com whisper/ffmpeg/WP/loops). O detalhe em aberto é o **tráfego Dell→Tencent** e a divisão exata de tarefas:
- **Opção 1 (mínima, recomendada):** Dell grava + extrai áudio → Tencent transcreve (Transkriptor roda onde? — validar: se o Transkriptor roda na Tencent, mandar só o áudio de 2h ~150-250 MB; se roda no Dell, nem isso) → cortes decididos na Tencent → Dell extrai as 2 janelas (~90 s cada) e manda → Tencent monta 9:16 + publica. Tráfego diário: ~200 MB (áudio) + ~15 MB (janelas), não 1-2 GB.
- **Opção 2 (simplicidade máxima):** Dell manda o MP4 de 2 h inteiro (1-2 GB) via scp noturno — simples, mas depende do uplink residencial e pode atrasar o corte 1. Medir uplink na Fase 0 e decidir com número.
- **Por que não montar o 9:16 na Dell:** a Dell é a porta burra por desenho; todo o ferramental de prova (legenda, WP, agenda, GA4) vive na Tencent; o git do Dell nem sincroniza (divergência estrutural). **Decisão: Dell burra (grava + fatia), Tencent cérebro.**

---

## 5. Lacunas do desenho v2 (o que falta fechar antes da Fase 1)

- **L1 — transporte do vídeo Dell→Tencent:** não especificado no fórum. Resposta recomendada: áudio p/ transcrição + 2 janelas de corte (Opção 1); medir uplink na Fase 0 (Opção 2 como alternativa simples).
- **L2 — Dell fora do ar na janela 20h-22h:** sem fallback de gravação (bloqueio de IP). SLA degradado + aviso. Regime, não bug.
- **L3 — heartbeat da gravação:** watchdog na Dell (processo + arquivo crescendo a cada 5 min; reinicia; avisa). Sem isso o corte 1 das 23h morre calado às 20h40.
- **L4 — gate "só CL/CM publica" vs "sinal publica DIRETO":** o Miguel decidiu o mérito (sinal = escolha editorial dele), mas a casa tem rito de Consenso Duplo (ZM-041). Conteúdo autoral do próprio Miguel = caso mais simples; preciso do "sim" escrito dele para a fórmula: **palavra-sinal = autorização editorial; gate técnico automatizado (template aprovado 1×); veto no relatório do dia seguinte** (ver P4 §6).
- **L5 — capa do corte:** cat 28 fora da caça (ZM-042) → `thumbnail_oficial_video` gerada do próprio frame no ffmpeg (não depender de caça nem capa manual).
- **L6 — storage/banda do self-hosted:** 2 × ~7 MB/dia ≈ 420 MB/mês + banda no espelho e depois canônico. Validar plano do host; poda automática (manter últimos N dias no site, arquivo frio fora) decidir na Fase 2.
- **L7 — ajuste `<video>` self-hosted no carrossel (IDEIA-009 §6):** a esteira depende desse ajuste existir no espelho (2º bloco). Dependência explícita de execução (ZM).
- **L8 — título do corte:** LLM na Tencent com padrão da casa + banco de nomes da TV Fórum; template aprovado pelo Miguel na Fase 1.

---

## 6. Perguntas / confirmações que preciso do Miguel (destravam Fase 0)

- **P1 — URL/playlist da live:** ✅ RESOLVIDO (TV Fórum `UC3sMBA3BdnsKSVI0WB9yVWQ`, Jornal da Fórum; playlist ID mecânico na Fase 0 via porta Dell — herda o achador `--jornal`).
- **P2 — palavra-senha (ÚNICO item aberto):** confirma "CORTA!"? Sugiro **frase-sinal rara** (ex.: "CORTA AQUI!") ou palavra + 🔥 — menos falso positivo; registrar variantes aceitas no config.
- **P3 — relógio:** ✅ APROVADO (23h/08h). Falta só: tolerância a SLA degradado se a Dell cair (corte 1 → 23h30/00h com aviso, ou pular pro 08h?).
- **P4 — gate do conteúdo DELE:** "sinal publica direto" = autorização editorial dele para furar a fila do Consenso Duplo, com gate técnico automatizado (template aprovado 1×) + veto no relatório do dia seguinte? **(Recomendo SIM — conteúdo autoral dele; quero o "sim" escrito.)**
- **P5 — storage/banda:** ok manter 2 vídeos/dia (~420 MB/mês) acumulando no site (poda opcional na Fase 2)?

---

## 7. Arquitetura refinada (relógio com herança do achador) — para o executor

```
~19h55  Dell: pré-checagem (Dell viva? cron ok?) — se não, aviso "hoje sem gravação salvo VOD"
20h00   Dell: yt-dlp grava a live em tempo real (.ts/.mkv local) — modo NOVO (hoje: AGUARDANDO_VOD)
20h05-  Dell: watchdog 5 min (processo vivo + arquivo crescendo; senão reinicia/avisa)
22h00   Dell: remuxa MP4 local (1-2 min) · herda o achador --jornal (já roda 22:30/23:00 p/ confirmar edição)
22h30-  Tencent: transcrição com timestamps (Transkriptor 2h≈5min; whisper/AssemblyAI fallback)
22h40   Tencent: varredura da palavra-sinal → candidatos; sinais (até 2) ou fallback LLM ("auto")
22h45   Dell: ffmpeg -ss/-to extrai as 2 janelas (~20s antes + 30-90s + fecho de frase) → Tencent
22h50   Tencent: monta 9:16 (blur fundo + legenda assada libass MarginV≤100 + loudnorm, <10MB)
        + thumbnail_oficial_video do frame + upload biblioteca WP (rito backup→prova→registro)
        + post cat 28 (título LLM + banco de nomes TV Fórum) + meta + AGENDA: corte1 23h · corte2 08h
23h00   🔴 CORTE 1 NO AR (carrossel 2º bloco, <video> self-hosted)
08h00   🔴 CORTE 2 NO AR
08h05   Relatório Telegram: links + trecho da transcrição de cada + flag auto/sinal + veto do Miguel
```

**Componentes:** (1) porta Dell modo live + watchdog; (2) herança do achador `--jornal`; (3) transcrição (Transkriptor — onde roda a validar) + varredor de palavra-sinal; (4) fatiador de vídeo na Dell (ffmpeg -ss/-to); (5) montador 9:16 + gerador de thumbnail; (6) publicador WP (upload + post cat 28 + agenda future); (7) relatório Telegram. Onde roda: 1/2/4 na **Dell** · 3/5/6/7 na **Tencent** (cérebro).

---

## 8. Plano de execução (passos numerados, riscos, reversibilidade — protocolo da casa: backup → prova → registro → rollback escrito)

> Executor = ZM (runtime). Eu (DS-N) fico no desenho/refino. Nada é executado sem ✓ do Miguel nas P2-P5.

1. **Fase 0 — destravamento (só Miguel):** palavra-senha (P2) · tolerância SLA degradado (P3) · ✓ gate P4 · ✓ storage P5.
2. **Fase 0 técnica — provas de conceito (espelho, nada no ar):**
   2.1 Gravar 1 live real em tempo real pela porta Dell (modo live novo; backup do fetcher atual — `.bak_pre_live_20260902`), conferir remux .ts→MP4 e tamanho. [reversível: volta ao modo AGUARDANDO_VOD]
   2.2 Medir uplink Dell→Tencent (bloco de áudio de 10 min e janela de 90 s de vídeo) — decide Opção 1 vs 2 (§4d). [reversível: leitura]
   2.3 Transcrever 1 bloco/edição (Transkriptor) e conferir timestamps + varredura da palavra de teste. [reversível: leitura]
   2.4 Montar 1 corte 9:16 de teste (blur + legenda + <10 MB) + gerar `thumbnail_oficial_video` do frame. [reversível: arquivo local]
   2.5 Ajuste `<video>` self-hosted no carrossel do espelho (IDEIA-009 §6) — dependência da esteira. [rito casa: backup mu-plugin → prova HTTP → rollback escrito]
3. **Fase 1 — espelho (1ª semana, após ✓ das provas):** esteira completa apontada pro `cafezinho.news`; 2 cortes/dia; relatório Telegram; GA4 baseline; calibração da palavra-sinal (preview + veto); template de título aprovado pelo Miguel. [risco: corte torto/falso positivo — preview e veto; reversível: desligar esteira + remover agendados (1 comando)]
4. **Fase 2 — canônico:** portar pro `ocafezinho.com` após validação visual dele (rito espelho → canônico).
5. **Fase 3 — redes:** mesmos MP4 alimentam Reels IG/FB, Shorts, TikTok, X (grava 1×, publica em tudo).
6. **Registro:** cada fase registra no canal DS YouTube/ponte com prova (MP4, thumb, ID do post, REST) + ledger. Rollback escrito de cada mudança.

**Riscos principais (com dono):** Dell fora 20h-22h (regime — SLA degradado + aviso; dono: Miguel decide tolerância) · falso positivo da palavra (calibração Fase 1; dono: DS-N/ZM) · Transkriptor atrasa (fallback whisper/AssemblyAI; dono: ZM) · WP storage (P5; dono: ZM/Miguel) · carrossel ainda com iframe (dependência IDEIA-009; dono: ZM).

---

## 9. Rascunhos (DENTRO deste arquivo — nunca em produção; executor adapta)

### 9.1 Varredura da palavra-sinal (pseudo — Tencent)
```python
# varredura_transcricao.py — roda pós-transcrição (Transkriptor com timestamps); NÃO é produção
PALAVRA = "corta aqui"          # P2 com o Miguel; normalizar (caixa, pontuação, variantes)
def normaliza(t): return t.lower().replace("!", "").replace(",", "").strip()
def achar_sinais(transcricao):  # transcricao = segmentos [{start, texto}] em segundos da live
    sinais = []
    for seg in transcricao:
        fala = normaliza(seg["texto"])
        if PALAVRA in fala and len(fala.split()) <= 6:   # frase-curta = heurística anti-falso-positivo
            sinais.append({"ts": seg["start"], "texto": seg["texto"]})
    return sinais
# janela mínima entre sinais: 600 s; 2+ → 2 primeiros; 0 → fallback LLM ("auto")
```

### 9.2 Fatia das janelas na Dell (comando conceitual)
```bash
# na Dell, sobre o MP4 local da live (fecho 22h); janela = ~20s antes do ts da palavra
ffmpeg -ss <ts_sinal-20> -t 90 -i live_20260902.mp4 -c copy janela_1.mp4   # montagem 9:16 na Tencent
# thumb do frame (na Tencent, após montar o 9:16):
ffmpeg -ss 5 -i corte_9x16.mp4 -frames:v 1 thumbnail_oficial_video.jpg
```

### 9.3 Watchdog de gravação (Dell — cron 5 min)
```bash
# gravação viva? arquivo crescendo? senão: reinicia yt-dlp (--live-from-start se possível) e avisa Telegram
```

---

## 10. O que preciso do Miguel (síntese curta)
**P2 palavra-senha** (único item aberto do alvo) · **P3 tolerância** se a Dell cair (corte 1 atrasa ou pula?) · **✓ P4 gate** ("sinal publica direto" = autorização editorial dele com gate técnico automatizado + veto no relatório) · **✓ P5 storage**. Com isso, a ZM executa a Fase 0 técnica (provas no espelho — gravação live, uplink, corte 9:16, ajuste do carrossel) e eu refino a calibração da palavra na Fase 1. Nada publica sem o ✓.

*Análise do DS Nuvem Ideias (DS-N Ideias) — arquiteto de brainstorms da casa O Cafezinho · 02/09/2026.*

`PRONTO_ANALISE_CORTES_LIVE`

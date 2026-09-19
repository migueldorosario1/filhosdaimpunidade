# 🎬 IDEIA_PRO_DSNUVEM_IDEIAS-011 — PLANO REALISTA DE EXECUÇÃO: ESTREIA HOJE (~23h) DOS CORTES DA LIVE DO MIGUEL NO ESPELHO (com a voz DELE)

**Data:** 02/09/2026 · **Bloco:** IDEIA_PRO_DSNUVEM_IDEIAS-011 (ZM 19:25, ordem do Miguel ~19:1x por voz) · **Evolui:** IDEIA-010 (`2026-09-02_esteira_cortes_live_diaria_miguel_analise.md`, 18:54) · **Companions:** fórum `forum_carrossel_videos_miguel_captacao_automatica_20260902.md` (v2) · `ZM-20260902-RECORD-001` (ordem ao DS-Dell, de_dell.md 19:27) · IDEIA-009 §6 (carrossel `<video>` self-hosted) · **Marcador:** `PRONTO_PLANO_CORTES_REALISTA`

> Escopo (ZM 19:25): plano REALISTA de execução pra HOJE, por etapa com SLA e plano B, costurando as responsabilidades da noite. Nada publica no canônico; Fase 1 = espelho (`cafezinho.news`). Entreguei análise de viabilidade na 010; este arquivo é o plano de campo.

---

## 0. O requisito NOVO (muda o seletor da 010)

**O corte tem que ser do MIGUEL falando (âncora), não de convidado.** Ordens do Miguel (fiel, ZM 19:25): *"pega a parte mais interessante que EU FALO — você tem que reconhecer minha voz, pega só trecho meu falando"*.

- **Camada 1 (HOJE):** filtro de falante PELA TRANSCRIÇÃO com timecode. A casa já distingue apresentador × convidado pela transcrição (Miguel/Glauco/Süssekind/Janine detectados sozinhos; Miguel = abre o programa, comenta entre blocos, encerra). A entrada do juiz `--jornal` pode ajudar a rotular.
- **Camada 2 (v2, não hoje):** diarização por impressão de voz (pyannote/resemblyzer; referência = edições anteriores guardadas).
- A palavra-senha ("CORTA!", ainda NÃO confirmada) continua como prioridade **quando for ele falando**.

---

## 1. Definição de pronto da noite

1. **Corte 1 no ar ~23h** no espelho `cafezinho.news` (carrossel 2º bloco, `<video>` self-hosted, vertical 9:16 com blur + legenda amarela assada, cat 28, `thumbnail_oficial_video`), trecho do **Miguel falando**.
2. **Corte 2 às 08h** do dia seguinte (mesmo material, agendado).
3. Tolerância do Miguel (resposta ao meu P3, via ZM): **"o ideal é HOJE, pior caso amanhã"** — se a Dell cair, o corte desliza pro 08h (default aplicado salvo veto).
4. Estreia no ESPELHO = laboratório (resposta ao meu P5): storage crítico só quando for pro canônico.

---

## 2. Divisão de responsabilidades da noite (costura)

| Quem | Papel na noite | Já ordenado? |
|---|---|---|
| **DS-Dell** | Grava a live 20h-22h (yt-dlp, única porta que passa no bloqueio YT) · watchdog 5min · entrega **áudio completo + janelas ~90s cortadas NA DELL** (~15MB) · guarda o MP4 de 2h por 7 dias · plano B = VOD | ✅ `ZM-RECORD-001` (de_dell.md 19:27) |
| **DS-N Ideias (eu)** | **Este plano** (costura) + seletor/critérios do corte + checkpoints da noite + planos B | este arquivo |
| **Tencent (cérebro)** | Recebe áudio → transcrição com timecode → seletor (falante + senha/LLM) → pede janelas → monta 9:16 + thumb → entrega MP4 pro ZM | via este plano (executor ZM) |
| **ZM** | Sobe o carrossel no espelho (ajuste `<video>` da IDEIA-009 §6 — precisa existir até ~22h50) · sobe o MP4 na biblioteca de mídia do WP do espelho · publica/agenda · validação visual | própria ordem (fórum/ponte) |
| **CL/CM** | Fora do publish de HOJE (espelho = laboratório do dono; conteúdo autoral do próprio Miguel; regra ZM-041: canônico segue Consenso Duplo, espelho não) | — |

---

## 3. O relógio da noite (etapas com SLA e plano B)

| Hora | Etapa | Dono | SLA | Plano B |
|---|---|---|---|---|
| **19h55** | Pré-checagem: Dell viva? yt-dlp ok? espaço? Resolve a URL da live (`@forumrevista/live`) | DS-Dell | 5 min | Se Dell fora → aviso no Telegram "hoje sem gravação salvo VOD" (regime, não bug) |
| **20h00** | **Início da gravação em tempo real** (yt-dlp na live; Jornal da Fórum entra como premiere "Jornal da Fórum 02.09.26"; pós-ar renomeia p/ manchete com "|" — achador `--jornal` conhece) | DS-Dell | 20h00 em ponto | VOD quando sair (fluxo AGUARDANDO_VOD); corte desliza |
| **20h05→22h00** | **Watchdog 5min** (processo vivo + arquivo crescendo; se cair: religa + avisa) — risco P1 da minha 010 | DS-Dell | cada 5 min | Perda parcial avisada; `--live-from-start` se o formato permitir |
| **22h00** | Live acaba → remux MP4 (1-2min) + **extrai áudio completo** (mp3/opus ~64-128kbps ≈ 60-120MB) | DS-Dell | 22h05 | Se gravação falhou → VOD (ver linha 19h55) |
| **22h05-22h10** | **Transporte Dell→Tencent: só o áudio** (achado da 010: NÃO mandar o MP4 de 2h) | DS-Dell | ~1-3 min (uplink 10-50Mbps) | Se uplink lento: transcrever na Dell e mandar só o JSON com timestamps (pequeno) |
| **22h10-22h20** | **Transcrição com timestamps palavra-a-palavra** (Transkriptor 2h≈5min, validado na casa, US$ 0,098; AssemblyAI word-timestamps + `speaker_labels` como alternativa) | Tencent | 22h20 | Whisper local (~1,2× o áudio → ~2h20) SÓ se o corte 1 deslizar p/ 01h/08h; legendas auto do YT = bônus se o VOD publicar cedo |
| **22h20-22h35** | **SELETOR** (ver §4): rótulo de falante (L1) → candidatos (senha falada por ELE | LLM escolhe momentos DELE, marcados "auto") → fecha corte em frase completa → timestamps início/fim | Tencent | 0 sinais + 0 auto com confiança → escolhe 2 mesmo assim e marca "auto" no relatório |
| **22h35-22h40** | Tencent → Dell: pedido das 2 janelas (~90s cada, `ffmpeg -ss X -to Y` **NA DELL**) | Tencent→Dell | 5 min | Dell corta 3 janelas (1 extra de reserva) |
| **22h40-22h50** | Dell corta (~15MB/janela) e sobe → Tencent monta **9:16 1080×1920 blur + legenda amarela (libass, MarginV≤100, bug PlayResY=288 documentado) + loudnorm** (~7MB) + **`thumbnail_oficial_video` do frame** (cat 28 fora da caça — ZM-042) | Dell→Tencent | 10 min | Se o 9:16 atrasar: sobe o corte em landscape primeiro (quente > formato) e verticaliza depois |
| **22h50-22h58** | ZM: MP4 → biblioteca de mídia do WP (espelho) → post carrossel 2º bloco `<video>` self-hosted → `post_status=future` 23h00 (corte 1); título padrão da casa + banco de nomes TV Fórum | ZM | até 22h58 | Post direto (publish imediato) se o agendamento falhar — espelho, laboratório |
| **23h00** | 🔴 **CORTE 1 NO AR** (quente, 1h pós-fim) — **PROVA** no canal (link + REST + thumb) | ZM | 23h00 | Checkpoint 22h45 (§6): se não fecha 23h → no ar até 00h30 OU desliza p/ 08h |
| **08h00** | 🔴 **CORTE 2 NO AR** (fresquinho) — idem | ZM | 08h00 | Montado à noite e agendado; se não, fluxo da manhã com o mesmo material |
| **08h05** | Relatório do dia no Telegram do Miguel: links dos 2 cortes + trecho da transcrição de cada + flag sinal/"auto" + falante | ZM/Tencent | 08h05 | — |

---

## 4. Seletor de HOJE: "só o Miguel falando" na prática (Camada 1)

1. **Rótulo de falante por segmento** (a partir da transcrição com timecode):
   - Se AssemblyAI: `speaker_labels` nativo (A/B) → mapear A/B→quem é via LLM (quem fala nos primeiros 60s = âncora/Miguel; padrão de abertura "Boa noite...").
   - Se Transkriptor sem rótulo: heurística de POSIÇÃO + juiz LLM (Miguel abre, comenta entre blocos de convidado, encerra; o juiz `--jornal` já distingue o programa e conhece o elenco fixo) → marcar **confiança** (alta/média/baixa).
2. **Candidatos válidos = segmento rotulado MIGUEL** ∩ (ocorrência da senha SE ele falar | score LLM de "parte mais interessante que ele fala": tese forte/frase de efeito/reação a fato do dia).
3. **Anti-falso-positivo (regra nova):** se a senha aparecer em segmento de CONVIDADO → **ignora** (não é o Miguel mandando cortar). Normalização (minúsculas/sem pontuação) + frase-curta + janela mínima entre sinais (~10 min) — herdei da 010.
4. **Fechamento do corte:** LLM fecha em frase completa; ±5s de margem ajustável; 30-90s de duração.
5. **0 candidatos bons:** fallback LLM escolhe 2 momentos DELE (marcados "auto"; 1ª semana com visibilidade no relatório). 
6. **v2 (não hoje):** pyannote/resemblyzer com referência de voz das edições anteriores — os áudios guardados na Dell (7 dias) viram o dataset de calibração.

---

## 5. Riscos da noite + planos B (curtos)

| # | Risco | Plano B / mitigação | Dono |
|---|---|---|---|
| R1 | Dell fora 20h-22h (sem 2ª porta — Tencent/NYC bloqueados) | VOD quando sair; corte 1 desliza p/ 08h (tolerância autorizada) | DS-Dell |
| R2 | Gravação cai no meio | Watchdog 5min religa + avisa; perda parcial declarada | DS-Dell |
| R3 | VOD/legendas atrasam | Caminho do áudio é INDEPENDENTE do VOD (transcrição via Transkriptor/AssemblyAI) | Tencent |
| R4 | Transcrição sem rótulo de falante confiável | Heurística + juiz (L1); confiança baixa → marca "auto" e mostra no relatório (nunca esconde) | Tencent |
| R5 | Uplink da Dell lento | Transcreve na Dell, manda só JSON de timestamps; janelas sempre cortadas na Dell | DS-Dell |
| R6 | Carrossel `<video>` do espelho não pronto até 22h50 | ZM publica o post simples com `<video>` no 2º bloco (fallback manual do ajuste IDEIA-009 §6) — dono do espelho é a ZM | ZM |
| R7 | Corte torto (frase no meio) | LLM fecha em frase completa; ±5s ajustável; re-corte rápido na Dell (janela já local) | Tencent |
| R8 | Relógio estoura | Checkpoint 22h45: no ar até 00h30 OU desliza p/ 08h — decisão registrada no relatório | ZM+Tencent |

**Reversibilidade total:** gravação = leitura pura do YouTube (como a porta já faz); publicação SÓ no espelho (laboratório, removível); nada no canônico; nada de post_status no site principal.

---

## 6. Checkpoints da noite (quem decide, quando)

| Hora | Checkpoint | Decisão |
|---|---|---|
| 19h55 | DS-Dell | Gravação confirmada? senão: aviso "sem corte 23h salvo VOD" |
| 22h00 | DS-Dell | MP4 local + áudio extraído? (senão: VOD) |
| 22h20 | Tencent | Transcrição com timestamps pronta? (senão: AssemblyAI/Transkriptor retry; whisper só se SLA 23h já cair) |
| 22h35 | Tencent | 2 candidatos escolhidos (falante=Miguel)? flags sinal/"auto" definidos |
| 22h45 | ZM+Tencent | Corte 1 fecha 23h? senão: até 00h30 no ar OU desliza p/ 08h (regra da tolerância) |
| 22h58 | ZM | Corte 1 agendado/publicado? PROVA no canal |
| 08h00 | ZM | Corte 2 no ar? PROVA |

---

## 7. Fora do escopo de HOJE (registrado p/ Fase 1+)

- Diarização por voz (v2 — pyannote/resemblyzer) e calibração da senha/config.
- Playlist ID mecânico ("Jornal da Fórum") — pendência mecânica da ZM, Fase 0 (1 comando na porta).
- Poda/storage do canônico (P5: só quando sair do espelho) e Fase 3 (redes sociais).
- Melhorias estruturais da esteira (runbook, relatório automático) — aprendizado da noite entra na Fase 1.

---

## 8. Registro

- **Refs:** IDEIA-010 (análise de viabilidade, 18:54) · fórum carrossel v2 (ZM) · `ZM-20260902-RECORD-001` (DS-Dell) · IDEIA-009 §6 (carrossel espelho) · regra ZM-042 (cat 28 + thumb fora da caça) · regra ZM-041 (Consenso Duplo p/ canônico; espelho = laboratório do dono).
- **Marcador de conclusão:** `PRONTO_PLANO_CORTES_REALISTA`.
- Nada executado em produção por mim (Lei de Poderes): este arquivo é planejamento; execução = ZM/DS-Dell sob ordens já postadas.
- Sem segredos/chaves neste arquivo (§82).

— DS Nuvem Ideias (DS-N Ideias) · arquiteto de brainstorms · 02/09/2026

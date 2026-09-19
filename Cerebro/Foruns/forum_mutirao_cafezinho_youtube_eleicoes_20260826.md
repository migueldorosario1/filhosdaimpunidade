# 🎯 Fórum — MUTIRÃO CAFEZINHO ELEIÇÕES: agente YouTube pesado (sabatinas Ponto Poder) + ritmos novos (26/08/2026)

> **Ordem do Miguel (26/08 ~17:45, quase literal):** "lá na página do jornal O Povo e do Diário do Nordeste, o Ponto Poder, está acontecendo várias entrevistas com governadores, candidatos — dá para fazer artigos, transcrever. O agente YouTube do Cafezinho tem que brilhar nessas eleições. Fazer várias matérias por dia. Transcrever tudo. Todos os candidatos. Sempre com essa linha pró-Lula, pró-anti-imperialista. Nos próximos 2 meses você pode parar todos os outros sites — faz só uma por semana nos outros. Continua fazendo diariamente no Global South News, Rio Carta e Cafezinho. GSN um por dia, Rio Carta dois por dia. Cafezinho vamos jogar pesado: transcrever entrevistas, inteligência artificial, vários vídeos transcritos e matérias de IA. Vamos fazer um mutirão, acelerar o Cafezinho."

## 1. A ordem em números (vigência: 26/08 → ~26/10/2026, eleições)

| Site | Ritmo novo | Ritmo anterior |
|---|---|---|
| **Cafezinho** | **PESADO** — várias matérias/dia (sabatinas, candidatos, IA) | 3 rodadas/dia + jornal + fórum 11.6 |
| **Global South News** | 1/dia | variável |
| **Rio Carta** | 2/dia | ~2/dia (já era) |
| **Demais sites temáticos** | 1/semana cada | parados/variável |

Linha editorial reafirmada: **pró-Lula, anti-imperialista**; transcrever TODAS as entrevistas de candidatos (Haddad citado nominalmente); IA como vertical reforçada no Cafezinho.

## 2. Diagnóstico do agente YouTube Cafezinho (26/08 17:45→18:15, ZCode/GLM-5.3)

### BLOQUEIO EXTERNO TRIPLO — transcrição inoperante desde 25/08 15:29

1. **YouTube bloqueou os IPs dos 3 servidores do ecossistema:**
   - Dell (local): yt-dlp → `HTTP Error 403: Forbidden`
   - Tencent (43.156.151.165): `Sign in to confirm you're not a bot` — persiste mesmo após yt-dlp 2026.08.19 + deno 2.9.5 (instalados nesta sessão, backup `yt-dlp.bak_20260826`)
   - NYC (198.199.121.136): mesmo bot-check (yt-dlp 2026.08.19 + deno já existiam)
2. **Transkriptor em pane geral:** último `Completed` = 25/08 15:29 (Jangadeiro Eleições). Desde então TODOS os jobs `Failed` (22+ de hoje, de todos os agentes — Cafezinho, GSN, temáticos). Teste isolado com arquivo WAV **não-YouTube**: submit aceito (202 + order_id) mas o job **evapora** (404 no /content, ausente da listagem) → pane de conta/backend, não só bloqueio YouTube×Transkriptor.
3. **iProyal sem crédito:** proxy responde `402 Payment Required` (renovado em 03/08 — crédito de tráfego esgotado). Era a rota que contornava o bloqueio (IP residencial). Estava `YOUTUBE_PROXY_MODE=off` no cofre (o AGY desligou após o ritual dos 30 dias); **religado para `fallback` nesta sessão** (backups `.bak_pre_proxy_fallback_20260826` nos 2 cofres) — mas sem crédito não resolve ainda.

### Bug próprio encontrado e CORRIGIDO

- **Canal "Diário do Nordeste (Ponto Poder)" na config apontava para canal ERRADO** (`UCi9JxJuwkMTW_5BzArzf6Ig` = entretenimento: "VAR TE LASCAR", "É Pôdi", último vídeo abr/2026). Corrigido para o canal principal DN que publica as sabatinas (`UCMf_wuiFqxdhZI1GVx02mmw` — Roberto Cláudio vice hoje, Camilo live PONTOPODER ontem) e **adicionado o canal do programa Ponto de Poder** (`UChHqX_jmsN3ddng9aCiBT9Q`). Backup `canais_cafezinho_youtube.json.bak_pre_pontopoder_20260826`.
- O canal **O Povo** (`UCj-RTZE-V3Q6jleatRR9k2A`) já estava certo e está ATIVÍSSIMO: sabatinas ao vivo com candidatos ao governo do Ceará (Danilo Soares/Democratas, Vera Lúcia/Novo hoje), Debates do POVO, Lula×Flávio.

### Estado saudável

- **Fila de revisão LIMPA:** só 1 draft YouTube no WP (267352) — breaker livre; quando a transcrição voltar, o fluxo anda sem entulho.
- Cache anti-desperdício (10 transcrições em disco) intacto; kill switch livre.
- Último draft criado pelo agente: 267639 (antes da pane).

## 3. Rota de destrave proposta (aguardando OK do Miguel)

**Recomendada:** recarregar **iProyal** → yt-dlp Dell via proxy residencial → upload S3 → **AssemblyAI** como transcriber (chave já válida no cofre, testada HTTP 200 nesta sessão). Vantagens: ~US$ 0,37/hora de áudio (~16× mais barato que Transkriptor US$ 6/vídeo), diarização nativa (separa entrevistador × candidato — ideal para sabatinas), e independe da pane do Transkriptor.

**Alternativa grátis/imediata mas frágil:** cookies de sessão do YouTube (navegador do Miguel) no yt-dlp — contorna bot-check de IP marcado, mas expira.

**Nota:** AssemblyAI não baixa YouTube direto (testado nesta sessão: recebe HTML, `Transcoding failed`) — precisa do áudio via yt-dlp+proxy.

## 4. O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** diagnóstico completo do bloqueio triplo; correção do canal DN/Ponto Poder na config; proxy religado no cofre; yt-dlp Tencent atualizado + deno; fila verificada limpa; feeds do Ponto Poder/O Povo/DN mapeados (sabatinas fresquinhas esperando).
- **Falta:** (a) decisão do Miguel sobre recarga iProyal (ou cookies); (b) integrar AssemblyAI como transcriber no `util_youtube_transcript.py` (patch pronto para escrever assim que houver rota de áudio); (c) ajustar ritmos dos sites (GSN 1/dia, Rio Carta 2/dia, temáticos 1/semana) — depende da transcrição; (d) reforçar rodadas do Cafezinho após destrave.
- **Preciso do Miguel:** 1 decisão — **recarregar o iProyal?** (ou prefere cookies do navegador / esperar o Transkriptor voltar). Com o "vai", o mutirão começa na mesma hora.

## 5. Referências

- Memória técnica irmã: `Memorias/memoria_mutirao_cafezinho_youtube_pane_20260826.md`
- Fóruns pais: `forum_agente_youtube_antidesperdicio_20260822.md` · `forum_auditoria_agentes_youtube_transcricoes_20260824.md` · `forum_iproyal_renovacao_fallback_youtube_20260803.md`
- Config corrigida: `agent_data/canais_cafezinho_youtube.json`

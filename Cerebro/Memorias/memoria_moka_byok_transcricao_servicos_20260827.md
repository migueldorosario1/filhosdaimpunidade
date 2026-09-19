# Memória — Moka: serviços de transcrição BYOK (Supadata/Transkriptor/TranscriptAPI/AssemblyAI) — 27/08/2026

**Missão:** ordem do Miguel ~14:35 — montar no espelho ousadia o seletor multi-serviço de transcrição com chave do próprio usuário, explicação nas ⚙️ (ícone 🎬), links de "como pego minha chave" e seção no /ajuda.

**Commit:** `b57fa79` na branch ousadia, push ousadia→main+ousadia no remote ousadia-mirror. NO AR em https://moka-ousadia.vercel.app (espelho 1 e canônico intocados).

## Arquitetura entregue

- **Cliente:** `lib/config.ts` ganha getTxService/setTxService + setTxKey/getTxKey (localStorage `mokavideo.txService`/`mokavideo.txKey`, chave criptografada com encrypt/decrypt de crypto.ts) + TX_SERVICE_LINKS (URL de onde pegar chave por serviço).
- **UI:** SettingsForm seção "🎬 Moka Vídeo" (seletor + chave mascarada + salvar + link); /ajuda seção com passo a passo por serviço; ui-strings 18 chaves (`tx_*` + `video_tx_hint`/`video_tx_link`/`video_listening_own`) × 12 idiomas inseridas linha-a-linha ancoradas na linha `video_whisper:` de cada bloco (âncora hindi difere: "ट्रांसक्रिप्ट" sem स् extra — copiar do arquivo, não digitar).
- **Servidor:** `lib/video/byok-services.ts` (novo) — façada byokSubmit/byokStatus + adapters:
  - Supadata: GET api.supadata.ai/v1/transcript?url= com header x-api-key; body {content:[{text,offset,duration}]} (ms); erro 401 corpo {"error":"unauthorized"}; timeout 150s (Whisper fallback deles demora em vídeo sem legenda; 2 créditos/min).
  - TranscriptAPI: GET transcriptapi.com/api/v2/youtube/transcript?video_url= Bearer; parse defensivo (transcript|content|segments); SÓ legendas existentes (sem legenda → recado sugerindo Supadata).
  - Transkriptor: tk* do transkriptor.ts agora aceitam `byokKey?` (fallback env casa): POST api.tor.app/developer/transcription/url → order_id; /files/{id} status; /files/{id}/content segmentos; gate tkQualityOk reaproveitado.
  - AssemblyAI: innertube ANDROID streamingData.adaptiveFormats → menor bitrate áudio com URL direta → download via ProxyAgent (PROXY_RESIDENCIAL_URL) → POST /v2/upload → POST /v2/transcript {speaker_labels:true} → polling GET /v2/transcript/{id}; utterances (Falante N) > words agrupados ~12s > text. Limite 120MB.
- **Rota /api/ingest (serverless):** headers x-tx-service/x-tx-key (CORS ampliado). **Ordem:** meta normal → transcript: captions grátis FIRST → falhou → BYOK → worker OpenAI → casa. **status:** BYOK intercepta ANTES do handler da casa (bug pego no smoke: orderId BYOK ia pro polling da casa e ficava 202 eterno). Erros mapeados (401/402/429/genérico) em recados sem tecniquês.

## Pegadinhas & lições

1. Status interceptado pela casa — precedência do status BYOK tem que vir antes de handleTranscricaoStatus.
2. Grátis-primeiro: primeira versão do fix colocou BYOK antes das captions → usuário pagaria crédito em vídeo com legenda. Reequilibrado (transcript: captions→BYOK; status: BYOK→casa).
3. TypeScript: union ByokPoll exige `"pending" in st` (não `st.pending`); Record<string,string> para headers (ternário com spread cria chaves undefined).
4. Smoke local do caminho serverless: MOKA_DISABLE_YTDLP=1 npx next dev -p 3199.
5. Vídeos de teste: hTWKZoEtwcQ (Nirvana) = hasCaptions FALSE (perfeito p/ BYOK); jNQXAC9IVRw = com legenda (prova grátis-first).
6. Deploy Vercel demora ~30-60s; teste discriminante: resposta muda de 428 (velha) para 401 amigável (nova).

## Estado / próximos passos

- ✅ No ar no ousadia; E2E com chave REAL do Miguel pendente (criar conta Supadata grátis).
- AssemblyAI sem E2E (sem chave real).
- Promover p/ espelho 1 + canônico só após aval do Miguel (fluxo oficial dos 3 ambientes).
- Transkriptor casa segue desligado (MOKA_CASA_TRANSCRICAO≠1) — BYOK independe disso.

## Adendo ~15:35 — multi-serviço com FALLBACK em cascata (commit 8791b30)

- **Storage:** `mokavideo.txServices` = lista ORDENADA de ativos; chaves por serviço em `mokavideo.txKey.<id>`; migrateTxLegacy() converte o formato antigo (txService/txKey únicos) na primeira leitura — chave do Supadata do Miguel preservada.
- **Cascata é no CLIENTE** (decisão de arquitetura): a rota /api/ingest continua recebendo UM serviço por vez (headers); o page.tsx itera getTxChain() tentando 1º→2º→3º com stage ao vivo txTrying (`⚠️ X falhou — caindo pro próximo…`). Zero mudança server, avisos em tempo real de graça.
- **pendingJob.service** decide os headers do polling (dono do job); retomada só se o serviço ainda tem chave.
- **UI ⚙️:** linhas com ☑ + badge Nº + ▲▼ (swap na lista e persiste) + chave/teste/link POR SERVIÇO; txTest é um-por-vez com service no estado.
- **Frente 2 pendente:** fallback das chaves de IA (fila ordenada por função + aviso "X falhou, usando Y" durante tradução) — hoje NÃO existe no app (verificado: nenhum fallback em ai-client/book-translate). Spec entregue no chat, aguarda aval.

## Promoção final (~15:30)

Miguel aprovou ("maravilha perfeito") → push ousadia→main nos 3 remotes (d9212e9..e4c7fd8). Alinhamento provado: /api/tx-test 200 nos 3, /ajuda c/ cascata nos 3, chunk de vídeo page-1fe0509a85232a9b.js IDÊNTICO nos 3. Toda a saga 27/08 em produção.

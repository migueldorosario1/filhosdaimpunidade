# 🧠 MEMÓRIA — MOKA: MODO REVISOR GOOGLE (gateway + app) — 05/09/2026

> Irmã do fórum `Foruns/forum_moka_modo_revisor_google_20260905.md`. Log técnico completo.

## Arquivos tocados

**Tencent `/home/ubuntu/moka/pontos_api/`** (backups `.bak_pre_revisor_20260905` de app.py/.env/moka_pontos.db):
- `app.py` (+57 linhas): `OPENAI_API_KEY`/`OPENAI_URL`/`OPENAI_TTS_URL`; `MODELOS_CASA` += gpt-4o-mini(1×)/gpt-4o(4×, flag `openai`); gate 503 aceita qualquer provedor; loop de chamada roteia url/key por modelo (sem chave = skip); NOVO `/ia/tts` (TtsIn; auth `_auth`; checa saldo `precos_acoes.acao='tts'`; OpenAI `/v1/audio/speech` tts-1 mp3; trava 1500 chars; allowlist 6 vozes; `_debitar` só no sucesso).
- `.env`: + `OPENAI_API_KEY` (valor do cofre unificado, pipe ssh sem exibir).
- DB: usuario id=7 senha_hash NOVO (hash local→arquivo→UPDATE, ver lição 1) + carteiras +1300 (65→1305).

**Cofres (rito [SEGREDO])**: `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado` (+`.bak_pre_moka_revisor_20260905`): `MOKA_REVISOR_EMAIL`/`MOKA_REVISOR_SENHA` (sha8 eab5f63e nos 2).

**App `~/ZCodeProject/moka-app` branch obra/memoria, commit `5b2d739` (5 arquivos, +160/−48), push `ousadia-mirror obra/memoria:main`**:
- `src/lib/moka-conta.ts`: MODELOS_CASA UI += GPT-4o mini/GPT-4o (default "" = GPT-4o mini); `gatewayProvider` default `getModeloCasa() || "gpt-4o-mini"`; erro sem conta reescrito; NOVO `iaTtsCasa()` (POST /api/pontos/ia/tts, 402→SaldoInsuficienteError, slice 1500).
- `src/lib/ai-client.ts`: import {getConta, gatewayProvider}; `resolveProvider` → BYOK primeiro, conta logada = `gatewayProvider("resumo_livro")` com config sintético {providerId:"moka-casa"}, senão erro-guia atualizado.
- `src/hooks/useTTS.ts`: `ttsConfig.casa?: boolean` (baseUrl/apiKey viram opcionais); ramo casa → `iaTtsCasa` → Blob mp3 do base64; telemetria/fallback/cache preservados; removido `const blob` duplicado.
- `src/components/Reader.tsx`: import getConta; NOVO `getTtsConfigOuCasa()` (BYOK → senão conta → senão null); 2 callers de TTS trocados.
- `src/app/ajuda/page.tsx`: FAQ revisor em PT e EN (conta de teste com IA da casa, contato info@mokareader.com).

## Comandos-chave

```bash
# estado gateway
ssh tencent 'ps aux | grep "[u]vicorn app:app"; curl -s -m 6 http://127.0.0.1:8420/'
# restart (padrão da casa; NÃO matar via TaskStop — o ssh pendura no bg)
ssh tencent 'cd /home/ubuntu/moka/pontos_api && set -a && . ./.env && set +a && nohup setsid /home/ubuntu/moka/venv/bin/uvicorn app:app --host 127.0.0.1 --port 8420 >> /home/ubuntu/moka/api.log 2>&1 < /dev/null & disown; sleep 8'
# prova texto (senha nos cofres MOKA_REVISOR_SENHA)
curl -X POST http://127.0.0.1:8420/ia/completar -d '{"email":"...","senha":"...","acao":"resumo_livro","sistema":"...","prompt":"...","modelo":"gpt-4o-mini"}'
# prova voz
curl -X POST http://127.0.0.1:8420/ia/tts -d '{"email":"...","senha":"...","texto":"...","voz":"alloy"}'
```

## Provas

- OpenAI da Tencent: `/v1/models` HTTP 200 em 1,3s (sem GFW).
- `/ia/completar` gpt-4o-mini: 200, tradução correta, debitado 40, saldo 365→325.
- `/ia/tts` alloy: 200, MP3 base64 45.568 chars, debitado 20, saldo 325→305.
- Build Next: falhou 1× (tipo baseUrl/apiKey obrigatórios no speakNeural) → corrigido → sucesso.
- Push: `5159cca..5b2d739 obra/memoria -> main` (moka-ousadia); deploy Vercel automático.

## Lições técnicas

1. **Hash de senha via ssh heredoc come o `$`**: `f"{sal}\${h}"` no bash remoto gravou sem separador → `_verifica_senha` quebrou ("not enough values to unpack"). Cura: gerar o hash NO DELL em arquivo, scp, e o python remoto LER do arquivo. Sempre validar com login real depois.
2. **Restart de serviço com `nohup setsid` via ssh**: o comando local em background prende o ssh (TaskStop depois pode derrubar a sessão). Rodar o restart num ssh ÚNICO que termina sozinho (`& disown; sleep 8`) e NUNCA TaskStop nele.
3. **O gateway de pontos (pontos_api) é infraestrutura viva desde 01/08** — nuvem esquecida útil: login, pontos, /ia/completar, painel. Antes de construir proxy novo, checar o que já existe lá.
4. **OpenAI é alcançável da Tencent** (região sem GFW p/ api.openai.com — 1,3s). O GFW que derrubou a Alibaba não afeta OpenAI aqui.
5. **resolveProvider é o ponto único de decisão BYOK×casa** — 9 call-sites herdam o modo casa de uma vez.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** gateway OpenAI + voz neural + trava de pontos; conta revisor 1305 pts com senha nova nos cofres; app religado (commit 5b2d739) e deployado no Ousadia.
- **Falta:** E2E de UX no Ousadia (login ⚙️ → traduzir + ouvir); envs de transcrição do projeto Vercel ousadia; promoção ao canônico pós-aval; teto mensal no dashboard OpenAI.
- **Preciso do Miguel:** testar no Ousadia com o par entregue no chat e autorizar o uso no appeal ao Google.

— ZM · ZCode/GLM-5.3 · 05/09/2026

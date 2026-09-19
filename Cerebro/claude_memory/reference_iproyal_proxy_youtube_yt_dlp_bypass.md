---
name: reference-iproyal-proxy-youtube-yt-dlp-bypass
description: "AUTH-047 16/06 15:09 BRT — IPRoyal residential proxy BR sticky 168h destrava yt-dlp/Transkriptor no Tencent (datacenter IP é bot-checkeado pelo YouTube). Credencial guardada em `/root/iproyal_credentials.env` chmod 600 (NÃO compartilhar em fórum/canal — só ponteiro). Endpoint geo.iproyal.com:12321. Senha codifica sticky session: `<base>_country-br_session-<id>_lifetime-168h`. Patch em `util_youtube_transcript.py:_duracao_segundos()` lê `IPROYAL_PROXY` e injeta `--proxy` no yt-dlp. Bypass do `Sign in to confirm you're not a bot` 100% PASS testado em y8zhwctLKfI e SHCu3ZmT288. Outros agentes que usam yt-dlp (agente_youtube/twitter_video/cortador/bots Telegram) ainda NÃO foram patchados — escopo futuro."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# IPRoyal proxy bypass YouTube bot-check (AUTH-047)

## TL;DR

YouTube bloqueia yt-dlp em IPs de datacenter (Tencent Cingapura) com erro literal `Sign in to confirm you're not a bot. Use --cookies-from-browser or --cookies for the authentication`. Solução: usar IPRoyal residential proxy BR via `--proxy` no yt-dlp. Bypass 100% testado 2026-06-16 15:05 BRT.

## Credencial

**NUNCA escrever a credencial completa em canal_trindade / fórum público / inbox.** Foi vazada uma vez em 2026-05-21 e Codex teve que mascarar histórico.

Localização da credencial real:
- **Arquivo Tencent**: `/root/iproyal_credentials.env` (chmod 600)
- **Env var Tencent**: `IPROYAL_PROXY` no `/root/.env.unificado` (linha adicionada AUTH-047 16/06 ~15:09 BRT)

Formato: `http://<user>:<base>_country-br_session-<id>_lifetime-168h@geo.iproyal.com:12321`

Sticky session BR 168h foi a config que funcionou (US/Los Angeles deu HTTP 429 — IPs muito usados). Se a sessão expirar (168h = 7 dias), Miguel reseta no painel IPRoyal.

## Como o patch funciona

Em `util_youtube_transcript.py:_duracao_segundos()` (linha 519):

```python
def _duracao_segundos(self, url: str) -> float:
    try:
        cmd = ["yt-dlp", "--no-playlist", "--print", "%(duration)s", url]
        # AUTH-047: usa proxy IPRoyal residencial pra bypassar bot-check YouTube em IP datacenter
        proxy = os.getenv("IPROYAL_PROXY", "").strip()
        if proxy:
            cmd = ["yt-dlp", "--no-playlist", "--proxy", proxy, "--print", "%(duration)s", url]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        ...
```

Se `IPROYAL_PROXY` não estiver setado, yt-dlp roda sem proxy (fail-open suave — vai bater no bot check, mas não quebra fluxo).

## Outros agentes que usam yt-dlp (escopo futuro)

`/root/agente_tradutor_legenda.py`, `/root/agente_twitter_video.py`, `/root/agente_youtube.py`, `/root/bot_mayrag_v3.py`, `/root/bot_zizi_linda.py`, `/root/cortador_youtube.py`, `/root/test_youtube_transcriber.py`.

AUTH-047 cobriu APENAS `util_youtube_transcript.py` (pipeline editorial principal). Os outros vão precisar do mesmo patch quando forem reativados — preferencialmente extraindo helper compartilhado tipo `util_yt_dlp.py` que centralize a chamada com proxy injection.

## Comportamento esperado

- yt-dlp `_duracao_segundos` PASS com proxy → cost guard libera Transkriptor → pipeline editorial roda
- Transkriptor baixa transcrição diretamente da URL (Transkriptor tem proxy próprio, não depende de yt-dlp)
- Pipeline LLM redige + audita + publica em WP draft (status default `YOUTUBE_AUTONOMO_STATUS=draft`)

## Quando renovar/rotacionar

- A cada 168h (sessão expira), Miguel reseta no painel IPRoyal e fornece nova senha
- Atualizar `IPROYAL_PROXY` no `.env.unificado` Tencent (sem mudar nada em código)
- Atualizar `/root/iproyal_credentials.env` (chmod 600) com a nova string completa

## Relacionados

- [[feedback_creditos_apis_primeiro_item_diagnostico_lentidao]] — IPRoyal é serviço pago tipo API LLM, monitorar consumo
- [[feedback_peer_review_obrigatorio_quando_util_ja_existe]] — quando expandir patch pros outros agentes, peer review por util compartilhado
- [[feedback_corrigir_na_raiz_nao_no_auditor]] — corrigir bot-check na origem (yt-dlp via proxy) em vez de mexer em downstream

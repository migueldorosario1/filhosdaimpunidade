# Fórum — Bug §86: drafts V4 órfãos sem featured_media (diagnóstico raiz)

**Data:** 2026-08-01 ~01:10 BRT · **Autor:** Kimi K3 Desktop (ZCode) · **Gatilho:** cartinha Claude `pending_delegados_20260731_1120` (8 posts travados) · **Execução autorizada por Miguel ("vai")**

## Resumo executivo
O worker V4 cria o draft primeiro (`skip_image=True`) e anexa a imagem depois, em funil transacional (`generate_upload_attach_cartoon`). Quando o funil falha, o draft fica órfão (sem `featured_media`), a regra §86 barra o publish e o reparo órfão automático (1 post/ciclo) não dá vazão ao backlog. Em 31/07 eram 8 órfãos acumulados.

## Cadeia do bug (evidências em `draft_events` SQLite NYC, 30/07–01/08)
1. **Gerador de cartoon desenha TEXTO na ilustração.** Auditoria de visão (regra: nenhum texto renderizado) rejeita com `bloqueio_grave`. Casos reais: 'REVISTAFORUM', 'DRILLED BY THE RIGS', '25%', nomes de pessoas, 'PASSAPORT', 'AIR' no casco do navio, marca d'água na proa. Após 4 tentativas: `RuntimeError:cartoon_visual_rejected_after_4_attempts` → `image_pending` → órfão.
2. **Kimi vision judge 401 na NYC** (`kimi_vision_http_401: API Key appears to be invalid`) → fallback Qwen-VL. Funciona, mas a chave morreu e ninguém alertou.
3. **Acervo R2 com URLs mortas (HTTP 400)** — ex.: `.../entidades/eduardo-bolsonaro/c4d8a88494a1_...jpg` (113 bytes XML de erro). O caminho "foto real" do Nacional degrada em silêncio pra cartoon (que é onde o bug #1 morde).
4. ~~**Flux Pro falhando**~~ **RESOLVIDO 01/08 ~05:06 UTC:** era falta de crédito na fal.ai. Miguel recarregou; smoke no caminho de produção (`generate_editorial_image`) retornou `sucesso=True, gerador=flux-pro` (HTTP 200, 3,3s). Residual cosmético: erro mascarado como `HTTP ?` quando a exceção não carrega resposta — dificulta diagnóstico (proposta §extra, aguarda autorização).
5. (menor) `repair_preflight_failed` por ProxyError no senado.leg.br via proxy NYC.

## Por que "travava em silêncio"
Os eventos existem no SQLite (`image_pending`, `repair_preflight_failed`), mas nenhum alerta sobe pro Telegram/painel — o órfão só aparece quando alguém varre `pending` manualmente (foi o Claude, 31/07 11h).

## Mitigação aplicada nesta sessão (sem tocar produção)
- 8 órfãos resolvidos: 6 via `--repair-post` canônico (wan2.6 aprovado na 1ª geração), 2 via foto real Wikimedia Commons com crédito (após 2 reprovações cada no juiz).

## Propostas de correção (AGUARDAM autorização Miguel, 1 por item)
1. Reforçar negative prompt do gerador: "sem texto, letras, números, logotipos, marcas d'água" (hoje só no retry_guard a partir da 2ª tentativa — subir pra 1ª).
2. Recalibrar juiz: distinguir texto central proposital (bloqueia) de ruído irrelevante de fundo (warning).
3. Revalidar `storage_url` do acervo (`acervo.db`): varrer HTTP 400 e re-espelhar via `R2_PUBLIC_URL`.
4. Renovar chave Kimi vision na NYC (Cofre) + alerta quando juiz cai em fallback.
5. Alerta Telegram quando `image_pending` ocorrer (hoje é silencioso).

## Referências
- Worker: `/root/v4_vertical_draft_worker.py` (NYC) — `generate_upload_attach_cartoon`, `repair_orphan_wp_draft`, flag `--repair-post`
- ACK canal: `[KIMI-PENDING-3-DELEGADOS]` 01/08
- Backups/registros: eventos `draft_events` nas 3 SQLite de verticais

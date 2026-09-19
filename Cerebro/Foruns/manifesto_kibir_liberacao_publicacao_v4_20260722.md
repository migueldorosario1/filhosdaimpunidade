# MANIFESTO KIBIR — Liberação da publicação V4 (tribunal visual)

**Agente:** Kibir (Kimi k3, ZCode CLI local)
**Data:** 2026-07-22 ~21:10 UTC (18:10 BRT)
**Autorização:** Miguel, em chat, com urgência — "libera a publicação; tudo que mexer, backup antes"
**Servidor alvo:** NYC (`198.199.121.136`) — casa única dos agentes V4 (Tencent parada, confirmado por Miguel)

## O que vou fazer (e o que NÃO vou fazer)

1. **NÃO alterar código.** O tribunal visual consultivo já está deployado em produção
   (`/root/v4_vertical_draft_worker.py`, `audit_generated_cartoon`, hard_block só para
   anomalia grave; indisponibilidade do Kimi = não bloqueante). Mexer agora seria risco
   sem benefício.
2. **Reparar o único resíduo real:** draft WP `262493` ("Irã fecha Ormuz…", 21/07) sem
   `featured_media`, usando o mecanismo nativo do próprio worker
   (`--repair-post`), que é transacional: só devolve a draft após upload + attach + readback.
3. **NÃO tocar** nos 10 drafts antigos sem imagem (7 reais estagnados de 06–17/07,
   3 testes). Registrados para decisão editorial do Miguel — fora do escopo urgente.
4. **NÃO tocar** nos 6 pendings antigos sem imagem (junho, maioria testes).

## Diagnóstico (evidências)

- Tribunal Kimi barrava imagem com versão ESTRITA (backup `/root/backups/v4_fal_kimi_brave_20260722_0255`,
  300 linhas de diff). Log real: `cartoon_visual_rejected_after_4_attempts: A balança e a folha em
  branco não comunicam que a desaprovação supera a aprovação…` (pauta de pesquisa — falso negativo clássico).
- Versão consultiva entrou em produção entre 02:55 e 14:23 UTC de hoje. Desde então:
  **zero rejeições do tribunal**, drafts confirmados a cada 2h nas 3 verticais
  (geopolítica, ciência, nacional), incluindo pauta de pesquisa ("Lula dispara 7 pontos…").
- Proxy residencial 504 (fal.run/DashScope/OSS) também já mitigado no código
  (`trust_env=False` nas sessões de geração e download).
- Fila `image_pending`: **0 eventos não resolvidos** nos 3 bancos SQLite.
- Publicação ao vivo confirmada: Repetidor Estatal publicou `262573` às 20:12 UTC;
  últimos 10 posts publicados todos com imagem.

## Backups (protocolo dobrado)

| Cópia | Local |
|-------|-------|
| 1 (servidor) | `/root/backups/kibir_liberacao_publicacao_20260722_2110/` (worker + gerador + coletor + snapshot JSON do post 262493) |
| 2 (local) | `Cerebro/Backups/kibir_liberacao_publicacao_20260722_2110/` (espelho idêntico) |

MD5 worker remoto = backup = `d09f64aafff52d1ec0118786a9040e60`.

## Rollback

- Post 262493: restaurar `featured_media=0` via WP API usando `wp_post_262493_antes.json`.
- Código: não alterado; rollback desnecessário.

## Riscos residuais conhecidos (não tratados neste manifesto)

- Proxy 504 intermitente pode derrubar geração pontual → fluxo cai em `image_pending`
  e o `repair_pending_image` recupera na batida seguinte (comportamento observado OK).
- 7 drafts reais estagnados sem imagem aguardam decisão editorial (reparar ou descartar).
- Reforma ampla do V4 = fase 2, a combinar com Miguel/Trindade.

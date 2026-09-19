---
de: ZCode/Kimi K3 (workspace ZCodeProject, sessão cb0f90df)
para: Loop Laura (Claude Laura + Codex Laura + Grok Laura)
ts_brt real: 2026-08-16T09:46:35-03:00
assunto: AGENTE YOUTUBE reativado — agora publica como RASCUNHO; revisão externa solicitada
---

# Agente YouTube do Cafezinho — reativado e em modo rascunho

**Ordem Miguel (16/08 ~10:00):** o agente YouTube passa a operar como os demais: **publica como draft** e aguarda **revisão externa do Loop Miguel e do Loop Laura** antes de ir ao ar. Miguel pediu para informar os dois loops para ficarem atentos.

## Ficha técnica
- **Pipeline:** NYC `/root/youtube_v2_pipeline.sh` (coletor→produtor→auditor→publicador), cron `0 11,17 * * *` (8h/14h BRT) — re-add 16/08 (entrada tinha sumido; bloco Vídeos parou ~10/08).
- **Publicador:** `/root/agents_labs/youtube_v2/agente_youtube_v2_publicador.py` — agora `--status draft` (backup `.bak_pre_draft_20260816`); todo post leva cat editorial + **Vídeos (28)** + Youtube (20751).
- **Canais coletados:** Opera Mundi, Revista Fórum, TV 247, ICL Noticias, DCM (per fila do coletor; transcrição via transkriptor c/ gate anti-alucinação <100 chars/min).

## O que observar (achados típicos que valem subir)
- título/excerto com metalinguagem, código ou bastidor (houve hoje o incidente `short_open_tag` — código PHP vazou em páginas novas; **resolvido** nos 2 servidores, excerpts limpos nos 2 bancos; post 266062 foi o caso);
- texto de transcrição fraco/inventado (alucinação — o gate já rejeita os piores, mas pode passar texto pobre);
- imagem: hero = thumbnail do YouTube (baixa resolução 480x360 é o normal do agente — não é bug);
- categoria: o guard de precedência no WP já expulsa 22/5003/15 quando houver Tecnologia — não "corrigir" contra essa regra;
- cadência: se nenhum draft novo chegar por >48h, provável falha de proxy iProyal (flaps 504) ou cron — reportar como falha de worker.

## Referências
- Fórum do dia: `Foruns/forum_agente_youtube_reativado_20260816.md` (reativação + incidente short tag + mudança p/ draft).
- Item aberto na fila do Loop Miguel: `ponte_trindade_daemon/fila_para_claude.md` ticket `ZCODE-YOUTUBE-DRAFT-REVISAO-LOOPS-20260816`.

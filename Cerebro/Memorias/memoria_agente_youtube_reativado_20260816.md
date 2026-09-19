# Memória — Agente YouTube reativado (16/08 ~09:20 BRT)

Par: `Foruns/forum_agente_youtube_reativado_20260816.md`. NYC `/root/agents_labs/youtube_v2/`.

- Pipeline: `youtube_v2_pipeline.sh` (4 estágios; log `/root/agent_data/youtube_v2_pipeline.log`). Cron `0 11,17` UTC re-add 16/08.
- Patch publicador: `montar_payload()` resolve_terms → `cats = [editorial, 28]`; py_compile OK; deploy com backup.
- Diagnóstico rápido futuro: (1) `crontab -l | grep youtube`; (2) `tail youtube_v2_pipeline.log` (existe? parou em qual estágio?); (3) grep ProxyError no log → testar proxy c/ curl via `chaves.sh`; (4) stats do banco no fim de cada estágio (`publicaveis_pendentes`).
- Publicador publica via `controle.ocafezinho.com` — hooks mu-plugin do www NÃO disparam nesse caminho (auto-cat-videos só pega em re-save). Lição: patches de categoria têm que ir NA FONTE do agente, mu-plugin é só rede de segurança parcial.

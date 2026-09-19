# 🧠 Memória — Auditoria Transkriptor×GSN 13/09 (log técnico completo)

**Companion do fórum:** `Foruns/forum_transkriptor_gsn_pipeline_sangramento_20260913.md` (ZM-20260913-010). Sessão ZCode/GLM-5.3 (Dell), 13/09 ~17:2x→17:5x BRT. Auditoria read-only — NENHUM arquivo remoto alterado.

## Trilha de investigação (comandos e provas)

1. `ssh nyc crontab -l` → linha `0 11,17 * * * /root/youtube_v2_pipeline.sh` COMENTADA com `# PAUSADO_TEMATICOS_20260912_ZM`; mas `journalctl -u cron` de 13/09 11:00:02 mostra `(root) CMD (/root/youtube_v2_pipeline.sh ...)` EXECUTANDO descomentada, e `youtube_v2_pipeline.log` tem "Pipeline Done" 13/09 17:09:57 UTC. Crontab root mtime `2026-09-13 20:10:47 UTC` — editado 1h depois da última corrida, não por esta sessão.
2. `banco_custos_2026-09.jsonl` (NYC) → linhas transkriptor 12/09 (5) e 13/09 (4, último 17:08:55) com custo_usd=6.0 (registro duplicado 6.0+0.0 por vídeo); `transkriptor_detalhe.log` contador 81→84 hoje.
3. Tabela autoridade: `youtube_dialogos.sqlite` (NYC) → `dialogos`: transkriptor desde 10/09 = 11×US$ 3,00; setembro total 24× = US$ 71,60; até 31/08: 91× US$ 172,57. Provider `transkriptor_url_direto`.
4. Vídeos de 12-13/09 (oEmbed): Dialogue Works (Larry Johnson satélites Aramco; Nima power balance), Judging Freedom shorts ×2 (FBI 2026; 9/11 Israeli Involvement), Daniel Davis (IRAN war; Saudi/Yemen/Iran), Neutrality Studies (11-Set lies), kremlin (conversa bin Zayed) — 100% geopolítica.
5. `publicaveis`: matérias 10-11/09 majoritariamente `descartado_vencido`; as 3 de 13/09 `pronto` wp= -. `gsn_fila/` (NYC): 8 JSONs de 10/09 17:12→13/09 17:09 SEM consumo (materializador = orquestrador temático `globalsouth_publicador.py`, pausado 12/09 "--site riocarta"). Home www.globalsouth.news (colada pelo Miguel): último post 12/09; 11/09 zero posts de vídeo.
6. Publicador (`agente_youtube_v2_publicador.py`): roteamento por idioma 17/08 — EN NUNCA vai ao WP Cafezinho, vai à gsn_fila (Astro/Vercel sites-v4/globalsouth). PT/espelho para o WP Cafezinho (o cron do espelho PT `40 12,18` NÃO está mais no crontab do NYC — pausado/embutido na pausa dos temáticos).
7. Espelho PT GSN→Cafezinho (fórum 11/09): cron `40 12,18` também fora do crontab atual → os drafts 269875/269876 seguem os últimos do espelho.

## 🔴 Achado de segurança (fora do escopo, reportado)

- `/dev/shm/kworkers/` (mtime 10/09 08:41 UTC) com binário `kworkers` 30.360 bytes www-data 777 + crontab www-data `*/30 * * * * bash /dev/shm/kworkers/kworker` — persistência de invasor no NYC, 3 dias antes do hack do espelho DO. `wtmp`/`last` sem logins interativos desde 09/08 (minha conexão BatchMode não aparece — normal, mas limita rastreio). Encaminhar à sessão da emergência (forense_hack_20260913 no espelho DO).

## Números-chave para reportar

- Aproveitamento 10-13/09: 11 transcrições pagas → ~3 posts no ar (≈27%).
- Desperdício pós-pause: 13/09 = US$ 12 (4 vídeos) + LLM de redação EN.
- Esteira custa ~US$ 6-9/dia quando roda 2 corridas (2-3 vídeos/corrida × US$ 3).

## Pendências

1. Confirmar 14/09 que 11h/17h UTC não rodaram (linha comentada às 20:10 UTC de 13/09 por origem não identificada — provável outra sessão da casa).
2. Miguel decide: religar GSN (consumidor) ou zerar esteira (produtor).
3. 8 JSONs na gsn_fila: os de 10-11/09 já vencidos (FRESCOR 48h); os de 12-13/09 publicáveis se religar em 14/09.
4. Forense kworker NYC.

---

## Adendo execução (13/09 ~17:5x→18:1x BRT)

- Crons NYC: `0 11,17 pipeline (max-itens 2)` + `40 12,18 espelho_pt --apply` + `20 12,18 gsn_fila_consumidor.py` (novo; reconstruído — o antigo sumiu; ledger `/root/agent_data/gsn_fila_consumidor_ledger.json`; log idem .log; repo `/root/tematicos/sites-v4/globalsouth` push origin github.com:migueldorosario1/globalsouth-v4).
- Tencent: flags dsn_youtube+alimentador_yt arquivadas em `controles_arquivadas/`; alimentador religado com nota CAFEZINHO_20260913.
- Fix NOMES: produzidos.meta_json entrevistado "Nima Rostami Alkhorshid"→"Nima R. Alkhorshid" (backup sqlite .bak_pre_nima_fix_20260913); reauditoria OK (media_wp_id 270570).
- Café drafts hoje: 270519/270520/270612/270613/270616 (cat 28, embed, capa) — provados via REST (403 sem UA navegador = WAF de 13/09; com UA 200).
- GSN: 6 briefs pushados (rebase sobre 55d8133 de outra esteira); home provada com 4 títulos novos ~1 min após build.
- Backups: youtube_v2_pipeline.sh.bak_pre_cafezinho_20260913 · painel_cctv_v6.py.bak_pre_yt_cafezinho_20260913 · youtube_dialogos.sqlite.bak_pre_nima_fix_20260913 · controles_arquivadas/.
- Pendências: anti-shorts no coletor; identificar esteira paralela que commita vídeos GSN (formato "youtube: <título> [<id>]"); forense kworker; vigiar 14/09 as corridas automáticas.

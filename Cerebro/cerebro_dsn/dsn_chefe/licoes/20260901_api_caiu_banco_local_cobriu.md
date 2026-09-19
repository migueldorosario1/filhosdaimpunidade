# Lição 2026-09-01 · A medição tem redundância: quando a API cai, o banco local cobre

**O quê:** na ronda 23:30, a API CCTV `/v6/api/audiencia-vertices` retornou 404 (×3 com retry + redirect 301→404). Em vez de ficar sem número, usei o banco local `/home/ubuntu/cafezinho/v6_data/farol_audiencia.db` + `lumina_audiencia.jsonl` + `farol_health.json` — mesmos dados da coleta CCTV (LUMINA 63 online · 1.784 distintos · FAROL db 172 · GA4 121 · posts_48h 94 · health OK gap 5min).

**Por quê:** a coleta (daemon da Tencent) grava localmente a cada 30 min ANTES de servir pela API; o banco local é a fonte primária, a API é só a vitrine. Uma queda da vitrine (404, 500, rota mudada) não apaga a fonte. Na vigília da promulgação, "sem número" seria um buraco de registro — e o ritual exige audiência em TODA ronda.

**Como aplicar:**
1. Se a API `/v6/api/audiencia-vertices` falhar, NÃO reportar "sem dado": ler `~/cafezinho/v6_data/lumina_audiencia.jsonl` (última linha = LUMINA + distintos/visitas), `farol_audiencia.db` (`SELECT ts,online,views_ga4,posts_48h FROM medicoes ORDER BY ts DESC LIMIT 1`), `farol_health.json` (status/gap).
2. Registrar o episódio como OBS leve (tipo OBS-037/038) — transiente ≠ quebra; sem alarme, watch item.
3. Nunca depender de um único caminho para o número: a redundância é o método (REST canônica + permalink real por ID + banco local da audiência).
4. Se a rota tiver MUDADO (404 persistente por horas/dias), avisar o ZM (dono da coleta CCTV) para publicar a rota nova — a casa inteira usa essa API.

Verificado: OBS-038 registrado no bloco DS-N-141 (ronda 23:30) + esta lição madura na MEMORIA_VIVA.

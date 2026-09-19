# 🧠 Memória — FAROL-MOKA (contador da casa no MokaReader)

**Tema Duplo:** Foruns/forum_farol_moka_20260915.md · **Data:** 15/09/2026 · ZCode/GLM-5.3

Arquitetura: pixel FarolBeacon.tsx (layout raiz do Moka, id anon no localStorage, keepalive) → relevo HTTPS mu-plugin cafezinho-farol-moka-relevo.php (REST /wp-json/cafezinho/v1/farol-moka, token público; repassa wp_remote_post non-blocking) → painel Tencent POST /api/moka-receber (token v6_data/moka_token.txt) → moka_audiencia.jsonl → GET /api/moka-resumo (agregação on-the-fly: hoje/online30/humanos por UA anti-bot/série 24h). Commit Moka 2615b95 (branch ousadia). Painel editado com backup .bak_pre_farolmoka_20260915 + restart cctv-v6 limpo.

Lições: (1) mixed content: site HTTPS (Vercel) não fala com colector HTTP/IP — relevo WP resolveu; (2) endpoint do relevo SÓ com www (301 derruba POST→GET); (3) grep de pixel client-side: a constante vive no CHUNK JS (app/layout-*.js), NUNCA no HTML — e borda da Vercel serve HTML velho: cache-buster na URL; (4) headless NÃO completa fetch keepalive (idem GA4) — prova real exige navegador de gente; (5) classificação humano×bot por UA no coletor (curl/python = bot; Chrome = humano) comprovada em produção.

Estado: NO AR no ousadia; aguarda visita real + OK do Miguel p/ promover espelho 1 + canônico. Leitura p/ rondas: ssh tencent 'curl -s "http://127.0.0.1:8084/api/moka-resumo?token=$(cat /home/ubuntu/cafezinho/v6_data/moka_token.txt)"'.

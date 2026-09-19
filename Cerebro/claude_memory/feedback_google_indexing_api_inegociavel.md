---
name: feedback-google-indexing-api-inegociavel
description: TODOS os posts publicados (Cafezinho e qualquer portal Trindade) DEVEM chamar Google Indexing API após publish. Inegociável. Verificação contínua obrigatória.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🚨 **TODO post publicado em QUALQUER portal da Trindade DEVE notificar a Google Indexing API.** Sem exceção. Inegociável. Mesmo nível de regra que [[feedback_imagem_destacada_obrigatoria]] §86.

**Why:** Miguel descobriu 06/06/2026 ~20:50 BRT que ~80% dos posts do Cafezinho NÃO disparavam Google Indexing porque `motor_publicador.py` (motor das pautas master_geopolitica/nacional/trends) não chamava `indexador_google.notificar_google()`. Só agentes nicho (temáticos premium, crime, editorial, optimizador_seo, MT_ferroviario, youtube_publicador) chamavam. Resultado: posts demoravam horas/dias pra aparecer no Google em vez de 2-10 minutos.

Reação do Miguel: "isso é crítico, todos os posts tem que ter o Google Index API, isso é muito crítico, bota no cérebro aí, e bota para sempre verificar se todos os posts estão completamente indexados".

**How to apply:**
- TODO agente publicador (motor_publicador.py + 60+ agentes nicho) chama `from indexador_google import notificar_google; notificar_google(url, "URL_UPDATED")` IMEDIATAMENTE após POST WP retornar 200.
- Fail-open: try/except em volta, falha de indexing NÃO prende post (respeita [[feedback_soltar_posts_nao_prender]]).
- Log da chamada em JSONL (`/root/agent_data/indexing_calls.jsonl`): post_id, url, timestamp, status, response_code, error.
- **Verificador contínuo:** cron periódico cruza posts `status=publish` últimos N (via WP API) × log JSONL. Posts publish sem registro de indexing → re-pingar + alertar Miguel.
- Auditoria no tick §53: amostragem rápida "X% dos publish da janela foram pingados?". Se <100% → escalar.
- Cobertura: Cafezinho (motor + temáticos + nichos), GSN, Mundo dos Trilhos, Discover Brazil, Rio Carta (Astro — usar IndexNow se Indexing API não cobrir), Mapa Rio.
- Service account já existe (`/root/agent_data/indexing_key.json`, scopes `https://www.googleapis.com/auth/indexing`), Owner no GSC de cafezinho.com.br + mundotrilhos.com. Quota Google Indexing API = 200 URLs/dia padrão → pra Cafezinho (~80-150 posts/dia) é suficiente; se ampliar, pedir quota raise (formulário oficial Google).
- Patch §92: backup motor_publicador.py.bak + rollback (remover chamada) + parecer Codex no fórum.

Relacionado: [[feedback_imagem_destacada_obrigatoria]] §86 (outro inegociável da publicação), [[feedback_soltar_posts_nao_prender]] (fail-open obrigatório).

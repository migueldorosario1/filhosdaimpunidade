---
name: feedback-reportar-agente-em-publishes
description: "Em qualquer report de produção/publishes/scans do Cafezinho, SEMPRE informar qual agente gerou o post. Não basta título+status+featured. Miguel 22/06 18:10 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

Quando reportar publishes/produção do Cafezinho (em ticks §53, scans WP API, triagens, parecer de auditoria), **SEMPRE informar o agente que gerou cada post**. Não basta `id + título + status + featured` — falta o agente.

**Why:** Miguel 22/06 18:10 BRT — "quando me falar dos posts, diz também qual foi o agente!!!". Sem o agente o report é cego: não dá pra atribuir qualidade/regressão ao produtor certo, comparar cadência entre agentes, ou identificar autoria de bug editorial.

**How to apply:**

1. **Fonte 1 (preferencial)**: meta `_agente_origem` via WP API. B-018 deployed 22/06 — `v3_politica`, `legado_eleicoes`, `legado_flavio_bolsonaro`, `youtube_v2`, etc. Já popula nos publishes pós-Kimi snippet PHP ativado (~18:00 BRT 22/06).

2. **Fonte 2 (fallback quando meta vazio)**: inferir por:
   - **Categorias**: 22+5088+1100 = política/V3; 5003+5062 = geopolítica/militar; 5008 = ciência/IA; 18896 = turismo; 19936 = saúde; 20751 = YouTube V2; 4996 = china; 43 = economia
   - **Author ID**: 5470 = Redator (default todos agentes); outros IDs raros
   - **Padrão de título**: V3 tem títulos longos com 2 cláusulas; YT V2 cita guest+host; lula sempre "Lula..."; eleicoes "Datafolha/Ipec/Quaest..."
   - **Timestamp + cron**: V3 a cada 30min (`0,30 8-22`); maestro `*/20`; china `5 * * * *`; manchete `0 */2`; YT V2 `0 * * * *`
   - **Featured image origem**: V3 sempre tem; LEGADO via Flickr live; china via Brave/Wikimedia

3. **Formato sugerido por linha**:
   ```
   18:01 #260302 publish ✅ feat=✅ [V3 política] cats=[43,5088,22,1100] | Mendonça censura...
   17:41 #260299 publish ✅ feat=✅ [turismo_embratur?] cats=[20699,18896] | Turismo 11 cidades...
   ```
   Onde agente vai entre colchetes. Se `?` = inferido (e B-018 ainda não populou).

4. **Quando reportar lote**: agrupar por agente também ajuda — "V3 política: 3 publish + 2 pending nas últimas 30min" é mais útil que listar 5 IDs soltos.

5. **Agentes diretos sem B-018 populado** (após 18:00 BRT 22/06): `turismo_embratur`, `analytics_v9`, `fantastico`, `feminino`, `coletor_social` etc — usar inferência por cats+timestamp+padrão. Kimi pode estar patchando esses gradualmente.

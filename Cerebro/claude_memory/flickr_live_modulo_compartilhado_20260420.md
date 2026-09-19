---
name: flickr_live.py — módulo compartilhado para foto oficial ao vivo
description: Novo módulo (root/flickr_live.py) busca foto oficial direto na API do Flickr para Lula/Trump/Senado/Macron/STF/etc. Já usado pelo Master Lula. Falta plugar na Trindade — Miguel pediu integração futura.
type: project
originSessionId: da85d7d2-f66a-4b5a-b9db-6d27f8e11791
---
Em 2026-04-20, ao depurar Master Lula, Miguel revelou que assinou Flickr API "só pra isso" e quer regra de mídia oficial ao vivo NÃO só pro agente Lula, mas também:
- Trindade (Nacional/Geopolítica/Trends) quando publicar matéria de Lula.
- Qualquer entidade com Flickr oficial ativo: Trump (casa branca), Macron (Élysée), Xi Jinping (embaixada China), STF, Senado, Bolsonaro, Itamaraty, PT.

**Solução**: criado `root/flickr_live.py` (módulo compartilhado). Funções principais:
- `detectar_contas(titulo)` — regex word-boundary mapeia entidade → contas Flickr.
- `consultar_conta(orgao, api_key)` — bate API `flickr.people.getPublicPhotos`, cache em memória por processo.
- `escolher(fotos, titulo, data, janela_h, jaccard_min)` — filtra por janela temporal + Jaccard temático.
- `buscar_foto_oficial(titulo, data_pauta)` — orquestra cascata Plano A (±36h, J 0.18) → Plano B (±7d, J 0.12).

**Mapa entidade→contas (NSID hardcoded copiado de robo_coleta_imagens.FLICKR_PERFIS_NSID):**
- lula/luiz inácio/planalto → ["lula", "planalto"]
- trump/biden/casa branca → ["casa_branca"]
- macron/élysée → ["elysee_macron"]
- xi jinping/embaixada china → ["embaixada_china"]
- stf/supremo/moraes/gilmar/barroso → ["stf"]
- bolsonaro/flávio/eduardo → ["flavio_bolsonaro"]
- senado/pacheco/alcolumbre → ["senado"]
- itamaraty/mre/chanceler → ["mre"]
- pt nacional/gleisi → ["pt"]

**Status:**
- ✅ `flickr_live.py` criado.
- ✅ `agente_master_lula.py` refatorado para usar `flickr_live.buscar_foto_oficial`.
- ✅ **Trindade integrada (motor_publicador.py:702-734) — Prioridade 1.5** (entre og:image e banco SQLite). Opt-in: só roda se `detectar_contas` achar entidade. Try/except amplo. Tribunal Visual obrigatório.
- 🟢 **DEPLOYADO LIVE no Tencent 2026-04-20 22:04 BRT** — 4 arquivos (motor_publicador, flickr_live, agente_master_lula, robo_coleta_lula). Backup em `/root/motor_publicador.py.bak_20260420_220424`. Smoke test pós-deploy: 9 módulos críticos importam OK (motor + 4 Masters Trindade + Lula + Estatal + Ferroviário + Observador Sentinela).
- ⚠️ `agente_master_lula.py` SEM CRON ativo — só roda manual. Pra ativar 4x/dia adicionar `0 8,12,16,20 * * *` no crontab.
- 🔍 Monitoramento sugerido: `sudo grep -E 'Prioridade 1\.5|flickr_live' /root/agent_data/master_*.log` nos próximos ciclos da Trindade pra capturar comportamento real.

**Plano de integração futura na Trindade (a discutir com Miguel):**

Lugar canônico: `motor_publicador.iniciar_publicacao_especializada` linhas 678-702 (bloco "PRIORIDADE 1: imagem da fonte original").

Inserir como **Prioridade 0.5** (antes do og:image), DESDE QUE detectar_contas() retorne entidade conhecida:
```python
from flickr_live import buscar_foto_oficial, detectar_contas
contas = detectar_contas(titulo_artigo)
if contas:
    foto_live = buscar_foto_oficial(titulo_artigo, data_pauta=datetime.now(), contas=contas)
    if foto_live:
        # Roda Tribunal Visual e usa
        veredicto, legenda = analisar_imagem_gemini_vision(foto_live["url"], titulo_artigo, ...)
        if veredicto == "APROVADA":
            m_id = fazer_upload_imagem_wp(foto_live["url"], legenda=legenda)
            ...
```

**Riscos/cuidados pra integração:**
1. Latência: cada chamada API ~1-3s × N contas. Cache por processo já está; cache cross-process precisaria Redis ou sqlite TTL.
2. Quota Flickr: API gratuita tem 3600 req/h; com cache + 1 req por entidade detectada por ciclo, fica longe disso.
3. Falsos positivos de detecção (ex.: "stf veta" → STF, mesmo se foto não é do julgamento específico): mitigado pelo Jaccard ≥0.18.
4. Coexistência com banco SQLite: NÃO remover `coletar_flickr_institucional` do crontab — banco ainda serve pra arquivos antigos e fallback offline.

**Diretrizes editoriais Miguel — gravadas 20:36 BRT 2026-04-20:**
- 📦 **Toda foto puxada do Flickr live → também grava no banco SQLite** (`banco_imagens_reais.db`). Implementado em `flickr_live._persistir_no_banco` reusando `robo_coleta_imagens.salvar_no_db`. Idempotente via md5(url) PK. Banco Tencent hoje: 62.910 imagens (62.148 Wikimedia + 762 Flickr de 11 contas oficiais).
- 🪶 **Fotos têm que vir leves** — cascata `url_c (800px) → url_z (640px) → url_n (320px) → url_l (1024px fallback)`. NUNCA url_o/url_h/url_k (originais multi-MB que reprovavam no Tribunal Visual conforme `fix_tribunal_visual_20260417`).
- ✏️ **Legendas oficiais do Flickr são reaproveitáveis**: já vêm no campo `titulo` da API. Em geral PT (Stuckert/Planalto), mas contas internacionais (casa_branca, elysee_macron, embaixada_china, ONU futura) virão em EN/FR/ZH. Implementado `traduzir_se_ingles()` com heurística leve (acento PT → mantém; ≥2 marcadores EN → chama LLM router). Tradução só é feita na foto ESCOLHIDA, não nas 30 retornadas (economia LLM). Original preservado em `titulo_original`.

**Expansão executada 2026-04-20** — descoberta automática via `flickr.urls.lookupUser` + validação `getPublicPhotos` (filtro: upload < 12 meses):

🟢 **CADASTRADAS** (6 novas, total 16 contas no `flickr_live.NSID_OFICIAIS`):
- `onu` = 35483578@N03 — United Nations Photo (mais nova: 2026-03-12)
- `world_bank` = 10816734@N03 — World Bank (HOJE)
- `unicef_ethiopia` = 86783452@N02 — UNICEF Ethiopia regional (32d)
- `nasa` = 35067687@N04 — NASA HQ PHOTO (HOJE)
- `esa` = 37472264@N04 — European Space Agency (HOJE)
- `pentagono` = 68842444@N03 — SECWAR/Pentágono (4d)

❌ **DESCARTADAS** (parados ou sem conta encontrada):
- OMS (parou em 2006), UNESCO (490d), Cancillería Colombia (2011), Presidencia MX pré-Sheinbaum (2018), FMI (1169d), Casa Rosada (sem fotos), Greenpeace (vazio).
- Sem URL Flickr conhecida: OEA, presidência colombiana atual, Itamaraty (2ª URL), Câmara BR, IPEA, BNDES, Sheinbaum.

**Regex de detecção adicionados ao `ENTIDADES` (total 15):**
- onu/nações unidas/guterres/conselho de segurança/assembleia → ["onu"]
- banco mundial/world bank/ajay banga → ["world_bank"]
- unicef/catherine russell → ["unicef_ethiopia"]
- nasa/agência espacial dos eua/cabo canaveral → ["nasa"]
- esa/agência espacial europeia/ariane/copernicus → ["esa"]
- pentágono/dod/hegseth/secwar → ["pentagono"]

Smoke test: 11 títulos → 10 detectaram entidade correta + 1 cai no fluxo genérico (esperado). "STF julga ação contra Bolsonaro" detecta ambos `[stf, flavio_bolsonaro]` — Jaccard decide qual foto vence.

**Validação NSID via Flickr:** `flickr.urls.lookupUser` aceita URL `flickr.com/photos/USERNAME` ou `flickr.com/people/USERNAME`. Resposta: `{user.id, user.username._content}`. Script de descoberta em `/tmp/descobrir_nsids_flickr.py` (refazer pra novos candidatos).

**Referência cruzada:**
- `lula_master_corrigido_20260420.md` — contexto completo da auditoria.
- `forum_lula_audit_20260420.md` — fórum F1-F6.
- `banco_midia_cafezinho.md` — arquitetura banco SQLite atual (continua valendo pra contexto não-vivo).

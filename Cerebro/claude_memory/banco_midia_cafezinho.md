---
name: Banco de mídia do Cafezinho (pipeline atual)
description: O pipeline de imagens do Cafezinho usa apenas o banco_imagens_reais.db (SQLite, ~9942 fotos) alimentado pelo robo_coleta_imagens.py. Os outros 3 scripts de mídia são legados.
type: reference
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
O banco de mídia do Cafezinho é um **SQLite único**: `/root/agent_data/banco_midia/banco_imagens_reais.db` (colunas: id, origem, url_alta, data_foto, titulo, descricao, tags, termo, coletado_em).

**Alimentador ativo:** `robo_coleta_imagens.py` — duas fontes:
- **Flickr institucional** via API oficial (10 NSIDs fixos): Lula/Stuckert, Planalto, Senado, Itamaraty, PT, STF, Casa Branca, Élysée, Flávio Bolsonaro, Embaixada China. Observação do Miguel: o perfil Flickr da **Câmara dos Deputados** "tentou mas está bloqueado ou não existe mais" — não incluir.
- **Wikimedia Commons** via API `action=query&generator=search` — lista de queries expandida em 2026-04-17 de ~60 para **358 termos**: líderes BR/globais, governadores, Judiciário BR, Congresso BR, Golfo Pérsico/Ormuz (prioridade alta para geopolítica), Gaza/Líbano, Ucrânia/Rússia, blocos (BRICS/SCO/G20/ONU), economia, tecnologia.

**Agendamento no cron Tencent:** `0 3,15 * * *` (2x/dia).

**Consumidor:** `gerenciador_imagens.buscar_imagem_banco_local` (chamado pelo `motor_publicador.iniciar_publicacao_especializada` quando `exige_imagem_real=True`). Default do `nota_corte_imagem=90` é agressivo e pode virar gargalo — alvo provável de ajuste futuro (ver `feedback_publicar_os_melhores.md`).

**Scripts legados (NÃO agendar):**
- `agente_banco_midia.py` — usaria `indice_midia.json` via Gemini Vision; arquivo não existe no disco
- `agente_curador_midia.py` — criaria `banco_midia/{categoria}/*.jpg`; pastas não existem
- `extrator_midia_wp.py` — geraria `cache_midias_wp.json`; arquivo não existe

**Módulos (usados sob demanda, não entram em cron):**
- `gerador_imagem_editorial.py` — gera via Ideogram/Flux quando não há foto no banco
- `processador_imagem.py` — crop 1:1 + badge para Instagram

**Why:** o sistema evoluiu para um SQLite único porque é mais simples consultar (`SELECT ... WHERE termo LIKE ...`) e o banco cresce devagar sem precisar de indexação redundante via JSON + pastas. A arquitetura legada via pastas/índices foi substituída.

# Fórum — Gestão de canais YouTube pelo Painel CCTV V6 (16/08/2026)

> **Tema Duplo:** decisões resumidas aqui; log técnico completo em `Memorias/memoria_painel_cctv_gestao_canais_youtube_20260816.md`.
> **Origem:** ordem do Miguel (voz, 16/08 ~21:50 BRT): "acrescenta lá um campo youtube que eu posso acrescentar ou remover canal do agente youtube do cafezinho... lá na página sites temáticos você bota especificamente para o Global South News e Aiatolah News Mapa Rio".

## 🎯 O que foi feito

1. **Página nova `/v6/youtube`** no painel CCTV V6 (NAV 📺 YouTube): lista os **32 canais do agente nacional do Cafezinho**, com status, peso, idioma, origem — e **formulário para adicionar / botão para remover** cada canal. Só Cafezinho, como o Miguel pediu.
2. **Cards "📺 Canais YouTube"** nas páginas dos temáticos **Global South News, Aiatolah News e Mapa Rio** (mesmo esquema de adicionar/remover). O **Mapa Rio não existia na página de temáticos — foi adicionado** (mapario.com.br, 🏙️).
3. **Arquitetura "caixa de entrada"** (o painel fica na Tencent, os agentes rodam no PC do Miguel e no NYC):
   - Painel grava pedidos em `youtube_canais/pedidos/` + visão otimista em `vivo/` (feedback imediato na tela).
   - **Cron local `*/5`** (`agentes_cafezinho/sync_youtube_painel.py`): puxa pedidos via SSH → **valida channel_id por RSS oficial** (aceita UC…, URL ou @handle e resolve) → aplica nos JSONs locais **com backup datado** → devolve o estado canônico ao painel. Latência: ≤ 5-10 min.
   - Canal inválido é **rejeitado com motivo** (aparece no histórico da página).
4. **GSN tem dupla escrita:** config local + reconciliação do JSON vivo do **NYC** (`/root/agent_data/canais_youtube.json`, formato preservado; remoção = `ativo:false`).
5. **Aiatolah e Mapa Rio:** os agentes YouTube V4 estão desativados desde 03/08 (ordem do Miguel) — as listas ficam nos configs, prontas para reativação.

## ✅ Testado ponta a ponta (provas no log técnico)

| Teste | Resultado |
|---|---|
| Canal inválido (`UCaaa…`) no Cafezinho | ❌ rejeitado: "RSS retornou HTTP 404" — exibido no painel |
| Canal real (Band Jornalismo) no Mapa Rio | ✅ adicionado no formato feed-URL do config, depois **removido** com sucesso (lista voltou ao normal) |
| **@handle** (`@AaronMate`) no GSN | ✅ resolvido → validado → adicionado no config local **e no NYC** |
| Push do estado vivo (4 sites) | ✅ painel sempre reflete o estado canônico local |

**Bônus permanente:** a reconciliação GSN colocou no NYC 2 canais que estavam só no config local (Neutrality Studies Français, kremlin) + **Aaron Maté ficou adicionado de vez** (está na lista de entrevistados preferidos do GSN — adição útil, não só teste).

## 📍 Estado da missão

- **O que aconteceu:** tudo no ar — página `/v6/youtube`, cards nos 3 temáticos, cron */5, validação RSS, backups (painel `.bak_pre_youtube_canais_20260816`; crontab `/tmp/crontab.bak_pre_sync_youtube_20260816`; JSONs `.bak_sync_*` a cada aplicação).
- **O que falta:** nada do pedido. (Aiatolah/Mapa Rio só passam a processar de fato se/quando os agentes V4 forem reativados — hoje quem processa canal é o agente nacional do Cafezinho e o pipeline GSN do NYC.)
- **O que preciso de você (Miguel):** só usar — `/v6/youtube` para o Cafezinho; aba 📺 dentro de cada temático para GSN/Aiatolah/Mapa Rio. Mudanças entram em até ~5-10 min.

## 🔑 Regras de operação

- **Fonte de verdade = JSONs locais** (`agent_data/canais_cafezinho_youtube.json`, `agent_data/configs/*.json`, NYC para o GSN). O painel é a porta de entrada, nunca grava direto neles.
- Cache de nomes: `agent_data/youtube_canais_nomes.json` (40 nomes resolvidos hoje, inclusive os 8 que estavam sem nome).
- Novos canais via painel entram no Cafezinho com peso 1.5, idioma do formulário, categorias `[22,28]` (pt-BR) ou `[5003,28]` (outro idioma), origem `painel` — editável manualmente depois.
- Logs: `agent_data/sync_youtube_painel.log`; pedidos aplicados ficam em `youtube_canais/aplicados/` (auditável).

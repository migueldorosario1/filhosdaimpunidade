# PONTO DE RETOMADA — DeepSeek (Cheng)
# Atualizado: 2026-07-17 10:00 BRT

⚠️ LEIA ESTE ARQUIVO PRIMEIRO AO ACORDAR. ELE É A FONTE CANÔNICA DO SEU ESTADO.

---

## O que voce fez nas ultimas sessoes

### 15/07 — Baleia Azul #8 e correcao do sistema
- Retomada apos 16 dias parado. Corrigidos 3 fatores: markdown, HTML, script de audiencia.
- Endpoints: http://43.156.151.165/painel/baleia_azul.html e http://43.156.151.165/v5/baleia

### 16/07 — Correcao dos protocolos de despertar + Baleia Azul #9
- Miguel mandou corrigir protocolos para nao acordar perdido.
- Atualizados: PONTO_DE_RETOMADA, despertar_leve, memoria_viva, INDICE_DESPERTAR_LEVE.
- Alerta sobre boletim_latest.md congelado afixado.

### 17/07 — Baleia Azul #10 (hoje)
- Madrugada de reformas estruturais pelo Claude.
- Boletim #10 publicado.

---

## ⚠️ MUDANCAS ESTRUTURAIS (17/07 — IMPORTANTE)

Na madrugada de 17/07, Claude executou duas reformas a pedido do Miguel:

### 1. Forum canonico agora e Cerebro/Foruns/
- 30+ foruns movidos de `Projeto Cafezinho Agentes/Foruns/` → `Cerebro/Foruns/`
- Symlinks de compatibilidade preservados no path antigo
- Manifesto: `Cerebro/Foruns/MANIFESTO_REORGANIZACAO_FORUNS_20260717.md`

### 2. Legado isolado
- `Projeto Cafezinho Agentes/legacy_reformado_20260717/` — 28 blocos de codigo historico
- Nada apagado. Tudo rastreavel.
- Ativo canonico: `root/`, `root/v4_labs/`, `agents_labs/youtube_v2/`, `agents_labs/ceo_cerebro/`, `sites-tematicos/`
- Forum: `Cerebro/Foruns/forum_reorganizacao_agentes_cafezinho_20260717.md`

### 3. Manifesto canonico
- `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
- Leia antes de mexer em `agents_labs/` ou `Foruns/`

### 4. Canal Trindade resetado
- Versao limpa, apenas circuit breakers de 17/07 06:00
- Backup do canal antigo: `Cerebro/Foruns/canal_trindade_backup_20260710_pre_reorg.md`

---

## Protocolo de Despertar (16/07)

Ordem canonica ao acordar:

1. **ESTE ARQUIVO** → `Cerebro/memorias_provisorias/PONTO_DE_RETOMADA_DEEPSEEK.md`
2. **Inbox** → `Cerebro/Foruns/inbox_trindade/deepseek.md`
3. **Canal Trindade** → `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` (atencao: resetado 17/07)
4. **Manifesto V4** → `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
5. **Forum ativo do dia** → ver `Cerebro/Foruns/`

⚠️ NAO CONFIE no `boletim_latest.md` — congelado desde 28/05/2026.

---

## Estado do Ecossistema (17/07)

### V4 — Ativo
- Rodada: `Projeto Cafezinho Agentes/root/v4_labs/dados/rodada_v4_20260716_2casos/`
- 2 artigos em rascunho no WP:
  - Ciencia: Post #261606 (slug `ciencia_20260714_02`)
  - Cultura: Post #261607 (slug `cultura_20260714_streaming`)

### Sites tematicos — Ordem de atividade
1. Mundo Trilhos (mais ativo)
2. Ceara Digital
3. Rail Post
4. Global South News
5. Discover Brazil
6. Cafezinho

### Sprint — Bloco A indexing (19-20/jul)
- Faltam 2 dias. Miguel precisa adicionar 7 SAs como Owner no GSC.
- Forum: `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md`

### Circuit breakers
- `gemini/gemini-3.5-flash` — auth_config, 1440min (17/07 06:00)
- `anthropic/claude-opus-4-8` — auth_config, 1440min (17/07 06:00)
- `deepseek/deepseek-v4-flash` — quota_exhausted, 60min (14/07 22:46)

### Estagnado
- Faxina do servidor: 37 dias
- Corretor de categorias: 28 dias
- V3: pausado sem prazo
- Boletim News dinamico (Kimi CEO): congelado desde 28/05

---

## Pipeline Baleia Azul

- Markdown: `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md`
- CCTV v5: http://43.156.151.165/v5/baleia
- Nginx estatico: http://43.156.151.165/painel/baleia_azul.html
- Script envio: `scratch/enviar_baleia_azul_v2.sh` (raiz do workspace)
- SSH Tencent: `ssh -p 38422 ubuntu@43.156.151.165`
- SSH NYC (audiencia): `ssh root@198.199.121.136`

---

## Arquivos essenciais

- `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
- `Cerebro/Foruns/MANIFESTO_REORGANIZACAO_FORUNS_20260717.md`
- `Cerebro/00_CEREBRO_CANONICO.md`
- `Cerebro/CEREBRO_INDEX_MASTER.md`
- `Cerebro/CEREBRO_NODE_COFRE_CHAVES.md`

---

## Pendencias

- Autorizacao do Miguel para Baleia Azul diaria
- Miguel: adicionar 7 SAs no GSC antes de sabado (19/07)
- Executar `scratch/enviar_baleia_azul_v2.sh` para enviar email + Telegram

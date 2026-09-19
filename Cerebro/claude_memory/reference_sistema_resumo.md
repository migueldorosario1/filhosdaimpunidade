---
name: Resumo do sistema Cafezinho (despertar rápido)
description: Visão de 30 segundos do projeto + ponteiros pra chaves, servidores e tarefa atual. Ler primeiro a cada sessão.
type: reference
originSessionId: 48473406-5e6a-4ebe-826e-53bfe7292cb4
---
## O que é
**O Cafezinho Autônomo** — enxame de IA 24/7 que produz, edita, publica e distribui jornalismo progressista (PT-BR + Sul Global). 6 portais; ~60 agentes Python; ~40 comentaristas; bots Telegram; pipelines de imagem/vídeo/áudio.

## Onde fica o quê
- **Código local (canônico):** `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/`
- **Servidor Tencent (produção, Cingapura):** `43.156.151.165:38422` user `ubuntu`. Estrutura plana em `/root/`.
- **NYC failover dormente:** `45.55.50.249` (porta 22, root).
- **GSN (EN):** `159.89.237.100` (porta 22, root).
- **Chaves:** **`chaves/` na raiz do projeto** — ver `chaves/CHAVES_GUIA.md`. Canônico vivo é `/root/.env.unificado` no Tencent.
- **Memória do projeto:** `Projeto Cafezinho Agentes/CLAUDE.md` (ler ANTES de qualquer infra change).
- **Protocolo de segurança:** `Projeto Cafezinho Agentes/protocoloseguranca.md` (vinculante).
- **Coordenação multi-sessão:** inbox Trindade (`Foruns/inbox_trindade/claude.md`) + canal Trindade + fóruns por frente.
- **Canal Antigravity ↔ Claude:** `Foruns/canal_claude_antigravity.md`.

## Espinha dorsal dos agentes
- **Trindade Editorial:** `maestro_editorial.py` + masters (`agente_master_geopolitica/nacional/trends.py`) + `motor_publicador.py`.
- **Trindade temática premium:** Lula, IA, Latam, Sheinbaum, Mercado, Matriz Energética (FOSSIL/TRANSICAO), Inflação. Schedule via `publicador_tematicos.py`.
- **Suporte:** Observador (sentinela `*/10`), Performance (GA4), Manchete, Autocura V4 (`:17` de cada hora).
- **Nicho:** Ferroviário (cross-post Mundo Trilhos), Fantástico, Feminino, China, Singularidade, Militar, Crime, Turismo Embratur.
- **Análise V2:** deployado 25/04, cron `13 11,18`, top-30 do `historico.db`.
- **Comentaristas:** ~40 personas, lock por (site,post_id) deployado 25/04 14:40.
- **Imagem:** banco SQLite `banco_midia_cafezinho.db` (~10k) + `flickr_live.py` ao vivo + Tribunal Visual Gemini.
- **Fact-check:** Perplexity sonar-reasoning-pro → fallback Claude.

## Hierarquia
**Miguel** (decisão editorial) → **Claude Code** (coda + deploya + audita) → **Antigravity** (consultor premium, opina, NÃO toca infra). Divergência técnica → fórum `.md` na raiz, aguarda Miguel.

## Regras críticas (resumo de CLAUDE.md §10)
1. **Rsync sem `-a/-o/-g`** pra `/root/` (quebra SSH 3+ vezes já).
2. **Nunca HEREDOC/`cat >`** em .md compartilhados (incidente 22/04 destruiu CLAUDE.md). Só `Edit`/`sed`.
3. **JSON atômico:** `util_safe_json.py`, nunca `json.dump` clássico.
4. **Crontab é multi-autor:** backup + check mtime + sentinelas (SHELL=bash, temáticos≥8, autocura≥3, sync_leve=1) antes/depois de deploy.
5. **Dúvida não-trivial vira fórum** (`forum<topico>hoje.md`), pausa, espera Miguel.
6. **Toda comunicação com Miguel abre com timestamp `[YYYY-MM-DD HH:MM:SS BRT]`** (rodar `date` antes).

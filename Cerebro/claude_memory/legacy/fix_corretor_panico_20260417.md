---
name: Fix botão de pânico do Corretor 2026-04-17
description: Corretor paralisou 26 linhas do crontab por 1 falha de imagem; panico desabilitado. Drift de deploy — server tinha versão antiga `>0`, local tinha `>3`, nenhuma servia.
type: project
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
Botão de Pânico do `agente_corretor_autonomo.py` disparou 20:22 e comentou 26 linhas do crontab (sentinela, manchete, performance, youtube, fantástico, newsletter, etc.). Coletores e maestro_editorial ficaram de pé — publicação básica não parou.

Gatilho: post 236028 (Monique Rodriguez, saúde materna) ficou sem imagem de capa, Corretor tentou Wikimedia 2x e falhou. Desde 2026-04-11 já eram 7 posts com o mesmo sintoma acumulados — qualquer novo caso paralisava tudo.

**Why:** Miguel afirmou que o pânico é para emergências DRÁSTICAS (não falha de imagem). Versão do server tinha `if falhas_criticas > 0:` (qualquer 1 falha), versão local tinha `if falhas_totais_historicas > 3:` — mas a local nunca foi deployada, e mesmo ela já teria disparado com 7 históricas.

**How to apply:**
- Servidor `/root/agente_corretor_autonomo.py`: linha ~184 `if False:  # PANICO DESATIVADO 2026-04-17`; backup em `.bak_panico_desativado`.
- Local `root/agente_corretor_autonomo.py`: linha 186 mesma desativação.
- Crontab restaurado via `root/crontab_server.txt` (41 linhas ativas).
- Posts `failed_paralyze` em `/root/posts_para_conserto.json` ficam congelados (Corretor só pega `pending_repair`) — não precisam ser limpos.
- Pendente: recuperação de imagem via Wikimedia está quebrada há 1 semana (7 posts), investigar `buscar_wikimedia()` que usa só `tags_list[0]` com filtro `filetype:bitmap|drawing`. Prova: API retorna resultados para "Monique Rodriguez" num teste direto, mas o código não loga o motivo da falha.

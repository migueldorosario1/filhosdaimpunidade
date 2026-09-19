---
name: Coletores Cafezinho leem fontes de JSON cache, não do código
description: Antes de desativar feed RSS, limpar AMBOS .py (DEFAULT_FEEDS) e agent_data/fontes_<modulo>.json — comentar só no .py NÃO TEM EFEITO
type: feedback
originSessionId: 64e4c471-3031-4a70-a7b1-a07c8b6e5a0d
---
Os robôs coletores do Cafezinho (`robo_coleta_<modulo>.py`) chamam
`load_feeds()` que carrega fontes de **`agent_data/fontes_<modulo>.json`**
(cache JSON persistente). O `DEFAULT_FEEDS` no código é apenas seed inicial.

**Why:** 2026-04-22 03:10 BRT — descobri durante o Ciclo 2 do monitoramento 24h
que meu fix do Ciclo 1 (comentar Tasnim na linha 30 do
`robo_coleta_geopolitica.py`) **não teve efeito nenhum**: 982 erros Tasnim
foram registrados nos 16 minutos seguintes. O coletor estava lendo Tasnim do
`agent_data/fontes_geopolitica.json` (mtime 13/04, fonte cacheada por
`load_feeds()`). Comentar no código não basta enquanto o JSON listar a fonte.

Bonus: o mesmo Tasnim estava **em 3 coletores diferentes** (`geopolitica.py:30`,
`militar.py:23`, `soberania.py:17` — esse último já comentado em 18/04).

**How to apply:** Antes de desativar uma fonte RSS:

```bash
# 1) Mapear TODAS as ocorrências da fonte no /root
ssh cingapura 'sudo grep -rn -i "nome_fonte" /root/*.py /root/agent_data/*.json'

# 2) Remover do JSON cache (fonte real do load_feeds)
ssh cingapura 'sudo python3 -c "
import json
arq = \"/root/agent_data/fontes_<modulo>.json\"
fontes = json.load(open(arq))
fontes = [f for f in fontes if \"nome_fonte\" not in f.get(\"nome\",\"\").lower()]
json.dump(fontes, open(arq,\"w\"), ensure_ascii=False, indent=2)
"'

# 3) Comentar nos .py de TODOS os coletores que listam a fonte
# 4) Validar no ciclo seguinte (contar erros do mesmo padrão na janela 30min)
```

Esta regra vale também pra:
- Adicionar fonte nova: criar entrada nos 2 lugares (.py e .json)
- Renomear fonte: atualizar nos 2 lugares
- Bloquear temporariamente: pode usar `ultimo_status` no JSON, mas o coletor
  IGNORA esse campo e tenta de novo — então melhor remover do JSON

Coletores afetados conhecidos: `geopolitica`, `militar`, `soberania`,
`nacional`, `trends`, `latam`, `sheinbaum`, `lula`, `imagens`. Cada um tem
seu próprio `fontes_<modulo>.json` e seu próprio `DEFAULT_FEEDS`.

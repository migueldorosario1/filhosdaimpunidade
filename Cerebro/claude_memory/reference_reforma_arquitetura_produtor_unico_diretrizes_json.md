---
name: reference-reforma-arquitetura-produtor-unico-diretrizes-json
description: "REFORMA NÃO tem agentes separados como LEGADO. Tem produtor único `Sistema/agentes/produtor_geral.py` + diretrizes JSON por tema em `Sistema/agentes/<tema>/diretriz_<tema>.json`. Auditor tem prompt próprio depois mas não é raiz do vício. Campos críticos pra clichê: redacao.linha_editorial_injetada, linha_editorial.angulo, linha_editorial.obrigatorio."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# REFORMA arquitetura — produtor único + diretrizes JSON por tema

Codex esclareceu em 2026-06-15 ~23:50 BRT (cartinha pós-AUTH-032a PASS) que **a arquitetura editorial da REFORMA é diferente do LEGADO**:

## LEGADO
- Tem ~60 agentes Python separados (`agente_china.py`, `agente_sheinbaum.py`, `agente_master_geopolitica.py`, etc.)
- Cada agente carrega seu próprio prompt e lógica de produção.

## REFORMA
- **Produtor único** Python: `/root/cafezinho/portal_cafezinho/Sistema/agentes/produtor_geral.py`
  - Monta o prompt geral.
  - É invocado por todos os temas — não tem agente_china.py / agente_sheinbaum.py separados.
- **Diretrizes JSON por tema**: `Sistema/agentes/<tema>/diretriz_<tema>.json`
  - Injetam tom e enquadramento de cada tema (china, sheinbaum, ia, nacional, geopolitica, militar, petroleo, soberania, etc.).
  - Carregam: `keywords`, `regex`, `score_*`, `fontes_*`, `redacao.linha_editorial_injetada`, `linha_editorial.angulo`, `linha_editorial.obrigatorio`.
- **Auditor/revisor** tem prompt próprio (`auditor_texto.py`) depois — mas **não é a raiz principal do vício de clichê**.

## Campos JSON críticos pra clichê (3 vetores de tese forçada)

| Campo | Função | Risco |
|---|---|---|
| `redacao.linha_editorial_injetada` | Injeta orientação no prompt do produtor | Pode forçar fórmula ("explique X com foco em soberania/conflito/hegemonia") |
| `linha_editorial.angulo` | Define ângulo editorial do tema | Pode virar tese pronta ("disputa tecnológica EUA × China × Sul Global") |
| `linha_editorial.obrigatorio` | Lista de tópicos obrigatórios | Pode forçar matéria técnica a virar geopolítica ("destacar alternativas Sul Global") |

## Campos JSON que NÃO devem ser tocados sem razão muito forte

- `keywords` — ajudam o coletor a achar pauta
- `regex` — mesma função
- `termos_busca` / `score_*` — scoring de coleta
- `fontes_*` — lista de fontes confiáveis do tema

**Princípio**: escopo de **coleta** ≠ escopo de **redação**. Pode ter "Sul Global" como keyword pra capturar pauta, sem que isso obrigue o produtor a escrever "Sul Global" em toda matéria.

## Como aplicar

### Quando o problema for clichê editorial

1. Ler `Sistema/agentes/<tema>/diretriz_<tema>.json`
2. Focar nos 3 campos críticos (linha_editorial_injetada/angulo/obrigatorio)
3. Trocar comando fixo de tese por orientação factual ("preserve fatos concretos primeiro; enquadramento entra quando sustentado")
4. NÃO mexer em keywords/regex/score/fontes

### Quando o problema for cobertura insuficiente

1. Ler `keywords` / `fontes_*` — pode ser falta de termos pra coletor pescar pauta nova
2. Verificar se a fonte tem RSS/sitemap rastreável

### Quando o problema for tom/voz editorial geral

1. Mexer em `produtor_geral.py` (prompt central comum a todos os temas) — não nos JSONs
2. Casos AUTH-022/AUTH-023a/AUTH-027

## Casos fundadores (15/06)

- **AUTH-023b** (Codex): cobriu 5 JSONs (china/geopolitica/militar/petroleo/soberania) com este padrão.
- **AUTH-032a** (Codex 23:50 BRT): cobriu 3 JSONs P0 (sheinbaum/ia/nacional) com mesmo padrão.
- **AUTH-032b** (fila): P1 (esportes/mobilidade/seguranca_publica) — aguarda GLM medir P0 antes.

## Implicação pra Daemon

- Não falar mais "agente_china/agente_sheinbaum" como entidade Python na REFORMA — falar "diretriz_china/diretriz_sheinbaum" (são JSONs invocados pelo produtor único).
- Em propostas de AUTH editoriais REFORMA: distinguir mudança em **JSON** (per-tema) vs mudança em **produtor_geral.py** (global) vs mudança em **auditor_texto.py** (pós-produção). Cada camada tem cobertura e risco diferentes.

Relacionados:
- [[feedback_corrigir_na_raiz_nao_no_auditor]] (princípio raiz)
- [[feedback_reforma_so_alguns_agentes_ligados_evitar_duplicar_legado]] (REFORMA controlada)
- [[feedback_cutover_legado_so_apos_saude_reforma]] (cutover por saúde)

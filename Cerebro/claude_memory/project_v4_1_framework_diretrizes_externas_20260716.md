---
name: v4-1-framework-diretrizes-externas-20260716
description: "Diretriz macro do Bloco B — sites temáticos vão pra V4.1, framework genérico config-driven com diretrizes externas por site (YAML/JSON/MD), zero hardcode, dinâmico. Rio Carta ganha identidade própria (não é repetidor). Todos os 7 sites entram, começa pelo Rio Carta como piloto."
metadata: 
  node_type: memory
  type: project
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# V4.1 — Framework config-driven pros sites temáticos

**Data:** 2026-07-16 01:40 BRT.
**Origem:** Miguel definiu diretriz macro do Bloco B logo após fechamento do Bloco A ([[project_separacao_sas_indexing_concluida_20260716]]).

## Diretriz Miguel (literal)

> "vamos fazer mudanças editoriais em todos os sites. todos terão agentes v4. rio carta não pode ser apenas repetidor de noticia. temos que dar qualidade e novidade a tudo que publica. todos os sites serão no estilo v4.1, com diretrizes externas, sem hardcode, bastante dinamicos e modernos."

## O que é V4.1 (delta em relação ao V4 atual)

**V4** = 9 inovações editoriais do Cafezinho canônico (auditor consenso 3/3, 6 invariantes hard-coded, dry-run, fact-check cascata, tribunal visual, autocura, preparador→publicador→auditor, detecção meta-discurso, regra sigla título). Cada agente V4 é **hardcoded pra site específico**.

**V4.1** = mesmas 9 inovações **+ 4 princípios arquiteturais novos**:

1. **Diretrizes externas** — configs por site em arquivos (YAML/JSON/MD), não em código
2. **Zero hardcode** — framework genérico, N configs. Um agente_v4.py operado por `--site <nome>` lê `sites/<nome>.yaml`
3. **Dinâmico** — configs podem mudar sem redeploy (recarrega no runtime)
4. **Moderno** — incorpora práticas 2026: structured output LLM, config-driven pipelines, contratos entre camadas explícitos, sem tomada-de-decisão embutida em código

## Config schema preliminar (a definir no piloto Rio Carta)

Provável formato por site:

```yaml
site: riocarta
identidade:
  tom: "jornalismo hiperlocal RJ, progressista"
  publico: "carioca informado"
fontes:
  rss: [urls...]
  scraping: [urls...]
  api: [config...]
categorias_alvo: [...]
volume_alvo:
  min: 5
  max: 10
auditor:
  threshold: 40  # veto-only conforme feedback_auditor_nao_e_curador
  consensus: 3/3
ranker:  # NOVO em V4.1 — separado do auditor
  criterios: [...]
  top_n: 3
curador:  # NOVO em V4.1 — refinamento tom/qualidade
  personalidade: [...]
publicador:
  tipo: vercel_git  # ou wp_rest, headless_api, etc
  config: {...}
```

## Consequências editoriais

- **Cross-post automático rígido provavelmente sai** — cada site com identidade própria
- **Rio Carta ganha jornalismo original** — não é só RSS reciclado nem cópia do Cafezinho
- **Cada temático recebe pauta própria alinhada com seu público**

## Consequências arquiteturais

- **Não é mais "1 agente por site"** — é **1 framework + N configs**
- **Piloto Rio Carta = piloto do framework V4.1** (não só config Rio Carta)
- **Publicador precisa abstrair backend** — Vercel git+push, WP REST, headless CMS, etc — tudo por config

## Sites em escopo (todos os 7)

Todos servidos por Vercel (confirmado no Bloco A):
- globalsouth.news
- riocarta.com (piloto)
- mundotrilhos.com
- discoverbrazil.news
- mapario.com.br
- aiatolah.com
- ceara.digital

## Próxima ação

Sessão 16/07 pela manhã ou tarde:
1. **Auditoria Rio Carta**: silo `Rio Carta Agentes/`, publicações últimas 30d, agentes ativos, publicador Vercel real
2. **Desenho framework V4.1**: schema config, componentes, contratos
3. **Fórum específico**: `forum_piloto_v4_1_riocarta_20260716.md`
4. **Miguel responde 5 perguntas restantes** do §7 do fórum sprint temáticos com contexto do relatório
5. **Só depois codar** (semana +1)

## Relação com decisões editoriais recentes

- Complementa [[feedback_auditor_nao_e_curador]] (16/07): auditor V4.1 = veto-only threshold 40, decisão de qualidade/relevância fica no **ranker + curador** (componentes novos no V4.1)
- Complementa [[project_repetidor_estatal_redeploy_nyc_20260714]] (14/07): repetidor estatal em modo draft é o outro lado da moeda — Miguel quer qualidade humana antes de publicar, V4.1 traz auditor consensual pra automatizar essa validação

## Referências

- Fórum: `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md` (entry 2026-07-16 01:40 BRT com esta diretriz)
- Bloco A concluído: [[project_separacao_sas_indexing_concluida_20260716]]
- Snapshot sessão: `Projeto Cafezinho Agentes/Ponto de Retomada/Claude Code/20260716_011500_sessao.md`

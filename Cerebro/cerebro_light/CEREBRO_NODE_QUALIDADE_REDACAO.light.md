# CEREBRO_NODE_QUALIDADE_REDACAO — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_QUALIDADE_REDACAO.md` (39KB) — 80 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_QUALIDADE_REDACAO

Node vivo para relatorios do Agente de Qualidade de Redacao.

## Regra

Este node guarda diagnosticos diarios de qualidade editorial do Cafezinho.

O agente de qualidade:

- le posts e logs em modo read-only;
- mede clareza, densidade factual, aderencia editorial, rigor temporal/factual, estilo, SEO e estrutura;
- registra vicios recorrentes e exemplos;
- pode sugerir ajustes de prompt/diretriz apenas como proposta;
- nao publica, nao rebaixa post, nao altera tier e nao edita codigo autonomamente.

Qualquer mudanca real em `diretrizes_editoriais.py`, prompts ou config exige consenso da Trindade, aprovacao de Miguel, backup, registro no indice de mudancas e monitoramento pos-ajuste.

## Ideias a Desenvolver

### 2026-06-16 — Agente de Aprendizado Editorial Controlado

Miguel pediu estudar uma camada nova ligada ao ecossistema do Agente Qualidade: um agente capaz de usar os relatorios de qualidade, diretrizes, monitoramento humano, auditor de titulos e ticks do Claude Daemon para propor melhorias estruturais em diretrizes editoriais, prompts e demais pontos que afetam a qualidade dos posts.

Esclarecimento de Miguel: o objetivo de longo prazo e automatizar tambem esse processo. A fase inicial deve ser segura/read-only, mas a arquitetura deve nascer preparada para evoluir ate automacao progressiva, com gates, rollback e medicao pos-mudanca.

Principio registrado:

- o agente deve aprender com evidencias recorrentes;
- nao deve transformar diagnostico fraco em regra dura;
- nao deve alterar producao sozinho;
- deve priorizar solucao upstream quando a causa estiver em produtor/diretriz;
- deve manter revisor/auditor como safety net inteligente, nao como muleta permanente;
- deve exigir websearch quando o problema envolver fato, fonte, data, cargo, identidade ou imagem;
- qualquer mudanca real precisa de proposta, diff candidato, simulacao antes/depois, autorizacao, backup, smoke, rollback e medicao pos-mudanca.
- meta evolutiva: read-only -> proposta -> diff candidato -> simulacao -> deploy supervisionado -> automacao restrita de baixo risco -> automacao assistida de patches seguros.

Forum de estudo: `Projeto Cafezinho Agentes/Foruns/forum_agente_aprendizado_editorial_controlado_20260616.md`.

Memoria relacionada: `Cerebro/Backups/memorias_provisorias/feedback_agente_aprendizado_editorial_controlado_20260616.md`.

## Relatorios

Relatorios detalhados ficam em:

```text
root/agent_data/qualidade_redacao/
```


## [2026-05-20 14:31:47 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_143146 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_143146.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_143146.md`
- Posts avaliados: 5

### Notas medias
- clareza: 9.6/10
- densidade_factual: 9.2/10

---

## ⏩ 75 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_QUALIDADE_REDACAO.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Resultado da primeira compilação no Tencent
```
Regras permanentes extraídas: 23
  redator: 5
  revisor: 5
  gerador_de_títulos: 5
  auditor: 4
  fact-checking: 4
Regras provisórias: 0
editorial_base: presente
```

---

### Backups feitos (rollback disponível)
- `/root/backups/diretrizes_deploy_20260601/agente_editorial_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/diretriz_editorial_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/diretrizes_editoriais_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/agente_diretrizes_editoriais_pre_deploy_20260601.bak`

---

### Arquivos novos no Tencent
- `/root/backup_diretrizes.py`
- `/root/compilar_diretrizes.py`
- `/root/agent_data/diretrizes_editoriais/diretrizes_provisorias_v1.md`
- `/root/agent_data/diretriz_ativa.json`

---

### Planos de monitoramento
- **Kimi Code:** monitorar compilação diária, verificar se regras chegam aos prompts
- **Claude Maestro:** monitorar qualidade dos posts, alertar se houver regressão

---

### §92
Deploy aprovado por Miguel (tick). Quórum: Kimi + Codex + DeepSeek + Miguel.

<!-- /DEPLOY_DIRETRIZES_20260601 -->

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_QUALIDADE_REDACAO.md`](./CEREBRO_NODE_QUALIDADE_REDACAO.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`
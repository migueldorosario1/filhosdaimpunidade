# Bugs Encontrados — Log de Instâncias

**Início:** 2026-07-23 11:20 BRT
**Criado por:** Claude Code (Anthropic, engenheiro-chefe)
**Motivo:** Miguel pediu registro sistemático de CADA erro encontrado no site + solução aplicada, com data/link/detalhes. Anteriormente só o manual de bugs (`Outros/manual_de_bugs.md`) tinha padrões estruturais — instâncias individuais ficavam perdidas.

## Estrutura

- `bugs_YYYY-MM-DD.jsonl` — 1 arquivo por dia, append por ocorrência
- Cada linha JSON tem: `ts_brt` · `post_id` · `link` · `tipo_bug` · `detalhe_encontrado` · `solucao_aplicada` · `ts_correcao_brt` · `agente_corretor` · `bug_manual_ref`

## Tipos de bug catalogados

| tipo_bug | descrição | manual_ref |
|---|---|---|
| `sujeira_metadata_slug` | `<em>Categoria</em>` vazando como texto (ex: Mundo, Ciência) | #18 grupo B |
| `agregador_como_fonte_visivel` | âncora "Redir" ou "REVISTAFORUM" em vez de "Folha", "Revista Fórum" | #20 |
| `ponto_virgula_titulo` | `;` em título proibido pela regra D4 | D4 |
| `nome_proprio_sem_contexto` | "Vorcaro", "Hugging Face" sem contextualizar (regra D2) | D2 |
| `partido_minuscula` | "Pt", "Pp", "Psdb" — sigla partido em minúsculas (regra D3) | D3 |
| `dia_semana_alucinado` | LLM alucina calendário ("terça-feira 21" errado) | #19 similar |
| `titulo_truncado_elipse` | `…` HTML no meio de título | D4 |
| `fact_check_grave` | cargo errado ministro, data inconsistente | prompt "V4 NACIONAL fact-check" |
| `duplicata_publish` | mesmo tema/personagem publicado <24h | prompt dedup |
| `image_pending_sem_recovery` | draft V4 sem featured_media, órfão do worker | #18 grupo A |
| `outro` | não categorizado ainda | — |

## Uso

Sentinela pode adicionar entradas a cada ciclo. Cartas semanais/mensais consolidam por tipo/frequência.

## Índice e incidentes graves

- Índice desta pasta: `INDEX.md`.
- Memória própria do editor-chefe:
  `../memoria_bugs_claude_miguel/INDEX.md`.
- Incidente grave não termina na correção do post. Aplicar:
  `../../Foruns/diretrizes/protocolo_incidente_grave_bastidores_v1.md`.

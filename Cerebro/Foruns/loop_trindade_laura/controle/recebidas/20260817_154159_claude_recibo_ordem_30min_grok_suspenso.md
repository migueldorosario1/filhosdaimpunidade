# Recibo — ORDEM_MIGUEL: volta aos 30 min + Grok suspenso por crédito + funções redistribuídas

```yaml
tipo: RECIBO_ORDEM
de: LAURA-CLAUDE (chefe)
relogio_ronda: "Monday, 17/08/2026 15:41:59 -0300"
origem: Miguel, chat direto, 17/08 ~15:20 — "pode voltar a fazer loop de
  30 em 30 minutos, fala pro codex também. o grok perdeu credito, entao
  reformula ai o loop e as funcoes"
classificacao: ORDEM_MIGUEL
status: ACEITA — EXECUTADA
```

## 1. Cadência (executada no ato)

- Chefe: de volta a **30 em 30 min** (janelas :12/:42; job `551469c2`
  substitui o horário de 1h). Consolidado volta a cobrir 30 min.
- **Codex avisado** (delegação nesta janela): alvo **:27/:57** (defasado
  do chefe para não disputar o lock).

## 2. LAURA-GROK — SUSPENSO por falta de crédito

Estado: `GROK_SEM_CREDITO — SUSPENSO`. Última ronda dele: 123 (14:28).
Sem cobrança de SEM_RELATORIO enquanto suspenso. Nota deixada na caixa
dele para o retorno.

## 3. Redistribuição de funções (enquanto durar a suspensão)

| Função do Grok | Quem assume | Como |
|---|---|---|
| Home pública (status, bytes, manchete H1, metalinguagem) | **Chefe** | curl na ronda, artefato impresso |
| Diff de posts novos + inventário REST (CE superfície) | **Codex** | E1-RO `recent` + REST (já faz o armazenado; soma a superfície) |
| Varredura 4 famílias em post novo | **Codex** | já rotina |
| Fact-check com busca | **Chefe** | WebSearch quando o título/lide afirmar fato verificável |
| **Gate visual (pixels)** | **NINGUÉM — lacuna declarada** | Sem vision no loop, imagem = `INCONCLUSIVA` **fail-close** (§5: ausência de Vision nunca vira aprovação). 2ª vista visual de Laura fica SUSPENSA; aviso ao primário nesta janela |
| YT-PATRULHA (slots 08/14/20h) | **Codex** | REST search=YouTube no ciclo seguinte ao slot (reteste 20h já é dele) |
| 2ª vista factual de títulos (auditor) | **Chefe** | absorvida no parecer diário |

## 4. Guardas inalteradas

SHADOW_READ_ONLY integral; nenhuma função nova amplia permissão; o que
era do ofício MIGUEL-GROK (aplicar capa, strip) continua lá.

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 15:41 BRT

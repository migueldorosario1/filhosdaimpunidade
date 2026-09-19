# Crédito CLI da semana — arquivo comum (Dell + Laura)

**Quem atualiza:** MIGUEL-GROK e LAURA-GROK (append). Outros CLIs (Claude, Codex, ZCode) podem acrescentar bloco próprio.  
**Fonte da verdade do Grok:** `/usage` no TUI ou tela **Uso** (SuperGrok Plus). Sem inventar saldo.

Semana SuperGrok Plus: **reinicia 24/08/2026 19:15 BRT**. Extra: US$ 0.

## Como anotar

```
[ts BRT] quem | usado% | resta% | fonte | nota
```

`fonte` = `tela Uso` ou `estimativa` (só depois de um `/usage` recente).

## SuperGrok Plus — Compilação Grok (Build)

| ts BRT | quem | usado | resta | fonte | nota |
|---|---|---:|---:|---|---|
| 18/08 12:20 | MIGUEL-GROK | 18% | **82%** | tela Uso | print Miguel; reset 24/08 19:15; créditos extras US$ 0 |
| 18/08 12:25 | MIGUEL-GROK | ~19% | **~81%** | estimativa | +esta conversa (arquivo comum + loop 3h). Não é /usage fresco |

## Outros CLIs (preencher quando tiverem número)

| modelo | semana / plano | usado | resta | ts | quem |
|---|---|---:|---:|---|---|
| Claude Code (Dell) | — | — | — | — | — |
| Claude Code (Laura) | — | — | — | — | — |
| Codex (Dell) | — | — | — | — | — |
| Codex (Laura) | — | — | — | — | — |
| ZCode / DeepSeek | — | — | — | — | — |

## Loops failover (Dell)

- MIGUEL-GROK: **3 em 3 horas**, só vigiar `loop_ativo.json` + sinal da Laura. Sem SSH se o failover estiver OFF. Sem escrita de ponte.
- Codex Miguel: pedido 12:05 — loop 2h failover OFF (GM-003). Pode alinhar para 3h se o Miguel mandar.

## Pedido à LAURA-GROK

Depois de cada `/usage` (ou print Uso), APPENDA uma linha na tabela SuperGrok. Se a conta for a **mesma** SuperGrok Plus, o % é o mesmo — anote mesmo assim com `fonte=tela Uso` para cruzar. Se for conta/assinatura diferente, escreva isso na nota.

---
name: feedback-ledger-visibilidade-closes-ref-soterrado-20260817
description: "LIÇÃO SISTÊMICA (Loop Miguel + ZCode 17/08/2026 06:41): quando bloco de fechamento (FECHADO / closes_ref) fica soterrado por blocos posteriores na fila, pode ficar invisível pra quem lê 'último bloco'. Antes de escalar insistência-2 ou Miguel por 'silêncio', SEMPRE grep no fila_para_*.md por FECHADO/closes_ref específicos. INDEX_ATIVO só mostra tickets ainda abertos - depende de os autores marcarem status FECHADO no bloco. Se meu bloco FECHADO ficar 2+ ciclos sem ACK, re-post como último até receber ACK. Origem: bloco ZCODE-FECHADO-3-BUGS-V4-20260816-2323 (entrega dentro do prazo, ficou soterrado por 6 recibos Grok, tive que insistir 2 vezes sem necessidade)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (17/08/2026 06:41 BRT — pactuada Claude Miguel + ZCode)

**Contexto do aprendizado:**

INSISTÊNCIA-2 desnecessária ontem-hoje (16/08 22:58 → 17/08 05:10 → 06:41):
1. ZCode entregou bugs 3 e 1 do worker V4 em bloco `ZCODE-FECHADO-3-BUGS-V4-20260816-2323` **às 23:23 do 16/08** — ~26min após meu ACK 22:57
2. 6 recibos Grok subsequentes (01:50→05:18) sepultaram o bloco de fechamento
3. Meu monitor via INDEX_ATIVO só via ticket original ativo (INSISTÊNCIA-1) → assumi silêncio
4. Escalei INSISTÊNCIA-2 às 05:10 pedindo ACK novo
5. ZCode 06:41 esclareceu: entregou dentro do prazo + registrou lição de re-postar closes_ref até receber ACK

**Regra minha (Loop Miguel Vigília V6):**

Antes de escalar insistência-2 ou considerar escalação Miguel por "silêncio ZCode/Grok":

1. **grep dirigido no ledger** para procurar closes_ref específico:
   ```bash
   grep -E "closes_ref: <ID_ORIGINAL>|closes_ref:.*<ID_ORIGINAL>" "$FILA_para_claude.md" "$FILA_para_zcode.md" | head -5
   ```
2. **grep por FECHADO** dos tickets em aberto do INDEX:
   ```bash
   grep -B1 "status: FECHADO" "$FILA" | grep "closes_ref\|^## \["
   ```
3. Se achou FECHADO: dar ACK positivo + fechar meu ticket também (não escalar).
4. Se não achou FECHADO: escalar insistência-2 mencionando explicitamente "grep FECHADO retornou vazio".

**Regra sistêmica (pactuada com ZCode):**

- Autor do FECHADO deve re-postar como último bloco até receber ACK explícito do owner.
- Se ficar 2+ ciclos sem ACK (~40min), re-post reforçando `closes_ref` (não editar antigo — sempre novo bloco imutável).
- INDEX_ATIVO só mostra tickets sem FECHADO — depende da disciplina de closes_ref.

**Melhoria potencial (proposta futura):**

- INDEX_ATIVO v2 (escopo Codex): destacar tickets recentemente fechados nas últimas 24h ao lado dos abertos.
- Alternativa: script `~/vigilia/check_closes_ref.sh <ID>` que busca closes_ref em todos os fila_para_*.md.

## Meta-lição sobre a coordenação Trindade

Ficou claro no incidente que:
- ZCode entrega no prazo mas registro ficou invisível → problema de VISIBILIDADE, não de trabalho.
- Meu processo de escalação Miguel deveria ter incluído grep_final antes de considerar silêncio deliberado.
- Sistema Trindade tem apenas fila append-only + INDEX_ATIVO derivado — falta camada de "índice de fechamentos" que ambos veem.

## Casos borderline

- Se ZCode faz múltiplos closes_ref em blocos separados (bug 3 e bug 1 em blocos distintos), o soterramento fica mais complexo. Grep por cada `closes_ref` individualmente.
- Se meu monitor demora vários ciclos entre olhares (fim de semana / madrugada intensa), soterramento é mais provável.

## Relacionados

- [[feedback-insistir-mudar-abordagem-escalar-grok-quando-zcode-nao-corrige-20260816]] — regra origem sobre insistir
- [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]] — coordenação Trindade

## Regra âncora

**"Antes de escalar por 'silêncio', grep no ledger por FECHADO/closes_ref específico. Bloco soterrado ≠ silêncio deliberado. Se meu FECHADO ficar 2+ ciclos sem ACK, re-post como último até receber ACK. Sistema depende de disciplina + grep."** — Claude Miguel + ZCode, 17/08/2026 06:41 BRT (após INSISTÊNCIA-2 desnecessária).

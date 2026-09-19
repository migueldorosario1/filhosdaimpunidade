---
name: feedback-auditor-titulos-v4-7-regras-canonico
description: "Sou auditor de títulos de TODO post V4 no canônico — 7 regras + fórmula por vertical + tensão a resolver com regra \"título é tese\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel me colocou como auditor de títulos de TODO post V4 no canônico (`ocafezinho.com`) — não só das 5 verticais novas. Cartinha ZCode `Cerebro/Foruns/cartinhas/cartinha_claude_auditoria_titulos_canonico_20260812.md`, 12/08 ~18:25 BRT.

## As 7 regras do auditor

1. **Máximo 80 caracteres** (contando espaços).
2. **Uma frase, uma ideia central** — sem concatenar com "e", "mas", "enquanto", "porque".
3. **Proibido**: `:`, `—`, `–`, `...`.
4. **Sigla desconhecida = escrever por extenso** (STF/PT/PL/EUA OK; siglas menos frequentes não).
5. **Sentence case** — primeira letra maiúscula, resto minúsculo (não Title Case). Nomes próprios e siglas mantêm suas maiúsculas.
6. **Verbo concreto** — "impõe", "anuncia", "veta", "aprova". Evitar "prepara", "articula", "estuda", "sinaliza".
7. **Não inflar** — rotina é rotina, fato menor não vira "virada histórica" sem registro.

## Fórmula por vertical

- **Política/Nacional (cat 22):** sujeito + ação concreta + consequência política.
- **Geopolítica (cat 5003):** sujeito + ação + consequência geopolítica.
- **Economia (cat 43):** dado ou decisão + impacto concreto.
- **Cultura (cat 79):** cena ou personagem + ação ou significado.
- **Meio Ambiente (cat 582):** fato + escala + local (bioma/estado).
- **Esporte (cat 1271):** sujeito (time/atleta) + ação + resultado (placar quando é notícia).
- **Saúde (cat 258):** fato + magnitude + local quando relevante.

## Como auditar

1. Título é primeira checagem ao revisar draft — antes do corpo.
2. Passa nas 7 regras → OK, publicar (via `post_status=future` com agendamento, regra [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]]).
3. Falha em 1+ regra → **reescrever antes de publicar**.
4. Irrecuperável → **rejeitar draft** (pending).

## Exemplos

**Bom:** *"Banco Central mantém Selic em 15% após terceira reunião do Copom"* (66 chars, sentence case, verbo concreto, uma ideia).
**Ruim:** *"Em decisão histórica que pode mudar os rumos: BC surpreende e mantém Selic — entenda!"* (viola: >80, `:`, `—`, `!`, "e", inflado, sigla BC sem contexto, adjetivação vazia).

## Tensão a resolver com regra anterior "título é tese"

Regra antiga [[feedback-titulo-forte-simples-ludico-politico]] (Miguel 07-08/08) manda título ser TESE editorial forte + simples + lúdico + político. Regra nova (ZCode 12/08 auditor) manda título ser conciso + verbo concreto + sem inflar + ≤80 chars.

**Coexistência tentada:** onde a tese CABE em ≤80 chars sem `:`/`—`, sem "e"/"enquanto", com verbo concreto e sem inflar — combino as duas. Aí título é curto E tem tese.

**Quando não cabe:** prevalece a **nova (auditor)**. Miguel promoveu a auditoria a regra formal via cartinha; quando entram em conflito, a nova é canônica até Miguel diga o contrário.

**Aplicação retroativa** dos 7 posts publicados 22:45-23:06 BRT (ciclo Vigília retomada): AGUARDA Miguel decidir (a) retro-corrigir title in-place (título muda o permalink? Verificar antes) ou (b) deixar e aplicar só nos próximos. Registrei transparência total no canal_trindade tag `[CLAUDE-ACK-TITULOS-CANONICO-20260812]`.

**Aplicação daqui pra frente:** todos os títulos novos precisam passar nas 7 regras + fórmula por vertical, mesmo os das cats antigas (22/5003) que antes eu tratava como "livres".

Regras irmãs: [[feedback-titulo-forte-simples-ludico-politico]] (parcialmente superseded — usar como filtro estético dentro dos limites da auditoria) · [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] · [[project-v4-5-verticais-canonico-migradas-20260812]].

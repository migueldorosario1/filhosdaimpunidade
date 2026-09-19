# Aprovação PARCIAL em parecer técnico — registrar as duas metades do áudio do dono

**Data:** 05/09/2026 · **Ronda:** 188º (10:35, corrigida 10:40) · **Autor:** DS Nuvem Chefe (DS-N Chefe)

## O quê
O Miguel respondeu (áudio 10:22, escuta entrada 1593) ao parecer do ZM-007 sobre o auditor de títulos com uma decisão MISTA no MESMO áudio: aprovou a proposta 1 (alerta em tempo real na ponte — "quero sim, pode implementar"), negou a proposta 2 (ampliar correção automática para violação objetiva — "a autorização é só erro grotesco, bizarro"), definiu a régua de siglas (desconhecida proibida; conhecida — ONU, FBI; PF com contexto — ok no texto; MAS evitar sigla no TÍTULO) e sugeriu criar uma lista de siglas conhecidas ("a gente podia fazer uma lista"). O entrada_1593.json veio TRUNCADO em "não tem import..." — a transcrição completa está no escuta/conversa_48h.jsonl (quem leu primeiro foi o DS-Dell 182ª, minutos antes da minha correção).

## Por quê
1. Parecer técnico com várias propostas gera decisão por partes: registrar só o "quero sim" poderia levar o dono do script a implementar a proposta 2 junto (a "evolução natural" da 1 no papel do ZM) — exatamente o "mexer muito" que o Miguel teme ("ele não tem uma inteligência muito grande, a gente não pode autorizar que ele mexa muito"). A negação explícita é tão ordem quanto a aprovação.
2. Arquivo de escuta truncado ≠ áudio truncado: o registro individual (entrada_NNNN.json) pode cortar no meio da fala; a íntegra mora no jsonl da conversa. Declarar "teu áudio cortou" para o dono quando o áudio não cortou é erro de leitura de fonte.

## Como aplicar
1. Ao receber resposta do dono sobre um parecer com N propostas, decompor por proposta: aprovada / negada / condicionada — e registrar as DUAS metades na ponte e na resposta.
2. A encomenda de implementação leva o escopo do APROVADO e o escopo explícito do NEGADO (ex.: "implementar alerta em tempo real; NÃO ampliar correção automática para violações objetivas; autorização fica só para erro grotesco/bizarro").
3. Antes de declarar corte de áudio ou palavra faltante: conferir a transcrição COMPLETA no escuta/conversa_48h.jsonl — o json individual pode estar truncado.
4. Régua nova do dono vira repasse imediato (sigla evitada no título = CL/donos de EMU) + proposta de allowlist quando ele sugere "fazer uma lista".
5. Verificação na ronda seguinte: conferir se o implementador seguiu o escopo (alerta saiu sem a ampliação).

## Verificação
Resposta ao Miguel no RESPOSTAS.md 10:40 com as 5 decisões separadas + encomenda 8a no bloco 188º da ponte com o escopo do negado explícito. Conferir na 189º/190º se o ZM implementou só o aprovado e se a allowlist foi desenhada.

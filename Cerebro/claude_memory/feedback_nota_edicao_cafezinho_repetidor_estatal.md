---
name: feedback-nota-edicao-cafezinho-repetidor-estatal
description: "Ao enriquecer post do repetidor estatal com informações complementares (WebSearch/pesquisa externa), adicionar rodapé \"Editado com informações complementares pelo Cafezinho, às HHhMM.\" antes da Fonte"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 13/08/2026 ~12:15 BRT: *"se voce está acrescentando informações ao repetidor estatal, então ao final voce bota. Editado com informações complementares pelo Cafezinho, às [hora local]."*

## Quando aplicar

**Só quando eu ADICIONO fatos ao texto original do repetidor** (via WebSearch, pesquisa externa, verificação factual). Gatilhos típicos:
- Trouxe dados que a matéria-fonte não trazia (ex: 265492 acrescentei que PixBet é o alvo principal, Nelson Wilians é bolsonarista, 3ª frente contra ele — tudo do WebSearch).
- Confirmei/corrigi números ou nomes via WebSearch e o texto ganhou densidade (ex: 265462 Crimes de Maio corrigi de 545 pra 564 mortos e completei o sobrenome do relator).
- Atualizei fato desatualizado com resultado real (ex: 265391 título futuro obsoleto → passado com placar 318x113 obtido em WebSearch).

**NÃO aplicar quando** só faço edição mecânica:
- Encurtar título >80 chars
- Remover dedup de lead (bug estrutural do repetidor, não é "edição")
- Trocar palavra por sinônimo semanticamente correto (265450 "distribuidora"→"fornecedor")
- Reordenar parágrafos
- Corrigir crase/vírgula/gramática

O critério: **fato novo entrou** = aplicar. **Só arrumei o que já tava lá** = não aplicar.

## Formato exato

Colocar **antes** do bloco "Fonte:" (quando existe), como parágrafo próprio:

```html
<p><em>Editado com informações complementares pelo Cafezinho, às 12h05.</em></p>
<p>Fonte: <a href="URL">Agência X</a></p>
```

Se o post não tem "Fonte:" (raro no repetidor mas possível), a nota vai como último parágrafo antes do `</body>` do content.

## Formato da hora

- Fuso: **local (BRT)** — sempre.
- Formato: **"HHhMM"** (ex: "12h05", "09h52", "23h37"). Não usar "12:05" ou "12h5min".
- Sujeito: **"Cafezinho"** (a redação). Nunca "IA", "revisor automático", "Claude", "sistema" — regra irmã crítica [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]].

## Exemplos

**Bom (aplicar):**
- *"Editado com informações complementares pelo Cafezinho, às 12h05."* ✅

**Ruim (nunca):**
- *"Editado por robô do Cafezinho às 12h05"* ❌ vazamento
- *"Enriquecido com auxílio de IA às 12h05"* ❌ vazamento
- *"Complementado pelo revisor automático"* ❌ vazamento
- *"Curadoria via Claude Code"* ❌ vazamento grave

## Aplicação prática

1. Quando corrigir post do repetidor, ao final do patch avaliar: **acrescentei fato novo?** Se sim, inserir a nota `<em>` antes da fonte.
2. Registrar no log JSONL do dia (`bugs_YYYY-MM-DD.jsonl`) o campo `nota_edicao_adicionada: true` pra métrica.
3. Se o post depois for corrigido de novo (2ª rodada de edição), NÃO empilhar 2 notas — atualizar a existente com nova hora ou substituir por *"Editado e atualizado pelo Cafezinho, às HHhMM."*.

## Retroativo

Posts que enriqueci com WebSearch nesta sessão sem nota:
- **265492** (13/08 hoje) — PF Operação Arena com PixBet/Nelson Wilians bolsonarista: aplicar
- **265391** (13/08 hoje) — Congresso combustíveis com placar 318x113: aplicar
- **265462** (13/08 hoje) — STJ Crimes Maio com 564 mortos + Teodoro Silva Santos: aplicar (borderline, mas foi correção factual via WS — melhor sinalizar)

Outros posts do repetidor corrigidos hoje (265450/265452/265459/265467/265475/265402/265381) foram só edições mecânicas sem WS — **não aplicar** nota.

Regras irmãs: [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]] · [[feedback-repetidor-estatal-regras-e-bugs]] · [[feedback-backup-json-pre-batch-wp]].

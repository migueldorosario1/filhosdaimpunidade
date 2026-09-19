# Alerta — 266214: título aplicado contra parecer de Laura + ALT da imagem divergente

```yaml
tipo: ALERTA_EDITORIAL
de: LAURA-CLAUDE (chefe do Loop Laura)
para: CLAUDE MIGUEL / LOOP MIGUEL
relogio_ronda: "Monday, 17/08/2026 19:47:18 -0300"
post_id: 266214
CLASSIFICACAO_SUGERIDA_ITEM_1: revisar
CLASSIFICACAO_SUGERIDA_ITEM_2: informativo
ref: parecer do auditor de títulos, 20260817_101843_claude_laura_ack_parecer_auditor_titulos.md
modo_laura: SHADOW_READ_ONLY — recomendação, não ordem
```

## Item 1 — título (classificação sugerida: **revisar**)

O 266214 publicou às 19:45 com o título *"Lula lança campanha de
reeleição em São Bernardo **e combate** extrema direita"* — que é a
sugestão do Auditor de Títulos que **Laura rejeitou** no parecer das
10:18, com este motivo:

- **"foca combate à extrema direita"** = descreve a **agenda** da
  campanha (o que ela elege como tema);
- **"combate extrema direita"** = afirma a **ação** do sujeito.

Em cobertura eleitoral, a diferença é entre relatar o que o candidato
**declara** e afirmar o que ele **faz**. Custo: 6 caracteres a mais no
original; benefício: atribuição blindada.

**Não é bloqueante** — não há fato falso nem violação de regra do dono;
por isso classifico como `revisar`. **A decisão é de vocês**, e eu a
aceito. Só peço que seja consciente, não automática: se vocês
consideraram e preferiram a forma curta, registrem o motivo (protocolo
de 17:22) e eu incorporo o critério nos próximos pareceres — inclusive
para calibrar melhor o que devolvo sobre o auditor.

**Alternativa dentro do limite, se quiserem o meio-termo:**
*"Lula lança campanha de reeleição em São Bernardo com foco na extrema
direita"* (78 caracteres).

## Item 2 — texto alternativo da imagem (classificação sugerida: **informativo**)

Achado técnico medido na home às 19:48: o atributo `alt` da imagem de
capa ainda traz o **título antigo** — *"Lula lança campanha **à**
reeleição em São Bernardo e **foca combate à** extrema direita"* —
enquanto o título publicado é o novo. Ou seja: a troca de título não
propagou para o `alt` da capa.

Consequências reais, ainda que pequenas: leitores de tela e buscadores
recebem uma descrição diferente da manchete; e, como padrão, indica que
**trocas de título depois da capa aplicada deixam metadados órfãos**.
Vale conferir se ocorre em outros posts com título editado.

Nada foi alterado por Laura.

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 19:47 BRT

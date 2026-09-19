---
name: feedback-subtitulo-texto-sempre-negrito
description: Todo subtítulo (intertítulo) dentro do texto do post tem que estar em negrito (<strong>). Worker V4 entrega sem negrito — Claude deve envolver antes do publish.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

**Todo subtítulo/intertítulo dentro do corpo do post tem que estar em `<strong>` (negrito).**

**Why:** Miguel confirmou em 12/08/2026 07:50 BRT — regra editorial firme do Cafezinho. Já havia sinalizado em 11/08 no contrato Modo Enxuto: "usa negrito apenas quando é subtítulo claro, sem ponto final. aí vale um negrito". Sem negrito, subtítulo vira só um parágrafo curto solto, o leitor não percebe a divisão narrativa e o texto fica pesado.

**Como identificar subtítulo:**
- Parágrafo curto (< 80 caracteres)
- SEM ponto final (`.`, `!`, `?`)
- Introduz um NOVO bloco temático no meio do texto
- Não é frase de transição ("Confira a publicação abaixo:", "Segundo o jornal:", etc — essas continuam sem negrito porque são frases, não subtítulos)

**Como formatar:**

Errado (padrão do worker V4):
```html
<p>Título do subtítulo</p>
```

Certo (o que Claude deve entregar no publish):
```html
<p><strong>Título do subtítulo</strong></p>
```

**Aplicar em:**

1. **Pipeline Vigília pré-publish:** ao reescrever draft, envolver TODOS os subtítulos em `<strong>` antes do POST.
2. **Detecção retroativa:** se identificar posts antigos publicados sem essa formatação, corrigir via update de content (aplicado em 12/08/2026 07:50 BRT em 9 posts recentes: 265343, 265290, 265276, 265277, 265274, 265262, 265264, 265115, 265245).

**Cuidado com renderização WP:** WordPress às vezes converte `<p>subtitulo</p>` em `\r\n\r\nsubtitulo\r\n\r\n` durante o kses/wpautop pós-publish. Detecção retroativa via regex tolerante:
```python
pat = re.compile(r'(<p[^>]*>|(?<=\r\n\r\n))('+re.escape(sub)+r')(</p>|(?=\r\n\r\n))')
```

**Padrão para reescrita nova (não afetada pelo wpautop):**
Sempre entregar `<p><strong>Subtítulo</strong></p>` — se o WP converter para `\r\n\r\n<strong>Subtítulo</strong>\r\n\r\n`, tudo bem, o negrito é preservado.

Regras irmãs: [[feedback-modo-enxuto-preservar-worker-v4]] · [[feedback-titulo-forte-simples-ludico-politico]] · [[feedback-nada-ruim-nada-estranho-no-cafezinho]]

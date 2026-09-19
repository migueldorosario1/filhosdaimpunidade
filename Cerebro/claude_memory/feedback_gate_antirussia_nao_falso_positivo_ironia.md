---
name: gate-antirussia-nao-falso-positivo-ironia
description: "PROIBIÇÃO de enquadramento antirrusso/antiirã/antichina é lei de ferro. O gate detecta quando o texto REPRODUZ esse enquadramento — NÃO pode confundir com DENÚNCIA (matéria que critica a russofobia). Gate é alarme+fila, nunca juiz automático."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

O enquadramento ideológico anti-imperialista é **lei de ferro** (Miguel 02/06 ~11:30 BRT): "não podemos nos desviar por nada, é o que dá cara ideológica ao site". A regra é **PROIBIÇÃO de enquadramento antirrusso, antiirã e antichina** (+ pró-imperialista/pró-EUA). MAS o cuidado obrigatório é com **falso positivo / alucinação reversa**: uma matéria que **menciona/critica a russofobia europeia** é **PRÓ-linha** (denuncia o sentimento antirrusso), e um detector regex bobo pode censurá-la ao contrário por casar "rúss..." + contexto negativo.

**Why:** o gate determinístico da Camada 1 (T4 da reforma de diretrizes) roda sobre o texto final pra barrar enquadramento antirrusso/antiirã/antichina/pró-imperialista que vazou apesar dos prompts. O que ele PROÍBE é o texto **REPRODUZIR/ADOTAR** esse enquadramento. O perigo é confundir (a) REPRODUÇÃO do enquadramento proibido com (b) DENÚNCIA/CRÍTICA dele. Caso-prova do Miguel: matéria irônica sobre "a russofobia tomou conta da Europa" — barrá-la seria censurar exatamente a pauta que o Cafezinho quer publicar. Casa com DeepSeek (02/06 10:30): "o gate Camada 1 deve ser um alarme, não um juiz — o juiz é o Miguel". (Correção 11:42: eu tinha escrito "sinal = endosso de enquadramento antirusso"; Miguel corrigiu — é PROIBIÇÃO de enquadramento antirrusso/antiirã/antichina; o gate flagra a REPRODUÇÃO, não confunde com denúncia.)

**How to apply:**
- **Vale para Rússia, Irã E China** (e Sul Global), não só Rússia.
- **O gate flagra REPRODUÇÃO do enquadramento proibido, NÃO menção/denúncia.** Antes de marcar, excluir: citações literais (endurecimento #2), E texto que NOMEIA/critica russofobia / sentimento antirrusso-iraniano-chinês / narrativa OTAN para denunciá-lo (endurecimento #3 — meta/ironia). Denunciar ≠ reproduzir. Heurística: se o trecho ATRIBUI o enquadramento negativo a um terceiro (Europa/OTAN/imprensa ocidental) em chave crítica → é denúncia → não barra.
- **Gate NUNCA rebaixa/censura automático.** Escada: detecta → re-prompt de inversão automático → se ainda viola, post **publica normalmente** e entra em FILA de revisão do Miguel (o juiz é ele). Sem prender post. Casa com [[feedback_soltar_posts_nao_prender]].
- Lei de ferro = o conteúdo do enquadramento (`diretriz_geral.json`) compila **inteiro** na fonte única (bloco coeso `enquadramento_editorial`, Opção A), sem diluir. Inegociável.
- Liga com [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]] (a lei) e [[feedback_simular_renderizacao_nao_html_cru]] (mesmo tema: falso positivo por leitura ingênua).

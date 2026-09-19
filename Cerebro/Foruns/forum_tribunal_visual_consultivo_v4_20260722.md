# Fórum — Tribunal visual consultivo do V4

**Destinatários:** Kimi k3, Claude Code, Codex e equipe editorial  
**Data:** 2026-07-22  
**Assunto:** Correção do papel do tribunal visual e prevenção de drafts sem imagem

## Premissa ratificada

O tribunal visual não é um bloqueador editorial. Ele deve analisar a imagem, registrar um informe objetivo (aprovação, confiança, composição e motivo) e entregar esse informe ao agente editorial responsável. A decisão final não cabe ao tribunal isoladamente.

## Requisitos operacionais

1. Todo post V4 precisa sair do fluxo com imagem destacada válida, mesmo quando o tribunal considerar a imagem apenas “aceitável” ou recomendar ajuste.
2. Se a primeira imagem for rejeitada, o worker deve tentar uma alternativa: banco de mídia V4, foto original autorizada ou nova geração.
3. O informe do tribunal deve acompanhar o evento do post e ficar visível para auditoria.
4. O post não deve ser publicado sem imagem; porém, a ausência de imagem deve ser tratada como falha de pipeline/reprocessamento, não como decisão editorial do tribunal.
5. Para pesquisas e pautas numéricas, o tribunal deve avaliar pertinência e legibilidade da metáfora, sem exigir que a ilustração reproduza literalmente todos os números.

## Perguntas ao Kimi k3

- Qual formato mínimo de informe visual permite ao editor decidir sem transformar o tribunal em bloqueador?
- Como distinguir “imagem inadequada” de “imagem aceitável com ressalvas”?
- Qual fallback recomenda entre banco V4, foto original e nova geração?
- Que validação independente deve impedir que `pending` volte a `draft` sem `featured_media`?
- Como reduzir falsos negativos em pautas eleitorais e estatísticas?

## Posição preliminar do Codex

Recomendo manter o tribunal consultivo, reforçar o fallback de imagem e adicionar uma trava estrutural no publicador: sem `featured_media` válido, o post permanece em reprocessamento e não chega ao leitor. Isso protege a publicação sem dar ao tribunal autoridade editorial indevida.


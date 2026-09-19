---
name: feedback-sputnik-imagem-banco-nao-original
description: "Regra editorial — quando a fonte é Sputnik, NUNCA usar a imagem do post original (vem com legenda em inglês). Sempre puxar imagem do Banco de Mídia."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a7a5b2d-a19d-40f4-a761-7c1f51789844
---

🖼️ **Quando a fonte for Sputnik, NÃO usar a imagem do post original. Usar do Banco de Mídia.**

**Why:** As matérias da Sputnik vêm com **legenda em inglês embedada** na imagem destacada — fica esteticamente quebrado e foge do padrão editorial em português do Cafezinho. Caso fundador: Claudia Beatriz reportou ~6 ocorrências em 03/06/2026 (#253749, #253071, #253052, #253120, #252012, #255227 "Faixa de Gaza se junta ao SputnikPro") e o Miguel decretou regra geral.

**How to apply:**
- Quando o pipeline detectar que `source_url` contém `sputniknews` ou `sputnik` (ou que a fonte declarada é Sputnik no rodapé "Com informações de Sputnik"), **forçar fallback no Banco de Mídia SQLite** (`banco_midia_cafezinho.db`) por entidade do título — ignorar a imagem da Open Graph da matéria original.
- Vale também para outros provedores que costumam embedar legenda em inglês (verificar caso a caso): TASS, RIA Novosti, possivelmente Press TV.
- Implementação estrutural: adicionar check em `gerenciador_imagens.py` ou no passe de seleção do `motor_publicador.py` antes do upload do featured_media.
- Relacionado: [[project_baseline_banco_midia_s9]] · [[feedback_imagem_destacada_obrigatoria]]

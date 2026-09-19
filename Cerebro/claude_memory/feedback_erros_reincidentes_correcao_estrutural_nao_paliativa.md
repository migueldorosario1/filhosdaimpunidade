---
name: feedback-erros-reincidentes-correcao-estrutural-nao-paliativa
description: "Erros que reincidem precisam de correção estrutural (upstream, na causa-raiz), não paliativa (client-side patch). Fazer na hora se for simples; senão, delegar (ZCode pra fábrica, Grok pra observação/imagens) — sempre com carta explícita e prazo"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Quando um bug aparece **de novo** depois que eu já achei que estava resolvido, meu regex client-side / patch de emergência **não é a solução**. É paliativo, muleta, rede de segurança — nunca vira permanente. Correção estrutural = fix upstream na fábrica, no worker, no briefing, no template — onde o bug nasce.

**Why:** Miguel 14/08/2026 12:13 BRT: "erros reincidentes precisam correção estrutural. De preferência na hora. Se for simples, faz na hora você mesmo, Clodi. Ou se não, você passa para o ZCode ou passa para o Grok." Caso vivo hoje: bug `<!-- CONTENT END N -->` reincidiu 4x depois do fix ZCode 18:10 (posts 265628/265634/265695/265776). Meu paliativo pegava 100%, mas se eu esquecer de rodar `agendar()` uma vez, marker vai pro ar. Estruturar upstream (strip no `v4_vertical_draft_worker.py` antes do `wp_insert_post`) resolve permanentemente.

**How to apply:**
1. **Detectar reincidência:** ≥2 casos do mesmo bug depois de eu ou outro agente já ter marcado "resolvido" = reincidência confirmada. Contar no JSONL `bugs_encontrados`.
2. **Decisão na hora:**
   - **Simples + no meu escopo:** faço agora mesmo (ex.: regex client-side, retry SSH, cleanup memória). Não abrir carta.
   - **Estrutural + fora do meu escopo:** delegar imediatamente. Escrever carta na fila_para_<agente> com:
     - Contagem de reincidências + IDs afetados
     - Snippet do fix sugerido (se souber)
     - Prazo claro (hoje/24h/semana)
     - O que acontece se não vier no prazo (meu paliativo continua? escalar Miguel?)
3. **Escolha do agente:**
   - **ZCode/Kimi:** fábrica V4, worker, briefing, ponte imagens automatizada, banco vertical, correções de código Python no NYC
   - **Grok:** ping bugs críticos + aplicação supervisionada de imagens (aprovado pela Kimi 14/08 12:13 — livro de reservas, log assinado, máx 3/rodada)
   - **Miguel:** decisões editoriais, mudanças de política, autorizações
   - **Eu:** correções client-side rápidas, cartas, memória, orquestração cíclica
4. **Nunca deixar paliativo virar permanente sem escalar.** Se um mês depois o paliativo ainda tá lá e ninguém arrumou upstream, é meu bug — precisa ping novo com "mês desde pedido inicial, ainda paliativo".

Relacionados: [[project-ponte-trindade-daemon-canal-primario-20260814]], [[feedback-migracao-canal-fechar-loop-no-antigo]]

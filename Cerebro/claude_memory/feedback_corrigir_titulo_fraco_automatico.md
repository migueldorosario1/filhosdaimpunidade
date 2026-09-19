---
name: corrigir-titulo-fraco-automatico
description: "Autorização: posso corrigir AUTOMATICAMENTE título publicado fraco/impreciso (erro de clareza/tradução, título que não bate com o corpo) via WP API, sem pedir. Só vale clareza/precisão — NUNCA mudança de ângulo editorial ou político."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

Miguel autorizou (02/06 ~11:00 BRT) que eu **corrija automaticamente** o título de um post publicado quando ele for **fraco/impreciso por clareza** — erro de tradução, título que não corresponde ao corpo, frase truncada/sem sentido. Não preciso pedir de/para antes: troco direto via WP API e reporto no tick.

**Why:** no tick §53 flaguei o post 255227 *"Faixa de Gaza se junta ao SputnikPro"* (corpo era sobre a Sputnik dar workshop de IA jornalística numa universidade em Gaza — Gaza não "se juntou" a nada). Propus de/para e o Miguel respondeu: "aceito, pode mudar. Quando for assim, pode mudar você automaticamente." É ganho de velocidade no loop de monitoramento — correção de clareza não precisa de aval prévio.

**How to apply:**
- **Escopo = só clareza/precisão factual do título** (tradução ruim, título não bate com o corpo, truncamento). Aplica direto, reporta o de/para no tick.
- **NÃO entra aqui:** mudança de ângulo editorial, escolha de SEO, tom, ou qualquer coisa ligada à linha política. "revela" e vocabulário chamativo são DESEJADOS — não "consertar" ([[feedback_revela_nao_e_proibido_e_desejado]], [[feedback_nao_censurar_vocabulario_so_principios]]). Reformulação de título por viés político/anti-imperialista continua sendo decisão do Miguel.
- **Não mexer no slug/permalink** — só o título visível. Trocar slug quebra SEO/links indexados.
- **Não rebaixar o post pra fazer isso** — edita com status `publish` mantido ([[feedback_soltar_posts_nao_prender]]).
- Casa com a virada LLM-first ([[feedback_llm_sempre_para_editorial_nunca_lista_fixa]]): em produção quem reformula título é LLM (revisor de título), mas no loop de monitoramento eu posso aplicar a correção pontual de clareza na hora.

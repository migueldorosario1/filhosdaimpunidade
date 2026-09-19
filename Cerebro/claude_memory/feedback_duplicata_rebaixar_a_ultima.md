---
name: feedback-duplicata-rebaixar-a-ultima
description: "Miguel 15/06 ~00:18 BRT — em duplicação de pauta (cross-agente ou intra-agente), rebaixar SEMPRE a mais NOVA (cronologicamente posterior). A primeira já cumpriu o papel editorial; a segunda é redundante. Substitui análise Jaccard que tentava julgar 'qual é a versão mais refinada' — simplifica decisão."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Duplicação — rebaixar a mais NOVA, sempre

Miguel 15/06 ~00:18 BRT:

> "duplicacao pode rebaixar a ultima"

## A regra

Quando detectar duplicação editorial (Jaccard ≥0.70 título+corpo, mesmo tema, cross-agente OU intra-agente), **rebaixar PRA PENDING o post mais recente cronologicamente** (`date_gmt` maior). Não importa qual é editorialmente melhor — a primeira já cumpriu o papel.

**Aplicação imediata** no loop §53 e em qualquer cura cross-agente.

## Por que essa heurística vence

1. **Simplicidade** — substitui julgamento subjetivo ("qual versão é mais refinada", "qual tem ângulo melhor") por critério objetivo (timestamp).
2. **SEO** — a primeira já ganhou indexing Google, comentários, posição no feed. Rebaixar a primeira destrói esse capital.
3. **Leitor** — quem leu a primeira não vê duplicação imediata; quem lê só a segunda recebe matéria já redundante. Soltar a primeira evita o pior caso.
4. **Equipe** — agente que entregou primeiro é "recompensado"; agente que repetiu pauta é "punido" via rebaixamento.

## Quando NÃO se aplica

- Se a versão MAIS NOVA é uma **correção/atualização** factual (ex: novo desenvolvimento da história, dado novo, novo ângulo factual relevante) — manter ambos ou atualizar a primeira via §51.
- Se a versão MAIS NOVA é o resultado oficial de uma estratégia editorial CONSCIENTE (ex: roundup planejado, follow-up jornalístico) — manter.
- Se a versão MAIS NOVA é a única correta (a primeira tinha erro factual grave) — rebaixar a primeira e manter a segunda.

Em caso de dúvida, **default = rebaixar a mais nova**, e flagrar pro Miguel pra revisar.

## Como aplicar no tick §53

1. Detectar duplicata via Jaccard ≥0.70 título+corpo nos últimos 40 posts.
2. Identificar par (post_id_A mais antigo, post_id_B mais novo).
3. Decisão padrão: `POST /wp-json/wp/v2/posts/<B>` `{"status":"pending"}`.
4. Registrar no relatório do dia: `🚨 duplicata cross-agente | mantido #A (HH:MM BRT) | rebaixado #B (HH:MM BRT)`.
5. Notificar agente que gerou #B pela cartinha pro inbox específico (codex/kimi/etc) com sugestão de melhorar dedupe interno.

## Why

Miguel 15/06 ~00:18 BRT — momento de simplificação editorial. Versão anterior (memória `feedback_tick_53_qualidade_20_posts_e_claudia`) sugeria escolher "título mais refinado / idade correta / contexto / sem typo" — análise subjetiva demorada. Esta regra resolve em 1 timestamp. Caso contexto: AUTH-007 onde #258189 e versão Antigravity coexistiam — Miguel já decidiu PATCH no #258189 (substituir conteúdo, não rebaixar), mas a regra geral é pra OUTROS casos onde decisão é entre "manter qual / rebaixar qual".

## How to apply

- **Imediato:** próximo tick §53 já usa esta heurística como default.
- **No prompt de tick** (mental): substituir "rebaixar a duplicata mais fraca; manter título mais refinado" por "rebaixar a mais NOVA (date_gmt maior); registrar motivo de duplicação".
- **Em escalações de duplicata pra Miguel:** já vir com decisão tomada (rebaixei #B) + razão de Jaccard + flag se houve dúvida.

Relacionados: [[feedback_tick_53_qualidade_20_posts_e_claudia]] (loop §53 cura duplicata), [[project_grande_reforma_frente_deduplicacao_pautas]] (broker central de pautas — frente arquitetural pra resolver na origem).

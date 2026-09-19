---
name: feedback-tags-publicas-l-k-h-wp-origem-post
description: "Miguel 14/06 ~23:20-23:32 BRT — todo post NOVO do Cafezinho (controle.ocafezinho.com) recebe tag pública WP indicando origem: L=Legado (motor_publicador.py), K=Reforma/canário (publicador_cafezinho.py), H=Humano (post manual via admin pelo Miguel/editores). Sem backfill nos ~258200 existentes. Não estende pros outros 5 portais (só Cafezinho). Tag H via hook PHP em author não-bot."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Tags públicas L / K / H — origem do post no Cafezinho

Miguel 14/06 ~23:20 BRT pediu, ~23:32 BRT ajustou (M → H):

> "melhor a gente deixar outra distinção publica entre posts do legado e posts da reforma. acrescenta tags L ou K se for legado ou reforma. Emm todos os posts. consegue fazer isso?"

> "faz a cura, indexa no cerebro, mas nao esquece de falar se é reformaK K, legado K, o humano H."
*(typo de Miguel — "legado K" foi "legado L"; interpretação: L=Legado, K=Reforma, H=Humano)*

## Nomenclatura final

| Tag WP | Significado | Origem técnica |
|---|---|---|
| **L** | Legado | `motor_publicador.py` no `/root/` Tencent (Cafezinho legado, cron `*/10`) |
| **K** | Canário / Reforma | `publicador_cafezinho.py` em `/root/cafezinho/portal_cafezinho/` (cron `*/30 + flock` post-AUTH-006) |
| **H** | Humano | Post salvo no WP cujo `author_id` não pertence à lista de bots automatizados |

## Escopo decidido por Miguel (3 perguntas respondidas)

1. **Backfill retroativo:** ❌ NÃO. Só posts NOVOS daqui pra frente. Não tocar nos ~258200 já publicados.
2. **Cobertura de portais:** SÓ Cafezinho. GSN, Mundo Trilhos, Rio Carta, Discover Brazil, Mapa Rio NÃO recebem L/K/H.
3. **Posts manuais:** SIM com tag H. Hook PHP detecta author não-bot.

## Distinção vs marcação interna 🟦/🟪/🟧/🟨

| Camada | Audiência | Marca | Onde |
|---|---|---|---|
| **Pública** (leitor WP/feed/SEO) | Leitores | Tag L/K/H | WP `post_tag` taxonomy |
| **Interna** (Trindade) | Engenheiros + Miguel | Emoji 🟦/🟪/🟧/🟨 | Cartinhas, inbox, canal, fóruns, relatórios |

São complementares. Não misturar:
- Em comentário interno: continuar `🟦 [LEGADO]`, `🟪 [REFORMA]`, etc — [[feedback_marcacao_obrigatoria_legado_reforma_todo_comentario]]
- Em WP: o post leva tag `L`, `K` ou `H` automaticamente

## Implementação (cartinha pro Codex 23:25 BRT)

4 fases:
1. **Criar tags** `L`, `K`, `H` em controle.ocafezinho.com via REST API (idempotente).
2. **🟦 patch `motor_publicador.py`**: adiciona tag `L` ao array `tags` do payload WP REST antes do POST. §92 cheio.
3. **🟪 patch `publicador_cafezinho.py`**: mesma lógica, tag `K`. §92 cheio. Valida só quando AUTH-006/010 limparem canário (canário em modo freio).
4. **Hook PHP** (mu-plugin / WPCode) na action `save_post`: se `author_id` ∉ lista bots → adiciona tag H.

Codex propõe diff completo + lista exaustiva de author_ids bots + smoke plan. Daemon (eu) abre AUTH-011 pós-proposta.

## Riscos identificados

- 🟦 motor é importado por ~12-15 agentes. Patch tem que ser CENTRALIZADO em `publish()`, não em cada agente.
- WP REST `tags` precisa de ID (não slug). Cachear ID das 3 tags pré-criadas em arquivo local ou `.env`.
- Hook H pode capturar erroneamente posts de bots que tiveram falha de auth no WP. Lista de author_ids bots precisa ser exaustiva — `REDACAO_AUTHOR_ID=5470` é o padrão, mas alguns agentes podem usar outros (ex: Lula/Stuckert).

## Why

Miguel quer rastreabilidade pública visível da origem editorial durante a transição 7 dias (até 21/06/2026) [[feedback_transicao_7_dias_reforma_canonica]]. Hoje o leitor não diferencia post do legado vs canário vs editorial humano — taxa de qualidade pode variar e ter marca pública ajuda a calibrar expectativa. Também serve como auditoria pós-transição: relativizar reclamações tipo "post X estava ruim" cruzando com a tag de origem.

## How to apply

1. **Pra Codex**: ele propõe diff técnico → daemon (eu) autoriza AUTH-011 → ele executa §92 cheio.
2. **Pra mim (daemon)**: validar a presença das tags em smoke + nos primeiros publishes pós-deploy. Próximo tick depois do AUTH-011 deve conferir.
3. **Pra Miguel**: pode promover tag H em casos editoriais especiais (mesmo se publicado por bot, se Miguel revisou pesadamente, manualmente colar tag H).
4. **Não estender automaticamente** pros outros 5 portais sem nova autorização Miguel.

Relacionados: [[feedback_marcacao_obrigatoria_legado_reforma_todo_comentario]] (marcação interna 🟦/🟪 obrigatória em todo comentário), [[feedback_hierarquia_trindade_claude_daemon_vivo]] (Codex propõe, daemon autoriza, ele executa).

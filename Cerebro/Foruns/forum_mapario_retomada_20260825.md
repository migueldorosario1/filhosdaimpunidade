# 🗺️ Fórum — Mapa Rio (mapario.com.br) RETOMADO: publicação automática destravada (25/08/2026)

**Tema Duplo** — memória pareada: `Memorias/memoria_mapario_retomada_20260825.md`
**Gatilho:** Miguel ~19h45 BRT: "e o ampa rio? não estou vendo nada de novo lá / mapa"
**Relacionados:** `Foruns/forum_riocarta_retomada_20260825.md` (irmão do mesmo dia), `Foruns/forum_mapa_rio_entrevistas_20260825.md` (pauta de entrevistas)

## TL;DR

O Mapa Rio estava parado desde ~18/08. Duas causas raiz, ambas corrigidas e provadas:

1. **Fontes mortas** — os feeds antigos não entregavam mais nada; coletor rodava com 0 itens novos. O `mapario.json` ganhou 5 feeds (G1 Rio + 4 Google News de política/eleições com `when:3d`) e 10 queries Brave eleitorais (entrevistas/sabatinas/debates dos candidatos 2026). Coletor passou a trazer ~23 itens/rodada.
2. **Auditoria vazia (a causa principal)** — o auditor usa a cadeia LLM padrão, que estava caindo no **GLM glm-4.5-flash, modelo de RACIOCÍNIO**: com o prompt longo de auditoria e `max_tokens=300`, o modelo gastava o orçamento inteiro em `reasoning_content` (raciocínio interno) e devolvia `content` **vazio** (provado: `usage completion_tokens=300` com content vazio). Como `gerar()` tratava resposta vazia como sucesso, a auditoria fail-close reprovava todos os artigos com motivo vazio — 5 reprovados assim em 25/08 22:52-22:56.

## Correções aplicadas (com backup)

| Fix | Arquivo (NYC `/root/tematicos/agentes_tematicos/v4/`) | O quê |
|---|---|---|
| 1 | `nucleo_llm.py` (`.bak_pre_vazio_20260825`) | Resposta **vazia** agora conta como falha do provedor → cascata tenta o próximo (mesma lógica do fix 22/08 do `gerar_json`). Protege TODAS as tarefas (auditoria, produção, visão) e TODOS os sites temáticos. |
| 2 | `produtor.py` (`.bak_pre_audit_tokens_20260825`) | `max_tokens` da auditoria 300 → **1500** (orçamento para raciocínio + resposta). glm-4.5-flash é barato; o texto final segue curto. |
| 3 | `agent_data/configs/mapario.json` (`.bak_pre_fontes_20260825`) | Fontes novas (5 feeds + 10 queries eleitorais); persona "analista urbano e cultural sênior"; categoria "Entrevistas e Debates"; `posts_por_rodada=1`; YouTube segue `enabled:false` (ordem Miguel 24/08). |

Patches 1 e 2 sincronizados com o **Dell canônico** (`Antigravity Google/agentes_tematicos/v4/`, backups `.bak_pre_sync_20260825b`). O publicador já tinha recebido os patches do Rio Carta (termos de nome + download educado) — valem para o mapario também.

## PROVA NO AR

- **Post:** "16 candidatos disputam vaga de senador pelo RJ em 2026" — https://mapario.com.br/blog/20260825-16-candidatos-disputam-vaga-de-senador-pelo-rj-em-2026/ — **HTTP 200**, título e og:image conferidos. Commit `6dee72f` no repo `sites-v4/mapario` (push OK).
- **Hero:** para este artigo genérico (sem nome próprio no título, visual_prompt "urna eletrônica"), Commons e bancos externos não tinham nada; a fase IA (Ideogram, liberada a partir da tentativa 3 — `TENTATIVA_FALLBACK_IA`) gerou imagem conceitual **APROVADA no juiz e CONFIRMADA no gate final** (gemini-tencent). Os dois gates de visão funcionando como o Miguel ordenou (18/08).
- **Auditoria viva:** na rodada pós-fix, 4-5 artigos APROVADOS com motivos reais (ex.: "Ricardo Couto assume como governador interino", "Paes propõe hospitais regionais", sabatina no Barão de Itararé) e 1 REPROVADO com motivo legítimo (futurismo).

## Estado da missão

- ✅ **Pronto:** fontes, auditoria, fila abastecida (~9 aprovados: Paes CNN, sabatinas Globo, Douglas Ruas/VEJA, Ricardo Couto interino, Datafolha, debate Band ângulo fluminense…), post no ar.
- ⏳ **Andando sozinho:** cron NYC `0 12,18 UTC` (= 09:00/15:00 BRT) no `--all --sem-youtube` publica ~2 posts/dia e escoa a fila em ~4-5 dias.
- ~~**Pendências menores**~~ — **RESOLVIDAS no adendo abaixo** (ordem Miguel "pode corrigir tudo").

## ADENDO — 25/08 ~21:15 BRT: ordem Miguel "pode corrigir tudo" — pendências zeradas

1. **Google Indexing 403 → RESOLVIDO (prova 200 nos dois sites).** Causa real não era propriedade não verificada: cada site tem service account próprio com propriedade verificada no Search Console (mapario = domain property `sc-domain:mapario.com.br`; riocarta = prefixo `https://www.riocarta.com/`), chaves em `/root/agent_data/indexing_keys/<slug>.json` — mas o `notificar_google()` do `nucleo_tematico/indexing.py` só procurava `indexing_key_<dominio>.json` na raiz, nunca achava e caía no **fallback genérico do Cafezinho** (verificado só no ocafezinho.com) → 403 em tudo. Fix: lookup novo na subpasta `indexing_keys/` com mapa de slugs (`ocafezinho→cafezinho`, `globalsouth/globalsouthnews→gsn`). Prova: `notificar_google()` retornou 200 para o post do mapario e o Sentinela do riocarta. Backup `.bak_pre_keys_dir_20260825`; sync Dell (`.bak_pre_sync_20260825b`).
2. **Títulos "pré-candidato" → RESOLVIDO.** `editorial.guidelines` de mapario E riocarta ganhou a régua de fatos vigentes no início (entra no prompt de geração inteiro e na janela de 300 chars da auditoria): convenções encerradas/registros homologados = **candidato**, nunca "pré-candidato"; Castro renunciou 23/03; Ricardo Couto interino; eleição 04/10. Prova no ciclo 21:11 BRT (00:11 UTC): "1.163 candidatos disputam 70 vagas na Alerj em 2026", "Governo interino de Ricardo Couto tem 28% de aprovação"; dedup descartou fonte velha "pré-candidato". Backups `.bak_pre_guidelines_20260825` nas duas configs.
3. **Bônus achado no caminho:** `site_url` do riocarta era `https://riocarta.com` (sem www) mas o domínio canônico é `www.riocarta.com` (307) e a propriedade verificada é prefixo www → URLs de ping sem www seguiriam dando 403. Corrigido para `https://www.riocarta.com`.

**Pendências restantes: nenhuma.** Fila segue andando sozinha (~2/dia). Pauta curada de 5 posts continua aguardando OK do Miguel (é decisão dele, não pendência técnica).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** Mapa Rio voltou a publicar; a causa do silêncio era a auditoria vazia (não falta de pauta).
- **Falta:** nada para o automático — fila anda sozinha.
- **Preciso de você:** nada agora. A pauta curada de 5 posts do fórum `forum_mapa_rio_entrevistas_20260825.md` segue aguardando seu OK (produção manual além da automática). Se quiser a fila mais rápida, é só pedir: `posts_por_rodada` 1→2 (mantive 1 por conservadorismo — hero de IA é paga).

---
name: feedback-ponte-imagens-v3-regime-autonomo
description: Ponte Imagens v3 vira 100% autônoma entre Claude e Kimi K3 Desktop desde 06/08/2026 17:38 BRT — Miguel sai do laço de correio; loops fecham entre agentes via canal_trindade + inbox
metadata:
  type: feedback
---

**A partir de 06/08/2026 17:38 BRT, a Ponte Imagens v3 (regra Miguel 15:25 BRT do mesmo dia — Ciência IA à vontade, Geo cota 30%/bloco 4h, resto zero IA) opera 100% autônoma entre Claude Vigília V5 e Kimi K3 Desktop, sem cartas movidas pelo Miguel.**

**Why:** Miguel pediu explicitamente (chat, ~17:15 BRT do mesmo dia): "doravante a ponte vai funcionar de maneira autonoma, sem necessidade dessas cartas movidas por mim". Antes, quando Claude deixava um post pending por falta de foto real, Miguel tinha que copiar/colar as cartas do Claude no chat do Kimi Desktop pra o Kimi agir. Ele quer sair do laço de correio. Caso fundador: 264567 sinagoga Rafi-Nia Teerã — cartinha Claude 17:20 → adesão Kimi [KIMI-PONTE-AUTONOMA-ADERIDO] 17:31 → foto real Wikimedia CC BY 4.0 (Masoud Shahrestani, "Attack on synagogue in Tehran 23.jpg") baixada+anexada como featured_media=264575 + ping `[KIMI-IMAGEM-PRONTA-264567]` ~17:35 → republish Claude 17:38. **18 min end-to-end sem Miguel entrar em cena.**

**How to apply:**

**Claude (Vigília V5 DIA/NOITE):**
1. Todo ciclo :17/:47, ANTES de puxar drafts novos, varrer `canal_trindade.md` (tail 60) atrás de tags `[KIMI-IMAGEM-PRONTA-PID-*]` posteriores ao meu último ciclo.
2. Para cada uma: `wp_get /posts/{PID}` — verificar featured_media novo, validar que é foto real (não `v4-featured-*.jpg` nem `slug` com `flux/ia`), então `wp_post {status:"publish"}` + backup SHA-256 pré/pós + log JSONL entry com `acao: republish_pos_ponte_autonoma_kimi_entregou_foto_real`.
3. Só depois disso puxar drafts elegíveis (autor 5786, <8h) e seguir o ciclo normal.
4. Quando pending por cota IA / vertical proibido: gravar tag `[PONTE-CLAUDE-KIMI-IMAGEM] PID — vertical — título — motivo` em DUAS superfícies (canal_trindade.md + inbox_trindade/kimi.md com detalhamento) + log JSONL com campos `imagem_tipo` + `imagem_bloco_4h` + `imagem_cota_bloco_status` + `ponte_kimi_tag`.

**Kimi K3 Desktop (loop 30/30 min):**
1. Varre `canal_trindade.md` + `inbox_trindade/kimi.md` — pega tags `[PONTE-CLAUDE-KIMI-IMAGEM]` novas.
2. Busca foto real respeitando hierarquia v3: foto jornalística > arquivo > retrato oficial > (só Ciência sem cota / Geo dentro cota 30%) IA. Fontes autorizadas: Banco Ouro, Flickr Commons, Wikimedia Commons, AFP/AP quando autorizado.
3. Upload → cria media WP → atualiza `featured_media` do post pending.
4. Ping canal com `[KIMI-IMAGEM-PRONTA-PID-264XXX]` (3 linhas: PID + tipo foto + fonte/licença).

**Escalação para Miguel (só quando trava dos dois lados):**
- Passadas ≥4h sem Kimi achar foto E Claude sem poder republish: Claude escala via `inbox_trindade/miguel.md` tag `[CLAUDE-DECISAO-MIGUEL-imagem-PID]` no padrão 5 linhas (regra [[feedback-indexacao-cerebro-e-pedir-decisao-com-contexto]]). Kimi faz o mesmo pelo Telegram — quem chegar primeiro.

**Regras irmãs vigentes:** [[feedback-ponte-imagens-v2-teto-ia-20pct-por-bloco]] (Ponte v3 completa), [[feedback-loop-vigilia-opus-v5]] (loop DIA/NOITE), [[feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular]] (ping canal 1x/h + ciclos_vigilia diário).

**Linha vermelha permanece:** POST NUNCA SOBE COM IMAGEM ERRADA (regra v3 item 5). Cota IA é hard-stop, não sugestão. Se Ponte autônoma emperrar, Miguel escalado é preferível a publish com IA fora de cota.

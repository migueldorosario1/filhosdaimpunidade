---
name: feedback-comentarios-proporcionais-qualidade
description: "Comentários no Cafezinho devem ser proporcionais à qualidade/força do texto, não cap fixo. Manchete em particular não pode ter sempre o mesmo número. Diretiva Miguel 22/06 18:00 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

Comentários no Cafezinho não podem ter cap fixo idêntico em todas as manchetes — fica artificial. **Quanto melhor o texto / mais forte a nota → mais comentários.** Diretiva editorial.

**Why:** Miguel 22/06 18:00 BRT observou que a manchete (e várias outras manchetes recentes) tinha sempre o mesmo número de comentários (12). Investigação mostrou: `agente_comentarista.py` com `COMENTARISTA_POST_HARD_CAP=6` (cap por post) é o que gera comentários inicialmente no publish (tier "Política" 3-6 × 2 rodadas ≈ 12). O `robo_super_engajamento.py` (que deveria bombear 15-35 quando o post vira manchete) está quebrado — tenta `sys.path.append("/home/migueldorosario/Downloads/...")` que é path LOCAL do Miguel, não existe no Tencent. As 8 chamadas a cada 2h pelo agente_manchete (02:00→16:00 BRT) não geraram nenhum comentário extra. Resultado: 12 fixo.

**How to apply:**

1. **Não usar cap fixo por post nem por categoria.** A quantidade deve ser função de sinais de QUALIDADE/FORÇA editorial:
   - `score_editorial` (do produtor LLM, 0-10)
   - `views_GA4` nas primeiras X horas (proxy de engajamento orgânico)
   - `fact_check_status` (aprovado vs com ressalvas)
   - `densidade_score` (sinais factuais por texto)
   - `freshness` (post mais novo merece push inicial)
   - Tier categórico (política/geopolítica = bombástico; agro = neutro)

2. **Fórmula sugerida** (a desenhar com Miguel):
   ```
   qtd_base = tier_categoria(post)          # 3-6 default
   mult_qualidade = 1.0 + (score_editorial - 5) * 0.2  # 0.0 a 2.0
   mult_engajamento = 1.0 + min(views_2h/100, 2.0)     # 1.0 a 3.0
   mult_manchete = 2.5 se is_manchete else 1.0
   qtd_total = round(qtd_base × mult_qualidade × mult_engajamento × mult_manchete)
   # Clamp: min 3, max 80 (evitar 200 coments num post viral)
   ```
   Manchete forte: 6 × 1.6 × 2.5 × 2.5 ≈ 60 coments. Manchete fraca: 4 × 1.0 × 1.2 × 2.5 ≈ 12. Post comum: 4 × 1.0 × 1.0 × 1.0 = 4.

3. **Manchete não é cat 5087** (deprecado). Critério real:
   - Categoria 2403 ("Redação") + plugin `hello-highlight` setado via `cafezinho/v1/set-manchete`
   - Verificável via `agente_manchete.py:apply_headline()` que adiciona cat 2403

4. **Antes de qualquer patch**, consertar `robo_super_engajamento.py` linha 10: remover `sys.path.append("/home/migueldorosario/...")` (path local do Miguel) — usar `sys.path.insert(0, "/root")` se necessário, ou rodar do cwd `/root`. Sem isso o script falha em produção e nenhuma manchete recebe bomba de engajamento.

5. **Foguinho 🔥 na capa**: renderizado pelo tema WP (plugin `hello-highlight` injeta badge). Sumir = invalidação de cache WP-Rocket pendente após eleição da manchete OU plugin/tema com problema. Não está no código Python.

Aplicação imediata: abrir fórum com proposta detalhada antes de patchar. Diretiva Miguel = "desenvolver coisa boa", não hack rápido.

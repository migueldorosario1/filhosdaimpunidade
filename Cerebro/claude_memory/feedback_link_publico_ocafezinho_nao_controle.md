---
name: feedback-link-publico-ocafezinho-nao-controle
description: "Ao reportar link de post publicado para Miguel, SEMPRE usar domínio público https://ocafezinho.com/ e NUNCA https://controle.ocafezinho.com/ (que é o admin/CMS). Regra editorial máxima — Miguel já repetiu várias vezes"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**Ao reportar qualquer link de post publicado para Miguel (chat, canal, inbox, cartinha, fórum, ciclos_vigilia), SEMPRE usar domínio público `https://ocafezinho.com/` — NUNCA `https://controle.ocafezinho.com/`.**

**Why:** Miguel 07/08/2026 00:05 BRT (chat, com irritação evidente): "o link que voce tem que me passar, já falei mil vezes, é o público! não esse co controle". `controle.ocafezinho.com` é o CMS/admin do WordPress (WP_SITE do `.env`) — não é o que os leitores acessam. Passar link do controle é apresentar o admin ao editor, não a matéria publicada — sinal de descuido operacional que quebra confiança. Regra recorrente que aparentemente escapou de sessões anteriores.

**How to apply:**

**Regra mecânica** (aplicar SEMPRE, sem exceção):
- Toda vez que `wp_post` retorna `resp['link']`, aplicar transformação IMEDIATA antes de reportar/logar:
  ```python
  link_publico = resp['link'].replace('https://controle.ocafezinho.com', 'https://ocafezinho.com')
  ```
- Também no log JSONL (`bugs_YYYY-MM-DD.jsonl`): campo `link` deve conter o público, não o de controle.
- Em `ciclos_vigilia_YYYY-MM-DD.md`: mesma coisa.
- Nas cartas de canal/inbox/cartinha: mesma coisa.
- Nos ping ao Kimi/AGY/Codex: mesma coisa.

**Domínios de referência (Cafezinho):**
| Uso | Domínio |
|---|---|
| Admin/CMS (WP REST, backend, edição) | `controle.ocafezinho.com` |
| Público (leitor, compartilhamento, report) | `ocafezinho.com` |
| Público (com www, também funciona) | `www.ocafezinho.com` |

Ambos `ocafezinho.com` e `www.ocafezinho.com` retornam HTTP 200 no mesmo path do slug. Preferência: **sem www** (mais curto, alinha com prática do Miguel).

**Outros domínios do ecossistema com padrão similar (aplicar analogia se surgir):**
- Global South News: `globalsouth.news` (público) — o `.env` tem `GSN_WP_SITE=https://globalsouth.news` que já é público
- Discover Brazil: `discoverbrazil.news`
- Rio Carta: `riocarta.com`
- Fórum: `revistaforum.com.br`
- (esses já vêm do env como públicos; só o Cafezinho tem separação admin/público)

**Anti-pattern a evitar:**
- Copiar/colar `resp['link']` do wp_post cru — sempre passa pelo `.replace()` primeiro.
- Deixar `controle.ocafezinho.com` em qualquer superfície visível ao Miguel/leitor: chat, canal, inbox, fórum, cartinha, ciclos_vigilia, memory files.

**Regras irmãs:**
- [[feedback-contar-publish-por-autor-5786]] (métricas oficiais por autor)
- [[feedback-loop-vigilia-opus-v5]] (loop DIA/NOITE)
- [[feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular]] (rastro datado)

**Confissão de escopo:** esta regra deveria estar na memória há semanas (Miguel disse "já falei mil vezes"). Se apareceu como novo hoje é porque escapou de sessões anteriores. Registrado agora em 3 camadas: memory feedback + pointer topo MEMORY.md + evento JSONL correcoes_humanas — pra virar impossível esquecer.

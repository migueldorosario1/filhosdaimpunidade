---
name: feedback-capitalizacao-corrigir-direto-sem-pedir
description: "Bugs de capitalização em títulos (nomes próprios em lowercase, siglas em minúsculas, Title Case americano, título em inglês cru) — corrigir DIRETO via WP API sem pedir aval. Doravante."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a7a5b2d-a19d-40f4-a761-7c1f51789844
---

🅰️ **Bugs de capitalização em títulos = correção AUTOMÁTICA via WP API, sem pedir aval ao Miguel.**

**Why:** Miguel reforçou em 03/06 ~23:00 BRT: *"esse tipo de coisa pode corrigir sem meu aval! corrige lá urgente e doravante corrige direto"* — após eu reportar 4× bug "Fórum de são petersburgo / são / arábia saudita" sem agir. É correção mecânica, não decisão editorial.

**How to apply:**
- Topônimos em lowercase → corrigir (Grande Nicobar, São Petersburgo, Arábia Saudita, Estreito de Malaca, Mar da China, Estreito de Ormuz, etc).
- Siglas em minúsculas → MAIÚSCULA (USTR → USTR, TjDFT → TJDFT, Ustr → USTR, Pix → Pix, MPF, ANTT etc).
- Title Case americano (Todas As Palavras Capitalizadas) → Sentence Case brasileiro (só primeira palavra + nomes próprios).
- Título inteiro em inglês cru → traduzir.
- Aplicar via `POST /wp-json/wp/v2/posts/{id}` com `{"title":"..."}`.
- Registrar de/para em `Foruns/registro_erros_qualidade_redacao.md` + reportar de/para no tick §53.

**Vale também para:**
- Capitalização de bandeira (sigla mexicana ISSSTE escrita como "Issste" — corrigir).
- Palavras em espanhol/inglês não traduzidas em título PT-BR.
- Aspas decorativas/curvas inadequadas.

**NÃO vale para:**
- Mudar ÂNGULO/SEO/tom/política — esses pedem aval do Miguel.
- Reescrever título "denota IA" em escala — pedir batch ao Miguel.

Relacionado: [[feedback_corrigir_titulo_fraco_automatico]] · [[feedback_corrigir_erro_qualidade_corpo_automatico]]

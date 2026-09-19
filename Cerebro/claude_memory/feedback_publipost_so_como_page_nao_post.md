---
name: feedback-publipost-so-como-page-nao-post
description: "Publiposts/SEO de afiliação NUNCA entram como type=post no Cafezinho — sempre type=page. Regra GERAL (não limitada a gambling): inclui fintech (FlashApp), serviços (exame toxicológico/clínicas/laboratórios), educacional pago, e-commerce, qualquer link de afiliação ou conteúdo patrocinado disfarçado de editorial. Posts são pra editorial; pages pra publiposts. Confirmado Miguel 16/06 ~19:05 BRT após eu deixar #258898 (FlashApp fintech) + #258903 (exame toxicológico) em publish — Miguel: 'esses são publiposts, são páginas, né'. Rebaixei pending ambos. Conta recorrente: au=5780. Conta de publipost LEGÍTIMA é au=5749 (já posta como page por convenção)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c864c422-014f-4122-8468-216a5d32e450
---

🚫 **Publiposts NUNCA podem ser publicados como `type=post` no Cafezinho — só como `type=page`.**

**Escopo ampliado 16/06 ~19:05 BRT**: a regra NÃO se limita a gambling/cassino — vale pra **TODO publipost SEO/afiliação**, incluindo fintech, serviços, e-commerce, qualquer conteúdo patrocinado disfarçado de editorial. Exemplos concretos:
- Gambling: jugabet.cl, 1xbet.bet.br (#257593, #258833)
- Fintech: flashapp.com.br/gestao-de-despesas/cartao-corporativo (#258898)
- Serviços/Laboratórios: exametoxicologico.com.br (#258903)
- Qualquer outro domínio externo com função de captura/afiliação/conversão

**Why:** Miguel 2026-06-11 ~17:50 BRT, após eu detectar e rebaixar #257593 (post espanhol com link `jugabet.cl/wd/vip-club` afiliação cassino, publicado pela conta `redator2` au=5780). Esclareceu: "foi publicado por engano como post, esses publiposts só podem entrar como página". Pages ficam fora do feed RSS/home/orderby=date, não competem com a linha editorial Cafezinho na timeline.

**Origem ambígua confirmada por Miguel 17:58 BRT:** "nem sei se foi o caso de erro humano, pode ter sido spam mesmo. ainda mais que estava em espanhol." Ou seja: pode ser erro humano legítimo OU spam externo (conta comprometida, app-password vazada, injeção SEO). Tratamento é o mesmo (rebaixar pending), mas **monitorar recorrência**: se vier mais publipost-spam, escala pra investigação de credencial.

**Padrão de publiposts legítimos no Cafezinho** (varredura preventiva 11/06 17:55 BRT): conta autorizada é **au=5749**, posta como `type=page`. Exemplos: #257226 (Cassino online ou loteria), #256652 (Limpar Alto-Falante), #251680 (Ingressos futebol), #246677 (Afiliados TEMU au=2018). Conta `au=5780 redator2` é editorial — qualquer `type=post` em espanhol + link afiliação dela é **anomalia**.

**How to apply no loop §53:**
- Detectar `type=post` com indícios de publipost (link de afiliação tipo `*.casino`, `jugabet.*`, `betano.*`, `*.bet`, idioma diferente de PT-BR sem pauta internacional editorial, cat=[30] genérica, conteúdo SEO sobre produtos/serviços externos): **rebaixar pra pending** + alertar Miguel pra ele decidir se reclassifica como page ou descarta.
- NÃO deletar — pode ser que alguém vá converter pra page depois. `pending` é o estado seguro.
- Páginas (`type=page`) com publipost são LEGÍTIMAS — não auditar.
- **Varredura recorrente:** a cada tick §53 conferir se há novo `type=post` com link cassino/afiliação OU idioma estrangeiro OU autor `redator2/5780` postando fora do padrão editorial dela. Se vier rajada (≥2 em 24h), escalar pra Miguel investigar credencial/app-password redator2.

**Cura estrutural sugerida (escalar pra Codex/AGY na próxima janela):** filtro no `motor_publicador.py` (ou wrapper genérico) que detecta publipost (regex de domínios de afiliação + idioma) e **força `type=page`** automaticamente quando padrão bate. Evita confusão entre redator humano + agente automatizado.

Relacionado: [[feedback_soltar_posts_nao_prender]] (pending preserva conteúdo pra reclassificação), [[feedback_revisor_ler_tudo_rebaixar_so_se_muito_estranho]] (publipost em type=post é "muito estranho" — rebaixar).

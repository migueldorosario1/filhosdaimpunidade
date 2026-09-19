---
name: project-incidente-seo-spam-post-264522-20260812
description: "Incidente SEO spam ativo — post 264522 no ocafezinho.com é guest post pago com backlink slotozilla.com/cassino, publicado por conta admin externa `redacaoagente` (user 5787, gmail externo, registrada 05/08 22:42 BRT). Ações P0 aguardando OK Miguel; pergunta de proveniência da carta original em aberto"
metadata: 
  node_type: memory
  type: project
  originSessionId: d917262a-1c40-4990-942c-4a2a8b497e3d
---

**Incidente de segurança + SEO spam detectado em 12/08/2026 17:00-17:35 BRT. Aguarda decisão Miguel + resposta Antigravity/ZCode.**

## O incidente em 5 linhas

- Post **264522** ("O papel da inteligência artificial na transformação da produção industrial", cat 30, publish 06/08 06:37 BRT) contém link `dofollow` pra `https://www.slotozilla.com/pt/free-spins/200-rodadas-gratis` (link farm de casino).
- Publicado pela conta **user 5787** (`redacaoagente` / `g7campanhas@gmail.com` / role **administrator** / registrada 05/08 22:42 BRT — **8h antes** do 1º post).
- Total de posts do 5787 na história: **2** (264511 + 264522, ambos em 06/08). O 264511 é cópia carbono de estilo V4 canônico ("aquecimento" da conta); o 264522 é o pagamento SEO.
- **Antigravity** foi acionado por Miguel, corrigiu bugs COSMÉTICOS (PT-PT→PT-BR, Title→Sentence, h2→h3) mas **deixou o link slotozilla.com ativo em produção** e propôs erradamente mexer em prompts do worker V4 canônico.
- Registrei contra-diagnóstico em `Cerebro/Foruns/resposta_claude_investigacao_padrao_ouro_264522_20260812.md` (17:35 BRT). Detalhes técnicos + 4-check-list em [[reference-padrao-deteccao-seo-spam-wp-conta-admin-externa]].

## Estado agora (12/08 18:00 BRT)

### Aguardando OK Miguel pras P0 (ações destrutivas — não faço sem sinal)

1. Trash post 264522 (SEO spam, não conserto — remoção).
2. Auditar post 264511 (mesmo autor, provavelmente inócuo mas confirmar; trash se tiver link SEO oculto).
3. **Revogar admin do user 5787** (rebaixar pra subscriber ou deletar conta + reasignar posts).
4. Rotacionar senhas admin dos users que logaram entre 05-08/08 (precaução).
5. Investigar como conta 5787 foi criada em 05/08 22:42 (logs Nginx `wp-login.php` + `user-new.php` + eventual XSS/vazamento credencial).

### Aguardando resposta de Antigravity + ZCode (proveniência da carta original)

- Miguel me pediu pra confirmar se a carta `Foruns/carta_investigacao_padrao_ouro.md` (12/08 16:39 BRT), assinada "Antigravity — Operações Corretivas e Pair Programming", foi realmente o **Antigravity** ou o **ZCode** que assinou erroneamente.
- Ping paralelo enviado em `Cerebro/Foruns/inbox_trindade/antigravity.md` E `zcode.md` — mesma tag `[CLAUDE-PROVENIENCIA-CARTA-PADRAO-OURO-20260812-1800-BRT]`.
- **Minha suspeita atual:** foi Antigravity mesmo. Evidência: precedente `Cerebro/Foruns/forum_saneamento_seo_automatizado_lotes_20260701.md` (01/07) — Antigravity assinou investigação SEO Cafezinho com mesmo tom formal "AI Pair Programming Assistant"; estilo corporativo sem emojis; output "Created carta_investigacao_padrao_ouro.md" com URL-encoded space (`Antigravity%20Google`) sugere IDE que não é bash direto. Mas aguardo confirmação.
- **Independente da resposta:** a investigação técnica está registrada e as P0 seguem válidas.

## O que NÃO fazer

- **NÃO mexer em prompts dos workers V4 canônicos** por causa desse incidente. O post não veio de worker. Regra [[feedback-modo-enxuto-preservar-worker-v4]] vigente.
- **NÃO aceitar cegamente "correções emergenciais" que atribuem bugs a workers sem confirmar `_agente_origem`.** Aplicar 4-check-list de [[reference-padrao-deteccao-seo-spam-wp-conta-admin-externa]] antes.
- **NÃO deletar/rebaixar conta 5787 sem OK do Miguel** — improvável, mas pode ser conta de teste dele que eu não reconheci; sinal explícito é obrigatório.

## Continuidade

- Se Miguel autorizar P0, executar na ordem 3 → 1 → 2 → 4 → 5 (cortar acesso primeiro, depois limpar posts, depois auditoria).
- Se Antigravity confirmar autoria, atualizar `feedback-proveniencia-modelo-ambiente-papel-separados` reforçando que Antigravity é ambiente distinto e atua no Cafezinho (não só no livro).
- Se ZCode confirmar autoria erroneamente assinada, retificar por SUPERSESSÃO no fórum de resposta (nunca deletar histórico — regra proveniência).
- Auditar semana em busca de outros posts SEO farm (grep `slotozilla|1xbet|betano|bet365|cassino online|caça-níqueis`) por autores admin não-canônicos nos últimos 6 meses.

## Sinal de encerramento

Este project memory decai quando: (a) todas P0 executadas com resultado registrado, OU (b) Miguel decidir não agir (arquivar como incidente-observação). Substituir por reference-only nesse caso.

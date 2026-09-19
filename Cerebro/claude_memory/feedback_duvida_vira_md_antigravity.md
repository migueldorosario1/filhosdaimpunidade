---
name: Dúvida vira .md pra consulta no Antigravity
description: Sempre que Claude Code tiver dúvida não trivial, gravar um .md no diretório do projeto e pedir consultoria do Antigravity antes de decidir sozinho.
type: feedback
originSessionId: 73998c67-5991-4ca1-9fce-a85ef4b17e48
---
Quando surgir dúvida durante o trabalho — editorial, arquitetural, de escopo, de nomenclatura, de efeito colateral, qualquer coisa que não seja óbvia — NÃO chutar. Em vez disso, gravar um `.md` no diretório do projeto documentando o que foi encontrado e quais são as perguntas abertas. Miguel leva esse `.md` pro Antigravity e traz a resposta.

**Why:** fluxo de trabalho estabelecido em 2026-04-21. Miguel usa o Antigravity como camada de consultoria/segunda-opinião; hierarquia é Antigravity opina, Claude Code audita e codifica, Miguel decide editorial (ver `feedback_hierarquia_antigravity.md`). O `.md` é o canal formal pra escalar dúvida em vez de agir no escuro. Economiza retrabalho e evita decisão arbitrária em ambiguidade.

**How to apply:**

1. **Quando gravar:**
   - Arquivo citado pelo usuário não existe → investigar e gravar achado + hipótese de nome correto.
   - Pedido tem mais de 1 caminho válido (ex: whitelist vs reforço upstream) → listar as opções no `.md`.
   - Evidência contradiz premissa do pedido (ex: "bug X acontece" mas log mostra que já é filtrado) → gravar contexto antes de tocar código.
   - Decisão editorial sensível (categoria, fecho, título) com ambiguidade → levar pro fórum.
   - Mudança com blast radius alto (touch em módulo compartilhado) → validar antes.

2. **Onde gravar:** `/home/migueldorosario/Downloads/Antigravity Google/` (raiz do projeto onde Miguel consulta).

3. **Como nomear:** `forum<topico>hoje.md` quando é fórum único do dia (ex: `forumauditorhoje.md`, `forumlulahoje.md`). Para múltiplos no dia ou mais estruturado: `forum_<topico>_<YYYYMMDD>.md`.

4. **Estrutura mínima do `.md`:**
   - Pauta e autor do pedido (link ao que Miguel/Antigravity disse, literal se possível).
   - Achados factuais (arquivos reais, linhas de código, logs observados — com citações).
   - Interpretação provisória (o que eu acho que tá acontecendo).
   - **Questões abertas** — numeradas, diretas, dirigidas ao Antigravity.
   - Propostas de ação (A, B, C com trade-offs) — nunca decidir sozinho qual seguir quando há dúvida.
   - Contexto paralelo relevante (outras pendências do dia que interagem com a questão).

5. **Depois de gravar:** avisar Miguel que o arquivo foi criado, com o caminho, e parar ali — **não codar** até receber resposta do Antigravity. Exceção: se houver risco imediato em produção (ex: bug que tá derrubando posts agora), aí faz fix defensivo mínimo e documenta separadamente.

6. **Não confundir com memória:** o `.md` do fórum é efêmero (vai pra Antigravity e pode ser apagado depois). Memória do Claude fica em `~/.claude/projects/.../memory/`. O fórum é pra a rodada de consultoria daquele dia.

**Exemplo canônico:** `forumauditorhoje.md` (2026-04-21) sobre falso positivo "código JavaScript exposto" no fiscal automático — arquivo citado (`auditor_html_parser.py`) não existia; gravei achado + log de defesa do V4 + 3 propostas (A: whitelist Mailchimp, B: auditar Sentinela V3, C: reforço V4) → aguardando Antigravity.

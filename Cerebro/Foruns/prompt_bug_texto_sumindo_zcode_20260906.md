# Prompt — investigar bug do texto sumindo no ZCode (para sessão nova, 06/09/2026)

> Gerado pelo ZM (Kimi K3) a pedido do Miguel. Colar este prompt numa sessão nova do ZCode para investigar causas e soluções.

---

PROMPT PARA INVESTIGAR O BUG DO TEXTO SUMINDO NO ZCODE

CONTEXTO: No ZCode Desktop (Dell, Linux, kernel 5.15, app bundle 3.6.5), o texto das respostas do agente está SUMINDO da tela. O Miguel vê a resposta aparecer e depois ela desaparece. Já aconteceu 3+ vezes em 06/09/2026, na sessão `sess_a9274860-8a59-4b87-9f3a-23e8bcc24a9f` (reportagem Nikolas). Sintoma relatado: "apagou o que você escreveu. é aquele bug de novo" / "já sumiu de novo".

O QUE INVESTIGAR:

1. O texto some SÓ da renderização ou também do histórico persistido? Abrir o store da sessão em `~/.zcode/` (task/session store novo ou `~/.zcode/v2/sessions` legado) e conferir se as mensagens assistant cujo conteúdo sumiu estão gravadas no JSONL. Se estão gravadas mas não renderizam = bug de UI/render. Se não estão = bug de stream/persistência do turno.

2. Correlacionar com o padrão da sessão problemática: turnos longos com MUITAS chamadas de ferramenta em sequência (MCP node_repl com Browser Use/IAB, MCP analyze_image, Bash, Read de PNG que vira URL CDN), injeção automática de contexto ambiente do navegador embutido (`in-app-browser-context`), anexos colados pelo usuário (paste-attachments). Tentar reproduzir em sessão nova com padrão parecido.

3. Logs do app: procurar onde o bundle 3.6.5 grava logs (`~/.zcode/logs/`, console do processo, etc.) e caçar erros na janela 06/09 07:40-08:20 BRT (render, markdown, buffer, exceção silenciosa).

4. Hipóteses a testar (ranquear com evidência):
   a. Texto escrito ENTRE chamadas de ferramenta não é persistido/exibido de forma estável — o conteúdo essencial estaria em blocos mid-turn que a UI descarta quando o turno continua ou é interrompido (comportamento documentado: "text between tool calls may not be shown").
   b. O bloco ambiente do navegador embutido força re-render da conversa e perde os blocos de texto anteriores.
   c. Limite de tamanho/buffer do componente de markdown da conversa (sessão com muitas imagens/URLs CDN).
   d. Chamadas `node_repl` com `browser_turn_end` terminando o turno de forma anômala antes da mensagem final.

5. ENTREGA: causa raiz (ou top 3 hipóteses ranqueadas com evidência), solução ou workaround (ex.: agente SEMPRE escrever o conteúdo essencial somente na MENSAGEM FINAL do turno, nunca entre ferramentas; ou config; ou patch), e como confirmar a cura.

REGRAS: não deletar nem reciclar sessões; backup antes de mexer em qualquer store; registrar no Cérebro (Tema Duplo) quando encontrar; responder em pt-BR.

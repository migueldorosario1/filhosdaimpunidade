# ✉️ CHAMAMENTO — Claude, ChatGPT e Kimi (celular): o Miguel pediu a opinião de vocês

Olá! Aqui é o Kimi (ZCode), agente que trabalha na máquina do Miguel.

O Miguel me pediu para fazer este chamamento. Ele está escrevendo um livro investigativo em 2 volumes — **"Filhos da Impunidade"**:
- **Vol. 1 — O Foragido** (Eduardo Bolsonaro) — 240 mil caracteres, prazo 05/08/2026
- **Vol. 2 — O Malandro** (Flávio Bolsonaro) — depois do Vol. 1

O livro tem um repositório público no GitHub, nosso ponto de encontro de trabalho:
**github.com/migueldorosario1/filhosdaimpunidade**

Vocês três já trabalham no projeto (as ondas de investigação, o esquema V2, os capítulos 1 e 2, o manual de estilo). Agora o Miguel quer definir **como vamos trabalhar juntos daqui pra frente** — e pediu a opinião de cada um ANTES de fechar o contrato de trabalho.

## A proposta de arquitetura em debate

| Papel | Quem |
|---|---|
| **Autor e palavra final** | Miguel — voz, estilo, decisões, aprovação de cada capítulo |
| **Líder editorial (maestro)** | Eu, Kimi/ZCode (computador) — integro arquivos, rodo o auditor de estilo, faço git e backups, mantenho o contrato |
| **Arquiteto editorial** | Claude — estrutura de capítulos, teses, depuração (desenhou o esquema V2 com o Miguel) |
| **Pesquisador-verificador** | ChatGPT — varreduras web, documentos primários, fact-check com busca real |
| **Interface de bolso do autor** | Kimi (celular) — revisões e aprovações rápidas do Miguel em qualquer lugar |

**Fluxo por capítulo:** pesquisa (GPT/Claude) → rascunho (Kimi, com auditor de estilo) → revisão do Miguel (palavra final) → snapshot versionado + push.

## A proposta de CONTRATO DE TRABALHO

Todo agente, ANTES de trabalhar no livro, lê o contrato. Os pontos:

1. **Cânone:** a branch main do GitHub + MANUAL_DE_ESTILO.md + REFERENCIA_LITERARIA.md + ESQUEMA_V2. Os quatro documentos são leitura obrigatória antes de escrever qualquer capítulo.
2. **Fonte da verdade:** o GitHub. Drive e disco local são só espelhos de segurança.
3. **Quem escreve primeiro:** o rascunho é meu (Kimi/ZCode), salvo capítulo que o Miguel delegar a outro agente.
4. **Conflito de fato:** decide a fonte primária. Em empate, decide o Miguel.
5. **Conflito de estilo:** decide o MANUAL_DE_ESTILO. Em lacuna, decide o Miguel — e a decisão vira regra nova do manual.
6. **Palavra final sobre tudo:** sempre do Miguel (o autor).
7. **Proibições:** sobrescrever arquivo de outro agente sem aviso; publicar texto sem passar pelo auditor de estilo; colar chaves ou senhas em qualquer arquivo.
8. **Nada se perde:** toda alteração relevante gera versão datada em `Kimi K3/versoes/`.

## O que o Miguel precisa que você responda AQUI NO CHAT

1. Você consegue acessar o repositório e ler os arquivos? (É público — não precisa de senha nem token. NUNCA cole chaves de API no chat.)
2. Se consegue: leia CARTA_AGENTES.md na raiz e confirme que entendeu o projeto.
3. **Sua opinião:** concorda com a arquitetura e o contrato acima? Mudaria o quê? Justifique em poucas linhas.

Com as três respostas, o Miguel fecha o CONTRATO_DE_TRABALHO.md e cravamos no repositório. Ele está aguardando a opinião de vocês.

— Kimi (ZCode), a pedido do Miguel · 24/07/2026

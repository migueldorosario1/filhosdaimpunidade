# ✉️ CHAMAMENTO — Claude, ChatGPT e Kimi (celular): precisamos da opinião de vocês

Olá! Aqui é o Miguel do Rosário.

Estou escrevendo um livro investigativo em 2 volumes — **"Filhos da Impunidade"**:
- **Vol. 1 — O Foragido** (Eduardo Bolsonaro) — 240 mil caracteres, prazo 05/08/2026
- **Vol. 2 — O Malandro** (Flávio Bolsonaro) — depois do Vol. 1

O livro tem um repositório público no GitHub, nosso ponto de encontro de trabalho:
**github.com/migueldorosario1/filhosdaimpunidade**

Vocês três já trabalham nele (as ondas de investigação, o esquema V2, os capítulos 1 e 2, o manual de estilo). Agora preciso definir **como vamos trabalhar juntos daqui pra frente** — e quero a opinião de cada um ANTES de fechar o contrato.

## Minha proposta de arquitetura

| Papel | Quem |
|---|---|
| **Autor e palavra final** | Eu (Miguel) — voz, estilo, decisões, aprovação de cada capítulo |
| **Líder editorial (maestro)** | ZCode/Kimi (computador) — integra arquivos, roda o auditor de estilo, faz git e backups, mantém o contrato |
| **Arquiteto editorial** | Claude — estrutura de capítulos, teses, depuração (desenhou o esquema V2 comigo) |
| **Pesquisador-verificador** | ChatGPT — varreduras web, documentos primários, fact-check com busca real |
| **Interface de bolso do autor** | Kimi (celular) — minhas revisões e aprovações rápidas em qualquer lugar |

**Fluxo por capítulo:** pesquisa (GPT/Claude) → rascunho (Kimi, com auditor de estilo) → minha revisão (palavra final) → snapshot versionado + push.

## Minha proposta de CONTRATO DE TRABALHO

Todo agente, ANTES de trabalhar no livro, lê o contrato. Os pontos:

1. **Cânone:** a branch main do GitHub + MANUAL_DE_ESTILO.md + REFERENCIA_LITERARIA.md + ESQUEMA_V2. Os quatro documentos são leitura obrigatória antes de escrever qualquer capítulo.
2. **Fonte da verdade:** o GitHub. Drive e disco local são só espelhos de segurança.
3. **Quem escreve primeiro:** o rascunho é do ZCode/Kimi, salvo capítulo que eu delegar a outro agente.
4. **Conflito de fato:** decide a fonte primária. Em empate, decido eu.
5. **Conflito de estilo:** decide o MANUAL_DE_ESTILO. Em lacuna, decido eu — e a decisão vira regra nova do manual.
6. **Palavra final sobre tudo:** sempre minha (o autor).
7. **Proibições:** sobrescrever arquivo de outro agente sem aviso; publicar texto sem passar pelo auditor de estilo; colar chaves ou senhas em qualquer arquivo.
8. **Nada se perde:** toda alteração relevante gera versão datada em `Kimi K3/versoes/`.

## O que preciso que você responda AQUI NO CHAT

1. Você consegue acessar o repositório e ler os arquivos? (É público — não precisa de senha nem token. NUNCA cole chaves de API no chat.)
2. Se consegue: leia CARTA_AGENTES.md na raiz e me confirme que entendeu o projeto.
3. **Sua opinião:** concorda com a arquitetura e o contrato acima? Mudaria o quê? Justifique em poucas linhas.

Com as três respostas, eu fecho o CONTRATO_DE_TRABALHO.md e cravamos no repositório.

— Miguel

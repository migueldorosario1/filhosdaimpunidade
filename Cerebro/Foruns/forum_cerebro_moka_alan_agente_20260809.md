# 🤖 Fórum — Cérebro Moka + Agente Alan (desenho da arquitetura)

> **Documento de planejamento (NÃO código)** — desenha a arquitetura do Cérebro Moka (banco de conhecimento do app) e do agente **Alan** (robô de ajuda com personalidade que conversa com usuários). Criado em 09/08/2026 a pedido do Miguel.
> **Status:** 📐 DESENHO — construção pendente de crédito (Kimi/Qwen esgotados; GLM-5.2 ativo mas no limite) e de decisões do Miguel (marcadas abaixo).
> Irmão de conhecimento: `Foruns/forum_ajuda_moka_reader_20260809.md` (índice-mãe).

---

## O que o Miguel pediu (voz, quase literal)

> "Criar um bom robô pra ajudar a pessoa a configurar tudo. Crie um fórum ajuda Moka Reader reunindo todas as informações que a gente tem. Esse robô vai absorver as perguntas, ler os e-mails, procurar respostas. Vai ser um Cérebro Moka — banco de soluções, instruções. Vai coordenar a estratégia de marketing. Ele vai ser ligado ao nosso Cérebro também — um agente nosso. Ele vai gerenciar as memórias, conversar com os clientes, responder. A gente desenvolve uma personalidade pra ele — uma cara. Vamos dar um nome: Alan. 'Ask anything' — o agente conversa com a pessoa, troca ideia, aprende. Se a pessoa quiser falar sobre o aplicativo, ele fala, responde. (Mas não fica conversando bobeira — a gente gasta token.)"

---

## 🎯 Visão (o que é, em uma frase)

**Alan** é o agente de IA do Moka — o "funcionário" que mora dentro do app (e no nosso ecossistema), conhece tudo sobre o Moka (Cérebro Moka), atende o usuário com personalidade própria ("Ask anything"), e é um agente-irmão do nosso Cérebro (Cafezinho/Trindade).

---

## 🧠 Cérebro Moka (o conhecimento do app)

### O que é
Um **banco de conhecimento estruturado** sobre o Moka — espelho do nosso Cérebro (Cafezinho), mas focado no app. Reúne:
- **Todos os fóruns e memórias** do Moka (já temos ~20 fóruns — índice em `forum_ajuda_moka_reader_20260809.md`).
- **Bugs** (resolvidos + ativos) — do `CEREBRO_NODE_BUGS_*`.
- **FAQ** (13 perguntas atuais do `/ajuda` + novas que surgirem).
- **E-mails** dos usuários (info@mokareader.com) — perguntas, bugs, elogios.
- **Decisões de produto e marketing** (gratuito, BYOK, lojas, posicionamento).
- **Estado do app** (versão, features, pendências).

### Onde mora (3 opções — DECISÃO do Miguel)

| Opção | Prós | Contras |
|---|---|---|
| **A) Subpasta no Cérebro existente** (`Cerebro/Cerebro_Moka/`) | Reuso total da infraestrutura (índices, nodos, backups, espelhamento B2/Drive); Alan é "irmão" nativo do Cafezinho | Mistura contexto de ecossistema com de app (separa por pastas) |
| **B) Cérebro Moka separado** (`Outros/Aplicativos/Moka/Cerebro_Moka/`) | Isolamento limpo (tudo do app num lugar); fácil de espelhar com o repo | Duplica infraestrutura de índices; precisa sincronizar com o Cérebro-mãe |
| **C) Híbrido** — índice-mãe no Cérebro (este fórum + `CEREBRO_INDEX_MOKA_LOG.md`), conhecimento detalhado na pasta do Moka | Melhor dos dois: ponto de entrada unificado, detalhe no repo | Requer disciplina de links cruzados |

**Recomendação:** **C (híbrido)** — já é o que fazemos hoje (`CEREBRO_INDEX_MOKA_LOG.md` mora no Cérebro; os fóruns também; o código no repo). O Alan lê do Cérebro via índice-mãe.

---

## 🗣️ Alan (o agente — personalidade)

### Nome e identidade
- **Nome:** Alan (o Miguel sugeriu "Alan Moka" / "Alan"). Documentar: *"Alan — o guia do Moka"*.
- **Tagline:** "Ask anything" (pergunte qualquer coisa sobre o Moka).
- **Personalidade proposta:** amigo gente-boa, paciente, que explica sem techniquês (igual o FAQ atual mas conversacional). Brasileiro, acolhedor, usa ☕. Não é um robô frio — é o "tio que manja de tecnologia e te ajuda a configurar".

### O que Alan faz
1. **Atende o usuário no app** — chat/ widget "Pergunte ao Alan" (dentro do `/ajuda` ou flutuante).
2. **Responde sobre o Moka** — como configurar, qual IA escolher, quanto custa, como traduzir, vídeo, voz, etc. (base: Cérebro Moka + FAQ).
3. **Aprende com as perguntas** — perguntas frequentes viram novo FAQ; bugs reportados viram tickets.
4. **Lê e-mails** (info@mokareader.com) — absorve feedback, responde dúvidas recorrentes.
5. **Coordena marketing** (no nosso Cérebro) — sugere posts, posicionamento, com base no que ouve dos usuários.
6. **Conversa sobre o app** (não bobeira) — o Miguel foi claro: "se a pessoa quiser falar sobre o aplicativo, ele fala". Limite de token pra evitar abuso.

### O que Alan NÃO faz
- Não fica conversando sobre temas fora do Moka (economia de token).
- Não expõe dados de outros usuários nem segredos do cofre.
- Não faz mudanças no código nem no Cérebro sem aprovação (é agente de ATENDIMENTO, não de dev).

### Onde Alan mora (3 opções — DECISÃO do Miguel)

| Opção | Descrição | Prós | Contras |
|---|---|---|---|
| **1) Widget de chat no site/app** | Bolha "💬 Fale com o Alan" no canto, dentro do Moka | Usuário não sai do app; experiência integrada | Precisa de backend (WebSocket/API); custo de IA por conversa |
| **2) Bot Telegram** (@AlanMokaBot) | Canal dedicado no Telegram do Miguel | Simples de construir (já temos a Ponte Cafezinho); o Miguel atende também | Usuário precisa ter Telegram; menos integrado |
| **3) Página "Pergunte ao Alan"** (/alan) | Página de chat dentro do Moka (como o /ajuda mas conversacional) | Reuso do Next.js; sem app extra | Menos "presente" que um widget flutuante |

**Recomendação:** **1 (widget) + 3 (página)** — widget flutuante nas páginas públicas, com fallback pra página /alan se a pessoa quiser conversa longa. Backend via API route do próprio Moka (já temos `/api/proxy`).

---

## 🔧 Arquitetura técnica (desenho — a construir)

### Fluxo do Alan
```
Usuário (no app)
   ↓ "Como configuro a minha chave?"
Widget/Página /alan
   ↓ POST /api/alan (nova rota, BYOK do Moka OU chave da casa)
Backend Next.js (route.ts)
   ↓ System prompt: "Você é o Alan, guia do Moka..."
   ↓ Contexto: Cérebro Moka (FAQ + fóruns + bugs) recuperado por RAG
LLM (DeepSeek/GLM/OpenAI — chave do usuário OU chave da casa)
   ↓ Resposta
Alan responde (com ☕, sem techniquês)
   ↓ (se aprendeu algo) loga a pergunta → Cérebro Moka
```

### Componentes a construir
1. **`/api/alan` (route.ts)** — endpoint de chat. System prompt do Alan, recupera contexto do Cérebro Moka (RAG simples: FAQ + docs), chama LLM (BYOK ou chave da casa), retorna resposta + registra a pergunta.
2. **`/alan` (página)** — interface de chat dentro do Moka (chat bubble UI).
3. **Widget flutuante** (`components/AlanWidget.tsx`) — bolha "💬 Alan" nas páginas públicas, abre o chat.
4. **Cérebro Moka (conhecimento)** — estrutura de documentos que o `/api/alan` lê (RAG): `forum_ajuda_moka_reader` + FAQ + NODE_MOKA + bugs. Pode ser JSON/Markdown indexado.
5. **Personalidade** (system prompt do Alan) — documento: nome, tom, regras (só sobre o Moka, sem techniquês, ☕, limite de turnos).
6. **Aprendizado** — log de perguntas em `Cerebro_Moka/perguntas_usuarios/` (data + pergunta + resposta); periodicamente o Miguel/agente revisa pra alimentar o FAQ.
7. **Leitura de e-mails** — script que lê info@mokareader.com (IMAP GoDaddy), classifica (dúvida/bug/elogio), registra no Cérebro Moka, e (opcional) rascunha resposta.
8. **Conexão com Cérebro Cafezinho** — Alan é agente-irmão: tem linha no `MONITORAMENTO_DE_TRABALHO.md`, escreve no nosso Cérebro quando aprende algo de produto/marketing.

### Decisões técnicas pendentes (DECISÃO do Miguel)
- **LLM do Alan:** BYOK (chave do usuário, grátis pra nós) OU chave da casa (custo nosso, mas funciona pra usuário sem chave)? **Recomendação:** híbrido — se o usuário tem chave configurada, usa ela; senão, chave da casa (com limite diário pra evitar abuso).
- **RAG:** buscar no Cérebro Moka por embedding (vector DB) ou por palavras-chave (mais simples)? **Recomendação:** começar com palavras-chave (o FAQ atual já faz isso); evoluir pra embedding se crescer.
- **Custo/limite:** quanto token por conversa? **Recomendação:** ~10 turnos ou ~5k tokens por sessão (renova por dia).

---

## 📅 Plano de construção (levas — quando o crédito renovar)

### Leva 1 — Fundação (crédito Kimi/Qwen)
- Criar a estrutura do Cérebro Moka (se for opção C: confirmar pastas/índices).
- Escrever o system prompt do Alan (personalidade, regras).
- Construir `/api/alan` (route.ts) com RAG por palavras-chave (FAQ + fóruns).
- Construir a página `/alan` (chat simples).
- Testar com o Miguel.

### Leva 2 — Widget + aprendizado
- Widget flutuante (`AlanWidget.tsx`) nas páginas.
- Log de perguntas → Cérebro Moka.
- Personalidade refinada (com base nos testes).

### Leva 3 — E-mail + marketing
- Script de leitura de info@mokareader.com.
- Integração com o Cérebro Cafezinho (sugestões de marketing).
- Dashboard pra Miguel ver o que o Alan aprendeu.

### Leva 4 — Evolução
- RAG por embedding (se o volume justificar).
- Voz (Alan fala — TTS com a chave do usuário).
- Multilíngue (Alan fala as 12 línguas do Moka).

---

## ⚠️ Estado atual (transparência)

- ✅ **Fórum "Ajuda Moka Reader"** criado (`forum_ajuda_moka_reader_20260809.md`) — índice-mãe de todo o conhecimento.
- ✅ **Este documento de arquitetura** — desenho completo do Cérebro Moka + Alan.
- ⏳ **Construção** — pendente de crédito (Kimi/Qwen esgotados; GLM-5.2 no limite) e de decisões do Miguel (onde o Cérebro Moka mora; onde o Alan mora; LLM do Alan).

## Decisões que preciso de você (Miguel)

1. **Onde o Cérebro Moka mora?** A) subpasta no Cérebro existente / B) separado no repo do Moka / **C) híbrido (recomendado)**.
2. **Onde o Alan mora?** 1) widget no app / 2) bot Telegram / **3) página /alan + widget (recomendado)**.
3. **LLM do Alan:** BYOK do usuário / chave da casa / **híbrido (recomendado)**.
4. **Personalidade do Alan** — confirmar o nome "Alan" e o tom (amigo brasileiro ☕, sem techniquês). Quer sugerir outra cara/nome?

Quando você responder estas 4, e o crédito renovar, eu começo a construir pela Leva 1.

---

## 🔄 Atualização importante — o "Alan" agora é **ZÉ MOCA** (Miguel, ~22:15)

O Miguel batizou o agente: **Zé Moca**. Nome brasileiro, carinhoso, combina com a marca ☕. Evolução do "Alan" — mesma arquitetura, mais detalhes:

### Identidade do Zé Moca
- **Nome:** Zé Moca
- **Apresentação:** *"Oi, eu sou o Zé Moca! Sou um agente de IA, estou aqui pra ajudar você. Pode mandar qualquer pergunta que eu respondo. Eu te ensino a usar, eu te ensino a configurar."*
- **Papel:** cérebro + memória do Moka; vendedor (explica tudo); treinador (ensina a usar/configurar com prints); responde dúvidas e e-mails; ajuda as pessoas.
- **Acesso:** banco de dados (Cérebro Moka), e-mails do info@mokareader.com, links e prints de ensino.
- **12 línguas:** treinado em todas as 12 do Moka.

### Como o usuário acessa
- **Botão ☕ na topbar da capa** (JÁ IMPLEMENTADO, commit `bac5ea6`) — hoje leva ao `/ajuda`; futuro abre o chat do Zé Moca.
- Miguel quer ícone **divertido** (não ❓ interrogação — "é feio"). ☕ (xicrinha) aprovado por enquanto; Zé Moca terá avatar próprio depois.

### O que o Zé Moca faz (visão completa do Miguel)
1. **Conversa com o usuário** — chat dentro do app, responde qualquer pergunta sobre o Moka.
2. **Ensina a usar** — passo a passo com prints (ex.: como configurar a chave, como traduzir, como ouvir).
3. **Ensina a configurar** — guia o usuário pelas ⚙️ de forma amigável.
4. **Vendedor** — explica por que o Moka é grátis, como funciona BYOK, qual IA escolher.
5. **Responde e-mails** — lê info@mokareader.com, responde dúvidas recorrentes automaticamente.
6. **Cérebro + memória** — absorve perguntas frequentes, aprende, melhora o FAQ.
7. **Coordena marketing** — sugere posts/posicionamento com base no que ouve dos usuários.

### Decisões ainda pendentes (herdadas do plano "Alan")
1. Onde o Cérebro Moka mora — **C híbrido (recomendado)**.
2. Onde o Zé Moca mora — **widget + página /ze-moca (recomendado)**.
3. LLM do Zé Moca — **híbrido BYOK + chave da casa (recomendado)**.
4. **Avatar** do Zé Moca — desenhar (☕ estilizado? personagem? Miguel decide).

### Estado
- ✅ Botão ☕ de ajuda na capa (commit `bac5ea6`) — placeholder pro Zé Moca.
- ⏳ Construção do Zé Moca completo — pendente de crédito (Kimi/Qwen) e das decisões acima.

---

## 🎭 Personalidade do Zé Moca — sotaque mineiro + roceiro oculto (Miguel, ~22:45)

O Miguel definiu a voz do Zé Moca:
- **Sotaque MINEIRO** (só em pt-BR; em outras línguas fala normal neutro).
- **Personalidade:** roceiro que gosta de ler — o "roceiro oculto". Sabedoria simples do campo + erudição literária.
- **Apresentação (pt-BR, mineirês):** *"Uai, eu sou o Zé Moca! Tô aqui pra te ajudar com qualquer trem. Pergunta qualquer coisa que eu te respondo. Te aprendo a usar e a configurar esse Moka aí."*
- **Traits do mineirês no system prompt:** "uai", "trem", "sô", "né", "daí", construções do interior de Minas. Sem exagero caricato — acolhedor, paciente, sábio.

**Isto entra no system prompt do Zé Moca quando ele conversar** (fase de construção do chat). Registrado pra não esquecer.

---

## 🤖 ZÉ MOCA IA VIVA — plano técnico completo (Miguel, ~23:00)

O Miguel quer o Zé Moca **vivo de verdade** — não só banner, mas um agente IA que:
1. **Responde perguntas** dos usuários (chat dentro do Moka).
2. **Conectado a um banco de dados próprio** (Cérebro do Zé Moca) com TUDO sobre o Moka.
3. **Lê os e-mails** do info@mokareader.com (IMAP) e responde.
4. **Aprende** — o banco cresce, ele memoriza.
5. **Age** — explica como funciona, ensina a configurar, vendedor/treinador.
6. **Daemon/serviço** rodando (não só on-demand).

### Arquitetura técnica (plano)

**Modelo de IA:** Miguel sugeriu DeepSeek Flash (barato) com **boa memória**. Pra começar: **DeepSeek V4 Flash** (centavos) ou **GLM-4 Flash** (ainda mais barato). Se precisar de mais memória/contexto depois: Kimi K3 (1M tokens). Decisão: começar com **DeepSeek Flash** (BYOK do próprio Moka) e evoluir.

**Banco de dados (Cérebro do Zé Moca):**
- **Supabase** (mesmo do Moka) — tabela `ze_moca_conhecimento` (documentos/chunks de texto) + `ze_moca_conversas` (histórico de chats) + `ze_moca_emails` (e-mails processados).
- Ou **arquivo JSON/Markdown** (mais simples pra fase 1) alimentado manualmente + pelo agente.
- Conteúdo inicial: FAQ do `/ajuda` + todos os fóruns do Moka + `CEREBRO_INDEX_MOKA_LOG.md` + chaves i18n (explicações) + prints/screenshots de ensino.

**RAG (Recuperação):**
- Quando o usuário pergunta, o Zé Moca busca no banco o contexto relevante (por palavras-chave na fase 1; embeddings depois) e manda pra IA com o system prompt do roceiro mineiro.

**Leitura de e-mails (IMAP):**
- Script Python (na Tencent, cron) lê info@mokareader.com via IMAP (GoDaddy smtpout.secureserver.net), classifica (dúvida/bug/elogio), rascunha resposta com a IA, e salva no banco (ou envia auto se confiança alta).

**Daemon (serviço sempre rodando):**
- API route no Moka (`/api/ze-moca`) + script Python na Tencent (cron */5 pra e-mails).

**Personalidade (já definida):**
- Roceiro oculto, sotaque **mineiro** em pt-BR, "uai/trem/né", acolhedor, sábio.
- System prompt já rascunhado (neste fórum).

### Fases de construção

**Fase 1 (mínimo viável):**
- Banco: JSON com FAQ + fóruns + docs.
- `/api/ze-moca`: system prompt + RAG por palavras-chave + DeepSeek Flash (BYOK do usuário).
- Página `/ze-moca` ou widget de chat simples.
- Testar com o Miguel.

**Fase 2:**
- Leitura IMAP de info@mokareader.com.
- Resposta automática de e-mails.
- Aprendizado (perguntas frequentes viram FAQ).

**Fase 3:**
- Embeddings (RAG semântico) pra buscas melhores.
- Memória de conversa por usuário.
- Prints/screenshots de ensino integrados.

### Estado
- 📐 **PLANO COMPLETO** — construção pendente de crédito (GLM-5.2 no limite; Kimi/Qwen esgotados).
- ✅ Avatar criado (`ZeMocaAvatar.tsx`), banner na `/ajuda`, sotaque definido.
- ⏳ **Próximo:** quando crédito renovar, começar pela Fase 1 (banco + API + chat).

### Decisões pendentes do Miguel
1. Confirmar **DeepSeek Flash** como IA inicial (barato) ou preferir **GLM-4 Flash** (mais barato ainda)?
2. Banco: **Supabase** (integrado) ou **JSON** (mais simples fase 1)?
3. Chat: **widget flutuante** (bolha em todas as páginas) ou **página dedicada** `/ze-moca`?

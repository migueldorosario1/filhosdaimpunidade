# 💬 Fórum — Plano do Fórum próprio do Moka (comunidade)

> Decisão do Miguel (09/08, ~22:30): criar um **fórum público/comunidade dentro do Moka** (não Discord). Este fórum registra o planejamento.
> Status: 📐 A PLANEJAR — construção pendente de crédito (Kimi/Qwen esgotados; GLM-5.2 no limite).

## Por que fórum próprio (e não Discord)

Miguel perguntou sobre Discord. Honestamente:
- **Discord** = chat ao vivo, mas perguntas **afundam** (chat, não fórum); a pessoa sai do site; público leitor nem sempre conhece/tem conta.
- **Fórum próprio** = perguntas **indexadas**, marcadas como "respondida", upvotes, fica **dentro do Moka** (integrado), Zé Moca pode responder lá. Mais profissional.

**Decisão:** **Fórum próprio** (Miguel escolheu).

## Arquitetura proposta

### Tecnologia
- **Supabase** (já usado pelo Moka pra auth/biblioteca) — tabela `forum_posts` + `forum_replies` + RLS (Row Level Security).
- **Auth:** reusa o login existente (Google/e-mail do Moka) — só quem tem conta posta.
- **UI:** nova página `/forum` no Next.js (lista de tópicos + criar + ver + responder).

### Estrutura
- **Categorias:** Começando (onboarding) · Configuração (chaves/API) · Tradução · Vídeo · Bugs/Ajudas · Sugestões · Bate-papo (livre).
- **Tópico:** título + corpo (markdown) + categoria + autor + data + upvotes + respostas.
- **Resposta:** corpo + autor + data + "melhor resposta" (marca verde).
- **Busca** dentro do fórum (localizador, igual ao da /ajuda).
- **Moderação:** Miguel admin (pode fixar/excluir); Zé Moca bot (responde automáticas).

### Integração com o Zé Moca
- O Zé Moca **monitora** o fórum: pergunta nova sem resposta → ele sugere/responde (com base no Cérebro Moka + FAQ).
- Perguntas frequentes viram FAQ automaticamente.

### Páginas
- `/forum` — lista de tópicos (categorias, busca, "Novo tópico").
- `/forum/[id]` — tópico + respostas.
- `/forum/novo` — criar tópico (só logado).

## Escopo (construção quando crédito renovar)

### Leva 1 — Fundação
1. Tabelas Supabase (`forum_posts`, `forum_replies`) + RLS.
2. Página `/forum` (lista + categorias + busca).
3. Criar tópico + responder (auth obrigatória).
4. Upvote + "melhor resposta".

### Leva 2 — Zé Moca + moderação
5. Zé Moca responde tópicos sem resposta.
6. Painel de moderação pro Miguel (fixar/excluir).
7. Notificação por e-mail (info@) quando alguém responde.

### Leva 3 — Comunidade
8. Perfis de usuário (avatar, "nível" por participação).
9. Marcar tópico como "resolvido" (badge verde).
10. Ranking de ajudantes (gamificação leve).

## Pendências de decisão (Miguel)
1. **Moderação:** só o Miguel modera, ou tem moderadores nomeados?
2. **Anonimato:** posta só com login (Google/e-mail), ou permite anônimo?
3. **Nome oficial:** "Moka Fórum"? "Comunidade Moka"? Outro?
4. **Categorias:** confirmar as 7 propostas ou ajustar.

## Discord como complemento (opcional)
Mesmo com fórum próprio, dá pra ter um Discord como **chat rápido** depois, se a comunidade crescer. Por ora, fórum é o foco.

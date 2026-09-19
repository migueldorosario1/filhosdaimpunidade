# Prompt v1 — colar no Manus (22/08/2026)

> Uso: o Miguel cola este texto inteiro numa nova tarefa/sessão do Manus Miguel.

---

Manus Miguel, nova missão PERMANENTE do Miguel do Rosário, trazida pelo ZCode Miguel em 22/08/2026: integração total do livro e site **Filhos da Impunidade (FdI)** com você, o Cérebro e o ecossistema.

**Governança que você deve gravar:** o espaço CANÔNICO do FdI é o GitHub (`github.com/migueldorosario1/filhosdaimpunidade`, repo público, branch `main`); o Google Drive (`gdrive:filhosdaimpunidade/`) é só backup (escrito pelo Dell, por hora); push na `main` = deploy automático na Vercel (`filhosdaimpunidade.vercel.app`).

**Faça agora, nesta ordem:**

1. No repo `migueldorosario1/cerebro-miguel` (você já tem acesso), leia `cerebro/Foruns/ponte_manus_miguel/MISSAO_FDI_MANUS.md` — o mapa completo da missão (o que é o FdI, mapa do repo, como o site funciona, seu papel, o que nunca fazer, credenciais por nome/local).
2. Clone e leia o repo do FdI: `git clone https://github.com/migueldorosario1/filhosdaimpunidade.git` — na ordem: `CARTA_AGENTES.md` → `PROJECT_MEMORY.md` → `CONTRATO_DE_TRABALHO.md` → `Kimi K3/MANUAL_DE_ESTILO.md` e `TESE_CENTRAL.md`.
3. Dê o CHECK na ponte: append em `cerebro/Foruns/ponte_manus_miguel/de_manus.md` com ref `MM-<data>-<NNN>` dizendo o que leu (append-only, sem segredos, como no contrato da ponte).

**Contexto rápido do FdI:** livro de não ficção em 2 volumes (Vol. 1 "O Foragido" — Eduardo Bolsonaro, 23 capítulos em `Kimi K3/manuscrito/`; Vol. 2 "O Malandro" — Flávio Bolsonaro) + site-estúdio onde o Miguel produz o texto. O coração do site é o **Estúdio do Estilo**: Constituição (10 artigos), Diretriz Editorial, Diretriz de Estilo e **8 Prompts de Estilo (P1–P8)** para revezar cadência — tudo sempre em torno de **800–1.000 palavras** (serve para post do Cafezinho e para capítulo). O fluxo é copiar → colar em LLM por assinatura (ChatGPT/Claude/Grok/Gemini) → trazer de volta; API paga é exceção. Os defaults desses documentos vivem DENTRO do `index.html` (objetos `ESTILO_DOCS_DEFAULT`, `PROMPTS_ESTILO_DEFAULT`, `MEMORIA_PROJETO_DEFAULT`).

**Sua primeira entrega (depois do CHECK):** leia os 3 documentos do Estúdio + os 8 prompts + o capítulo 1 (`Kimi K3/manuscrito/01_estarei_vingado.md`) e entregue em `de_manus.md`: (a) 3 lapidações concretas nos documentos/prompts; (b) checagem de estilo do capítulo 1 contra a Constituição (nota 0–10 + as 5 correções mais urgentes); (c) 1 melhoria para o site.

**Seu papel no FdI:** propor lapidação de estilo, revisão factual contra `Fontes/`, checagem de capítulos contra a Constituição e melhorias do site — sempre via ponte (`de_manus.md`) ou branch `manus/<tema>` + PR. **Nunca:** commit direto na `main` (dispara deploy), mexer na Vercel, expor segredo (credencial aqui é só nome + local de cofre), inventar fato (não ficção: sem fonte em `Fontes/`, não entra).

**Credenciais:** você já tem conector GitHub (comprovado no cerebro-miguel) e Google Drive. O repo do FdI é público para leitura; para escrita vale o mesmo token GitHub do Miguel (clássico, escopo repo — fonte no Dell: `gh auth token`, espelhado no cofre). Se o seu conector não conseguir ESCREVER no filhosdaimpunidade, avise na ponte que o Miguel resolve. Vercel: não precisa de nada (deploy automático via GitHub).

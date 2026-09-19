# 📕 MISSÃO FDI — Filhos da Impunidade (permanente)

**Criada:** 22/08/2026 11:46 BRT · ordem do Miguel · ZCode Miguel
**Ref:** ZM-20260822-005 · vale para TODAS as sessões do Manus Miguel

---

## 1. Governança (ordem do Miguel, 22/08/2026)

| O quê | Onde |
|---|---|
| **Espaço canônico do FdI** | GitHub: `github.com/migueldorosario1/filhosdaimpunidade` (repo PÚBLICO, branch `main`) |
| **Backup** | Google Drive: `gdrive:filhosdaimpunidade/` (horário no Dell, só o Dell escreve lá) |
| **Deploy do site** | automático: push na `main` → Vercel (`filhosdaimpunidade.vercel.app`) |
| **Memória do projeto no Cérebro** | `cerebro/CEREBRO_NODE_LIVRO_FILHOS_DA_IMPUNIDADE.md` + fóruns/memórias tema FdI |
| **Ponte (você ↔ Dell)** | esta pasta: `cerebro/Foruns/ponte_manus_miguel/` (append-only, sem segredos) |

Regra de ouro: **o GitHub é a verdade do livro**. Drive é estepe. Em divergência, vale o GitHub + registro da divergência aqui na ponte.

## 2. O que é o FdI

- Livro de não ficção de Miguel do Rosário, 2 volumes:
  - **Vol. 1 — O FORAGIDO** (Eduardo Bolsonaro) — 23 capítulos escritos em `Kimi K3/manuscrito/` (00 a 23 + 99 aparatos).
  - **Vol. 2 — O MALANDRO** (Flávio Bolsonaro) — arquitetura em `Kimi K3/ARQUITETURA_VOL2_O_MALANDRO.md`.
- **Site-estúdio:** `filhosdaimpunidade.vercel.app` — SPA monolítica (`index.html`, ~730 KB, livro inteiro embutido em objetos JS; Tailwind CDN + Lucide + marked.js).
- Reforma de 19/08/2026 (commit `1cf8684`): menu 5 dropdowns · **Estúdio do Estilo** (📜 Constituição 10 artigos + 📰 Diretriz Editorial + 🎵 Diretriz de Estilo + 🎼 **8 Prompts de Estilo P1–P8**, CRUD livre) · 📇 Memória do Projeto num arquivo · 📋 Copiar com caixinhas [prompt][memória] · API recuada a exceção.

## 3. Mapa do repo (o que ler, na ordem)

1. `CARTA_AGENTES.md` — como trabalhar no repo (regras de ouro entre agentes).
2. `PROJECT_MEMORY.md` — memória & banco canônico do projeto (Manual de Estilo #1–#27+, diretrizes da Trindade).
3. `CONTRATO_DE_TRABALHO.md` — contrato de trabalho do projeto.
4. `Kimi K3/MANUAL_DE_ESTILO.md` + `Kimi K3/TESE_CENTRAL.md` + `Kimi K3/REFERENCIA_LITERARIA.md` — estilo e tese.
5. `Kimi K3/manuscrito/` — os 23 capítulos canônicos.
6. `Fontes/` — acervo probatório (PDFs, pesquisas, transcrições, reportagem). **Todo fato do livro tem fonte aqui.**
7. `index.html` — o site; os defaults do Estúdio vivem dentro dele: `ESTILO_DOCS_DEFAULT` (Constituição/Diretrizes), `PROMPTS_ESTILO_DEFAULT` (P1–P8), `MEMORIA_PROJETO_DEFAULT` (memória indexada).
8. `Foruns/` (dentro do repo) — histórico de decisões do livro.

## 4. Como o site funciona (para não quebrar)

- Persistência: `localStorage` com chaves `fdi_*` (ex.: `fdi_estilo_doc_constituicao`, `fdi_prompts_estilo_v1`, `fdi_memoria_projeto_v1`, `fdi_copy_cfg_v1`). Defaults vêm do `index.html`; overrides ficam no navegador do Miguel (você não os vê — só os defaults do repo).
- **NUNCA remover o `<div class="hidden">` com os botões legados** (`btn-vol1-v7`, `btn-mode-single`, `theme-toggle-btn` etc.) — o JS reescreve a classe deles por ID; remover quebra volume/modo/tema.
- Teste padrão antes de propor mudança no `index.html`: validar sintaxe dos blocos `<script>` (padrão node/vm usado na reforma, ver memória da reforma no Cérebro).
- Conteúdo sempre **800–1.000 palavras** (vale para post do Cafezinho e para bloco/capítulo).
- Fluxo de produção: **copiar → colar no LLM por assinatura (ChatGPT/Claude/Grok/Gemini) → trazer de volta → gravar versão**. API paga é EXCEÇÃO (botão recolhido no Estúdio).

## 5. Seu papel no FdI

**Pode (e deve):**
- Ler tudo e manter contexto vivo (sessões Manus são efêmeras — registre o estado aqui na ponte).
- Propor: lapidação dos 3 documentos do Estúdio e dos 8 prompts; checagem de estilo de capítulos contra a Constituição (#1–#10 do Estúdio + Manual #1–#27 do PROJECT_MEMORY); revisão factual cruzando `Fontes/`; melhorias de UX do site.
- Trabalhar em branch `manus/<tema>` + PR no repo do FdI, ou entregar a proposta textual em `de_manus.md` para o Dell aplicar.

**Nunca:**
- Commit direto na `main` do FdI sem OK explícito do Miguel (a main dispara deploy na Vercel).
- Deploy/revert na Vercel.
- Expor segredos (tokens, chaves) em qualquer arquivo — aqui só entram NOMES e locais de cofre.
- Inventar fato: é não ficção; sem fonte em `Fontes/`, não entra.
- Apagar trabalho de outro agente; correção = entrada nova (append-only).

## 6. Credenciais (só nome + local — valores NUNCA aparecem aqui)

| Credencial | Onde está | Observação |
|---|---|---|
| GitHub (escrita) | token clássico do Miguel, escopo `repo` — fonte canônica: `gh auth token` no Dell; espelhado no cofre `.env.unificado` | você já tem conector GitHub (acesso ao cerebro-miguel comprovado 20/08); se NÃO conseguir escrever no filhosdaimpunidade, avise em `de_manus.md` |
| Vercel | **não precisa** — deploy automático via integração GitHub↔Vercel | se um dia precisar: criar em vercel.com/account/tokens e espelhar no cofre (ver `CEREBRO_NODE_COFRE_CHAVES.md` §FdI: `FDI_SYNC_SECRET`, `GDRIVE_REFRESH_TOKEN`) |
| Google Drive | você já tem conector (pasta da ponte: raiz `PONTE_MANUS_MIGUEL/`) | no backup `gdrive:filhosdaimpunidade/` você NÃO escreve |

## 7. Primeira missão (22/08)

1. **CHECK** `MM-YYYYMMDD-NNN` em `de_manus.md`: leu esta missão + `CARTA_AGENTES.md` + `PROJECT_MEMORY.md`.
2. Ler os 3 documentos do Estúdio + os 8 prompts (objetos dentro do `index.html`) + capítulo 1 (`Kimi K3/manuscrito/01_estarei_vingado.md`).
3. Entregar em `de_manus.md`: (a) 3 lapidações concretas nos documentos/prompts; (b) checagem de estilo do capítulo 1 contra a Constituição (nota 0–10 + 5 correções mais urgentes); (c) 1 melhoria para o site.

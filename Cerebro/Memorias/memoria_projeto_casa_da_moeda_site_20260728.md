# MEMÓRIA — Projeto Casa da Moeda: Site institucional (log técnico completo)

**Data:** 2026-07-28 · **Agente:** ZCode/Kimi · **Fórum par:** `../Foruns/forum_projeto_casa_da_moeda_site_20260728.md`
**Nodo:** `../CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md`

---

## 1. O que aconteceu nesta sessão (cronológico)

1. **Miguel pediu localização do diretório** do Projeto Casa da Moeda (certificação/controle logístico). Encontrado em `/home/migueldorosario/Downloads/Antigravity Google/Outros/Projeto Casa da Moeda` (279 MB). ⚠️ **O `INDICE_GERAL_PROJETO.md` interno está desatualizado**: aponta raiz em `~/Dados_Frios/Outros_docs/Projeto Casa da Moeda/` — **essa cópia NÃO existe mais**; a única cópia ativa é a do workspace Antigravity.
2. **Miguel anunciou: "vou fazer um site na Vercel, criar GitHub"**. Consulta ao Cofre de Chaves (REGRA Nº 1): `GITHUB_TOKEN` resolvido ✅ (escopo `repo`, smoke 2026-05-31, ecossistema Astro); `VERCEL_TOKEN` pendente mas **não bloqueante** (deploys via webhook GitHub→Vercel). Verificado na máquina:
   - `gh auth status`: logado como **migueldorosario1** (keyring), escopos `admin:org, admin:ssh_signing_key, repo, workflow`, protocolo SSH.
   - Vercel CLI **56.0.0** instalada e **logada como migueldorosario1**.
   - Miguel informado; decidiu usar as contas existentes (não criar novas).
3. **Miguel criou os destinos** e trouxe as URLs: repo `migueldorosario1/casadamoeda` (confirmado existente e vazio via `gh repo view`) e projeto Vercel `miguel-do-rosario-s-projects/casadamoeda`.
4. **ZCode leu o material-fonte completo**: tese final (`pesquisas ia/claude TESE_FINAL_CMB_certificacao.md`, 379 linhas) + roteiro ministerial (`CMB_eixo_certificacao_nacional_roteiro.md`, 20 slides) + base narrativa v4 (`CMB_controle_logistico_v4_base.md`, 39 slides em 6 módulos).
5. **Produzido o anexo técnico de dados** `PROMPT_SITE_ANTIGRAVITY.md` (stack Astro+Tailwind, 12 seções, todos os números verificados da tese, fontes primárias com URLs).
6. **Miguel refinou o pedido**: carta humanizada + estrutura do site "Filhos da Impunidade" adaptada (espaços de correção IA reformulados → cascata vertical de apresentações R1/R2/R3; partes em vez de capítulos).
7. **ZCode estudou a referência**: repo `migueldorosario1/filhosdaimpunidade` — site = `index.html` autocontido (325 KB) + `revisions.json` (schema por capítulo: R1{R2,R3} com `title/author/versionTag/badge/content/rawInstruction/summarizedRule`) + `custom_rules.json` + padrão de cartas em `Foruns/carta_antigravity_*.md` (ex.: `carta_antigravity_site_v7_23cap_vol2_20260727.md` — "🔒 Oficial, abas purpúreas R1/R2/R3, comparativo, DeepSeek V4 Pro").
8. **Produzida a carta** `CARTA_ANTIGRAVITY_SITE_20260728.md` (na pasta do projeto) — substitui/complementa o anexo técnico como documento-mestre para o Antigravity.

## 2. Arquivos criados nesta sessão

| Arquivo | Função |
|---|---|
| `Outros/Projeto Casa da Moeda/PROMPT_SITE_ANTIGRAVITY.md` | Anexo técnico: dados verificados seção a seção, fontes primárias, stack, identidade visual |
| `Outros/Projeto Casa da Moeda/CARTA_ANTIGRAVITY_SITE_20260728.md` | **Documento-mestre p/ o Antigravity**: contexto humanizado + 10 Partes + cascata de apresentações + correção IA reformulada + deploy |
| `Cerebro/Foruns/forum_projeto_casa_da_moeda_site_20260728.md` | Fórum (decisões resumidas) |
| `Cerebro/MEMORIA/memoria_projeto_casa_da_moeda_site_20260728.md` | Esta memória (log técnico) |
| `Cerebro/CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md` | Nodo Camada 2 do projeto (criado — não existia) |

## 3. Arquitetura decidida para o site (referência futura)

- **Padrão "site do livro" adaptado**: `index.html` estático autocontido + JSONs de manifesto — `apresentacoes.json` (parte → versões R1..Rn com oficial 🔒) + `revisoes.json` (correções de texto por parte, schema idêntico ao do livro). Sem backend, sem framework; deploy = push na `main`.
- **Visualização de apresentações**: PPTX não roda no browser → converter versões selecionadas LibreOffice→PDF→PNG/WebP por slide em `slides/<apresentacao>/<versao>/`; PDFs prontos (`CMB_controle_logistico_v4.pdf`, `O_Futuro_v7.pdf`) entram direto; demais arquivos só como download.
- **Mapeamento inicial Parte↔apresentações** (Miguel ajusta via JSON): Diagnóstico ← R1 v3 / R2 v4 / R3 O Futuro v7 🔒 · Evidência ← R1 certificadora / R2 eixo certificação / R3 tese final 🔒 · Solução ← R1 CLN v1 / R2 CLN v4 / R3 CLEC-CMB v4.0 🔒.
- **Regra de ouro de conteúdo**: não inventar números; estimativas marcadas como estimativas (ex.: ¼–⅓ do mercado mundial 2016); honestidade metodológica é argumento do site (R$ 500 bi FNCP = contexto, não receita).

## 4. Estado da infraestrutura (verificado 28/07)

| Item | Status |
|---|---|
| Repo GitHub | `migueldorosario1/casadamoeda` — vazio, `gh` autenticado |
| Vercel | projeto `casadamoeda` em `miguel-do-rosario-s-projects`; CLI logada; deploy automático via GitHub |
| Site do livro (referência) | `filhosdaimpunidade.vercel.app` operacional (200 ✅ 26/07) |
| Artigo CLN | PDF público no Drive: `1EeXMrtevxc-XDyd5yL2-Rr6NEjkyGd6z` |

## 5. Pendências

- Execução pelo Antigravity (carta entregue ao Miguel para colar) → aguardar confirmação no fórum do projeto.
- Validação do Miguel: mapeamento de versões das apresentações; texto final das 10 Partes.
- Conteúdo futuro: status do PL 3.025/2023 no Senado (checar antes de publicitar).

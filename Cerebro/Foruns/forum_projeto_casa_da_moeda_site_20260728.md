# FÓRUM — Projeto Casa da Moeda: Site institucional (decisões resumidas)

**Data:** 2026-07-28 · **Participantes:** Miguel + ZCode/Kimi
**Memória técnica:** `../MEMORIA/memoria_projeto_casa_da_moeda_site_20260728.md`
**Nodo:** `../CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md`

## Contexto

Projeto Casa da Moeda (CLEC-CMB): tese da CMB como âncora pública de confiança em certificação de lacres eletrônicos e cadeia de custódia. Pesquisa concluída (4 IAs × 3 etapas), tese final consolidada em 17/07/2026, artigo científico bilíngue diagramado, 13 apresentações. Pasta: `Outros/Projeto Casa da Moeda/` (279 MB). **Fase nova: site público da tese.**

## Decisões do Miguel (28/07/2026)

1. **Site na Vercel + GitHub** — Miguel criou/confirmou os destinos:
   - Repo: `github.com/migueldorosario1/casadamoeda` (vazio; `gh` já autenticado como `migueldorosario1`)
   - Vercel: `vercel.com/miguel-do-rosario-s-projects/casadamoeda` (deploy automático via push na `main`; Vercel CLI logada como `migueldorosario1`)
   - Não criar tokens/contas novos — usar o que existe (Cofre: GITHUB_TOKEN resolvido ✅).
2. **Construção pelo Antigravity**, guiado por **carta humanizada** (padrão do ecossistema): `Outros/Projeto Casa da Moeda/CARTA_ANTIGRAVITY_SITE_20260728.md` + anexo técnico de dados `PROMPT_SITE_ANTIGRAVITY.md` (todos os números verificados — regra de ouro: não inventar dados).
3. **Estrutura herdada do site "Filhos da Impunidade", reformulada:**
   - Capítulos → **PARTES** (10 partes: Tese · Diagnóstico · Por Que Agora · Evidência · Soberania · Solução · Economia · Roteiro · FAQ · Downloads). *"Não é um livro, é um projeto sobre certificação."*
   - Abas R1/R2/R3 de texto → **cascata vertical de APRESENTAÇÕES** por Parte: cards empilhados (R1 mais antiga → mais nova no topo), cada um com nome, versão, data e **visualizador de slides**; 🔒 Oficial no topo; mapeamento via manifesto JSON (`apresentacoes.json`), nada hardcoded.
   - Espaço de correção com IA **mantido, mas sobre o texto das Partes**: 🔒 Oficial + R1/R2/R3 com `rawInstruction` + `summarizedRule` + comparativo (mesmo schema do `revisions.json` do livro), posicionado abaixo da cascata.
4. **Visual:** tema escuro + verde-bandeira + dourado; big numbers institucionais; sóbrio (política pública).
5. **Mapeamento inicial das apresentações** (proposta do Kimi, Miguel ajusta): Diagnóstico ← v3/v4/O Futuro v7🔒 · Evidência ← certificadora/eixo certificação/tese final🔒 · Solução ← CLN v1/v4/CLEC-CMB v4.0🔒.
6. **Crédito e disclaimer:** "Projeto e pesquisa: Miguel do Rosário, jornalista" + aviso de proposta independente, sem vínculo oficial com CMB/Governo.

## Pendências / próximos passos

- [ ] Antigravity executar a carta (converter slides → imagens, montar site, push) e confirmar no fórum do projeto
- [ ] Miguel validar o mapeamento Parte↔apresentações no `apresentacoes.json`
- [ ] Verificar status do PL 3.025/2023 no Senado antes de divulgar o site (pendência herdada do índice do projeto)

---

## Adendo — Artigo CLN sem links numerados (22/08/2026 ~23:20, ZCode/GLM-5.3)

**Ordem do Miguel (22/08 ~23:15):** tirar os links numerados do texto do artigo e transformar os 2-3 melhores, confirmados, em links silenciosos nas palavras do próprio texto.

**Executado em `Outros/Projeto Casa da Moeda/artigo_cln/`** (backups `.bak_pre_links_silentos_20260822` de pt.tex e en.tex):
1. Removidos TODOS os marcadores `\rc{n}` do corpo (65 no PT + 47 no EN) e a seção "Referências"/"References" (enumerate numerado de 27 entradas com URLs) nas duas línguas.
2. Criados **3 links silenciosos** (hyperlinks nas palavras, sem número nem URL visível — todos HTTP 200 verificados na hora):
   - "passaporte digital de produto" / "Digital Product Passport" → EUR-Lex, Regulamento (UE) 2023/1542 (`eur-lex.europa.eu/eli/reg/2023/1542/oj`) — PT e EN, na Introdução.
   - "plataforma única de rastreio de cargas por satélite" / "single satellite cargo-tracking platform" → URA RECTS (`ura.go.ug/en/rects`) — PT e EN, na Introdução.
   - "Casa da Moeda do Brasil" (negrito mantido) → site oficial (`casadamoeda.gov.br`) — PT e EN, na Introdução.
3. Recompilado com tectonic: `main.pdf` (139 KB) + cópia oficial `Artigo_Controle_Logistico_Nacional_Miguel_do_Rosario.pdf` atualizada. Verificado: 0 marcadores [n] no PDF; as 3 URLs presentes como anotações de link clicáveis.

**Estado:** pronto/entregue. **O que falta:** nada desta ordem; revertíveis via backups .bak. Obs: GS1 EPCIS ficou de fora (curl 000 — não confirmado agora).

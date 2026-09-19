# MEMÓRIA — Portal LOGIS: artigo científico na Revista Logis (log técnico)

**Data:** 09/09/2026 · **Agente:** ZCode Dell (Qwen3.8-Max) · **Fórum:** `../Foruns/forum_logis_artigo_cientifico_20260909.md`

## Localização do artigo (rastro)

- Pedido: publicar na Revista Logis o artigo científico do site antigo (controlelogistico.vercel.app = projeto Vercel `casadamoeda`, código local `Downloads/Antigravity Google/casadamoeda/`).
- No site antigo o artigo é HTML: `paper_pt.html` + `paper_en.html` + `paper_data.js` (não há PDF do artigo no public/ do casadamoeda — só apresentações em `public/downloads/`).
- PDF canônico: `Outros/Projeto Casa da Moeda/artigo_cln/Artigo_Controle_Logistico_Nacional_Miguel_do_Rosario.pdf` ≡ `main.pdf` (md5 `5dd227be10ff8d49210b4e8b6c248861`, 142.433 bytes, 26 p. A4, bilíngue PT/EN — metadata /Title traz os dois títulos; CreationDate 22/08/2026 23:21 -03; Producer xdvipdfmx; fontes `pt.tex`/`en.tex` + `main.tex` wrapper; `.bak_pre_links_silentos_20260822` = versão anterior).
- Abstract real extraído de `pt.tex` (Resumo: conceito CLN, Casa da Moeda âncora, 23 países × 40 operadores, R$ 500 bi/ano, 5 fases) → usado nos resumos PT/EN/ES do card.

## Mudanças no portal (Dell `Downloads/Antigravity Google/logis/`)

| Arquivo | Mudança |
|---|---|
| `public/downloads/artigo-01-controle-logistico-nacional-pt-en.pdf` | NOVO — cópia fiel do PDF (tamanho byte a byte confere: 142.433) |
| `src/data/artigos.ts` | NOVO — `ArtigoCientifico` interface + `ARTIGOS_CIENTIFICOS[]`; artigo 1 com titulo/resumo/palavrasChave nos 3 idiomas (resumo traduzido do abstract real), autor, data 'Agosto de 2026', idiomas 'PT · EN', 26 páginas |
| `src/pages/[lang]/artigos.astro` | NOVO — página da seção: `Section` (hero/parágrafos/nota/cta do PAGES.artigos) + cards dos artigos com botões 📄 Ler (target=_blank) e ⬇️ Baixar (download); estilos .artigo-card/.artigo-numero/.artigo-meta/.artigo-chaves/.artigo-botoes |
| `src/content/pages.ts` | `PAGES.artigos` (pt/en/es: hero kicker 'Revista Logis', nota explicando que o nº 1 vem do site Controle Logístico 2026, cta → revista) + textos do bloco home 'Revista Logis' (3 idiomas) citam «primeiro artigo científico» |
| `src/content/ui.ts` | NAV: `{slug:'artigos', Artigos Científicos/Scientific Articles/Artículos Científicos}` após revista (coluna 2 do rodapé passa a 6 itens); NAV_GROUPS 'Quem Somos': child artigos após revista |
| `src/pages/[lang]/revista.astro` | T ganha artTitulo/artTexto/artVer (3 idiomas) + 2ª `download-box` com botão «Ver os artigos científicos» → langPath(lang,'artigos') |

## Build/deploy/provas

- `npm run build` → **77 páginas** (74+3), 2.31s, sem erro.
- dist checado: `downloads/artigo-01-…pdf` presente; 3 páginas artigos com título+PDF+botão; nav home/revista com `/pt/artigos/`.
- `python3 scripts/deploy_vercel.py` → 99 arquivos, `dpl_A3tBCMP7wxzsJke5Sfs9iJgNcRwE` READY, alias logis-magazine.vercel.app.
- Produção: `/pt/artigos/` 200 «Artigo nº 1» · `/en/artigos/` 200 «Article no. 1» · `/es/artigos/` 200 «Artículo nº 1» · PDF 200 `application/pdf` 142.433 bytes · revista PT com botão «Ver os artigos científicos».
- Git logis: commit `8c22c62` (6 arquivos, +PDF binário) pushado main.

## Links entregues ao Miguel

- Seção: https://logis-magazine.vercel.app/pt/artigos/ (EN: /en/artigos/, ES: /es/artigos/)
- PDF direto: https://logis-magazine.vercel.app/downloads/artigo-01-controle-logistico-nacional-pt-en.pdf

## Notas para o futuro

- Próximos artigos: acrescentar entrada em `ARTIGOS_CIENTIFICOS` (array ordenado; card mostra numero/data automaticamente) + PDF em public/downloads/.
- Candidato a artigo nº 2: `Outros/Projeto Casa da Moeda/artigo/artigo_selo_eletronico_fiscal_v6_cloddy.md` (markdown, precisaria diagramar).
- O site antigo controlelogistico.vercel.app segue no ar (projeto casadamoeda) — nada foi mexido lá.
- Pendência antiga: MTb do Miguel para a página da revista («me cobra depois», 22/08).


## Adendo — ajuste de posição (09/09 ~10:25)

Ordem do Miguel (voz + print da home): (1) 6º card «Artigos Científicos» no grid da home (fecha o buraco — embaixo de Sustentabilidade, do lado de Institucional); (2) item do menu de cima sai do submenu Quem Somos e vira submenu do 1º grupo «Mapas & Dados» («não bota no quem somos»).

- `src/content/pages.ts`: append de bloco `{ t, slug: 'artigos', x }` no fim de `PAGES.home.{pt,en,es}.blocos` (6ª posição = linha 2, coluna 3 do grid).
- `src/content/ui.ts`: child artigos REMOVIDO de 'quemsomos-grupo'; ADICIONADO ao grupo 'mapas' depois de pesquisa. NAV (rodapé) intacto.
- `src/pages/[lang]/index.astro`: `ILUSTRAS.artigos` novo (página com canto dobrado + 3 elipses de átomo, stroke 1.7 igual aos demais) — card da home procura ícone por slug (`b.slug && ILUSTRAS[b.slug]`); sem ícone o card nasceria sem desenho.
- Build 77 páginas (522 ms). Deploy REST `dpl_5WZUQbAJrZCChTXqgQdjZ5dczHGc` READY, alias logis-magazine.vercel.app.
- Verificação produção (curl+python): home pt/en/es 200; card presente; submenu Mapas & Dados com artigos; Quem Somos sem artigos; /pt/artigos/ 200. Os 4 links /pt/artigos/ na home = dropdown desktop + menu mobile + card + rodapé (todos esperados).
- Commit `e694273` (3 arquivos, +5/-1) pushado (github migueldorosario1/logis).

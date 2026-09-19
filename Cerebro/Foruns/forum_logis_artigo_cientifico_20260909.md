# FÓRUM — Portal LOGIS: artigo científico publicado na Revista Logis (1º artigo)

**Data:** 09/09/2026 ~09:1x→09:3x BRT · **Quem:** ZCode Dell (Qwen3.8-Max), ordem do Miguel (voz)
**Memória técnica:** `../Memorias/memoria_logis_artigo_cientifico_20260909.md`
**Nodo:** `../CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md` (seção Portal LOGOS/LOGIS)
**Seção NO AR:** https://logis-magazine.vercel.app/pt/artigos/ · **PDF direto:** https://logis-magazine.vercel.app/downloads/artigo-01-controle-logistico-nacional-pt-en.pdf
**Repo:** github.com/migueldorosario1/logis (commit `8c22c62`)

## O pedido do Miguel (voz, 09/09 ~09:1x)

«A gente publicou o artigo científico na primeira versão do site, que era o Controle Logístico… quero publicar esse artigo científico na revista Logis… cria uma seção Artigos Científicos, com um botão, página só de artigos científicos, e coloca esse artigo — vai ser o primeiro artigo científico da revista. E me dá o link aqui.»

## O artigo (localizado)

**«Controle Logístico Nacional: a Casa da Moeda do Brasil como âncora pública de confiança para a circulação de mercadorias / National Logistics Control: the Brazilian Mint as the public trust anchor for the circulation of goods»** — Miguel do Rosário.
- PDF **bilíngue PT·EN, 26 páginas A4**, compilado em 22/08/2026 23:21 (versão mais recente, com links silenciosos — `.bak_pre_links_silentos_20260822` dos .tex confirma).
- Fonte local: `Outros/Projeto Casa da Moeda/artigo_cln/` (LaTeX pt.tex+en.tex; `Artigo_Controle_Logistico_Nacional_Miguel_do_Rosario.pdf` = `main.pdf`, md5 `5dd227be10ff8d49210b4e8b6c248861`).
- Tese CLEC-CMB: pesquisa documental comparativa, **23 países e 40 operadores de certificação**; oportunidade de R$ 500 bi/ano; cronograma em 5 fases.
- No site antigo (controlelogistico.vercel.app, projeto casadamoeda) ele vivia como HTML (`paper_pt.html`/`paper_en.html` + `paper_data.js`) — o site antigo segue no ar, intocado.

## O que foi feito no portal LOGIS

1. **PDF publicado** em `public/downloads/artigo-01-controle-logistico-nacional-pt-en.pdf` (cópia fiel, md5 confere).
2. **Página nova «Artigos Científicos»** nos 3 idiomas (`/pt|en|es/artigos/`): hero + explicação da seção (acesso aberto diamante) + card do Artigo nº 1 com resumo real (tirado do abstract do LaTeX), autor, data, idiomas, páginas, palavras-chave e botões **📄 Ler o artigo** (abre PDF) + **⬇️ Baixar PDF**.
3. **Botão na página da Revista Logis**: caixa nova «Artigos científicos» com botão «Ver os artigos científicos» → a página nova (nos 3 idiomas).
4. **Navegação**: item no submenu «Quem Somos» ao lado da Revista Logis + rodapé; texto do card da Revista na home (3 idiomas) agora cita «o primeiro artigo científico para download».
5. **Dados centralizados** em `src/data/artigos.ts` — próximos artigos é só acrescentar entrada no array.

## Provas

Build 77 páginas (74+3); deploy REST API `dpl_A3tBCMP7wxzsJke5Sfs9iJgNcRwE` READY; produção: `/pt|en|es/artigos/` HTTP 200 («Artigo nº 1»/«Article no. 1»/«Artículo nº 1» presentes), PDF HTTP 200 `application/pdf` 142.433 bytes (idêntico à fonte), botão na revista presente, nav da home com link.

## Estado da missão

- **O que aconteceu:** 1º artigo científico da Revista Logis publicado em seção própria com botão, nos 3 idiomas, link entregue ao Miguel.
- **O que falta:** nada obrigatório. Futuro: chamada de trabalhos da edição nº 1 (4º tri 2026) pode referenciar esta seção; artigo nº 2 (selo eletrônico fiscal, já em `artigo/` como markdown v6_cloddy) quando o Miguel quiser diagramar.
- **O que preciso do Miguel:** nada para esta missão. Segue pendente o MTb (número de jornalista) para a página da revista (promessa de 22/08).


## Adendo — ajuste de posição (09/09 ~10:25, ordem do Miguel voz+print)

- 6º card «Artigos Científicos» na home: fecha o buraco do grid (embaixo de Sustentabilidade & Segurança, do lado de Institucional); ícone página+átomo desenhado para o card; texto cita acesso aberto diamante e o 1º artigo (3 idiomas).
- Menu de cima: «Artigos Científicos» SAIU do submenu Quem Somos e ENTROU no 1º grupo «Mapas & Dados» (depois de Pesquisa & Dados) — ordem literal: «não bota no quem somos». Rodapé (NAV) mantém o item.
- Arquivos: `src/content/pages.ts` (blocos home ×3), `src/content/ui.ts` (NAV_GROUPS), `src/pages/[lang]/index.astro` (ILUSTRAS.artigos).
- Build 77 páginas; deploy `dpl_5WZUQbAJrZCChTXqgQdjZ5dczHGc` READY; produção: home pt/en/es 200 com card + submenus verificados (mapas tem / quemsomos não tem), /pt/artigos/ 200. Commit `e694273` pushado.

# FÓRUM — Portal LOGIS: versão definitiva da matéria de capa (V6 bíblica + clássica)

**Data:** 09/09/2026 ~08:4x→09:0x BRT · **Quem:** ZCode Dell (Qwen3.8-Max), ordem do Miguel (voz)
**Memória técnica:** `../Memorias/memoria_logis_versao_capa_v6_20260909.md`
**Nodo:** `../CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md` (seção Portal LOGOS/LOGIS)
**Site:** https://logis-magazine.vercel.app · **Repo:** github.com/migueldorosario1/logis (commit `f0c2a83`)

## O pedido do Miguel (voz, 09/09 ~08:4x)

A matéria de capa do portal LOGIS («A logística do crime») tinha **7 versões (V1-V7)** com seletor na página. Pedidos: (1) **ZCode decide** a melhor versão — de preferência com **uma citação bíblica E outra clássica**; (2) guardar as outras numa pasta específica para não perder (**decisão provisória**); (3) site fica com **uma versão só, sem aba/seletor de versões** — só o artigo; (4) ver se o site está atualizado; (5) botar 1-2 matérias atualizadas no portal.

## Decisão: V6 · «a obra e a arma» ✅

Única das 7 que satisfaz o critério (bíblica + clássica):
- **Neemias 4:17** — «Com uma das mãos trabalhavam na obra e com a outra seguravam a arma.» → antes do parágrafo «Cada obra da nova malha logística é dupla por natureza…»
- **Agostinho de Hipona, A Cidade de Deus** — «A paz é a tranquilidade da ordem.» → antes de «A Constituição já deu a ordem…»
- **Foto:** muralhas da Cidade Velha de Jerusalém (Boris Jaramazović, CC BY-SA 4.0) — coerência máxima: Neemias É o reconstrutor das muralhas de Jerusalém; a imagem ilustra a citação.

Descartadas: V1-V5 só clássicas (Cícero/Sun Tzu/Sêneca/Públio Siro/Lao Tsé); V7 duas bíblicas (Neemias 6:3 + Ezequiel 33:7) sem clássica. Tabela completa das 7 em `logis/arquivo_versoes_capa/DECISAO_VERSAO_CAPA_20260909.md`.

## O que foi feito

1. **Arquivo das versões** (decisão provisória, nada se perde): pasta nova `logis/arquivo_versoes_capa/` com documento de decisão + snapshot TS do bloco `variantes` + backups integrais dos 2 arquivos mexidos. As 7 fotos seguem em `public/imagens/`.
2. **Site sem seletor**: `reportagens.ts` (campo `variantes` → `citas` canônicas + foto V6 promovida a foto da matéria) e `[slug].astro` reescrito (sem pills, sem JS de troca, citações fixas visíveis).
3. **2 notícias novas** no bloco «Últimas notícias» da capa (fontes reais, HTTP 200 verificado): **Portogente** «Acesso ao Porto de Santos: dragar o presente ou construir o futuro?» (06/09/2026) + **Gazeta do Povo** «"Dragão de Troia": decisão judicial e pressão dos EUA colocam na berlinda megaporto chinês no Peru» (27/08/2026, tema Chancay — tese central do portal).
4. **Deploy + provas**: build Astro 74 páginas; deploy REST API `dpl_AEvjzTmLibZSERhw6qC1Roadz4JS` READY; produção verificada — matéria PT/EN/ES 200, seletor=0, Neemias+Agostinho+crime-v6 presentes, home PT com as 2 notícias novas.
5. **Repo**: commit `f0c2a83` pushado na main.

## Estado da missão

- **O que aconteceu:** decisão tomada (V6), site atualizado no ar com artigo único + 2 notícias novas, 7 versões arquivadas e reversíveis.
- **O que falta:** nada obrigatório. Opcional: o número profissional de jornalista (MTb) do Miguel para a página da revista (pendência antiga de 22/08 — ele pediu para cobrar).
- **O que preciso do Miguel:** se quiser TROCAR a versão definitiva, é só dizer qual (tabela das 7 no documento de decisão); a reversão ao seletor também está documentada (2 arquivos .bak).


## Adendo — citações TECIDAS no texto (09/09 ~10:57, 2ª ordem do Miguel)

Miguel viu a V6 no ar e vetou os BLOCOS DESTACADOS: «a citação eu não quero com fonte diferente, cor diferente. Eu quero a citação integrada ao texto, colocada casualmente dentro do texto. E integrada ao contexto». Refeito:

- **Neemias 4:17** tecida no parágrafo da «obra dupla», amarrada à FOTO DA CAPA (as muralhas de Jerusalém são as mesmas que Neemias reconstruiu): «Os muros da fotografia que abre esta reportagem são os de Jerusalém. Foi reconstruindo-os, sob ameaça, que os homens de Neemias fixaram a regra de toda construção exposta: com uma das mãos trabalhavam na obra e com a outra seguravam a arma (Neemias 4:17).»
- **Agostinho** tecida no parágrafo da Constituição, jogo ordem × ordem: «A paz é a tranquilidade da ordem, ensinou Agostinho de Hipona há dezesseis séculos. A Constituição brasileira já deu a ordem, ainda que o país a leia pela metade.»
- Nenhuma citação precisou ser trocada — as duas acoplaram ao contexto (critério do Miguel: «se for uma coisa perdida, não tem graça»).
- Mecanismo `citas` REMOVIDO (interface + array em `reportagens.ts`; 3 renders blockquote.epigrafe + estilos em `[slug].astro`). Contagem de parágrafos preservada (substituições in-place) → índices dos gráficos intactos.
- Build 77 p.; deploy `dpl_FtQic4PRAeMTKv6SHht3QKdqnG6S` READY; produção: artigo 200, epigrafe=0, blockquote=0, citações inline (grep 1×1); en/es/home 200. Commit `5c1701f` pushado. Adendo também no doc de decisão em `logis/arquivo_versoes_capa/`.

## Adendo — 18/09/2026 ~20:0x BRT (ZCode/DeepSeek) — 🐞 Bandeirinha de idioma na página de reportagem (bug do Miguel)

1. **Observação do Miguel (18/09 ~19:4x, primeiro reportada como sendo do Moka, depois corrigida por ele: "essa observação era pro legis"):** clicar na bandeirinha de idioma não fica na mesma página — volta para Home.
2. **Causa raiz provada:** `src/pages/[lang]/reportagens/[slug].astro` passava `slug="reportagens"` (só a seção) ao `Base` → as bandeirinhas geravam `/en/reportagens/` (sem o slug do artigo) → **404** → e o `404.astro` é `Astro.redirect('/pt/')` → Home. Ou seja: de dentro de uma reportagem, a troca de idioma sempre caía na Home. No Moka o mesmo bug NÃO existe (testado por navegador em estante/leitor/praticamente todas as rotas: a troca fica na página).
3. **Cura (commit local 59c3bc7, SEM push — aguarda "vai" p/ publicar):** `slug={`reportagens/${r.slug}`}` — as flags passam a apontar para o MESMO artigo no idioma escolhido. Provas: build 95 páginas limpo + HTML gerado com hrefs `/pt|en|es/reportagens/{slug}/` corretos; classe de body `hero-reportagens/{slug}` não quebra nada (nenhum CSS usa `hero-reportagens`).
4. **Pendência:** "vai" do Miguel para rodar o deploy (scripts/deploy_vercel.py) e provar no ar em logis-magazine.vercel.app.

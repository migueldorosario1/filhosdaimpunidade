# 🧠 MEMÓRIA TÉCNICA — Pesquisa custo do crime no PIB + combustível ilegal (18/09/2026)

**Agente:** ZCode/DeepSeek · **Sessão:** ZCodeProject · **Ref monitor:** ZM-CM-CUSTO-CRIME · **Fórum irmão:** `Foruns/forum_custo_crime_combustivel_casadamoeda_20260918.md`

## Missão (ordem do Miguel ~14:4x)
Pesquisar dois blocos colados pelo Miguel (AI overviews de busca): (1) prejuízos da criminalidade + gastos com segurança privada × PIB × competitividade internacional; (2) sonegação/perdas do combustível ilegal administrado pelo crime organizado. Ir atrás dos links e artigos originais. Guardar tudo no diretório local do Projeto Casa da Moeda e no Cérebro.

## Entregas (arquivos tocados)
1. **Dossiê principal:** `/home/migueldorosario/Downloads/Antigravity Google/Outros/Projeto Casa da Moeda/PESQUISA_CUSTO_CRIME_PIB_COMBUSTIVEL_ILEGAL_20260918.md` (4 partes, tabela-mestra de estudos, 23 fontes com URL verificada, nota metodológica de divergências, conexão CLEC-CMB)
2. Fórum: `Cerebro/Foruns/forum_custo_crime_combustivel_casadamoeda_20260918.md`
3. Esta memória: `Cerebro/Memorias/memoria_custo_crime_combustivel_casadamoeda_20260918.md`
4. Catálogo: log no `CEREBRO_NODE_PROJETO_CASA_DA_MOEDA.md` + linha no `CEREBRO_NODE_ATUALIZACOES.md`
5. Monitor: linha ZM-CM-CUSTO-CRIME aberta 14:55 e fechada com ✅

## Receita técnica nova (reusável) — decodificar links do Google News
- **Problema:** `news.google.com/rss/articles/<ID>` não resolve via WebFetch (só retorna "Google News" — redirect JS); Bing RSS ignora aspas/operador site: e polui; DuckDuckGo HTML/Lite = CAPTCHA; Startpage = shell JS vazio; Mojeek = 403.
- **Solução que funcionou (2 scripts em /tmp, refazer se necessário):**
  1. `/tmp/gn_rss.py "<query>"` — lista título|data|ID do Google News RSS via curl+ElementTree (rápido, sem timeout; WebFetch no mesmo RSS dava timeout em paralelo)
  2. `/tmp/gn_decode.py "<ID>"` — GET na página do artigo → extrai `data-n-a-sg` (assinatura) e `data-n-a-ts` (timestamp) → POST batchexecute `rpcids=Fbv4je` com payload garturlreq → devolve a URL real do veículo. Formato do payload: `f.req=[[["Fbv4je","[\"garturlreq\",[...],\"<ID>\",<ts>,\"<sg>\"]",null,"generic"]]]` (3 níveis de colchetes — com 2 dá HTTP 400)
- **Nexo Jornal:** WebFetch lê só o título (Next.js); o texto completo está no JSON embutido `"content":"..."` — extrair com regex + unicode_escape (curl + python).
- **Paywalls:** Valor e Estadão abriram completos via WebFetch direto na URL canônica (sem login).

## Fontes extraídas (todas com URL verificada no dossiê)
Tema 1: Valor 26/08/2026 (Ethos/Insper R$ 285 bi = 4,38% PIB, decomposição 1,35/0,94/0,80/0,58/0,40/0,26/0,05) · Estadão 24/02/2024 (Ipea/Atlas: R$ 171 bi = 1,7% PIB 2022; total 5,9% = R$ 595 bi) · Agência Indústria/CNI 26/05/2026 (Sondagem Brasil Legal: R$ 107 bi = 68,5+39,1; 1.398 empresas, 32 setores, nov/2025) · Nexo 11/04/2026 (Robson Rodrigues: 4,2% PIB setor privado = R$ 450+ bi; CNI 16 setores; 370 mil empregos; R$ 500 bi) · Jovem Pan/David de Tarso 31/08/2026 (Fiesp 3 pesquisas: 70% competitividade internacional, 98% gastam c/ segurança, 84% famílias) · Gazeta 31/03/2025 (BID 1,6% PIB privado AL; 3,4% custos diretos; FMI +0,5 p.p.) · Gazeta 10/02/2026 (Igarapé/Muggah R$ 1,3–1,5 tri = 11–14% PIB, decomposição 373+468+300+190/200+3) · BBC 07/02/2017 (faixa 3,78%–13,5%; BID US$ 124 bi 2014; IEP US$ 338 bi 2016) · Agência CNI 15/08/2017 (R$ 27,1 bi = 10,5+10,8+5,8; 2.952 indústrias).
Tema 2: CNN 28/05/2026 Fluxo Oculto (nafta, 6 fintechs R$ 26 bi/4 anos, R$ 200 mi sonegação/2 anos, cripto R$ 365 mi, 12 empresas nomeadas) · G1 30/11/2025 (R$ 1 tri/ano o setor; PCC 40 fundos > R$ 30 bi; R$ 2 bi notas fictícias; Refit R$ 9,6 bi em SP) · CNN 13/06/2025 (FBSP R$ 347,8 bi desde 2022; cocaína R$ 15 bi; Esfera/FBSP R$ 335 bi cadeia cocaína; Bottini R$ 450 bi/2022) · Exame 13/02/2025 (Follow The Products: R$ 348,1 bi/ano; combustíveis R$ 61,5 bi = 41,8%; 13 bi litros = 8,7% mercado; recomenda blockchain + marcação isotópica) · Agência Brasil 27/11/2025 (Poço de Lobato: 126 mandados, R$ 10,2 bi bloqueados, 15+ offshores EUA, 50 fundos; Op. Cadeia de Carbono anterior apreendeu 4 navios + 180 mi litros) · CNN 27/11/2026 Refit (R$ 26 bi; R$ 70 bi movimentados; Receita+MPSP+CIRA+PGFN) · G1 28/11/2025 Refit (R$ 32 bi importações 2020–2025; Magro desde 2008, Miami desde 2016; Recomeço 2016; Carf 2020) · Metrópoles 15/05/2026 (Interpol difusão vermelha Magro; Op. Sem Refino; R$ 52 bi bloqueados; Cláudio Castro alvo; defesa: R$ 1 bi pago ao RJ) · Metrópoles 06/08/2026 especial (ICL R$ 30 bi = 15,7+14; Brasil Contra o Crime Organizado R$ 11,1 bi; FBSP/Datafolha 41,2% reconhecem facções = 68,7 mi) · Brazil Journal 04/09/2024 (FGV 2021: R$ 30 bi; nafta 1% TO × 25% SP; dívida ICMS R$ 65 bi, estados recuperam 1%; R$ 178 bi/10 anos; PLP 164/2022) · ICL 18/09/2026 (6 anos: 3 bi litros retirados; 28% adulteração 2025; **PLP 125/2022 = LC 225/2026**; PL 1482/2019; PLP 109/2025; PL 399/2025; LC 192/2022; Lei 14.993/2024).

## Erros corrigidos no caminho
- Texto do Miguel citava "CNI R$ 68,8 bi preventivos" → matéria oficial diz R$ 68,5 bi no corpo (divergência interna da própria CNI); "45% repassam ao preço" não confirmado.
- URL Metrópoles do snippet (`/mercadoilegal/combustiveis`) = 404; correta: `/conteudo-especial/ate-quando-o-brasil-pagara-a-conta-da-ilegalidade-nos-combustiveis`.
- Agência Brasil chama o grupo de "Grupo Fit" no corpo (typo do veículo; é Refit/Manguinhos).

## Estado da missão
- O que aconteceu: pesquisa 100% executada e arquivada (projeto + Cérebro), 19 artigos originais extraídos, fact-checking do texto-base registrado.
- O que falta: baixar PDFs primários (FBSP Follow The Products; Sondagem Brasil Legal CNI; Cerqueira/Ipea) se o Miguel quiser anexos; plugar números nas apresentações CLEC-CMB.
- O que preciso do Miguel: sinal sobre PDFs e sobre uso na apresentação da tese.

## ADENDO TÉCNICO (18/09 ~15:5x) — Transcrição YouTube

Vídeo KjVCEC7MPAY (Spotniks, "O problema geográfico do Brasil", 46:18, pub. 27/08/2026): yt-dlp 2026.07.04 baixou auto-subs PT OK (HTTP 429 na 1ª tentativa multi-idioma; resolver com `--sub-langs "pt-orig|pt"` + `--sleep-requests 2`; warning de JS runtime/ausência de impersonation não impediu). VTT→TXT: strip de tags/timestamps + dedup de fragmentos sobrepostos. Produto: `Outros/Projeto Casa da Moeda/videos/` (VTT + TXT bruto + MD analisado). Auto-legenda truncou 3 números falados (sistemas isolados ~R$ 1,8 bi/+115%; programa aéreo AM 2021; "século X"=XVI) e errou nomes próprios (Hu Huanyong, Borlaug, Kiihl, ANTAQ) — correções documentadas; [sic] onde incerto. Análise agregada como Parte 5 do dossiê (geografia = 3ª perna do imposto oculto; complementa crime + mercado ilegal).

## ADENDO TÉCNICO 2 (18/09 ~16:0x) — Dois dossiês completos

DOSSIE_1_SEGURANCA_PRIVADA_CUSTO_ECONOMIA_20260918.md + DOSSIE_2_PETROLEO_COMBUSTIVEL_CIRCULACAO_20260918.md em Outros/Projeto Casa da Moeda/. Dossiê 1 incorporou da coletânea do projeto: FNCP R$ 468 bi contrabando 2024 (G1 seção 12), Cerco Inteligente ES (seções 14-17, Dahua×SEFAZ placa×nota×rota), mercado segurança eletrônica R$ 6,52 bi 2018 ABESE, Mare Liberum R$ 86,6 bi (seção 24, IstoÉ). Ordem do Miguel: Sicobe rebaixado a exemplo histórico pontual (era fio condutor no 1º rascunho mental — corrigido). Próximo passo possível: expandir o resumo-semente em artigo completo p/ Revista Logis usando os 2 dossiês como base documental.

## ADENDO TÉCNICO 3 (18/09 ~18:0x) — Publicação Logis

3 artigos adicionados em logis/src/data/reportagens.ts (entradas 3-5 do array; REPORTAGENS[0] = capa preservada). Imagens Commons baixadas c/ UA browser (thumb URLs /1600px- falharam — usar originais + resize PIL 1600 local, quality 82); crop 16:10 na vertical. Build Astro 95 páginas. DEPLOY: scripts/deploy_vercel.py (REST); 1º deploy travou em INITIALIZING 15 min sem eventos → cancelamento via PATCH /v12/deployments/:id/cancel (DELETE/POST dão 404) → 2º deploy READY em ~1 min → alias de produção NÃO migra sozinho: POST /v2/deployments/:uid/aliases {"alias":"logis-magazine.vercel.app"}. Prova: 200 × 3 PT + notas + en/es + 3 imagens.

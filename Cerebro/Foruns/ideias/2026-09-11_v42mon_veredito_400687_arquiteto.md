# 🧮 VEREDITO V42MON-400687 — «O impacto da alta taxa Selic sobre a economia brasileira» (cat 100005 Estatística, 11/09/2026 06:36:06)

> **Ofício:** `IDEIA_PRO_DSNUVEM_IDEIAS-V42MON-OFICIO` (protocolo `2026-09-03_oficio_inicial_acompanhamento_v42.md`) · **Pedido formal:** AUSENTE — o watcher `v42_espelho_watcher.py` segue PARADO no 400328 (dono ZM; 20ª cobrança de religação). **Detecção:** sonda REST própria do DS-N ~7 min pós-publish (06:43), mesma via dos 400680/400683.
> **Refs:** vereditos anteriores do stem/gênero: **400683 (11/09 03:36, 🟠)** · **400680 (02:36, 🔴 gates furados)** · **400677 (10/09 14:07)** · **400668 (10/09 07:35)** · **400664 (10/09 05:35)** · **400660 (04:35)** · **400657 (03:36)** · **400648/400644/400636 (09/09)** · ofício inicial `2026-09-03_oficio_inicial_acompanhamento_v42.md`.
> **Assinatura do autor da matéria:** uid 5470 (mesmo id do canônico «esteira»; no espelho o slug é «Redação» — I9). **Meta:** só `v42_texto_sha256 = 28b0f8ced16c346aa433deef431f7df61c2b5a82212d2b1e9f2e8c3fc06b396f`.
> **Capa:** `featured_media 400685` (`bcb-bcb-432-line-14-scaled.png`, criada 06:35:53 = **13 s antes do post**), **alt correto** («Taxa básica de juros do Brasil (Selic), últimos 12 meses»), **caption VAZIA** (repetição do 400680).
> **Leitura:** REST pública do espelho `cafezinho.news` — leitura pura, nada executado, sem credencial. **publish=0 — Lei de Poderes.**

---

## 1. O que o post diz (resumo fiel)

Tese única, repetida em 6 parágrafos: **a Selic está em 14,0% a.a. (setembro/2026), quase 4× os 3,63% do Fed; isso segura o dólar (R$ 5,1149), mas custa caro — dívida pública caríssima, crédito caro, freio no crescimento, renda ao rentismo; reduzir a Selic é «tarefa histórica».** Números no corpo: **4** (14,0% · 3,63% · «quase quatro vezes» · 5,1149). Parágrafos de opinião pura: ~4 («entrave ao progresso», «compromete o futuro do país», «inclusão social»). **0 links, 1 imagem inline (o gráfico do Fed), rodapé de 3 fontes.** 2.206 caracteres de HTML.

## 2. Auditoria número a número — 3 de 3 conferidos no próprio rodapé

| Afirmação do texto | Fonte declarada no post | Veredito |
|---|---|---|
| Selic «14,0% ao ano em setembro de 2026» | BCB/BCB_432 (`14.0 % a.a.`, 2026-09-10) | ✅ confere |
| Fed «3,63%» | FRED/FEDFUNDS (`3.63 %`, 2026-08-01) | ✅ confere (mas janela/inst. — ver I2) |
| «quase quatro vezes superior» | 14,0 ÷ 3,63 = **3,857** | ✅ confere aritmeticamente |
| Dólar «R$ 5,1149» | BCB/BCB_1 PTAX venda (`5.1149`, 2026-09-10) | ✅ confere |

**Afirmado sem fonte / não conferível nesta matéria:**
- **«variação 12m: +0,00% · variação período anterior: +0,00%» na linha da Selic** — os dois períodos zerados. Plausível para série travada em 14%, mas é exatamente a assinatura de **campo nulo renderizado como zero** (família I1: o número tem de carregar a lista E o critério). **NÃO PROVADO** — fica como pergunta ao dono do pipeline, não como achado.
- **«sustentabilidade fiscal em risco» / «inclusão social»** — juízo editorial, não dado. Nenhuma fonte sustenta.

## 3. Achados (linhas de ouro do arquiteto)

**(1) 🔴 O ECO DA SÉRIE `politica_monetaria_comparada` É O MAIS EXPLÍCITO JÁ MEDIDO — E O GATE ANTI-ECO FALHOU PELA 3ª VEZ EM 26 h.** A mesma tese foi publicada **5 vezes em ~3 dias**: **400636 (09/09 04:35) · 400648 (09/09 09:36) · 400664 (10/09 05:35) · 400668 (10/09 07:35) · 400687 (11/09 06:36)**. Similaridade de título do 400687: **0,9107 com o 400636 · 0,7458 com o 400664 · 0,6393 com o 400668** — **três âncoras ACIMA do limiar 0,60** dentro da lista dos 10 últimos, e o gate passou. É o 3º furo em 26 h (400680=0,8333 contra 400641 · 400683=0,7794 contra 400660 · agora 400687=0,9107 contra 400636). **A manchete é reescrita por reordenação de palavras** («alta taxa Selic» ↔ «taxa Selic alta») e o gate de título não vê.

**(2) 🔴 O CORPO É O MESMO TEXTO COM SÓ A COTAÇÃO DO DIA TROCADA — agora com prova de frase.** A primeira frase depois do lide é **byte-idêntica** em 400664/400668/400687 — «A taxa básica de juros do Brasil (Selic) está em 14,0% ao ano em setembro de 2026. […] quatro vezes superior à taxa de juros dos Estados Unidos, que é de 3,63%» — e no 400636 muda só «está fixada em». O **único** campo que gira é o PTAX: **5,0856 (09/09) → 5,0979 (10/09) → 5,0979 (10/09) → 5,1149 (11/09)**. É o «rodapé byte-idêntico» dos 400680/400683 medido agora no **corpo**: o resto é cenário com carimbo de hoje.

**(3) 🟠 O GRÁFICO DO CORPO É DO OUTRO PAÍS — e é um asset FIXO que só troca o sufixo.** Em **todos** os posts da família a figura inline é a **FRED Fed Funds** (`fred-fedfunds-line-9/11/12/13-scaled.png`) com a legenda «Taxa básica de juros dos Estados Unidos (Fed)». A matéria é sobre a **Selic brasileira**; o gráfico que a ilustra é a série **dos EUA** (que é o contraponto, não o objeto). O sufixo «line-N» incrementa por post = **mesmo gráfico re-renderizado diariamente**, não um dado novo. A capa (BCB Selic) está correta; o corpo ilustra o outro país.

**(4) 🟠 O «SELO ANÁLISE DE…» É DE GÊNERO, NÃO DE UM STEM.** Os 5 posts abrem com o lide-molde **«Análise da/do…»** (400687 «Análise da Selic e suas consequências…» · 400664 «Análise do impacto da taxa Selic…» · 400668 «Análise da taxa Selic…»), e o veredito 400680 já tinha achado **8/8** do stem `comercio_sul_sul` com «Análise do…». **Não é um stem desobediente — é a regra 18 sem enforcement em pelo menos 2 stems.** A proposta I4 do 400680 (regex de abertura) segue sem dono.

**(5) 🟠 A JANELA MISTURA META COM REALIZADO E DIÁRIO COM MÉDIA MENSAL.** O post cola a **Selic META** (BCB_432, alvo, leitura de **2026-09-10**) com o **FEDFUNDS** (FRED, taxa **efetiva realizada**, **média mensal**, último **2026-08-01**) na mesma frase e mesmo tempo verbal («é de 3,63%»). São **dois instrumentos diferentes** (meta × efetiva) e **duas janelas diferentes** (10/09 × 01/08 = **41 dias**) — a mesma classe de erro de janela dos 400651/400683.

**(6) 🟠 O META É OPACO — E FALTA EM 3 DOS 6 ÚLTIMOS.** Só existe `v42_texto_sha256`; **não há** pacote, lista de comparação nem ramo do gate. E o sha **está ausente em 400668, 400657 e 400636** (3 de 6 da série recente). De fora do banco não se audita o portão — a assinatura que deveria fechá-lo é a que falta (I5 do 400680/400683, 3ª vez pedido).

**(7) 🟡 A CAPA NASCE 13 s ANTES E O caption NUNCA É PREENCHIDO.** A media 400685 existe às 06:35:53, o post sai 06:36:06 — o gate visual está vivo. Mas o `caption` vem **vazio** (como no 400680) enquanto o `alt` vem correto. A régua da casa pede **caption + crédito + alt**: o pipeline preenche 2 de 3 e não avisa.

## 4. Arquitetura do conserto (propostas; dono ZM/us65 — nada executado)

- **I1 — REGISTRO DO GATE NO META (repetido do 400680/400683):** gravar no meta o **pacote**, o **hash da lista de comparação**, o **ramo do gate** (`bloqueou`/`passou`) e, quando passar, o **par de maior similaridade e o score**. Sem isso, o 0,9107 do 400687 é indetectável de fora.
- **I2 — ECO POR CONJUNTO, NÃO POR TÍTULO (repetido):** bloquear quando o **conjunto de valores das fontes** (menos a cotação diária de série) repetir o de um post dos últimos N dias. O 400687 seria barrado: `{14.0, 3.63, 5.1149}` repetido com só a cotação girando.
- **I3 — GATE DE ABERTURA (enforcement da regra 18):** regex de primeira frase contra `^An[áa]lise d[ao]` no lide/corpo, com **bloqueio ou reescrita obrigatória**. Vale para os 2 stems medidos (comercio_sul_sul e politica_monetaria_comparada).
- **I4 — INTEGRIDADE DE JANELA E DE INSTRUMENTO:** o par (série × janela) não pode cruzar **meta × efetiva** nem **diária × média mensal** numa mesma frase sem rótulo explícito. Proposta mínima: exigir, na frase comparativa, a **data de referência de cada série** colada ao número.
- **I5 — RODAPÉ E GRÁFICO CASADOS COM A TESE:** se a matéria é sobre a Selic, o gráfico inline obrigatório é o **BCB_432** (hoje é o Fed); e `variação +0,00%` só sai se o pipeline **provar o zero** (senão imprime «n/d»), para não confundir nulo com zero (I1 da família Instrumento × Evidência).
- **I6 — CAPA 3/3:** preencher `caption` + `crédito` no `set-media` (o `alt` já vem); falha de caption deve **avisar**, não passar silenciosa.

## 5. Plano de execução (numerado; nenhum passo executado nesta ronda)

1. **Backup:** `pg_dump`/cópia das tabelas de pacote, gates e `postmeta` do V4.2 antes de qualquer toque (dono ZM/us65).
2. **Prova (somente leitura):** rodar a query que lista, para o 400687, o pacote de origem, a lista dos 10 últimos títulos e o score real do gate — responde **por que 0,9107 não bloqueou**. É o passo que precede qualquer conserto (I1).
3. **Registro:** gravar o resultado da query no Cérebro, com o par de maior similaridade e o ramo do gate.
4. **Conserto mínimo e reversível:** I3 (regex de abertura) e I6 (caption) são de 1 linha e reversíveis por revert do commit; I2 e I4 exigem dry-run sobre a série histórica antes de ligar.
5. **Rollback escrito:** cada item com o comando de reversão declarado antes de aplicar; nada aplicado sem ✓ do Miguel.

## 6. O que precisa do Miguel

1. **✓ I1** — gravar o ramo do gate no meta (4ª vez pedido; é o que destrava a auditoria de fora).
2. **✓ I2 e I3** — eco por conjunto numérico e enforcement da abertura (dono ZM) — o 400687 é a prova viva: 0,9107 de título e o lide-molde.
3. **✓ I4** — integridade de janela e de instrumento (meta × efetiva; diária × mensal).
4. **✓ I5 e I6** — rodapé/gráfico casados com a tese e capa 3/3 (caption + crédito).
5. Seguem abertos da série: **rel sponsored nofollow + regra comercial=página** (43 âncoras dofollow dos 269144/269155) — 9ª caçada pedindo; **P7** (zerar `aviso_ts`/`critico_ts` na recarga, pré-condição da recarga, saldo projetando zero ~12:00); **I8** reconciliação de páginas do espelho e **I9** identidade cross-site; **religar o watcher V42MON** (@ZM — 20ª cobrança); **✓ SEM_VERSAO** (msg 143).

---

*Veredito do DS-N Ideias (2/2h) — leitura pura, nada executado. publish=0 — Lei de Poderes. Donos: @ZM/us65 (pipeline, gates, capa) · CL/CM (abertura editorial).*

— DS Nuvem Ideias (DS-N Ideias) · 20260911 06:44:36 BRT

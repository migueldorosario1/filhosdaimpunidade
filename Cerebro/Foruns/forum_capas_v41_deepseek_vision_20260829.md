# Fórum — Capas V4.1 × DeepSeek Vision (missão 29/08/2026)

> **Estado:** FASE 1 (POC + fixes estruturais) CONCLUÍDA · FASE 2 (revisão humana + integração) AGUARDA "vai" do Miguel
> **Quem:** ZCode/Qwen 3.8 (ZM), a pedido do Miguel ("voce consegue resolver essas capas? a gente tem agora o deep seek vision se precisar")
> **Regra sagrada aplicada (ordem do Miguel 29/08 ~17h):** nada publica sem VER — visão descreve, segunda visão descreve e cruza, olho humano confirma.

## O que aconteceu

1. **POC provou o pipeline E2E** (`codigo.featured_image_runtime_cli` no NYC): cascata acervo auditado → Flickr contas oficiais → Commons/Openverse → ilustração IA; auditoria de pixels com **DoubleCheckMediaVisionProvider = DeepSeek (primário) × Qwen (cruzamento)**; fail-closed sem imagem auditada; upload WP é operação separada por design.
2. **Causa-raiz nº 1 (credencial):** `chaves.sh` tinha DUAS linhas `DEEPSEEK_API_KEY` — a morta (sha8 `b6c4d4de`, 401 em texto E visão) e a viva (sha8 `f0aaa272`, validada 28/08). Quem sourciava `chaves_novas.env` POR ÚLTIMO ficava com a morta → DeepSeek 401 → Qwen respondia SOZINHO (sem cruzamento) com bboxes errados → 100% de rejeição. **Fix (Regra 4):** morta deprecada com carimbo nos cofres vivos, backups `.bak_pre_higiene_deepseek_20260829`, válida espelhada em `chaves.sh` + `chaves_novas.env` + `.env.unificado` (paridade conferida por hash, valores nunca expostos).
3. **Causa-raiz nº 2 (Flickr fora dos crons):** `FLICKR_API_KEY` só existia em `chaves_novas.env`; espelhada no `chaves.sh` (sha8 `9c684254`) para qualquer cron que sourceia só o primeiro.
4. **Causa-raiz nº 3 (bug real no collector Commons, `open_catalog_media.py`):** declarava dimensões do ORIGINAL mas servia thumb derivado → `media_declared_width_mismatch` matava toda a perna Wikimedia ANTES da visão; e `iiurlwidth=2400` hoje dá **HTTP 400** (Wikimedia só aceita tamanhos comuns da lista w.wiki/GHai). **Fix:** derivado declarado proporcional + `iiurlwidth=1920`. Backup `.bak_pre_fix_thumbdims_20260829`. Depois do fix, as fotos da estação Santa Cecília 2024 CHEGARAM à visão.
5. **Lotes:** 6 rodadas dos 5 pedidos (268226/268228/268236/268245/268250). Com as duas visões abertas, as rejeições restantes são EDITORIAIS, não técnicas.

## Leitura humana (olho do editor, regra sagrada)

| Draft | Melhor candidata vista | Veredito do gate | Leitura ZM |
|-------|------------------------|------------------|------------|
| 268228 Leila Pereira | Foto Agência Senado, CPI das Apostas, jun/2024, CC BY, close dela falando ao micro | bloqueado: origem não confiável p/ pessoa nomeada + divergência DS×Qwen de identidade | **válida p/ Emenda 12** (jornalística, recente, pessoa proeminente) → caso de revisão humana |
| 268226 Santa Cecília SP | Estação Santa Cecília, 2024, CC BY-SA, nome do bairro grande na faixa | bloqueado: painel artístico da parede classificado como logo/montagem + proeminência | **válida editorialmente** (marco do bairro, recente) → caso de revisão humana |
| 268236 EUA×Canadá | só fotos de cúpula antigas/letters de tarifa | rejeitado | fraco — precisa busca nova ou revisão humana |
| 268245 Anthropic | só Dario Amodei 2023 no Commons + screenshots | rejeitado | fraco p/ regra de frescor do Miguel |
| 268250 Siraya | Lai Ching-te em atividade Siraya 2021 (CC BY) | coleta openverse lenta (timeout) | médio — caso de revisão humana |

## O que falta (Fase 2 — proposta)

1. **Ferramenta de revisão humana** (`media_human_review_cli`): o contrato gera status `human_review` mas NÃO tem caminho de promoção aprovada por editor humano ao acervo auditado (`promote()` é fail-closed no recibo). Proposta: CLI append-only que grava registro auditado com operador+motivo+recibo+hash da imagem, mantendo trilha. **Muda política editorial → aguarda "vai" do Miguel.**
2. **Integração no `v41_ciclo`** (oferta ZM-009): chamar o runtime após criar rascunho + cron varredura de drafts sem capa no NYC (crons atuais nem sourcam chaves.sh — item 2/3 acima já resolvem o env).
3. Aplicar as capas aprovadas (upload WP + `_thumbnail_id` + meta de cheque §86 + mapeamento `wordpress_media_cli add`).

## O que preciso de você (Miguel)

- **"vai" p/ ferramenta de revisão humana** (item 1) — sem ela, capas de pessoa/temas nichados nunca passam automaticamente, por design.
- Se preferir: autorizar exceção pontual p/ as 2 capas que EU vi e aproveito sob minha assinatura (268228/268226), registradas como revisão humana no acervo.

## Backups desta missão (NYC)

`/root/v4_labs/codigo/open_catalog_media.py.bak_pre_fix_thumbdims_20260829`, `/root/chaves.sh.bak_pre_higiene_deepseek_20260829`, `/root/chaves_novas.env.bak_pre_higiene_deepseek_20260829`.

— ZCode/Qwen 3.8 · 29/08/2026

## ADENDO 29/08 ~18:20 — DeepSeek Vision testado do Dell + cruzamento de identidade (caso-escola da regra sagrada)

Pergunta do Miguel: "o deepseek vision está funcionando? você pode usar ele aqui se precisar?" → **SIM nas duas.** Teste ao vivo do Dell (`/tmp/ds_vision_dell.py`): chave lida do cofre local (sha8 `f0aaa272` = mesma viva do NYC; espelhos locais corretos — a diferença de hash anterior era só metodologia de cálculo) · HTTP 200 · 746 tokens (195 de raciocínio) · custo < US$ 0,001.

**Cruzamento de identidade na candidata de 268228 (`/tmp/leila_cpi.jpg`):** o DeepSeek disse **Maria do Rosário (ERROU)**; meu olho sozinho ficou incerto (também inclinou p/ Maria do Rosário); o desempate veio do metadado oficial: busca por SHA1 (`6931e37b…`) no Commons devolveu o arquivo `Leila_Pereira_-_CPI_da_Manipulação_de_Jogos_e_Apostas_Esportivas_(cropped).jpg` — o título da agência-fonte nomeia a MESMA entidade do draft (Leila Pereira).

**Lição (reforça a regra sagrada):** visão é fundamental mas NÃO é infalível em identidade de pessoa. Ordem de evidência: metadado oficial da fonte > cruzamento de duas visões > visão sozinha. O gate `origin_trusted` do pipeline e a divergência DS×Qwen nesta foto foram comportamento CORRETO, não defeito.

**Impacto em 268228:** identidade agora confirmada por legenda oficial + olho (Leila Pereira, CPI das Apostas 2024, CC BY, foto recente e jornalística = Emenda 12 satisfeita). O caso da exceção de revisão humana fica MAIS forte; o único bloqueio continua sendo o gate de contrato (Commons = origem não confiável p/ pessoa nomeada) → `media_human_review_cli` ou exceção única seguem aguardando o "vai" do Miguel.

## ADENDO 2 29/08 ~18:30 — PAINEL DE VISÃO: 5 olhos, 5 nomes, 0 acertos (a prova definitiva da hierarquia de evidência)

Ordem do Miguel: "tira a prova com gemini vision, glm, assemblyai ou qualquer outra". Rodado `/tmp/painel_visao.py` do Dell (chaves do cofre local, só hashes expostos) na mesma foto (`/tmp/leila_cpi.jpg`, ground truth = título oficial Commons via SHA1: **Leila Pereira** na CPI das Apostas):

| Olho | Resposta | Veredito |
|---|---|---|
| ZCode/Qwen 3.8 (olho humano-agente) | incerto, inclinou p/ Maria do Rosário | ❌ |
| DeepSeek `vision-exp` | Maria do Rosário | ❌ |
| Qwen-VL `qwen-vl-max` (dashscope-intl) | "Zulema S. Gómez", política mexicana | ❌ alucinado |
| Grok-4 (api.x.ai) | Marina Silva | ❌ |
| Gemini 2.5-flash | "Maria Emilia de Rueda", diplomata | ❌ alucinado |
| **Metadado oficial (SHA1→Commons)** | **Leila Pereira** | ✅ |

**Conclusão estrutural:** NENHUM modelo de visão é confiável para NOMEAR pessoa por rosto — todos alucinam com confiança. Visão serve para o que o pipeline já usa: formato (screenshot/logo/montagem), enquadramento, qualidade, frescor visual, pessoa-ocupa-o-frame. Identidade = metadado de origem confiável + olho humano (e, na falta, `media_human_review_cli`). GLM 5.3: sem pacote de visão (429 provado 28/08). AssemblyAI: transcrição de áudio, não vê imagem. O DoubleCheck DS×Qwen continua valendo como gate de FORMATO/consistência, não de identidade.

## ADENDO 3 29/08 ~18:45 — CAÇADA DE FONTES POLÍTICAS ATUAIS (ordem do Miguel: Flickr sobretudo + bancos estatais)

**Método:** API Flickr do NYC (chave do cofre) — descoberta por texto (7 dias, licenças abertas {4,5,7,8,9,10,11,12} = as que o pipeline aceita; 11=CC BY 4.0, 12=CC BY-SA 4.0) + auditoria de atividade/licença de cada conta da allowlist.

**Resultados:**
- **NOVAS na allowlist (verificadas ativas + abertas):** `cldf` = Câmara Legislativa do DF / Agência CLDF (150593541@N02, CC BY-SA 4.0, postou há 1d) e `camara_itajai` = Câmara de Vereadores de Itajaí (130745879@N07, CC BY 4.0). Legislativos, como pedido.
- **DEPRECADAS (histórico preservado em `_deprecadas_20260829` no config, backup `.bak_pre_fontes_flickr_20260829`):** `camara`/`stf`/`tse`/`agencia_brasil` (usernames não resolvem na API — as fontes estavam MUDAS sem ninguém perceber), `planalto` (0 fotos), `governo_rio` (88d + licença 0 ARR).
- **Descartadas na auditoria:** Ministério da Fazenda (158 fotos mas licença 0 ARR) e Vice-Presidência (14 anos sem postar, ARR) — existem mas não servem; STF/TSE/Câmara/EBC **não têm** conta Flickr viva com licença aberta.
- **Vivas e fortes (já na allowlist):** Senado (29 fotos/7d, CC BY-SA 4.0, última há 1d) e Lula Oficial (9 fotos/7d, última HOJE).

**Catálogo de bancos estatais NÃO-Flickr (caminho real p/ foto política atual — Fase 2/3, coletores dedicados):** Agência Senado (senado.leg.br, CC BY — foi a origem da foto da Leila na CPI via Commons), Agência Câmara (camara.leg.br, CC BY), Agência Brasil/EBC (agenciabrasil.ebc.com.br, CC BY), agências de notícias estaduais e sites das assembleias legislativas (CLDF inclusa), ministérios (Fazenda etc. publicam no próprio site), TSE/STF (centros de mídia). O Flickr é espelho pobre desses órgãos; os bancos oficiais são a fonte primária. Commons já espelha parte (caso Leila provou).

**Incidente de segurança:** num grep de cofre (`cut -c1-60`) parte do valor da FLICKR_API_KEY apareceu no output da ferramenta (~26 chars). Sem exposição em chat/fórum/código, mas recomendo ao Miguel rotação da chave quando quiser (Flickr app dele); procedimento Regra 4 já padrão p/ espelhar a substituta. ⚠️ Não confundir com o incidente do pacote aberto `c16c3c121` (3 credenciais) — esse o Miguel ENCERROU sem rotação por ordem direta (DSC-20260829-020, 21:59, "não manda trocar nada"); a recomendação da chave Flickr segue aberta e separada.

## ADENDO 4 29/08 ~22:05 — A FILA ANDOU: loop noturno publicou os drafts COM CAPA (inclusive a Leila da CPI que a missão validou)

**O que aconteceu (janela 19:43→22:00, publicado pelo loop Laura/AGY):**
- **268228 Leila Pereira** (20:05) → capa **268263 "Leila Pereira na CPI da Manipulação de Jogos e Apostas Esportivas"** (`leila-cpi-2024.jpg`) — EXATAMENTE a candidata que esta missão verificou a olho + prova SHA1→Commons (ADENDO 1). O caso-escola fechou no ciclo completo: visão errou o nome, metadado oficial acertou, foto certa foi ao ar.
- **268250 Siraya/Taiwan** (20:38) → capa **268265 "Jovens indígenas de Taiwan em evento cultural"** (`taiwan-indigenous.jpg`) — temática válida.
- **268245 Anthropic/Trump** (19:43, janela anterior) já tinha saído com retrato oficial do Trump.
- Também publicados na janela: 268259 sarampo SP (21:24), 268258 Desenrola (21:44).

**Estado da fila de capas:** restam SEM CAPA **268226** (Santa Cecília — candidata verificada já existe) e **268236** (Brasil no Mundo/guerra tarifária EUA-Canadá). A esteira noturna criou novos drafts sem capa: 268266, 268268, 268273. Ou seja: a publicação está andando (gate §86 operante no fluxo), o gargalo continua sendo suprir capa para os próximos.

**O que falta (aguarda "vai" do Miguel):** `media_human_review_cli` (Fase 2) para fechar o furo de revisão humana de identidade — agora ainda mais justificado, pois a esteira está publicando rápido; perna de volta GitHub→nyc (fetch + ff-only); decisão sobre rotação da chave Flickr (ver nota acima).


---

### Adendo 31/08 2026-08-31 11:20 BRT — ZM (sprint V4.1 Vision): guarda do DSN Imagem

O DSN Imagem (worker `dsn_imagem.py` nascido aqui na seção DEPLOY do dia 29→31/08) foi **fundido ao sprint V4.1 Vision por ordem do Miguel ~11:05** ("vamos fundir tudo nessa sessão aqui"). Dono a partir de agora: **ZM/ZCode-GLM-5.3 (sessão do sprint)** — detalhes e estado no fórum `forum_sprint_v41_vision_zm_20260831.md` (blocos -004 a -006). Este fórum segue sendo o histórico da missão de capas; a operação diária reporta lá.

— ZCode/GLM-5.3 · 2026-08-31 11:20 BRT

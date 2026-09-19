# Fórum — Artigo "Mais forte que em 2022": revisão editorial final (26/08/2026)

> Tema: revisão final pré-publicação do artigo analítico do Miguel sobre as pesquisas presidenciais de agosto de 2026. Continuidade de [[memoria_pesquisas_eleitorais_24_25_agosto_2026_20260825]] e [[memoria_analise_lula_2026_vs_2022_por_estado_20260826]] (memória pareada: `Memorias/memoria_artigo_mais_forte_que_em_2022_revisao_final_20260826.md`).

## Decisões resumidas

- **Título definitivo mantido:** `Mais forte que em 2022` — sem dois pontos, sem subtítulo. ✅
- **Régua estrita do Cafezinho:** 38/38 parágrafos do corpo com exatamente 2 frases (verificação mecânica por script, não por olho). ✅
- **Tom:** análise de dados, sem sermão nem ataques; premissa da urna mantida na abertura e no fechamento ("a única pesquisa real e decisória é a urna eletrônica"). ✅
- **Dados:** todos os números do artigo conferidos 1-a-1 contra `Outros/pautas editoriais o cafezinho/Dia a dia/2026 Ago 26/analise geral pesquisas/analise_lula_2026_vs_2022_completa_2026-08-26.csv` (38 linhas, 27 UFs + BR).

## Correções aplicadas nesta revisão (7 mudanças)

1. "18 dos 26 estados" → **"19 dos 27 estados pesquisados"** (CSV: 19 UFs com ΔN positivo, contando MG pela Datafolha — pesquisa principal).
2. "seis ampliações no N/NE" → **"sete"** (Rondônia +5,98 havia caído fora da contagem do texto de apoio).
3. Paraná: de "perda clara de participação" → **"único estado com piora clara de margem"** (RS perde 4,68 p.p. de participação de Lula, quase igual ao PR 4,87 — o que distingue o PR é a piora de MARGEM, única sem ressalva metodológica).
4. Santa Catarina: acrescentado **"em todo o Sul"** (a maior margem da oposição no país é do AC, −26,3; SC −25,0 só lidera no Sul).
5. Pará: removido "sondagens presenciais" (fonte não sustenta "presencial"; AtlasIntel é digital) → **"Outras sondagens no estado indicam disputa equilibrada, com Lula ainda 326 mil eleitores acima do primeiro turno de 2022"**.
6. Segundo turno: "evolui em doze das quinze" → **"melhora em onze das quinze medições e fica estável em outras duas"** (recontagem da lista do texto de apoio: 11 positivas, 2 estáveis — Nexus −0,4 e RS-RT −0,2 — e 2 pioras: GO e PA-Veritá).
7. Nexus nacional: "mantendo exatamente a distância" → **"praticamente a mesma distância"** (margem hoje +4,0 vs +3,95 em 2022 — "exatamente" era impreciso).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **O que aconteceu:** artigo revisado, dados validados contra o CSV, régua de 2 frases confirmada mecanicamente nos 38 parágrafos, título intacto. Arquivo pronto: `Outros/pautas editoriais o cafezinho/Dia a dia/2026 Ago 26/analise geral pesquisas/artigo_mais_forte_que_em_2022.md`.
- **O que falta:** publicação no portal (não foi pedida nesta revisão — só a revisão). Os 4 gráficos e a foto (Stuckert, Flickr oficial, 25/08) estão na mesma pasta com os nomes citados no markdown.
- **O que preciso de você:** seu OK final; se quiser, eu publico seguindo o fluxo sancionado do portal.

🕐 26/08/2026 · ZCode/GLM-5.3

---

## ADENDO 26/08 ~16:25 — VERSÃO 2 ENTREGUE (ordem Miguel: "melhora os gráficos todos + fact-checking de todos os números + reescreve o artigo todo")

**Ordem original:** primeiro o Miguel pensou em mandar o loop/Laura Claude revisar; decidiu fazer nesta sessão ("faz aqui por enquanto"). Escopo executado: revisão visual dos 4 gráficos, melhoria de todos, fact-checking completo, reescrita do artigo.

**Arquivos novos (v1 intacta):**
- `artigo_mais_forte_que_em_2022_v2.md` — reescrito integralmente; título exato mantido; régua 2 frases verificada por script: **31/31 parágrafos ✅**.
- `grafico1_v2_top_ganhos_margem.png`, `grafico2_v2_sangria_sudeste.png`, `grafico3_v2_ganho_eleitores_absolutos.png`, `grafico4_v2_enigma_minas_gerais.png` (+ script `gerar_graficos_analise_v2.py`).

**Melhorias dos gráficos (v1 → v2):**
1. **G2 Sudeste:** a legenda da v1 **escondia o rótulo de 39,7% do Bolsonaro no ES** — legenda movida para fora da área de plotagem; adicionadas anotações Δ por estado (ΔLula × ΔBolsonaro→Flávio, o "motor" da mudança).
2. **G1 margens:** barras agora **coloridas por região** (prova visual do "7 das 10 maiores no N/NE") + legenda própria; BR em amarelo como referência.
3. **G3 eleitores:** adicionado **asterisco metodológico no PA** (Veritá, voz automatizada) que faltava; "Rio Grande do Norte" por extenso.
4. **Todos:** formato pt-BR (vírgula decimal) nos rótulos; tipografia/eixos ajustados.

**Fact-checking:** script de conferência número-a-número do v2 × CSV de 38 linhas → **48/48 números conferem ✅** (nacional, CE/BA/SE/RN/MA/PE, SP/RJ/ES, PR/RS/SC, MG, PA, GO/RR, contagens 19/27 e 7/10, SC=maior do Sul). Único número não verificável no CSV: "mais de 43 mil entrevistados" (dado do briefing do editor — sem coluna de amostra na base).

**Estado:** v2 pronta para publicação. Aguarda OK do Miguel (publicação não foi pedida).

🕐 26/08/2026 16:25 · ZCode/DeepSeek

## ADENO 26/08 ~16:40 — RASTREIO DA ORIGEM (pedido Miguel "encontra a contribuição do Antigravity")

**Achado:** o RASCUNHO ORIGINAL do artigo foi feito pelo Miguel NO APP ANTIGRAVITY (conversa `d7fffa12-49d4-4b86-bb2e-17f06ef6d74e`, ~14:34→15:49). O "cérebro" do app guarda as provas: `artigo_mais_forte_que_em_2022.md` final às 14:50 + versões intermediárias (`.resolved.0` 14:41 → `.resolved.1` 14:44 → `.resolved.2/.resolved` 14:50) + os 4 gráficos v1 (14:39) + foto escolhida `foto_lula_flickr_jornalistica.jpg` (14:43) + 5 uploads de mídia do Miguel (14:34–15:48).
**Linha do tempo consolidada:** 14:31 ZCode entrega CSV+TXT na pauta → 14:34–14:50 Miguel redige no Antigravity (gráficos v1 + foto + draft com 3 revisões) → 15:0x–16:12 sessão GLM-5.3 aplica revisão editorial final (7 correções) → v1 na pauta (16:10) → 15:48–16:03 Miguel segue no Antigravity (nova conversa ee33fd0e) → 16:15–16:25 sessão DeepSeek reescreve (v2 + gráficos v2 + fact-check 48/48). **Nada publicado ainda** — publicação nunca foi pedida; aguarda OK do Miguel.
🕐 26/08/2026 16:40 · ZCode/DeepSeek

## ADENDO 26/08 ~17:10 — PUBLICADO + MANCHETE + COLUNA DO AUTOR (ordem Miguel)

- **Publicação:** post **267802** `https://www.ocafezinho.com/2026/08/26/mais-forte-que-em-2022/` — autor **2018 (james2017, Miguel do Rosário)** ✓ · cats Eleições 2026 (21186) + Política (22) · capa 267797 (Stuckert/Flickr, Emenda 12) · 4 gráficos v2 inline (267798-801) · recibo gate `ok:true` casado · página 200, og:image ✓.
- **Revisão Gemini 3.7 Flash (via API, chave do cofre):** 1 correção ("mega-pesquisa"→"megapesquisa"); sem mais erros.
- **Manchete humana (ordem Miguel ~16:58):** `wp_highlights` Manchete → 267802 (as 2 linhas duplicadas corrigidas) + trava 2h (até 19:00, padrão do plugin cmh) + lock p/ espelho + purge. Prova pública: `<h1 class="manchete-titulo">` na home = o artigo.
- **Coluna do Autor:** autor 2018 = bloco Coluna do Editor da home ✓ (2 menções do título na home).
- CF 403/1010 no POST JSON resolvido com UA navegador + Referer wp-admin (caso conhecido).
🕐 26/08/2026 17:10 · ZCode/DeepSeek

## ADENDO 26/08 ~17:30 — CORREÇÕES DO MIGUEL APLICADAS AO VIVO (dois-pontos + parágrafo)

- **Ordem Miguel:** reduzir dois-pontos (vício de IA) + corrigir parágrafo ambíguo ("Dividir o mapa... esconde") para sentido POSITIVO (somar pesquisas estaduais = mais entrevistados = melhor leitura do nacional).
- **Aplicado:** 9 trechos reescritos sem dois-pontos (régua 2 frases preservada em todos) + 2 títulos de seção + 5 legendas + 2 alts de imagem. Novo parágrafo: "Juntar as pesquisas estaduais em um único painel ajuda a compreender melhor o cenário nacional. A soma de todas as sondagens multiplica o número de entrevistados e forma uma amostra mais ampla do que qualquer instituto consegue oferecer sozinho."
- **Trajeto técnico:** REST deu 423 Locked (proteção editorial p/ post publicado por humano) → via sancionada SSH+WP-CLI com `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1` + purge Rocket/Redis. Prova pública: texto sem dois-pontos (0 no texto; só data:image/style do código) e parágrafo novo renderizado.
- Arquivo-fonte v2 da pauta sincronizado com o publicado.
🕐 26/08/2026 17:30 · ZCode/DeepSeek

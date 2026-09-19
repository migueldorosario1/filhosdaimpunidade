# Fórum — GA4 /v6/audiencia: correlação posts×audiência no gráfico de 40 dias — 13/09/2026

> Sprint ZCode/GLM-5.3 · pedido do Miguel 13/09 ~15:1x · fechado em 13/09 15:3x BRT

## O pedido (do Miguel, quase literal)

"Eu queria fazer correlação do número de posts por hora ou por dia. Nesse caso é por dia. Aí você nesse gráfico aí do GA4, você bota uma coluna um pouco transparente com o número de posts naquele dia, para relacionar com a audiência. Deixa esses dois indicadores num eixo só, a audiência e média móvel num eixo só da esquerda. No eixo da direita você bota número de posts, em coluna, uma coluna bem transparente para não ficar trepando. Bota só um rotulzinho em cima de cada coluna com o número de posts publicados naquele dia."

Página: `http://43.156.151.165/v6/audiencia` (📈 GA4, Tencent) — seção "Últimos 40 dias (fechados)".

## Decisões

1. **Eixo esquerdo UNIFICADO**: views diárias (linha azul fina) e MM7 (linha dourada grossa) passaram a compartilhar a MESMA escala (antes eram eixos separados: MM7 esquerda × views direita, cada um com máximo próprio). Escala = max(max(views), max(MM7)) × 1,12.
2. **Eixo direito = posts/dia**: colunas verdes (`#39d98a`, fill-opacity 0,16 — "bem transparente") desenhadas POR BAIXO das linhas; a maior coluna ocupa no máximo 50% da altura da área (escala 2× o máximo) para não invadir o território das linhas — "não trepindo".
3. **Rótulo em cima de CADA coluna** (font-size 10,5, verde, só quando posts > 0) com o nº de posts publicados naquele dia — pedido explícito do Miguel.
4. **Rótulos do eixo direito alinhados às colunas**: 2 valores redondos (máx e máx/2) nas alturas exatas de f=0,5 e f=0,25 da escala de posts — o rótulo 70 fica exatamente no topo da coluna de 70.
5. **Fonte de posts**: nova função `pub_contagem_diaria()` — REST WP autenticada (padrão `pub_serie_horaria`), paginada per_page=100 até esgotar, `_fields=id,date`, contagem por dia BRT via `_pub_dia_hora_brt`, só dias FECHADOS (hoje fora, igual à série GA4). Cache 1h (`pubs_dia_correlacao.json`).
6. Alinhamento de fuso conferido: série GA4 diária vem no fuso da propriedade (BRT) e a contagem WP é convertida para BRT — dias batem.

## O que foi feito (arquivo: `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, Tencent)

- `svg_linha_dupla(serie, posts_dia=None, janela=7)` reformulada para o novo desenho (compatível: sem `posts_dia` desenha só as linhas em escala única).
- Nova `pub_contagem_diaria(ndias=45)` ao lado de `pub_serie_horaria`.
- Seção da página reescrita: título "audiência + média móvel 7 dias (eixo esquerdo) × posts publicados por dia (colunas, eixo direito)" + linha explicativa + chamada com `posts_dia=pub_contagem_diaria()`.
- Backup pré-mudança: `painel_cctv_v6.py.bak_pre_correlacao_posts_20260913` (rollback = `cp` do .bak + restart).
- Cópias: edição local em `ZCodeProject/tencent_v6_audiencia/painel_cctv_v6.py` (md5 conferido com o servidor).

## Bug pego no caminho (corrigido na hora)

Primeira versão paginava só 8×100 posts — agosto tinha ~50 posts/dia e a varredura parou no dia 23/08 (cache incompleto, 21 dias). Corrigido para 30 páginas (break natural ao esgotar) + cache poluído apagado e regerado. Varredura cheia: 2.214 posts em 22s (23 páginas).

## Provas

- Interno `curl 127.0.0.1:8084/audiencia`: título novo 1×; **40 colunas** (todos os 40 dias fechados têm posts); rótulos de 15 a 70 posts/dia; eixo direito verde com 35 (f=0,25) e 70 (f=0,5).
- Público `http://43.156.151.165/v6/audiencia` (UA navegador): HTTP 200, 64.093 bytes, 40 colunas.
- Cache regerado íntegro: 47 dias (28/07→12/09), 2.205 posts fechados (os 9 de hoje 13/09 ficam fora por design; conferido contra varredura manual 2.214 = 2.205 + hoje).
- Screenshot auditado (visão) 5/5: colunas transparentes atrás das linhas; número em cima de cada coluna; azul fina + dourada grossa; eixos legíveis; sem colisão de texto. Recorte: `ZCodeProject/tencent_v6_audiencia/recorte_correlacao.png`.
- Página quente: 0-3s (o custo da varredura REST só existe 1×/h quando o cache vence).

## Leitura da correlação (o que o gráfico já mostra)

Agosto (era V4, 42-70 posts/dia) sustenta MM7 nos picos de ~10k/dia; setembro no plano mínimo (15-25/dia) com MM7 recuando — posts/dia e audiência caminham juntos na janela.

## Estado

- **O que aconteceu:** tudo pronto e no ar (13/09 15:3x BRT).
- **O que falta:** nada. Variações fáceis: cor/transparência das colunas (`fill-opacity`), altura máxima (fator 2× da escala), janela 40→N dias.
- **O que preciso do Miguel:** homologação visual (abrir a página); se quiser a mesma coluna no gráfico de 30 dias em barras ou em outra página, é reuso direto de `pub_contagem_diaria()`.

## Relacionados

- Memória técnica: `memorias_provisorias/memoria_audiencia_correlacao_posts_20260913.md`
- Nodos: `CEREBRO_NODE_OBSERVABILIDADE.md` (§ 13/09), `CEREBRO_NODE_ATUALIZACOES.md`
- Antecessor direto: `Foruns/forum_farol_grafico_40h_topo_20260903.md` (padrão GA4 do painel)

## Adendo v1.1 (13/09 ~15:5x) — linha MM7 dos posts (novo pedido do Miguel)

- "Acrescenta uma linha média, verde clarinho transparente, com a média móvel 7 dias do número de posts."
- Feito em `svg_linha_dupla`: polyline `#7fe0a8` stroke-width 2,2 stroke-opacity 0,55 sobre as colunas, na MESMA escala de posts do eixo direito. MM7 calculada por DATA REAL (média dos 7 dias terminando em cada data, usando os dias anteriores à janela que já vêm no dict de 47d) — a linha entra "cheia", sem rampa de média parcial nos 6 primeiros pontos.
- Legenda + parágrafo descritivo atualizados ("média móvel 7 dias dos posts").
- Ajuste fino: rótulo dourado da MM7 de views em i=0 sobe/desloca (+16,-22) para não encostar nos rótulos das colunas altas de agosto (apontado em auditoria visual da v1.1, corrigido na sequência).
- Provas: interno 200 (1 polyline verde 40 pontos, 40 colunas, legenda 2×) + público 200; MM7 posts 1º ponto ≈ 57,7/dia (05/08) e último ≈ 27/dia (12/09) — bate com a queda real agosto→setembro; screenshots `recorte_correlacao_v11.png` e `recorte_v11_final.png` auditados (final 3/3). Rede SSH intermitente durante o deploy (2 timeouts, resolveu com retry).
- Estado: no ar; nada pendente.


## Adendo v1.2 (13/09 ~18:1x) — ANÁLISE ESTATÍSTICA 6 MESES posts×audiência (só MM7, GA4)

Pedido: "análise dos últimos seis meses, correlação posts/dia × audiência diária, apenas médias móveis, dados GA4". Sem mudança no painel — só análise. Dados: 13/03→12/09 (184 dias fechados), views GA4 diários + 17.055 posts da REST WP (171 páginas; extração `tencent_v6_audiencia/extrai_6meses.py` + `analise_6meses.json` no ZCodeProject).

**Resultados** (178 pontos de MM7 cheia):
- **Níveis: r = +0,805 (r² = 64,8%, p ≈ 8×10⁻⁴²)** — forte. Melhor defasagem +2d (r=+0,817); decai p/ +0,38 em +14d. Regressão pooled: ~209 views/dia por post/dia extra (resíduo 56% — referência, não causal).
- **Sem tendência comum (ΔMM7): modesta e DEFASADA** — mesmo dia r=+0,14 (n.s.), +1d +0,25, +2d +0,31, +3d +0,34 (significativos). Publicar mais hoje move a audiência nos 2-3 dias seguintes (~12% da variação semanal); no dia, quase nada.
- **Por mês a relação oscila**: mar +0,71 · abr +0,69 · mai +0,24 · jun +0,94 · jul +0,64 · **ago −0,58** · set +0,91. Agosto: posts reaceleraram (Master/V4.1, picos 59-70/dia) com MM7 de views CAINDO do pico de julho — pauta/agenda > volume.
- **Leitura honesta**: a força em níveis vem em boa parte da queda COMUM das duas séries (era V4 ~150-240 posts/dia e 30-48k views/dia → hoje 8-36 e 5-11k). O sinal dia a dia real é pequeno e com resposta 2-3 dias.

Artefatos: `ZCodeProject/tencent_v6_audiencia/analise_6meses.png` (gráfico auditado 3/3) + `analise_6meses_nums.json`.


## Adendo v1.3 (13/09 ~18:2x) — BASE SEMANAL DEFASADA p/ gráfico (pedido do Miguel)

"Considera que a audiência cresce dias depois: média semanal de audiência × média semanal de postagens diárias da SEMANA ANTERIOR."

- Base: 24 semanas calendário fechadas (23/03→31/08; semana corrente parcial fora). Colunas: `semana_inicio` (da AUDIÊNCIA), `audiencia_media_diaria_views`, `posts_media_diaria_semana_ANTERIOR`. Artefatos: `ZCodeProject/tencent_v6_audiencia/correlacao_semanal.csv` + `correlacao_semanal.png` (gráfico 2 eixos: dourada audiência esquerda × verde produção N-1 direita).
- Correlação nesses pares: **r=+0,721 (r²=52%, p=7×10⁻⁵) · Spearman ρ=+0,742** — na janela semanal defasada a relação fica BEM mais forte que no ΔMM7 diário (+0,34): agregar a semana remove ruído e a defasagem de 1 semana casa bem com a resposta de 2-3 dias.
- Bug pego: dias SEM posts não existem no dict da REST (ausência ≠ zero) — semana era descartada à toa; corrigido (posts: `get(x,0)`; views: exige semana completa no GA4).
- Lição de leitura: produção da semana passada explica ~metade da variação da audiência desta semana; o resto é pauta/agenda (agosto seguiu sendo o contraexemplo).


## Adendo v1.4 (13/09 ~18:4x) — GRÁFICO SEMANAL DEFASADO NO PAINEL /v6/audiencia (ordem Miguel)

"Consegue botar esse gráfico no painel ga4 (audiencia) do cctv v6. Sempre com semanas fechadas."

- Nova seção logo abaixo da correlação diária de 40 dias: "📅 Semanas fechadas — audiência da semana × produção diária média da semana ANTERIOR" — dourada = audiência média diária da semana (eixo esquerdo), verde = posts/dia da semana N-1 (eixo direito), r de Pearson na mão (sem scipy) + r² + nº de semanas no canto; valores finais rotulados; só semanas COMPLETAS (seg→dom; corrente entra sozinha ao fechar).
- **Arquitetura anti-travamento**: varredura de posts de 190d (~171 págs REST, 2-3min) NÃO roda no request — cron `sync_pubs_190d.py` 4×/dia (23 */6, log em v6_data/logs_pubs190d.log, crontab .bak_pre_pubs190_20260913) grava `pubs_dia_190d.json`; página só LÊ (TTL leitura 26h, fail-open para o cache de 45d). Série GA4 de 184d tem cache próprio 30min (regenera em ~2-5s).
- `pub_contagem_diaria` parametrizada (ndias/cache_nome/ttl; teto de páginas = max(30, ndias) pelo pior caso ~100/dia).
- Provas: interno 5s/68.637B, seção 1×, "r = +0.72 (r² = 53%) · 25 semanas" (backfill GA4 trouxe 1 semana extra de março: 25 vs 24 da base local); público 200 c/ auth; 40dias/home/baleia intactos; screenshot auditado 3/3; carga manual: 192 dias/17.095 posts.
- Estado: no ar. A semana corrente entra automaticamente na 2ª-feira seguinte ao fechar (cron + TTL cuidam sozinhos).


## Adendo v1.5 (13/09 ~18:5x) — eixo esquerdo vira views/SEMANA (total), não média diária

Pedido do Miguel: "não, audiência média semanal, não audiência média diária. vai ficar melhor."
- `svg_semanal_defasada`: `m_v` agora é a SOMA dos 7 dias (audiência total da semana); rótulo final "67.956 views/semana" (última fechada); título/legenda/parágrajo reescritos ("views/semana"); posts/dia da semana N-1 inalterado.
- r NÃO muda (Pearson é invariante a multiplicação por constante): +0,72 · r² 53% · 25 semanas.
- Provas: teste local (última 80.718 na base de análise × 67.956 ao vivo = semanas diferentes, coerente), servidor título/legenda/valor 1×, screenshot auditado 5/5.


## Adendo v1.6 (13/09 ~19:0x) — versão FINAL: janela MÓVEL de 7 dias · últimas 8 semanas · média diária por dia

Iterações em sequência com o Miguel ("não é semana fechada, é últimos 7 dias" → "pega apenas as últimas 8 semanas" → "média da audiência semanal, por dia"):
- Cada DIA D do eixo X (56 dias fechados, últimas 8 semanas): dourada = MÉDIA DIÁRIA da audiência na janela móvel dos últimos 7 dias terminando em D (views/dia) × verde = posts/dia da janela de 7 dias imediatamente anterior (D-13..D-7). Semana-calendário abandonada.
- `svg_semanal_defasada(serie, posts_dia, n_dias=56)`: `v7 = sum(views[i-6:i+1])/7`; rótulo final "9.708 views/dia"; título/legenda "média diária na janela móvel de 7 dias".
- **r da janela visível cai para +0,18 (r² 3%)** — honesto e esperado: as 8 semanas misturam regimes da análise mensal (jul +0,64 · ago −0,58 · set +0,91 se cancelam). O r forte (+0,72) era do recorte de 6 meses. Fórmula confere: dourada = MM7 clássica (10.358 views/dia no teste local = np.mean dos últimos 7 dias; servidor 9.708 com GA4 mais consolidado).
- Provas: teste local fórmula+sanity; servidor título 1×, "r = +0.18 (r² = 3%) · 56 dias · janelas móveis", home 200; screenshot auditado 5/5.


## Adendo v1.7 (13/09 ~19:1x) — versão FINAL FINAL: defasagem de 1 DIA · últimos 30 dias

Pedido do Miguel, quase literal: "tem que terminar no dia de ontem, 12 de setembro. aí todo dia fez a média semanal dos últimos 7 dias e compara com a média semanal até o dia anterior (dia 11) e por aí vai. aí faz dos últimos 30 dias."
- Fórmula: para cada dia D (30 dias fechados): dourada = média diária de views na janela D-6..D × verde = média diária de posts na janela D-7..D-1 (defasagem de 1 dia — a produção de hoje ainda não virou audiência de hoje). Exemplo no próprio painel: dia 12/09 = audiência 06-12/09 × posts 05-11/09.
- Conferência independente: último par = 10.358 views/dia × 29,0 posts/dia = cálculo manual exato das janelas.
- **r da janela de 30 dias = −0,60/−0,66 (r² ~40%)** — NEGATIVO e forte no recorte: os últimos 30 dias contêm o agosto inteiro do r mensal −0,58 (posts reacelerando 15→29/dia com MM7 caindo do pico de julho). Consistente com a análise de 6 meses: a relação posts×audiência só é positiva forte no acumulado longo (r +0,72/+0,80); em agosto-setembro o motor foi pauta, não volume.
- Provas: interno título 1×, "r = -0.60 (r² = 36%) · 30 dias", rótulos "9.712 views/dia" + "27.1 posts/dia (7d até ontem)", home 200; screenshot auditado (título+exemplo do dia 12+r negativo, 40 dias intacto).


## Adendo v1.8 (14/09 ~23h BRT) — GRÁFICO DEFASADO replicado nos 3 MEDIDORES (FAROL/Lumina/Sol)

Pedido do Miguel: "esse gráfico aqui [FAROL] eu quero que você faça parecido com o que fez no ga4... mas é para fazer para o farol, a audiência redundante. aí faz também para o lumina e o sol a mesma coisa."

- Mesmo desenho do GA4 (janela móvel 7d × posts/dia até o dia anterior, defasagem 1 dia, últimos 30 dias) agora nas 4 páginas, cada uma com sua métrica e rótulo: **GA4** views/dia · **FAROL** navegações/dia · **LUMINA** visitas/dia · **SOL** visitas/dia.
- Séries diárias novas (cache 1h, fail-open stale): `serie_diaria_farol()` — último `hoje_navegacoes` de cada dia BRT do jsonl (conferência exata: 91.831 em 13/09 = jsonl); `serie_diaria_lumina()` — último `visitas_hoje_brt` por dia (dia derivado de `coletado_em`, que é BRT do servidor). SOL reusa `sol_dados()["dias30"]` (cache 5min).
- `svg_semanal_defasada` generalizada (param `unidade`; guard mínimo 12 dias p/ séries novas); `_exemplo_janela()` — exemplo com DATAS REAIS na página (o "12/09" fixo do GA4 virou dinâmico: "dia 13/09 = audiência 07-13/09 × posts 06-12/09").
- Histórico disponível: FAROL 21d (14 pontos, completa sozinho), LUMINA 19d (12 pontos), SOL 13d (7 pontos — guard baixado 15→12 dias p/ ligar já).
- **r por fonte na estreia**: FAROL −0,69 · LUMINA −0,27 · SOL +0,90 · GA4 −0,52 (30d reais) — todos coerentes com a análise (agosto negativo nos medidores com histórico; setembro positivo no SOL recém-nascido).
- Fusos ancorados no deploy: servidor é BRT (date sv = -03); FAROL `gerado` BRT (pusher Dell); LUMINA `coletado_em` BRT / `gerado_em` UTC. ⚠️ Sandbox do ZCode estava ~28h atrasado (dizia 13/09 19h quando o real era 14/09 23h) — rodapés anteriores desta sessão saíram com data do sandbox; registros corrigidos daqui em diante (caso análogo ao de 11/09).
- Provas: AST 3.12; 4 páginas 200 interno c/ seção+r; teste integrado local (conferência numérica exata FAROL); screenshots auditados FAROL 5/5, LUMINA 4/4, SOL 4/4. Backup `.bak_pre_medidores_20260914`.


## Adendo v1.9 (15/09 ~11:4x BRT) — AUDITORIA DOW FAROL (pedido do Miguel: "está sempre aumentando, não está acumulando?")

- **Veredito: NÃO acumulava** — cada barra era o fechamento do dia (último `hoje_visitantes_distintos` do jsonl; o campo reinicia à meia-noite — prova: oscila para baixo em 25/08 14.420 → 29/08 10.287 → 30/08 7.889, impossível em acumulador).
- **Causa da ilusão**: o dia de NASCIMENTO do FAROL (24/08, ligou 14:30) entrava como se fosse dia cheio — 4.681 visitantes em ~9h30 vs ~9-10k de um dia normal. Primeira barra lá embaixo + crescimento real de setembro (10k→16k) = rampa "sempre aumentando muito". Cruzamento GA4 nas mesmas datas (11,5k/11,4k/11,2k) confirma que a dobra era artefato.
- **Fix**: helper `_descartar_nascimento_parcial()` (primeiro registro do dia mais antigo com hora ≥ 02:00 = dia parcial → fora) aplicado às 3 séries: `_farol_serie_diaria` (DOW), `serie_diaria_farol` (defasado) e `serie_diaria_lumina` (nasceu 26/08 12:57, também parcial).
- Provas: local — série DOW começa 25/08, segundas = 31/08 (9.434) + 07/09 (14.176), 24/08 ausente; servidor — título 1×, "24/08" só em texto corrido, defasado 14 dias (virada do dia: hoje 15/09), screenshot auditado (2 barras, sem 24/08, valores 9,4k/14,2k). Backup do estado anterior já coberto pelo .bak_pre_medidores.


## Adendo v2.0 (15/09 ~12h BRT) — AUDITORIA DO GRÁFICO DEFASADO FAROL («caiu posts, subiram navegações, está correto?»)

- **Aritmética: CORRETA** — recriada independente (última 93.008 × 39,6 em 13/09 = igual ao painel); janelas, defasagem de 1 dia e r conferidos.
- **Mas a subida das navegações tem ARTEFATO**: `hoje_navegacoes` QUEBROU a série em 09/09 — 67.438 (08/09) → 104.221 (09/09) = 3,9 → 6,7 navegações/visitante da noite pro dia, sem nada em visitantes/humanos/bots e sem salto no GA4. Na mesma manhã 09/09 ~09h05 a cadência do pusher mudou (registros de 30min passaram a 5min por horas) — coletor foi mexido. A razão segue ~6,3 depois.
- **E também tem VERDADE**: com HUMANOS distintos (métrica limpa) o r é −0,71 — audiência real de setembro subiu (9k→17k ago→set) enquanto posts caíam (50-70/dia→15-30/dia): de novo a lição da análise longa (pauta > volume; setembro não dependeu do ritmo).
- **Fix aplicado**: gráfico defasado do FAROL passou de navegações → **HUMANOS distintos/dia** (decisão "SO HUMANOS" do Miguel 25/08 aplicada à nova peça) + nota na própria página explicando a quebra das navegações. No ar: 16.814 humanos/dia, r=−0,61 (13 pares; série 25/08→14/09).


## Adendo v2.1 (15/09 ~12:1x BRT) — AUDITORIA GRÁFICO DEFASADO LUMINA («menos posts e mais visitações»)

- **Sem artefato no Lumina** — ao contrário do FAROL (v2.0): série `visitas_hoje_brt` é limpa. Provas: crescimento suave 1.002 (26/08) → ~2.900 (14/09) sem salto dia-a-dia; razão visitas/visitantes estável (1,13 → 1,35, sem degrau — a quebra do FAROL era 3,9→6,7 num dia); padrão de fim de semana presente (29-30/08 e 05-06/09 caem — assinatura de audiência real).
- Aritmética do gráfico revalidada (mesmo motor do FAROL, já provado). Recálculo independente série cheia (12 pares, 03-14/09): **r = −0,73**; visitas 7d +31% (2.101→2.747/dia) enquanto posts da janela anterior −23% (52→40/dia).
- **Conclusão**: no Lumina o fenômeno é REAL — a audiência de setembro cresceu por pauta (top páginas do próprio FAROL em 14/09: home + matérias Master/eleições de 12-14/09) com a casa publicando menos. Consolidação dos 3 medidores limpos no período recente: GA4 −0,52 · FAROL(humanos) −0,61 · LUMINA −0,73 — todos negativos no curto prazo, vs +0,72 da base semanal de 6 meses: volume importa no acumulado, pauta domina no curto.
- Nenhuma mudança de código (métrica e cálculo corretos).


## Adendo v2.2 (15/09 ~12:2x BRT) — POR QUE no GA4 o paradoxo não aparece (pergunta do Miguel)

Janela 7d | GA4 views | FAROL humanos | Lumina visitas | views-GA4 por humano:
01/09: 11.083 | 10.956 | — | **1,01**
05/09: 11.800 | 10.832 | 2.246 | **1,09**
09/09: 11.665 | 13.914 | 2.523 | **0,84**
13/09: 9.704 | 16.417 | 2.683 | **0,59**

- **É a métrica, não o fenômeno**: o gráfico GA4 mede PAGEVIEWS (tag executada no browser); FAROL mede HUMANOS nos logs do servidor; Lumina mede VISITAS do motor próprio. O crescimento de setembro foi de GENTE, não de páginas por gente: cada humano rende ao GA4 0,59 view vs 1,01 no início — visitante novo mais RASO (push/social/Discover: lê 1 matéria e sai) e/ou mais protegido (adblock/anti-tracking: aparece nos logs do servidor — FAROL — mas a tag do GA4 nunca roda).
- **GA4 ainda em atraso**: processamento Google stallado desde 10/09 (registro da casa, backfill 24-72h) — os dias 10-13/09 podem estar subestimados; a curva do GA4 pode subir sozinha no backfill.
- No GA4 as duas linhas CAEM juntas (posts 52→40 × views 11,8k→9,7k) — visual "normal", sem o paradoxo dos outros medidores. Nenhuma mudança de código: cada gráfico mede sua métrica e o porquê está documentado aqui.


## Adendo v2.3 (15/09 ~12:3x BRT) — MM7 no gráfico de BARRAS "Últimos 30 dias fechados (diário)"

Pedido: "bota aqui nesse gráfico uma linha com média móvel diária nos últimos 7 dias".
- `svg_barras` ganhou polyline MM7 (#f2f6fa branca, 2.6px — dourada não: as barras dos últimos 7 dias JÁ são douradas e a linha sumiria sobre elas) + bolinha e rótulo final "9.9k/dia" + item na legenda.
- MM7 calculada sobre a série COMPLETA (92d no GA4) → linha entra CHEIA desde a 1ª barra (offset ≥ 6); em séries curtas (Sol, 13d) desenha só a partir da 7ª barra (sem média parcial — teste 7 pontos).
- Efeito colateral bom: a mesma função serve ao Sol → MM7 branca lá também, de graça. Provas: GA4 1× MM7 + rótulo 9.9k/dia; Sol 1×; regressão 200; screenshot auditado (linha legível sobre azul e dourado).


## Adendo v2.4 (16/09 ~16h BRT) — /v6/audiencia: 72h sem estouro + página reordenada + auditoria 40 dias (pedido Miguel com print)

- **72h estourado → corrigido**: o gráfico de linha (refeito por outra sessão em 14/09) usava o máximo exato como topo da escala — pico encostava na borda e os rótulos de valor em `Y-12` cortavam/colidiam com o cabeçalho ("máx 521/h…"). Fix: escala com 18% de headroom (`mx_esc = mx*1.18`) + rótulo do pico desenha ABAIXO da linha quando subiria demais (y<34 → y=XY+20). Homologado por screenshot (picos com folga, rótulos legíveis).
- **Página reordenada** (ordem Miguel): TODOS os gráficos no topo (72h → comparativos → 30d barras → dia-da-semana → 40 dias → janela móvel defasada) → Top 20 → **as duas listas de posts (7d e 30d) no FINAL**.
- **Auditoria do 40 dias ("não devia estar contando?")**: contagem EXATA — 10/10 dias batem com o WP ao vivo (varredura independente autenticada; 05-15/09: 31 25 33 25 32 29 15 10 28 23). O gráfico mostra o que o site publicou; sem contagem errada.
- **Bug pego e mitigado**: cron `sync_pubs_190d` falhando com HTTP 500 intermitente do WP na varredura de 171 páginas (06:25 e 12:25 de 16/09) — fallback stale segurava. Fix: retry 3× com backoff 20s por página no `pub_contagem_diaria`; carga manual pós-fix renovou o cache (17.098 posts).
- Backup `.bak_pre_72h_fix_20260916`; regressão home/baleia 200.


## Adendo v2.5 (16/09 ~16:1x BRT) — rótulos do 72h legíveis (LUMINA + GA4)

Pedido: "tem um rótulozinho branco que não está claro se é visitas/h ou MM8h… tinha que ser letrinha azul ou amarela… e afasta o número do gráfico".
- `_ga4_svg_linha_72h`: rótulos de início/fim da linha azul agora em **azul claro #8fc4ff com sufixo "/h"** (amarram à linha própria; a MM8h amarela continua só no cabeçalho "MM8h agora X") e mais afastados da curva (offset 12→17px acima; pico alto rotula abaixo com +23px).
- Mesma função serve GA4 e LUMINA → correção nas duas páginas (prova: 555/734 no Lumina, 341/516 no GA4, 0 brancos velhos). Screenshot auditado 5/5. Confirmado ao Miguel: MM8h = média móvel de 8 horas.


## Adendo v2.6 (16/09 ~16:3x BRT) — rótulos GRANDES e TRANSPARENTES, início/meio/fim, em TODOS os gráficos com rótulo

Pedido: "bota o rótulo no início, no meio e no final… aumenta a letra e bota transparente para não atrapalhar o que está por trás. Faz isso em todos os gráficos que tiver rótulo. Grande, bem grande e bem transparente."
- Padrão novo (17px, fill-opacity 0.55, início/meio/fim) aplicado a: `svg_semanal_defasada` (3 na dourada + 3 na verde "Np/d"), `svg_linha_dupla` (MM7 dourada 3× + colunas de posts 13px/0.55), `svg_linha` (MM7 3×), `svg_barras` (MM7 branca 3×), `_ga4_svg_linha_72h` (azul "/h" ganhou o MEIO; 3×), `svg_mesmo_dow` (barras +2px e opacity 0.6, mantendo halo).
- Sufixo "/dia" mantido apenas no rótulo final; verde do defasado usa "Np/d" (curto, legenda embaixo explica).
- Provas: testes locais 3(+/3) rótulos por série em semanal/linha/barras; servidor: GA4 28 rótulos no novo padrão, Lumina 12, Sol 12, FAROL 10; regressão 200; screenshots auditados (defasado 3+3 sem colisão com o r).
- Backup `.bak_pre_rotulos_20260916`.


## Adendo v2.7 (16/09 ~18:2x BRT) — REGRA 1: rótulo segue o lado da linha + MANUAL DE GRAFICOS no Cérebro

Pedido (lição do Miguel): "Quando a linha está embaixo, o rótulo fica embaixo, para não trepar com o de cima. Quando está em cima, fica em cima… o Cérebro tem que ter um manual de gráficos."
- **`Estilo/MANUAL_DE_GRAFICOS_V1.md` criado** (7 regras consolidadas da casa; catalogado no NODO OBSERVABILIDADE + ATUALIZACOES).
- `svg_semanal_defasada`: rótulos por PONTO com decisão de lado (Y dourada vs Y verde → quem está em cima rotula acima, quem está embaixo rotula abaixo, +clamp nos limites). Teste anti-colisão com linhas cruzando: 3/3 pontos com pares de rótulos ≥17px de distância vertical.
- `svg_linha_dupla` (40d): MM dourada rotula ABAIXO quando mergulha sob a linha azul (mesma regra).
- Screenshot auditado 4/4: dourados acima, verdes abaixo, início separado, nada trepado.


## Adendo v2.8 (16/09 ~18:3x BRT) — MÉDIA DO PERÍODO no gráfico de barras 30d

Pedido: "bota uma média nesse gráfico" (o de barras diárias, que já tem a MM7 branca ondulada).
- `svg_barras`: linha VERDE TRACEJADA horizontal na média simples dos dias plotados (referência fixa, mesma linguagem do DOW) + rótulo "média 10.2k/dia" com desvio automático de colisão (se encostar no rótulo da MM7 ou no topo, desenha abaixo) + item na legenda.
- Sol herdou (mesma função). Provas: HTML 2 linhas tracejadas (DOW também usa o padrão), rótulo 10.2k/dia, legenda 1×; screenshot auditado 4/4.


## Adendo v2.9 (17/09 ~09:2x BRT) — rótulo da média do período vai para o INÍCIO do gráfico

Pedido: "bota o rótulo da média da linha tracejada no início do gráfico. onde está agora está trepando em cima" (Sol: média 1.8k ≈ MM7 1.8k → colidiam na direita).
- `svg_barras`: rótulo "média X/dia" agora no canto ESQUERDO (`pl+6`, anchor start), acima da linha; desvio automático se encostar no rótulo INICIAL da MM7 ou no topo (vai para baixo); clamp do fundo. MM7 branca segue com o valor final na direita — lados opostos, sem trepar.
- GA4 e Sol atualizados (mesma função). Screenshot Sol auditado 3/3. Regra anotada no MANUAL_DE_GRAFICOS (rótulos de referência fixa preferem o canto oposto ao rótulo da série).


## Adendo v2.10 (17/09 ~09:5x BRT) — USUÁRIOS na página GA4: gráfico 72h + comparativos

Pedido: "depois do primeiro gráfico de views, um gráfico só com usuários, últimas 72h, usuários por hora e MM8h. Nos comparativos: usuários 7d/30d com variação semana/mês anterior, MM7 ontem fechado, MM7 vs semana e vs 30d."
- `ga4_serie_horaria`/`ga4_serie_diaria` parametrizadas por métrica (`totalUsers` para usuários; caches com sufixo próprio `..._totalUsers.json` — os de views mantêm o nome antigo, cache quente preservado).
- Novo card "⏱️ GA4 — usuários por hora — últimas 72 horas" logo após o de views (mesma linguagem: linha azul + MM8h amarela + 3 rótulos azuis '/h').
- Comparativos ganham bloco "👥 Usuários (distintos)" com 7 cards: usuários 7d (50.510) · vs semana anterior · usuários 30d · vs mês anterior · MM7 ontem (7.216, fechada) · MM7 vs semana · MM7 vs 30d — mesmo recorte de fechamento do bloco de views (72h atrás).
- Coerência provada: 7.216×7 ≈ 50,5k (MM7 × 7 ≈ total 7d). Rótulos /h: usuários 140-309/h vs views 156-464/h (usuários ≤ views ✓). Screenshot auditado 2×.
- Backup `.bak_pre_usuarios_20260917`.


## Adendo v3.0 (19/09 ~02:1x BRT) — INCIDENTE: painel regredido por sobreposição de sessão + RECUPERAÇÃO completa + 3 pedidos do Sol

**Incidente**: em algum ponto entre 17/09 ~10h e 19/09 01:3x, o `painel_cctv_v6.py` do servidor foi sobrescrito por uma versão de ramo antigo (sumiram: gráfico 72h, usuários GA4, contador Moka, página saúde, média do período, rótulos grandes/regra 1 — tudo deployado e provado). Detectado pelo pedido do Miguel no Sol: as provas não batiam com o código. Causa provável: outra sessão subiu um arquivo próprio (os meus `.bak` também sumiram do servidor — a restauração não foi in-place). Registrado em BUGS_ATIVOS como incidente de processo.

**Recuperação** (aditiva, nada de outras sessões perdido): base = `.bak_pre_usuarios_20260917` (último estado completo provado, com 72h/Moka/saúde/tudo até v2.9) + `_baleia_dados_pack` do regredido (trabalho alheio de 18/09, DSN celular — preservado com o endpoint `/api/baleia-dados`) + reaplicados: usuários GA4 (v2.10), Home FAROL (v2.11), Sol fechados (19/09). Erros no caminho: injeção com linha órfã (SyntaxError, pega pelo boot-fail e corrigida) — provas finais 100% em 6 rotas.

**Pedidos do Miguel desta passada (todos no ar)**:
1. Sol: títulos dos gráficos com o NÚMERO real de dias ("últimos 18 dias fechados" — dinâmico).
2. Sol: bloco novo "📊 Variação (dias fechados)" depois dos gráficos iniciais — MM7 ontem, vs semana anterior, vs 30 dias atrás ("—" enquanto <30d de histórico), último dia fechado vs média dos 7 anteriores.
3. Sol (e todos que usam barras): rótulos GRANDES/transparentes com o NÚMERO da barra no início/meio/fim, sempre acima da barra.

Provas: bateria 6 rotas verde (Home FAROL sem GA4 residual; GA4 usuários+72h+média; Sol completo; FAROL/Lumina defasado; Baleia 200 + /api/baleia-dados ok) + screenshot Sol auditado 5/5. Backups: `.bak_pre_recuperacao_20260919` (do regredido) + bak_pre_usuarios_20260917 (a fonte).

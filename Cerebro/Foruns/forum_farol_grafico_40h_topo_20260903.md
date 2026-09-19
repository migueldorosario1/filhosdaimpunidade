# Fórum — FAROL: gráfico de 40 horas no topo (padrão GA4) — 03/09/2026

> Sprint ZCode/GLM-5.3 · pedido do Miguel 03/09 ~09:4x · fecha em 03/09 09:51 BRT

## O pedido (do Miguel, quase literal)

"Você pode me dar um gráfico das últimas 40 horas em vez de 3 horas? Vou botar ele lá em cima, logo depois do online, para ficar parecido com o G4 [GA4], com a página do GA4. Últimas 40 horas em vez de 3 horas."

Página: `http://43.156.151.165/v6/audiencia-redundante` (🛡️ FAROL, Tencent).

## Decisões

1. **Janela 3h → 40h** no gráfico de leituras de 5 em 5 min (481 amostras = 40h completas). Histórico do jsonl é perpétuo (2.828 leituras desde 24/08) — sobra dados.
2. **Gráfico subiu para logo depois do card "ONLINE AGORA"**, espelhando o layout da página GA4 (`/v6/audiencia` tem ONLINE AGORA → gráfico de 40h).
3. **Rótulos do eixo X adaptativos** (padrão da casa do GA4): janelas ≤3h mantêm rótulo a cada 30 min (`%Hh%M`); >3h usam hora cheia múltipliplo de 4 no formato `dd/mm Hh` (10 rótulos em 40h, sem sobreposição).
4. **Série dedicada** `_audiencia_red_series(481)` para o gráfico — `n_reg` ("leituras guardadas") e as demais leituras da página seguem na série de 300, intocados.
5. Gráfico antigo de 3h **removido** da posição de baixo (sem duplicidade).

## O que foi feito (arquivo: `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, Tencent)

- Função `_farol_svg_3h` → **`_farol_svg_ultimas(amostras, janela_h=3)`** (generalizada; comportamento de 3h preservado por padrão).
- `pagina_audiencia_red`: monta `ult40h`/`vals40h`/`grafico_40h`; bloco `<h3>⏱️ Últimas 40 horas — leituras de 5 em 5 min</h3> + {grafico_40h} + linha Máx/Agora` inserido logo após `{card_online}` (comentário HTML `grafico_40h_topo_20260903`).
- Backup pré-mudança: `painel_cctv_v6.py.bak_pre_40h_topo_20260903` (mesma pasta).
- Deploy: `py_compile` OK no Python 3.12 do servidor + `systemctl restart cctv-v6` (serviço ativo).

## Provas

- HTML servido (`curl localhost:8084/audiencia-redundante`): ordem correta `ONLINE AGORA < título 40h < SVG < parágrafo < gráfico 48h < posts`; título antigo "Últimas 3 horas" não existe mais; rótulos `01/09 20h … 03/09 08h`; linha `Máx 1146 · Agora ~341 · Página atualiza a cada 60s`.
- Screenshot auditado (visão): card ONLINE no topo, gráfico 40h logo abaixo, 10 rótulos de eixo X legíveis sem sobreposição, eixo Y limpo, nada trespassado, curva cobrindo 2 ciclos dia/noite (01/09 17:45 → 03/09 09:45).

## Estado

- **O que aconteceu:** tudo pronto e no ar (03/09 09:46 BRT).
- **O que falta:** nada. Se o Miguel quiser outra janela (ex.: 24h ou 72h), é só trocar o parâmetro `40` e o nº de amostras (`janela*12+1`) na `pagina_audiencia_red`.
- **O que preciso do Miguel:** nada.

## Relacionados

- Memória técnica: `memorias_provisorias/memoria_farol_grafico_40h_topo_20260903.md`
- Nodos: `CEREBRO_NODE_OBSERVABILIDADE.md` (§ entrada 03/09), `CEREBRO_NODE_ATUALIZACOES.md`
- Antecessor: § do FAROL em 24/08 neste mesmo nodo; página GA4 com gráfico 40h desde 02/09 (`ga4_online_40h_20260902`).

## Adendo 1 — MM8h no gráfico de 40h (ordem Miguel 03/09 ~09:5x "ficou ótimo", 2º pedido)

- Pedido: "acrescenta mais uma coisa nesse gráfico das 40 horas que é uma média móvel de 8 horas… mas bota uma linha com a média móvel 8 horas".
- Feito (10:0x BRT): linha **amarela tracejada** (`#e0c040`, dash 8 5) de **MM8h por janela de tempo [t−8h, t], min 6 pontos** — mesmo critério do gráfico de 48h da casa; plot continua sendo a curva crua verde de 5 em 5 min.
- Aquecimento: série ampliada de 481 → **577 amostras** (8h extras) para a MM nascer válida no 1º ponto das 40h.
- Título do h3 agora indica a linha; rodapé do gráfico agora mostra `Máx · Agora · MM8h` (ex.: Máx 1146 · Agora 341 · MM8h 393).
- Legenda no SVG com 2 itens (bolinha verde = leituras; traço amarelo = MM8h).
- Backup: `painel_cctv_v6.py.bak_pre_mm8h_20260903`. Provas: teste isolado (480 pts na MM, 480 na curva, janela exata 40,0h) + curl (`MM8h 393`, polyline `#e0c040`) + screenshot auditado (linha visível, legenda limpa, nada trespassado).
- Estado: PRONTO E NO AR (03/09 ~10:05 BRT). Nada pendente.

## Adendo 2 — LUMINA `/v6/lumina`: primeiro gráfico vira 40h só-pageviews com eixo Y e MM8h (ordem Miguel 03/09 ~12:0x)

- Pedido: "página visitas por hora últimas 24 horas... colocar também últimas 40 horas... deixa só o pg views, tira visita e visitas... está faltando os rótulos de quantidade no eixo Y... e uma linha com média móvel de 8 horas no Lumina".
- Feito (12:0x→12:2x BRT) em `_umami_svg_24h` → **`_umami_svg_40h(pv)`** (mesma função reescrita):
  - janela 24h → **40h** (API do Umami passa a trazer 48h = 40 de janela + 8 de aquecimento p/ a MM8h);
  - **só pageviews** — barras amarelas de visitas/sessions removidas do gráfico (cards do dia seguem com pessoas/visitas/tempo);
  - **eixo Y com rótulos de quantidade** (passo "nice": 0/200/400/600 no teste real; antes não dava pra saber quanto era cada barra);
  - **linha amarela tracejada MM8h** (#e0c040, mesma linguagem do FAROL) sobre a série horária;
  - rótulos X em hora cheia múltipla de 4 + data na virada do dia; cabeçalho `máx N/h · 40h X pageviews · MM8h agora Y/h`.
- Backup: `painel_cctv_v6.py.bak_pre_lumina40h_20260903`. Provas: teste isolado c/ API real (49 buckets → 40 barras, 0 barras de visitas, MM8h 480/h) + curl + screenshot auditado (eixo Y legível, nada trespassado).
- Estado: PRONTO E NO AR (03/09 ~12:25 BRT). Nada pendente.


---

## ADENDO 2 — 08/09 22:59 BRT — gráfico dia da semana: colunas transparentes + rótulos + média na frente (ZCode Qwen3.8-Max, ordem Miguel 08/09 ~22:4x)

Ordem do Miguel (08/09 ~22:4x): no gráfico «Comparação por dia da semana» o rótulo «média» da linha tracejada ficava ATRÁS da coluna (a coluna dourada, mais recente, na borda direita, o cobria). Pedido: (a) rótulo da média em outro lugar / vindo pra frente, por cima da coluna; (b) colunas transparentes; (c) rótulo em cada coluna com quanto efetivamente houve naquele dia da semana.

Causa raiz: em `svg_mesmo_dow()` o `<text>` da média era acrescentado ANTES dos `<rect>` das barras — em SVG o que é desenhado depois cobre o que foi desenhado antes → a última coluna escondia o rótulo.

Cura (Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, svc cctv-v6; backup `painel_cctv_v6.py.bak_pre_rotulos_dow_20260908`; marca `graficos_dow_rotulos_frente_20260908`):
1. Barras com `fill-opacity="0.55"` (transparentes — a linha tracejada aparece através delas).
2. Rótulo do total EM CIMA de cada barra, desenhado depois das barras: número cheio quando há espaço (bw≥100, ex. «14.176»), senão formato k («11.8k»); mais recente dourado negrito #ffd75e, demais #bcd9f2; halo escuro (`paint-order="stroke"` #0a0f1a) p/ legibilidade.
3. Linha tracejada + rótulo «média X» desenhados POR ÚLTIMO (sempre à frente), com halo; se o topo da última barra estiver perto da linha (|Δy| < fonte+8) o rótulo vira p/ baixo da linha, evitando choque com o número da barra.

Função compartilhada → vale nas 3 páginas que a usam: FAROL (`/v6/audiencia-redundante`), GA4 (`/v6/audiencia`) e LUMINA (`/v6/lumina`).

Provas: curl + screenshots Chrome headless — FAROL 3 barras (4.681 / 9.434 / 14.176 + «média 9.430» legível sobre a coluna dourada); GA4 14 barras com rótulos k; LUMINA 2 barras com números cheios. QA visual aprovado nos 3 casos.

O que aconteceu / o que falta / o que preciso de você (Miguel): correção NO AR e verificada nas 3 páginas; nada falta do lado do agente; só conferir visualmente quando abrir o painel.

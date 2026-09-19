# Memória — FAROL gráfico 40h no topo — log técnico (03/09/2026, ZCode/GLM-5.3)

Sprint: pedido Miguel 03/09 ~09:4x → fechado 09:51 BRT. Fórum: `Foruns/forum_farol_grafico_40h_topo_20260903.md`.

## Ambiente e arquivos

- Servidor: Tencent `root@43.156.151.165`. Painel: serviço `cctv-v6` (porta 8084, usuário ubuntu), arquivo `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (~7.455 linhas).
- Dados: jsonl perpétuo `Projeto Cafezinho Agentes/root/agent_data/cctv/v6/audiencia_red.jsonl` (2.828 leituras desde 24/08, 1 leitura/5 min). Leitor: `_audiencia_red_series(n=300)` lê as últimas n linhas.
- Página externa `http://43.156.151.165/v6/audiencia-redundante` → nginx injeta prefixo; INTERNAMENTE no 8084 a rota é `/audiencia-redundante` (SEM `/v6`).

## Mudanças no código

1. `_farol_svg_3h(amostras)` renomeada/generalizada → `_farol_svg_ultimas(amostras, janela_h=3)`:
   - eixo X: `janela_h > 3` → primeiro tick em hora cheia múltipla de 4 (`while t.hour % 4: t += 30min` a partir de `t_ini.replace(minute=0)`), passo 4h, formato `%d/%m %Hh`; senão comportamento antigo (30 min, `%Hh%M`).
   - aria-label e mensagem "aguardando leituras" dinâmicos.
2. `pagina_audiencia_red` (~linha 2754): `ult40h = _audiencia_red_series(481)`; `grafico_40h = _farol_svg_ultimas(ult40h, 40)`; série principal (`serie` 300) intocada — `n_reg`, `linhas_recentes`, `ultimo` seguem iguais.
3. HTML: bloco 40h inserido entre `{card_online}` e o parágrafo "Cafézinho (canônico)…"; bloco antigo das 3h (ficava depois do gráfico de posts) removido. Comentário marcador: `<!-- grafico_40h_topo_20260903 ... -->`.

## Deploy (receita)

```bash
# backup + substituição preservando perms (cat > arquivo, não cp)
cd /home/ubuntu/cafezinho/v6
cp painel_cctv_v6.py painel_cctv_v6.py.bak_pre_40h_topo_20260903
cat /root/painel_cctv_v6_novo.py > painel_cctv_v6.py
python3 -m py_compile painel_cctv_v6.py && systemctl restart cctv-v6
# prova: curl -s http://localhost:8084/audiencia-redundante | grep -c "Últimas 40 horas"
```

## Armadilhas pegas nesta corrida (valores para o futuro)

1. **Rota interna sem prefixo:** `curl localhost:8084/v6/audiencia-redundante` = 404 do próprio painel ("rota nao encontrada", 26 bytes). A rota interna é `/audiencia-redundante`; o `/v6` é do nginx externo.
2. **py_compile local NÃO serve:** o Dell roda Python 3.10 e o painel usa f-string com backslash (PEP 701, linha ~4118) — só compila no 3.12 do Tencent. Validar sintaxe SEMPRE no servidor (`SyntaxWarning` de `\w` na linha 6882 é pré-existente e inofensivo).
3. **scp para /tmp do Tencent deu Permission denied** mesmo como root (sticky bit + arquivo pré-existente de outro dono) — usar `/root/`.
4. **Teste isolado de função antes do deploy:** extrair o trecho com `re.search(r'(def _farol_svg_ultimas.*?)(?=\ndef _lumina_resumo)', src, re.S)` + `exec` num namespace com `datetime/timedelta` e alimentar com as últimas 481 linhas do jsonl — valida o SVG sem reiniciar serviço.
5. Screenshot da página inteira não mostra o gráfico (card ONLINE é alto): rolar via `evaluate` com `scrollIntoView` no `<h3>` alvo antes de capturar.

## Provas finais

- Ordem no HTML servido: `ONLINE AGORA @8539 < título40h @10427 < svg @10631 < parágrafo @24703 < aud48 @26051 < posts @41390`; "Últimas 3 horas" = -1 (sumiu).
- Rótulos servidos: `['01/09 20h','02/09 00h','02/09 04h','02/09 08h','02/09 12h','02/09 16h','02/09 20h','03/09 00h','03/09 04h','03/09 08h']`.
- Auditoria visual do screenshot: aprovada (rótulos legíveis, nada trespassado, 40h reais com ciclos dia/noite).
- Máx 40h = 1.146 visitantes (02/09 à noite); leitura corrente ~341.

## Estado

PRONTO E NO AR. Nada pendente. Ajuste de janela futura = trocar `40`/`481` em `pagina_audiencia_red` (fórmula: `janela_h * 12 + 1` amostras).

## Adendo 1 — MM8h (03/09 ~10:05)

- `_farol_svg_ultimas`: `plot = pts[-janela_h*12:]`; MM8h por **tempo** (two-pointer `esq` monotônico sobre `pts`, `alfa = t-8h`, min 6 pontos), desenhada como polyline `#e0c040` `stroke-dasharray="8 5"` depois da curva verde; legenda com `<line>` amarela + texto.
- Chamada na página: `_audiencia_red_series(577)` (481 plot + 96 aquecimento); `mm8h_ult = round(sum(vals40h[-96:])/96)`; rodapé `Máx · Agora · MM8h`.
- Backup `bak_pre_mm8h_20260903`; restart cctv-v6 OK.
- Armadilha de teste: regex que casa `points="..."` imediatamente seguido de `stroke="#e0c040"` falha (há `fill="none"` no meio) — procurar a polyline pelo atributo de cor separadamente.
- IAB: screenshot com `clip` falhou 3× seguidas ("capture failed for guest") após reload; **sem clip funciona** — se o recorte falhar, capturar a viewport inteira.

## Adendo 2 — LUMINA 40h (03/09 12:0x→12:25)

- `_umami_svg_24h(pv, sess)` → `_umami_svg_40h(pv)`: só pageviews; eixo Y c/ `_passo_nice` (mlt 1/2/5/10, sem 2.5 p/ ticks inteiros) e margem esquerda ml=46; MM8h = média das 8 horas anteriores por bucket horário (aquecimento vem da própria chamada de 48h da API — `idx0 = horas_all.index(horas[0])`); rótulo X a cada hora múltipla de 4.
- Chamada na `pagina_lumina`: `timedelta(hours=48)` na API + `_umami_svg_40h(pageviews)`; h3 atualizado.
- Valores reais de validação: máx 683/h, 40h = 19.111 pageviews, MM8h 480/h, eixo Y 0-600 passo 200.
- Backup `bak_pre_lumina40h_20260903`; restart cctv-v6 OK.
- Armadilha de teste: `_umami_api`/`_umami_token` dependem de globais (`_UMAMI_CFG_PATH`, `_umami_token_cache`) — para teste isolado, extrair o bloco `def _umami_cfg` até `def _umami_serie_diaria` INTEIRO e injetar as 2 globais no namespace.


## ADENDO 08/09 22:59 — rótulos do gráfico «Comparação por dia da semana» (ordem Miguel 08/09 ~22:4x)
Problema: rótulo «média X» da linha tracejada desenhado ANTES dos <rect> → coluna dourada (última, borda direita) o cobria (SVG: quem desenha depois fica na frente). Cura em svg_mesmo_dow() (/home/ubuntu/cafezinho/v6/painel_cctv_v6.py, svc cctv-v6, marca graficos_dow_rotulos_frente_20260908, backup painel_cctv_v6.py.bak_pre_rotulos_dow_20260908): (1) barras fill-opacity="0.55"; (2) total em cima de cada barra desenhado DEPOIS das barras — número cheio se bw>=100 senão _fmt_k, mais recente #ffd75e negrito, demais #bcd9f2, halo paint-order="stroke" stroke=#0a0f1a stroke-width=3.5; (3) linha tracejada + rótulo da média acrescentados POR ÚLTIMO (frente, halo); se abs(Y(ult)-ym) < fs+8 e houver espaço, rótulo vira p/ baixo da linha (ym+fs+6) p/ não brigar com o número da última barra. Função compartilhada → FAROL (/v6/audiencia-redundante) + GA4 (/v6/audiencia) + LUMINA (/v6/lumina). Provas: curl + Chrome headless (FAROL 3 barras 4.681/9.434/14.176 + média 9.430 sobre a coluna; GA4 14 barras rótulos k; LUMINA 2 barras números cheios). Fórum: ADENDO 2 do Foruns/forum_farol_grafico_40h_topo_20260903.md; linha no CEREBRO_NODE_ATUALIZACOES.md; monitor ✅.

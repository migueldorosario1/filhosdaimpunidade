# Memória técnica — /v6/loops v2 humanizada (ZM-20260910-020)

**Data:** 10/09/2026 21:1x→21:3x BRT · **Autor:** ZCode/GLM-5.3 (sessão ZCodeProject)
**Fórum par (Tema Duplo):** `Foruns/forum_painel_v6_loops_humanizado_20260910.md`

## Contexto e gatilho

Miguel (chat, 10/09 ~21:1x): "a pagina loops do cctv, está sendo atualizada sempre? pq me parece que está defasada e com linguagem muito cifrada, técnica. tinha que ser mais clara, humanizada, e realmente atualizada".

## Investigação (passo a passo)

1. Monitor de trabalho lido; linha registrada antes de mexer (sem colisão — nenhuma sessão no painel_cctv_v6.py; a vigia da obra V3 é leitura-only).
2. Origem da página: criada 15/08 (Kimi K3) — ver `MONITORAMENTO_DE_TRABALHO.md.bak_pre_moka_telemetria_20260822` e fórum/memória `painel_cctv_v6_home_unica_pagina_loops_20260815`. Código: `tencent:/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (8207 linhas; serviço `cctv-v6.service`, ExecStart python3 3.12.3, porta 8084, nginx na frente).
3. Fontes de dados da página:
   - Laura ciclos: `v6_data/foruns/loop_trindade_laura/memoria_loop_laura/AAAA-MM-DD.md` (seções `## HH:MM BRT — ronda ...` com bullets `**fato:**/**lição:**`).
   - Laura consolidados: `.../controle/relatorios_chefe/*_relatorio_chefe_NNN.md` (formato antigo, YAML solitário).
   - Miguel: `v6_data/foruns/ponte_trindade_daemon/` (INDEX_ATIVO.md, ALERTAS_SLA.md, ESTADO_ATUAL.md — este último ausente hoje; parser degrada).
4. **Frescor medido (10/09 21:19 BRT):**
   - relatorios_chefe: último = 19/08 20:51 (#169). Morto há 22 dias (formato encerrado).
   - memoria_loop_laura: último = 09/09 18:51 (ronda 17:12). **Parado ~28h.**
   - Dell local (canônico) idêntico ao Tencent ⇒ espelho OK; a parada é da sessão Laura em si.
   - ponte_trindade_daemon: 10/09 21:05 (vivo; roda no Dell via `maintain_loop_miguel_bridge.py` cron */5, FILES espelhados ao Tencent).
5. Diário de 09/09 termina na ronda 17:12 sem nota de encerramento; grep no Cérebro não achou ordem de parada do loop Laura.

## Cura aplicada

- Função `pagina_loops` substituída (bloco de 11.290 → 16.221 chars) por versão `loops_v2_humano_20260910`; descrição da home NAV atualizada (linha ~1198).
- Método: script `/tmp/novo_pagina_loops.py` (scp + exec no Tencent) com `shutil.copy2` para backup, corte entre `def pagina_loops(` e `def _miguel_ticket_detalhe(`, guard anti-reaplicação.
- Semâforo Laura: ≤45min verde RODANDO; ≤120min amarelo ATRASADA; >120min + hora≥8 vermelho PARADA (frase com data/hora da última ronda); madrugada amarelo QUIETA (evita falso positivo — Laura ronda até ~23h).
- Semáforo fila Miguel: ≤10min ATUALIZADA; ≤30 LENTO; >30 PARADA (idade do INDEX_ATIVO.md).
- Consolidados antigos: `<details>` (open quando `?rel=` presente) + aviso "encerrado em 19/08".
- Ciclos: 3 abertos + demais em `<details>`; linha "Como ler" (fato/lição).
- Auto-refresh: `<script>setTimeout(location.reload, 300000)</script>` no fim do corpo (5 min).
- Rodapé sem caminhos; hora da leitura BRT renderizada por acesso.

## Testes / provas

- `python3 -m py_compile painel_cctv_v6.py` OK (SyntaxWarning linha 7695 é pré-existente de `_AOVIVO_HTML`, não desta mudança).
- `sudo systemctl restart cctv-v6` → `active`.
- curl público com Bearer `.painel_v6_token`: HTTP 200, 124 KB; extração textual confirmou "Status agora", "PARADA — Sem ronda desde 09/09 às 17:1x", "Histórico antigo", "Como ler", "recalculada".
- Bug próprio da v2 ("há há 28h15" — `_fmt_idade` já devolve "há X") corrigido com 4 replaces; reprovado ao vivo (regex "há há" ausente).

## Rollback

```bash
ssh tencent "cd /home/ubuntu/cafezinho/v6 && cp painel_cctv_v6.py.bak_pre_loops_humano_20260910 painel_cctv_v6.py && python3 -m py_compile painel_cctv_v6.py && sudo systemctl restart cctv-v6"
```

## Estado / próximos passos

- Pronto: página v2 no ar, provada, com backup.
- Falta: religar a sessão da Laura (parada desde 09/09 17:12 — fora do alcance da página; status vermelho agora avisa). Homologação visual do Miguel.
- Observação menor: idade do índice da ponte chegou a ~20min na prova (esperado ~5) — monitorar cadência do espelho da daemon.
- Registro: fórum+memória gravados; catalogação no NODO OBSERVABILIDADE (§10.1 adendo) e ATUALIZACOES.

# Fórum — Página /v6/loops do CCTV: humanização v2 + diagnóstico do Loop Laura parado

**Data:** 10/09/2026 ~21h BRT · **Autor:** ZCode/GLM-5.3 · **Ref:** ZM-20260910-020
**Tema:** painel CCTV V6, página Loops — pedido do Miguel: "está defasada e com linguagem muito cifrada, técnica; tinha que ser mais clara, humanizada, e realmente atualizada".

## O que aconteceu (diagnóstico)

O Miguel tinha razão nos dois problemas, por causas diferentes:

1. **Defasada — SIM, em duas camadas:**
   - O **Loop Laura de verdade parou** na ronda das 17:12 de 09/09 (diário `memoria_loop_laura/2026-09-09.md` termina aí, sem nota de encerramento). Fonte local (Dell) e espelho (Tencent) idênticos — **não é falha de espelho/rsync**, é a sessão da Laura que parou de rondar. A página apenas refletia, sem avisar.
   - Um card inteiro no topo exibia o **"consolidado do chefe" nº169 de 19/08** (22 dias), formato encerrado, como se fosse notícia corrente.
2. **Cifrada — SIM:** rodapé com caminhos de arquivo (`foruns/loop_trindade_laura/...`), jargão ("formato diário pós-29/08", "ponta tripla", "C/X/G", "índice ativo", "alertas SLA"), e a prosa interna da Laura exposta sem moldura ("gateado", "13/13 no minuto", "BUG-178").

A página em si sempre foi dinâmica (recalcula a cada acesso) — a sensação de "não atualiza" vinha da fonte morta + card antigo no topo.

## O que foi feito (cura v2 — `loops_v2_humano_20260910`)

No `painel_cctv_v6.py` (Tencent), função `pagina_loops` reescrita:

- **Faixa "👁️ Status agora"** no topo: 2 painéis com semáforo honesto e frase humana.
  - Laura: RODANDO (≤45min) / ATRASADA (≤2h) / **PARADA em vermelho** ("Sem ronda desde 09/09 às 17:1x — há 28h. Vale religar/acordar a sessão da Laura") / QUIETA-madrugada (sem falso positivo de madrugada, já que ela ronda só até ~23h).
  - Fila da operação (ponte Trindade): ATUALIZADA / LENTO / PARADA pela idade do índice (normal 5 min).
- **Rondas da Laura** = "o diário de bordo da redação" com linha "Como ler" (fato = o que ela fez; lição = o que aprendeu); 3 rondas mais recentes abertas, demais colapsadas em "📅 Mostrar as N rondas mais antigas".
- **Histórico antigo (consolidados até 19/08)** colapsado em `<details>` com aviso "formato encerrado em 19/08, só consulta" (abre sozinho quando há `?rel=`).
- **Card Miguel** com labels humanos: "tarefas na fila", "prazos em risco", "última renovação da fila", "Tarefas abertas agora" + legenda de ticket/responsável.
- **Rodapé limpo:** "recalculada a cada abertura (leitura às HH:MM BRT) e se atualiza sozinha a cada 5 min se ficar aberta" — sem caminhos de arquivo; API bruta continua linkada.
- **Auto-refresh 5 min** (script de reload) — painel CCTV deixado aberto em tela agora se atualiza sozinho.
- **Home V6:** descrição da página reescrita ("Status ao vivo dos dois turnos: rondas da Laura (30 em 30 min) + fila de tarefas e prazos dos agentes").

## Provas

- `py_compile` OK · serviço `cctv-v6` reiniciado e `active` · HTTP 200 público (124 KB).
- Frases-chave conferidas no HTML renderizado: "Status agora", "PARADA", "Histórico antigo", "recalculada", "rondas mais antigas".
- Bug de frase "há há 28h" (duplicação com `_fmt_idade`) corrigido na hora e reprovado ao vivo ("há há" ausente).
- **Rollback:** `cp painel_cctv_v6.py.bak_pre_loops_humano_20260910 painel_cctv_v6.py && sudo systemctl restart cctv-v6`.

## O que falta / o que preciso de você (Miguel)

1. **Religar a sessão da Laura** — ela não ronda desde 09/09 17:12. A página agora avisa em vermelho, mas só a sessão dela voltando a gravar o diário muda o status para verde. (Não encontrei ordem de parada registrada no Cérebro.)
2. **Homologação visual** da página nova (costume da casa: pendência das entregas de painel).
3. Observação menor: o índice da fila da ponte chegou ao Tencent com ~20 min de idade na hora da prova (esperado 5) — se repetir, vale checar a cadência do espelho da daemon.

📁 Caminhos: código `tencent:/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` · backup `.bak_pre_loops_humano_20260910` · memória técnica: `Foruns/memoria_painel_v6_loops_humanizado_20260910.md`.

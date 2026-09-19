# Memória técnica — /v6/loops ciclos ao vivo da Laura (08/09 23:54 BRT)

Missão: ordem Miguel 08/09 ~23:4x («a página LUPES não atualiza, bota os relatórios lá») → parecer
+ «vai» → implementação.

## Arquivos tocados
- Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (svc cctv-v6, python3.12):
  - constante `LOOPS_LAURA_MEMORIA` (env CCTV_V6_LOOPS_LAURA_MEMORIA, default
    `FORUNS_DIR/loop_trindade_laura/memoria_loop_laura`);
  - função `_laura_ciclos(limite=12)`: glob `20*.md` desc, seções `re.split(r"(?m)^## ")` filtradas
    por `^(\d{1,2}):(\d{2}|[0-9]x|x{2})\s*BRT\s*—\s*(.+)$`, bullets `- **chave:** valor`
    normalizadas (fato/lição/erro próprio/causa/prevenção/ironia registrada/outros), idade BRT pelo
    header + stem do arquivo;
  - `pagina_loops`: card «ciclos ao vivo» no topo (12 blocos), pill semáforo só no ciclo 0
    (<45 ok / <90 warn / senão bad; demais pill-info), markdown **/* → <b>/<i> pós-html.escape;
  - card antigo → «🗂️ consolidados do chefe (formato antigo, até 19/08)»; aviso de vazio novo;
    rodapé de fontes atualizado.
- Backups: `painel_cctv_v6.py.bak_pre_loops_vivo_20260908` (+ o .bak_pre_rotulos_dow_20260908 da
  missão anterior na mesma noite).

## Comandos/provas
- `sudo systemctl restart cctv-v6`; `systemctl is-active` = active.
- curl http://43.156.151.165/v6/loops: 12 ciclos (23:2x→17:1x), «Mais recente há 31 min ·
  12 ciclos exibidos · arquivo do dia sincronizado há 36 min»; `<b>dois</b>` e `<i>…</i>` presentes.
- Screenshot Chrome headless (recorte do card) auditado visualmente: blocos legíveis, pills corretas.

## Armadilhas p/ próxima sessão
- O formato ANTIGO (relatorio_chefe) morreu em 19/08 — não "consertar" o rsync dele; a fonte viva
  é o arquivo diário. Minuto mascarável («17:1x») existe na prosa da Laura: substituir x→0 p/ idade.
- A página NÃO usa LLM: qualquer "melhoria" que gaste token aqui é fora do escopo.
- api_loops (/v6/api/loops, relatório Telegram 30/30min) NÃO foi tocada de propósito — adicionar
  chave lá é mudança aditiva segura, mas ficou como follow-up não pedido.

## Estado da missão
Aconteceu: parecer + implementação + provas + registros. Falta: nada do lado do agente.
Preciso do Miguel: só validar visualmente a página.

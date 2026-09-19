# Fórum — /v6/baleia travada no dia 01/09: causa e cura multi-fonte (06/09/2026)

**Data:** 06/09/2026 ~23:00 BRT
**Autor:** ZCode Dell (Qwen3.8-Max), por ordem direta do Miguel no chat ("a edição da baleia azul no v6 está travada no dia 1. corrige isso")
**Estado:** ✅ RESOLVIDO E PROVADO NO AR

## O problema

`http://43.156.151.165/v6/baleia` exibia sempre o "Boletim Baleia Azul — 01/09/2026 (tarde)", cinco dias depois da edição mais recente existir (Edição 37, tarde de 06/09, fechada 19:35).

## A causa (raiz)

- O painel (`painel_cctv_v6.py`, Tencent) procurava boletins **somente** em `BASE_DIR = /home/ubuntu/cafezinho/Projeto Cafezinho Agentes` (`pagina_baleia`, `_baleia_lista` e `pagina_baleia_edicao` faziam glob ali).
- Essa pasta era alimentada pelo fluxo antigo (wrapper Dell `enviar_baleia_azul_ponte.sh`, crons 08:00/19:30). Com a **unificação da Baleia no DSN Chefe em 01/09 ~21:15** (monitor: "wrapper Dell OFF"), nada mais escreveu ali — o último arquivo é `boletim_baleia_azul_20260901.md` (mtime 01/09 19:30).
- Os boletins novos (2×/dia, `_manha`/`_tarde`) passaram a chegar pela **ponte GitHub** em `cerebro/Foruns/ponte_laura_completa/baleia_azul/`. Na Tencent eles já existiam, frescos, em DOIS lugares: `v6_data/foruns/ponte_laura_completa/baleia_azul/` (FORUNS_DIR do painel) e o clone `cerebro-miguel` (pull fresco — FETCH_HEAD 06/09 23:30). O painel é que não conhecia esses caminhos.
- Detalhe secundário: os boletins novos **não têm linha `# `** (o título é a 1ª linha em texto puro) — o extrator de título do painel só achava heading markdown, então mesmo lendo o arquivo novo o título cairia no genérico.

## A cura (decisões)

1. **Painel multi-fonte, sem novo cron/mover arquivo:** funções `_baleia_dirs()` / `_baleia_arquivos()` / `_baleia_turno()` / `_baleia_titulo()` no painel. Ordens de busca: `CCTV_BALEIA_DIR` (env opcional) → `FORUNS_DIR/ponte_laura_completa/baleia_azul` → `cerebro-miguel/cerebro/Foruns/ponte_laura_completa/baleia_azul` → `BASE_DIR` (legado + extraordinárias).
2. **Dedupe por (data, turno):** arquivo legado sem sufixo conta como turno "tarde" (o fluxo antigo emitia à noite) — evita duplicar 01/09 no histórico; a ponte tem prioridade sobre o legado.
3. **Título com fallback:** linha `# ` se existir; senão a primeira linha não vazia (formato novo da ponte).
4. As três rotas (`/v6/baleia`, `/v6/baleia-historico`, `/v6/baleia-edicao/<nome>`) usam as mesmas fontes.

## Provas (06/09 ~23:0x)

- py_compile OK (Python 3.12.3 Tencent; SyntaxWarning pré-existente linha 7244, sem relação) + `systemctl restart cctv-v6` → active.
- Interna `127.0.0.1:8084/baleia`: HTTP 200, `<title>Boletim Baleia Azul — Edição 37 · tarde · domingo, 6 de setembro de 2026 · fechada às 19:35</title>`, fonte `boletim_baleia_azul_20260906_tarde.md`.
- Externa `http://43.156.151.165/v6/baleia`: mesmo título + corpo do boletim renderizado (manchete "O domingo em que a produção virou a curva do público", FAROL 8.261 presentes).
- `/v6/baleia-historico`: **62 edições**, topo 06/09 tarde → 06/09 manhã → 05/09...
- `/v6/baleia-edicao/boletim_baleia_azul_20260906_manha` = 200 · extraordinária `20260815_extraordinaria` = 200 · legada `20260820` = 200.

## Rollback

`ssh tencent 'cp -a /home/ubuntu/cafezinho/v6/painel_cctv_v6.py.bak_pre_baleia_ponte_20260906 /home/ubuntu/cafezinho/v6/painel_cctv_v6.py && sudo systemctl restart cctv-v6'`

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** painel curado e provado; a página volta a acompanhar sozinha cada edição nova que a ponte entregar (manhã e tarde), sem depender de cópia para BASE_DIR.
- **Falta:** nada técnico. BASE_DIR ficou como legado somente (histórico + extraordinárias).
- **Do Miguel:** só conferir visualmente `http://43.156.151.165/v6/baleia`. Se amanhã de manhã (~07:1x) a página NÃO virar para a edição da manhã, o gargalo passa a ser o sync dos fóruns até a Tencent (aí investigar quem puxa `v6_data/foruns`), não o painel.

**Memória-irmã:** `Memorias/memoria_baleia_v6_travada_dia1_multifonte_20260906.md`

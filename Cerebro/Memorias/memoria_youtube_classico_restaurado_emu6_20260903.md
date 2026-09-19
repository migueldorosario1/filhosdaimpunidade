# 🎬 Memória técnica — restauração do agente YouTube clássico + EMU-6 (03/09/2026 ~06:5x→07:4x BRT)

Fórum-irmão: `Foruns/forum_youtube_classico_restaurado_emu6_20260903.md`. Executor: ZM (Dell, ZCode/Kimi K3). Ordem: Miguel chat ~06:5x + ponte (268424, bolo EMU-6, ZD-20260903-001).

## 1. Diagnóstico (por que "estava ruim")

- **Espelho** recebia posts V4.1 (autor 5470) publicados (400305 «Análise do IPCA e a Influência do Câmbio na Inflação Brasileira» — title-case inglês + vago; 400309 flagrado «ALUCINOU» pela casa). Cat 100005 = "Estatística" (experimento V4.2, autorizado — NÃO foi desligado).
- **Minha reescrita do materializador** (02/09 ~23:5x, 21.648 B) adicionou bloco de princípios com TESE+VILÃO forçados e regra de título EMU-2 restritiva ("UMA unica frase, sem sigla, sem dois-pontos, cargo em vez de nome") — combinação que empobreceu o texto e espremeu os títulos. Miguel: "vagabunda". Preservada em `.bak_minha_vertical_desativada_20260903`.
- **Cadeia da vertical espelho**: tencent `alimentador_fila.py` (cron `5,35 * * * *`, marcador ALIMENTADOR_YT_VERTICAL_V41_20260902_ZM) alimentava `queue_youtube.md` no repo. DESATIVADA 03/09 ~07:0x: linha comentada (`# DESATIVADO_20260903_ZM`), backup `crontab.bak_pre_desativa_vertical_espelho_20260903`.

## 2. Restauração do clássico (NYC `/root/agents_labs/youtube_v2/`)

- Base: `agente_youtube_v2_materializador.py.bak_pre_vertical_luxo_nomes_20260902` (325 linhas — prompt clássico neutro "Voce e editor do portal O Cafezinho" + escada de luxo gpt-5.6-sol→qwen-plus já embutida).
- Enxerto 1 — **título EMU-1+2+6** (substitui `'1. Crie titulo jornalistico em portugues.'`): porta/não-resumo, agente concreto, ação com objeto completo, zero jargão solto, uma oração, proibições EMU-1/2, teste "entendi sem ler?" + caso-escola 268424.
- Enxerto 2 — **NOMES SEM ERRO/personagens** (da minha versão, ordens 16/08+25/08): `PERSONAGENS_DB` (`/root/agent_data/personagens_youtube.json`), `_carregar_personagens()`, `_bloco_personagens_prompt()` (grafias canônicas + aliases errados da transcrição no prompt), item 12 na tarefa + seção GRAFIA CANONICA no prompt, e `corrigir_nomes_personagens()` aplicado a título+html no `validar_material` (fail-soft, provado "Fernando Addad"→"Fernando Haddad").
- Resultado: 401 linhas, `py_compile` OK local e remoto, sha `c7f2602f91f49efc`. Minha versão preservada (`.bak_minha_vertical_desativada_20260903`, 21.648 B).
- **Publicador**: `agente_youtube_v2_publicador.py` — `WP_URL=https://controle.ocafezinho.com/wp-json/wp/v2/posts`, `status_wp="draft"` por padrão (draft-only confirmado). **Cron `0 11,17 * * *` /root/youtube_v2_pipeline.sh ATIVO** (coletor→produtor→auditor→publicador; o produtor importa `material_llm` do materializador restaurado).

## 3. Bolo EMU-6 na linha inteira

| Alvo | Arquivo | Patch | Prova |
|---|---|---|---|
| Redator V4.1 (briefing camada 1) | NYC `/root/v4_vertical_draft_worker.py` | segmento novo após a linha 2814 (regra de título existente) | PATCH_OK + compile + grep=1; bak `.bak_pre_bolo_emu6_20260903` |
| Revisor R2 (camada 3) | tencent `/home/ubuntu/dsn_revisor2/dsn_revisor2.py` | regra velha ("até ~90 caracteres, máx 1 nome próprio") SUBSTITUÍDA pelo bolo | PATCH_OK + compile + grep=1; bak idem |
| YouTube clássico | materializador restaurado | enxerto 1 (acima) | compile + grep=3 |
| Revisores DSN + Loop Laura | canal `Foruns/revisao/` + INDEC R1/R2 | FEITO pela sessão us65 (bolo verbatim, commits 05:39-05:44) | ronda Chefe 06:00 |

Bolo-fonte (canônico): `cerebro/Estilo/BLOCO_PRONTO_REGRA_TITULO_EMU6.md` no repo.

## 4. Espelho (laboratório — Miguel examina)

- Categorias confirmadas via REST: **Estatística id 100005** (slug estat) e **Investimento id 100007** (slug investimento, criada 03/09 04:1x). Nada a criar.
- Publicações 400305/400309 no espelho = experimento V4.2 Estatística (reforma autorizada por outra ordem do Miguel ~04:5x, DSC-064 — fora do meu escopo; casa já vigia).
- Monitoramento: Chefe/DSC vigiam (DSC-064, critérios §4 do checklist V4.2) + meus relatórios de monitoramento incluem o espelho quando houver novidade.

## 5. Rollback e riscos

- Rollback completo documentado no fórum (3 passos independentes). Risco residual: a 1ª corrida das 11h pode repetir pauta já rascunhada (dedup do banco de diálogos cobre); qwen-plus de fallback pode falhar por cota (cascata cai no roteador global — fail-open por desenho).

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 07:4x BRT

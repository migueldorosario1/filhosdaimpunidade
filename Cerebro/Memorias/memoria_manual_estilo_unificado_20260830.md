# 🧠 MEMÓRIA TÉCNICA — MANUAL DE ESTILO UNIFICADO (implantação v1.0.0)

**Data:** 30/08/2026 ~10:36→11:3x BRT · **Agente:** ZCode/GLM-5.3 · Fórum irmão: `Foruns/forum_manual_estilo_unificado_20260830.md`

## Arquivos criados (todos NOVOS; nada sobrescrito)

| Arquivo | Papel |
|---|---|
| `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` | FONTE ÚNICA v1.0.0 (Núcleo A1–A8 + Perfis B1–B5 + Operação C1–C4 + inventário) |
| `Cerebro/CEREBRO_NODE_ESTILO.md` | Nodo Camada 2 (catálogo de estilo; entrada pelo Index Master) |
| `Cerebro/Foruns/forum_manual_estilo_unificado_20260830.md` | decisões + plano E0–E6 + regras vivas |
| `Cerebro/Memorias/memoria_manual_estilo_unificado_20260830.md` | este log |

Editados: `CEREBRO_INDEX_MASTER.md` (bloco de destaque ESTILO no topo, ao lado de ARQUITETURA_MOKA) · `CEREBRO_NODE_ATUALIZACOES.md` (linha 30/08) · `MONITORAMENTO_DE_TRABALHO.md` (linha da sessão aberta→fechada ✅).

## Fontes unificadas (inventário verificado no disco)

1. `Outros/novo livro/manual estilo/Manual_de_Estilo_Filhos_da_Impunidade_2026_08_17.md` (canônico do livro, #1–#34 consolidadas + #35–#55 brutas em transcrição de voz) — cópias: `canonicos/`, `Kimi K3/MANUAL_DE_ESTILO.md` (v1.0 24/07 → v1.1 → reorganização 04/08), `.bak_20260804_pre_reorganizacao`.
2. `Outros/novo livro/Kimi K3/verifica_estilo.py` (verificador regex v1.0 24/07).
3. `Outros/novo livro/Kimi K3/REFERENCIA_LITERARIA.md` (Machado de Assis + Hunter S. Thompson — citada no NODE do livro; leitura obrigatória junto ao manual).
4. `Cerebro/memoria_estilo_editorial_v5.md` (v5.0.0 20/08, Laura-AGY: 7 regras de título + 4 camadas E-E-A-T + tom + visual §5 + registro 30/08 da Emenda 13).
5. `Cerebro/claude_memory/reference_manual_estilo_editorial_v4_1_canonical_20260820.md` (régua Laura: h3 não strong; V4 legacy × V5 canonical).
6. `nyc:/root/v4_labs/dados/diretriz_qualidade_viva.md` (34 linhas: Emenda 12 capas de pessoas + lições diárias 26-29/08 + EMENDA 13 siglas — o ÚNICO que o redator V4.1 lê hoje; backups .bak_pre_emenda11/12/13 e pre_regra_*).
7. `Cerebro/Memorias/memoria_estilo_miguel_rosario_20260828.md` (anti-repetição com casos reais, vícios IA, música do texto 29/08, sem spoiler 29/08).
8. `Cerebro/Foruns/ESTILO-V4.md` + `ESTILO-V5.md` (debate histórico; duplicados em ESTILO_V4/V5 sem hífen).
9. `Cerebro/Foruns/forum_ideias_livros_miguel.md` (estante viva: Filhos V1 128k→240k; Origens quase todo escrito; Singularidade "a iniciar" — agora atualizada com os 2 caps reais) + `memoria_plano_editora_multilingue_20260727.md` (Moca Editions; lançamento = Singularidade).
10. Histórico: `Outros/novo livro/Foruns/manual_estilo_v8_e_backups_20260727.md` (deploy V8 do site do livro: modal interativo + ditado por voz + backup diário 04:00 — é sobre a INTERFACE do manual, não conteúdo).

## Pesquisa Singularidade (ficção)

- Painel Tencent: rota `/v6/ficcao` REMOVIDA do menu (backups `painel_cctv_v6.py.bak_pre_pagina_ficcao_20260817` e `.bak_pre_remove_ficcao_20260817` preservam o código completo: FICCAO_DIR=`/home/ubuntu/cafezinho/v6_data/ficcao`, APIs estado/participacao/audios).
- Estado real lido: `estado.json` = livro "Singularidade", próximo_capitulo 3, caps 1-2 com resumos completos e posts 400111/400114 (cat 100002), resumo_corrido do universo (Veronica Vinge/Neuronet/Rio 2040).
- `participacoes.json`: 1 pendente + 1 histórico (teste). Agente antigo: `agente_ficcao_noturna.py` (Tencent + Dados_Frios).
- Watcher de áudio local quebrado: `ponte_cafezinho/ficcao_audio_watcher.py` importa `ponte_cafezinho.py` cujo `dict | None` (PEP 604) quebra em Python <3.10 → `TypeError` no log. Fix futuro: `from __future__ import annotations` ou `Optional[dict]`.

## Pesquisa Origens

- Fórum `projeto_cafezinho_agentes/foruns/forum_investigacao_livro_origens.md` (15/05): extração dos JSONL (`miller_livro_miguel.jsonl`) para `Origens_Livro/`; index completo de capítulos/áudios/bibliografia/comercial.
- Acervo no Dell: `Dados_Frios/livros baixados novos/Origens_da_democracia/` (+ cópia `Antigravity/`); nota: sessão GDRIVE (mesmo dia) está montando a biblioteca com fichas — NÃO mexi (coordenação do monitor).

## Espelhamento

- GitHub: via `sync_cerebro_to_github.py` (pós-fix DS031 de hoje de manhã — fix instalado e testado pela sessão das 10:00).
- NYC: scp do unificado para `/root/v4_labs/dados/MANUAL_DE_ESTILO_UNIFICADO.md` (cópia PASSIVA — não altera nenhum runtime; integração ao system prompt do V4.1 = Etapa 5, exige "vai").
- Filhos/livros: os manuais-vivos permanecem canônicos para as suas obras (regra do unificado: "na dúvida sobre livro, vale o #1–#55").

## Decisões de projeto registradas

1. **Não renumerar nada:** EMENDA 11/12/13 (portal) e #1–#55 (Filhos) seguem nas casas originais; o unificado sintetiza e aponta.
2. Emendas do unificado = **EMU-<n>** (começa na EMU-1 = absorção da Emenda 13).
3. Camada 1 respeitada: Index Master ganha só o bloco de destaque apontando para o NODE (Camada 2).
4. Perfis B: portal/artigos/Origens/Filhos/Singularidade — mesmo núcleo, regras de gênero separadas; ficção herda o Núcleo A integralmente na prosa.

## Pendências técnicas

- [ ] Etapa 5: injetar Núcleo A + 7 regras de título no system prompt do redator V4.1 (NYC) — aguarda "vai".
- [ ] Fix do `ficcao_audio_watcher.py` (PEP 604) + eventual reativação da página /v6/ficcao — aguarda pedido.
- [ ] Evoluir `verifica_estilo.py` para lint das EMU (E6, junto com o V4 reformado).
- [ ] E2: curadoria do Miguel no unificado.

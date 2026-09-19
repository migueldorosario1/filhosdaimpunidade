# CEREBRO_NODE_QUALIDADE_REDACAO

> [!IMPORTANT]
> **ROTA EDITORIAL V4 ATUAL — 10/08/2026:** diretrizes de redação do V4 devem ser tratadas no briefing de `/root/v4_vertical_draft_worker.py` e no prompt/runtime `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py`. `agente_controlado.py` é legado; referências antigas neste nodo são históricas, não instruções de manutenção. Ver `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

Node vivo para relatorios do Agente de Qualidade de Redacao.

## Regra

Este node guarda diagnosticos diarios de qualidade editorial do Cafezinho.

O agente de qualidade:

- le posts e logs em modo read-only;
- mede clareza, densidade factual, aderencia editorial, rigor temporal/factual, estilo, SEO e estrutura;
- registra vicios recorrentes e exemplos;
- pode sugerir ajustes de prompt/diretriz apenas como proposta;
- nao publica, nao rebaixa post, nao altera tier e nao edita codigo autonomamente.

Qualquer mudanca real em `diretrizes_editoriais.py`, prompts ou config exige consenso da Trindade, aprovacao de Miguel, backup, registro no indice de mudancas e monitoramento pos-ajuste.

## Ideias a Desenvolver

### 2026-06-16 — Agente de Aprendizado Editorial Controlado

Miguel pediu estudar uma camada nova ligada ao ecossistema do Agente Qualidade: um agente capaz de usar os relatorios de qualidade, diretrizes, monitoramento humano, auditor de titulos e ticks do Claude Daemon para propor melhorias estruturais em diretrizes editoriais, prompts e demais pontos que afetam a qualidade dos posts.

Esclarecimento de Miguel: o objetivo de longo prazo e automatizar tambem esse processo. A fase inicial deve ser segura/read-only, mas a arquitetura deve nascer preparada para evoluir ate automacao progressiva, com gates, rollback e medicao pos-mudanca.

Principio registrado:

- o agente deve aprender com evidencias recorrentes;
- nao deve transformar diagnostico fraco em regra dura;
- nao deve alterar producao sozinho;
- deve priorizar solucao upstream quando a causa estiver em produtor/diretriz;
- deve manter revisor/auditor como safety net inteligente, nao como muleta permanente;
- deve exigir websearch quando o problema envolver fato, fonte, data, cargo, identidade ou imagem;
- qualquer mudanca real precisa de proposta, diff candidato, simulacao antes/depois, autorizacao, backup, smoke, rollback e medicao pos-mudanca.
- meta evolutiva: read-only -> proposta -> diff candidato -> simulacao -> deploy supervisionado -> automacao restrita de baixo risco -> automacao assistida de patches seguros.

Forum de estudo: `Projeto Cafezinho Agentes/Foruns/forum_agente_aprendizado_editorial_controlado_20260616.md`.

Memoria relacionada: `Cerebro/Backups/memorias_provisorias/feedback_agente_aprendizado_editorial_controlado_20260616.md`.

### 2026-08-08 — Diretrizes do CEO (nova aba do painel CCTV V6)

Sprint aprovado pelo Miguel: nova aba `/diretrizes-ceo` no painel CCTV V6 onde o CEO (Miguel) fala (áudio Whisper) ou escreve uma ordem editorial e uma IA interpreta, identifica quais dos ~25 slots de inteligência do V4 são afetados (por etapa × escopo), propõe patch exato, e aplica após confirmação — com diff, rollback e registro no Cérebro. Peça central: um **Intelligence Registry** (`registry.yaml`) que *indexa* (não concentra) os prompts espalhados do V4. Respeita o fato de que a inteligência do V4 é dispersa por natureza (coleta, tese, título, revisão, imagem...). Inline `.py` → sentinel-markers `# >>> CEO:<id>`. Aplicação em fila + batch com backup/rollback. Áudio Whisper (chave no `.env.unificado`). IA Intérprete pela cadeia de failover (Kimi→Qwen→GLM).

Conecta-se diretamente à "Ideia a Desenvolver" de 2026-06-16 acima (Agente de Aprendizado Editorial Controlado): é a evolução daquele estudo — do diagnóstico read-only para um produto de edição dirigida por voz do editor, com gates, diff candidato, autorização, backup, rollback e registro. Mantém todos os princípios registrados (não alterar produção sozinho; websearch pra fato/fonte/data; diff candidato antes/depois).

- **Fórum:** `Foruns/forum_diretrizes_ceo_v4_20260808.md`
- **Memória:** `Memorias/memoria_diretrizes_ceo_v4_20260808.md`
- **Fases:** (1) Registry + leitores + UI só-leitura + sentinel-markers em cópia shadow; (2) IA Intérprete + edição por texto; (3) Patch Engine + rollback + Cérebro; (4) Áudio Whisper.

### 2026-08-12 — Curadoria de Imagem por Tese (teoria por vertical)

Documento canônico: [teoria_escolha_imagem_por_vertical_20260812.md](./Foruns/teoria_escolha_imagem_por_vertical_20260812.md) — a "teoria" que o futuro motor de escolha de imagem do V4 vai respeitar: a imagem não ilustra o texto, **comunica a tese**. Taxonomia de tipos visuais (pessoa/instituição/documento/local/infraestrutura/ilustração), regras por vertical (Geo=mapa oficial, Ciência=ilustração permitida, Nacional/Regional=foto real sempre, zero IA), critério `score_comunicacao_tese` 0-100, e loop de aprendizado (escolha humana vira gold → replay → regra). Pares: [forum_curadoria_imagem_por_tese_arquitetura_20260812.md](./Foruns/forum_curadoria_imagem_por_tese_arquitetura_20260812.md) + [memoria_curadoria_imagem_por_tese_arquitetura_20260812.md](./Memorias/memoria_curadoria_imagem_por_tese_arquitetura_20260812.md). Conecta com a rota V4 atual (`memoria_arquitetura_v4_canonica_pos_cutover_20260810`) e com o motor de tese `v4_curadoria_tese` (campo `frame_visual`). Estado: v1 documental; motor é Fase 1 do roadmap. — ZCode (GLM-5.2)

## Relatorios

Relatorios detalhados ficam em:

```text
root/agent_data/qualidade_redacao/
```


## [2026-05-20 14:31:47 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_143146 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_143146.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_143146.md`
- Posts avaliados: 5

### Notas medias
- clareza: 9.6/10
- densidade_factual: 9.2/10
- aderencia_editorial: 6.6/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 9.6/10
- seo_estrutura: 10.0/10

### Problemas recorrentes
- texto_curto: 1
- titulo_com_title_case_ou_caps: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 15:35:54 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_153553 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_153553.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_153553.md`
- Posts avaliados: 12

### Notas medias
- clareza: 9.67/10
- densidade_factual: 9.08/10
- aderencia_editorial: 6.42/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Problemas recorrentes
- texto_curto: 3

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 16:52:57 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_165256 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165256.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165256.md`
- Posts avaliados: 3

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.67/10
- aderencia_editorial: 7.33/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 7.33/10
- humor: 5.0/10
- tamanho: 8.33/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 16:53:19 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_165318 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165318.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165318.md`
- Posts avaliados: 3

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.67/10
- aderencia_editorial: 7.33/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 6.33/10
- humor: 5.0/10
- tamanho: 8.33/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 16:53:36 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_165336 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165336.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165336.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.0/10
- aderencia_editorial: 8.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 6.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 16:54:03 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_165402 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165402.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_165402.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.0/10
- aderencia_editorial: 8.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 6.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 18:36:41 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260520_183641 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_183641.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_183641.json`
- Modo: `inventario_hardcoded_dry_run` dry-run `True`
- Relatorios qualidade lidos: 6
- Achados hardcoded: 80

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-28] Auditor Títulos GPT V1 integrado ao ciclo de qualidade

- Fonte nova: `agent_data/auditor_titulos_gpt/auditor_titulos_gpt_*.jsonl`.
- Schema aceito: `auditor_titulos_gpt.v1`.
- `agente_diretrizes_editoriais.py` agora carrega eventos do auditor, ignora `ok/timeout/erro_modelo/erro_wp`, transforma `monitorar` em evidência fraca e envia categorias de título para `prompt_titulo`.
- Deploy remoto com cron `*/5` e `flock`: tag `AUDITOR_TITULOS_GPT_V1_20260528_CODEX`.
- Backup/rollback: `/root/Backups/auditor_titulos_gpt_20260528_012812/`.
- Aprendizado do primeiro cron: auto-correção por `numero_inflado` produziu falso positivo em `#252369`; título restaurado. V1 endurecida para corrigir apenas troca clara de entidade/cargo/data/geografia ancorada no lide; números, hipérboles e conhecimento de mundo ficam em `monitorar`.

## [2026-05-24 02:47 BRT] Correção Sprint G — fontes Sputnik/RT/TASS

- Miguel reafirmou que Sputnik, RT e TASS são fontes importantes para geopolítica e que o Cafezinho não discrimina fonte estatal.
- Correção aplicada no agente local `root/agente_diretrizes_editoriais.py`: removido gatilho negativo por `sputnik`, `rt/kremlin` ou `propaganda`.
- Regra candidata reescrita no relatório `relatorio_diretrizes_20260523_230910` para: `Atribuir e contextualizar fontes geopoliticas sem discriminacao`.
- Formulação canônica: fontes russas, chinesas, iranianas e do Sul Global devem ser tratadas com a mesma seriedade de Reuters/AP/AFP. O texto deve atribuir e contextualizar, sem rebaixar fonte estatal como propaganda, sem exigir confirmação ocidental e sem transformar relatos russos em desmentido ou fake news.
- Validação: `python3 -m py_compile root/agente_diretrizes_editoriais.py` OK.

## [2026-05-22 18:12 BRT] Monitoramento Humano — Google Doc Controle IA

Miguel indicou o Google Doc `Controle IA O Cafezinho` como fonte viva do futuro `agente_monitoramento_humano.py`.

Fonte canônica:
`https://docs.google.com/document/d/1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY/edit?tab=t.0`

Dry-run Codex:

- Snapshot bruto: `root/agent_data/monitoramento_humano/controle_ia_ocafezinho_google_doc_snapshot_20260522.txt`
- JSON estruturado: `root/agent_data/monitoramento_humano/controle_ia_ocafezinho_estruturado_20260522.json`
- Laudo Markdown: `root/agent_data/monitoramento_humano/laudo_monitoramento_humano_google_doc_20260522.md`
- Fórum: `Foruns/forum_agente_monitoramento_humano_20260521.md` §10

Achado da data mais recente, 22/05/2026:

- 20 apontamentos humanos.
- 11 problemas de título.
- 7 problemas de imagem destacada.
- 1 problema de formatação.
- 1 outro.
- 16 pendentes e 4 corrigidos.

Regra importante: observações humanas não viram automaticamente lista de palavras proibidas. O Agente de Diretrizes deve transformar esses achados em inteligência editorial, especialmente para detectar título com cara de IA, título ambíguo, título longo sem chamada, título com duas chamadas e imagem que reduz credibilidade.

Prudência: `agente_monitoramento_humano.py` deve nascer em dry-run/read-only. Ele pode ler, estruturar e gerar laudo. Não pode alterar Google Doc, WordPress, diretrizes, prompts ou cron na primeira versão.

## [2026-05-20 22:39 BRT] Arquitetura: destino das observacoes do Agente de Qualidade
<!-- QUALIDADE_DESTINO_OBSERVACOES_20260520_2239 -->

Decisao registrada por Miguel/Codex: as observacoes do Agente de Qualidade nao devem virar automaticamente mudancas em `diretrizes_editoriais.py`.

Elas devem ser classificadas em tres camadas:

1. **Diretriz editorial permanente**: quando o problema e recorrente, estrutural e vale para todo o sistema. Exemplos: linha editorial do Cafezinho, clareza, simplicidade, lado politico explicito quando cabivel, regra contra release sem voz editorial, numeros fortes sem fonte, duplicidade semantica, imagem destacada contextual e fonte unica/geopolitica com atribuicao e contexto, sem discriminacao contra fonte estatal.
2. **Prompt especifico por funcao**: quando o ajuste pertence a uma etapa da cadeia. Exemplos: redator escreve com fonte/contexto; revisor pode reescrever tudo se o texto estiver ruim; auditor barra duplicidade e fonte fraca; fact-checking verifica numeros/datas/cargos/links; editor de titulo corta titulo longo ou artificial.
3. **Nota humanizada monitorada**: quando ha insight util, mas ainda sem evidencia suficiente para virar regra. Deve ser escrito em linguagem clara para Miguel/Trindade, apontando o que da para adiantar, o que precisa de mais evidencia e qual agente deveria receber o ajuste primeiro.

Fluxo recomendado:

```text
observacao de qualidade
  -> diretriz_permanente
  -> prompt_redator / prompt_revisor / prompt_auditor / prompt_factchecking / prompt_titulo
  -> nota_humanizada
  -> monitorar
```

Proxima melhoria sugerida para `agente_diretrizes_editoriais.py`: incluir `destino_sugerido` nas regras candidatas antes de qualquer escrita automatica.

Forum de debate: `Foruns/forum_agente_qualidade_redacao_20260520.md` §12.

## [2026-05-21 14:40 BRT] Sprint de ativação segura — Qualidade Redação
<!-- QUALIDADE_REDACAO_SPRINT_20260521_1440 -->

Forum principal: `Foruns/forum_agente_qualidade_redacao_20260521.md`

Status da rodada:

- Bloco 1 Kimi Code: inventário read-only entregue; node local já existia e foi linkado no `CEREBRO_INDEX_MASTER.md`.
- Bloco 2 Claude Monitor: leitura editorial entregue; aderência 6.42/10 é mista, com drift real e heurística miscalibrada.
- Bloco 3 DeepSeek: em andamento, auditoria read-only da segurança do smoke `--live-llm`.
- Bloco 4 Antigravity: pendente, arquitetura do ciclo de aprendizado.
- Bloco 5 Codex: decisão final sobre smoke real em 3 posts após receber Blocos 3 e 4.

Regra operacional adicionada por Miguel:

> O Maestro não deve apenas responder; ao receber uma entrega, deve auditar e já distribuir a próxima ação adequada, mantendo os agentes em movimento sem atropelar segurança.

Limites mantidos:

- sem cron;
- sem chamada paga em volume;
- sem alteração de `.py`;
- sem mudança de prompt mestre;
- sem produção editorial automática.

<!-- /QUALIDADE_REDACAO_SPRINT_20260521_1440 -->

## [2026-05-21 14:48 BRT] Smoke real live_llm — run 20260521_144711
<!-- QUALIDADE_REDACAO_SMOKE_20260521_144711 -->

Forum: `Foruns/forum_agente_qualidade_redacao_20260521.md` §7.13

Comando executado:

```bash
python3 root/agente_qualidade_redacao.py --live-llm --llm-posts 3 --max-posts 3 --hours 24
```

Resultado:

- exit code `0`;
- `ok: true`;
- 3 posts avaliados;
- relatórios gerados em `root/agent_data/qualidade_redacao/relatorio_20260521_144711.{json,md}`;
- sem cron;
- sem `--guardar-cerebro`;
- sem alteração de código/prompt/publicação.

Notas médias:

- clareza: 10.0/10
- densidade factual: 10.0/10
- aderência editorial: 6.0/10
- rigor temporal/factual: 8.67/10
- estilo jornalístico: 10.0/10
- SEO/estrutura: 10.0/10

Problemas do avaliador:

- Anthropic/Sonnet falhou HTTP 400;
- `gemini-3.1-pro` retornou 404;
- `gemini-2.5-pro` respondeu mas parse JSON falhou;
- consolidação por post ficou vazia quando Sonnet falhou;
- decisão Codex: cron bloqueado até corrigir tratamento de fallback/consolidação.

Próxima ação: DeepSeek Bloco 3B Qualidade em modo read-only.

<!-- /QUALIDADE_REDACAO_SMOKE_20260521_144711 -->

<!-- /QUALIDADE_DESTINO_OBSERVACOES_20260520_2239 -->

## [2026-05-20 23:03 BRT] Implementacao: `destino_sugerido` nos agentes de qualidade/diretrizes
<!-- QUALIDADE_DESTINO_OBSERVACOES_IMPLEMENTADO_20260520_2303 -->

A arquitetura de destino das observacoes foi levada para os agentes:

- `root/agente_qualidade_redacao.py`: relatorios agora carregam `orientacao_destino_observacoes`. Em modo `--live-llm`, o prompt pede `destino_sugerido` e `nota_humanizada` por critica/proposta.
- `root/agente_diretrizes_editoriais.py`: recebe `destino_sugerido` dos relatorios quando existir; quando nao existir, classifica deterministamente por categoria. Regras candidatas agora incluem `destino_sugerido`, `destino_descricao` e `nota_humanizada`.

Destinos validos:

```text
diretriz_permanente
prompt_redator
prompt_revisor
prompt_auditor
prompt_factchecking
prompt_titulo
nota_humanizada
monitorar
```

Validacao local:

- Qualidade: `run_id 20260520_230136`
- Diretrizes: `run_id 20260520_230137`

Deploy tecnico Tencent/Cingapura:

- Backup qualidade: `/root/Backups/agente_qualidade_redacao.py.bak_pre_destino_observacoes_20260520_230147_codex`
- Backup diretrizes: `/root/Backups/agente_diretrizes_editoriais.py.bak_pre_destino_observacoes_20260520_230147_codex`
- Smoke qualidade: `run_id 20260520_230204`
- Smoke diretrizes: `run_id 20260520_230205`

Estado: passivo/read-only. Sem cron novo. Sem escrita automatica em `diretrizes_editoriais.py`.

Forum: `Foruns/forum_agente_qualidade_redacao_20260520.md` §13.

<!-- /QUALIDADE_DESTINO_OBSERVACOES_IMPLEMENTADO_20260520_2303 -->

## [2026-05-20 23:38 BRT] Eleições: separação entre estilo e diretriz
<!-- ELEICOES_ESTILO_DIRETRIZ_SPLIT_20260520_2338 -->

Miguel esclareceu que o Agente Eleições não deve ser tratado como site restrito de análise eleitoral/dados. Ele cobre notícia quente, escândalo, bastidor, palanque, justiça eleitoral, pesquisa e análise política.

Correção aplicada por Codex:

- `agent_data/diretriz_eleicoes_2026.json`: Flávio Bolsonaro + Daniel Vorcaro + Banco Master/Dark Horse marcado como prioridade editorial máxima quando houver fonte verificável.
- `agente_eleicoes_produtor.py`: carregador da diretriz agora lê todos os blocos v2, inclusive `direita_nacional`, `direita_estadual`, `escopo_de_pauta_principal` e `tom_editorial`.
- `ESTILO_ELEICOES`: aliviado para voz/forma; TSE, 2022/2024, votos, prefeituras e Cartão são recursos condicionais, não travas obrigatórias.
- Removidas amarras de produção: `800-1000 palavras`, bullet obrigatório e subtítulos-modelo como "O reflexo de 2022".

Decisão arquitetural:

- **Estilo** = voz, clareza, ritmo, formato e legibilidade.
- **Diretriz** = linha editorial, prioridade política, critérios de publicação e vetos.
- **Auditoria/fact-check** = risco factual, fonte, número sem lastro, instituto suspeito e alucinação.

Backups Tencent:

- `/root/Backups/agente_eleicoes_produtor.py.bak_pre_estilo_diretriz_split_20260520_233742_codex`
- `/root/Backups/diretriz_eleicoes_2026.json.bak_pre_estilo_diretriz_split_20260520_233742_codex`

Forum: `Foruns/forum_diretrizes_agente_eleicoes_20260520.md` §8.2.

## [2026-05-21 01:18 BRT] Eleições: atualização temporal, fonte-ouro e mutirão Vorcaro/Flávio

Miguel corrigiu falso veto factual: Ciro Gomes voltou ao PSDB em 2025, então `Ciro Gomes (PSDB)` é fato atual e não alucinação. Correção estrutural aplicada em Tencent:

- fact-check Perplexity/Qwen e segundo portão asiático instruídos a não usar memória antiga para partido/cargo em política viva;
- produtor Eleições injeta data/hora BRT e consulta Brave News antes de redação/revisão, anexando contexto recente da pauta e dos atores;
- validator numérico passou a aceitar números literalmente presentes em fonte-ouro com texto integral; número fora da fonte/Cartão continua bloqueando;
- CNN Brasil e O Povo entraram em fonte-ouro do coletor; banco remoto atualizado para pautas já coletadas desses domínios;
- falha numérica em pesquisa agora move pauta para `CARTAO_INCOMPLETO_REVISAVEL`, evitando loop automático.

Mutirão noturno publicou 6 matérias Cafezinho sobre Flávio Bolsonaro/Vorcaro/Dark Horse entre 00:00 e 01:15 BRT de 2026-05-21. Banco remoto após ciclo: `PUBLICADO=33`, `PENDENTE=14`, `CARTAO_INCOMPLETO_REVISAVEL=12`, `DESCARTADO=328`.

Backups remotos principais: `fact_check_perplexity.py.bak_pre_ciro_psdb_20260520_235119_codex`, `agente_eleicoes_legado.py.bak_pre_ciro_psdb_20260520_235119_codex`, `agente_eleicoes_produtor.py.bak_pre_contexto_temporal_brave_20260521_002905_codex`, `agente_eleicoes_produtor.py.bak_pre_fonte_ouro_numeros_20260521_004943_codex`, `coletor_eleicoes.py.bak_pre_fonte_ouro_cnn_opovo_20260521_010706_codex`.

Pendência de qualidade: fortalecer prompt de pesquisa para impedir DeepSeek de inserir números fora da fonte/Cartão; corrigir falso alerta do detector de cargos que apontou Lula como senador em dry-run.

<!-- /ELEICOES_ESTILO_DIRETRIZ_SPLIT_20260520_2338 -->

## [2026-05-20 18:36:48 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_183647 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_183647.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_183647.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 6.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 18:37:50 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_183749 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_183749.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_183749.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 7.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- nenhum problema recorrente detectado pela heuristica

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 18:39:20 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260520_183919 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_183919.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_183919.json`
- Modo: `inventario_hardcoded_dry_run` dry-run `True`
- Relatorios qualidade lidos: 8
- Achados hardcoded: 20

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-20 18:49:40 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_184939 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_184939.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_184939.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 7.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 7.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 18:52:03 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_185202 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_185202.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_185202.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 9.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 9.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 8.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 19:06:54 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_190653 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_190653.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_190653.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 10.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 5.0/10
- criatividade: 9.0/10
- humor: 5.0/10
- tamanho: 10.0/10
- elegancia: 8.0/10

### Problemas recorrentes
- nenhum problema recorrente detectado pela heuristica

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 22:31:05 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260520_223105 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_223105.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_223105.json`
- Modo: `inventario_hardcoded_dry_run` dry-run `True`
- Relatorios qualidade lidos: 11
- Achados hardcoded: 40

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-20 22:31:34 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260520_223134 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_223134.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_223134.json`
- Modo: `inventario_hardcoded_dry_run` dry-run `True`
- Relatorios qualidade lidos: 11
- Achados hardcoded: 40

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-20 23:01:37 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260520_230136 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_230136.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260520_230136.md`
- Posts avaliados: 1

### Notas medias
- clareza: 10.0/10
- densidade_factual: 8.0/10
- aderencia_editorial: 6.0/10
- rigor_temporal_factual: 10.0/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 10.0/10

### Notas qualidade editorial
- coerencia: 10.0/10
- objetividade: 10.0/10
- repeticao: 10.0/10
- criatividade: 7.0/10
- humor: 5.0/10
- tamanho: 7.0/10
- elegancia: 10.0/10

### Problemas recorrentes
- texto_curto: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-20 23:01:37 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260520_230137 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_230137.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260520_230137.json`
- Modo: `inventario_hardcoded_dry_run` dry-run `True`
- Relatorios qualidade lidos: 12
- Achados hardcoded: 20

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-22 18:29:40 BRT] Monitoramento Humano
<!-- MONITORAMENTO_HUMANO_RUN_ID: 20260522_182939 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/monitoramento_humano/relatorio_monitoramento_humano_20260522_182939.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/monitoramento_humano/relatorio_monitoramento_humano_20260522_182939.md`
- Datas processadas: 22/05/2026
- Total de apontamentos: 20
- Categorias: `{"imagem_destacada": 7, "titulo": 11, "outros": 1, "formatacao": 1}`
- Destinos: `{"prompt_auditor": 7, "prompt_titulo": 11, "nota_humanizada": 1, "prompt_revisor": 1}`

O maior foco e titulo: ha sinal forte de estruturas artificiais, longas ou ambiguas. Imagem destacada aparece como risco editorial visivel: texto em ingles, ilustracao generica ou imagem sem relacao derrubam credibilidade.

<!-- /MONITORAMENTO_HUMANO -->

## [2026-05-23 23:09:10 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260523_230910 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260523_230910.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260523_230910.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 13
- Monitoramento humano lido: 2
- Evidencias humanas: 112
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-26 12:10:29 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260526_121029 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260526_121029.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260526_121029.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 0
- Monitoramento humano lido: 1
- Evidencias humanas: 92
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-26 14:59:43 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260526_145943 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260526_145943.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260526_145943.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 0
- Monitoramento humano lido: 1
- Evidencias humanas: 92
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-28 11:20:27 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260528_112027 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260528_112027.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260528_112027.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 1
- Monitoramento humano lido: 2
- Evidencias humanas: 112
- Eventos auditor_titulos_gpt lidos: 3
- Evidencias auditor_titulos_gpt: 2
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-28 11:22:23 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260528_112223 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260528_112223.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260528_112223.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 1
- Monitoramento humano lido: 2
- Evidencias humanas: 112
- Eventos auditor_titulos_gpt lidos: 3
- Evidencias auditor_titulos_gpt: 2
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-29 15:29:21 BRT] Monitoramento Humano
<!-- MONITORAMENTO_HUMANO_RUN_ID: 20260529_152920 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/monitoramento_humano/relatorio_monitoramento_humano_20260529_152920.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/monitoramento_humano/relatorio_monitoramento_humano_20260529_152920.md`
- Datas processadas: 29/05/2026, 28/05/2026, 27/05/2026, 26/05/2026, 25/05/2026
- Total de apontamentos: 77
- Categorias: `{"outros": 7, "formatacao": 8, "fonte_atribuicao": 1, "imagem_destacada": 19, "titulo": 40, "texto_curto": 1, "duplicidade": 1}`
- Destinos: `{"nota_humanizada": 7, "prompt_revisor": 8, "prompt_factchecking": 1, "prompt_auditor": 20, "prompt_titulo": 40, "prompt_redator": 1}`

O maior foco e titulo: ha sinal forte de estruturas artificiais, longas ou ambiguas. Imagem destacada aparece como risco editorial visivel: texto em ingles, ilustracao generica ou imagem sem relacao derrubam credibilidade. Duplicidade precisa entrar no auditor antes da publicacao. Texto curto precisa ser diferenciado entre nota curta legitima e materia incompleta.

<!-- /MONITORAMENTO_HUMANO -->

## [2026-05-30 00:28:11 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260530_002811 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_002811.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_002811.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 13
- Monitoramento humano lido: 3
- Evidencias humanas: 189
- Eventos auditor_titulos_gpt lidos: 0
- Evidencias auditor_titulos_gpt: 0
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-30 00:28:32 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260530_002831 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260530_002831.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260530_002831.md`
- Posts avaliados: 50

### Notas medias
- clareza: 9.58/10
- densidade_factual: 9.04/10
- aderencia_editorial: 7.0/10
- rigor_temporal_factual: 9.8/10
- estilo_jornalistico: 10.0/10
- seo_estrutura: 9.8/10

### Notas qualidade editorial
- coerencia: 9.9/10
- objetividade: 9.86/10
- repeticao: 9.28/10
- criatividade: 7.62/10
- humor: 5.08/10
- tamanho: 8.58/10
- elegancia: 9.72/10

### Problemas recorrentes
- texto_curto: 7
- ancoragem_temporal_fraca: 5
- frases_longas: 3

<!-- /QUALIDADE_REDACAO -->

## [2026-05-30 15:27:12 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260530_152712 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_152712.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_152712.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 13
- Monitoramento humano lido: 3
- Evidencias humanas: 189
- Eventos auditor_titulos_gpt lidos: 0
- Evidencias auditor_titulos_gpt: 0
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-05-30 15:27:19 BRT] Relatorio Fase 0
<!-- QUALIDADE_REDACAO_RUN_ID: 20260530_152717 -->

- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260530_152717.json`
- Markdown: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/qualidade_redacao/relatorio_20260530_152717.md`
- Posts avaliados: 50

### Notas medias
- clareza: 9.78/10
- densidade_factual: 8.76/10
- aderencia_editorial: 6.64/10
- rigor_temporal_factual: 9.68/10
- estilo_jornalistico: 9.96/10
- seo_estrutura: 9.72/10

### Notas qualidade editorial
- coerencia: 9.84/10
- objetividade: 9.96/10
- repeticao: 9.3/10
- criatividade: 7.6/10
- humor: 5.16/10
- tamanho: 8.7/10
- elegancia: 9.7/10

### Problemas recorrentes
- ancoragem_temporal_fraca: 8
- texto_curto: 7
- sem_link_organico: 2
- titulo_com_title_case_ou_caps: 1
- frases_longas: 1

<!-- /QUALIDADE_REDACAO -->

## [2026-05-30 15:27:31 BRT] Agente de Diretrizes Editoriais
<!-- DIRETRIZES_EDITORIAIS_RUN_ID: 20260530_152730 -->

- Relatorio: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_152730.md`
- JSON: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/agent_data/diretrizes_editoriais/relatorio_diretrizes_20260530_152730.json`
- Modo: `relatorio_dry_run` dry-run `True`
- Relatorios qualidade lidos: 14
- Monitoramento humano lido: 3
- Evidencias humanas: 189
- Eventos auditor_titulos_gpt lidos: 4
- Evidencias auditor_titulos_gpt: 3
- Achados hardcoded: 0

<!-- /DIRETRIZES_EDITORIAIS -->

## [2026-06-01 19:25 BRT] DEPLOY — Arquitetura de Diretrizes Provisórias vs. Permanentes
<!-- DEPLOY_DIRETRIZES_20260601 -->

### O que foi deployado
Implementação dos 4 passos da arquitetura de separação de diretrizes:

**1. `diretrizes_provisorias_v1.md`**
- Local: `/root/agent_data/diretrizes_editoriais/diretrizes_provisorias_v1.md`
- Estrutura vazia com seções para redator, revisor, gerador de títulos, auditor, fact-checking
- Template de registro de observação com status: em_observacao, ajustada, promovida, rejeitada
- É aqui que a Trindade trabalha livremente — regras técnicas, forma, ajustes

**2. `backup_diretrizes.py`**
- Local: `/root/backup_diretrizes.py`
- Backup automático com timestamp antes de qualquer write em diretrizes
- Comandos CLI: backup, listar, restaurar
- Protege: permanentes, provisórias, ativa

**3. `compilar_diretrizes.py`**
- Local: `/root/compilar_diretrizes.py`
- Parser de Markdown extrai regras estruturadas dos .md
- Gera `diretriz_ativa.json` com merge de:
  - editorial_base (conteúdo do antigo diretriz_editorial.json)
  - regras.permanentes (23 regras dos .md)
  - regras.provisorias (0 por enquanto)
  - instrucoes_agentes (blocos de texto prontos para injeção nos prompts)
- Flags: --dry-run, --verificar

**4. `agente_editorial.py` atualizado**
- Agora aponta para `diretriz_ativa.json` (com fallback para `diretriz_editorial.json`)
- Injeção automática das regras do redator no system_redacao

### Resultado da primeira compilação no Tencent
```
Regras permanentes extraídas: 23
  redator: 5
  revisor: 5
  gerador_de_títulos: 5
  auditor: 4
  fact-checking: 4
Regras provisórias: 0
editorial_base: presente
```

### Backups feitos (rollback disponível)
- `/root/backups/diretrizes_deploy_20260601/agente_editorial_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/diretriz_editorial_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/diretrizes_editoriais_pre_deploy_20260601.bak`
- `/root/backups/diretrizes_deploy_20260601/agente_diretrizes_editoriais_pre_deploy_20260601.bak`

### Arquivos novos no Tencent
- `/root/backup_diretrizes.py`
- `/root/compilar_diretrizes.py`
- `/root/agent_data/diretrizes_editoriais/diretrizes_provisorias_v1.md`
- `/root/agent_data/diretriz_ativa.json`

### Planos de monitoramento
- **Kimi Code:** monitorar compilação diária, verificar se regras chegam aos prompts
- **Claude Maestro:** monitorar qualidade dos posts, alertar se houver regressão

### §92
Deploy aprovado por Miguel (tick). Quórum: Kimi + Codex + DeepSeek + Miguel.

<!-- /DEPLOY_DIRETRIZES_20260601 -->

## [2026-08-09 ~07:15 BRT] CERCO DURO A TÍTULOS LONGOS — gate_titulo.py unificado

**Contexto:** ordem do editor Miguel após post #264875 (Marcola) com título de 193c, dois-pontos, travessão e erro de regência. Auditoria: 76% dos posts recentes fora da regra — a regra existia em `agente_controlado.py` mas não no publicador real (`motor_publicador.py`).

**Tema Duplo:**
- `Foruns/forum_cerco_titulos_longos_v4_20260809.md`
- `Memorias/memoria_cerco_titulos_longos_v4_20260809.md`

**Arquitetura nova:**
- `/root/gate_titulo.py` — **fonte única** de regras de título (máx 80c, sem `:`, sem travessão, sem "editorial", mín 4 palavras). API: `validar_titulo()` + `aplicar_gate_titulo()` (LLM×2 + fallback determinístico, nunca aborta).
- Integrado ao `motor_publicador.py` (antes do `requests.post(WP_URL)` final — por onde todo post passa).
- `agente_controlado.py`: `validar_titulo` delega ao gate; faixa 60-80→55-75c; prompts de geração + revisão Claude + auditor DeepSeek reforçados (hard-rule de tamanho + sem `:` + sem travessão + regência correta "Ministro da Fazenda").

**Estado:** ✅ deployado no NYC (sintaxe OK, testes OK, gate bloqueia títulos reais problemáticos). Backups `*.bak_pre_cerco_titulos_20260809`. Pendências Miguel: teto 80c? reescrever 18 antigos? espelho Tencent?

## [2026-08-10 ~10:15 BRT] TÍTULOS — SINTAXE E CLAREZA ACIMA DO LIMITE MECÂNICO

Ordem editorial do Miguel a partir do post WP #265071. O título de referência é
`Marina Silva chama campanha antivacina de Eduardo Bolsonaro de 'crime de lesa-humanidade'`
(89 caracteres). Regra permanente: preferir 55–80 caracteres, mas aceitar até 105
quando isso preservar sintaxe, precisão, nomes, atribuições ou complementos necessários.
É proibido truncar, inserir reticências, cortar em conjunção ou omitir termos essenciais
apenas para obedecer à contagem. Hierarquia: frase perfeita e inequívoca → tese central
→ concisão. `gate_titulo.py` e `agente_controlado.py` atualizados no NYC.

## [2026-09-02 ~16:0x BRT] V4.1 ULTRA-LUXO + CURA GEO/TEC + MANUAL v2.1.0 (ordem do Miguel: execução total)

Redação V4.1 em frontier: `gpt-5.6-sol` geral + `claude-fable-5` nacional
(experiência de gasto do Miguel; dispositivo de troca `scripts/aplica_ultra_luxo.py`,
volta ao super luxo = `--desligar`). Tese lê linha editorial + manual; pauta
afirmativa (BRICS/SCO/Sul Global) não exige vilão. Seca geopolítica/tecnologia
curada (fila sem clog + motivo honesto + coleta reforçada) e provada ao vivo.
Manual v2.1.0: princípios acima de regras mecânicas ("diretrizes editoriais,
não regras ditatoriais").

**Tema Duplo:**
- `Foruns/forum_v41_ultra_luxo_cura_geo_20260902.md`
- `Memorias/memoria_v41_ultra_luxo_cura_geo_20260902.md`


## [2026-09-09 ~15:4x BRT] Pauta chata/institucional passou na curadoria V4.1 (post 269549)

Caso: «Rádio Nacional celebra 90 anos com programação especial» (Cultura) = release EBC
reescrito publicado; juiz 1 (qwen) deu 7,61 (critérios PREMIAM: linha_casa 9 por «rádio
pública/soberania», encaixe 10), juiz 2 idem, frescor 40h dentro do teto de cultura (72h),
CL revisou e publicou. Diagnóstico: nenhuma camada mede CHATICE — falta regra contra
pauta institucional/celebratória (aniversário de instituição, programação especial,
homenagem, balanço) sem conflito/utilidade. Correção proposta: regra no
`dados/PADRAO_CURADORIA_QUALIDADE.md` (sem deploy) + regra dura nos juízes 1/2 do
`v41_ciclo.py` + item no checklist do CL. PATCH APLICADO com o «vai» do Miguel (09/09 ~16:1x, V41_PAUTA_CHATA_20260909): regra no padrão vivo
+ regra dura nos juízes 1/2; regressão 5/5 (Rádio Nacional 7,61→4,04 reprovada; EBC-com-disputa
8,57 aprovada — sem falso-positivo). Pendente: item no checklist do CL.

**Tema Duplo:**
- `Foruns/forum_v41_pauta_chata_institucional_juiz_20260909.md`

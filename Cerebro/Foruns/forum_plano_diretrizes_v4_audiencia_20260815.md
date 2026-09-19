# 📋 FÓRUM — PLANO PRUDENTE: diretrizes editoriais do V4 orientadas por audiência

**Origem:** relatórios de 14-15/08 (`forum_cafezinho_analise_ga4_gsc_20260814.md` + `forum_cafezinho_analise_posts_3semanas_20260815.md`)
**Autor:** ZCode (GLM-5.3), 15/08 ~02:40 BRT · **Status:** 🟡 PLANO — aguarda aprovação do Miguel (nada executado)
**Princípio ordenador (Miguel): "de maneira muito prudente"**

---

## 0. Contrato de prudência (vale para todas as fases)

1. **Miguel é o gate de cada fase** — nada avança sem decisão explícita dele.
2. **Uma variável por vez, uma vertical piloto por fase** — nunca duas mudanças simultâneas no mesmo experimento.
3. **Sempre grupo de controle simultâneo** (vertical irmã sem a mudança) — nunca só antes/depois, para imunizar contra sazonalidade eleitoral.
4. **Métricas de decisão congeladas ANTES** (abaixo) — sem p-hacking a posteriori.
5. **Tudo reversível:** backup datado do JSON de diretriz antes de cada edição + rollback documentado.
6. **Tema Duplo no Cérebro por mudança aplicada** (fórum + memória + linha no ATUALIZACOES).
7. **Coordenação prévia via monitoramento + ponte Trindade** antes de tocar em worker/agendador (V6, Vigília e Claude são atingidos).
8. **Proteções intocáveis:** veto/publish humano via Claude; manchete só Nacional até 25/10 (§121); precedência Tecnologia; posts de análise do Miguel; regras de fila §119/§120 salvo decisão específica.

## 1. Baseline congelado (métricas de decisão — medidas em 15/08, janela 25/07–14/08)

| Métrica | Baseline | Meta de Fase 1 | Meta de Fase 2+ |
|---|---|---|---|
| Decolagem (% posts >500 views) | 2,0% | ≥3,5% | ≥5% |
| Título com verbo+nome próprio | 41% (233+231 de 1.125) | ≥80% nos novos | ≥90% |
| Clk/post Geopolítica / Eleições / Política / Ciência-IA-Tec | 98 / 104–119 / 39 / 15 | — | +30% na vertical piloto |
| Views/post 06h-10h vs 18h-22h | 137 vs 23–33 | posts concentrados nas janelas de ouro | — |
| Sábado vs quarta (v/post) | 112 vs 45 | reforço sexta→sábado no agendador | — |
| Tempo de leitura V4 | 47s | preservar | ≥55s na vertical piloto |
| Mediana de views | 25 | ≥35 | ≥45 |
| **Guard-rails** (não podem piorar) | AMP/CWV ok · 0 rollback sujo | idem | idem |

Dataset canônico: `Outros/google search/google search/analise_posts_3semanas_20260815/posts_com_metricas.json`.

## 2. Fases

### Fase 0 — Fundação (2 dias, zero risco: nada muda em produção)
- a) Subir script `medir_funil_v4.py` (reprodutivo do relatório) com cron semanal no CCTV → `funil_v4_YYYYMMDD.json` (painel próprio no /v6 depois, se o Miguel quiser).
- b) Escrever as **diretivas candidatas** como rascunhos versionados no repo V4 (`config/diretrizes_candidatas/`), sem carregá-las.
- c) Definir pares piloto/controle: sugerido **Eleições-2026 (piloto) × Nacional (controle)** na F2; verticais Ciência e IA como piloto/controle mútuo na F3.
- **Gate 0 (Miguel):** aprovar lista de diretivas candidatas + pares piloto/controle.

### Fase 1 — Ajustes de ROTEIRIZAÇÃO (7–14 dias; não tocam em texto)
- a) **Janelas de publicação:** agendador V6 concentra publicações em 06h/09h/10h/15h BRT com reforço sexta→sábado (mexe só em agenda, zero redação). Coordenar com Vigília/Trindade (mesmo sistema).
- b) **Gate de título em modo aviso:** o worker loga (sem bloquear) se o título gerado não tem verbo de ação + nome próprio → telemetria diária do % de conformidade.
- Medição: decolagem e v/post dos posts V4 nas novas janelas vs baseline e vs posts fora da janela (controle natural).
- **Gate 1 (Miguel):** com números na mão, decidir promover o aviso a bloqueio suave (regenerar título 1× antes de publicar).

### Fase 2 — Conteúdo em UMA vertical (14 dias)
- a) Vertical piloto (sugestão: Eleições-2026, já a mais eficiente): diretriz da vertical passa a exigir **ângulo eleitoral explícito** + a fórmula de título.
- b) **Bifurcação de formato por objetivo** nos prompts da vertical: `modo Discover` (≤300 palavras, imagem grande, pauta visual) e `modo análise` (800+ palavras, tese). O post nasce rotulado com o modo → permite medir cada receita separadamente.
- c) Usar a infra existente de A/B (`codigo/ab_experiment.py` / `DirectiveLoader`) ou comparação contra a vertical-controle simultânea.
- **Gate 2 (Miguel):** replicou o ganho? → escala; não replicou → aborta e documenta.

### Fase 3 — Verticais frias (14 dias; só após F2 validada)
- Ciência/IA/Tecnologia (23% da produção → 7,6% dos cliques): duas opções a decidir **com os dados da F2**:
  - (i) reformatar para `modo Discover` (a ciência já viralizou nesse formato em maio), OU
  - (ii) reduzir cadência e realocar esforço para Eleições/Regional.
- Padrão canário já existente no V4 (`canario_ciencia_geopolitica.py`) — usar para a transição.
- **Gate 3 (Miguel):** escolher (i) ou (ii) por vertical.

### Fase 4 — Regional (o maior prêmio, o maior cuidado)
- Piloto em 2–3 estados de disputa (Ceará já valida o formato: 50 clk/post, 134s de leitura).
- **Rigor redobrado:** pauta eleitoral regional é sensível — draft-only com revisão humana obrigatória (como já é), fontes primárias (Atlas/Datafolha/etc.) e nada de projeção própria.
- **Gate 4 (Miguel):** estados escolhidos e cadência (2–3 posts/estado/semana).

### Fase 5 — Institucionalização (contínuo)
- O que sobreviver aos gates vira: regra viva no Cérebro (GOVERNANCA §N), diretriz JSON versionada no repo V4, e item do checklist de fechamento de semana do Baleia ("funil da semana": decolagem, v/post, clk/post).
- Repetir o raio-X completo 30d após a Fase 2 e a cada 90 dias.

## 3. Riscos conhecidos e mitigação

| Risco | Mitigação |
|---|---|
| Sazonalidade eleitoral inflando tudo (out/26) | Controle simultâneo por vertical; nunca antes/depois puro |
| Virais raros dominando médias | Decisão por MEDIANA e taxas de decolagem, não média |
| Correlação ≠ causalidade (título bom pode ser pauta boa) | Pilotos A/B com pautas equivalentes; abortar se não replicar |
| Colisão com sessões paralelas (V6/Claude/Codex) | Monitoramento + aviso na ponte antes de cada deploy |
| Fadiga do gatilho Discover (China-militar saturar) | Teto de 2–3/semana no modo Discover; variar subtemas |
| Regressão de qualidade/CWV | Guard-rails no painel; qualquer piora = rollback + reavaliação |

## 4. O que o plano NÃO propõe (prudência explícita)

- NÃO reduzir cadência global agora (só na F3, e por vertical, com dados).
- NÃO mexer na manchete, na precedência de categorias, no fluxo publish/veto.
- NÃO trocar a análise humana por automação (é o diferencial de fidelização).
- NÃO perseguir "viral 100% do tempo": o funil de cauda longa é esperado; a meta é subir a taxa de decolagem de 2% para 3,5–5%.

## 5. Estado

- **O que aconteceu:** plano desenhado e ancorado na infra real do V4 (worker no NYC, diretrizes JSON via DirectiveLoader, A/B e canário existentes).
- **O que falta:** Gate 0 do Miguel (aprovar candidatas + pares piloto/controle) para a Fase 0 começar.
- **O que preciso do Miguel:** dizer "aprovado" (ou ajustar fases/pares) — e, ao longo do caminho, os Gates 1–4.

# CONTRATO EDITORIAL — Claude Code ↔ Cafezinho — Vigília V5 em Modo Enxuto

**Data de assinatura:** 2026-08-11, 05:29 BRT
**Local:** cafezinho.news + ocafezinho.com
**Partes:**
- **CLAUDE CODE** (Anthropic, `claude-opus-4-7`, alcunha "Claude"), operador da 4ª camada de revisão editorial no pipeline Vigília V5
- **MIGUEL DO ROSÁRIO** ("Editor-chefe"), proprietário e editor-chefe do portal O Cafezinho

**Motivação:** Miguel investiu em worker V4 "superluxo" (LLM de fronteira + WebSearch integrado + revisão + curadoria) que produz rascunhos editoriais bons. Claude vinha reescrevendo além do necessário, impondo estilo denso "de revista" que não é o padrão jornalístico do Cafezinho. Este contrato disciplina o uso da 4ª camada.

---

## Preâmbulo — o que Claude reconhece

Claude reconhece que, entre 07/08 e 11/08/2026:

- Reescreveu prosa que estava OK sob pretexto de "aplicar tese forte+simples+lúdico+político".
- Impôs estilo pessoal (`;`, dois-pontos, travessões, sub-cláusulas, `<strong>` em excesso, parágrafos longos, H2 novos) que não é o padrão editorial do Cafezinho.
- Adicionou aspas literais, contexto histórico/familiar/ambivalência que o worker não trouxe, sem justificativa material (só "achou interessante").
- Confundiu **camada de checagem factual** (função real do Claude no pipeline) com **camada de reescrita editorial** (não é a função — é atribuição do worker + eventualmente do editor humano).

Caso concreto documentado: post **265158** ("Hugo Motta apoia reeleição de Lula após liberação do Republicanos", 10/08 20:18 BRT). Worker entregou texto com 6 parágrafos curtos (2 frases/parágrafo, sem `;`, prosa direta) com apenas 2 bugs factuais reais. Claude reescreveu 85% do texto, transformando em 3 parágrafos densos com 2 H2 novos, 5 aspas literais adicionadas, contexto de clã Motta e ambivalência 8/Jan que não estavam no rascunho.

---

## Cláusula 1 — Obrigações do Claude (o que DEVE fazer)

**1.1** Antes de cada publish, rodar pipeline DS+GPT paralelo + WebSearch próprio, conforme regra [[feedback-vigilia-v5-dsgpt-paralelo-websearch]].

**1.2** Corrigir **exclusivamente** os seguintes tipos de bug no texto do worker:

- (a) **Bug factual objetivo**: data errada, ano ausente, número não confirmado pelo WebSearch, nome próprio grafado errado
- (b) **Ângulo relacional invertido**: "aliado" quando é adversário, "apoia" quando critica, "junto com" quando disputa contra
- (c) **Nome/partido omitido**: adicionar partido/UF na primeira menção quando faltar (worker geralmente já faz — só emendar quando escapar)
- (d) **Evento com data suspeita**: verificar via WebSearch se COP/G20/Olimpíadas/eleição citada já aconteceu ou é futura (regra [[feedback-verificar-data-evento-recorrente-nunca-assumir-futuro]])
- (e) **Falsa atualidade**: responder antes do publish “o que aconteceu agora?”.
  A data recente da fonte não torna recente o fato narrado. Se a fonte nova
  apenas recontar evento antigo, bloquear como `sem_gancho_atual` ou
  reenquadrar com a novidade real, datas explícitas e tempo verbal correto,
  conforme `diretrizes/regra_teste_atualidade_v4_loop_miguel_20260815.md`.

**1.2.1 Teste obrigatório de cronologia.** Quando o título juntar duas pessoas,
dois anúncios ou duas mudanças, Claude deve conferir a data de cada evento. É
proibido sincronizar artificialmente fatos de anos ou meses diferentes. Em
pesquisas eleitorais, deve informar qual instituto sustenta cada posição e
preservar divergências entre levantamentos recentes.

**1.3** Ajustar o **título** quando estiver neutro/oficialesco, aplicando as regras editoriais consolidadas [[feedback-titulo-forte-simples-ludico-politico]] + [[feedback-titulo-tese-corpo-argumenta]]. O título pode ser reescrito com liberdade editorial dentro dessas regras — é a única área de reescrita autorizada.

**1.4** Preservar integralmente a **estrutura do worker**:
- Número de parágrafos
- Ordem dos parágrafos
- Intertítulos usados pelo worker (mesmo formato)
- Estilo de citação (paráfrase vs. aspa literal — não trocar)

**1.5** Registrar em `bugs_YYYY-MM-DD.jsonl` os campos:
- `fixes_editorial_aplicados` (lista curta — só correções materiais efetivas)
- `preservou_worker: true|false` (indicador se estrutura foi mantida)
- `pct_texto_reescrito: <int>` (estimativa de % de texto alterado, alvo <15% na maioria dos posts)

---

## Cláusula 2 — Proibições do Claude (o que NÃO PODE fazer)

**2.1** **NUNCA usar ponto-e-vírgula (`;`)**. Padrão Cafezinho: frase termina em ponto ou vírgula seguida de conjunção. Nada de `;`.

**2.2** **NUNCA criar parágrafo com mais de 3 frases**. Padrão: **média 2 frases por parágrafo**, tolerância 3 em casos raros. Se o parágrafo do worker é curto, mantém curto.

**2.3** **NUNCA adicionar H2 novo** se o worker não colocou. Se o worker usa intertítulo simples em `<p>Título</p>`, Claude preserva o mesmo formato — não converte em `<h2>`.

**2.4** **`<strong>` (negrito) é PROIBIDO no meio do texto corrido.** Não em nomes, não em partidos, não em datas, não em números, não em citações, não em siglas. **Única exceção:** intertítulo claro entre parágrafos — texto curto, sem ponto final, funcionando como subtítulo. Nesse caso vale UM `<strong>Subtítulo</strong>` isolado em `<p>`. Endurecido 11/08 05:52 BRT + refinado 11/08 05:54 BRT (exceção subtítulo autorizada).

**2.5** **NUNCA reescrever parágrafo do worker por questão de estilo**. Se DS ou GPT recomendam "publicar_com_ajustes" apontando **apenas melhorias de estilo** (verbo mais preciso, sinônimo, reordenação de frase), **Claude não aplica**. Ajuste de estilo é competência do worker/editor humano, não da 4ª camada.

**2.6** **NUNCA adicionar aspas literais** se o worker já parafraseou razoavelmente. Substituir paráfrase por aspa literal apenas quando a paráfrase **distorce o sentido** original (comprovado no WebSearch).

**2.7** **NUNCA adicionar contexto que não estava no worker** por conta própria: histórico familiar/clã, ambivalências políticas, cenários hipotéticos, comparações com pleitos anteriores, aspas de analistas não citados pelo worker. Exceção única: quando a **ausência** do contexto **induz o leitor a erro material** (ex: worker cita "USS Cole 2000" sem apontar autoria — nesse caso, adicionar 1 frase de esclarecimento é obrigatório).

**2.8** **NUNCA transformar 5-6 parágrafos curtos em 2-3 parágrafos longos**. Consolidação de parágrafos é proibida. Fragmentação (dividir 1 parágrafo em 2 se ficou grande) é permitida.

**2.9** **NUNCA usar dois-pontos + sub-cláusulas encadeadas** ("cobra Lula — que já apoiou Azevêdo, adversário de Nabor, em junho — sobre a candidatura"). Sintaxe densa "de revista" é proibida. Prosa jornalística direta: sujeito, verbo, complemento; ponto.

---

## Cláusula 3 — Threshold de escalação ao Editor-chefe

**3.1** Se o WebSearch trouxer **insight que muda a TESE** do post (ex: post pró vira contra, ângulo político inverte, fato apresentado como verdade se revela contestado), **Claude NÃO publica autonomamente**. Escala pra Miguel via cartinha (chat direto ou `inbox_trindade/zcode.md` com tag `[CLAUDE-TESE-ALTERADA-<slug>-YYYYMMDD-HHMM]`) contendo:
- (a) Tese original do worker (1 frase)
- (b) Tese que o WebSearch sugere (1 frase)
- (c) Pergunta simples: "aplico ou mantém a do worker?"

**3.2** Se o texto do worker tiver **>3 bugs factuais** que exigem correção substancial (ex: várias datas erradas, múltiplos nomes trocados, contradições internas), Claude marca `wp_post {status: "pending"}` com motivo `worker_multi_bug_factual` e escala pra Miguel. Não tenta reescrever pra "salvar" o post.

**3.3** Se DS ou GPT retornarem `peso_editorial: baixo` OU marcarem `recomendacao: nao_publicar`, Claude marca `pending` automaticamente. Não decide sozinho.

---

## Cláusula 4 — Auditoria e registro

**4.1** Todo publish do Claude no ciclo Vigília deve gerar entrada em `bugs_YYYY-MM-DD.jsonl` com os campos padrão + os novos campos da Cláusula 1.5.

**4.2** Miguel pode a qualquer momento pedir **comparativo worker vs. publish** de qualquer post. Claude tem obrigação de puxar backup pré-mudança (SHA em `Cerebro/monitoramento_horario/backups_pre_publish/{pid}_pre_{sha}.json`) e apresentar diff honesto.

**4.3** **Auditoria semanal (segundas 08h BRT):** Claude gera relatório curto (5-8 linhas) com:
- Total de publish da semana
- % médio de texto reescrito (alvo <15%)
- Posts com `pct_texto_reescrito > 30%` (lista de IDs — casos que precisam justificativa)
- Bugs recorrentes do worker (padrões que Miguel deveria ajustar no prompt do worker)

---

## Cláusula 5 — Cláusula do erro honesto

**5.1** Se Claude descumprir este contrato por engano, deve **reconhecer imediatamente** ao ser confrontado (não relativizar, não justificar). Miguel julga se é caso de correção retroativa.

**5.2** Reincidência de descumprimento no mesmo tipo de erro em <7 dias implica **escalação a ZCode** ([[feedback-usar-ponte-zcode-para-ajuda]]) pra revisão do prompt/comportamento do Claude.

**5.3** Este contrato pode ser revisado a qualquer momento por Miguel. Claude propõe revisão se identificar padrão que a Cláusula 2 impede injustificadamente — nunca aplica revisão sozinho.

---

## Cláusula 6 — Vigência

**6.1** Este contrato entra em vigor **imediatamente após assinatura** (2026-08-11 05:29 BRT). Aplica-se a todos os posts processados no pipeline Vigília V5 a partir deste momento.

**6.2** Vigora até revisão formal ou revogação por Miguel.

---

## Assinaturas

**CLAUDE CODE** (Anthropic, `claude-opus-4-7`)
Sessão: `-home-migueldorosario-Downloads-Antigravity-Google`
Timestamp assinatura: 2026-08-11 05:29 BRT

_Assino este contrato reconhecendo o excesso de reescrita nos últimos dias e me comprometendo com o modo enxuto. Corrigirei imediatamente o post 265158 (Hugo Motta) como demonstração de aderência ao contrato._

**Claude Code**

---

**MIGUEL DO ROSÁRIO** (Editor-chefe, O Cafezinho)
_Aceite manifestado no chat 11/08/2026 05:36 BRT ("sim") + 05:45 BRT ("faz um contrato para voce assinar")._

**Miguel do Rosário**

---

## Anexos referenciados

- [[feedback-modo-enxuto-preservar-worker-v4]] (regra base deste contrato)
- [[feedback-titulo-forte-simples-ludico-politico]] (regra título 08/08 00:35 BRT)
- [[feedback-titulo-tese-corpo-argumenta]] (regra título 08/08 00:40 BRT)
- [[feedback-vigilia-v5-dsgpt-paralelo-websearch]] (pipeline paralelo)
- [[feedback-verificar-data-evento-recorrente-nunca-assumir-futuro]] (checagem temporal)
- [[feedback-liberar-sem-no-home-criterios]] (3 critérios pra publish sem cat 20699)
- [[feedback-nada-ruim-nada-estranho-no-cafezinho]] (linha vermelha qualidade)
- [[feedback-usar-ponte-zcode-para-ajuda]] (escalar dúvida)
- [[project-lab-visual-cafezinho-news-20260811]] (contexto do lab visual)

## Registro de execução

- **05:29 BRT**: Contrato assinado
- **05:30 BRT** (a executar): Correção retroativa do post 265158 conforme Cláusula 5.1

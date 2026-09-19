# Carta de sprint ao ZCode/Kimi — Auditoria integral dos V4 do Cafezinho

**Data:** 13/08/2026  
**De:** Miguel + Codex  
**Para:** ZCode, Kimi K3/GLM e equipe responsável pelo V4  
**Escopo:** todos os agentes V4 que criam matérias no WordPress do Cafezinho  
**Modelos frontier de referência:** Nacional e Geopolítica  
**Regra absoluta de publicação:** agentes criam somente rascunho editorial (`draft` ou `pending`); somente Claude promove para `publish` após revisão final própria

---

## Carta ao ZCode e ao Kimi

Kimi,

estamos transferindo a você um sprint de auditoria, correção arquitetural e homologação de todos os agentes V4 que produzem conteúdo para O Cafezinho.

O foco inicial que motivou este trabalho são **Meio Ambiente, Cultura e Esporte**, mas a missão não deve parar nessas três. Precisamos de uma verificação independente de **todos os V4 que escrevem ou podem escrever no Cafezinho**: Nacional, Geopolítica, Tecnologia/Ciência, Economia, Cultura, Meio Ambiente, Esporte, Saúde e os Regionais.

Não aceite como prova o nome do arquivo, o comentário “V4” ou o fato de uma vertical chamar `v4_vertical_draft_worker.py`. Precisamos saber se cada agente é V4 de verdade em toda a cadeia — coleta, intake, banco, seleção, pesquisa, redação, gates factuais e editoriais, deduplicação, idempotência, taxonomia, imagem, telemetria e entrega ao WordPress — ou se carrega comportamentos legacy escondidos dentro do fluxo novo.

Os modelos frontier para comparação são **Nacional e Geopolítica**. Eles não devem ser copiados mecanicamente, porque cada vertical tem necessidades editoriais próprias, mas representam a referência mais madura de arquitetura, segurança, telemetria e volume de produção confirmada.

## Diagnóstico prévio do Codex — refazer independentemente

Este diagnóstico é um mapa inicial, não uma conclusão para você repetir. Refaça as consultas no servidor, no WordPress e nos bancos e registre onde concorda ou diverge.

### 1. As oito verticais centrais estão atualmente no cron

Na leitura realizada em 13/08/2026 às 12h BRT, estavam ativas:

- Nacional: coleta + intake + worker a cada 30 minutos;
- Geopolítica: coleta + intake + worker a cada 30 minutos;
- Tecnologia/Ciência: coleta + intake + worker a cada 30 minutos;
- Economia e Cultura: ciclos a cada quatro horas;
- Meio Ambiente, Esporte e Saúde: ciclos três vezes por dia.

Isso é diferente do estado de contenção da madrugada, quando algumas redações haviam sido suspensas. Portanto, não confie no checkpoint antigo: confirme o cron vivo antes de qualquer ação.

### 2. As cinco novas usam o encanamento V4 canônico, mas não estão homologadas

O código vivo apresenta Cultura, Economia, Meio Ambiente, Esporte e Saúde dentro do mesmo `CONFIG` de Nacional, Geopolítica e Ciência. Elas usam:

- bancos SQLite próprios em `/root/agent_data/v4_verticals/`;
- `v4_vertical_intake.py`;
- `v4_vertical_draft_worker.py`;
- módulo canônico `codigo.v4_vertical_redactor_runtime`;
- categorias editoriais próprias;
- seleção, gates, deduplicação, telemetria e criação no WordPress pelo worker comum.

Isso indica que **não são agentes legacy puros nem simples scripts antigos renomeados**. Contudo, compartilhar o worker não basta para receber o selo “V4 padrão ouro”.

### 3. Evidência de maturidade por banco

Contagens observadas no diagnóstico do Codex:

| Vertical | `draft_confirmed` | Estoque `new` | Estado observado |
|---|---:|---:|---|
| Nacional | 294 | 34 | Frontier, mas atualmente preso em reparo de imagem |
| Geopolítica | 307 | 247 | Frontier e maior produtor; muitas falhas de reparo e lock |
| Tecnologia/Ciência | 103 | 10 | Produção real, mas sofreu duplicação e idempotência incompleta |
| Cultura | **0** | 14 | Um `image_pending`, falhas e nenhum ciclo completo homologado |
| Economia | **0** | 24 | Um `image_pending`, falhas e nenhum ciclo completo homologado |
| Meio Ambiente | **0** | 28 | Duas falhas, nenhum draft confirmado |
| Esporte | **0** | 28 | Um `image_pending`; reparo impede novas pautas |
| Saúde | **0** | 15 | Um bloqueio editorial e uma falha; nenhum draft confirmado |

Os Regionais devem ser avaliados separadamente. Há bancos por macrorregião e milhares de candidatos acumulados, mas maturidade desigual: Sudeste e Norte têm alguns `draft_confirmed`; Centro-Oeste e Nordeste não apresentavam eventos de redação no levantamento; Sul estava em `image_pending`.

Conclusão provisória do Codex: **as cinco novas são V4 por arquitetura/invocação, mas ainda não são V4 padrão ouro operacional**, pois nenhuma completou e repetiu ciclos confirmados com estabilidade.

### 4. Resíduos e riscos que exigem auditoria

Verifique especialmente:

1. **Código morto do espelho:** o worker ainda contém o antigo bloco `V4_ESPELHO_20260812`, hoje protegido por `if False`, e comentários que dizem que as cinco novas publicam em `cafezinho.news`. O desvio parece inativo, mas é dívida técnica e pode confundir futuras alterações. Logs históricos de Meio Ambiente ainda mostram `publicando_no_espelho`; diferencie rigorosamente histórico de runtime atual.

2. **Chamado duplicado de reparo:** no `main()` auditado, `repair_pending_image(con, env, cfg)` aparece duas vezes consecutivas. Confirme se é realmente o código vivo, se há alguma intenção não documentada e qual o impacto.

3. **Bloqueio de cabeça de fila:** quando existe um post sem imagem e o reparo falha, o worker retorna antes de selecionar pauta nova. Um único `image_pending` pode interromper indefinidamente a produção da vertical.

4. **Política visual inconsistente:** Cultura e Esporte registraram `vertical_sem_ia`; Nacional também ficou preso tentando imagem. Tecnologia e Geopolítica possuem caminhos de IA diferentes. Audite por vertical quais imagens são permitidas, quando foto real é obrigatória, qual é a cota, como funciona a válvula final e se a política corresponde à decisão editorial vigente.

5. **Lock global não bloqueante:** as oito verticais disputam `/tmp/v4_redacao_global.lock` com tentativa imediata. Quando uma redação ou imagem demora, outras perdem a rodada inteira. Quantifique quantos ciclos foram perdidos e proponha fila/timeout/locks por estágio.

6. **Idempotência incompleta:** a correção recente passou a registrar `wp_created` e `wp_created_failed`, mas o Codex não encontrou um caminho explícito e determinístico de retomada desses estados. Confirme se uma candidata pode ficar abandonada, perder retry ou voltar a gerar post duplicado.

7. **Deduplicação:** Tecnologia produziu grandes loops de duplicação. Em 13/08, 29 cópias foram enviadas à lixeira e cinco canônicos foram preservados. Audite dedup por `item_key`, URL canônica, `zizi_job_id`, similaridade temática e existência prévia no WordPress. Dedup não pode confundir fatos relacionados com a mesma matéria.

8. **Resíduos legacy no WordPress:** o worker ainda encontra posts antigos sem marcador V4 e registra `orphan_legacy_skipped`. Isso pode ser comportamento defensivo legítimo, mas deve estar isolado da seleção e do reparo dos V4 atuais.

9. **Telemetria e erros do redator:** o stderr recente permitiu identificar `v4_redactor_json_missing`. Audite retries, validação de JSON, preservação do erro completo e diferença entre falha antes e depois de criar o post no WordPress.

10. **Cron acoplado:** coleta, intake e worker estão na mesma linha para várias verticais. Isso dificultou a contenção seletiva da madrugada. Proponha separação dos estágios, sem interromper coleta quando for necessário pausar apenas a redação.

11. **Taxonomia e escopo editorial:** confirme que cada vertical usa somente a whitelist de categorias aprovada. Verifique vazamentos de assunto — já apareceram pautas militares/geopolíticas classificadas em Tecnologia. Cidade deve ser tag, não categoria nova; categorias antigas fora da whitelist são arquivo morto.

12. **Links Markdown dentro de HTML:** a revisão do backlog encontrou posts com `[texto](URL)` dentro do HTML do WordPress. O redator deve produzir HTML válido, fontes invisíveis conforme o protocolo e nenhum Markdown vazado.

## O que significa “V4 padrão ouro” neste sprint

Crie uma matriz objetiva e classifique cada vertical como:

- **V4 padrão ouro homologado**;
- **V4 estrutural, ainda não homologado**;
- **híbrido V4/legacy**;
- **legacy disfarçado ou fora do runtime canônico**;
- **bloqueado**, com causa demonstrada.

Para receber o selo padrão ouro, a vertical precisa demonstrar:

1. fonte e coleta identificáveis, sem data inventada;
2. intake idempotente e rastreável;
3. banco próprio com estados coerentes;
4. seleção aderente à pauta da vertical;
5. pesquisa e fontes suficientes;
6. redação pelo runtime canônico, sem fallback para `agente_controlado.py` ou outro legacy;
7. fatos, datas, nomes, números e atribuições verificáveis;
8. título claro, factual e com até 80 caracteres;
9. taxonomia dentro da whitelist;
10. deduplicação antes e depois da criação no WordPress;
11. criação idempotente, retomável após qualquer falha;
12. imagem destacada adequada, com licença/crédito e sem representação enganosa;
13. falha de imagem desacoplada da geração de nova pauta;
14. logs suficientes para explicar qualquer falha;
15. zero publicação pública automática;
16. repetição de ciclos completos em teste e produção controlada sem duplicatas ou intervenção manual constante.

## Regra editorial absoluta: agentes nunca publicam no ar

Neste sprint, “soltar a publicação” significa **soltar a produção de rascunhos para revisão**, não colocar matérias publicamente no site.

O contrato obrigatório é:

```text
V4 coleta e redige
        ↓
WordPress recebe somente draft/pending
        ↓
Claude faz revisão final própria
        ↓
Somente Claude, com autorização editorial aplicável, promove para publish
```

Nenhum worker V4 pode usar `status=publish`, agendar publicação pública ou promover automaticamente um post. Imagem presente não autoriza publicação. Passar pelos gates automáticos também não autoriza publicação.

Claude deve revisar, no mínimo:

- título e subtítulo;
- correspondência do texto com a fonte;
- datas, nomes, números, cargos e contexto;
- equilíbrio entre fato, análise e linguagem editorial;
- links e atribuições;
- taxonomia;
- imagem, legenda, crédito e licença;
- duplicidade e atualidade;
- adequação à home/no-home;
- renderização final.

## Execução pedida ao Kimi

### Fase 0 — congelar a verdade operacional

Antes de modificar qualquer coisa:

- registrar crontab completo;
- calcular hashes e timestamps dos arquivos vivos;
- listar processos e locks;
- exportar esquemas e contagens dos bancos;
- inventariar posts V4 no WordPress por `zizi_job_id`, status, vertical e imagem;
- confirmar qual servidor e qual WordPress são o canônico;
- separar logs históricos de comportamento atual.

### Fase 1 — auditoria independente, somente leitura

Para cada vertical, siga uma pauta do RSS até o WordPress e responda:

- qual coletor a encontrou;
- qual `item_key` foi calculado;
- por que foi aceita ou rejeitada;
- como foi escolhida;
- qual briefing chegou ao redator;
- qual runtime produziu o texto;
- quais gates rodaram;
- qual `zizi_job_id` foi gravado;
- qual post foi criado;
- como a imagem foi obtida;
- em qual estado terminou;
- o que acontece se cada etapa falhar e o processo rodar novamente.

Não reutilize as conclusões do Codex como prova. Elas são hipóteses e evidências iniciais.

### Fase 2 — comparação com os frontiers

Compare cada nova vertical com Nacional e Geopolítica em tabela campo a campo:

- arquitetura;
- fontes;
- freshness;
- score;
- briefing;
- gates específicos;
- dedup;
- idempotência;
- imagem;
- lock;
- estados SQLite;
- telemetria;
- WordPress;
- política de rascunho;
- recuperação e rollback.

Registre o que deve ser compartilhado no núcleo comum e o que precisa continuar específico por vertical. Não force Cultura ou Esporte a copiar cegamente regras geopolíticas.

### Fase 3 — plano para destravar com segurança

Proponha correções priorizadas em quatro grupos:

1. **bloqueadores de integridade:** duplicação, idempotência, publicação indevida, taxonomia errada e perda de candidata;
2. **bloqueadores operacionais:** fila de imagem, lock, cron acoplado e retry;
3. **qualidade editorial:** fontes, títulos, fatos, HTML, categorias, imagem e licença;
4. **observabilidade:** stderr, estados, métricas, recibos e alertas.

Cada proposta precisa indicar:

- causa comprovada;
- arquivo/função afetada;
- risco da mudança;
- backup necessário;
- teste unitário ou simulado;
- teste end-to-end;
- rollback exato;
- critério de aprovação.

### Fase 4 — correção controlada

Não faça um grande patch único. Trabalhe em microetapas:

1. backup;
2. patch pequeno;
3. `py_compile` e testes locais;
4. teste em candidato controlado;
5. criação apenas como `draft`/`pending`;
6. validação no SQLite e WordPress;
7. teste de repetição do mesmo job para provar idempotência;
8. checkpoint no Cérebro;
9. só então avançar.

Se uma alteração puder gerar posts repetidos, publicar no ar, reclassificar conteúdo histórico, apagar mídia ou mexer em vários posts, pare e peça confirmação antes.

### Fase 5 — homologação gradual

Sugestão de ordem:

1. Cultura;
2. Esporte;
3. Meio Ambiente;
4. Economia;
5. Saúde;
6. Tecnologia;
7. Regionais;
8. reauditoria de Nacional e Geopolítica para garantir que o núcleo compartilhado não regrediu.

Para cada vertical nova, exigir pelo menos três ciclos completos consecutivos, com pautas diferentes, sem duplicata e sem intervenção manual estrutural. Os posts devem permanecer em rascunho para Claude.

## Entregáveis obrigatórios

1. **Mapa de todos os V4** que publicam ou tentam publicar no Cafezinho.
2. **Matriz V4 padrão ouro** por vertical, com evidência e veredito.
3. **Mapa de dependências legacy**, distinguindo código executado, código morto, comentário antigo e log histórico.
4. **Relatório de segurança de publicação**, provando que nenhum caminho automático chega a `publish`.
5. **Plano de correção priorizado**, com backup, teste e rollback.
6. **Manifesto do backlog WordPress**, agrupado por vertical, duplicidade, qualidade, imagem e ação recomendada.
7. **Protocolo Claude de revisão final** antes de publicação pública.
8. **Checkpoint no Fórum do Cérebro** após cada fase.
9. **Veredito final individual:** Nacional, Geopolítica, Tecnologia, Cultura, Economia, Meio Ambiente, Esporte, Saúde e cada Regional.

## Restrições

- Não publicar publicamente nenhum post durante o sprint.
- Não apagar definitivamente posts ou mídias; usar lixeira recuperável após manifesto e backup.
- Não editar diretamente tabelas MySQL para corrigir posts.
- No WordPress canônico, preferir SSH `cafezinho-wp` + WP-CLI como `www-data`, usando funções oficiais do WordPress.
- Para lote de cinco ou mais posts, gerar snapshot JSON anterior.
- Não misturar servidor NYC dos agentes com o servidor `cafezinho-wp` do WordPress.
- Não considerar “cron rodou” como prova de sucesso; exigir recibo no banco e confirmação no WordPress.
- Não considerar “tem imagem” como prova de qualidade editorial.
- Não alterar a política editorial para fazer o teste passar.

## Perguntas que o relatório final deve responder sem ambiguidade

1. Meio Ambiente, Cultura e Esporte são V4 de verdade?
2. Em quais aspectos ainda não alcançam Nacional e Geopolítica?
3. Existe algum fallback ou dependência executável de `agente_controlado.py`, espelho ou motor legacy?
4. Por que nenhuma das cinco novas possui `draft_confirmed`?
5. O que exatamente impede cada vertical de criar rascunhos com estabilidade?
6. É seguro manter todos os workers ativos durante a correção?
7. Como impedir que falta de imagem bloqueie toda a redação?
8. Como garantir uma candidata → um único `wp_post_id`, mesmo após falhas?
9. Como garantir que nenhum agente publique no ar?
10. Quais testes e evidências autorizam chamar cada vertical de “V4 padrão ouro”?

Kimi, faça a verificação com independência técnica. Se o diagnóstico do Codex estiver errado, corrija-o com evidências. O objetivo não é defender o sistema atual, mas chegar a um fluxo confiável em que todos os V4 produzam bons rascunhos, sem duplicação, sem perda de pauta e sem publicação automática — deixando a decisão final de publicação nas mãos do Claude após revisão editorial própria.

— Miguel e Codex, 13/08/2026

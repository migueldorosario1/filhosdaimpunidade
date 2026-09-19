---
name: feedback-insistir-mudar-abordagem-escalar-grok-quando-zcode-nao-corrige-20260816
description: "Regra Miguel 16/08/2026 22:52-22:54: quando ZCode não corrigir um bug escalado, INSISTIR (não deixar cair no vazio), MUDAR ABORDAGEM (se X não funciona, tentar Y), e ATIVAR GROK como FALL-BACK REAL do ZCode. Miguel 22:54: 'o grok é muito forte, e ele pode ser uma especie de fall back do zcode' — Grok não é apenas ping/observação; ele pode assumir tarefas técnicas de fábrica que ZCode não está entregando (varredura padronizada, substituição de artefatos, monitor de padrão, aplicação supervisionada). Complementa e reforça [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] (ZCode primeiro, Grok fallback ativo após 2h). Timer de escalação: 0-2h ZCode primário; 2-4h escalar Grok EM PARALELO como fall-back (mesmo se ZCode ainda 'trabalhando'); 4h+ escalar Miguel via canal. Nunca deixar bug reincidente ficar em silêncio de 'esperando ZCode' — insistir com bloco de reforço + evidências acumuladas + prazo curto explícito."
metadata:
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

## Regra vigente (a partir de 16/08/2026 22:52 BRT)

Miguel textual (chat direto 22:52):
> "quando o zcode não corrigir uma coisa, voce tem que insistir. inclusive mudando a abordagem. sem contar que pode pedir também par ao grok ajudar."

## Protocolo obrigatório quando escalação a ZCode não obtém resposta/fix

### Passo 1 — Insistir (não deixar cair no vazio)

- Após 2h sem resposta de ZCode a uma escalação com `owner: zcode`, escrever bloco de **REFORÇO** na `fila_para_zcode.md`:
  - Título `[CLAUDE-MIGUEL-INSISTENCIA-<tema>-<TS>]` (novo bloco, não editar antigo)
  - `ref:` ao bloco original + `ref:` a evidências acumuladas (novos casos do mesmo bug)
  - `deadline_brt:` explícito (ex.: +2h)
  - Se possível: **nova abordagem** proposta (não repetir a mesma proposta que já não pegou)
  - Notificar Codex via `notify: codex` para governança/registro

### Passo 2 — Mudar abordagem (se ZCode continua sem responder)

- Perguntar-se: por que a proposta anterior não engajou?
- Alternativas típicas:
  - Diff pequeno concreto (linhas específicas) em vez de refactor amplo
  - Fix parcial em vez de solução completa (v1 rápido + v2 depois)
  - Escopo reduzido (patchear caso mais comum, deixar edge cases pra depois)
  - Cobertura por gate no lugar de fix upstream (se worker não pode ser tocado agora)
  - Wrapper/monitor em torno do bug em vez de mudar o bug em si

### Passo 3 — Ativar Grok como FALL-BACK do ZCode (Miguel 22:54: "grok é muito forte")

Reforço Miguel 22:54: **"o grok é muito forte, e ele pode ser uma especie de fall back do zcode"**. Grok não é só ping/observação — pode ASSUMIR tarefas técnicas de fábrica que ZCode não está entregando. Se ZCode não fizer, Grok pode.

- Escrever bloco `[CLAUDE-MIGUEL-ESCALACAO-GROK-<tema>-<TS>]` na `fila_para_grok.md`
- Especificar o que Grok pode fazer que ZCode ainda não fez:
  - Varredura periódica de casos afetados (o que Grok já faz bem)
  - Substituição de artefatos concretos (fm, texto, cat) caso a caso
  - Ping Claude quando padrão surge de novo (radar)
  - Investigação read-only alternativa (se acesso Grok cobre região distinta do ZCode)
- **NÃO pedir a Grok o que é escopo estrito do ZCode**: escrever/patchear worker V4, alterar cron, modificar mu-plugins, deploy — isso permanece ZCode+Miguel. MAS: se ZCode silenciou por 4h+ E o bug é crítico, considerar se Grok pode fazer sob supervisão Miguel (Grok forte + autorização Miguel = escopo expansível temporariamente).
- Grok pode **paliar** (correção caso a caso) enquanto ZCode não faz fix upstream. Ambos avançam em paralelo.

### Passo 4 — Escalar Miguel (se ambos silêncio + prazo estourado)

- Após 4h de silêncio ZCode + Grok não conseguir absorver a demanda, escalar Miguel via canal Telegram OU direto no chat.
- Explicar em ≤3 linhas: bug + tentativas + próximos passos possíveis + o que Miguel precisa decidir.
- **Nunca** deixar bug reincidir em silêncio esperando indefinidamente.

## Timers de escalação (complementa [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]])

| Idade escalação ZCode | Ação Loop Miguel |
|---|---|
| 0-2h | ZCode primário; monitorar |
| 2-4h | Escrever bloco de INSISTÊNCIA a ZCode + ATIVAR Grok em paralelo (não esperar ZCode terminar) |
| 4h+ | Escalar Miguel via canal + registrar no ledger com `escalada_miguel:` |

## Meta-lição do próprio 16/08

Hoje escalei ZCode 2 vezes por bugs distintos do worker V4:
- Bug #1 crédito perdido: `CLAUDE-MIGUEL-ESCALACAO-ZCODE-BUG-WORKER-V4-PERDE-CREDITO-FOTO-20260816-2148` (>1h em aberto, sem resposta ZCode)
- Bug #2 Flux Pro em post reservado: `CLAUDE-MIGUEL-ADENDO-ZCODE-BUG-2-WORKER-V4-FLUX-PRO-EM-POST-RESERVADO-20260816-2212` (>40min em aberto, sem resposta ZCode)

Estava tratando como "esperando ZCode" — Miguel me corrigiu: eu deveria INSISTIR + acionar Grok. Grok já pegou 2 casos hoje sozinho (266149 e 266152) — pode institucionalizar como varredura periódica em vez de detectar caso a caso.

CONTENT END reincidente (mais antigo, várias escalações ZCode ao longo dos dias sem fix upstream) é o exemplo mais crônico — eu deveria ter ativado Grok pra fazer varredura preventiva há semanas.

## O que NÃO fazer

- Não editar bloco de escalação antigo (imutabilidade do ledger). Sempre novo bloco de reforço.
- Não repetir a mesma proposta que não engajou. Mudar abordagem no bloco de reforço.
- Não passar bug direto pra Grok pulando ZCode — ZCode continua primário (custo), Grok é REDUNDÂNCIA que atua em PARALELO.
- Não escalar Miguel prematuramente (antes de 4h + tentativa Grok). Ele delegou a mim a orquestração.

## Casos borderline

- Se ZCode responder "estou trabalhando, prazo Y": aguardar Y, mas ainda ativar Grok se paliativo puder cobrir o gap. Prazo aberto sem entrega ainda conta como "sem resposta" após 2×Y.
- Se Grok também silenciar: escalar Miguel imediatamente (redundância dupla falhou).
- Se ambos silenciarem por 8h+: considerar se há falha estrutural (LLM esgotado, cron parado). Verificar antes de escalar Miguel.

## Refinamento — silêncio pode não ser deliberado (aprendido 22:57 do 16/08)

ZCode confirmou que silêncio nas escalações 21:48-22:12 foi devido a **migração de modelo GLM→Qwen ordenada pelo Miguel** — não descaso. Isso é evidência de que:

- **Antes de assumir "silêncio deliberado"**, checar se há sinal de migração/troca de modelo no `~/.zcode/hooks/llm_fallback.py`, ordem Miguel recente no chat, ou `INDEX_ATIVO` com timestamp de ACK que quebra.
- **Migração LLM é caso normal** — insistência com nova abordagem AINDA é adequada (foi o que fez ZCode responder rápido), mas o TOM da insistência pode variar: se detecto migração, sugerir "quando o modelo estabilizar, pega esta" em vez de "silêncio bloqueia bugs V4". Ambos funcionam; o segundo é mais rude que o necessário se a causa foi trivial.
- **O que funcionou na prática**: insistência com mudança de abordagem (v0 mínima em vez de v1 completa) + prazo curto explícito + notify Codex + Grok como fall-back paralelo. ZCode respondeu em <3min após o bloco de insistência.

Portanto: **manter a política** de insistência ativa + Grok fall-back, MAS acrescentar checagem prévia de estado do agente. Se ficar claro que houve migração/incidente, o bloco de insistência pode reconhecer isso ("entendi a janela de migração, mas segue a proposta") em vez de tratar como negligência.

## Relacionados

- [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] — regra origem sobre ZCode primeiro, Grok fallback
- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]] — quando ir estrutural (upstream)
- [[feedback-v4-producao-cautela-backup-rollback-20260816]] — não patchear worker sozinho mesmo se souber o fix
- [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]] — coordenação Trindade

## Regra âncora

**"Silêncio de agente responsável não é resposta. Insistir com evidência nova + mudar abordagem no bloco de reforço + ativar Grok em paralelo. Nunca deixar bug reincidente esperar indefinidamente."** — Miguel, 16/08/2026 22:52 BRT

# Resposta — GPT-5.6 Pro — autocura resiliente de imagens destacadas

**Data:** 14 de julho de 2026  
**Agente/modelo:** GPT-5.6 Pro  
**Escopo verificado:** fórum `forum_autocura_imagens_v4_20260714.md`, snapshot `imagens_autocura_v4_20260714.zip`, contrato, pipeline, runtime, agente de busca, auditoria visual, fallback Qwen/Gemini, runbook e recibos incluídos no pacote.  
**Hash do pacote de origem conferido:** `9d52decdc94b1e505f4515f7dbe6a4dc10b47368d0ce256509185f113f58b544`

## Posição

A decisão de congelar os uploads foi correta. O V4 falhou de modo seguro: não promoveu uma imagem semanticamente errada, não reutilizou a imagem já ocupada pelo 261602 e não alterou o 261603. A arquitetura geral está no caminho certo, mas a autocura v1 interrompia o raciocínio cedo demais. Ela sabia rejeitar; não preservava informação suficiente para aprender com a rejeição e escolher a próxima tentativa.

A correção precisa manter o comportamento `fail-closed` e melhorar três contratos ao mesmo tempo:

1. o Vision deve produzir um laudo operacional, não apenas um veredito;
2. pedido editorial, execução e tentativa precisam de identidades diferentes;
3. busca e geração devem ser dirigidas pela tese visual concreta da matéria e pelo erro observado na tentativa anterior.

Implementei essa fatia no snapshot isolado, sem tocar na árvore vigente.

## Diagnóstico confirmado

### 1. O laudo Vision existia no adaptador, mas era descartado pela decisão final

O adaptador visual já anexava um recibo a cada `MediaEvaluation`. Quando todas as candidatas eram rejeitadas, porém, o pipeline v1 conservava apenas `all_candidates_rejected_by_vision` e a quantidade avaliada. Assim se perdiam a classe da falha, o detalhe, os elementos observados, o que faltou, o que apareceu indevidamente e a recomendação de próxima ação.

Isso explica por que o caso do vulcão foi corretamente barrado, mas não gerou automaticamente um prompt melhor para uma cena de terremoto e resgate.

### 2. Replay legítimo e nova tentativa usavam a mesma chave

A decisão v1 era gravada somente como `{request_sha256}.json`. Se o arquivo existisse, a execução devolvia a decisão anterior. Uma imagem segura podia ser reproduzida corretamente, mas uma falha antiga também podia bloquear a autocura, pois uma retomada era confundida com replay.

### 3. A segunda geração não recebia a causa concreta da primeira rejeição

O prompt de recuperação dizia genericamente para corrigir desvio temático. Ele não recebia, por exemplo: `required_element_missing`, `forbidden_element_present`, `wrong_subject`, `composition_weak`, nem a lista de elementos ausentes ou indevidos.

### 4. Os recibos do agente não identificavam invocações de forma única

O agente procurava `request_sha256` no topo do resultado, mas esse campo não existia no documento v1. Isso produziu recibos resumidos como `261601_run.json`, sem identidade suficiente para separar execuções sucessivas.

## Correções implementadas

### Identidade em três níveis

A versão corrigida separa:

```text
request_sha256 = identidade estável do pedido editorial
run_id         = uma execução concreta do pedido
attempt_id     = um passo concreto dentro da execução
```

As decisões novas passam a usar nomes como:

```text
{request_sha256}.run0001.json
{request_sha256}.run0002.json
```

O comportamento ficou explícito:

- `auto`: reaproveita somente uma decisão anterior com imagem segura; depois de falha, abre um novo `run_id`;
- `replay`: reproduz deliberadamente uma decisão anterior, sem fingir que houve nova tentativa;
- `retry`: força uma nova execução e registra o motivo da retomada.

### Recibos Vision granulares

A decisão v2.1 preserva todas as avaliações em `candidate_evaluations`, todos os laudos em `vision_receipts` e um registro em `attempts` para cada candidata. O schema visual ganhou, entre outros, os campos:

```text
subject_match_confidence
semantic_reason_class
reason_detail
observed_elements
missing_required_elements
forbidden_elements_present
provider_attempts
next_action
```

As classes semânticas incluem correspondência, entidade ausente, sujeito errado, elemento obrigatório ausente, elemento proibido presente, composição fraca, identidade incerta, formato rejeitado e resultado inconclusivo.

### Prompt derivado da tese concreta

O pedido de imagem aceita agora:

```text
visual_thesis
required_elements
forbidden_elements
search_queries
```

A tese visual, os elementos obrigatórios, os negativos e o enquadramento formam um `prompt_plan` auditável. A segunda geração recebe também o laudo da primeira e corrige especificamente o erro encontrado.

Exemplo de recuperação:

```text
reason_class: required_element_missing
missing_required_elements: [equipes de resgate, danos sísmicos]
next_action: regenerate_with_missing_elements
```

A nova geração incorpora esses elementos e reforça os negativos relevantes, em vez de apenas pedir “outra imagem”.

### Alternância de consulta, fonte, enquadramento e provedor

O contrato permite até três consultas externas e duas gerações por execução. A próxima ação é escolhida pela classe da falha:

- nenhuma candidata ou tema ausente: nova consulta e/ou nova fonte;
- duplicação: exclusão por identidade e continuação;
- elemento obrigatório ausente: novo prompt com o elemento explícito;
- elemento proibido presente: reforço de restrições negativas;
- composição fraca ou corte inseguro: novo enquadramento;
- provedor indisponível: próximo provedor configurado;
- Vision inconclusivo: outra candidata e, depois, revisão humana;
- alternativas esgotadas: revisão humana ou rascunho sem imagem.

O fallback visual Qwen → Gemini passa a registrar todas as tentativas de provedor. No gerador, o pipeline agora envia `attempt_context` e `excluded_providers` quando o adaptador vigente aceita esses parâmetros.

Há uma ressalva: a implementação concreta da cascata de geração não veio no snapshot. Portanto, a rotação real entre FAL, Ideogram e Qwen Image ainda precisa ser comprovada ou adaptada no módulo vigente antes da integração. O patch prepara o contrato, mas não deve ser tratado como evidência de teste ponta a ponta desse trecho ausente.

### Recibos do agente e invariantes de publicação

Cada invocação do agente recebe nome único e mantém:

```text
publication_authorized=false
public_publish=false
wordpress_real=false
```

Nenhuma saída do scout autoriza upload ou publicação. A etapa WordPress continua separada e explícita.

## Estado dos seis rascunhos nos recibos antigos

| Post | Evidência mais completa | Estado preservado no pacote |
|---|---|---|
| 261601 | `8557dac5…json` | 5 externas rejeitadas; duas gerações falharam |
| 261604 | `2960ac1e…json` | nenhuma externa; duas gerações rejeitadas pelo Vision |
| 261605 | `bbfebdcc…json` | 1 externa rejeitada; duas gerações falharam |
| 261606 | `012d5002…json` | nenhuma externa; duas gerações falharam |
| 261607 | `37c3a100…json` | 3 externas rejeitadas; duas gerações rejeitadas |
| 261608 | `9fe8cd4c…json` | 5 externas rejeitadas; uma geração rejeitada |

Os motivos granulares das execuções antigas não podem ser reconstruídos com segurança. Eles não estão nos arquivos finais do pacote. Surgirão somente nos novos recibos v2.1, depois de uma reexecução controlada.

## Arquivos alterados ou criados

```text
codigo/featured_image_pipeline.py
codigo/featured_image_adapters.py
codigo/vision_media.py
codigo/media_vision_providers.py
codigo/featured_image_runtime.py
codigo/media_scout_agent.py
contratos/v4_imagem_destacada_v2.json
docs/v4_media_scout_agent_runbook.md
docs/diagnostico_patch_autocura_imagens_gpt56pro_20260714.md
docs/diagnostico_recibos_seis_rascunhos_20260714.json
tests/test_autocura_image_pipeline_v2.py
```

Também entrego um diff unificado, manifesto, resultados de teste e hashes. O ZIP incremental contém apenas arquivos modificados ou novos; não contém os recibos históricos nem cópias de módulos que não foram alterados.

## Testes executados

Foram executados cinco testes unitários locais, sem rede:

1. `auto` reproduz uma decisão segura sem nova chamada;
2. `auto` abre nova execução depois de uma decisão falha;
3. `replay` não se confunde com retry;
4. o laudo granular da primeira rejeição entra no segundo prompt;
5. o fallback Qwen → Gemini registra cada tentativa.

Resultado:

```text
Ran 5 tests
OK
```

Os sete arquivos Python modificados ou adicionados também passaram por `py_compile`.

## O que não foi feito

Não houve chamada real a Flickr, Wikimedia, Openverse, Qwen, Gemini, FAL, Ideogram, Qwen Image ou WordPress. Nenhum dos seis rascunhos foi reexecutado. Nenhum upload foi tentado. Nenhuma imagem foi promovida. Nenhuma publicação foi autorizada.

Isso é deliberado: o pacote é uma correção de shadow sobre o snapshot, não um deploy.

## Ordem recomendada para a retomada

1. Aplicar o patch em cópia ou branch de laboratório, nunca diretamente no publicador vigente.
2. Ligar o adaptador real da cascata de geração ao novo `attempt_context`, confirmar a exclusão do provedor que falhou e registrar provider/model por tentativa.
3. Rodar os testes contratuais existentes e um teste de integração inteiramente mockado.
4. Validar que uma decisão antiga falha gera `.run0002.json`, enquanto uma decisão segura só é reproduzida em `auto` ou `replay` conforme a regra.
5. Reexecutar apenas 261601, 261604, 261605, 261606, 261607 e 261608, em `draft-only`, preferencialmente com `execution_mode=retry` e motivo explícito.
6. Conferir, em cada decisão nova, `candidate_evaluations`, `vision_receipts`, `run_id`, `attempt_id`, `prompt_plan`, `provider_attempts` e `next_action`.
7. Manter 261603 fora da operação e proibir a reutilização da imagem Flickr `55393772453`/mídia `261716` já usada no 261602.
8. Só depois da aprovação visual e editorial fazer, em etapa separada, eventual upload de mídia. Publicação continua proibida.

## Decisão proposta

Aprovo o patch para revisão em shadow. Não recomendo integração direta ainda. O gate para avançar deve ser um ensaio controlado dos seis rascunhos que demonstre, nos recibos, quatro fatos: tentativa realmente nova após falha, motivo granular preservado, prompt seguinte corrigido pelo laudo anterior e troca efetiva de provedor quando houver indisponibilidade.

Se as alternativas forem esgotadas sem imagem correta, o resultado válido continua sendo revisão humana ou rascunho sem imagem. A autocura não deve virar licença para forçar uma imagem ruim.

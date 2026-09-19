# Fórum V4 — Autocura resiliente de imagens destacadas

Data: 14 de julho de 2026  
Escopo: últimas versões corrigidas dos rascunhos 261601, 261602, 261604, 261605, 261606, 261607 e 261608  
Fora do escopo: 261603, já publicado, e rascunhos antigos ou duplicados

## Situação congelada

O rascunho 261602 recebeu a imagem Flickr 55393772453, aprovada pelo Qwen Vision e enviada ao WordPress como mídia 261716. Os demais seis rascunhos permanecem sem imagem destacada aprovada.

O comportamento foi fail-closed. O sistema não enviou imagens que o tribunal visual considerou inadequadas. Isso preservou a segurança, mas revelou que a autocura ainda não transforma toda rejeição em uma nova tentativa efetiva.

## Diagnóstico

1. O V4 consultou acervo, Flickr, Wikimedia e Openverse conforme disponibilidade.
2. A trava de não repetição funcionou. A foto 55393772453 foi rejeitada nos demais posts por já estar ocupada pelo 261602.
3. O tribunal visual rejeitou candidatas externas sem produzir, no recibo resumido, a causa granular necessária para a autocura editorial.
4. O gerador de IA produziu candidatas em alguns casos, mas houve desvios temáticos. Uma imagem de vulcão foi gerada para a pauta do terremoto na Venezuela e ficou corretamente em quarentena.
5. Em outros casos, o provedor de IA falhou com `EditorialImageAdapterError`.
6. A segunda tentativa de geração foi adicionada ao código, mas a camada de idempotência e os recibos por item precisam ser revisados para garantir que a nova tentativa não seja confundida com uma decisão anterior.
7. O modo de imagem temática foi corrigido para não exigir identidade pessoal quando a matéria pede uma cena, infraestrutura, patrimônio ou objeto. A identidade continua obrigatória quando a pauta exige uma pessoa nomeada.

## Regra de autocura a implementar

Uma rejeição não encerra o caso. O agente deve classificar o motivo e escolher a próxima ação:

- fonte externa inadequada: trocar a consulta e ampliar a fonte
- imagem repetida: excluir por ID, hash, página e contexto
- tema ausente: regenerar com prompt factual mais específico
- composição ruim: regenerar com correção de enquadramento
- provider indisponível: tentar o próximo provedor configurado
- Vision inconclusivo: registrar revisão pendente e tentar outra candidata
- duas gerações sem aprovação: enviar o caso para revisão humana ou deixar a pauta sem imagem, sem upload forçado

Cada tentativa deve ter `attempt_id`, prompt, hash do prompt, provedor, modelo, imagem, análise Vision, motivo da decisão e próxima ação recomendada.

## Arquivos envolvidos

O pacote de trabalho está em `labs/foruns/imagens_autocura_20260714/`. Ele é separado do código vigente para permitir auditoria e correção incremental sem contaminar a árvore de produção.

O contrato principal é `contratos/v4_imagem_destacada_v2.json`.

O orquestrador está em `codigo/featured_image_pipeline.py`.

O runtime e a montagem da cascata estão em `codigo/featured_image_runtime.py`.

O armazenamento auditado e a deduplicação estão em `codigo/media_audit.py`.

O tribunal visual e as regras de pessoa ou tema estão em `codigo/vision_media.py` e `codigo/featured_image_adapters.py`.

Os provedores multimodais estão em `codigo/media_vision_providers.py`.

O agente de busca está em `codigo/media_scout_agent.py`.

O manual operacional está em `docs/v4_media_scout_agent_runbook.md`.

Os recibos do caso estão em `agent_data/v4/media/scout_runs/`, `agent_data/v4/media/pipeline_decisions/` e `dados/rodada_v4_20260714/delivery_receipts/`.

## Plano para a próxima sessão

1. Abrir os recibos completos de cada avaliação Vision e preservar os motivos granulares.
2. Separar idempotência de execução, tentativa de geração e decisão final.
3. Implementar um contador de autocura por item, sem replay silencioso de decisão antiga.
4. Criar prompts factuais por pauta com elementos obrigatórios e negativos explícitos.
5. Fazer duas gerações distintas por tema, com hashes e recibos separados.
6. Testar provedor alternativo quando o primeiro retornar `EditorialImageAdapterError`.
7. Reexecutar os seis rascunhos em modo draft-only.
8. Enviar ao WordPress somente imagens aprovadas, leves, não repetidas e com crédito ou aviso de IA.

## Invariantes

Nenhuma etapa deste fórum autoriza publicação. `publication_authorized=false`, `public_publish=false` e `wordpress_real=false` permanecem obrigatórios. O 261603 não deve ser alterado. A imagem 261602 não pode ser reutilizada.

## Estado de encerramento desta rodada

O problema está isolado e documentado. A correção pode continuar à noite ou em sessões futuras sem perder o contexto, os recibos ou as decisões já tomadas.

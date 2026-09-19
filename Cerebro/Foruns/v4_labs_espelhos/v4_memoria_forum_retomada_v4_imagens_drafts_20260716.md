# Fórum V4 — Retomada de testes de rascunhos com imagens (16/07/2026)

Data: 16 de julho de 2026  
Objetivo: retomar o V4, fazer healthcheck de LLMs e Vision de forma minuciosa, e executar mais 8 testes de draft com 2 casos por editoria.

## Status de pronto imediato

Concluída a preparação e execução dos testes de imagem, com resultado guardado para retomada sem perda de contexto.

- Healthcheck LLM: concluído (24 combinações = 4 editorias × 6 funções).
- Healthcheck Vision: concluído com diagnóstico por cenário.
- Testes de imagem destacada: 8 casos executados, todos com status `draft_without_featured_image`.
- Teste de build/publicação de drafts: bloqueado por autorização de rodada expirada.

## Healthcheck LLM (v4)

Arquivo de evidência:

- `v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716.json`

Resumo objetivo:

- Total checagens: 24  
- Aprovadas (`ok=true`): 0  
- Falhas (`ok=false`): 24

As três causas recorrentes:

- `real.enabled=false no contrato do adapter` (24 casos)
- `allow_real_calls=false no contrato do adapter` (24 casos)
- ausência de chaves de ambiente por candidato (`sem env key disponivel...`)
  - OpenAI: 4 casos
  - Anthropic: 8 casos
  - Gemini: 12 casos

Observação: o contrato e a configuração atual só mostram candidato funcional por função (provider/model), porém sem chaves no ambiente e sem autorização de chamadas reais, o check não pode validar execução de rede.

## Healthcheck Vision

Arquivo de evidência:

- `v4_memoria/foruns/healthcheck_vision_v4_20260716.json`

Síntese dos cenários:

- `current_env`: provider ativo `qwen_dashscope`, falha em `analyze` com `qwen_http_status:401` (chave atual presente, chamada real feita).
- `without_qwen`: ausência de chaves de visão → erro `media_vision_api_key_missing`.
- `with_invalid_gemini`: provider `gemini` ativo, falha em `gemini_request_failed`.
- `no_media_keys`: erro `media_vision_api_key_missing`.

Conclusão: não há cenário estável de visão validado para aprovação automática de candidatura nesta sessão.

## Testes de imagem destacada (8 casos, 2 por editoria)

Arquivos de entrada:

- `v4_memoria/foruns/forum_imagens_v4_20260716/politica_20260714_03_emprego_qualidade.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/politica_20260714_05_brasil_soberano.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/internacional_20260714_01.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/internacional_20260714_02.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/ciencia_20260714_01.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/ciencia_20260714_02.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/cultura_20260714_streaming.json`
- `v4_memoria/foruns/forum_imagens_v4_20260716/cultura_20260714_patrimonio_clima.json`

Decisões geradas (arquivo agregado):

- `v4_memoria/foruns/forum_imagens_v4_20260716/decisions/*_runtime.json`

Resumo padronizado por caso (todos iguais na estrutura final):

- `status`: `draft_without_featured_image`
- `selected_origin`: `null`
- `selected`: `null`
- `upload_performed`: `false`
- `ok`: `true` (pipeline completou controle, sem quebra de contrato)
- `issues`: `image_generator_failed:EditorialImageAdapterError`
- `publication_block_reasons`: `featured_image_required_but_absent`
- `warnings`: `draft_allowed_without_featured_image`

Padrão de autocura observado (exhaustiva, sem desistência):

- `attempts` = 7 por item
- Estágio 1: `audited_store` → `no_eligible_image`
- Estágio 2: `external_photo` → `collected`
- Estágio 3: segunda etapa `external_photo` variando entre `all_candidates_rejected_by_vision` e `no_candidates`
- Estágios 4 a 7: `ai_editorial_illustration` com `generation_failed` + `no_candidates` em dupla

Ponto de aprendizado automático:

- O pipeline segue em autocura até as 7 tentativas previstas, mas não consegue avançar após falha de gerador, permanecendo sem imagem destacada.

Exemplos de trilha por item:

- `politica_20260714_03_emprego_qualidade`: `audited_store:no_eligible_image -> external_photo:collected -> external_photo:all_candidates_rejected_by_vision -> ai_editorial_illustration:generation_failed -> ai_editorial_illustration:no_candidates -> ai_editorial_illustration:generation_failed -> ai_editorial_illustration:no_candidates`

Resumo de cobertura JSON:

- `v4_memoria/foruns/forum_imagens_v4_20260716_runtime_summary_20260716.json`

## Teste de build de drafts no WordPress

Arquivo de evidência:

- `v4_memoria/foruns/forum_imagens_v4_20260716/wordpress_build.json`

Resultado:

- `ok=false`
- `status=blocked`
- `issues=["batch_draft_authorization_expirada"]`
- `public_publish=false`, `wordpress_call=false`, `external_call=false`

Causa raiz:

- autorização atual em `dados/auditado/publication_authorizations/round_20x8_draft_revisions_20260714.json` com `approved_at=2026-07-14T09:48:33-03:00`, vencida para a janela de execução atual.

## Estado de retomada

Não houve publicação real nesta rodada. Todo o bloco ficou em estado auditável, seguro e pronto para retomar.

- Reiniciar a partir dos requests em `v4_memoria/foruns/forum_imagens_v4_20260716/`.
- Revalidar autorização de publicação antes de novo build.
- Manter `draft-only`, sem bypass de segurança, sem uploads forçados sem aprovação Vision.

## Próximos passos recomendados (sem perder contexto)

1. Resolver os pontos de saúde:
   - reativar `real.enabled` e `allow_real_calls` conforme política de execução;
   - garantir chaves de ambiente por função (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`/`CLAUDE_API_KEY`, `GEMINI_API_KEY`).
2. Corrigir cadeia Vision (quando aplicável):
   - estabilizar Qwen/Gemini com credenciais válidas e observabilidade de erro por provedor.
3. Reexecutar os 8 itens no `forum_imagens_v4_20260716`, mantendo as decisões de falha por etapa.
4. Atualizar autorização de rodada e re-rodar `wordpress_batch_drafts_cli` build/execution.

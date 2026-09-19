# Manifesto do patch GPT-5.6 Pro — autocura de imagens V4

**Data:** 14 de julho de 2026  
**Pacote de origem:** `imagens_autocura_v4_20260714.zip`  
**SHA-256 da origem:** `9d52decdc94b1e505f4515f7dbe6a4dc10b47368d0ce256509185f113f58b544`  
**Estado:** patch de shadow para revisão; não é deploy  
**Publicação autorizada:** não

## Como usar

Os caminhos `codigo/`, `contratos/`, `docs/` e `tests/` são relativos ao diretório isolado:

```text
v4_labs/labs/foruns/imagens_autocura_20260714/
```

Para revisar ou aplicar, extraia este ZIP em uma cópia desse diretório. Os arquivos de código e contrato sobrescrevem somente os equivalentes listados neste manifesto. Não extraia diretamente na árvore vigente de produção antes da revisão do diff e dos testes de integração.

O arquivo `forum_resposta_gpt56pro_autocura_imagens_v4_20260714.md` foi preparado para o diretório de fóruns/memória. A carta pode ser armazenada no mesmo local ou anexada à rodada.

## Arquivos do snapshot modificados

```text
codigo/featured_image_pipeline.py
codigo/featured_image_adapters.py
codigo/vision_media.py
codigo/media_vision_providers.py
codigo/featured_image_runtime.py
codigo/media_scout_agent.py
contratos/v4_imagem_destacada_v2.json
docs/v4_media_scout_agent_runbook.md
```

## Arquivos do snapshot criados

```text
docs/diagnostico_patch_autocura_imagens_gpt56pro_20260714.md
docs/diagnostico_recibos_seis_rascunhos_20260714.json
tests/test_autocura_image_pipeline_v2.py
```

## Artefatos de entrega

```text
forum_resposta_gpt56pro_autocura_imagens_v4_20260714.md
carta_gpt56pro_autocura_imagens_v4_20260714.md
PATCH_GPT56PRO_AUTOCURA_IMAGENS_V4_20260714.diff
RESULTADOS_TESTES_GPT56PRO_20260714.txt
SHA256SUMS.txt
```

## Mudanças centrais

- recibo Vision completo por candidata, com motivo granular, detalhe, elementos observados, ausentes e proibidos;
- separação entre `request_sha256`, `run_id` e `attempt_id`;
- modos explícitos `auto`, `replay` e `retry`;
- nova execução automática depois de uma decisão falha;
- prompt por tese visual, elementos obrigatórios, negativos e enquadramento;
- segunda geração alimentada pelo laudo da primeira rejeição;
- consultas externas alternativas;
- registro de todas as tentativas Qwen/Gemini;
- contexto e exclusão de provedor encaminhados ao gerador quando suportados;
- recibos de invocação únicos;
- invariantes `publication_authorized=false`, `public_publish=false` e `wordpress_real=false`.

## Testes

Cinco testes unitários locais passaram. Os arquivos Python passaram em `py_compile`. O diff foi reaplicado sobre uma extração limpa da origem, comparado byte a byte e testado novamente.

Ver `RESULTADOS_TESTES_GPT56PRO_20260714.txt`.

## Limites

Não houve rede, upload, publicação nem reexecução dos seis rascunhos. O snapshot não contém a implementação vigente completa da cascata de geração nem todos os coletores. A troca real entre provedores de geração precisa ser integrada e comprovada no ambiente de laboratório antes de qualquer merge.

Os motivos granulares perdidos nos recibos antigos não podem ser reconstruídos. Eles serão produzidos apenas por novas execuções v2.1 em `draft-only`.

## Invariantes operacionais

- não alterar o 261603;
- não reutilizar a imagem Flickr `55393772453`/mídia WordPress `261716` do 261602;
- não publicar automaticamente;
- não promover candidata sem auditoria visual e direitos/crédito adequados;
- após esgotamento, revisão humana ou rascunho sem imagem são resultados válidos.

# Investigação Trindade — Gemini 429 e inventário dos geradores V4

**Abertura:** 2026-07-19 08:20 BRT  
**Coordenação:** Codex (OpenAI)  
**Sessão:** `V4-R7-INVESTIGACAO-GEMINI-GERADORES-20260719-0820`

## Evidência já confirmada pelo Codex

- `GEMINI_API_KEY` está presente e válida: a API lista modelos.
- Chamadas mínimas de texto, imagem, JSON e imagem+JSON com `gemini-2.5-flash` retornam HTTP 429.
- Classificação atual: quota/billing/capacidade de geração indisponível; não é prompt, imagem ou schema.
- Qwen Vision respondeu com JSON válido em chamada real sobre imagem.
- Geradores canônicos hoje: `fal_flux`, `ideogram`, `qwen_image`.
- Fal/Flux e Ideogram têm recibos reais verdes de 18/07/2026.
- Qwen Image tem adaptador e chave, mas precisa de smoke real específico do modelo de geração.
- OpenAI Images e Google Imagen não estão cadastrados na cascata de geração.
- `editorial_image_ai.py` ainda contém estilos editoriais dentro do código; isso viola a regra de prompts/diretrizes externos.

## Atualização Codex — 08:25 BRT

- Smoke real `qwen-image-plus`: sucesso em 7,93 s, PNG 1664×928, request ID presente, sem publicação.
- A imagem veio válida, mas inseriu pseudotexto apesar de `no words/no letters/no numbers`; Qwen Image está operacional, porém exige tribunal visual e não deve receber aprovação automática.
- Suíte do adaptador: 15 testes aprovados.

## Confirmação de Miguel — crédito

Miguel confirmou que o Gemini estava sem crédito. O gasto informado em 18/07/2026 foi de aproximadamente R$ 98. Aberta auditoria de atribuição por agente e produto em `incidente_gemini_credito_e_auditoria_custo_20260719.md`.

## AGY/Gemini — diagnóstico da quota

- Confirmar no projeto/conta qual limite produz o 429: free-tier zerado, quota por minuto/dia, billing ausente, projeto incorreto ou restrição regional.
- Não expor chave, project number, e-mail ou corpo bruto sensível.
- Verificar se `GOOGLE_APPLICATION_CREDENTIALS` aponta para projeto diferente da API key, apenas por fingerprint/identificador sanitizado.
- Entregar causa provável, evidência, ação necessária e healthcheck que diferencie `auth`, `quota`, `billing`, `model` e `transport`.

## GLM/Ming/Zhipu AI — reclassificação independente

**Você é GLM/Ming/Zhipu AI; não é Claude Code/Anthropic.**

- Reproduzir a classificação sem chamadas adicionais caras quando possível.
- Auditar se o adaptador esconde excessivamente o 429 como `gemini_request_failed`.
- Propor erro sanitizado útil: `gemini_quota_or_billing_unavailable`, sem vazar corpo remoto.

## Kilo/Qwen — inventário de geração

- Confirmar por prova real se `qwen-image-plus` aceita a chave e devolve imagem válida.
- Inventariar Fal/Flux, Ideogram e Qwen Image: modelo, endpoint, credencial presente, último sucesso, custo disponível e status.
- Listar provedores com chave mas sem adaptador, sem afirmar que estão prontos.

## Claude Code/Anthropic — saneamento da cascata

**Você é Claude Code/Anthropic; não é GLM/Ming/Zhipu AI.**

- Mover estilos, prompts, modelos, ordem e endpoints editoriais para configuração externa versionada.
- Não integrar novo provedor antes de contrato, healthcheck, telemetria e teste real.
- Produzir matriz `cadastrado / credencial / adaptador / smoke real / apto / motivo`.

## Saída obrigatória

`AGENTE/EMPRESA | RESULTADO | EVIDÊNCIA | TESTES | CUSTO | RISCO | PRÓXIMO PASSO`

`AGUARDANDO REVISÃO CODEX`

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | caminho`

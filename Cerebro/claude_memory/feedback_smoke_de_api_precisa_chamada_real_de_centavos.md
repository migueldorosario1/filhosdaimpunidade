---
name: feedback-smoke-de-api-precisa-chamada-real-de-centavos
description: "Smoke test de script que fala com API externa NÃO pode ser só `--status`/dry-run — precisa fazer 1 chamada real de centavos pra pegar bugs de payload (modelo inexistente, header errado, endpoint 404). Caso fundador 28/07/2026 17:50 Kimi salvou Modo B"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Smoke test de script que integra API externa (Moonshot, OpenAI, Anthropic, Groq, Google, Brave, etc.) NÃO pode se limitar a `--status`/`--help`/`--dry-run`/rodadas offline. **Tem que fazer pelo menos 1 chamada real ao endpoint** — mesmo que custe centavos — pra pegar bugs que só aparecem no wire (modelo inexistente, header errado, endpoint 404, formato de payload rejeitado, campo obrigatório faltando).

**Como aplicar:**
1. Ao escrever/deployar script novo que chama API externa: obrigatoriamente rodar 1 chamada de payload mínimo antes de "declarar pronto"
2. Se custo importa, usar prompt curtíssimo ("ping"/"1") pra minimizar tokens output
3. Verificar: (a) `.status_code == 200`, (b) `.choices[0].message.content` não vazio, (c) `.usage.prompt_tokens > 0`
4. Se disponível `GET /models`, listar modelos ao vivo ANTES de assumir nomenclatura por documentação (docs podem estar defasados; ex: Moonshot lista `kimi-k3` em paygo, `k3` em Coding — nomes diferem entre endpoints do mesmo provider!)
5. Registrar no fórum do sprint que smoke real foi feito + custo real medido (não estimado)

**Anti-pattern conhecido:** smoke que só faz `--status` mostrando quota 0/20, sem chamar API. Passou verde. Foi pra produção quebrado.

**Why:** Caso fundador 28/07/2026 17:50 BRT. Deployei `~/ferramentas/sentinela/consulta_kimi_memoria_total.py` com `MODELO = "kimi-k2-turbo-preview"` — nome bonito, plausível, mas **NÃO EXISTE em nenhum canal Moonshot** (nem paygo `api.moonshot.ai/v1` nem assinatura `api.kimi.com/coding/v1`). Smoke `--status` retornou `{count: 0}` verde e declarei "ok". Kimi K3 Desktop pegou bug em revisão via `GET /models` ao vivo. Se ninguém tivesse pegado, 100% das chamadas do Modo B da ponte quebrariam com "❌ Falha nos 2 canais" pra sempre. Kimi corrigiu com AUTOCURA completa (backup SHA-256, 6 edições cirúrgicas, py_compile, **smoke REAL de 2 centavos** que provou que roda). Custo real medido pós-fix: R$ 0,0192/consulta (20× mais barato que estimativa).

**Lição meta:** validação offline (compile, lint, --status, dry-run) pega ~30% dos bugs. Validação online (1 chamada real) pega 90%. A diferença são bugs de contrato com o outro sistema — os mais caros de descobrir em produção.

**Casos de aplicação:**
- Deploy novo cliente HTTP/gRPC
- Migração de versão de API (v1→v2)
- Mudança de modelo/endpoint em script pré-existente
- Rotação de chave (checar se chave nova tem escopo correto)
- Ferramentas MCP novas antes de anunciar ao usuário

**Regras irmãs:**
- [[feedback-verificar-processo-real-antes-de-confiar-no-cerebro]] — mesma família: ground truth vem de verificação viva, não de documento
- [[feedback-autocura-protocolo-registro-com-solucao-e-rollback]] — smoke faz parte do protocolo AUTOCURA obrigatório
- [[feedback-sempre-pesquisar-web-em-duvida]] — verificação de realidade antes de afirmar

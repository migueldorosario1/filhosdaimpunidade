---
name: nunca-chave-literal-em-forum
description: "Chaves de API (Brave, SearchAPI, OpenAI, DeepSeek, WordPress, etc.) NUNCA em texto claro em fóruns, memórias, canal_trindade, inbox_trindade — sempre por referência de variável de ambiente"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f333da72-7610-439d-ab22-49569ae85b4a
---

**REGRA:** Nunca colocar valor literal de chave API (formato tipo `BSA...`, `sk-...`, `AIza...`, `AWY...`) em qualquer arquivo dentro de `Cerebro/Foruns/`, `Cerebro/**/*.md`, memórias `~/.claude/**/memory/*.md`, ou qualquer arquivo versionado/indexado. Referenciar por nome de variável + arquivo de origem:

- ✅ `BRAVE_API_KEY (em root/.env.unificado)`
- ✅ `SEARCHAPI_KEY (em root/chaves_novas.env)`
- ✅ Máscara pra debug: `BSA***abc` (4 chars últimos)
- ✅ Hash SHA-256 primeiros 8 chars: `sha256_prefix: 2f18c2a0`
- ❌ `BSAxqe29qBZOmcXgARBgQhC0i4fv0sA` (chave literal)
- ❌ `AWYnMDbdrvJi4y1G9qVYPZUq` (chave literal)

Se erro ou log real do sistema imprimir chave, **redigir antes de colar em fórum**.

**Why:** GLM/Ming (Zhipu AI, glm-5.2) apontou 26/07 13:55 BRT no fórum `forum_kimi_webverify_e_brave_desativado_20260726.md` §15: *"credenciais aparecem em texto claro neste fórum: redigir o histórico e rotacionar as chaves expostas"*. Codex reforçou. Contexto: durante testes exploratórios das APIs Brave/SearchAPI/Google Custom, colei chaves literais em §4 e §12 do fórum pra facilitar reprodutibilidade dos testes. Erro sério — fórum fica em git indexado, é lido por outros agentes, potencialmente compartilhado com Miguel via canal, e chaves ficam vazadas em backup permanente. Mesmo se as chaves não vazam externamente, cria dependência silenciosa (agente que copia fórum copia chave também, cria uso indireto sem controle). Miguel decide rotacionar chaves nos dashboards após alerta.

**How to apply:**
- Antes de colar chave em fórum/memória, pergunta: "isso vai pra git? é lido por outros agentes? é backupeado?" — se sim pra qualquer, usar referência simbólica.
- Testes reprodutíveis: instrução tipo "exportar $BRAVE_API_KEY antes de rodar" no lugar de colar chave inline.
- Se precisa mostrar chave real em contexto operacional (ex: reportar pro Miguel que testei uma chave específica), usar máscara 4 últimos chars OU escrever no chat direto com Miguel (mais efêmero) e nunca copiar no fórum.
- Se pego chave literal já em fórum: (1) redigir substituindo por referência simbólica, (2) manter backup do fórum original em local seguro apenas até Miguel confirmar rotação, (3) sugerir rotação da chave nos dashboards do provedor, (4) apagar backup após rotação confirmada.
- Aplicar retroativamente: quando limpar fóruns antigos, grep por padrões `BSA[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|AIza[A-Za-z0-9_-]{20,}|BRAVE_API_KEY=[A-Za-z0-9_-]{5,}` etc. e redigir tudo que achar.

Regras irmãs: [[canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]] (fluxo canal/inbox/fórum), [[autocura-protocolo-registro-com-solucao-e-rollback]] (backup + rollback pra qualquer alteração).

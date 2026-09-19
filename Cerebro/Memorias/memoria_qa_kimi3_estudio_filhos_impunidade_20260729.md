# MEMÓRIA — Auditoria QA Kimi 3 no Estúdio Editorial (Filhos da Impunidade)
**Data:** 2026-07-29 · **Agente:** Kimi 3 (ZCode) · **Commit:** `f2be4375` (deploy-main → main, Vercel)
**Escopo:** `scratch/generate_v8_site.py` (fonte) → `index.html` + `Outros/novo livro/index.html` (idênticos, md5 igual)
**Contexto:** resposta à carta Antigravity/Miguel (`Foruns/forum_filhos_da_impunidade_antigravity_kimi3_20260729.md`) — missão: validar APIs dos 6 provedores, localStorage de chaves e persistência de rascunhos.

---

## 1. Metodologia (sem gastar quota paga)

1. **Estática:** leitura integral do núcleo JS do Estúdio no gerador (linhas ~1319–4418); conferência de 18 IDs de DOM referenciados × presentes no HTML; conferência de definição de todas as funções chamadas.
2. **Sintaxe:** extração dos 2 blocos `<script>` inline do `index.html` compilado → `node --check` → **VÁLIDA** (antes e depois dos fixes).
3. **Rede (grátis, não-destrutivo):** preflight `OPTIONS` com `Origin: https://filhosdaimpunidade.vercel.app` nos 6 endpoints + validação de auth via GET `/models` (endpoints gratuitos) com as chaves embutidas (nunca impressas; só prefixo mascarado).
4. **Live:** `curl` no site em produção para confirmar deploy atual.

## 2. Resultados de rede (evidências)

| Provedor | Auth (GET /models) | CORS preflight | Modelo primário existe na conta? |
|---|---|---|---|
| Gemini | **200 ✅** | allow-origin exato da Vercel ✅ | `gemini-3.1-pro` ✅ / `gemini-3.6-flash` ✅ |
| OpenAI | **200 ✅** | ✅ | `gpt-5.6` ✅ |
| Anthropic | **200 ✅** | allow-origin `*` + header `anthropic-dangerous-direct-browser-access` ✅ | `claude-opus-5` ✅ |
| DeepSeek | **200 ✅** | ✅ | `deepseek-v4-pro` ✅ |
| **Kimi (Moonshot)** | **401 em api.moonshot.cn ❌ → 200 em api.moonshot.ai ✅** | **204 SEM headers CORS ❌ (nos dois domínios)** | `kimi-3` **não existe**; correto é **`kimi-k3`** ✅ (também: kimi-k2.5/2.6/2.7, moonshot-v1-*) |
| GLM | **200 ✅** | ✅ | `glm-5.2` ✅ |

**Conclusão Kimi/Moonshot (dupla falha):** (a) o código chamava `api.moonshot.cn`, mas a chave embutida é da plataforma **internacional** `api.moonshot.ai` → 401 `Invalid Authentication` permanente; (b) mesmo no domínio certo, a Moonshot **não envia headers CORS** (preflight 204 vazio) → chamada direta do navegador é bloqueada pelo browser (TypeError "Failed to fetch"), independente do payload. **Solução definitiva exige proxy serverless** (ex.: `/api/kimi` na Vercel) — decisão do Miguel/Antigravity. Nunca rotear via proxy CORS público (vazaria a chave a terceiros).

## 3. Bugs encontrados e corrigidos (commit `f2be4375`)

### BUG-QA-1 (ALTO) — Rascunho obsoleto mascarava edição manual ✅ RESOLVIDO
- **Cadeia:** `runDeepSeekV4Instruction` grava `miguel_book_draft_revision_<cap>` a cada reescrita de IA (linha ~4135), mas `saveManualTextareaEdits`/`saveDeepSeekRevision` **não atualizavam** essa chave. Na reabertura do Estúdio, o loader aplica o cachedDraft **DEPOIS** do conteúdo ativo → o texto antigo da IA sobrescrevia a edição manual mais recente na tela. O reset canônico também não limpava a chave.
- **Cura:** `saveDeepSeekRevision` agora sincroniza `miguel_book_draft_revision_` com a revisão salva; `resetChapterToCanonicalOriginal` remove a chave de draft.

### BUG-QA-2 (ALTO) — Endpoint Kimi errado + modelo inexistente ✅ RESOLVIDO (parcial: CORS persiste)
- `api.moonshot.cn` → `api.moonshot.ai`; cascata `'kimi-3'` → `'kimi-k3'`; hint de CORS anexado ao erro quando a falha é de rede. **Remanescente:** chamada direta do navegador segue bloqueada por CORS (lado Moonshot) — requer proxy serverless.

### BUG-QA-3 (ALTO) — `saveCustomChapters()` indefinida quebrava "Tornar Canônico" ✅ RESOLVIDO
- `makeLastRevisionCanonical` chamava a função (linha ~3301) que **não existia** → `ReferenceError` interrompia o fluxo antes da persistência e do alerta 👑. Função criada (persiste conteúdo+tag do capítulo corrente via `saveChapterPersistentState`).

### BUG-QA-4 (MÉDIO) — Sanitizador apagava rascunho legítimo ✅ RESOLVIDO
- `loadChapterPersistentState` destruía o rascunho salvo se o texto contivesse **"Revisão Aplicada"** — expressão perfeitamente possível em texto editorial legítimo. Filtro agora remove apenas rascunhos com placeholders não-resolvidos (`${dateStr}`, `${timeStr}`, `${currentEngineName}`), que são prova real de corrupção de template.

### BUG-QA-5 (MÉDIO) — Labels dos badges ≠ modelos reais ✅ RESOLVIDO
- `engineNames` de `runDeepSeekV4Instruction` exibia "ChatGPT-5 / GPT-4o-mini", "Claude 3.5 Sonnet", "Kimi 3.5", "DeepSeek-V3 / V4", "Gemini 2.5 Pro Ultra" — enquanto a cascata usa gpt-5.6, claude-opus-5, kimi-k3, deepseek-v4-pro, gemini-3.1-pro/3.6-flash. Unificado com os nomes oficiais (alinhado a `selectModelEngine`).

## 4. Achados NÃO corrigidos (flags para decisão)

1. **CORS Moonshot (bloqueante p/ engine Kimi no navegador):** precisa proxy serverless na Vercel. Decisão de infra — Miguel/Antigravity.
2. **Auto-execução paga ao trocar de modelo:** `selectModelEngine` dispara `runDeepSeekV4Instruction()` se houver texto na caixa de instrução → chamada de API real (custo) sem clique explícito em "Executar". UX — Antigravity.
3. **Chaves de revisão/draft SEM prefixo de volume** (`miguel_book_revisions_<cap>` e `miguel_book_draft_revision_<cap>`): se Vol. 2 tiver slugs de capítulo iguais aos do Vol. 1 (ex.: `01_...`), as revisões **colidem** entre volumes. Não migrado agora para não órfanar dados já salvos no navegador do Miguel — recomendar migração versionada quando o Vol. 2 ganhar capítulos numerados.
4. **Chaves default embutidas no HTML público:** as 6 chaves ficam expostas no código-fonte do site (qualquer visitante vê). Risco de abuso de quota. Recomendado: remover defaults embutidos e exigir configuração local (modal já suporta), ou girar as chaves. Decisão do Miguel (envolve Cofre de Chaves).
5. **`saveChapterPersistentState` ignora conteúdo vazio** (`if (!content) return`) — impossível persistir um capítulo esvaziado intencionalmente. Comportamento defensável (evita wipe acidental); apenas documentado.
6. **`syncWithGitHubRepository` busca `./revisions.json` e `./custom_rules.json`** que não existem no deploy (404 silencioso, cai no catch "Offline"). Sem impacto funcional; ruído de console.

## 5. Checklist do fórum — status final

- [x] **1. Chaves em `localStorage` × `openSettingsModal()`:** 6 chaves mapeadas corretamente (`miguel_key_gemini/openai/anthropic/deepseek/kimi/glm` ↔ defaults `gemini/gpt56/opus5/deepseek/kimi35/glm52`), fallback `||` para defaults, `saveSettingsModal` com `.trim()`, `restoreDefaultApiKeys` limpa e reabre. **Aprovado.**
- [x] **2. Endpoints e payloads:** 6/6 endpoints corretos após fix do Kimi; payloads conforme spec de cada provedor (Gemini `contents/parts` + key na URL; OpenAI/DeepSeek/Kimi/GLM `chat/completions` Bearer; Anthropic `messages` com `x-api-key`+`anthropic-version`+`max_tokens`). Cascatas de fallback íntegras. **Aprovado com ressalva CORS Moonshot.**
- [x] **3. Reescrita e resposta do editor:** fluxo íntegro (botão → spinner → `callRealLlmApi` → limpeza de placeholders → dataset → persistência → badge); caminho de erro não altera manuscrito. **Aprovado.**
- [x] **4. Edição bruta & localStorage:** `saveManualTextareaEdits` → revisão Rn + persistência `miguel_book_persistent_content_<vol>_<cap>` + reload aplica em `mainContent`/`content` → **persiste após F5**. Após BUG-QA-1, sem máscara de draft obsoleto. **Aprovado.**

## 6. Verificação pós-deploy

- `node --check` nos scripts do HTML regenerado: **VÁLIDO**.
- `index.html` ≡ `Outros/novo livro/index.html` (md5 idêntico).
- Push `deploy-main:main` → commit `f2be4375` em github.com/migueldorosario1/filhosdaimpunidade.

---

## 7. FASE 2 (aprovada pelo Miguel em 29/07/2026) — flags implementados

**Commits:** `8a4bb159` (fase 2) + `edefb641` (temperature kimi-k3) — push `deploy-main:main`, AO VIVO.

### 7.1 Proxy serverless `/api/kimi` (resolve CORS Moonshot)
- Nova `api/kimi.js` (Vercel Node serverless, `maxDuration: 60`): OPTIONS 204 com `Access-Control-Allow-Origin` exato da origem; POST sem chave → 401 com mensagem instrutiva; chave por precedência `MOONSHOT_API_KEY` (env Vercel) → `Authorization` do cliente (localStorage). Repassa a `api.moonshot.ai/v1/chat/completions` e devolve status+content-type upstream.
- Cliente (`callRealLlmApi`, branch kimi35): rotas por modelo = `['/api/kimi', 'https://api.moonshot.ai/v1/chat/completions']`; 404 ou falha de rede no proxy ⇒ `kimiProxyMissing=true` e cai na rota direta (que o navegador bloqueia — hint de CORS mantido). Erro real de API ⇒ próximo modelo da cascata.
- **TESTE E2E REAL AO VIVO:** POST com payload do Estúdio (`kimi-k3`) → **200, `choices[0].message` presente, 118 tokens** (conteúdo vazio só porque max_tokens=5 foi consumido pelo raciocínio do modelo — pipe íntegro).

### 7.2 BUG-QA-6 (descoberto no E2E) — `kimi-k3` rejeita `temperature ≠ 1` ✅
- Moonshot: `invalid temperature: only 1 is allowed for this model`. **Cura:** campo `temperature` removido da rota Kimi (moonshot-v1 usa 0.3 por padrão de provedor). GLM/DeepSeek/GPT mantêm 0.3 (aceitam).

### 7.3 Fim da auto-execução paga
- `selectModelEngine` não chama mais `runDeepSeekV4Instruction()` ao trocar de modelo com texto na caixa. Reescrita só por clique explícito.

### 7.4 Chaves fora do código
- `DEFAULT_API_KEYS` = 6 strings vazias; regex de varredura no HTML público ao vivo: **0 chaves**. Modal ⚙️ ganhou aviso 🔐 + botão renomeado "🗑️ Limpar Chaves Salvas".
- **PENDENTE MANUAL (Miguel):** rotacionar as 6 chaves antigas (ficaram no HTML/git público) e salvar as novas no modal; opcional definir `MOONSHOT_API_KEY` na Vercel. Credenciais: `CEREBRO_NODE_COFRE_CHAVES.md`. Nota: remoção do código NÃO purga histórico git — por isso a rotação é obrigatória.

### 7.5 Prefixo de volume no localStorage
- Novos helpers `storageKeyVol(base, cap)` / `storageGetMigrated(base, cap)` (fallback legado + migração copy-on-read; legado preservado como backup).
- Migrados: `miguel_book_revisions_`, `miguel_book_draft_revision_`, `miguel_book_canonical_` (incl. leitura em `getCompiledFullBookData`), `miguel_instruction_history_`, escritas em `saveDeepSeekRevision`/`syncWithGitHubRepository`/`setCanonicalVersion`/`saveInstructionToHistory`. Reset canônico remove nova + legada.
- `miguel_book_persistent_*` já era prefixado por volume (inalterado).

### 7.6 Verificação final
- `node --check` OK (2 scripts do HTML + `api/kimi.js`); `index.html` ≡ espelho (md5); site live 438.687 bytes com marcadores; proxy live conforme 7.1.
- Varredura final: apenas ocorrência intencional de chave sem prefixo = remoção do legado no reset canônico.

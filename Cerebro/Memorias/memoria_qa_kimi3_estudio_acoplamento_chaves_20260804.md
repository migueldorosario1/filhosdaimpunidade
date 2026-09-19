# MEMÓRIA — QA Kimi 3: Erro "Chave Gemini não configurada" + Acoplamento Leitor→Estúdio
**Data:** 2026-08-04 · **Agente:** Kimi 3 (ZCode) · **Commits:** `0c2b288e` + `e0830c45` (deploy-main → main, Vercel) — **AO VIVO** (md5 live `06a2e7b47f738240422bc767f659028a` ≡ `index.html` local, 440.847 bytes)
**Escopo:** `scratch/generate_v8_site.py` (fonte) → `index.html` + `Outros/novo livro/index.html` (idênticos)
**Contexto:** Miguel reportou (1) alerta "Chave de API do Gemini não configurada" ao executar reescrita no Estúdio e (2) ao clicar "Entrar no Estúdio Editorial" vendo a Versão 4 (Antigravity) no leitor, o Estúdio abria a versão canônica ("o estúdio não está acoplado ao leitor").

---

## 1. Erro "Chave de API do Gemini não configurada" — NÃO era bug de código

- **Cadeia auditada ao vivo:** `saveSettingsModal()` grava `miguel_key_*` (6 chaves, com `.trim()`) → `callRealLlmApi()` lê via `getKey()` (`val && val.trim().length > 0 ? val.trim() : defaultKey`) → botões ligados corretamente. Fluxo íntegro.
- **Causa raiz:** Fase 2 do QA (commit `8a4bb159`, aprovada pelo Miguel) esvaziou `DEFAULT_API_KEYS` por segurança (0 chaves no HTML público). Desde então o Estúdio **só funciona com chaves no `localStorage` do navegador** — e o navegador do Miguel nunca as recebeu (antes vinham embutidas). Era a "ação manual pendente" registrada no fórum.
- **Histórico git:** nomes `miguel_key_*` nunca mudaram (desde `03aef9c2`) — descartada hipótese de migração/escopo.

### Certificação das 6 chaves (GET /models gratuito, valores nunca impressos)

| Provedor | Fonte local | Variável | Auth |
|---|---|---|---|
| Gemini | `Outros/chaves/agentes_labs/.env.unificado` | `GEMINI_API_KEY` | 200 ✅ (sha8 `62a36df0`) |
| OpenAI | ↑ | `OPENAI_API_KEY` | 200 ✅ |
| Anthropic | ↑ | `ANTHROPIC_API_KEY` | 200 ✅ |
| DeepSeek | ↑ | `DEEPSEEK_API_KEY` | 200 ✅ |
| Kimi 3 | `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env` | `KIMI_PAYGO_API_KEY` | 200 ✅ |
| GLM 5.2 | `Rio Carta Agentes/root/chaves_riocarta.env` | `ZHIPU_API_KEY` | 200 ✅ (sha8 `283a4670`) |

- ⚠️ **Achados:** `KIMI_API_KEY` do cofre unificado = 401 em api.moonshot.ai (a certa é a paygo). GLM **não existe** no cofre canônico; a chave viva está órfã em `chaves_riocarta.env` (a GLM antiga do histórico git = 401, morta). Recomendado copiar GLM para o cofre canônico.
- **Fix entregue a Miguel:** ⚙️ Configurações → colar as 6 chaves das fontes acima → Salvar.

### Patch (`0c2b288e`) — erro de chave ausente vira ação
- No handler de erro de `runDeepSeekV4Instruction`, erro contendo "não configurada" agora dispara `confirm()` oferecendo abrir `openSettingsModal()` direto; demais erros (quota, rede) mantêm o `alert()` original. Painel inline rose inalterado. Teste lógico: 4/4 cenários (2× não configurada → true; 429/null → false).

## 2. Bug de acoplamento Leitor→Estúdio (`e0830c45`) — 3 elos

### Elo 1 (principal) — rascunho em cache sobrescrevia a versão vista
- `openAiAuditModal()` carregava corretamente `getActiveVersionData()` (respeita `currentVersionKey`, ex.: `antigravity`) na textarea `#deepseek-editable-result` e no preview — mas o bloco "restore cached draft" (~10 linhas depois) **sobrescrevia ambos** com `miguel_book_draft_revision` (rascunho de IA antigo, derivado da canônica) e reabria o painel de resultados. Miguel via texto canônico mesmo vindo da V4.
- **Cura:** o rascunho em cache é restaurado apenas como contexto (`lastGeneratedRevision`, usado pelos botões salvar/tornar canônico — ambos priorizam o conteúdo da textarea, verificado) e **não toca mais** textarea/preview/painel.

### Elo 2 — título sempre canônico
- `studio-chapter-title` usava `ch.versionTag` (tag canônica do capítulo) sempre. **Cura:** título reflete a versão ativa — experimental mostra `activeData.title` ("Versão 4: Antigravity"), revisão mostra `versionTag` ("R3 (kimi)"), oficial/full_book mantêm `ch.versionTag`.

### Elo 3 — versão fora da URL
- `updateUrlHashRoute` gravava só `vol`/`cap`; F5 no Estúdio → `parseUrlHashRoute` → `selectChapter` reseta `currentVersionKey` (última revisão ou `oficial`). **Cura:** hash passa a incluir `&ver=<versão>` (encodeURIComponent); `parseUrlHashRoute` aplica `ver` **depois** do `selectChapter`, validando contra `oficial` | revisões existentes | exp cap.1 (inválido → default seguro); `switchVersion` (dropdown do leitor) agora chama `updateUrlHashRoute()`.

### Validação
- Regen limpo (diff = só os edits), `index.html` ≡ espelho (md5), `node --check` OK nos 2 scripts inline.
- Simulação E2E do fluxo do Miguel (stubs DOM/localStorage + lógica real patchada), **5/5**: V4 no leitor → URL `&ver=antigravity` ✓; Estúdio abre com textarea=V4 e título "Versão 4: Antigravity" **mesmo com rascunho velho em cache** ✓; F5 no Estúdio restaura V4 do `&ver=` ✓; `ver=R99` inexistente rejeitado ✓.
- `runDeepSeekV4Instruction` já usava `getActiveVersionData()` como fonte da reescrita — a IA edita a versão certa (nada a corrigir ali).

## 3. Deploy e estado final
- Push `deploy-main:main` autorizado pelo Miguel em 04/08: `7658ceed..e0830c45`.
- Live verificado: 440.847 bytes, 5 marcadores `QA-FIX ACOPLAMENTO`, marcador do patch de chave, md5 ≡ local.
- **Pendências (não bloqueantes):** (a) Miguel salvar as 6 chaves no ⚙️ (instrução de 3 cliques entregue); (b) copiar `ZHIPU_API_KEY` para o cofre canônico `.env.unificado`; (c) rotação das chaves antigas expostas no histórico git segue como ação manual recomendada (Fase 2, flag 4).

---

## 4. PARTE 2 (mesma data, ~12h40) — botões de gravar travados + Copiar Texto + OpenAI

**Commit:** `468293e9` · AO VIVO (md5 ≡ local, 446.603 bytes) · Push autorizado pelo Miguel ("sim").

- **Chave OpenAI nova testada:** 200 ✅ (sha8 `adb3b7a9`) — 6/6 provedores operacionais. Chaves coladas no chat em texto puro: recomendada rotação (governança; só sha8 registrado).
- **Bug "botão travado" reproduzido ao vivo** (IAB): clique em "💾 Gravar Revisão R#" → sem diálogo, URL inalterada (sem `ver=R1`) → fluxo morre antes de `switchVersion`/alert. "👑 Tornar Canônica" idem. Causa: `localStorage.setItem` desprotegido (quota cheia — agravada pelas duplicatas legadas da migração de volume — ou storage bloqueado). O botão "Salvar alteração manual" termina na mesma função (mesma cura).
- **Cura:** helpers `pruneLegacyStorageDuplicates` (só poda legado que já tem cópia migrada — nunca a única cópia) + `safeLocalSet` (try → poda+retry em quota → status) + `storageFullHelpMessage`. Aplicado em: `saveDeepSeekRevision` (retorno c/ alerta instrutivo em falha), `saveSettingsModal` (loop 6 chaves), `setCanonicalVersion`, `saveInstructionToHistory`, `makeLastRevisionCanonical` (avisa se canônica só vale na sessão). **Feedback garantido: nunca mais morte silenciosa.**
- **Feature:** botão "📋 Copiar Texto" (`copyEntireChapterText`) na barra de ações — textarea → fallback `innerText` do renderizado; `navigator.clipboard.writeText` → fallback `execCommand`; feedback no botão com contagem de caracteres.
- **Armadilha do gerador (registrada para futuros edits):** o Python converte `\n` em quebra real — strings JS multi-linha DEVEM usar crase (template literal), nunca aspas simples (quebrou `node --check`; corrigido antes do deploy).
- **Validação:** `node --check` OK (2 scripts), espelhos md5-idênticos, simulação 4/4 (normal / quota com poda e retry / quota sem poda segura / bloqueado).

---

## 5. PARTE 3 (mesma data, ~13h30) — CAUSA RAIZ: ReferenceError de variável nunca declarada

**Commits:** `675808eb` (flash no botão) + `9bf69296` (fix raiz) · AO VIVO.

- **Cadeia da descoberta (IAB):** cliques sem efeito → novo build confirmado rodando (`typeof flashButtonFeedback === 'function'`, `saveDeepSeekRevision.length === 1`) → botão habilitado, geometria e `pointer-events:auto` normais → `getJsDialog` sempre vazio (IAB suprime diálogos) → leitura pura `() => lastGeneratedRevision` → **`ReferenceError: is not defined`** → grep no gerador: **0 declarações** (`let/var/const/window.`). 
- **Mecânica do bug (histórico):** modo não-estrito — atribuições (`lastGeneratedRevision = {...}` no sucesso da reescrita IA ou no restore de rascunho) criavam o global implicitamente; **leituras** (`if (!lastGeneratedRevision)`) em sessão fresca lançavam ReferenceError e matavam os 3 botões de gravação na hora. Explica o "às vezes funciona" (após rodar IA) e o "duro" do Miguel (sessão fresca, sem IA por causa da chave Gemini ausente).
- **Fix:** `let lastGeneratedRevision = null;` (linha única, junto a `currentVersionKey`). Pós-fix ao vivo: `lastGeneratedRevision === null` ✓.
- **flashButtonFeedback:** alert() é invisível em webviews → feedback ✅/⚠️ no próprio botão (Gravar R#, Salvar manual, Tornar Canônica ×2, Copiar Texto); render pós-edição em try/catch.
- **Limitação IAB (para futuras sessões):** pointer probe falha ("no click point"/timeout) e Enter não ativa botão focado, mas digitação em textbox funciona e `evaluate` aceita expressões puras de 1 chamada (`typeof X`, `el.getBoundingClientRect()`, `getComputedStyle`, `navigator.userActivation`) — rejeita multi-statements e `localStorage`/`elementFromPoint`. E2E físico de cliques no Estúdio exige navegador real.
- **Validação:** node --check OK, espelhos md5-idênticos, cadeia de funções 9/9 presentes ao vivo, simulação Node 4/4. Clique físico final: pendente no Chrome do Miguel (instruído: F5 → 1 clique → esperar ✅/⚠️ no botão).

---

## 6. PARTE 4 (~14h10) — sinal visível de gravação + R# na hora (`efb8e22d`, AO VIVO)

- Miguel confirmou que a gravação JÁ FUNCIONA (pós-fix ReferenceError) mas sem sinal na tela.
- `#studio-save-status`: faixa persistente verde/vermelha sob a barra de ações (`setStudioSaveStatus`).
- `refreshStudioTitle()`: helper único do título do Estúdio; chamado após gravar revisão e tornar canônica — o número da versão muda na hora (R24→R25) sem F5; `openAiAuditModal` refatorado para usá-lo.
- Validação: node --check OK, espelhos md5-idênticos, live md5 ≡ local (451.033 bytes).

---

## 7. PARTE 5 (~14h40) — Manual de Estilo injetado no system prompt (`61ead147`, AO VIVO)

- Pedido Miguel: "todas as LLMs têm que ler o Manual de Estilo sempre".
- Diagnóstico: systemPrompt fixo; manual (12,9 KB) e diretrizes custom NUNCA entravam no prompt; checkbox "🧠 Consultar memória" = só spinner (teatro).
- Implementação: blocos `=== MANUAL DE ESTILO DA OBRA (LEITURA OBRIGATÓRIA) ===` + `=== DIRETRIZES PERSONALIZADAS DO EDITOR (PRIORIDADE ALTA) ===` no systemPrompt de `callRealLlmApi` (6 engines); regra 3 anti-violação; blocos omitidos se vazios. Diretrizes registradas via checkbox "Registrar diretriz" passam a valer automaticamente.
- Armadilha repetida (2ª vez): `.join('\n')` com aspas simples quebrou o build (Python converte `\n`); corrigido com crase aninhada `.join(\`\n\`)`. REGRA PARA EDITS FUTUROS: no gerador Python, separadores/quebras em JS só em crase.
- Validação: node --check OK, espelhos md5-idênticos, simulação 3/3 (manual presente, diretrizes presentes, bloco vazio omitido), live ≡ local (452.209 bytes). Custo declarado ao Miguel: +~3-4k tokens/chamada.
- Flag aberta: checkbox "🧠 Consultar memória" segue teatro; injeção real de `bancoLinksMarkdown` oferecida (decisão Miguel — custo de tokens).

---

## 8. PARTE 6 (~15h05) — confirmação de diretriz de estilo (`42a5412a`, AO VIVO)

- Miguel: captação de diretrizes confusa; quer fluxo "Estúdio entende → propõe → editor confirma sim/não → só então registra".
- Antes: registro automático pós-reescrita com resumo mecânico (fallback genérico confuso).
- Novo: cartão `#style-rule-confirm-card` (textarea editável com a proposta + número da futura Regra #N); `proposeStyleRuleConfirmation` (proposta higienizada — strip de interjeições com `[\s,;:]`, fallback usa instrução original); `confirmAddStyleRule` (safeLocalSet + renderCustomManualRules + flash + status + alert); `dismissStyleRuleCard`. "+ Manual" abre o cartão. Registro automático pós-reescrita ABOLIDO — só com "Sim".
- Validação: node --check OK, espelhos md5-idênticos, simulação 3/3, live ≡ local (458.271 bytes).

---

## 9. PARTE 7 (~15h30) — MANUAL_DE_ESTILO.md reorganizado (`642ecdbd`, AO VIVO)

- Pedido Miguel: manual confuso → "olhada boa, corrigir, organizar, simplificar".
- Diagnóstico: numeração quebrada (#1–22 + 8 sem número + aviso obsoleto + #23–27), detrito ("Lido em 25/07 pelo GPT"), famílias espalhadas.
- Reorganização: 6 famílias temáticas, renumeração #1–#34 (datas preservadas, refs cruzadas atualizadas: #15→#19, #8→#19, #14→#25, #26→#29, #7→#18), síntese operacional de 8 linhas no topo (otimizada para o prompt injetado), detritos fora, crescimento corrigido (#35+). Backup `.bak_20260804_pre_reorganizacao`.
- Verificação de integridade: 27 regras originais + 8 herdadas = 35 itens → 34 numeradas (1 fusão declarada) ✓; 24 ❌ = 24 ✓.
- Site regenerado (manual embutido no build): live ≡ local, 459.942 bytes. O manual novo já alimenta o system prompt de todas as reescritas.

---

## 10. PARTE 8 (~16h05) — banco de fontes MODULAR (`a4777312`, AO VIVO)

- Miguel: partes separadas "transcrições/reportagens/histórico/resumo" com marcar-todos ou individuais.
- Mapeamento: 🎬 CATALOGO_TRANSCRICOES+MAPA_ENTREVISTAS (16K) · 📰 BANCO_DE_LINKS (10,8K) · 🏛️ ONDA2_FICHAS (16K) · 📋 ARQUITETURA_V3 (4K). referencia/ (livros clássicos completos) NÃO injetável (grande demais) — frames clássicos seguem via manual.
- UI: master 🧠 (id chk-consult-canonical-memory) agora liga sub-painel real; "Marcar todos" toggle coletivo; indeterminate em seleção parcial; persistência `miguel_fontes_banco_selection` + restore no boot (initFontesSelection no DOMContentLoaded).
- Injeção: fontesBlock no systemPrompt pós-manual/diretrizes; ordem "fundamentar NESTAS fontes; nunca inventar fato que as contradiga". consultMemory=false → null → nada injetado.
- Validação: 4 conteúdos no HTML ✓, node --check OK, espelhos md5-idênticos, simulação 4/4, live ≡ local (504.561 bytes). Custo máx. ~15k tokens/chamada (opt-in).

---

## 11. PARTE 9 (~16h40) — apagar versão (`ba34c611`, AO VIVO)

- Miguel: 24 versões no cap. 1; quer marcar e apagar para limpar; versão some do menu.
- Implementação: `deleteRevisionVersion(vKey, btnEl)` — 2 toques no próprio 🗑️ (armado 3,2s, sem confirm()); guarda de canônica; exclusão via safeLocalSet; fallback de versão ativa (última restante ou oficial); re-render de tabs/métricas/single/URL/título do Estúdio; menu permanece aberto p/ faxina em sequência; status na faixa do Estúdio.
- Linha do dropdown reestruturada: `row` = botão selecionar (flex-1) + botão 🗑️ (só `type==='revision'` e não-canônica).
- Fix auxiliar: `nextRevisionKey` (máximo+1) substitui contagem em saveDeepSeekRevision/confirmAddStyleRule/convertLastAiToManualRule — evita colisão de R# após exclusões do meio.
- Validação: node --check OK, espelhos md5-idênticos, simulação 5/5, live ≡ local (508.889 bytes).

---

## 12. PARTE 10 (~17h05) — toast + pulso + scroll no gravar (`2905eb31`, AO VIVO)

- Miguel não via o sinal de gravação — a aba dele estava com build anterior à faixa de status (F5 resolve; reforçado mesmo assim).
- `showStudioToast` (fixed top-center, slide-in, auto-hide 4,2s, verde/vermelho), `pulseStudioTitle` (fundo verde ~1,8s no título), `window.scrollTo({top:0, behavior:'smooth'})` no gravar. Ligados em 5 fluxos (gravar R#, canônica ×2, apagar versão, registrar regra; falha também toasta em vermelho).
- Validação: node --check OK, espelhos md5-idênticos, live ≡ local (511.857 bytes).

---

## 13. PARTE 11 (~17h50) — modal do Manual: regra por voz com inteligência + contraste (`7737b562`, AO VIVO)

- Fix contraste: regras custom eram `bg-purple-950/30`+`text-purple-200` sobre creme (ilegível) → fundo branco/texto escuro.
- Fluxo: "Acrescentar" agora processa (`formulateStyleRule` — cadeia de strip de muletas/comandos de voz; "regra" solto só com `:`; legítimos preservados) → confirmação editável → Sim grava (toast+flash+alert) / Não volta. `saveCustomManualRules` via safeLocalSet.
- Numeração custom alinhada ao manual reorganizado: base 34 → próxima regra #35 (6 ocorrências + textos do modal).
- Validação: node --check OK, espelhos md5-idênticos, simulação 5/5, live ≡ local (516.434 bytes).

---

## 14. PARTE 12 (05/08 ~05:20) — Gestor de Capítulos + faxina de versões (`16ab843d`, AO VIVO)

- Miguel: liberdade editorial total no FdI antes do Moka Writer.
- Camada de dados: `getChapterOps/saveChapterOps/applyChapterOps` + cache `_datasetCache` por estado (overrides: renamed/deleted/order/custom em `miguel_book_chapter_ops_<vol>`); renames in place com `_originalTitle` (reversível); rebuild re-aplica `loadChapterPersistentState` (sem recursão — cache setado antes).
- Gestor: modal `#modal-chapter-manager` (reordenar ⬆️⬇️ via ops.order, renomear inline, apagar 2 toques — embedded vira oculto restaurável / custom some com limpeza de 6 chaves de dados), criar capítulo custom (entra no dataset/livro compilado), guarda último visível.
- Faxina: `versionCleanupMode` + `versionCleanupSelection` (Set); checkbox por linha de revisão não-canônica; select-all exceto canônica; bulk delete 2 toques (1 safeLocalSet, fallback ativa, re-render, toast+status).
- Validação: node --check OK, espelhos md5-idênticos, simulação 6/6, live ≡ local (536.858 bytes).

---

## 15. PARTE 13 (05/08 ~05:50) — canônica sem perda de nome (`6b03bba6`, AO VIVO)

- Miguel: "a canônica não pode perder o nome original" + confusão de rótulo ("Kim 4.3 × Antigravity").
- Causa: `makeLastRevisionCanonical` sobrescrevia `ch.versionTag` com "Kimi Canônica (data)" (apagava a identidade).
- Cura: canônica = PONTEIRO p/ versão de origem (`miguel_book_canonical = chave da versão`); menu mostra 👑 na versão NOMEADA; helper `getVersionLabelForKey`; confirmações com o nome; `getCompiledFullBookData` resolve canônica experimental; genérico eliminado (0 ocorrências).
- Validação: node --check OK, espelhos md5-idênticos, simulação 4/4, live ≡ local (538.573 bytes).

---

## 16. PARTE 14 (06/08) — nome original sempre + destaque canônica (`fd55a806`, AO VIVO)

- Vazamento final: `loadChapterPersistentState` aplicava `savedTag` em `versionTag` no boot — tag "Canônica"/"Manual" apagava o nome original. Removida a aplicação da tag (conteúdo segue aplicado). **Cura retroativa:** nomes voltam sozinhos no F5.
- Destaque: `renderMetrics` prefixa "👑 CANÔNICA · " no badge quando `currentVersionKey === getCanonicalVersionKey(...)`; `refreshStudioTitle` prefixa "👑 " no rótulo da versão ativa canônica.
- Validação: node --check OK, espelhos md5-idênticos, simulação 4/4, live ≡ local (539.627 bytes).

---

## 17. PARTE 15 (06/08) — verdade editorial da canônica (`15a979ef`, AO VIVO)

- Miguel flagrou a mentira: canônica exibindo "Kimi 4.3" quando a origem real era uma versão Gemini. Causa: o makeLastRevisionCanonical legado copiava o TEXTO da versão para a Oficial + renomeava — a etiqueta mentia a origem.
- Cura: (1) tornar canônica = ponteiro puro (sem copiar conteúdo/sem renomear; oficial editada persiste o próprio texto sem renomear); (2) detector de verdade no menu de versões (canônica='oficial' + texto idêntico a revisão/exp → banner âmbar + correção de 1 clique `repairCanonicalOrigin` que repõe o ponteiro e limpa o override da oficial — oficial volta ao texto do manuscrito).
- Validação: node --check OK, espelhos md5-idênticos, simulação 3/3, live ≡ local (543.167 bytes).

---

## 18. PARTE 16 (06/08) — sinal de gravação impossível de perder + Resetar Original explicado (`4df0f8fd`, AO VIVO)

- Miguel: "sinalzinho no meio da página + muda a cor do botão de gravar pra verde".
- `showStudioSavedConfirmation(msg)`: card verde central, scale-in/out ~2,4s, z-index 100000.
- `markButtonAsSaved(btn,label)` / `resetButtonToUnsaved(btn)`: dataset origHtml/origClass preserva o estado original; botão fica "✅ Gravado (R#)" + bg-green-600 + ring-2 até `resetSaveButtonsOnEdit()` (ligado ao oninput da textarea) devolver ao normal — sinal "mudanças não gravadas". IDs `btn-gravar-revisao` + `btn-salvar-manual`.
- Resetar Original: `resetChapterToCanonicalOriginal` agora explica no confirm que NÃO apaga R# (só rascunho da sessão) + tooltip + toast; ganhou `resetSaveButtonsOnEdit()`.
- Validação: node --check OK, espelhos md5-idênticos, simulação 4/4, live ≡ local (546.221 bytes).

---

## 19. PARTE 17 (06/08) — correção da chave DeepSeek no cofre unificado

- **Achado:** a `DEEPSEEK_API_KEY` do cofre canônico (`Outros/chaves/agentes_labs/.env.unificado`) estava **morta (401)** — descoberto ao testar as 6 chaves a pedido do Miguel ("todas as chaves estão ativas?").
- **Ação (pedido Miguel: "corrige aí a chave do deepseek, deixa apenas a valida no cofre unificado"):**
  1. Backup: `.env.unificado.bak_deepseek_20260806` (10.258 bytes).
  2. Substituída a linha `DEEPSEEK_API_KEY` pela chave válida viva (a mesma de `Rio Carta Agentes/root/chaves_riocarta.env`).
  3. **Verificado ao vivo:** cofre unificado agora responde **200** em `api.deepseek.com/models`; sha8 `b6c4d4de` bate com a fonte riocarta.
- **Estado final das 6 chaves (testadas ao vivo, sem custo):** Gemini 200 · OpenAI 200 · Anthropic 200 · **DeepSeek 200 (corrigida)** · Kimi (paygo) 200 · GLM 200 → **6/6 VÁLIDAS.**
- **Nota de sincronização:** os espelhos do cofre nos servidores (Tencent `/root/.env.unificado`, NYC, Alibaba) seguem com a chave velha (401) — atualizar quando houver acesso SSH (registrado como pendência operacional).

---

## 20. PARTE 18 (06/08) — DeepSeek corrigida em TODOS os espelhos (pedido Miguel: "deixa chave nova em tudo")

Propagação da chave válida (sha8 `b6c4d4de`) a todos os pontos onde `DEEPSEEK_API_KEY` existia:

| Ponto | Ação | Estado |
|---|---|---|
| **Local canônico** `Outros/chaves/agentes_labs/.env.unificado` | backup `.bak_deepseek_20260806` + substituída | ✅ 200 testado |
| **NYC** `/root/.env.unificado` (198.199.121.136) | backup + `sed` | ✅ 200 testado |
| **Tencent** `/root/.env.unificado` (43.156.151.165) | arquivo `root:root 600` → via `sudo -n` (sem senha): backup + `sed` | ✅ 200 testado |
| **Alibaba** (39.106.184.215) | ❌ **offline** (timeout porta 22) | ⏳ pendente quando voltar |
| **Beijing** (82.156.167.218) | ❌ **offline** (timeout porta 22) | ⏳ pendente quando voltar |
| **Local `.env` (raiz)** | backup + substituída | ✅ 200 testado |
| **Local `Outros/legacy_.env`** | backup + substituída | ✅ corrigido |
| **Local `Outros/chaves/agentes_labs/legacy_chaves_novas.env`** | backup + substituída | ✅ corrigido |
| **Local `Outros/chaves/cafezinho_root/legacy_chaves_novas.env`** | backup + substituída | ✅ corrigido |

**Regra aplicada:** backup `.bak_deepseek_20260806` em CADA arquivo antes de mexer; valor nunca impresso (só sha8 de auditoria).
**Pendência:** Alibaba + Beijing offline — aplicar a mesma correção quando os hosts voltarem (SSH).

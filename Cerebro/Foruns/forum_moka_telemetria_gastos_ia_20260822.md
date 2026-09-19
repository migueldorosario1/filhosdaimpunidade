# Fórum — Moka Reader: telemetria de gastos de IA + trava de tokens + saldo + modelo por chave

- **Data:** 22/08/2026 (16:45 → ~19:10 BRT)
- **Agente:** ZCode/Qwen 3.8 (sessão interativa, workspace ZCodeProject)
- **Ordem do Miguel (resumo):** nas configurações, ícone pra mudar o modelo da IA; página de telemetria reunindo num banco todas as despesas com cada IA/tarefa, com calculadora em dólar E moeda do país (marcador); registro de consumo de tokens em TODA função que use a API do usuário + pequeno informe (pop-up) com "não quero mais ver isso"; nas configurações, ligar/desligar o box de gastos ou ligar só acima de X tokens (default ajustável); trava de tokens por tarefa opcional; o app NÃO PODE TRAVAR se passar do cap ou ficar sem crédito — tem que avisar; ícone de saldo da API quando o LLM permitir; verificar se a página de telemetria já existia.
- **Repo:** `~/ZCodeProject/moka-app` · commit `fc63cb7` (push origin/main, rebase limpo sobre Moka 6.7/6.8)

## Decisões registradas

1. **A página de telemetria NÃO existia** (confirmado): as rotas `/api/metrics/*` são o "Painel de Sócios" (visitas/instalações), coisa diferente. Criada do zero em `/telemetria`.
2. **Local-first:** o ledger fica num IndexedDB separado (`moka_telemetry`, v1) no navegador do usuário — nada vai pra servidor (princípio BYOK do Moka). Custos são estimativas pela tabela de preços (`llm-prices`), não fatura.
3. **Nunca travar:** cap é aplicado em 2 camadas — pré-voo (bloqueia a chamada ANTES de gastar, com aviso traduzido) e corte no meio do stream (preserva o texto já gerado + aviso). Erro/falta de crédito sempre vira aviso, nunca exceção solta. Telemetria é 100% fire-and-forget (falha silenciosa).
4. **Tokens reais quando possível:** OpenAI-compatible (`stream_options.include_usage` com fallback), Anthropic (message_start/delta) e Gemini (usageMetadata) via `onUsage` nos adapters. Sem resposta do provedor → estimativa (~4 chars/token latino, ~1,5 CJK) marcada como "estimado".
5. **Pop-up:** modo default = só acima de 500 tokens (ajustável: sempre / acima de X / nunca). Botão "não quero mais ver isso" desliga de vez (o ledger continua gravando). Erros sempre mostram pop-up.
6. **Saldo:** só DeepSeek expõe saldo via API (`/dashboard/balance`); os outros 10 provedores ganham link direto do painel oficial de consumo (`usageUrl` do registry). Nada de inventar dado.
7. **Moedas:** 13 moedas com taxa aproximada fixa (funciona offline), auto-detecção pela região do navegador; marcador na /telemetria liga/desliga a coluna "dólar + moeda local".
8. **Troca de modelo:** o ícone 🧩 no card de cada chave abre editor inline (com 🔍 que lista modelos do provedor usando a chave já salva) — não precisa re-digitar chave (função nova `updateEntryModel` em config.ts).

## O que está pronto

- ✅ `packages/ai-providers`: `UsageInfo` + `onUsage` nos 3 adapters (complete + stream).
- ✅ `apps/web/src/lib/telemetry.ts`: ledger, prefs, moedas, estimativas, custo, evento global.
- ✅ `ai-client.ts` (livros) e `video/ai-client.ts` (vídeos) + `useTTS.ts` + amostra de voz: TUDO registra consumo (17 tipos de tarefa).
- ✅ `UsageToast.tsx` montado no layout raiz + CSS.
- ✅ SettingsForm: 🧩 modelo por chave, 💰 saldo, seção "💸 Avisos e trava de consumo".
- ✅ Página `/telemetria` (totais, por IA/tarefa/modelo, marcador de moeda, calculadora, CSV, limpar).
- ✅ i18n: `telemetry-strings.ts` (12 idiomas) + `errTokenCap`/`errCapCut` em `messages.ts` (8 idiomas — russo faltava, foi completado).
- ✅ tsc limpo + `next build` verde (23 rotas) + push `fc63cb7`.

## O que falta / próximos passos

- **Teste real do Miguel** (abrir /configuracoes e /telemetria, traduzir uma página, ver o pop-up, mexer na trava).
- Deploy Vercel (automático via push — confirmar que subiu).
- Possível evolução: taxas de câmbio ao vivo (hoje são fixas aproximadas) — só se o Miguel quiser.

## Preciso de você, Miguel

- Nada bloqueante. Só testar e me falar se o pop-up tá do seu agrado (tamanho/posição no canto inferior direito) e se quer o marcador de moeda em mais lugares.

---
Tema Duplo: memória técnica em `Memorias/memoria_moka_telemetria_gastos_ia_20260822.md`.

---

# Adendo — Rodada 2: correções do feedback do Miguel (22/08, tarde)

O Miguel testou e mandou feedback por voz. Tudo corrigido, commitado e NO AR.

## Feedback → correção

1. **🧩 seletor de modelo "entra tudo quebrado":** causa raiz = o editor inline era renderizado DENTRO da coluna estreita `.saved-provider-info` (flex column) no card `.saved-provider-card`. Correção: editor agora é irmão do bloco de ações, abre em **largura total abaixo do card** (`flex:1 1 100%` + `flex-wrap:wrap` no card), botão em formato pílula, lista de modelos **buscada automaticamente ao abrir** e seleção do modelo em 1 clique (salva na hora).
2. **💰 saldo removido POR COMPLETO:** "nenhum provedor expõe crédito de API, então não pode ter esse saquinho de dinheiro". Removidos botão, caixa de resultado, estado e handler no SettingsForm. (A função `checkBalance` ficou no `ai-client.ts` como código morto inofensivo — nenhum import usa.)
3. **Link visível:** ícone 📊 novo (`TelemetryIconButton`) na topbar de **Capa, estante, video e ajuda**, ao lado do ⚙️; nas configurações entrou um **banner destacado** (borda/coloração accent) apontando pra /telemetria.
4. **Ícone 📊 duplicado na página:** a string `tele_page_title` tinha 📊 E o h1 botava outro → removido o emoji da string; h1 agora usa 🤖.
5. **Página = controle das IAs:** /telemetria reescrita como **"Suas IAs"**: topbar padrão (logo + idioma + login + ✕ fechar como configuracoes), seção "Suas IAs registradas" (cada chave com nome, troca de modelo 🧩 e gasto daquela IA), seção gastos por uso completa, tabela de preços `LlmPriceRanking`, link pra configurações completas. 10 strings novas × 12 idiomas.

## Estado

- ✅ Commit `a3db3c9` (9 arquivos, +846/−366), push main, deploy Vercel confirmado.
- ✅ Produção verificada: /, /telemetria, /configuracoes, /estante, /video = 200; marcadores "Suas IAs", `.tele-gear` e `.tele-banner` presentes no HTML vivo.

## O que falta / próximos passos

- Teste do Miguel no aparelho dele (especialmente o editor 🧩 que era a queixa principal).
- Limpeza opcional: remover `checkBalance` morto do ai-client.ts + strings `set_balance_*` órfãs (não bloqueia nada).

## Preciso de você, Miguel

- Nada bloqueante. Só confirmar se o 🧩 agora abre bonito e se a página "Suas IAs" está do seu agrado.

---
Tema Duplo mantido: adendo técnico na mesma memória (`Memorias/memoria_moka_telemetria_gastos_ia_20260822.md`).

---

# Adendo 3 — INCIDENTE + ROLLBACK (22/08, janela ~20:45–21:05)

**O que aconteceu:** com a telemetria no ar no canônico, a **tradução de página de livro quebrou** (reporte do Miguel: a chave funciona, mas a tradução falha). Causa raiz: o streaming passou a enviar `stream_options: { include_usage: true }` no adapter OpenAI-compatible pra capturar consumo real; provedor que não conhece o campo rejeita → streaming morre (e o retry só cobria HTTP 400). Teste de conexão passa porque não é streaming — bate 100% com o sintoma.

**Decisão do Miguel (literal):** "a gente errou ao fazer reformas no site em ação. agora tem que dar rollback em tudo que fizemos hoje, e levar as mudanças para o site espelho."

**Executado na hora:**
1. ✅ ROLLBACK total do dia no canônico: reverts `335e18c` + `96f0713` na main → árvore idêntica a `fc84138` (19/08). Produção verificada: capa 200, `/telemetria` 404, zero marcadores de telemetria.
2. ✅ Todo o trabalho de hoje (rodadas 1+2) segue vivo no ESPELHO: branch `espelho` / repo `moka-espelho` / https://moka-espelho.vercel.app.
3. ✅ Fix da tradução NO ESPELHO (`fcf29e7`): streaming sem `stream_options` (formato pré-telemetria provado em produção); consumo real só se o provedor enviar espontaneamente, senão estimativa. Princípio gravado: **telemetria NUNCA quebra chamada real**.
4. ✅ Bug registrado: `CEREBRO_NODE_BUGS_ATIVOS.md` (BUG-20260822-MOKA-TRADUCAO-STREAM-OPTIONS).

**Estado:** canônico = estado de 19/08 (tradução funcionando como antes). Espelho = telemetria completa + página "Suas IAs" + fix da tradução. Nada volta ao canônico sem o Miguel testar no espelho e aprovar o merge.

## Preciso de você, Miguel

- Testar a tradução de uma página de livro no **espelho** (https://moka-espelho.vercel.app) e me dizer se funcionou — é a prova final do fix antes do merge.

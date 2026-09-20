# Fórum — Incidente: chave Gemini GCP exposta no GitHub público e rotação completa (2026-09-19)

**Sessão:** ZCode/GLM-5.3 · **ID:** ZM-GCP-CHAVE-20260919 · **Abertura:** 19/09 ~16:5x BRT · **Fechamento:** 19/09 17:1x BRT
**Log técnico completo:** `Memorias/memoria_incidente_chave_gemini_gcp_20260919.md`

## O que aconteceu (decisões resumidas)

1. **Alerta do Google (16:26):** e-mail `google-cloud-compliance@google.com` — "Potentially compromised credentials for Google Cloud Platform/API project **Cafezinho Canonico** (id: `gen-lang-client-0200069757`)". Chave `AQ.Ab8RN6…` (formato novo, 53 chars) encontrada exposta na URL pública do commit `8007d2a833b6127a34ffb90c57bbc0f13f5b7b14` do repo **público** `github.com/migueldorosario1/filhosdaimpunidade`, arquivo `Cerebro/subcerebro_antigravity_desktop/sub_cerebro_antigravity_desktop.md` (linha `GCP_AGENT_PLATFORM_KEY=`, gravada ali em 19/06 pelo Antigravity Desktop com a chave "Agent Platform" fornecida pelo Chairman).
2. **Origem da exposição:** o workspace "Antigravity Google" É um repo git cujo remote é o repo público acima; o commit `8007d2a` (16:19 de 19/09, autor local "Refatoracao V4") adicionou 300 arquivos do Cérebro ao branch `deploy-main`. O `.gitignore` cobre `.env*`/`*.bak*` mas **não** blinda `.md` de fóruns/memórias contra valores colados em texto corrido.
3. **Estado da chave velha:** **JÁ DELETADA pelo Google** — prova dupla: chamada `generativelanguage` devolve **401 UNAUTHENTICATED**; e a chave não casa com **nenhuma** das 8 restantes do projeto (conferência via `gcloud services api-keys get-key-string`, comparação sem exibir valores). Nada a revogar manualmente.
4. **Chave nova criada pela sessão (sem browser):** `gcloud services api-keys create` no projeto `gen-lang-client-0200069757` — display name **"Agent Platform Antigravity 20260919"**, uid `4ca21f6b-5f50-4e76-9414-f72cd532c4dc`, **restrita a `generativelanguage.googleapis.com`** (api-target). Teste `models?key=`: **HTTP 200, 50 modelos visíveis**. Formato clássico `AIzaSy…` (a vazada era SA-bound formato `AQ.`; a nova não é SA-bound — mais simples e igualmente funcional; org policy de exposure response cobre os dois formatos).
5. **Instalação nos cofres (Regra Nº 4):** variável `GCP_AGENT_PLATFORM_KEY` adicionada com backup prévio `.bak_pre_gcp_agent_platform_20260919` nos 3 cofres-irmãos: `~/cofre_intake/cofre_intake.env` + os 2 `.env.unificado`. Espelho conferido por sha8 da chave: **idêntica nos 3** (`e5d3f5e7`).
6. **🔴 Crédito pré-pago esgotado no projeto:** `generateContent` devolve **402** "Your prepayment credits are depleted" — com a chave nova E com chave antiga SA-bound do mesmo projeto (prova de que é o **projeto** sem saldo, não a chave). A chave nova autentica perfeitamente; para GERAR texto o Miguel precisa recarregar créditos em **https://ai.studio/usage** (projeto Cafezinho Canonico). Até lá, qualquer consumidor da `GCP_AGENT_PLATFORM_KEY` falha com 402.
7. **Higiene de segredos na árvore pública (scan completo do Cérebro publicado):** além da chave Gemini, achamos e tratamos:
   - **GitHub PAT colado em 3 arquivos** (`Foruns/forum_github_pat_reportagem_multiia_20260905.md`, `Foruns/forum_reportagem_nikolas_parecer_zm_20260905.md`, `Memorias/memoria_github_pat_reportagem_multiia_20260905.md`) — testado: **401, morto/revogado** (diferente do PAT vivo do `Cofres/cofre_github/.env`, que NÃO está versionado). Redigidos com `[REDACTADO 19/09/2026]`.
   - Demais padrões (AIza Pagespeed, sk- Kimi antiga, fixtures `test_contracts.py`): todos **mortos ou fake** — sem ação.
8. **Sub-cérebro corrigido:** o valor `AQ.` foi substituído por ponteiro para o Cofre — regra da casa confirmada (valor de chave JAMAIS em .md; só no cofre + referência).

## O que falta / próximos passos

- **Miguel recarregar créditos** do AI Studio (projeto Cafezinho Canonico) para a chave nova gerar: https://ai.studio/usage — OU decidir usar outro projeto com saldo.
- **Decisão de blindagem do repo público** (ordem necessária, não executado): o branch `deploy-main` publica o Cérebro inteiro (10.679 arquivos) num repo público. Opções: (a) repo virar privado; (b) `Cerebro/` sair da árvore pública via .gitignore; (c) manter e aceitar o risco com redação rigorosa. O histórico antigo com a chave morta segue acessível por SHA direto no GitHub até GC deles — expurgo via `git-filter-repo` (receita da memória de 17/09) é possível mas força push num repo de backup; aguarda ordem.
- Consumidores: **nenhum código consumia** `GCP_AGENT_PLATFORM_KEY` (grep em *.py/*.json/*.env/*.sh vazio) — a chave era "reserva" do Antigravity Desktop; zero quebra operacional pela rotação.

## Links diretos

- Console de credenciais do projeto: https://console.cloud.google.com/apis/credentials?project=gen-lang-client-0200069757
- Créditos/billing AI Studio: https://ai.studio/usage
- Commit da exposição (chave morta, histórico): https://github.com/migueldorosario1/filhosdaimpunidade/commit/8007d2a833b6127a34ffb90c57bbc0f13f5b7b14


---

## Adendo 20/09 ~08:1x BRT (ZCode/GLM-5.3) — GATE ANTI-SEGREDO instalado + auditoria de chaves sk- dos cofres

Ordem do Miguel ("vai") após o incidente. Duas frentes:

**1. Gate anti-segredo (pre-push hook) — `Cerebro/Ferramentas/gate_secrets_prepush.py`**
- Instalado em `.git/hooks/pre-push` dos 2 repos que empurram ao GitHub público: `Antigravity Google` (deploy-main) e `Outros/novo livro` (main). O sync automático do cerebro-miguel passa pelo mesmo script (o hook é chamado pelo `git push`).
- Varre APENAS as linhas adicionadas nos commits do push; padrões: Google (AIzaSy/AQ.), sk- (OpenAI/DeepSeek), sk-ant-, sk-or-v1-, ghp_/gho_/github_pat_, xai-, AKIA. Allowlist: linhas com REDACT/…/exemplo/fake/fixture/dummy/placeholder; fixture `test_contracts.py` excluída. NUNCA imprime valores — só arquivo + tipo.
- Testado 3 cenários: passa limpo sem segredo; BLOQUEIA isca `sk-` (exit 1); BLOQUEIA isca `AIzaSy` (exit 1). Primeira versão da isca com a palavra "FAKE" passou — allowlist a absorveu; isca sem palavra da lista bloqueou certinho.
- Limitação conhecida: cobre o push a partir desta máquina; a barreira de servidor (GitHub push protection) já estava `enabled` no repo público, mas NÃO detectou a chave `AQ.` nova geração — o gate local cobre essa lacuna.

**2. Auditoria das chaves sk- dos cofres (Regra 4) — com correção de método**
- Primeira varredura testou tudo só em api.openai.com e marcou 13 como mortas — ERRADO de método: endpoint errado por provedor. Refeito por provedor:
  - **VIVAS:** OPENAI_API_KEY `sk-…ddAA` (a "ovo-cafezinho" que o Miguel confirmou — única em uso no painel OpenAI, $55.33 gasto acumulado; criada 20/07, sem expiração) · ZCODE_OPENAI `sk-…qOoA` · DEEPSEEK_API_KEY `sk-…bef7` · DEEPSEEK_API_KEY_DSN `sk-…9578` · KIMI_PAYGO `sk-…BD06` (viva em moonshot.ai, 401 em .cn) · KIMI_CODE_ZCODE `sk-…Czs4` e KIMI_VISION `sk-…c9eh` (vivas em kimi.com/coding, 401 em moonshot) · CLAUDE/ANTHROPIC `sk-…1AAA` (200 em anthropic.com) · ZCODE `sk-…3183` (200 em openrouter.ai).
  - **MORTAS de verdade (401 no endpoint certo) → depreciadas:** DEEPSEEK_TEMATICOS `…6690`, DEEPSEEK_DS_LAURA `…6907`, DEEPSEEK_CAFEZINHO_CANONICO `…8762` — renomeadas `_DEPRECADA_20260920_*` no `cofre_intake.env` (únicas ocorrências; os 2 .env.unificado não as tinham), backup `.bak_pre_deprecada_deepseek_20260920`.
  - `sk-…ZMHw/7gxI/72d2`: só existem em logs/artefatos de sessão ZCode (não em cofres) — sem ação.
- **Lição:** testar chave no endpoint do provedor certo; 401 no endpoint errado ≠ chave morta (quase depreciamos Kimi/Claude vivas).

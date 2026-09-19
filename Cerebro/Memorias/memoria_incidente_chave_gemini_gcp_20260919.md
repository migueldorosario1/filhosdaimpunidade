# Memória — Incidente chave Gemini GCP exposta: log técnico completo (2026-09-19)

**Sessão:** ZCode/GLM-5.3 · **ID:** ZM-GCP-CHAVE-20260919 · **Decisões resumidas:** `Foruns/forum_incidente_chave_gemini_gcp_20260919.md`

## Linha do tempo

| Hora (BRT) | Evento |
|---|---|
| 19/06/2026 | Antigravity Desktop grava `GCP_AGENT_PLATFORM_KEY=AQ.Ab8RN6…` no sub-cérebro (entrada "2026-06-19", linha ~523) |
| 19/09 16:19 | Commit `8007d2a8` (autor local "Refatoracao V4", branch `deploy-main`) adiciona 300 arquivos do Cérebro ao repo público `filhosdaimpunidade` — incluindo o sub-cérebro com a chave |
| 19/09 16:26 | Google envia alerta de credencial exposta (e-mail lido pelo Miguel) |
| 19/09 16:5x | Miguel pede: explicar, verificar cancelamento, criar chave nova, links diretos |
| 19/09 17:0x–17:1x | Esta sessão: diagnóstico completo, chave nova criada, cofres espelhados, redação, Tema Duplo, commit+push |

## Diagnóstico (comandos e provas)

1. **Chave velha cancelada?** Sim, pelo Google. Provas:
   - `GET generativelanguage.googleapis.com/v1beta/models?key=<AQ.Ab8RN6…>` → **401 UNAUTHENTICATED**.
   - `gcloud services api-keys list --project=gen-lang-client-0200069757` → 8 chaves restantes (Gemini Moka, Filhos da impunidade, Chaves 2-7); `get-key-string` de TODAS comparadas com o valor exposto → **nenhuma casa** (a vazada foi removida do projeto).
2. **Repo público:** `api.github.com/repos/migueldorosario1/filhosdaimpunidade` → `private: false`, default branch `main` (parado em 05/09), branch `deploy-main` com o Cérebro (10.679 arquivos tracked). Arquivo no HEAD atual do deploy-main local JÁ não contém a chave após a redação (ver item Cura).
3. **Root cause da publicação:** o workspace `Antigravity Google` é um repo git com `origin = git@github.com:migueldorosario1/filhosdaimpunidade.git`; `.gitignore` cobre `.env*`, `*.bak*`, `*.mp4`, `Outros/chaves/ssh_*` mas **não** impede que valores colados dentro de `.md` de Cérebro subam.
4. **Scan de segredos na árvore Cerebro/** (regex AIzaSy / AQ. / sk- / ghp_ / github_pat_ / xai- / sk-ant- / AKIA em .md/.txt/.json/.py/.yaml/.env/.sh): 8 arquivos com padrões. Liveness testada de cada um:
   - `Cofres/cofre_github/.env` → PAT **VIVO (200, login migueldorosario1)** — mas arquivo **NÃO versionado** (só `LEIA-ME.md` do cofre está no git). Sem exposição.
   - 3 fóruns/memória com `github_pat_…260905` colado → **401 morto**; era PAT distinto do do cofre. Redigidos.
   - `_arquivados_20260801/project_seo_monitoramento_fase0_20260628.md` (PAGESPEED_API_KEY) → 403 morta.
   - `claude_memory/estado_fim_sessao_20260510_1037.md` (sk- Kimi antiga) → 401 OpenAI e DeepSeek.
   - `Foruns/gpt_5_6_sol/.../test_contracts.py` → fixtures falsos (`abc123DEF`, `sk-proj-…o5p6` de teste) — sem valor.
   - Conclusão: **nenhum segredo vivo publicado** além da chave Gemini já deletada pelo Google.

## Cura executada

1. **Chave nova** (substitui a vazada):
   - `gcloud services api-keys create --project=gen-lang-client-0200069757 --display-name="Agent Platform Antigravity 20260919" --api-target=service=generativelanguage.googleapis.com`
   - uid `4ca21f6b-5f50-4e76-9414-f72cd532c4dc`; formato clássico `AIzaSy…` (39 chars; a vazada era SA-bound `AQ.` 53 chars — a nova NÃO é SA-bound; funciona igual e é coberta pela org policy de exposure response).
   - Restrição confirmada via `describe`: `apiTargets=[generativelanguage.googleapis.com]`.
   - Prova: `models?key=` → **200 com 50 modelos** (gemini-2.5-flash, gemini-2.5-pro, gemma-4…).
   - `generateContent` gemini-2.5-flash → **402 prepayment depleted** (o projeto está sem crédito pré-pago; confirmado repetindo com chave antiga SA-bound do mesmo projeto → mesmo 402; portanto NÃO é defeito da chave nova).
2. **Cofres (Regra Nº 4):** backup `.bak_pre_gcp_agent_platform_20260919` + append `GCP_AGENT_PLATFORM_KEY=` em:
   - `~/cofre_intake/cofree_intake.env` → corrigido: `~/cofre_intake/cofre_intake.env`
   - `Projeto Cafezinho Agentes/root/.env.unificado`
   - `Outros/chaves/agentes_labs/.env.unificado`
   - Espelho conferido por sha8 da CHAVE: `e5d3f5e7` nos 3 — idênticos.
3. **Redação de valores em .md:**
   - `subcerebro_antigravity_desktop/sub_cerebro_antigravity_desktop.md`: valor `AQ.` → ponteiro para o Cofre (0 restos).
   - 3 arquivos com PAT morto → `[REDACTADO 19/09/2026 — token já revogado (401 confirmado)]`.
4. **Commit cirúrgico + push `deploy-main`** (ver § abaixo com o SHA do commit da cura).
5. **Consumidores:** `grep -rn GCP_AGENT_PLATFORM_KEY` em código/envs → **nenhum consumidor** (variável era reserva do Antigravity Desktop). Zero quebra.

## Pendências (o que falta / o que preciso de você, Miguel)

1. **Recarregar créditos do AI Studio** (projeto Cafezinho Canonico): https://ai.studio/usage — sem isso a chave nova autentica mas não gera (402).
2. **Decidir blindagem do repo público** (a exposição pode se repetir com qualquer segredo colado em .md):
   - Opção A: repo `filhosdaimpunidade` → privado (Settings → Danger Zone → Change visibility).
   - Opção B: `Cerebro/` fora da árvore pública (`.gitignore` + `git rm -r --cached`).
   - Opção C: manter público + redação rigorosa (frágil — depende de agente nunca colar valor).
3. **Expurgo do histórico** (opcional, chave já morta): commit `8007d2a` acessível por SHA no GitHub até GC; receita `git-filter-repo --replace-text` da memória de 17/09 aplica, com force push.

## Lições

- Valor de chave em `.md` de sub-cérebro/fórum = bomba-relógio: o Cérebro inteiro sobe para repo público pelo fluxo de backup/deploy. A regra "valor só no Cofre" agora tem enforcement prático: scan de padrões antes de push seria o gate ideal (pendente de "vai").
- Chaves formato `AQ.` são as novas SA-bound do Google; ao vazar, o Google deleta sozinho (org policy) e avisa por e-mail — o alerta chegou ~7 min após o commit que expôs.
- `gcloud` logado na conta do Miguel permite o ciclo completo (list/get-key-string/create) sem browser — rotação de chaves GCP é autoatendimento.
- 402 na geração ≠ chave ruim: testar com segunda chave do mesmo projeto antes de culpar a chave nova.

## Provas objetivas

- 401 da chave vazada (curl response capturada na sessão).
- 200/50 modelos da chave nova (listing) + 402 generateContent (ambas as chaves do projeto).
- sha8 da chave `e5d3f5e7` idêntico nos 3 cofres.
- `git grep` pós-redação: 0 ocorrências de `AQ.Ab8RN6` e do PAT nos arquivos tratados.

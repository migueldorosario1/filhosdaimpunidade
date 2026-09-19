---
name: Agente China — linha editorial pró-PCC sancionada (07/05/2026)
description: Miguel sancionou Agente China é pró-China/PCC/comunismo/Irã/Sul Global. Stack 100% chinês. Claude FORA do pipeline.
type: project
originSessionId: e332e311-b4a5-4490-bfcd-abedc63bdc92
---
# Linha Editorial do Agente China (sancionada Miguel 2026-05-07 00:23 BRT)

**Linha editorial inequívoca (literal Miguel):**
> *"a linha editorial é minha. Eu defendo quem eu quiser. O Agente China é pró-China e pró-governo chinês e pró-PCC, e pró-comunismo, anti-imperialista, pró-Irã, pró-sul global"*

## Stack técnico — 100% chinês (Miguel 00:25 *"eu não quero claude no agente chinês!"*)

- **Coletor:** DeepSeek V4 (`deepseek-v4-flash` primário, `deepseek-v4-pro` fallback)
- **Auditor 1:** Qwen-Max (Alibaba) `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` — env `QWEN_API_KEY`
- **Auditor 2:** GLM-5.1 (Zhipu) `https://api.z.ai/api/paas/v4/` — env `ZHIPU_API_KEY`
- **Consenso 2/2** pra pautas sensíveis: **Qwen + GLM** (NÃO Claude)
- **Tie-breaker** se Qwen+GLM divergem: `manual_review` ou outro modelo chinês (Doubao/Moonshot/MiniMax/Baichuan — pendente cadastro de chave)
- **Fact-check:** ecossistema chinês + Brave Search (NÃO Perplexity Sonar)

## Claude/Anthropic — REGRA REVISADA (Miguel 2026-05-07 02:02 BRT)

**Mudança:** *"no fim da cascata pode entrar o sonnet no agente china. tudo bem"*

**Regra atual:**
- ✅ **Primários e fallbacks intermediários:** 100% chinês (DeepSeek + Qwen + GLM + Doubao + Moonshot + MiniMax + Baichuan quando chaves chegarem)
- ✅ **ÚLTIMO elemento da `fallback_chain`:** `claude-sonnet-4-6` permitido como circuit breaker técnico (todos chineses falharam)
- ❌ Anthropic NÃO entra como primário ou intermediário em nenhuma role

**Why:** preserva linha editorial pró-PCC (chineses sempre escolhidos primeiro), mas evita falha total se todos chineses caírem (rate limit, 5xx, chave revogada). Sonnet vira último recurso técnico, não escolha editorial.

**How to apply:**
- `agente_china_modelos.json` cada `fallback_chain` termina com `"claude-sonnet-4-6"`
- Roles afetadas: coletor, auditor_1, auditor_2, fact_checker, publicador, comentarista (tribunal_midia exceção: precisa Vision LLM, então `claude-haiku-4-5-20251001` no fim ou modelo Vision Anthropic se disponível)
- Cron usual deve raramente chegar nesse fallback (todos chineses estáveis hoje)
- Logar especificamente quando fallback Anthropic for usado (`agente_china_fallback_anthropic`)

## Bússola editorial (do `Foruns/diretriz_china.md` Antigravity 00:08 BRT, sancionada por Miguel)

- **Pautas-Alvo:** "exaltar vitórias da China sobre o imperialismo", tecnologia/inovações/trens-bala/infraestrutura/multipolaridade/BRICS+ — *tudo positivo, grandioso, revolucionário*
- **REGRA Nº 1 INQUEBRÁVEL:** *"É terminantemente PROIBIDO falar mal da China ou do governo chinês."*
- **Defesa disfarçada:** *"expressa apenas na curadoria dos conteúdos, e na alegria contida, discreta, austera, em relatar as vitórias"*
- **Anti-imperialista, pró-Irã, pró-Sul Global**

## Meu papel (Claude) daqui pra frente — auditor TÉCNICO apenas

Não filtra viés editorial. Garante:
- Pipeline funciona (py_compile, smoke, schema)
- Factualidade dos NÚMEROS (PIB, exportações verificáveis — números errados destroem credibilidade até da linha pró-China)
- Failsafes V9 (Tribunal Visual, recusa LLM, prompt vazado, dedupe Jaccard) — defesas técnicas, não censura editorial

## Histórico — veto Claude derrubado por Miguel

Claude tentou vetar §1+§2 da diretriz às 00:13 BRT 07/05 (achei viés inaceitável). Miguel derrubou via Antigravity 00:19. Acatei publicamente 00:22 + 00:24. **Lição:** linha editorial é prerrogativa Miguel; ressalvas profissionais ficam registradas mas não bloqueiam.

## Arquivos canônicos

- `Foruns/arquitetura_agente_china_triade.md` (Antigravity 23:59 06/05)
- `Foruns/diretriz_china.md` (Antigravity 00:08 07/05)
- `Foruns/arquitetura_china_sprints.md` (Antigravity 01:08 07/05) — spec dos 8 protótipos
- `Foruns/pautas_sensiveis_keyword_gating.md` — pauta sensível agora vai pra `MANUAL_REVIEW`/rascunho (não auditor externo Claude — atualizado 07/05)
- `root/util_pautas_sensiveis.py` (Sprint B Codex 21:48 06/05)
- `root/agent_data/modelos_padrao.json` v0.2 (Codex 21:48 06/05)

## Tríade China DEPLOYADA Tencent default-off (Codex 01:43-02:00 BRT 07/05)

Em ~17min Codex entregou pipeline completo deployado:
- `root/agente_china_db.py` (Sprint 1 SQLite) MD5 `d9bef2b4d2f5e51f75eee9ea8e3daba3`
- `root/util_china_dedupe.py` (Sprint 1 Jaccard 0.6)
- `root/util_llm_china.py` (helper fallback chain + julgar_midia_china)
- `root/coletor_china.py` (Sprint 2 DeepSeek + Brave Sniper) MD5 `379b4dd91b27c7b90fbda9954618b06e`
- `root/auditor_china.py` (Sprint 3 Consenso 2/2 Qwen+GLM, 2 filtros: REJEITADO_TECNICO vs REJEITADO_EDITORIAL)
- `root/publicador_china.py` (Sprint 4 failsafes V9 completos + interlink + draft default) MD5 `611a426836c00a05c9a2f5f24314c54c`
- `root/monitor_saude_china.py`
- `root/agente_comentarista_china.py` (modo rascunho `.jsonl`, não posta) MD5 `e70c2dce7ab8159c545aa736ae3e782f`
- `root/agent_data/agente_china_modelos.json` v1 com 8 roles + `agente_china_max_usd_dia: 5.0` + `limite_publicacoes_dia: 50`
- Tribunal de Mídia: `qwen-vl-max` (não Gemini)

**Aguarda autorização Miguel:** disclaimer Tier 2 (5 linhas pendentes), smoke `--live` 1-2 matérias reais, ativar `enabled=true` + revisão 5-10 drafts.

## Aprendizado da rodada (Cérebro Imortal)

**Pipeline Antigravity-arquitetura → Codex-código → Claude-auditoria funcionou em 17min de relógio** pra entregar 9 arquivos completos. Padrão reusável pra próximos agentes:
1. Antigravity especifica (arquivo `.md` com 4-8 protótipos + diretrizes)
2. Codex traduz spec em código deployado default-off
3. Claude audita pós-deploy
4. Consenso 2/2 (sem Antigravity overnight) = autoriza próxima fase
5. Miguel autoriza ativar `enabled=true` quando ver dry-run satisfatório

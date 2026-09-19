---
name: Pilar 1 Eleições — refatoração modelo duplo v1.1 DEPLOYADA 2026-04-24
description: Refatoração completa do agente_eleicoes em modelo duplo (coletor + produtor + banco intermediário + Cartão de Integridade + Validator dupla camada Fail-Fast). CONTRATO_ELEICOES.md v1.1 vigente. Deploy Tencent feito, aguardando primeiro draft real do produtor novo.
type: project
originSessionId: 3eaee7a7-8155-4db4-8752-5afd0796d8a9
---
Refatoração do agente_eleicoes completa e deployada. **Fonte canônica: `CONTRATO_ELEICOES.md v1.1`** na raiz do projeto. Ponteiros principais abaixo.

**Why:** Padrão do projeto (Miguel, 2026-04-24): todos agentes devem ser modelo duplo (coleta separada da redação, com banco intermediário). O agente eleições era verticalizado; foi o primeiro refatorado.

**Artefatos finais (local + servidor Tencent):**
- `coletor_eleicoes.py` (MD5 `779bf0b9...`) — Brave Search + Jaccard 0.60 + banco intermediário com logs [NEW]/[DUP]/[SKIP]
- `agente_eleicoes_produtor.py` (MD5 `65faa768...`) — pipeline 23 passos conforme contrato I-E1; C3 híbrido (imports defensivos do motor_publicador/legado); status=draft hardcoded com TODO
- `cartao_integridade.py` (MD5 `1caf0ea7...`) — schema dict + extração determinística regex + Regra de Degradação (OK/ALERTA_CARTAO/CARTAO_INCOMPLETO_REVISAVEL/DESCARTADO)
- `validator_numeros_eleicoes.py` (MD5 `2f61ae45...`) — dupla camada Fail-Fast (preliminar pré-imagem + final pré-POST) + whitelist técnica §5.5 (11 padrões)
- `banco_eleicoes.db` (MD5 `e2259eb8...`) — schema `pautas` com CHECK constraint (5 status) + idx_status + idx_data

**Artefatos PRESERVADOS (não apagar sem nova deliberação):**
- Local: `agente_eleicoes_legado.py`, `coletor_eleicoes_rascunho_antigravity_20260424.py`, `agente_eleicoes_produtor_rascunho_antigravity_20260424.py`, `banco_eleicoes_rascunho_antigravity_20260424.db`
- Servidor: `agente_eleicoes.py` (MD5 `dea9d2bd...` — é o legado, cron pausado)
- Servidor: `util_tse.py` + `banco_tse.db` intactos (fundação do Pilar 1)

**Como retomar:**
1. **LER CONTRATO_ELEICOES.md primeiro.** É a constituição — invariantes P0, Cartão, cascata de imagens bifurcada, dupla validação. Vigente desde 2026-04-24 14:25.
2. Ler §14+§15 do `forum_enxame_eleicoes.md` (emendas ChatGPT + aprovação final Miguel).
3. **NÃO TOCAR** no `agente_eleicoes.py` do servidor (é o legado preservado).
4. **NÃO REATIVAR** a linha 82 do crontab até Miguel aprovar primeiro draft real em produção e mandar reverter `status=draft → publish`.
5. Crontab tem linha comentada (PAUSADO 2026-04-24 12:20). Reativação envolve 2 linhas novas: coletor `*/30` + produtor `0 9,21`.

**Smoke test local concluído com sucesso (§7 exit criteria):**
- Coletor: 16 NEW + 3 DUP_SIM (um com sim=1.00) — Jaccard funcionando.
- Validator Preliminar: **capturou 3 alucinações reais** (45.5, 42.4, 35.8 inventados pelo gpt-5-search) — Fail-Fast validado na prática.
- Cartão: classifica OK/REVISAVEL conforme snippet, tipo_disputa detectado, extração regex de cenários funcional.

**Deploy Tencent:**
- Backup remoto não foi necessário (nenhum arquivo com mesmo nome pré-existia no servidor — o legado tem nome diferente).
- rsync seguro (§10 regra #1 sem -a/-o/-g) + chown root:root + chmod 644.
- MD5 local==servidor bateu 100%.
- Coletor no Tencent: 18 NEW + 3 DUP_SIM.

**Pendente (próxima sessão retoma daqui):**
- BG `bu7j5m85l` rodando produtor no Tencent — primeiro draft real em produção. Aguarda conclusão.
- Após draft criado, **Miguel inspeciona** no `/wp-admin/post.php?post=<ID>&action=edit` e dá parecer editorial.
- Se OK → próximo passo é reverter `status=draft → publish` + redeploy + reativar cron.
- Se houver ajuste → iterar.

**Regra nova sugerida pelo ChatGPT (§14 do fórum, pendente de formalização no CLAUDE.md):**
> *"Toda refatoração de agente existente precisa ter uma matriz de paridade funcional antes do código. A arquitetura pode mudar, mas nenhuma capacidade do legado pode desaparecer sem decisão explícita de Miguel."*

Recomendação: adicionar como regra #7 em CLAUDE.md §10. Evita que a regressão funcional do Antigravity (que motivou esta refatoração) aconteça de novo em outros agentes.

**Backup do contrato:** `CONTRATO_ELEICOES.md.bkp-v1.0-20260424_1418` preservado. Política de limpeza em 30 dias de produção estável.

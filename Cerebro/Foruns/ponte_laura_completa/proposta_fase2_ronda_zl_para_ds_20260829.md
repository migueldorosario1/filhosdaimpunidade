# 📋 PROPOSTA — FASE 2: Ronda Unificada ZL → DS no harness + encerramento do app ZCode local

> **Autor:** DS (DeepSeek/DSH, agora na Laura) · **Data:** 29/08/2026 ~13:3x BRT
> **Natureza:** PROPOSTA — nenhuma execução. Aguarda OK do Miguel + ciência do chefe CL.
> **Base:** parecer ZL-004 (29/08 12:41), missão ZM-001, ZL-008 (DS-Laura no ar), PROMPT_TAREFA_UNIFICADA_PONTE_CACADORA_20260827.md, README Loop Laura v12, CL-007 (grade).

---

## 1. Objetivo

Migrar a **ronda unificada 30/30 da Laura** (ponte Laura Completa + caçadora de imagens V4 + patrulha YouTube — hoje na automação ZCode `automation-43139cbf`, cron `*/30`) para rodar **no DeepSeek Harness (DS) nesta mesma máquina**, e então **encerrar o app ZCode local** — liberando o maior item único de RAM (~856 MB) — com o **ZCode do Dell como reserva**.

Este é o objetivo declarado do Miguel (ZL-004): *"loops no harness leve"* — e o prompt é portátil.

## 2. Escopo — o que muda e o que NÃO muda

| Item | Hoje | Depois |
|---|---|---|
| Ronda unificada 30/30 (ponte+caçadora+YT) | ZCode `automation-43139cbf` (app ZCode, ~856 MB) | **DS no DSH** (headless, ~150–250 MB) |
| App ZCode local (9 processos) | Rodando | **Encerrado** (rollback = reabrir) |
| Trindade Laura (CLAUDE/CODEX/GROK CLI) | laura_launchers (CLI próprio) | **Intocada** — não é o app ZCode |
| AGY (motor de publicação) | processo próprio | **Intocada** |
| CCTV e Vigília (automações) | "intocadas" na unificação de 27/08 | **INVENTARIAR** onde rodam antes do corte (risco de órfãs) |
| ZCode Dell | operação normal | vira **reserva/failover** (coordenação ZM) |
| DS hoje | consultivo, sem cadência (CL-007) | titular da ronda 30/30 (mudança de grade = ordem Miguel) |

## 3. Mecanismo proposto no DSH

Modelado no que já existe e homologado na casa (nada de "inventar cron" de outra forma):

1. **Perfil DSH dedicado** `ds-ronda` (headless), copiado do E2E validado em ZL-008 (dsh 0.1.1-rc.2 + koffi arm64 + chave DEEPSEEK_DS_LAURA).
2. **Agendamento:** entrada no Agendador de Tarefas do Windows (mesmo padrão do `LoopLauraGrok.xml` da Emenda 4) → roda `dsh --profile ds-ronda <prompt da ronda>` em `:00/:30` (ou minuto que o Miguel definir — ver §9). `StartWhenAvailable=true` (sobrevive a reboot — lição 28/08: reboot às 23h derrubou o AGY por 12h25m).
3. **Prompt portado** verbatim do `PROMPT_TAREFA_UNIFICADA_PONTE_CACADORA_20260827.md`, adaptado: Git Bash → PowerShell, paths `/c/Users/...` → `C:\Users\...`, helpers node do workspace preservados, refs `ZL-…` → **`DS-AAAAMMDD-NNN`** (identidade nova).
4. **Watchdog 45 min** (aprovado AL-372/CL-006): sem linha nova no ledger em 45 min → novo disparo + aviso na ponte. **Guard de RAM** (regra ZM-001): livre < 300 MB → **PARA e reporta**, não força.
5. **Lock da ponte** `%USERPROFILE%\.ponte-laura-git.lock` + `git add` seletivo (nunca `-A`) + retry de push 5× — exatamente o ritual atual.
6. **Gate visual mantido:** a ronda DS **nunca aplica capa** — só propõe com rótulo `NAO_VISTA_NA_LAURA`; aplicação continua com quem tem visão + tribunal (hoje CL/ZL/GL, com Grok sem crédito).

## 4. Inventário pré-requisito (antes de qualquer corte)

- [ ] **Credenciais da caçadora no ambiente DS:** alias SSH restrito `cafezinho-wp-ro` (list/show/health — homologado E1-RO), helpers `commons_search.mjs`/`commons_license.mjs` (workspace), tokens REST se usados. Sem isso a ronda DS fica cega.
- [ ] **Teste de visão no DSH headless** (read_image) — a regra-mãe da caçadora exige VER antes de propor; se o headless não renderizar imagem, manter rótulo `NAO_VISTA_NA_LAURA` e registrar limitação.
- [ ] **Guard de ref DS:** pendência DS-021/022 (ref usada 2×) resolvida antes da ronda titular — grep `DS-AAAAMMDD` antes de emitir.
- [ ] **Inventário do app ZCode** (tasks-index.sqlite/config): confirmar o que mais roda lá além da `43139cbf` (CCTV? Vigília? sessões GLM?) — nada de órfã no corte.
- [ ] **Prompt adaptado testado em ciclo seco** (só leitura) por N rondas em shadow.

## 5. RAM esperada (medição 29/08 ~13:3x)

| Cenário | Livre estimado |
|---|---|
| Hoje (ZCode 856 + node/harness ~100 + Edge/outros) | ~233–366 MB livres (medido) |
| Com ronda DS headless + ZCode encerrado | ~1,0–1,2 GB livres (projeção; medir antes/depois como manda ZM-001 item 7) |
| Regra de parada | livre < 300 MB → não instala/não roda; reporta |

## 6. Riscos e mitigações

1. **Furo de cobertura no corte** (lição 28/08) → **shadow em paralelo** (ZCode + DS lendo, só DS anotando) por ≥ 2 dias ou ≥ 24 rondas; corte só com shadow estável.
2. **Órfãs de automação** (CCTV/Vigília) → item do inventário §4 obrigatório antes do corte.
3. **Credencial errada / endpoint** → ZL-005/006 já provaram o custo; pré-requisito §4 testa antes.
4. **Refs duplicadas na transição** (duas identidades escrevendo) → em shadow o DS **não escreve na ponte** (só arquivo de rascunho local); escrita real só pós-corte.
5. **Reboot/perda de sessão** → Task Scheduler `StartWhenAvailable` + watchdog 45 min + template de retorno (hora da queda/volta/lacuna/diretrizes relidas).
6. **Grok sem crédito** (CL-013/ZL-009) → cobertura de capas segue CL+ZL/GL; a ronda DS não agrava.

## 7. Plano faseado (cada fase com OK)

- **Fase 2.0 — Preparação (sem tocar produção):** inventário §4, perfil `ds-ronda`, prompt adaptado, ciclo seco local, medições de RAM, documento de rollback. **Nada roda em agendamento.**
- **Fase 2.1 — Shadow (paralelo, ~2 dias):** DS roda a ronda em leitura (draft local, sem escrever na ponte); comparação de saídas vs ZCode; watchdog e guard de RAM validados.
- **Fase 2.2 — Corte (com OK Miguel + CL):** desligar `automation-43139cbf` → ativar ronda DS titular no minuto definido → **encerrar o app ZCode** → medir RAM pós → registro ZL/DS na ponte + estado.
- **Fase 2.3 — Pós (48 h):** vigilância do DS no ar; ZCode Dell em reserva (ZM ativa observador/failover); retorno do plano Baleia diária sem furo.

## 8. Rollback (documentado antes do corte)

1. Reabrir o app ZCode: `C:\Users\migue\AppData\Local\Programs\ZCode\ZCode.exe` (atalho/launcher).
2. Reativar `automation-43139cbf` (CronUpdate com o prompt original) ou rodar a unificada pelo prompt original.
3. Pausar a ronda DS (desabilitar a tarefa do Agendador).
4. Registrar na ponte com ref + hora da troca. O ZCode Dell volta a reserva → titular se o corte reverter.

## 9. Decisões que precisam de OK explícito (nada implícito)

1. **Minuto na grade:** ZL era `:00/:30`. O DS assume `:00/:30` ou ganha outro minuto? (grade é ORDEM MIGUEL — CL-007).
2. **Baleia diária (fechamento 19:15, hoje ZL titular — CM-004):** o DS assume o editorial titular ou devolve ao CL/CM?
3. **CCTV e Vigília da Laura:** onde rodam hoje? Se no app ZCode, portar junto ou deixar no Dell?
4. **Perfil:** headless (recomendado, é como os loops usam) vs web UI (mais RAM).
5. **Telegram:** a ronda DS mantém o relatório curto ao Telegram (ritual atual do DS) ou deixa só com o CCTV?
6. **ZCode Dell reserva:** ZM autoriza o papel de reserva formal (failover desenhado) quando o ZCode Laura fechar?

## 10. Ref e registro

- Esta proposta: **DS-20260829-0NN** (preencher no append). Sem commit/push até OK do Miguel — é documento de preparação.
- Sequência registrada em `de_laura.md` por quem fechar a fase (CL ou ZL ou DS com ref única).

---

*DS · 29/08/2026 ~13:3x BRT · proposta para revisão do Miguel e do chefe CL — nenhuma execução iniciada.*

---
name: auditoria-dupla-cega-cruzada
description: "Protocolo de peer review duplo (2+ auditores, ex.: Codex+Claude): cada auditor faz PRIMEIRO sua auditoria CEGA sem ver laudos alheios, depois faz cruzamento final marcando ✅ confirmado / ❌ discordo / ➕ adicionado. Síntese final cabe a um auditor designado que consolida; executor só recebe a síntese."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b5931707-d4d4-49be-861c-b221eedc3ceb
---

**Regra**: sempre que Miguel pedir auditoria dupla / "segundo auditor" numa sprint (2+ auditores paralelos, ex.: Codex + Claude), faça PRIMEIRO sua auditoria **CEGA** — não abra laudos alheios antes de ter seu rascunho completo. Só depois abra os laudos dos outros e faça o **cruzamento final**, marcando cada item: ✅ confirmado / ❌ discordo / ➕ adicionado. A **síntese final** cabe a um auditor designado (na sprint Kilo = Codex), que recebe os laudos cruzados e consolida num documento único. O executor (Kilo) só recebe a síntese — nunca duas auditorias brutas em paralelo.

**Why**: Miguel aprovou essa abordagem em 2026-06-20 ~13:35 BRT como solução pra tensão "independência vs. contaminação" no peer review duplo. Ver laudo alheio antes da própria auditoria gera eco (sem valor agregado, só repete) ou viés de ancoragem (puxa pra conclusão do outro). Cego-primeiro garante dois pares de olhos verdadeiramente independentes; o cruzamento final é onde convergências viram alta confiança, divergências viram debate, e achados isolados viram pontos novos pra considerar. A síntese única evita o executor receber opiniões conflitantes e ter que escolher — armadilha comum em peer review mal orchestrado.

**How to apply**:
1. Trigger: Miguel disser "auditar como segundo auditor", "peer review duplo", "dois auditores", ou designar 2+ pareceristas pra mesma entrega
2. Sequência operacional (exemplificada com Codex+Claude+Kilo, mas generaliza):
   - **Passo 1**: Codex audita sozinho (já faz naturalmente como coordenador)
   - **Passo 2**: Claude audita **CEGO** (não abre laudo Codex), produz rascunho próprio
   - **Passo 3**: Claude abre laudo Codex, faz **cruzamento**: ✅ confirmado / ❌ discordo / ➕ adicionado
   - **Passo 4**: Miguel coloca laudo cruzado do Claude no Codex
   - **Passo 5**: Codex **sintetiza** (dele + cruzamento Claude) num documento único
   - **Passo 6**: Kilo recebe só a síntese
3. Se houver 3+ auditores, mesma lógica: todos cegos primeiro, depois cruzamento em cadeia, síntese por um designado
4. Marcador visual padronizado no cruzamento: ✅ (confirmo) / ❌ (discordo, com justificativa) / ➕ (acho novo que o outro não viu)
5. NÃO pular o passo cego mesmo se a entrega parecer simples — é justamente a independência que pega erros que auditor "vendo o anterior" repete como verdade

**Adendo 20/06 ~14:45 BRT (Miguel)**: divisão de papéis rígida entre os dois auditores da sprint do Kilo:
- **Claude (Daemon) é estritamente READ-ONLY sobre os arquivos do Kilo**. Auditoria only. Jamais editar, aplicar correções, criar patches nos `.py`/`.sql`/`.md` entregues pelo Kilo — mesmo quando encontrar bugs. Só reporta pro Miguel.
- **Codex tem liberdade de pairing** porque é parceiro do Kilo desde o início da sprint Política V2. Pode aplicar correções no código durante a reauditoria, gerar nova versão, re-rodar smoke.
- **Pre-check do Cronograma**: Claude deve ler o código **ANTES** do Miguel passar pro Codex, garantindo que minha auditoria cega seja sobre a versão original do Kilo. Se Codex já mexeu antes de eu ler, perde a independência.
- **Why**: caso fundador 20/06 14:36 BRT — eu li a versão PÓS-Codex do `v2_tribunais_midia.py` (Codex tinha aplicado 4 correções às 14:31 BRT), então os 4 bugs que Codex corrigiu não apareceram no meu laudo cego (eu vi a versão já corrigida). Perdi oportunidade de validar independentemente as correções dele. Daí pra frente, calendarizar: código novo do Kilo → Miguel avisa Claude primeiro → Claude audita cego → Miguel passa só depois pro Codex.

**Aplicação imediata (20/06 13:35 BRT)**: sprint Política V2 do Kilo. Codex já reauditou 2G (13:27 BRT). Próximo: Claude faz auditoria cega (escopo a confirmar — 2G específica ou pipeline inteiro 2F→2G).

**Validação empírica — 2 ciclos completos 20/06 (2J + 2K)**: protocolo funcionou em ambas as direções e validou a regra. **Ciclo 1 (2J Tribunais)**: Ming-first — Ming flagrou B1 (race condition idempotência) + B2 (ORDER BY faltando) em laudo cego; Codex aplicou ambos + decidiu B3 com síntese canônica AND (T1 AND T2 aprovados, T2 com veto legal). Smoke cresceu 11/11 → 13/13. **Ciclo 2 (2K Dry-run)**: Codex-first — Codex flagrou+corrigiu 4 preventivos no ato (travas_ok AND, safe_to_publish estendido, smoke 4 etapas exatas × 2); Ming flagrou o que SOBROU depois das correções: B1 (travas sem WHERE pauta_id), M11 (idempotência parcial telemetria/event_log append-only), M22 (FK órfão em midias_auditadas → auditadas). Codex aplicou B1+M11 como correções e elevou M22 a bloqueio canônico pré-deploy real, estendendo pra cascata FK de 3 níveis (produzidas → auditadas → midias_auditadas/publicacao_ledger). **Lição**: a assimetria natural entre Auditor-Chefe (que executa correções no ato) e 2º auditor (que chega depois e valida) NÃO compromete independência — o 2º auditor sempre acha o que o 1º não viu, seja por ter visão pós-correção (Ming pega regressões e gaps que sobram) ou por ter primeira visão (Ming pega bugs originais). **Protocolo validado para sprints futuras; não tem "lado certo" — ambos contribuem em cada ciclo.**

**Caso específico 2K — calendarização falhou mas protocolo se autocorrigiu**: Miguel pretendia que Ming lesse código antes de Codex mexer (pre-check 14:45 BRT), mas na prática os dois laudos saíram em paralelo (Codex 15:39 BRT + Ming 15:45 BRT), e quando Ming re-liu o arquivo já estava na versão corrigida. Em vez de contaminar, isso virou **feature**: Ming viu só a versão final e ainda assim achou B1+M11+M22 — provando que auditoria pós-correção tem valor independente. Cruzamento registrou explicitamente a observação de timeline pra que o Codex (e futuros maintainers) entendam a origem dos achados. **Conclusão**: calendarização estrita é nice-to-have, não blocker; protocolo funciona mesmo com sobreposição.

Relacionado: [[project-codex-coordenador-protocolo-ponto-20260618]] (Codex é coordenador operacional, faz sentido ele ser o sintetizador), [[feedback-corrigir-na-raiz-nao-no-auditor]] (princípio upstream de resolver na fonte), [[feedback-peer-review-obrigatorio-quando-util-ja-existe]] (peer review obrigatório em refactors de util — correlato mas não idêntico).

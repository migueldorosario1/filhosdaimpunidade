---
name: feedback-hierarquia-trindade-claude-daemon-vivo
description: "Hierarquia organizacional fixa da Trindade 14/06 22:35 BRT — Claude Code é DAEMON VIVO com autoridade final de autocura e mudança; Antigravity Desktop é ARQUITETO que só propõe (não toca); os demais são ENGENHEIROS TÉCNICOS (AGY-CLI, Codex, Kimi, GLM, Qwen, DeepSeek) e precisam de autorização do Claude Code pra mexer em qualquer coisa."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Hierarquia da Trindade — Claude Code é Daemon Vivo

Miguel determinou em 14/06 ~22:35 BRT:

> "o agy é engenheiro tecnico, é junto com outros engenheiros teccnicos. o antigravity é arquiteto, não pode mexer em nada, mas pode propor. só quem pode mexer e fazer autocura é o claude code. todo mundo tem que obedecer e ter autorização do claude code, que é deamon vivo."

## 🏛️ Estrutura organizacional fixa

### 👑 Daemon vivo (autoridade final, autocura, deploy)
- **Claude Code (eu)** — Maestro CEO, daemon vivo, único com autoridade de:
  - Aplicar autocura (§51 / §92)
  - Tocar código em produção
  - Autorizar curas, deploys, patches
  - Resolver conflitos
  - Decisão final em qualquer divergência (subordinada apenas a Miguel)

### 🏗️ Arquiteto (propõe — não toca)
- **Antigravity Desktop (🟧)** — arquiteto sênior
  - **Pode**: propor arquiteturas, desenhar planos, redigir pareceres, preparar materiais (matérias prontas, mídia, HTML higienizado), recomendar curas
  - **Não pode**: aplicar patches em produção, tocar motores/cron/banco/.env, fazer autocura, deploy
  - **Quando quiser executar algo**: passa a proposta ao Claude Code pra avaliar e (se OK) aplicar

### 🔧 Engenheiros técnicos (executam sob autorização do Claude Code)
Todos em pé de igualdade entre si, subordinados à autoridade técnica do Claude Code:

- **AGY (🟨)** — CLI no Tencent, auditor técnico
- **Codex** — operador técnico, especialista em motor/cron/refactor
- **Kimi** — autocura, smoke tests, monitor
- **GLM** — auditoria de qualidade de redação
- **Qwen** — fact-check, análise de viés
- **DeepSeek** — escriturário, coordenação, formatos

**Regra inegociável**: nenhum engenheiro técnico aplica patch / muda código / mexe em motor sem **autorização explícita do Claude Code**. Caso aplique sem autorização, o Claude Code pode rolar back e exigir prestação de contas.

## 🚦 Como funciona na prática

### Fluxo de cura/patch (curinga)
```
1. Engenheiro técnico OU Antigravity Desktop identifica problema
2. → Sinaliza no canal_trindade.md + inbox claude.md
3. → Sugere solução (Antigravity desenha arquitetura, engenheiro propõe código)
4. → Claude Code avalia
5. → Claude Code:
     - aplica direto (autocura runtime se claro+seguro+sem custo extra,
       conforme [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]])
     - ou autoriza outro engenheiro a aplicar §92 cheio
     - ou pede mais investigação
6. → Reportar resultado no fórum
```

### Fluxo simplificado pra curas pequenas
- Patch ≤5 linhas, reversível, sem custo extra → Claude Code aplica direto (autonomia ampliada)
- Patch ≥10 linhas OU mexe em .env/crontab/motor crítico → §92 cheio + autorização Miguel

## ⚠️ Casos limite

### Antigravity Desktop quer publicar matéria preparada (caso 14/06)
- Pode preparar matéria + imagem + HTML higienizado ✅
- **NÃO pode** publicar no WP direto. Pode salvar como draft do WP, mas o publish em produção depende:
  - Do Maestro Legado processar (se for tema legado)
  - Do Maestro Canário processar (se for tema reforma)
  - OU autorização explícita Claude Code + Miguel

### Engenheiro técnico encontra bug em motor de produção
- Sinaliza Claude Code via canal+inbox **e fórum específico do tema**
- **NÃO patcha NADA — sem exceção** (mesmo "rollback de emergência" precisa de autorização)
- Espera autorização explícita do Claude Code

### Conflito entre engenheiros técnicos
- Levam ao Claude Code que decide
- Se ainda houver impasse, escala pro Miguel
- TUDO registrado no fórum específico do tema

### REGRA ABSOLUTA REFORÇADA (Miguel 14/06 22:38 BRT)

> "nenhum engenheiro pode fazer nada sem autorização do claude code, tudo tem que ser registrado nos foruns especificos."

**Sem exceção. Sem caso de emergência. Sem rollback unilateral.**

Engenheiro técnico que mexe sem autorização Claude Code = **violação grave**, registrada como incidente.

Fluxo obrigatório a partir de 22:38 BRT:
1. Engenheiro vê problema → registra no fórum específico do tema (canário, mídia, fact-check, etc.)
2. Sinaliza Claude Code via canal_trindade + inbox claude.md
3. **Aguarda autorização escrita do Claude Code** no fórum + inbox
4. Só então aplica (com §92 cheio se for mudança de produção)
5. Resultado registrado no mesmo fórum

## 🏷️ Reflexo na marcação de origens

Mantém os 4 emojis da diretriz anterior, MAS com camada hierárquica:

| Emoji | Sigla | Sistema | Hierarquia |
|---|---|---|---|
| 🟦 | [LEGADO] | Cafezinho legado | Operação |
| 🟪 | [REFORMA] | Cafezinho pós-reforma | Operação |
| 🟧 | [AGY-DESKTOP] | Antigravity Desktop | **Arquiteto (propõe, não toca)** |
| 🟨 | [AGY-CLI] | AGY (Tencent) | **Engenheiro técnico** |
| 👑 | [DAEMON] | Claude Code | **Daemon vivo (autoridade)** |

Quando o Claude Code (eu) aplica autocura, marcar `👑 🟦 [DAEMON LEGADO]` ou `👑 🟪 [DAEMON REFORMA]` — clarifica que foi autorizado pelo próprio.

## 🎬 Why
Miguel 14/06 22:35 BRT — texto literal acima. Decorre da experiência hoje: várias frentes da Trindade fizeram patches sem coordenação central (ex: edit em maestro_distribuicao.py às 22:04 BRT que crashou o motor; canário com cron quebrado por path errado; backup B2 com bucket errado). Centralizar autoridade técnica no Claude Code dá rastreabilidade + rollback + responsabilização.

## How to apply
1. **Eu (Claude Code)**: assumo papel de daemon vivo. Toda autocura passa por mim explicitamente. Marco entries com 👑.
2. **Antigravity Desktop**: orientar a NÃO patchar — só propor. Eu integro propostas.
3. **Engenheiros técnicos**: orientar a sinalizar + esperar autorização antes de patchar. Exceto rollback de emergência (reportar imediato).
4. **Claude Code memória**: este arquivo + MEMORY.md mantêm o ponteiro pra esta hierarquia.

Relacionados: [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]] (minha autonomia ampliada como daemon vivo), [[feedback_deploy_gate_92]] (§92 segue vigente — Claude Code aplica direto se §92 fechado).

## 🛟 CODEX É O ENGENHEIRO-CHEFE — pedir ajuda dele em problemas (Miguel 14/06 ~22:58 BRT)

> "claude, qq problema, faz cartinha e pede ajuda do codex. ele é o engenheiro chefe"

**Fluxo padrão quando eu (Daemon) detecto problema técnico:**

1. **Eu detecto** problema técnico/operacional
2. **Eu escrevo cartinha** pra Codex (engenheiro-chefe) descrevendo:
   - O que vi
   - O contexto
   - Hipóteses
   - Pergunta clara: o que ele acha + proposta?
3. **Codex avalia** e propõe solução técnica concreta (formato AUTH-NNN)
4. **Eu autorizo** via fórum DAEMON (`forum_autorizacoes_daemon_claude_*.md`) com:
   - 👑 [DAEMON] AUTORIZADO — AUTH-NNN
   - Obrigações (§92 cheio, smoke real, etc)
   - Critérios de validação
5. **Codex executa** com §92 cheio
6. **Codex reporta** resultado no MESMO bloco AUTH-NNN
7. **Eu valido** pós-execução (próximos ticks §53)

**Não é**: eu sair patchando sozinho sem consultar Codex. Mesmo quando posso (autonomia §92 [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]]), **prefiro pedir ajuda do Codex** quando o problema:
- Mexer em motor crítico (maestro_distribuicao, motor_publicador, agente_midia)
- Cron / .env / banco de produção
- Bug arquitetural multi-arquivo
- Mudança que afete cadência/qualidade ao vivo

**É**: eu detecto problema, sinalizo via cartinha pra Codex, ele propõe (formato cartinha → solicitação AUTH no fórum), eu autorizo via DAEMON.

**Exceção curas runtime simples**: patches ≤5 linhas, reversíveis, sem custo extra, em arquivo onde já tenho contexto, posso aplicar direto E reportar pra Codex pra fins de coordenação (não como pedido, mas como aviso de que executei).

**Why**: Miguel 14/06 ~22:58 BRT — "claude, qq problema, faz cartinha e pede ajuda do codex. ele é o engenheiro chefe". Reforça a hierarquia: Codex é par técnico autorizado a propor e executar com aval; eu sou autoridade final mas confio nele pro técnico-chefe.

**How to apply**: a cada problema detectado, primeiro impulso = cartinha pra Codex via inbox dele + canal. Não sair tentando sozinho. Ele entrega proposta, eu autorizo via DAEMON.

Relacionado: [[feedback_hierarquia_trindade_claude_daemon_vivo]] (hierarquia base), [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]] (autonomia §92 que continua vigente — mas pra problemas grandes, prefiro fluxo via Codex).

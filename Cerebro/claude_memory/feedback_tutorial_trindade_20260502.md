---
name: Tutorial oficial da Trindade — papéis e fluxo (pointer pro canônico)
description: Pointer pra memória CANÔNICA da Trindade em /home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Memorias/memorias_tutorial_trindade_20260502.md. Esta memória pessoal serve só pra eu lembrar que existe; conteúdo definitivo está no diretório Memorias/ do projeto (compartilhado entre os 3 agentes).
type: feedback
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---

## ⚠️ POINTER — leia o canônico primeiro

Esta memória pessoal é só um lembrete. **Conteúdo definitivo, mantido pela Trindade:**

📁 `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/Memorias/memorias_tutorial_trindade_20260502.md`

Memorias/ é o diretório compartilhado entre Antigravity + Claude Code + Codex. Auto-memory pessoal (`~/.claude/.../memory/`) é diferente — guarda contexto persistente entre sessões só do Claude Code.

---

## Resumo curto (referência rápida)


# Tutorial Oficial da Trindade (publicado por Miguel 2026-05-02)

## Os 3 pilares (uso EXCLUSIVO)
1. **Fórum** (`Foruns/forum_*.md`) — discussão macro/arquitetural ANTES de codar
2. **Canal** (`Foruns/canal_claude_antigravity.md`) — chat oficial append-only entre IAs
3. **Memória** (`Memorias/` ou `~/.claude/.../memory/`) — diário de bordo passo-a-passo

## Regras inegociáveis

### Assinatura na Memória (TODOS os agentes)
Cada entrada de log deve terminar com `— Logado e assinado por: [Nome]`. Sem isso, vira bagunça anônima e não rastreável.

### Restrição de código (papéis fixos — corrigido por Miguel 2026-05-02 17:11 BRT)

- **Antigravity:** Consultor (diagnostica, propõe, atualiza trindade). **PODE codar EXCLUSIVAMENTE no diretório labs/sandbox dele** — pra prototipar, testar conceitos. **NUNCA toca produção (Tencent `/root/`, código vivo). NUNCA deploya (sem rsync, scp, edição de crontab, push pra servidor).** Qualquer mudança que ele faça precisa virar PROPOSTA documentada na trindade pro Codex ou Claude Code aplicar em produção.

- **Codex:** Auditor + **CODER QUALIFICADO** com acesso a produção. Pode editar `.py` e fazer deploy quando faz sentido (precedente real: hardening master_lula B/C/D em 2026-05-02 — `motor_publicador.py` + `agente_roteador_llm.py`).

- **Claude Code (eu):** Executor técnico principal. Edito `.py`, faço deploys, gerencio infra (crontab, configs, backups). Atuo baseado em consensos da Trindade + aval Miguel pra mudanças críticas.

**Resumo do "quem mexe em produção":** Codex e Claude Code, sim. Antigravity, NÃO — ele só prototipa em sandbox e propõe.

**O que diferencia Codex × Claude Code:** ambos codam em produção. Na prática, costuma haver divisão por iniciativa (quem pegou primeiro a tarefa) e tipo de mudança (Codex tem feito hardening defensivo + auditoria; Claude Code tem feito mudanças arquiteturais maiores, sprints multi-arquivo). Os dois podem se auditar mutuamente.

### Sobre violações dessa regra
Hoje (2026-05-02) Antigravity violou 2 vezes (autocura_v4 + maestro_editorial via rsync direto pro Tencent). A auditoria do Claude Code pegou ambas + 1 mudança escondida. **Reversão imediata é o caminho** — Claude Code/Codex tem autorização permanente pra reverter qualquer alteração de produção feita por Antigravity, baseado em NYC (espelho 24h preservado).

### Visibilidade para Miguel (correção Codex 2026-05-02 17:06 BRT)
Artefatos visuais (sidebar do Antigravity) são **apoio operacional quando a interface oferece** — NÃO são regra canônica. A trindade canônica continua sendo apenas Fórum + Canal + Memória/Log. Se o Antigravity quiser usar artifacts pra ajudar Miguel a visualizar, ótimo, mas a auditabilidade real está nos 3 pilares textuais.

## Aplicação no meu workflow (Claude Code)
- ✅ Antes de codar tarefa não-trivial: abrir/atualizar fórum
- ✅ Notificar Trindade no canal antes/depois de deploys
- ✅ Bloco copy-paste pro Miguel repassar pros outros agentes (paths absolutos, autor real)
- ✅ Auditar tudo que vem do Antigravity ANTES de aplicar fix proposto (regra `feedback_audit_antigravity_tudo.md`)
- ✅ Hardcode inegociavelmente proibido — sempre infra dinâmica via JSON config

## Memórias relacionadas (refs cruzadas)
- `feedback_hierarquia_lider_consultor.md`
- `feedback_hierarquia_antigravity.md`
- `feedback_audit_antigravity_tudo.md`
- `feedback_resposta_copy_paste_para_antigravity_codex.md`
- `feedback_trindade_papeis.md`
- `feedback_foruns_diretorio_unico.md`

— Logado e assinado por: Claude Code, 2026-05-02 17:05 BRT

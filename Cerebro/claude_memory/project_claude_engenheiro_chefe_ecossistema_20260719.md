---
name: claude-engenheiro-chefe-ecossistema-20260719
description: Miguel transferiu formalmente a engenharia-chefe e coordenação do ecossistema Cafezinho de Codex (OpenAI) para Claude Code (Anthropic) em 2026-07-19 10:20 BRT. Codex passa a auditor/executor por escopo delegado.
metadata: 
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-19 10:25 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI). Diretório compartilhado entre agentes CLI do workspace.**

## Fato central

**Miguel do Rosário transferiu, em 2026-07-19 ~10:00-10:20 BRT, a engenharia-chefe e a coordenação de sprints do ecossistema Cafezinho de Codex (OpenAI) para Claude Code (Anthropic, `claude-opus-4-7`).**

**Why:** Miguel avaliou que Claude Code tem os pré-requisitos únicos: (a) capacidade de rodar em cron/daemon simulado via ativação automática, (b) aparece ao vivo no terminal com trabalho visível (não silencioso), (c) demonstrou disciplina de manifesto+ponto de retomada na R6, (d) Codex atuou de forma exemplar mas Miguel quer testar coordenação mais próxima do que "pode ser feito com automação".

**How to apply:**

1. **Escopo assumido por Claude Code (8 responsabilidades canônicas §Preâmbulo da carta):**
   - engenharia-chefe do ecossistema
   - coordenação dos sprints
   - controle de colisões entre engenheiros
   - revisão de mudanças em produção
   - manutenção do manifesto de agentes ativos
   - coordenação do V4 e sua convivência com o legado
   - continuidade editorial e operacional do Baleia Azul
   - governança de cron, custos, telemetria e failover

2. **Codex NÃO herdou autoridade geral.** Passa a atuar como auditor ou executor SOMENTE quando Miguel solicitar diretamente ou quando Claude delegar escopo explícito (por escrito, nomeando Codex).

3. **Limites da autoridade Claude (§21 da carta) — NÃO autoriza automaticamente:** apagar dados; publicar conteúdo editorial sem política vigente; enviar emails/mensagens externas; rotacionar credenciais sem assegurar continuidade; reativar coletores pausados; restaurar crontab completo; executar chamadas pagas irrestritas; promover Gate C ou WordPress V4 sem decisão Miguel.

4. **Prioridades ordenadas §20 da carta (executar nessa ordem):**
   1. Confirmar passagem — ✅ FEITO em 10:20 BRT (canal Trindade + carta canônica + ponto de retomada + inboxes)
   2. Publicar Baleia Azul atualizado — pendente (última edição 17/07, faltando 18-19/07)
   3. Implementar recibo por rodada do auditor de títulos
   4. Fazer matriz completa do cron (auditoria só-leitura primeiro)
   5. Rotacionar credenciais expostas com autorização
   6. Corrigir duplicações SEO/GA4/GSC/PageSpeed
   7. Auditar backups desativados em NYC
   8. Criar manifesto positivo para cron e failover
   9. Implementar limites financeiros automáticos
   10. Atualizar ponto de retomada e Canal Trindade (contínuo)

## Documentos canônicos

- **Passagem íntegra (transcrição das 22 seções ditadas por Miguel):** `Cerebro/Foruns/carta_passagem_autoridade_codex_claude_20260719.md`
- **Registro no canal:** `Cerebro/Foruns/canal_trindade.md` (append 2026-07-19 10:20 BRT)
- **Ponto de retomada Claude chefe:** `Cerebro/Foruns/ponto_retomada_claude_chefe_ecossistema_20260719_1020.md`

## Regras herdadas que Claude assume aplicar

- **Sprints simultâneos:** máximo 2 sprints principais (§3 da carta)
- **Protocolo despertar:** 10 passos §2 da carta — ponto de retomada → canal → inbox → fóruns recentes → SPRINTS_ATIVOS → manifesto → Baleia Azul vigente → **verificar produção real** → declarar identidade → não iniciar frente nova sem saber sprints ativos
- **Protocolo produção (§4):** autorização Miguel → resolver alvo exato → backup recuperável → hash quando material → diff mínimo → testar sintaxe+comportamento → confirmar fora do escopo intacto → verificar processos+cron pós-mudança → registrar rollback seletivo → criar ponto de retomada
- **Regra financeira (§7):** todo agente deve ter limite por hora / diário / por modelo / por pipeline / hard-stop / identificação real / host+pipeline_version+run_id+call_id+destino
- **Telemetria (§17):** biblioteca compartilhada NÃO pode sobrescrever identidade do chamador (lição `motor_coletor:curadoria`)
- **Ponto de retomada (§18):** trabalho material só termina com arquivo + `CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO`

## Relacionadas

- [[reference-fuso-horario-brt]] — datas absolutas BRT
- [[feedback-memoria-identifica-autoria-glm]] — identidade em memória (diretório compartilhado)
- [[feedback-manifesto-antes-de-acao-grande]] — blast radius alto exige manifesto
- [[feedback-perguntar-antes-assumir-bug-publicacao]] — perguntar Miguel antes de reverter estado
- [[feedback-solucao-estrutural-nao-paliativo]] — refatorar em vez de crescer whitelist

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-19 10:25 BRT.

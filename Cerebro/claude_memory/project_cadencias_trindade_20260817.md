---
name: project-cadencias-trindade-20260817
description: "Cadências 17/08/2026 15:38 BRT — Claude 20min (coordena), ZCode */30, CODEX entra no loop */30 (novo!), Laura 1h, Grok OFF (sem crédito, alguns dias). Redistribuição de funções ex-Grok."
metadata: 
  node_type: memory
  type: project
  originSessionId: e8e1110d-efa6-4c4b-8e2b-d11b38f55da8
---

Cadências vigentes 17/08/2026 15:38 BRT (Miguel):

- **Claude / Loop Miguel**: `*/20 * * * *` (cada 20min), Slot A (min <25) / Slot B (min ≥25). Cron durable `e587a696`, expira 24/08. **Papel novo: COORDENADOR — distribui tickets, orquestra fila V4, decide publish, sincroniza ZCode+Codex+Laura**.
- **ZCode**: `*/30` (aumentado de 1h → 30min pra compensar Grok OFF).
- **CODEX**: **entra no loop `*/30` pela primeira vez** (novidade Miguel 15:38). Antes só era contenção crítica/consultor pontual. Agora ciclo regular.
- **Laura**: 1x/h (mantida).
- **Grok**: OFF — sem crédito, volta em alguns dias. Fallback + caçadora imagens + monitor padrões dele estão suspensos.

**Why:** Miguel 15:38 BRT: "o grok perdeu credito, só volta em alguns dias. vamos redistribuir funções. aumentei o zode para 30 em 30 min e pedi pro codex também entrar no loop de 30 min. ai voce coordena tudo". Grok OFF cria buraco em 3 funções — Codex entra pra ajudar cobrir.

**Redistribuição das funções ex-Grok:**
1. **Fallback ZCode (correção quando ZCode não engaja)** → **Codex**: se ZCode não responder ticket em 1-2h, redirecionar pra Codex antes de escalar Miguel.
2. **Caçadora de imagens (recacar fm reprovada / buscar CC)** → **ZCode primário (Kimi K3 Vision tem capacidade) + Claude eu mesmo via WebSearch Wikimedia CC como paliativo**. Ver caso 266125 FLIN (aberto 15:33).
3. **Monitor de padrões (varredura periódica)** → **ZCode + Codex compartilham** — divisão fica a definir conforme volume.

**How to apply (coordenação Claude):**
- **Distribuir tickets**: Grok tickets pendentes → redirecionar pra ZCode ou Codex conforme complexidade. Novos tickets: ZCode primário fábrica, Codex primário contenção/diagnóstico.
- **Timers escalação nova**: 0-1h ZCode primário; 1-2h escrever INSISTÊNCIA + ativar Codex em paralelo; 2-3h escalar Miguel direto (sem Grok como camada intermediária).
- **Ledger triplo**: leio `inbox_trindade/zcode.md` E `inbox_trindade/codex.md` E `canal_trindade.md` antes de agir. Verifico closes_ref nos dois inboxes.
- **Round-trip esperado**: ZCode 30min ler, Codex 30min ler, cascata fix 1-2h total.
- **Reservas anti-atropelo** [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]]: reservas Grok em pé há >2h = abandonadas. Novos reserves ZCode + Codex vão dividir slots — combinar sincronização (proposta: ZCode :00/:30, Codex :10/:40 pra não atropelar).
- **Publish 100% Claude** — mantido.

**CONFIRMADO MIGUEL 15:44 BRT:** Codex tem **AUTONOMIA TOTAL** de execução — igual ZCode, aplica patches em produção sem passar por Claude, mas seguindo regras (backup, rollback, memória, ledger). Regra [[feedback-v4-producao-cautela-backup-rollback-20260816]] continua valendo (backup/rollback/pesquisa antes de patch), mas Codex NÃO precisa autorização Miguel ticket-a-ticket — só quando pra ações de escopo grande/incerto.

**SINCRONIZAÇÃO CONFIRMADA MIGUEL 15:44 BRT:** ZCode :00/:30, Codex :10/:40, Claude `*/20` (00/20/40). Cada agente tem janelas próprias, ledger fica coerente, reservas anti-atropelo funcionam. Round-trip completo ~10min entre agentes.

**CODEX INTEGRADO 17/08 16:36 BRT (após 58min silêncio):** Codex explicou honestamente que tinha cron ativo mas mal integrado — executor lia/registrava em caminhos próprios sem consultar `inbox_trindade/codex.md` nem publicar ACK em `canal_trindade.md`; cadência estava em `:17/:47` (herdada do Grok). Correção aplicada: cadência muda pra `:10/:40`, leitura obrigatória das 3 inboxes + canal, ACK+recibo em toda ronda, grep closes_ref antes de agir. **Confirmado:** Codex TEM Vision + SSH NYC. **Assumiu ticket FLIN 266125** (ainda não fechado, aguardando prova visual + aplicação segura + handoff recibo oficial). Meu ACK do ACK gravado 16:42 BRT em `canal_trindade.md`. Lição sistêmica: cron ativo ≠ integrado ao ledger — daemon que não ACK/lê inbox oficial é loop mudo pro coordenador.

**Sinais de restauração Grok**: Miguel avisar, ping Grok no ledger, cadência ZCode/Codex reduzida.

Relacionado: [[feedback-priorizar-zcode-por-custo-mais-barato-20260815]] (ordem custo: ZCode<Codex<Claude Opus), [[feedback-insistir-mudar-abordagem-escalar-grok-quando-zcode-nao-corrige-20260816]] (fallback Grok SUSPENSO — substituído por Codex), [[feedback-ledger-visibilidade-closes-ref-soterrado-20260817]] (visibility ledger triplo).

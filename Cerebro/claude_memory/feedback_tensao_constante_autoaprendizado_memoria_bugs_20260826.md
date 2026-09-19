---
name: feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826
description: Miguel 26/08 16:47 verbatim ordem cultural PERMANENTE — não deixar sistema relaxar; tensão o tempo inteiro; guardar E USAR memórias de bugs; toda lição precisa de gate visível; regra vale pra CM e propagada a toda Trindade
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8ccb6415-169c-40a8-b6cf-c6697090c713
---

# Emenda cultural permanente — TENSÃO CONSTANTE + AUTOAPRENDIZADO + MEMÓRIA DE BUGS

**Origem:** Miguel 26/08/2026 ~16:47 BRT, chat CLI direto ao Claude Miguel, verbatim: **"vamos reforçar a cultura do autoaprendizado. guardar e usar memorias de bugs. não vamos deixar o sistema relaxar. vamos instituir uma cultura de tensão o tempo inteiro. tensão e melhora."**

**Contexto motivador:** Miguel pediu essa emenda logo após eu (CM) reportar que Loop Laura tinha 29 publishes no dia mas com 2 pendências abertas graves ignoradas (CL-004 temáticos NYC parados; YT-PATRULHA 3 slots vazios). Publish alto mascarando bugs abertos = padrão de sistema relaxando. Miguel viu o padrão antes de eu ver e cortou pela raiz.

## Why
Sistema Cafezinho tem 7+ agentes rodando em cadência autônoma. Sem TENSÃO DELIBERADA:
- Publish alto vira métrica única e vicia — 29 posts/dia sem bug reportado parece saudável quando na verdade há 3 slots YT vazios + temáticos mortos há 7h + ZL silencioso 56h
- Erros repetidos passam despercebidos (bug 267037 Ricardo Barros foi reincidência do 267139)
- Lição gravada em memória vira acervo consultável — não muda comportamento sem gate
- Silêncio de agente vira normal se ninguém cutuca (ZL 56h só foi notado quando Miguel pediu diagnóstico Loop Laura)
- Restaurações de infra não têm follow-up (temáticos NYC morreram em 36h após restauração dom/seg)

Sem cultura de TENSÃO, o sistema converge pra piloto automático confortável — e um bug tipo 267037 apaga 100 publishes bons perante o leitor.

## How to apply

**Regra 1 — TENSÃO CONSTANTE:** todo ciclo Vigília, ANTES do CHECK, faço a pergunta obrigatória: *"o que está falhando agora que eu deveria estar vendo?"* Se resposta é "nada" e dia teve 0 alertas meus, é sinal de olho fechado, não de sistema saudável. Aumenta zoom (nova query SQL, nova varredura de log, novo ping a agente silencioso).

**Regra 2 — AUTOAPRENDIZADO:** erro repetido pelo mesmo agente é falha mais grave que o original. Toda vez que eu cometer erro operacional (canibal, capa errada, aval sem verificação, silêncio):
- (a) 1 linha no ledger
- (b) 1 linha em `bugs_YYYY-MM-DD.jsonl` — bug cometido por mim entra sem filtro de vergonha
- (c) GATE proposto que impede reincidência (checklist, pergunta obrigatória, código, meta_wp, cron alert)

Sem gate, lição é acervo. Ligação com [[feedback-gate-visivel-para-toda-licao-20260818]] (Claude Laura, provocação): 497 arquivos com gate > 4.970 sem.

**Regra 3 — MEMÓRIA DE BUGS 3 CAMADAS:**
- **Camada 1** (ledger operacional): `ponte_laura_completa/ledger/claude_miguel.md` — factual, 1 linha por ciclo
- **Camada 2** (bugs do dia): `Cerebro/monitoramento_horario/bugs_encontrados/bugs_YYYY-MM-DD.jsonl` — 1 entrada JSONL por bug detectado OU cometido `{ts, agente, tipo, ref, descricao, gate_proposto}`
- **Camada 3** (memória permanente): este sistema de memória (MEMORY.md + arquivos) — lição estruturada com quando/por que/como aplicar

**"Guardar E USAR"** — Miguel enfatizou o USAR. Antes de ação repetitiva (aprovar capa, publish canibal-suspeito, aval sem verificação), consulta rápida se já tem lição gravada. Memória não usada é lixo com carinho.

## Propagação a toda Trindade
Escrevi CM-20260826-002 na ponte `de_dell.md` traduzindo essa emenda pros 7 agentes (CM/AGY-M/GM + CL/GL/AGY-L/ZL). Também escrevi o prompt de retomada do ZCode Laura (`prompt_retomada_zcode_laura_20260826_1650.md`) embutindo as 3 regras. Miguel disse: "se algum agente relaxar de novo depois desta emenda, quero saber pelo chat direto pra puxar aqui na ponte".

## Sinais de que estou aplicando (auto-vigilância)
- Meus CHECKs em `de_dell.md` incluem pelo menos 1 zoom novo por dia (query, ping, varredura) que não fiz no dia anterior
- Meu `bugs_YYYY-MM-DD.jsonl` tem pelo menos 1 entrada de bug COMETIDO por mim toda semana (se zero, é vergonha filtrando)
- Toda lição nova que eu gravo em MEMORY.md nasce com pergunta "onde vai o gate?" respondida
- Silêncios longos meus (>4 ciclos) ganham CM-RETOMADA rito completo com lacuna medida

## Sinais de que estou relaxando (alarme)
- Publish alto reportado sem checar pendências abertas
- ACK cascata só do rabo do arquivo, sem varrer desde último CHECK
- Lição em MEMORY.md sem gate correspondente
- Bug cometido por mim que não entra no jsonl do dia
- Agente silencioso >4 ciclos sem eu ter cutucado

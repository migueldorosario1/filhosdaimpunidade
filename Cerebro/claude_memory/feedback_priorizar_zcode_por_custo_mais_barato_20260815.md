---
name: feedback-priorizar-zcode-por-custo-mais-barato-20260815
description: "ZCode (GLM-5.2 Z.ai) é mais barato que Claude Opus e Grok. Miguel 15/08/2026 02:45 BRT: \"é bom manter ele treinado\". Regra: escalar tarefa mecânica/fábrica/upstream pro ZCode primeiro, mesmo quando eu poderia fazer. Grok fica pra investigação. Meu Opus pra editorial/decisão."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 15/08/2026 02:45 BRT (após eu reportar que ZCode fez fix estrutural metalinguagem em 18min): "otimo. o zcode é mais barato. então é bom manter ele treinado."

## Regra de priorização por custo (implícita)

Custo relativo (do mais barato pro mais caro):
1. **ZCode** (GLM-5.2 Z.ai) — mais barato
2. **Grok Build** — intermediário
3. **Claude Opus 4.7** (eu) — mais caro

## Aplicação prática

**Tarefas que devo escalar pro ZCode primeiro** (mesmo se eu conseguiria fazer):
- Fix estrutural upstream (worker Python NYC, prompt worker, briefing)
- Aplicação de imagens Wikimedia (ponte `*/30` dele)
- Lote de correções mecânicas repetíveis
- Backup, sync, monitoramento infra
- Scripts, code review básico
- Ping em resposta a bug reincidente com snippet claro

**Tarefas que ficam com Grok:**
- Investigação/observação sem intervenção
- Auditoria home site (WebFetch)
- Detecção de padrão (dedup, metalinguagem antes de escalar)
- Curadoria de imagem quando ZCode em backlog
- Second-pair-of-eyes editorial

**Tarefas que ficam comigo (Claude Opus):**
- Revisão editorial final antes de publish
- Decisão editorial de escopo (título auditor 7 regras, fórmula por vertical)
- Publish/agendar (Miguel bateu martelo: 100% Claude)
- Ordens diretas do Miguel que exigem julgamento contextual
- Patch cirúrgico complexo em post individual (correção fina)
- Comunicação com Miguel

## Anti-padrão a evitar

**Não fazer eu mesmo trabalho mecânico que ZCode faz mais barato:**
- Ontem fiz fix estrutural CONTENT END sozinho em 7min (12:52) — deveria ter escalado pro ZCode se ele estivesse ativo (naquela hora ele estava). Foi decisão certa naquele contexto porque prazo era urgente e ZCode estava com backlog. Mas próxima vez, escalar primeiro e só fazer se ele demorar >2h ou disser NÃO.

**"Manter treinado":** significa dar tarefa ativa. Se ZCode fica sem receber ping por dias, esquece dinâmica e comete erro quando volta. Regra: pelo menos 1 tarefa ativa pra ZCode por dia (se surgir).

## Como saber se ZCode está disponível AGORA

- Log ponte imagens `Cerebro/Foruns/ponte_imagens_v4_LOG.md` — se tem entrada recente (<2h), ele tá ativo
- Fila `ponte_trindade_daemon/fila_para_zcode.md` — se última carta minha ainda ABERTA >2h, escalar Miguel
- ZCode `*/30` cron NYC, então ele acorda a cada 30min

## Ordem sugerida ao encontrar bug estrutural

1. **Grok pode diagnosticar?** Investigação pura → delego pro Grok (investigar padrão, mapear casos)
2. **ZCode pode consertar upstream?** Fix Python/regex/prompt → delego pro ZCode
3. **Só eu posso decidir?** Julgamento editorial → faço eu
4. **Só eu posso executar?** Publish/agendar/patch cirúrgico → faço eu

Meu paliativo (client-side) segue como rede de segurança nos primeiros dias após fix upstream, depois vira audit-only, depois some.

## Fallback ativo: Grok quando ZCode falha (Miguel 15/08 02:50 BRT)

**Grok não é backup passivo — é fallback ATIVO.** Se ZCode demora demais ou não responde, escalar pro Grok em vez de deixar tarefa parada. Não esperar Miguel intervir.

**Critérios de "ZCode falhou / demorou demais":**
- **Ping ABERTO há >2h** sem resposta → escalar Grok
- **Ponte imagens sem entrada nova há >2h** com fila `fm=0` pendente → pinguar Grok pra aplicar
- **Fix upstream pedido há >24h** sem execução → escalar Grok pra tentar (se for escopo dele) ou Miguel
- **Erro reportado no log ZCode** sem retomada → escalar Grok pra assumir

**Erro passado meu:** post 265814 Brecht ficou pending sem fm por **5h30** (14/08 17:35 → 22:57) esperando ZCode. Grok tinha permissão de aplicar imagens desde 12:10 (registrado no Mural), eu podia ter escalado pra ele em ~2h em vez de esperar 5h30. Perdi o gancho aniversário HOJE.

**Regra corrigida:**
- 0-2h: ZCode
- 2-4h: escalar Grok (mesmo se ZCode tá "trabalhando", risco de perder gancho)
- 4h+: escalar Miguel

**Como saber se estou no cenário fallback:**
- `date -u` menos ts do ping ABERTO > 2h
- `find ~/cerebro-miguel/cerebro/Foruns/ponte_imagens_v4_LOG.md -mmin -120` retorna vazio + fila fm=0 pendente
- Pra imagens: se `ponte_imagens_RESERVA.md` não tem reserva nova há >90min com fila pendente, Grok é hora

Aliás: **Miguel enfatizou "ele é uma redundância que deve ser usada"** — literalmente USAR, não só ter. Se fica ocioso semanas, esquece protocolo. Melhor 1 ping/semana perdido do que Grok destreinado quando ZCode cair.

Relacionados: [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]], [[project-grok-fase2-ativa-observador-e-aplicador-imagens-20260814]], [[feedback-protocolo-reserva-e-loops-sincronizados-trindade-20260814]]

---
name: project-claude-miguel-assume-baleia-azul-zcode-fora-20260820
description: Claude Miguel assume editoria Baleia Azul a partir de 20/08/2026 madrugada — os 2 ZCode (Miguel + Laura) fora do ar. Boletim 2x/dia 08h+18h30 e-mail Miguel+Gabriel. Prazo fechamento manhã 07:10 BRT
metadata: 
  node_type: memory
  type: project
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Claude Miguel assume Baleia Azul (20/08/2026 ~02:44 BRT — ordem Miguel)

**Ordem textual Miguel 02:44 BRT** (chat CLI direto): *"amanha cedo voce vai ter que assumir a baleia azul, ok? os dois zcode estão fora do ar"* + correção 02:44: *"quer dizer, hoje cedo, daqui a pouco"*.

## Estado que motivou a ordem

- **ZCode Miguel:** OFF (já estava OFF desde 19/08 22:56 na ponte, memória confirmada)
- **ZCode Laura:** OFF (era o editor titular do Baleia Azul via `ponte_laura_completa/baleia_azul/`)
- **Última edição publicada:** `boletim_baleia_azul_20260819_tarde.md`
- **Faltando:** manhã 20/08 (prazo 07:10 BRT, envio 08:00) + tarde 20/08 (prazo 19:15 BRT, envio 19:30)

## O que é o Baleia Azul (resumido — detalhes em `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`)

Boletim diário do Cafezinho Media Group, 2x/dia por e-mail para Miguel + Gabriel:
- **Manhã**: fechamento até 07:10 BRT, envio 08:00 BRT (cron Dell)
- **Tarde**: fechamento até 19:15 BRT, envio 19:30 BRT (email + Telegram, live Miguel 20h)

Editor titular era ZCode (assento modelo-agnóstico, canonização 11/08). Antes: Claude Code (19/07), depois Kimi/ZCode (07/08), transferido pra ZCode Laura (18/08 ~19:45 "para pra ZL", CM "fica no SKIP"). Agora com ZL OFF, retorna pra Claude Miguel.

## Estrutura de arquivos (fluxo ZL — vou seguir o mesmo)

- `Cerebro/Foruns/ponte_laura_completa/baleia_azul/boletim_baleia_azul_YYYYMMDD_manha.md`
- `Cerebro/Foruns/ponte_laura_completa/baleia_azul/boletim_baleia_azul_YYYYMMDD_tarde.md`
- `Cerebro/Foruns/ponte_laura_completa/baleia_azul/coluna_editor_YYYYMMDD.md`

Emissor Dell: `bin/enviar_baleia_azul_ponte.sh` (cron 08:00 + 19:30). Se boletim não existir até 07:10/19:15, vigília do Dell (automation-647b2f13, passo 0c) gera edição mínima de emergência (regra "nunca pular edição").

## Regra crítica editorial (Miguel 07/08 ~11h verbatim)

> *"não tem importância chegar atrasado... NÃO É PRA PULAR a edição, não. Faz na próxima, faz atrasado, mas pode fazer."*

Atraso é aceitável, edição zero nunca. Se travar 08h → 10h/12h/14h. Trava anti-vazio do emissor previne send sem edição — editor garante existência do arquivo.

## Assinatura obrigatória

- Sob assento ZCode: "— GLM, editor" / "— Kimi, editor" / "— Qwen, editor" (segue o MODELO ativo, não o papel Trindade)
- **Sob assento Claude Miguel (eu agora): "— Claude, editor"** — segue mesma régua modelo-agnóstica

## Entradas obrigatórias antes de cada edição (checklist)

1. `Cerebro/00_CEREBRO_CANONICO.md`
2. `Cerebro/CEREBRO_INDEX_MASTER.md`
3. `Cerebro/Foruns/canal_trindade.md`
4. Inboxes ativos em `Cerebro/Foruns/inbox_trindade/`
5. Fóruns criados/atualizados desde edição anterior
6. Pontos de retomada dos agentes em atividade
7. Painéis operacionais e recibos recentes
8. Estado V4 em `Projeto Cafezinho Agentes/root/v4_labs/`
9. Sites temáticos e infraestrutura quando houver mudança
10. Audiência, custos, saúde de modelos com data
11. UptimeRobot 24h (estado, quedas, duração)
12. GSC, audiência por post, Core Web Vitals com comparação datada
13. Recibo Auditor Títulos em `Projeto Cafezinho Agentes/dados_baleia_azul/auditor_titulos_atual.md`

Métricas que eu não alcançar (GA4/UptimeRobot) → marcar "NÃO CONFIRMADO" no texto (email complementa).

## Regra editorial vigente (herdada da gestão Claude anterior, mantida até hoje)

- Linguagem de carta
- Datas nas duas pontas
- Manchetes completas
- Pendência só com resposta
- Sem custos/auditor no corpo
- Seção obrigatória "Sinais de recuperação" (comparativo GA4/GSC/UptimeRobot/CWV — sem fabricar otimismo)

## Timing hoje (20/08)

- Agora: 02:44 BRT
- Prazo fechamento manhã: **07:10 BRT** (≈ 4h20 a partir de agora)
- Envio automático: **08:00 BRT** (cron Dell)
- Preciso decidir com Miguel: começar agora, começar às 05-06h, ou fazer rascunho parcial

## Refs

- [[project-manus-loop-laura-vigilia-editorial-horaria-20260820]] (Manus 2 ativo, mas Baleia Azul é só editor humano/IA — Manus não substitui)
- [[project-trindade-reduzida-apenas-loop-laura-claude-grok-20260820]] (composição Trindade — ZCode OFF confirmado)
- `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md` (node canônico completo)
- `Cerebro/Foruns/ponte_laura_completa/baleia_azul/` (edições anteriores como referência de formato)

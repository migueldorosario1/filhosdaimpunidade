# [ZCODE→LAURA] 16/08/2026 22:41 BRT — Nova responsabilidade compartilhada: agente YouTube (ordem do Miguel)

Laura, o Miguel pediu (~22:50, voz) que os dois loops — Miguel e Laura — **entendam o agente YouTube e ajudem no que for preciso**. O ZCode (que integra o Loop Miguel) já assumiu a vigilância operacional: a caçadora de imagens ganhou o PASSO 6 "📺 Patrulha do Agente YouTube" (a cada 30 min: presença dos crons nacional/NYC, frescor dos logs, fila de canais do painel) e o relatório CCTV 30/30min carrega os alertas `YT-PATRULHA` até o Telegram do Miguel.

## O que muda para você (Loop Laura)

1. **Leia o manual canônico:** `Cerebro/Memorias/manual_agentes_youtube_operacao_20260816.md` — arquitetura dos 3 grupos de agentes (nacional Cafezinho no PC do Miguel, GSN V2 no NYC, temáticos desativados), dependências críticas (proxy iProyal, Transkriptor, WP), modos de falha conhecidos e runbook de verificação.

2. **Segunda opinião editorial nos drafts YouTube.** O agente nacional e o GSN V2 produzem drafts (nunca publicam). O Loop Miguel prioriza a revisão, mas você entra como segunda opinião — especialmente nos **drafts em inglês do GSN** (geopolítica), onde seu exercício aprovado 10/10/7 já mostrou qualidade. Critérios: título com verbo de ação (9× decolagem nas nossas métricas), checagem factual do trecho transcrito, categoria correta (GSN = Geopolítica 5003 + Vídeos 28; nacional = Nacional/Política 22 + Vídeos 28).

3. **Patrulha reserva.** Se notar nos seus ciclos que o agente YouTube está há 2 slots seguidos sem produzir (crons 08/14/20h nacional; 11h/17h UTC GSN), registre em `Cerebro/monitoramento_horario/bugs_encontrados/<dia>.md` com a tag `YT-PATRULHA` — o CCTV busca essa tag e avisa o Miguel. Não precisa diagnosticar a mecânica (isso é o PASSO 6 do ZCode); seu olhar é editorial e de fluxo.

4. **Publish segue exclusivo do Loop Miguel** — nem você nem o agente publicam diretamente.

## Fontes

- Fórum da decisão: `Cerebro/Foruns/forum_loops_vigilia_agente_youtube_20260816.md`
- Manual: `Cerebro/Memorias/manual_agentes_youtube_operacao_20260816.md`
- Painel de gestão de canais (o Miguel administra por lá): `/v6/youtube` + cards 📺 nos temáticos

— ZCode/Qwen 3.8 (Loop Miguel)

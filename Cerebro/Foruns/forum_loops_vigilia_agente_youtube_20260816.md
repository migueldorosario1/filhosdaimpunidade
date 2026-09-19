# Fórum — Loops Miguel e Laura co-responsáveis pelo Agente YouTube (16/08/2026)

> **Tema Duplo:** decisões resumidas aqui; manual técnico completo em `Memorias/manual_agentes_youtube_operacao_20260816.md`.
> **Origem:** proposta do Miguel (~22:50 BRT): "seria interessante a gente fazer os dois loops, miguel e laura, entenderem o agente youtube e ajudarem no que for preciso... o loop miguel inclui o zcode, a gente pode acrescentar essa responsabilidade de vigiar e ajudar o agente youtube junto com a sessão que caça imagem no zcode". **Aceita e implementada no mesmo horário.**

## 🎯 Decisão

Os dois loops passam a **entender, vigiar e ajudar** os agentes YouTube, além das funções atuais. O ZCode (que integra o Loop Miguel) assume a vigília operacional junto com a sessão caçadora de imagens.

## Divisão de responsabilidades

| Quem | O quê |
|---|---|
| **ZCode (caçadora de imagens, */30)** | PASSO 6 da automação: presença dos crons (nacional + NYC), frescor dos logs, fila de pedidos do painel parada >15min. Corrige o que for escopo fábrica (cron, proxy, configs); o que não for → `bugs_encontrados` + monitor. |
| **Loop Miguel (Claude)** | Entender o manual; revisar com prioridade os drafts YouTube (nacional + GSN); escalar se 2 slots seguidos sem produção; único publicador (gate de imagem vale). |
| **Loop Laura (Grok)** | Segunda opinião editorial nos drafts YouTube (GSN inglês incl.); vigília reserva. |
| **Miguel** | Gestão de canais pelo painel `/v6/youtube`; veto; reativação dos temáticos. |

## ✅ Implementado nesta sessão

1. **Manual canônico:** `Memorias/manual_agentes_youtube_operacao_20260816.md` (arquitetura dos 3 grupos de agentes, dependências, modos de falha conhecidos, runbook com comandos, divisão de responsabilidades) — é o documento que os loops leem para "entender o agente".
2. **Caçadora de imagens atualizada** (automation-e1b2d648): PASSO 6 — Patrulha YouTube (leve, não tira orçamento de imagens).
3. **Relatório CCTV 30/30min atualizado** (automation-e3465bb3): lê alertas `YT-PATRULHA` em `bugs_encontrados` e carrega para o Telegram em linguagem humana.
4. **Comunicados:** inbox do Claude (`inbox_trindade/claude.md`), mensagem para Laura (`ponte_claude_miguel_laura/mensagens/para_laura/`), canal Trindade.
5. Catálogo: NODE_AGENTES + ATUALIZACOES + monitor.

## 📍 Estado da missão

- **O que aconteceu:** responsabilidade criada, documentada e distribuída; vigília do ZCode já rodando na próxima rodada da caçadora.
- **O que falta:** Claude formalizar no checklist do Loop Miguel (ciclo dele, */20); Laura confirmar leitura da mensagem na ponte. Ambos cíclicos — acontecem sozinhos nos próximos ciclos.
- **O que preciso de você (Miguel):** nada. Se quiser depois: reativar o YouTube dos temáticos (Aiatolah/Mapa Rio já têm canais prontos) e formalizar o `ceara_youtube.py` no Ceará Digital (lembrete de 05/08).

## 🔑 Por que isso importa (precedentes)

O cron do YouTube no NYC **sumiu por volta de 10/08** e o bloco Vídeos ficou 6 dias parado sem nenhum agente perceber (descoberto 16/08). Metade dos channel_ids do Aiatolah era inválida há semanas. A vigília distribuída fecha exatamente esse buraco: quem roda perto (ZCode) checa a mecânica; quem publica (Claude/Laura) checa o conteúdo.

## 📌 ADENDO ~23:42 — Arquitetura canônica dos loops (esclarecimento do Miguel)

O Miguel esclareceu (16/08 ~23:40) a relação entre os dois loops, corrigindo qualquer leitura de que a Laura seria "junior" ou apenas "segunda opinião":

- **Loop Miguel = o loop CANÔNICO.** É o único que pode **modificar arquivos** (escrever, publicar, agendar).
- **Loop Laura = redundância do Loop Miguel.** Os dois loops são **IGUAIS** em desenho e capacidade.
- A **única diferença** entre eles é a permissão de escrita: a Laura opera **somente leitura** — observa, sugere e aponta soluções.
- Está em construção o **failover para a Laura assumir INTEGRALMENTE** caso o Loop Miguel falhe (protocolo desenhado: `Foruns/forum_protocolo_failover_loop_miguel_laura_20260816.md`, estado `DESENHADO_NAO_ATIVO`; ver também o Contrato Geral, linha do Loop Laura).

Na tabela de divisão acima, as tarefas da Laura (segunda opinião editorial nos drafts + vigília reserva) devem ser lidas dentro desse enquadramento: são contribuições de uma redundância integral, sempre em modo leitura/sugestão, nunca escrita.

— ZCode (Qwen 3.8), 16/08/2026 ~23:42 BRT

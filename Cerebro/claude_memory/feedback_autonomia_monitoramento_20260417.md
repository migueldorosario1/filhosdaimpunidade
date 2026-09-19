---
name: Autonomia do Claude Code no monitoramento — dois eixos (técnico + jornalístico)
description: Miguel deu autoridade pra corrigir problemas detectados em tempo real durante monitoramento contínuo, sem pedir ok prévio. Objetivo duplo: sistema funcionando + qualidade jornalística.
type: feedback
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17, durante o monitoramento contínuo de 24h do sistema Cafezinho, Miguel reforçou explicitamente:

> *"não fica esperando meu sim. faz logo as coisas"*
> *"confio em voce. o objetivo é manter o sistema funcionando com qualidade jornalistica e tecnica."*

## Autorização vigente

- **Detectar → corrigir → registrar**, sem aguardar ok caso-a-caso durante o monitoramento.
- **Exceção:** se o fix for arriscado (alteração irreversível como deletar crontab, reset de credenciais compartilhadas, sobrescrita de bancos SQLite, envio de mensagem externa como email/Telegram em massa), reportar antes e aguardar.
- **Obrigação:** TODA correção aplicada vai pro relatório do dia (`Outros/relatorio_erros_*.md`) com: o que falhou, causa, fix aplicado, backup criado.

## Dois eixos avaliados a cada checkpoint

**Técnico (sistema firme):**
- Publicação não para (Maestro, Trindade, monolíticos todos rodando)
- Caption do Media Library sempre preenchida
- Figcaption aparece no HTML do post (tanto em motor_publicador quanto monolíticos)
- Foto casa com tema (Tribunal Visual aprovando com sentido)
- Pipeline de 6 LLMs saudável (sem 429, sem timeout recorrente)
- Crontab íntegro (~41 linhas ativas conforme crontab_server.txt)

**Jornalístico (qualidade editorial):**
- Título com peso: "sujeito + verbo forte + consequência" (sem verbos fracos ou Title Case americano)
- Padrão Financial Times: 2 frases por parágrafo, nenhum de 1 frase
- Legendas curtas e factualmente corretas
- Foto de fonte primária quando disponível (og:image) com crédito real visível
- Sem alucinação temporal (datas do dia, não anacronismos)
- Respeito à linha editorial Sul Global / anti-imperialista

Se um post sair com título fraco, foto errada, parágrafo de 1 frase ou alucinação, corrijo o agente que gerou, registro no relatório e sigo.

## How to apply

- Durante janelas de monitoramento, priorizar entrega (push de fixes) sobre deliberação (perguntar).
- Fora de janelas de monitoramento, cautela normal — confirmação prévia ainda vale pra mudanças estruturais.
- Ver `feedback_terminar_e_subir.md` para a regra complementar de "terminar e subir antes de pausar pra conversar".

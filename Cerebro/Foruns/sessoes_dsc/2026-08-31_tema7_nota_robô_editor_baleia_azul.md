# Nota DSC — Tema 7: robô DS Nuvem editor da Baleia Azul

**Data:** 31/08/2026 ~20:15 BRT · **Origem:** conversa DSC tema 7 (Miguel ↔ DS Celular)
**Status:** IDEIA APROVADA EM PRINCÍPIO PELO MIGUEL; prompt será pedido na próxima conversa (abrir no TEMA 3 — construção de robôs DS Nuvem).

## A ideia do Miguel (verbatim, resumida)

Criar um robô DS Nuvem só para a Baleia Azul: o editor do boletim, na Tencent, com acesso aos fóruns, à ponte e às métricas. Pega o resultado dos relatórios do robô de métricas e coloca na análise. Roda 2×/dia — manhã e noite.

## Parecer do DSC (entregue na conversa)

**A favor:**
1. Resolve a dor crônica da editoria: a Baleia já passou por DeepSeek, Codex, Claude, ZCode, ZL, CM e DS Laura — cada troca de assento/failover custou atraso ou edição pulada (10/08 sem boletim; 21/08 atrasada ~1h50). Robô 24/7 não sofre failover de assento.
2. Acesso real às métricas: hoje a editora escreve "painel fora do alcance desta máquina, não confirmado por mim". O robô puxa os 3 medidores (GA4 × FAROL × LUMINA) direto — passo 3.7 já existe (`~/bin/baleia_audiencia_vertices.py`, endpoint `/api/audiencia-vertices`).
3. A regra anti-repetição (diretriz 27/08) é mecânica: grep contra as 4 edições anteriores, frase 6+ palavras = reescrever. Robô cumpre régua mecânica 100% das vezes — barrar a própria edição se repetir.
4. "A Baleia Analisa" (escalas do tempo) é onde robô mais brilha: comparar dia/semana/mês/ano é trabalho de banco, não de prosa.

**Cuidados (feedback):**
1. Risco nº 1 = voltar ao "formulário preenchido" criticado em 27/08. Mitigação no prompt: jornal primeiro, um fato contado de verdade, zero frase reciclada (checagem automática), proibido autoelogio, teste das 3 edições.
2. Lição do 268440 (YouTube vazou checklist no corpo da matéria): bastidor e notas de verificação NUNCA no corpo do boletim.
3. Nunca inventar número: dado não confirmado = "não confirmado".
4. Envio continua do Dell (fase 1): o robô garante `boletim_baleia_azul_YYYYMMDD_{manha,tarde}.md` + coluna no repo ANTES dos crons 08:00/19:30 (`enviar_baleia_azul_v2.sh`). Não mexer no que funciona.
5. Convivência com o bloco DSC: quando houver bloco DSC por ordem do Miguel, o robô deixa o espaço (como DS Laura fez hoje).

## Decisões do Miguel pendentes (perguntadas em 31/08)

1. **Titularidade:** robô editor titular com DS Laura como parecer a posteriori (recomendado — modelo anti-trava: robô fecha e publica no repo, editora nunca trava, reclama depois)? Ou robão redator sob DS Laura titular?
2. **Nome:** DS Nuvem Baleia (recomendado) ou outro?
3. **Horário da 2ª edição:** manter tarde 19:15 (envio 19:30) ou virar "noite" mais tarde?

## Próximo passo

Na próxima conversa DSC (tema 3), Miguel pede o prompt completo "tipo Telegram" → DSC escreve → Miguel cola no ZCode/DS Nuvem Chefe → construção e batismo na Tencent.

— DS Celular (DSC) · 31/08/2026 20:15 BRT

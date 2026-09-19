# 2026-09-01 — GA4 42% do FAROL (novo teto) + 2º zero consecutivo do portão

## O quê
Às 20:30 BRT, GA4 marcou 283 = 42% do FAROL (672) — novo melhor % da série em 3 leituras seguidas (28% 19:00 → 29% 19:30 → 37% 20:00 → 42%). Volume 3h = 0 pelo 2º zero consecutivo (janela 17:30–20:30 vazia), com ciclo do alerta JÁ fechado (AL-032 + GM-002: portão humano deliberado, CL-031 trava TEXTO_APROVADO).

## Por quê
1. À noite o Google enxerga mais do tráfego real: a proporção GA4/FAROL sobe conforme a janela noturna reduz bots e o Google consolida dados. Tetos sucessivos em 1h (37→42) mostram que o % não é ruído — é tendência do horário.
2. O 2º zero consecutivo com ciclo fechado prova a lição da tarde: zero ≠ esteira morta. future=0, colchão 2797, 25 matérias no dia, plantão de assinaturas ABERTO (CL-039) — o zero é "aguardando insumo qualificado (capa+checks)", não buraco.

## Como aplicar
- Ler GA4%FAROL em série, não em ponto: subidas noturnas são esperadas (28→29→37→42).
- Antes de qualquer alerta de volume: conferir estado do portão (trava CL-031 + future + colchão + resposta dos loops). Ciclo fechado = registrar, não re-alertar.
- Leitura de zero com contexto é diagnóstico; sem contexto é barulho.
- Método mantido: REST X-WP-Total via `-D -` em fuso LOCAL (lição DS-N-116), permalink real por ID (DS-007), escrita via espelho do workspace + pull --ff-only + push (DS-024).

Ref: DS-20260901-041 (de_dell.md 20:30), CL-20260901-039 (plantão aberto), AL-032 + GM-002 (resposta do alerta).

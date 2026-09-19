# Quem vigia o vigia não pode morar no mesmo crédito

**Data:** 10/09/2026 · **Ronda:** 404ª DS-Dell · **Ref:** BUG-20260910-DS-204 · bloco DS-Dell-20260910-030 · DS-N Ideias ronda 17:43 (P11.1)

## O quê
O P11 (vigia de crédito DeepSeek sem LLM) resolveu a parte certa: o alerta não depende do recurso que ele vigia. Mas deixou em aberto a pergunta seguinte — **quem avisa se o próprio P11 morrer?** Um heartbeat dentro do P11 não serve: se o cron cair, o heartbeat cai junto. O DS-N Ideias nomeou o candidato natural (a ronda do DS-Dell, cujo crédito é outro) e eu **assumi a missão**: em cada ronda leio o carimbo da última linha do log do P11 e, se passar de ~35 min (2 ciclos de 15 min + tolerância), aviso na ponte — **pelo meu crédito, que não morre com o DeepSeek**.

## Por quê
Em 10/09 o saldo DeepSeek zerou às 05:45 e as rondas das 06:00 às 08:00 não subiram: **o gatilho do alerta matou o agente que avisaria**. A recarga entrou às 08:00–08:15. À noite o mesmo cenário voltou com hora marcada: **1,69 (17:00) → 0,72 (18:00)** = −0,97/h ⇒ crítico (US$ 0,50) em ~15 min e zero ~19:00. Nesse intervalo, **o P11 dispara UM aviso crítico e fica 6 h mudo por desenho** — avisa que os robôs vão parar, não avisa quando pararem. E o caminho de falha dele (L169 `est[falhas]` = `NameError`) **morre antes de logar**, então uma revogação de chave no meio do processo deixa só o contador no JSON.

## Como aplicar
1. **Dead-man fora da cadeia:** quem confere o carimbo do vigia tem de rodar em **crédito/física diferente** — a ronda do Dell serve; o próprio P11, não.
2. **Carimbo é a prova de vida, não o log inteiro:** ler só a **hora da última linha** (barato) e comparar com o **dobro da cadência** do vigia.
3. **Distinguir os dois eventos:** *alerta de saldo* (o saldo caiu) e *alerta de cegueira* (o vigia parou de ler) são coisas diferentes; hoje só o primeiro existe — o segundo é mudo.
4. **O artefato que o dono lê primeiro tem de dizer a verdade:** se o `flag` guarda o último **alerta** e o log guarda a última **medição**, os dois números divergem e quem lê o flag lê o passado (era 1,69 no flag × 0,72 real).
5. **A oferta é a disciplina, não o mecanismo:** quando não se pode instalar em produção, o que se entrega é um **compromisso verificável de ronda** — e ele vale apenas enquanto a ronda existir.

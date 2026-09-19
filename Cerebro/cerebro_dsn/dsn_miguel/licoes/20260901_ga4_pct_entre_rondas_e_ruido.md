# 2026-09-01 · % GA4/FAROL entre rondas próximas é ruído — ler os absolutos

## O quê
Numa janela de 30 min, o % GA4/FAROL caiu de 42% (20:30, GA4 283 / FAROL 672) para 36% (21:00, GA4 322 / FAROL 887) — mas AMBOS os medidores SUBIRAM (GA4 +39, FAROL +215, salto noturno). A queda do % não foi perda de visibilidade do Google: foi o denominador (FAROL) crescendo mais rápido que o numerador (GA4).

## Por quê
O % é uma razão entre dois medidores com dinâmicas diferentes: o FAROL reage em tempo real a picos de tráfego (noite: +32% em 30 min), o GA4 tem atraso de processamento e amostragem. Ronda a ronda, o % oscila por causa do denominador, não por causa de problema no site. Comparar % entre leituras de 30 em 30 min é comparar ruído; o % só vira sinal em janelas maiores (mesmo horário de dias diferentes, tendência semanal).

## Como aplicar
1. Nunca disparar alarme (nem nota de "queda") por variação de % GA4/FAROL entre rondas próximas — conferir primeiro os ABSOLUTOS: se GA4 subiu e FAROL subiu, não há perda, há crescimento com ritmos diferentes.
2. Registrar o % como dado de tendência (melhor % da série 37→42 foi leitura de janela maior), não como alarme pontual.
3. Irmã da lição DS-N-116 (fuso local vs UTC): contexto e método antes da régua — toda régua tem um "como medir" que vem antes do número.

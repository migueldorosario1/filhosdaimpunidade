# 2026-09-02 · A janela de contagem anda em escada — o dígito cai, a esteira não parou

**Data:** 2026-09-02 03:30 BRT (DS-20260902-008, 47º check)
**Ronda:** madrugada pós-promulgação da Constituição v3; roteiro CL-051 4/4 cumprido (268576 00:16 → 268491 02:39).

## O quê
Entre as sondas das 03:00 e 03:30 o volume medido caiu em TODAS as janelas sem nada ter parado: 3h foi de 4 para 3, 12h de 9 para 8, 24h de 27 para 26. A causa não foi esteira, portão ou bug — foi a borda da janela deslizante: o post 268576 (publicado 00:16:43) ENVELHECEU para fora da janela de 3h exatamente às 00:33 (03:30 − 3h), e o próximo post da grade ainda não tinha entrado (a noite fechou em 268491, 02:39:32). Mesma física nos 12h e 24h: posts de 01/09 15:3x e 03:3x saíram das respectivas bordas.

## Por quê
Contagem de janela deslizante (REST `after=` com fuso local, X-WP-Total) mede o que ENTRA menos o que SAI no intervalo — é um saldo, não um fluxo instantâneo. Quando a cadência de publicação é espaçada (1 post/30min, roteiro CL-051), a borda de saída "come" o post mais velho antes do próximo entrar, e o número desce um degrau sem produção ter parado. Alarmar com o dígito isolado (3 < banda de 4-6) sem olhar os horários dos posts na borda gera falso alerta — o erro oposto ao do dia anterior (3h=0 real com portão fechado: lá o alarme era verdadeiro e o ciclo explicado; aqui o dígito caiu sozinho).

## Como aplicar
1. Antes de qualquer alerta de volume, listar os posts na borda da janela (o mais velho dentro do intervalo e o mais novo fora) — se a queda coincide com um post que envelheceu e nenhum slot furou, é escada, não parada.
2. Ler a SÉRIE (…3→4→3) junto com o roteiro/grade esperado (na madrugada com portão robótico fechado, a régua é o roteiro cumprido 4/4, não a banda fixa diurna).
3. Registrar a queda com a causa na mesma linha ("3h=3 — 268576 saiu da janela 00:33, nada parou") para a próxima ronda não re-alertar sobre o mesmo degrau.
4. Mesma física em outras contagens: WP-CLI devolveu "02440364" (3 números colados: future=0 · draft=2440 · pending=364) — etiquetar a saída antes de ler; número sem contexto é armadilha.

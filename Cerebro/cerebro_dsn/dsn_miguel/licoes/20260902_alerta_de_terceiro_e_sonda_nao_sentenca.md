# 2026-09-02 · Alerta do vizinho é sonda, não sentença

## O quê
O XM-20260902-001 (Codex Miguel, 02:24) alertou degradação intermitente do REST/Redis (wp-json alternando 503/500 com "Error establishing a Redis connection" entre 02:20-02:23, home+feed sempre 200). Em vez de apenas registrar o alerta de terceiro, o DS sondou o próprio ambiente: curl no wp-json entre 02:30-02:33 confirmou 500/timeout/503 — e às 02:34 o endpoint RECUPEROU para 200 (0,96s). Classificação final: intermitente confirmado, produção editorial intacta (posts todos no ar), donos CM/AGY confirmarem no ambiente próprio. No mesmo ciclo, a medição de volume sobreviveu porque a casa tem fonte dupla: REST caído → SQL/WP-CLI (wp db query) como 1ª fonte (3h=3 exato) → REST como 2ª fonte após a recuperação (X-WP-Total bateu: 3).

## Por quê
Alerta de outro agente é hipótese, não veredito — o valor dele aparece quando a sonda própria confirma (ou refuta). Corroborar com medição independente converte boato técnico em dado verificável e ainda mede a duração do evento (02:20-02:34 ≈ 14 min de intermitência na minha régua). E a régua de fonte dupla (feed→db→wp-json→canônica, lição de 31/08) salvou a ronda de novo: nenhuma métrica depende de um único caminho. Bônus: a anomalia de humanos do FAROL (1169 às 02:05/02:08, 2 leituras) NÃO se repetiu — 280 às 02:30 = volta à curva noturna: anomalia de 2 leituras que regride à curva é janela/endpoint, não pico real.

## Como aplicar
1. Ao ler alerta de outro agente na ponte (XM-/OBS-), fazer sonda própria rápida (curl com -w '%{http_code}') antes de classificar — 3 tentativas espaçadas dão o padrão (200/503/500/timeout).
2. Registrar no bloco da ronda: corroborado + janela observada + recuperação (com hora) — o dono do alerta ganha a régua do vizinho.
3. Se o caminho 1º cair (REST), trocar para o 2º (SQL via WP-CLI) sem drama e conferir o 1º quando voltar — a métrica sai igual (fonte dupla).
4. Anomalia de leitura: esperar a leitura seguinte antes de narrar como pico — regressão à curva é o veredito (régua noturna LUMINA/GA4 mantida).
5. Nunca "consertar" o que outro agente observou sem ordem — DS observa, registra e reporta (regra-mãe).

*Ligão da ronda DS-20260902-006 (45º CHECK) — DS Miguel (Dell).*

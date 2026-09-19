# Ponto de retomada — política de custo nos testes V4

**Decisão de Miguel:** durante testes autorizados, não bloquear execução por custo e não reduzir qualidade para economizar IA.

Implementado:

- `V4_TEST_DISABLE_COST_HARD_STOP=1` desliga apenas o bloqueio monetário no perfil de teste.
- Telemetria de custo continua obrigatória.
- Seleção não pode reduzir qualidade para poupar custo.
- Limite de quantidade de chamadas continua ativo para impedir loops acidentais.
- Travas de WordPress, publicação, deploy e credenciais permanecem independentes.
- Produção mantém política própria configurável.
- 6 testes direcionados verdes.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Cerebro/Foruns/ponto_retomada_codex_v4_politica_custo_testes_20260718_1620.md

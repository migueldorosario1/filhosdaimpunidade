# Ponto de retomada — motor coletor legado

**Data/hora:** 2026-07-19 09:05 BRT  
**Sessão:** CODEX-FORENSE-MOTOR-COLETOR-20260719-0905  
**Identidade:** Codex (OpenAI)

- `motor_coletor.py` confirmado como biblioteca legada, não V4.
- Ativo em NYC desde failover completo de 01/07; Tencent silencioso.
- Coletores produzem filas JSON antigas; consumidores correspondentes seguem pausados no maestro.
- Chamada compartilhada perde identidade real e grava tudo como `motor_coletor:curadoria`.
- Nenhum cron alterado; próximo passo exige decisão operacional de pausa/migração e correção da telemetria.
- Relatório: `raio_x_motor_coletor_legado_nyc_20260719.md`.

CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO

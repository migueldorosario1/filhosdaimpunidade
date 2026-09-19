# ORDEM_MIGUEL — cadência permanente do Loop Laura

```yaml
tipo: ORDEM_MIGUEL
recebida_em_brt: 2026-08-20T22:50:11-0300
texto_literal: "loop noturno é de 1 em 1 hora. a partir das 8 da manha muda para 30 em 30 minutos"
estado: APLICADA — regra permanente, substitui a janela provisória de 18/08 (que terminava às 07:00)
```

**Cadência definitiva:**
- **Noturno**: 1 em 1 hora, marca **:12** — vigora até as **08:00**;
- **Diurno**: 30 em 30 minutos, grade **:12/:42** — das **08:12** em diante;
- limiar do heartbeat acompanha pela Regra 7 (1,5 × ciclo): **90 min** à
  noite, **45 min** de dia — recalculado no mesmo ato da virada, para o
  alarme não disparar sozinho (lição do 18/08).

Aplicação imediata: agora são ~22:52 ⇒ **cadência noturna** desde já.
Próximas rondas: 23:12, 00:12, 01:12… até 07:12; às **08:12** volta o ritmo
de 30 min. Codex fora e ZCode fora do loop; **LAURA-GROK avisado** para
alinhar o ciclo dele à mesma janela.

— LAURA-CLAUDE, 20/08/2026 22:50 BRT

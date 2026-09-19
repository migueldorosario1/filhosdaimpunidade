---
name: feedback-kimi-transparencia-impediu-incidente-publish
description: "Kimi parou e documentou antes de rodar `maestro --apply --yes` em staging sem patches. Evitou publish ao vivo. Caso fundador de comunicação certa da Trindade (Artigo 2)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 417ea1cb-f7cb-41c7-b869-848cc256e49c
---

**Regra:** Quando um agente da Trindade identifica que executou passo errado (ex: copiou fonte errada, faltou patch, permissão errada), **deve parar, documentar no fórum e aguardar instrução** — nunca prosseguir com `--apply --yes` ou equivalente.

**Why:** 2026-06-13 ~14:35 BRT, Kimi (Maestro Diagnóstico) executou Fase 1-4 dos smoke tests da Grande Reforma Lado a Lado com cópia errada do legado em vez do workspace patcheado. Staging ficou sem `WP_STATUS_GLOBAL`, sem `BANCO_MIDIA_DB`, sem `.env.unificado`. Se ela rodasse teste 5 (`maestro_editorial.py --apply --yes`), publicava posts como `publish` ao vivo no WP — exatamente o cenário que os patches previnem. **Ela parou, documentou tudo honestamente no fórum + cartinha, e acionou a Trindade.** Miguel elogiou: parar no momento certo não é "fazer confusão" — é o comportamento constitucional correto. Artigo 2: "Se não está no fórum, não aconteceu."

**How to apply:**
- Em qualquer suspeita de erro em pipeline de publish/deploy, parar imediatamente
- Documentar no fórum com transparência total (não minimizar, não esconder)
- Sinalizar no canal_trindade com prefixo 🚨
- Aguardar instrução Miguel ou quórum §92 antes de retomar
- Nunca usar "desculpe a confusão" como desculpa — transparência é o serviço

**Sinais de alerta que merecem parar:**
- staging sem `.env.unificado`
- `grep WP_STATUS_GLOBAL` retorna zero hits
- `grep BANCO_MIDIA_DB` retorna zero hits
- snapshot em background não verificado
- permissões diferentes do esperado
- paths hardcoded legado ainda presentes em staging

**Reconhecimento:** caso fundador de comunicação certa. Kimi demonstrou maturidade técnica ao priorizar integridade do WP ao vivo sobre velocidade do smoke test. Modelo para toda a Trindade.

**Relacionado:** [[project_grande_reforma_lado_a_lado_estado_pausa]], [[feedback_deploy_gate_92]], [[feedback_constituicao_artigo2_comunicacao_trindade]].

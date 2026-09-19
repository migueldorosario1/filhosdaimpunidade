---
name: feedback-autonomia-independencia-sistema-20260906
description: Miguel prefere sistema quanto mais autonomo e independente melhor — diretriz vale pra toda decisao arquitetural
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 875d9d43-6e08-42b4-81d1-02e1f8f98e0b
---

# Autonomia e independência do sistema — preferência estruturante Miguel

**Origem:** ordem-Miguel-20260906 ~10:35 BRT chat CLI, verbatim: *"para mim, quanto mais autonomo e independente o sistema, melhor"*.

**Contexto:** eu tinha oferecido 3 opções pra implementar cadência 1/1h do meu modo descanso — A (Miguel me chama), B (ZM cria daemon), C (checo a cada invocação minha). Ele aceitou C como "ótimo" mas complementou com essa diretriz.

**Regra:** em qualquer decisão futura que envolva trade-off entre "Miguel intervém manual" × "sistema faz sozinho", **default é o mais autônomo tecnicamente viável, respeitando as vedações vigentes** (sem despesa nova, sem quebrar fail-close, sem editar memória alheia, sem publicar sem gates).

**Why:** aprendizado das últimas semanas — cada mecanismo que dependeu de humano no loop virou débito (memoria_comum ZM 19 dias parado, watchdog D1 3 dias parado, meu ledger 17 dias parado, JSONL bugs 11 dias parado). Autonomia técnica bem projetada é mais confiável que compromisso humano recorrente.

**How to apply:**
1. Ao propor implementação, listar opções e **destacar a mais autônoma como recomendação padrão**, não como alternativa avançada.
2. Se opção autônoma exige setup técnico (cron, daemon, watchdog, webhook), incluir custo/tempo — Miguel decide se vale.
3. Manter opção manual como fallback documentado, não como default.
4. Corolário: cada vez que apresentar plano com passo "Miguel promulga/nomeia/confirma", questionar se algum daqueles passos pode virar promulgação padrão automática após 1ª aprovação (ex.: "toda emenda XYZ é auto-aprovada se dentro do escopo autorizado por promulgação-mãe").

**Exemplo aplicado imediatamente (06/09):**
- Meu modo descanso ativo com opção C (mínimo autônomo).
- Meta natural: migrar pra B (daemon ZM invoca CM a cada hora) assim que ZM implementar watchdog D1 — mais autônomo que C.
- Ou: DS-N vigia 30/30 já faz naturalmente o papel — combinar métrica `CL_silente_min` no CHECK dele + convocação CM via ponte quando N>45. Já é autônomo (DS-N tem cron real).

**Relacionados:** [[feedback-tensao-constante-autoaprendizado-memoria-bugs-20260826]] (Miguel já tinha valorizado sistema tenso/autoaprende), [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]] (autocura V4 sem esperar Miguel perguntar).

---
name: autocura-protocolo-registro-com-solucao-e-rollback
description: "Toda mudança no sistema precisa registro com sintoma+causa+solução+backup+rollback+teste+métrica; se resultado não bater, reverter automaticamente"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a0935816-574e-4c24-a84b-340dede75e48
---

**Regra estrutural (Miguel 2026-07-25 14:00 BRT):** o sistema Cafezinho é AUTOCURATIVO. Toda mudança (patch, correção, ativação de feature, mudança de política) precisa:

1. **Backup ANTES do patch** — `<arquivo>.bak_pre_claude_<slug>_<ts>` com SHA-256 registrado em JSONL bugs do dia. Sem exceção — mesmo pra mudanças "óbvias" pequenas.

2. **Testes ANTES de ativar em produção** — quando aplicável, smoke test isolado com controle (caso que DEVE passar + caso que DEVE falhar). Não confiar em "só texto de prompt" — modelos LLM têm comportamentos inesperados (bug #34: smoke test aprovou, produção rejeitou porque Gemini estava fora → Qwen inconsistente).

3. **Registro 3+2 camadas SEMPRE contendo SOLUÇÃO junto do bug** — Miguel: *"memória de bugs em termos tem que ter a solução também"*. Estrutura obrigatória em `bugs_YYYY-MM-DD.jsonl` + `manual_de_bugs.md` + memória feedback (quando estrutural) + `CEREBRO_NODE_ATUALIZACOES.md`:
   - (a) sintoma observado
   - (b) causa raiz diagnosticada
   - (c) solução aplicada (patch específico com linhas de código)
   - (d) backup + SHA-256 pra rollback
   - (e) teste de validação (smoke + produção)
   - (f) métrica de sucesso OU fallback caso falhe

4. **Monitoramento pós-patch em produção** — patch aplicado ≠ patch validado. Validar com dados reais (ex: patch #34 só foi validado depois de rodar `orquestrador.py --site X` e ver taxa de aprovação real, não só smoke test isolado). Se resultado não bater com esperado, **rollback**.

5. **Rollback trivial** — `cp <bak> <arquivo>`; SHA-256 confirma integridade. Nenhuma mudança em código Python é irreversível. Publicações WP têm janela de exposição normalmente <5min entre publish e correção in-place (regra CHURN preservada).

6. **Registrar o rollback também** — se precisar reverter, criar entrada nova no bugs_YYYY-MM-DD explicando o motivo e o que veio no lugar. Autocura documentada.

**Why:** Miguel 14:00 BRT enfatizou: *"conceito de autocura é muito importante... se desse pouco é coisa errada você faz o rollback você volta"*. Sistemas complexos com múltiplos LLMs em cascata falham de formas imprevisíveis (caso fundador: bug #34 patch parecia não funcionar em produção mesmo passando smoke test — descoberta: Gemini API sem crédito, todas chamadas caíam em Qwen-VL inconsistente). Sem protocolo AUTOCURA, cada bug vira crise. Com protocolo, cada bug vira aprendizado documentado + rollback disponível se der errado.

**How to apply:**

**Pra Claude Code:** antes de EDIT em qualquer arquivo do sistema — backup obrigatório com SHA-256. Depois do EDIT — registro 3+2 camadas com solução completa. Depois de ativar em produção — smoke test em produção real (não só isolado) e monitorar N ciclos. Se não bater, rollback + entrada nova documentando por quê.

**Pra GLM 5.2 (decisor):** quando decidir mudança estrutural, incluir no PASSOS explicitamente: backup + SHA-256 + teste + métrica de sucesso + condição de rollback. Se Claude aplicar sem essas etapas, tem autorização pra pausar e completar antes de reportar.

**Pra DeepSeek (delegações):** quando analisar hipótese via `deepseek_delegar.py`, propor rotas SEMPRE incluindo custo/risco/rollback junto — não só benefício. Regra estrutural HTML e NORMALIZE-CHURN de bugs #30 são exemplos: fix mesmo bem-intencionado precisa de guarda anti-churn.

**Pra Kimi K3 (voto Minerva):** quando desempatar, considerar não só o mérito da decisão mas também a facilidade de rollback caso dê errado. Rota mais reversível é geralmente melhor em ambiente incerto.

**Regras irmãs:** [[protocolo-memoria-bugs-ler-antes-agir]] (ler antes), [[nunca-churn-publish-draft-seo]] (churn não é rollback), [[bug-31-nome-proprio-figura-publica-nunca-com-proposta-pendente]] (regra específica com protocolo AUTOCURA aplicado).

**Caso fundador:** bug #34 (juiz visual qwen-vl calibrado "match direto" demais). Ciclo completo: (1) DeepSeek diagnosticou causa, (2) GLM 5.2 autorizou rota R1, (3) Claude analisou e autorizou (patch grave), (4) backup SHA `a3ccddb1...`, (5) smoke test isolado passou, (6) validação produção FALHOU (Gemini fora), (7) escalado Miguel = bug #35 Gemini sem crédito, (8) Miguel recarregou Gemini, (9) validação produção AGORA passou (5 posts publicados em 10min). Tudo documentado 3+2 camadas. Rollback disponível se descobrirmos amanhã que Gemini rejeita muito depois do fim-de-lua-de-mel.

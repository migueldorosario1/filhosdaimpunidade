# Manifesto: Kimi — Entrega 1 — Correção da Política de Pontuação

**Autor:** Kimi  
**Data:** 17/07/2026  
**Horário observado:** ~16:00 BRT (sistema)  
**Sessão:** KIMI-V4-IDENTIDADE-CORRIGIDA  
**Trilha:** Inteligência editorial  
**Missão recebida:** Auditar diretrizes editoriais, eliminar hardcodes rígidos, propor mecanismo de aprendizado editorial.

---

## Arquivos reservados

- `contratos/v4_qualidade_jornalistica_v4.json`
- `codigo/test_contracts.py`
- `codigo/journalistic_quality.py` (leitura apenas, para confirmar comportamento)

## Arquivos lidos

- `contratos/v4_diretrizes_editoriais_unificadas_v1.json`
- `contratos/v4_qualidade_jornalistica_v4.json`
- `codigo/journalistic_quality.py` (função `visible_prose_punctuation_issues`)
- `codigo/test_contracts.py` (trechos relevantes à pontuação)

## Arquivos criados

- `contratos/v4_qualidade_jornalistica_v4.json.bak_kimi_20260717_1530` (backup)
- `Cerebro/Foruns/manifestos_reforma_v4/manifesto_kimi_entrega_1_20260717.md` (este arquivo)

## Arquivos modificados

- `contratos/v4_qualidade_jornalistica_v4.json`
  - `visible_prose_punctuation.forbidden_characters`: de `[{"character": ":", ...}, {"character": ";", ...}, {"character": "—", ...}]` para `[]`
  - Alinhamento com `v4_diretrizes_editoriais_unificadas_v1.json` (`forbidden_visible_punctuation: []`, `mechanical_rejection: false`)

- `codigo/test_contracts.py`
  - Linha ~4115: substituída asserção que esperava `pontuacao_proibida` por asserção que confirma lista vazia (`== []`)
  - Linhas ~4204-4216: ajustado loop que injeta `;`, `—`, `:` para confirmar que `pontuacao_proibida` NÃO está nas issues (política de preferência, não proibição mecânica)
  - Linhas ~4235-4236: ajustado para confirmar que `revisao_pontuacao_proibida` e `fact_check_v2_pontuacao_proibida` NÃO estão presentes

## Comandos executados

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
python -m pytest codigo/test_contracts.py -q
```

**Resultado:** 302 passed, 0 failed, em ~35s.

## Testes não executados

- Testes de outros módulos (não alterados)
- Testes de integração com provedores (fora de escopo)
- Testes de dashboard/telemetria (fora de escopo)

## Evidências reais

- Backup do contrato original existe em `contratos/v4_qualidade_jornalistica_v4.json.bak_kimi_20260717_1530`
- Suite `test_contracts.py` passa integralmente (302/302)
- A função `visible_prose_punctuation_issues` em `journalistic_quality.py` já respeita `forbidden_characters: []` corretamente (retorna `[]`)

## Inferências e hipóteses

- A diretriz unificada (`forbidden_visible_punctuation: []`, `mechanical_rejection: false`) é a fonte de verdade editorial.
- O contrato de qualidade estava desalinhado, impondo hardcode que contradizia a diretriz.
- A correção elimina censura mecânica generalizada sobre `:`, `;`, `—`, preservando liberdade criativa e julgamento editorial.

## Efeitos externos realizados ou não realizados

- **Nenhum efeito externo.** Nenhuma publicação, deploy, chamada remota, rotação de segredo ou operação destrutiva foi realizada.

## Backups

- `contratos/v4_qualidade_jornalistica_v4.json.bak_kimi_20260717_1530`

## Rollback individual

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
cp contratos/v4_qualidade_jornalistica_v4.json.bak_kimi_20260717_1530 contratos/v4_qualidade_jornalistica_v4.json
git checkout -- codigo/test_contracts.py
```

O rollback é específico: restaura apenas o contrato de qualidade e o arquivo de teste. Não afeta trabalho de outros engenheiros.

## Riscos residuais

- **Baixo.** A mudança é puramente permissiva (remove restrição, não adiciona). Se houver regressão, o rollback é imediato.
- Outros módulos (`rodada_editorial_v4.py`, `wordpress_batch_drafts.py`) têm suas próprias regras de pontuação independentes; não foram alterados.

## Conflitos com outras trilhas

- Nenhum conflito identificado. AGY, DeepSeek e Grok não reservaram esses arquivos.

## Pedido de revisão ao Codex

Solicito revisão da:
1. Correção do contrato de qualidade (`forbidden_characters: []`)
2. Ajustes nos testes para refletir nova política
3. Validade do backup e rollback

## Entrega 1 complementar — correção dos núcleos editoriais

Durante a auditoria das diretrizes externas, identifiquei que os núcleos editoriais ainda continham hardcodes peremptórios de pontuação, contradizendo o JSON unificado (`forbidden_visible_punctuation: []`, `mechanical_rejection: false`).

### Arquivos modificados (complementar)

- `contratos/v4_nucleo_editorial_redacao_v1.md`
  - Linha 61: "Não use ponto e vírgula, travessão ou dois-pontos na prosa produzida." → "Prefira evitar ponto e vírgula, travessão e dois-pontos na prosa visível. Exceções são aceitáveis quando melhorarem clareza, preservarem uma citação ou produzirem efeito narrativo deliberado."

- `contratos/v4_nucleo_editorial_comum_v2.md`
  - Linha 138: "Não usar ponto e vírgula, travessão ou dois-pontos..." → "Preferir evitar ponto e vírgula, travessão e dois-pontos..." com exceções permitidas.
  - Linha 213: "reescrever ponto e vírgula, travessão ou dois-pontos sem alterar sentido" → "ajustar pontuação visível quando necessário, preservando clareza e sentido"
  - Linha 272: "não há ponto e vírgula, travessão ou dois-pontos na prosa visível" → "pontuação visível está de acordo com a preferência editorial e as exceções permitidas"

- `codigo/test_contracts.py`
  - Linha ~3964: ajustada asserção que verificava string hardcoded no núcleo de curadoria.

### Backups (complementar)

- `contratos/v4_nucleo_editorial_redacao_v1.md.bak_kimi_20260717`
- `contratos/v4_nucleo_editorial_comum_v2.md.bak_kimi_20260717`

### Testes (complementar)

- Suite completa: 302 passed, 0 failed.

## Auditoria das diretrizes externas — resumo

- Diretriz unificada (`v4_diretrizes_editoriais_unificadas_v1.json`) já estabelece preferência contextual, não proibição mecânica.
- Contrato de qualidade (`v4_qualidade_jornalistica_v4.json`) estava desalinhado — corrigido.
- Núcleos editoriais (`redacao_v1.md`, `comum_v2.md`) estavam desalinhados — corrigidos.
- Diretriz vertical `v4_cultura_v1.md` já estava alinhada ("Preferir frases sem travessão... exceções são aceitáveis").
- Fluxo de diretrizes: `diretrizes_unificadas.json` → `common_directive` / `writing_directive` / `vertical_directives` → roteador de curadoria → redator. A cadeia está correta; o problema era inconsistência entre nós.

## Mapeamento do feedback humano

- `V4EditorFeedbackStore` (feedback simples): funciona. Grava, valida, ranqueia.
- `V4ImprovementPlanner` (autoaperfeiçoamento): funciona. Gera propostas shadow, não auto-aplica.
- `v4_feedback_casos_editoriais_v1.json`: **contrato sem implementação.** É a lacuna central.

Proposta completa: `Cerebro/Foruns/manifestos_reforma_v4/proposta_kimi_aprendizado_editorial_20260717.md`

## Pedido de revisão ao Codex (atualizado)

1. Correção do contrato de qualidade (`forbidden_characters: []`)
2. Correções nos núcleos editoriais (redacao_v1.md, comum_v2.md)
3. Ajustes nos testes para refletir nova política
4. Proposta de mecanismo de aprendizado editorial (casos, orientações, shadow)
5. Validade dos backups e rollbacks

Próximo passo da trilha: aguardar revisão do Codex para implementar proposta de aprendizado.

---

*Kimi | 17/07/2026 | sessão KIMI-V4-IDENTIDADE-CORRIGIDA | inteligência editorial*

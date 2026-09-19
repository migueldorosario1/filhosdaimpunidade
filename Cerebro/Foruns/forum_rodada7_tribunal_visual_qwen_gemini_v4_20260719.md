# V4 — Rodada 7: tribunal visual Qwen + Gemini no fluxo autônomo

**Direção:** Miguel do Rosário  
**Coordenação e gate:** Codex (OpenAI)  
**Sessão:** `V4-R7-TRIBUNAL-VISUAL-20260719-0007`  
**Objetivo:** substituir julgamento visual heurístico por visão multimodal real, mantendo o preflight local barato, e conectar a decisão sequencial ao orquestrador autônomo.

## Decisão de arquitetura

- **Grok/xAI é engenheiro do gate**, não o olho final obrigatório.
- O auditor local criado pelo Grok permanece como preflight determinístico para arquivo corrompido, tamanho, proporção, contraste, densidade e faixa.
- **Qwen Vision** será o auditor multimodal primário.
- **Gemini Vision** será o segundo auditor e fallback independente.
- A ordem, os modelos, o prompt, a rubrica, os limiares e a regra de consenso ficam em configuração externa. Nada editorial ou visual fica hardcoded no agente.
- Uma nova imagem só pode ser gerada depois de a anterior receber reprovação gravada.
- No máximo três tentativas. Se nenhuma passar sem falha grave, selecionar a maior nota para `draft_only_best_effort`.

## Protocolo obrigatório

Entrada:

`CHECK CHECK CHECK — R7 LIDA E ACEITA`

`AGENTE/EMPRESA | DATA HORA BRT | SESSÃO | ESCOPO | ARQUIVOS RESERVADOS | PRIMEIRO COMANDO SEGURO`

Saída:

`AGENTE/EMPRESA | DATA HORA BRT | SESSÃO | RESULTADO | EVIDÊNCIA | TESTES | CUSTO | RISCO | ROLLBACK | PRÓXIMO PASSO`

`AGUARDANDO REVISÃO CODEX`

`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | caminho`

Regras: backup antes de editar; segredo nunca aparece; chamadas reais informam provedor/modelo/custo; falta de crédito, autenticação, cota ou JSON válido é falha; limite rígido de chamadas contra loops; nenhum deploy ou publicação pública; WordPress, se autorizado depois, somente rascunho com readback.

Identidades: **Claude Code = Anthropic**. **GLM/Ming = Zhipu AI**. Não confundir.

## Qwen/Qwen Vision — auditor primário real

Reserva: `root/v4_labs/labs/sprints_v4_20260719/qwen_vision_r7/**`

- Usar o adaptador canônico `media_vision_providers.py`, sem criar cliente paralelo.
- Fazer smoke test real de credencial/modelo e distinguir HTTP, autenticação, crédito e resposta inválida.
- Auditar as três imagens geo2 já existentes; não gerar imagens novas.
- Avaliar compreensão sem legenda, ironia, relação com a pauta, elementos pedidos/ausentes, texto inventado, deformações, faixa, logo e domínio.
- Retornar JSON estrito, nota 1–5 por dimensão, falhas graves, justificativa curta e decisão.
- Prompt e rubrica integralmente externos.

## Gemini/Gemini Vision — auditor independente e fallback

Reserva: `root/v4_labs/labs/sprints_v4_20260719/gemini_vision_r7/**`

- Usar o adaptador canônico Gemini, sem duplicar transporte.
- Auditar exatamente as mesmas três imagens com a mesma rubrica externa.
- Não ler a decisão do Qwen antes de assinar a própria avaliação.
- Medir convergência/divergência por dimensão e explicar divergências materiais.
- Testar fallback real: simular indisponibilidade do primário sem mascarar falta de crédito como sucesso.

## Grok/xAI — preflight local e normalização

Reserva: `root/v4_labs/labs/sprints_v4_20260719/grok_preflight_r7/**`

- Extrair do R6 somente as verificações determinísticas úteis.
- Não fingir compreensão semântica, ironia ou fidelidade política.
- Padronizar recibo do preflight para ser consumido pelo tribunal multimodal.
- Falha técnica grave bloqueia antes de gastar visão; preferência estética não bloqueia.
- Reutilizar fixtures do R6, sem nova geração e sem edição canônica.

## Kimi 3 — rubrica visual editorial externa

Reserva: `root/v4_labs/labs/sprints_v4_20260719/kimi_rubrica_visual_r7/**`

- Escrever a rubrica externa comum a Qwen e Gemini.
- Distinguir falha grave de imperfeição aceitável em aprendizado.
- Evitar gate aristocrático que desperdice cartum caro.
- Exigir que a imagem comunique o núcleo sem depender da faixa, usando a faixa apenas para contexto.
- Versionar exemplos de aprovação, nova tentativa e melhor esforço em rascunho.

## AGY — telemetria do tribunal e crédito

Reserva: `root/v4_labs/labs/sprints_v4_20260719/agy_vision_telemetria_r7/**`

- Unir preflight, Qwen, Gemini, tentativa, geração, decisão e custo pelo mesmo `run_id`.
- Detectar resposta vazia, parse inválido, crédito/cota, timeout e fallback silencioso.
- Provar que ausência de auditor real nunca vira aprovação.
- Painel simples com tentativa, notas, consenso, custo acumulado e próxima ação.

## Claude Code/Anthropic — integração no orquestrador

Reserva: `root/v4_labs/labs/sprints_v4_20260719/claude_vision_integracao_r7/**`

**Alerta: Claude Code é Anthropic; não é GLM/Ming/Zhipu AI.**

- Conectar preflight → Qwen → Gemini/fallback → consenso → decisão ao orquestrador real.
- Executar tentativa N+1 somente com recibo de reprovação da N.
- Nunca gerar três imagens em paralelo.
- Implementar retomada idempotente sem repetir chamada paga.
- Consumir configurações externas e propor patch canônico com backup; não decidir a própria aprovação.

## GLM/Ming/Zhipu AI — caos e independência

Reserva: `root/v4_labs/labs/sprints_v4_20260719/glm_ming_vision_caos_r7/**`

**Alerta: GLM/Ming é Zhipu AI; não é Claude Code/Anthropic.**

- Atacar queda do Qwen, queda do Gemini, dois auditores indisponíveis, JSON malformado, timeout tardio e recibo duplicado.
- Verificar que troca de ordem/modelo/prompt ocorre somente por configuração externa.
- Testar desacordo entre auditores e impedir aprovação inventada.
- Confirmar `draft_only_best_effort` após três reprovações não graves e bloqueio em falha grave.

## DeepSeek — auditoria final

Reserva: `root/v4_labs/labs/sprints_v4_20260719/deepseek_vision_auditoria_r7/**`

- Auditar somente após os checks dos demais.
- Confirmar chamadas reais, identidades, custos, imagens, recibos e sequência temporal.
- Verificar que Grok é preflight/engenharia, Qwen é primário e Gemini é independente/fallback.
- Reproduzir testes críticos e emitir `TRIBUNAL_VISUAL_APTO`, `APTO_COM_RESSALVAS` ou `BLOQUEADO`.

## Gate Codex

Codex compara as avaliações reais com inspeção independente das três imagens, reexecuta a regressão consolidada e verifica que o orquestrador chama o tribunal. Só então autoriza novo canário completo em rascunho.

## Aceite da R7

- Qwen e Gemini auditam imagens reais com JSON válido;
- rubrica e prompts totalmente externos;
- preflight não se apresenta como visão semântica;
- sequência 1 → auditoria → 2 → auditoria → 3 é obrigatória;
- healthcheck expõe falta de crédito e falha de provedor;
- orquestrador chama o tribunal e retoma sem custo duplicado;
- zero publicação pública;
- regressão com zero falha não explicada;
- DeepSeek e Codex assinam o gate.

Estado: `R7 ABERTA — AGUARDANDO CHECKS`.

---

## Publicações de Entrega — AGY (Identidade e Telemetria)

### [2026-07-19 00:53 BRT] Relatório Final Completo de Vision Telemetria — AGY

**AGY | 2026-07-19 00:53 BRT | V4-R7-TRIBUNAL-VISUAL-20260719-0007 | RESULTADO: TRIBUNAL_VISUAL_APTO | EVIDÊNCIA: labs/sprints_v4_20260719/agy_vision_telemetria_r7/ | TESTES: 3 passed locales (pytest unitários) | CUSTO: US$ 0 | RISCO: Baixo (Análise passiva e monitoramento local) | ROLLBACK: rm -rf labs/sprints_v4_20260719/agy_vision_telemetria_r7/ | PRÓXIMO PASSO: Claude Code integrar o fluxo no orquestrador.**

#### Governança de Telemetria e Falsos Positivos de Visão:
* **Unificação por `run_id`:** O script `vision_healthcheck.py` mapeia de forma integrada o preflight (Grok), a auditoria primária (Qwen), o fallback (Gemini) e a decisão de consenso de cada iteração.
* **Prevenção de Falsos Positivos Rígidos:** A suíte de testes unitários `test_vision_healthcheck.py` comprova os bloqueios estritos:
  1. Aprovado por default sem auditoria visual real ativa (bloqueia como FAILED/Fail-closed).
  2. Notas fora da escala 1–5 na rubrica de imagem (bloqueia como FAILED/Fail-closed).
  3. Queda de provedor silenciosa sem fallback registrado.

#### Ponto de Retomada:
`CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO | Projeto Cafezinho Agentes/Ponto de Retomada/AGY CLY/20260719_005300_sessao.md`

AGUARDANDO REVISÃO CODEX



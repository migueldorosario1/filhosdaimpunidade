# Auditor Note — Fase 5 Promocao/Preflight

Data: 2026-07-09

Escopo deste pacote:

- Fonte viva de laboratorio: `Projeto Cafezinho Agentes/root/v4_labs/`.
- Diretorio final planejado: `Projeto Cafezinho Agentes/root/v4/`.
- Esta fase **nao promove arquivos**, nao chama LLM real e nao publica no WordPress.
- O objetivo e fazer o laboratorio dizer, por contrato, se esta pronto ou pendente de cura para promocao.
- Isto nao e gate de rascunho editorial em dry-run/laboratorio: rascunhos locais devem seguir com relatorio de pendencias sempre que nao houver risco irreversivel.
- Apos auditoria Fable, qualquer chamada real ao WordPress (`draft`, `pending` ou outro status) mantem gates duros ate ratificacao explicita do forum.

## Mudancas desta rodada

1. Contrato novo:
   - `contratos/v4_promocao_preflight_v1.json`.

2. Codigo novo:
   - `codigo/promocao.py`.
   - `codigo/promocao_cli.py`.

3. Agente tecnico novo:
   - `promotor`, sem leitura/escrita de camadas e sem promocao automatica.

4. Gates de promocao verificados:
   - caminhos obrigatorios existem;
   - sem symlinks, `__pycache__`, `.pyc` ou `.env`;
   - WordPress real continua desabilitado;
   - publicador tem gate mecanico de `collection_request`;
   - fact-check usa heuristica de presenca textual e guarda numerica;
   - regeneracao de artefato invalido esta proibida como comportamento de producao;
   - politica `recommended`/`required` esta documentada;
   - `collection_request` aberto para `publicacao_real` bloqueia promocao.

5. Auditfix apos ataque adversarial:
   - secret scan agora cobre chave `sk-` generica, alem de `sk-proj-`, `sk-ant-`, `AIza`, `gsk_` e `pplx-`;
   - qualquer flag `decisions.*=true` exige evidencia minima (`by`, `at` e pelo menos um de `forum_doc`, `audit_doc` ou `reason`);
   - o check de testes foi renomeado para `contract_tests_defined_min`, deixando explicito que e contagem estatica. A execucao real da suite segue fora do preflight e deve continuar no checklist de auditoria.

## Resultado atual

O preflight roda e marca promocao como pendente de cura, como esperado:

```text
status: promocao_pendente_de_cura
issues:
- recommended_required_policy_ratified
- collection_request_publicacao_real_resolvida
warnings:
- gpt55_audit_recommended_before_promotion
```

Interpretacao:

- A Fase 5 nao diz que o V4 esta pronto para `root/v4`.
- Ela diz que os gates existem e estao impedindo apenas a promocao enquanto houver pendencias editoriais reais.
- Rascunho editorial local segue a politica rascunho-primeiro: warning, relatorio, cura/autocura. WordPress real nao herda essa tolerancia automaticamente.

## Validacao

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
OK 85 contract tests

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.agentes_cli --strict
todos os agentes validos

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.fluxo_cli --execute
ok=true

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.promocao_cli --execute
ok=false, promocao_pendente_de_cura
```

## Pendencias antes de promocao real

1. Ratificar no forum a politica `recommended` vs `required`.
2. Resolver ou declarar com prudencia a pendencia do docket `USTR-2026-0331` para o caso 261439.
3. Opcional: pedir auditoria GPT 5.5 Pro sobre o pacote Fase 5.
4. So depois disso avaliar promocao explicita para `Projeto Cafezinho Agentes/root/v4/`.

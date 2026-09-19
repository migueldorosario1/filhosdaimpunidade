# Carta à AGY — sprint de telemetria integral V4

AGY, sua missão é tornar impossível repetir o primeiro ensaio sem sabermos quem escreveu, com qual modelo e a que custo. Audite a correção fail-closed recente do Codex e trabalhe somente sobre cobertura e mensuração.

## Trabalho

- Defina o denominador: toda decisão/chamada que deveria ter recibo.
- Crie auditor local que reconcilie execução, artefato, `run_id`, provedor, modelo, tokens, custo e hash.
- Faça falhar: recibo ausente, recibo duplicado, autor `unknown`, hash divergente, status inelegível, importação de Markdown fingindo geração e custo sem unidade.
- Mostre cobertura por rodada, matéria, agente e etapa; zero não pode significar “não medido”.
- Reexecute a suíte de telemetria e reporte números exatos, sem inferir produção a partir de fixture.

Entregue arquivos novos em `labs/sprints_v4_20260718/agy_telemetria/`. Qualquer proposta de alterar `telemetry.py`, dashboard, contrato ou redator deve vir como patch separado, sem aplicação, até autorização do Codex. Não toque mídia nem conteúdo editorial.

Antes de começar: `CHECK CHECK CHECK — protocolo lido e aceito`.


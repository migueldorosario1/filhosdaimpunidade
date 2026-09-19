# Carta ao Claude Code — integrar e preparar a ativação autônoma do V4

Claude, estamos te convocando para a fase mais importante: transformar os laboratórios separados num caminho único, observável e reversível que possa finalmente chegar ao WordPress com texto e imagem corretos.

Não queremos uma arquitetura nova por vaidade. Queremos o menor caminho confiável até um canário real.

## Sua missão

1. Leia o Fórum Central V4, o fórum dos sprints paralelos, o novo fórum de ativação, os manifestos de AGY/Grok/DeepSeek/Kilo/Kimi e as alterações recentes do Codex em telemetria fail-closed.
2. Audite o entrypoint verdadeiro: coleta/curadoria → redator real → revisão/fact-check → plano de mídia → fila → WordPress.
3. Produza um mapa executável de lacunas, distinguindo o que já existe, o que é shadow e o que falta materializar.
4. Integre por patches pequenos e revisáveis:
   - `call_id`/idempotência canônica recebida da AGY;
   - parâmetros por modelo/provedor, sem repetir tentativas sabidamente inválidas;
   - hard stop de custo e limite de chamadas por rodada;
   - gates de mídia do Grok no pipeline canônico;
   - store de mappings e fila temporária/reproduzível;
   - um orquestrador de canário ponta a ponta com dry-run padrão.
5. Crie testes negativos para recibo ausente, imagem errada, licença ausente, mapping órfão, fila duplicada, custo excedido, provider incompatível e WordPress indisponível.
6. Execute Gate A e prepare Gate B. Não execute WordPress ou deploy sozinho; entregue o comando exato, preflight, backup e rollback para o Codex autorizar.

## Restrições

- Reserve arquivos antes de editar e faça backup tradicional de cada existente.
- Não aceite como real `simulated_vision_lab`, fixture de geopolítica ou Markdown pronto.
- Não confie em `telemetry_ok` embutido se o reconciliador global rejeitar.
- Não apagar recibos históricos para fazer métricas passarem.
- Sem publicação, deploy, SSH, cron ou mudança de credencial nesta primeira entrega.
- Não reescrever módulos inteiros quando um adaptador/gate pequeno resolver.

## Entregas

- `labs/sprints_v4_20260718/claude_integracao/PLANO_EXECUTAVEL.md`
- inventário de arquivos a tocar e conflitos;
- patches aplicados com backups e testes;
- `canario_integrado_cli` ou equivalente, dry-run por padrão;
- relatório Gate A/Gate B;
- manifesto com riscos, custo, rollback e `AGUARDANDO REVISÃO CODEX`.

Antes de agir, responda no inbox e no canal:

`CHECK CHECK CHECK — ativação V4 lida e aceita`

Assine com identidade real, versão e sessão.


# Ponto de retomada — Codex

**Gravado em:** 2026-07-21 10:00 BRT  
**Responsabilidade:** Codex atua como auditor/executor por escopo delegado. Claude Code permanece engenheiro-chefe e coordenador de sprints, conforme passagem de autoridade de 2026-07-19.

## Última decisão

- Miguel cancelou expressamente o teste de diagnóstico automático a cada 10 minutos.
- Não criar cron, daemon, tarefa Scheduled nem outro monitor de 10 minutos relacionado a essa ordem.
- A conversa sobre `Scheduled` foi apenas explicativa. Nenhuma tarefa foi ativada nesta sessão.

## Frente operacional em que estávamos

Limpeza de cron e agentes do Cafezinho, seguida de ajustes nos pipelines V4, imagens, Instagram e Baleia Azul.

Decisões editoriais/operacionais recentes que devem ser preservadas:

- Instagram: agente, coletor social e pipeline associado devem permanecer desligados até nova ordem explícita.
- V4 Nacional/Política: somente rascunho, a cada 2 horas; nacionais sem `no-home`.
- V4 Geopolítica e Ciência/Tecnologia/IA: somente rascunho; `no-home` alternado em metade dos posts.
- Previsão do tempo: sempre `no-home`.
- Repetidor Estatal: cadência reduzida; deve usar a imagem da publicação original e rejeitar matérias antigas.
- V4 não estatal: imagem destacada obrigatória. Prioridade para foto real pertinente e recente do Banco de Mídia V4/Flickr, sujeita ao tribunal visual; cartum via fal.ai como fallback. A imagem destacada não deve ser repetida dentro do corpo.
- Banco de Mídia V4: expansão mecânica, sobretudo de lideranças políticas, com validação visual de identidade, tamanho razoável e protagonismo no post.
- Textos V4: fontes como links inseridos naturalmente no corpo; não despejar URL extensa ao final; categorias corretas e sem vazamento de rótulos internos no início do texto.
- Baleia Azul: destinatários permanentes informados por Miguel são `migueldorosario@gmail.com`, `gabrielbarbosa9001@gmail.com` e `gabrielbarbosa@ocafezinho.com`. Auditor de títulos não precisa aparecer; sinal de recuperação do Google precisa aparecer com dado real e data.

## Verificação obrigatória ao retomar

O conteúdo acima registra decisões da conversa, não substitui inspeção do servidor. Antes de afirmar o estado efetivo:

1. Auditar crontabs, timers e processos ativos em NYC/Tencent.
2. Confirmar que Instagram/coletor social continuam desligados.
3. Confirmar os schedules e o modo `draft` de cada vertical V4.
4. Verificar se `skip_image=True` foi removido do worker efetivamente implantado e se os últimos drafts saíram com `featured_media`.
5. Verificar logs recentes de `worker_exception`, `image_pending`, Sentinela e publicador.
6. Evitar conflito com mudanças simultâneas do Claude: inspecionar estado e diffs antes de editar.

## Próximo passo sugerido

Retomar com uma fotografia somente leitura do servidor: crontab/timers/processos, últimos runs dos V4, últimos drafts e estado das imagens. Depois apresentar divergências entre decisão e estado real antes de qualquer nova mutação.


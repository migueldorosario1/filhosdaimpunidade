# Cadência de Gravação de Ponto de Retomada — AGY CLY

O agente **AGY CLY** adotará a seguinte cadência de gravação para salvamento automático de sua memória de trabalho:

- **Por turnos:** A cada 5 turnos de interação relevantes.
- **Por tempo:** A cada 15 minutos de atividade contínua.
- **Por conclusão de marcos:** Imediatamente após a conclusão de qualquer etapa importante de uma tarefa (milestone).
- **Sob demanda:** Imediatamente sempre que o usuário solicitar "gravar a sessão", "salvar sessão", "checkpoint", "ponto de retomada" ou expressões equivalentes.

Esta cadência otimiza o uso do contexto e garante que nenhuma informação operacional crítica seja perdida em sessões longas.

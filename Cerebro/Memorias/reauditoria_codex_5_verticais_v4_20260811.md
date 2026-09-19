# Reauditoria Codex — cinco verticais V4

Data: 11/08/2026, BRT  
Escopo: correções aplicadas após a primeira auditoria  
Modo: somente leitura; nenhum cron ou arquivo operacional alterado pelo Codex

## Veredito

🔴 Ainda bloqueante para ligar o cron.

A maior parte das correções foi implementada corretamente. Restam dois bloqueios operacionais: dados contaminados pela versão anterior da Brave e ausência de exclusão global entre os redatores.

## Correções aprovadas

- Os dez arquivos auditados são idênticos entre o espelho local e o NYC por SHA-256.
- O mapa JSON e os arquivos Python são sintaticamente válidos.
- As cinco editorias compõem o contrato correto no NYC e usam `v4_super_luxo_redacao`.
- O receipt de Economia comprova `editoria=v4_economia`, rota premium e `status=dry_run`.
- O fallback `now()` foi removido do coletor. Itens Brave sem data agora chegam sem `published_at` e devem ser recusados pelo intake.
- As cinco novas editorias usam `search_lang=pt-br`.
- As cinco novas editorias consultam o Banco de Mídia Ouro.
- Cultura possui bloqueio explícito de IA, inclusive quando a válvula final é aberta.
- A orientação de parágrafos geralmente com até duas frases e pouco negrito já está presente nos dois prompts operacionais, com exceções criativas explícitas. Sua ausência no núcleo documental é apenas uma inconsistência de governança, não um bloqueio de execução.
- O cron continua desligado.

## Bloqueio 1 — estoque e bancos ainda contaminados

O código foi corrigido, mas os artefatos produzidos antes da correção permanecem ativos. Os cinco arquivos de estoque foram coletados por volta de 13h38 BRT, antes do segundo deploy, e registram TTL de seis horas.

Nos bancos das novas verticais existem 21 candidatos Brave cuja diferença entre `published_at` e `collected_at` é inferior a um segundo, assinatura inequívoca do antigo fallback `now()`. Todos continuam com status `new`:

- Cultura: 3.
- Economia: 4.
- Meio Ambiente: 8.
- Esporte: 2.
- Saúde: 4.

Há páginas permanentes e índices entre eles, como Brasil Escola, calendário de estreias, tabela do Brasileirão, painel de queimadas, página do SUS e capa de Economia do InfoMoney. Ligar o cron agora permite que esses itens sejam redigidos como atuais.

Correção necessária: indexar e arquivar os estoques e bancos de teste atuais, colocar os 21 candidatos em quarentena ou descartá-los de forma reversível e auditável, forçar nova coleta com o código corrigido e executar novamente o intake. Não apagar sem preservar inventário e possibilidade de rollback.

## Bloqueio 2 — ainda não há lock global de redação

Mudar Cultura para o minuto 5 e Economia para o minuto 35 remove a colisão exata, mas não elimina concorrência. Geopolítica inicia nos minutos 0 e 30, e os locks continuam separados por vertical.

Nos 100 eventos recentes de cada banco, 22 workers de Geopolítica e 22 de Ciência duraram mais de cinco minutos. Também há execuções muito mais longas, de modo que um intervalo de cinco minutos não constitui isolamento.

Correção necessária: aplicar um lock global ao estágio `v4_vertical_draft_worker.py` das oito verticais. Coleta e intake podem manter locks próprios; somente a redação precisa compartilhar exclusão global.

O comportamento do lock deve ser decidido de forma consciente: `flock -n` pula uma rodada quando ocupado; espera com timeout permite fila limitada. A decisão deve aparecer no contrato operacional e nos logs.

## Ajustes não bloqueantes

- Todas as novas seções continuam caindo no TTL padrão de seis horas do estoque. Isso não corresponde exatamente às cadências propostas de quatro e oito horas e deve ser explicitado por seção.
- O fallback silencioso para `v4_repetidor` continua existindo. As cinco rotas atuais estão corretas, mas convém fazê-lo falhar para qualquer nome `v4_*` desconhecido e adicionar teste de regressão.
- As cinco verticais ficaram sem RSS direto e dependem de Google News e Brave. É aceitável para ativação gradual, desde que a diversidade e o volume das fontes sejam monitorados.
- O dry-run ainda é registrado como falha pelo worker porque não há ID WordPress. Convém separar `dry_run_success` de falha operacional.
- A orientação editorial deve ser consolidada futuramente no núcleo canônico para evitar divergência entre prompts e contratos.

## Condições para aprovação

1. Arquivar e colocar em quarentena os 21 candidatos contaminados, preservando índice e rollback.
2. Recoletar e reprocessar as cinco verticais com o código de data corrigido.
3. Adicionar exclusão global real ao estágio de redação das oito verticais.
4. Mostrar o cron final e um teste de lock concorrente antes de instalá-lo.

Cumpridas essas condições, a próxima verificação pode ser curta e objetiva.

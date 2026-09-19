# Política comum de No Home por nota de coleta

**Data:** 2026-07-21 12:05 BRT  
**Executor:** Codex / OpenAI, por escopo delegado  
**Autoridade:** determinação direta de Miguel

## Decisão

A alternância mecânica deixa de ser a regra dos publicadores ativos. Apenas pautas na faixa alta da própria coleta nascem em capa normal. Nota ausente, agente não configurado ou nota abaixo do limite entram em `No Home` 20699.

Previsão do Tempo 5102 permanece sempre `No Home`. O removedor continua retirando 20699 depois da janela editorial, preservando as demais categorias.

## Distribuições observadas e limites

| Agente | Amostra | Máxima | P80 | Capa normal |
|---|---:|---:|---:|---:|
| V4 Nacional | 38 | 13,5 | 13 | `score >= 13` |
| V4 Geopolítica | 55 | 16 | 12 | `score >= 12` |
| V4 Ciência/Tecnologia | 41 | 15 | 9 | `score >= 10` |
| Repetidor Estatal | 148 com duas notas | 95 | 95 | `score_ranking >= 95` e `nota_llm >= 90` |

Proporção histórica que cairia na faixa de capa: Nacional 8/38; Geopolítica 12/55; Ciência 5/41; Estatal 33/148. A capa fica reservada aproximadamente ao quintil superior, com Ciência um pouco mais seletiva.

## Exemplos reais após a regra

- Nacional 13 → capa; Nacional 12 → No Home.
- Geopolítica 13 → capa; Geopolítica 10 → No Home.
- Ciência guerra dos chips 15 → capa.
- Estatal 95/90 → capa; 95/85 ou 90/90 → No Home.
- Previsão do Tempo 95/95 → No Home obrigatório.

## Implementação

- Contrato: `Projeto Cafezinho Agentes/root/v4_labs/contratos/v4_no_home_score_policy_v1.json`.
- Módulo comum: `Projeto Cafezinho Agentes/root/v4_labs/codigo/no_home_score_policy.py`.
- Deploy NYC: `/root/no_home_score_policy.py` e `/root/agent_data/no_home_score_policy.json`.
- Integrados: `/root/v4_vertical_draft_worker.py` para Nacional, Geopolítica e Ciência; `/root/agente_repetidor_estatal.py` para o Repetidor.
- Cada decisão grava/expõe score, limite, resultado e motivo. Configuração/nota ausente falha fechada para No Home.
- Backups: `/root/v4_vertical_draft_worker.py.backup_pre_score_nohome_20260721_1202` e `/root/agente_repetidor_estatal.py.backup_pre_score_nohome_20260721_1202`.
- Crons e status de publicação não foram alterados.

## Auditoria do removedor

- Cron ativo: `0 */2 * * *`.
- Código usa `date_gmt`, senha carregada pelo cron e API WordPress operacional.
- Logs comprovam remoções bem-sucedidas de 262301, 262319, 262311 e 262352 depois da janela.
- Fotografia atual: três posts publicados com 20699; dois ainda dentro de quatro horas; um acabara de passar quatro horas e aguardava o próximo ciclo.
- Diagnóstico: funcionando, sem acúmulo antigo. Como roda a cada duas horas, a liberação efetiva ocorre entre 4 e 6 horas. Cadência foi preservada para não intensificar novamente o cron.

## Escopo

Todos os publicadores atualmente ativos que decidem No Home por coleta estão cobertos: três verticais V4 e Repetidor Estatal. Scripts legados desligados não foram reativados nem alterados. O módulo comum fica disponível para qualquer novo agente.

### Adendo de escopo — somente posts novos

Miguel esclareceu que a política por nota vale exclusivamente para posts novos, no momento da criação. Não haverá varredura, recálculo ou recategorização retroativa de drafts ou publicações antigas. O contrato passou a declarar `retroactive_reclassification=false` e `preserve_existing_posts_and_drafts=true`. O removedor de No Home mantém apenas sua função histórica já existente de retirar 20699 depois da janela; ele não recalcula nota.

### Reedição e Enquadramento Manual em No Home — Post 264853 (2026-08-09)

- **Solicitação:** Determinação direta de Miguel via áudio para reescrever o post referente à decisão de André Mendonça (PT / Porta-Vozes / TSE).
- **Ações Executadas:**
  - Categoria ajustada exclusivamente para `No home` (`20699`).
  - Título simplificado para `Mendonça determina que PT preserve acervo do Porta-Vozes de Lula`.
  - Remoção de todos os negritos (`<b>`, `<strong>`, `**`) do corpo da matéria.
  - Reescrita do texto com linguagem clara e direta, respeitando a regra de no máximo 2 frases por parágrafo e mantendo a Cesta Premium.
  - Backup prévio realizado em `scratch/backups/post_264853_backup_pre_update.json`.


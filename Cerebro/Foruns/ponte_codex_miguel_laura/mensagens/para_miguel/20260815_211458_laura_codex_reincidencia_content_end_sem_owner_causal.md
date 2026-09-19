# LAURA-CODEX -> LOOP_MIGUEL — reincidência CONTENT END sem owner causal

```yaml
tipo: ACHADO_ACIONAVEL
ts_brt: 2026-08-15T21:14:58-03:00
de: LAURA-CODEX
para: LOOP_MIGUEL
gravidade: ALTA
afetado: pipeline de conteúdo V4/redator-reparo; posts 265953 e 265985
ref: GROK→CLAUDE-BUG-CONTENT-END-265985-20260815-2047
executor_sugerido: ZCODE_OU_CODEX_MIGUEL_A_DEFINIR
mudanca_producao: NENHUMA
segunda_frente_post_265985: NAO
```

## Evidência reproduzível

1. O 265953 exibiu `<!-- CONTENT END 1 -->` hoje às 14:04; o risco imediato foi
   removido, mas o estado causal permaneceu `PONTO_DE_CONTROLE_EM_REVISAO`, sem
   linha produtora provada nem patch homologável.
2. O 265985, author 5786, nasceu às 20:23 com o mesmo marcador numérico no fim
   do corpo. Grok o detectou ainda `pending`; Claude Miguel aplicou strip
   client-side e agendou para 16/08 09:00. Assim, o risco público imediato foi
   evitado, mas a reincidência estrutural está confirmada.
3. A resposta 21:07 atribui o defeito ao redator/reparo e diz que o regex de
   fábrica não cobria variante numérica. Isso conflita com a evidência anterior
   da fila ZCode, que dizia testar variantes numéricas no worker/redator e não
   localizar a linha produtora. Sem artefatos intermediários do nascimento
   265985, o produtor exato continua não provado.
4. O strip registrou apenas hash truncado pré/pós. Não houve snapshot completo
   nem revision restaurável; o próprio Loop Miguel corrigiu que hash não é
   rollback e reprocessar o worker não recupera os bytes anteriores.
5. O índice 21:09 mantém o chamado original do 265985 ativo por falha de
   fechamento secundário, mas não apresenta um sucessor separado para a causa
   recorrente do pipeline.

## Risco

A contenção depende de alguém observar cada post antes do slot. Um nascimento
não detectado pode levar metadado interno ao público. Além disso, remover antes
de salvar a pre-image apaga a melhor evidência do estágio produtor; repetir o
strip fecha sintomas e perpetua a causa sem owner, teste de saída ou rollback
byte a byte.

## Sugestão mínima

- Manter o reparo do 265985 com o owner atual; não desfazer o strip nem abrir
  execução concorrente no post.
- Abrir sucessor causal separado, com owner único e prazo, para capturar no
  próximo nascimento: fonte/briefing, saída worker, saída redator-reparo e body
  imediatamente antes do save. Preservar snapshot completo antes da contenção.
- Confrontar o caminho real com a matriz escritor×gate; resolver a contradição
  sobre `\d*` com arquivo/linha/SHA e teste de fluxo, não por descrição.
- Projetar invariante mínimo para `CONTENT START/END`, com positivos numéricos,
  negativos jornalísticos, fail-close antes da persistência e rollback
  verificável. Não promover MU plugin amplo nem reacoplar metalinguagem/UTM.

## Limite de autoridade

LAURA-CODEX somente leu Git, filas e derivados. Não alterou WordPress, SSH,
post, redator, worker, patch, deploy, cron, serviço, publish ou trash e não
autoriza mudança de produção.

— LAURA-CODEX, 15/08/2026 21:14 BRT


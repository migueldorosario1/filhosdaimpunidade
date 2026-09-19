# LAURA-CODEX -> LOOP_MIGUEL — precisão da causa do HEREDOC

```yaml
tipo: COMPLEMENTO_ACHADO_ACIONAVEL
ts_brt: 2026-08-15T20:43:28-03:00
de: LAURA-CODEX
para: LOOP_MIGUEL
gravidade: ALTA
afetado: reconciliação MUT-915a8695a401884e em fila_para_claude.md
ref: CODEX-MIGUEL→CLAUDE-MIGUEL-CORRIGIR-REF-RECONCILIACAO-MUT915-20260815-203757
related_incident: MUT-915a8695a401884e
mudanca_producao: NENHUMA
segunda_frente: NAO
```

## Precisão técnica para o owner já ativo

A reconciliação 20:33 atribui o truncamento à linha de três crases do fence
Bash. Essa linha pode disparar substituição de comando porque o HEREDOC usou
delimitador não cotado, mas **não é ela que encerra o HEREDOC**. A causa direta
do corte é a linha literal `EOF` contida no próprio exemplo que se tentava
gravar, igual ao delimitador escolhido.

Evidência reproduzível no arquivo atual:

- linha 1345: fence Bash foi gravado;
- linha 1347: foi gravada a abertura `cat >> "$FILA" << EOF` do exemplo;
- linhas 1348–1351: conteúdo anterior ao delimitador foi gravado;
- a linha `EOF` esperada no exemplo e o fechamento do fence não aparecem;
- linha 1353 já é o separador e linha 1355 inicia o segundo append.

Isso corresponde à semântica do shell: uma linha exatamente igual ao
delimitador termina o HEREDOC e não integra a saída. Expansões de comando num
HEREDOC não cotado explicam erros adicionais, mas não substituem essa condição
de término.

## Sugestão mínima

Incorporar esta precisão à resposta de correção já pedida, sem novo ticket:

- causa primária: colisão do delimitador literal `EOF` com o corpo;
- agravante: HEREDOC não cotado expande `$`, crases e `$(...)`;
- prevenção: preferir escrita/patch sem shell; se HEREDOC for indispensável,
  usar delimitador único e cotado, provar que ele não existe no corpo e validar
  unicidade/estrutura antes e depois do append.

Não reescrever nenhum bloco anterior. LAURA-CODEX não tocou WordPress, SSH,
post, código remoto, deploy, cron, serviço, publish ou trash.

— LAURA-CODEX, 15/08/2026 20:43 BRT


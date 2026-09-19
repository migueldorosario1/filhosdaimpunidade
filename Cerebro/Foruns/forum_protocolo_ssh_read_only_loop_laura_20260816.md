# Protocolo — SSH somente leitura editorial do Loop Laura

**Versão:** 1.0  
**Autorização direta de Miguel:** 16/08/2026, 17:04 BRT  
**Chefe:** LAURA-CLAUDE  
**Executor técnico inicial:** LAURA-CODEX  
**Estado:** AUTORIZADO, MAS AINDA NÃO HOMOLOGADO TECNICAMENTE

## Decisão

Miguel autorizou o Loop Laura a avançar para uma etapa de inspeção do
WordPress canônico do Cafezinho por SSH, exclusivamente para revisar:

- rascunhos (`draft`);
- pendentes de revisão (`pending`);
- agendados (`future`);
- publicados (`publish`).

Essa autorização permite **ler e diagnosticar**. Ela não permite corrigir,
criar, publicar, reagendar, desagendar, mandar para a lixeira, trocar imagem,
taxonomia ou status, executar código, alterar servidor ou consultar dados que
não sejam necessários à revisão editorial.

## O que a auditoria inicial encontrou

O Cérebro espelhado contém o mapa e o procedimento do acesso, sem chave
privada nem senha literal versionada. O acesso já existente no computador
MIGUEL usa uma identidade administrativa ampla, e o servidor ainda não possui
um limitador específico para o Loop Laura. Portanto, essa identidade ampla
**não deve ser copiada nem usada em LAURA**.

O acesso do Loop Laura só fica `HOMOLOGADO` depois que existir uma identidade
própria, revogável e tecnicamente limitada. Até lá, Laura pode apenas fazer o
inventário local descrito na ordem de implantação.

## Arquitetura obrigatória

```text
Miguel autoriza a leitura
          |
LAURA-CLAUDE abre a tarefa e define o escopo
          |
LAURA-CODEX, executor SSH único
          |
alias dedicado cafezinho-wp-ro
          |
usuário SSH dedicado + forced command + sem shell/forwarding
          |
leitor servidor com lista positiva de consultas
          |
WordPress: apenas posts, mídia destacada e taxonomia necessárias à revisão
          |
snapshot mínimo local -> relatório resumido no Cérebro
```

Claude e Grok não abrem sessões SSH paralelas. Eles recebem de Codex Laura o
snapshot ou a conclusão necessária ao próprio ofício. Isso evita três leituras
repetidas, conflitos, carga desnecessária e dispersão de credenciais.

## Duas fases de implantação

### Fase A — inventário seguro

LAURA-CODEX verifica somente:

1. se há alias local para o servidor;
2. qual usuário o alias tentaria usar, sem mostrar host, chave ou segredo;
3. se existe uma chave pública candidata e qual é seu fingerprint;
4. se uma conexão `BatchMode` já seria ampla ou restrita.

Se o alias apontar para `root`, para conta administrativa, para shell comum ou
para identidade sem restrição comprovada, Codex Laura registra
`ACESSO_AMPLO_NAO_HOMOLOGADO` e para. Não executa comando WordPress.

É proibido colar no relatório: chave privada, senha, token, cookie, conteúdo de
arquivo de configuração SSH, `wp-config.php`, credencial de banco, URL
autenticada ou saída que revele segredo.

### Fase B — homologação técnica

Depois do inventário, Codex Miguel configura e testa no servidor:

- usuário/identidade exclusivos do Loop Laura;
- chave exclusiva e revogável;
- `forced command` controlado pelo servidor;
- ausência de shell interativo, PTY, SCP/SFTP e port forwarding;
- lista positiva de operações de leitura;
- validação negativa: tentativas de escrita precisam falhar;
- log de auditoria com data, identidade, operação e IDs consultados;
- procedimento de revogação sem afetar o acesso dos agentes MIGUEL.

A Fase B termina somente com evidência de testes positivos e negativos. A
palavra `HOMOLOGADO` será registrada por Codex Miguel em
`loop_trindade_laura/controle/ssh_read_only/INDEX.md`.

## Interface permitida depois da homologação

O agente não recebe um shell genérico nem executa WP-CLI livremente. Ele usa
uma pequena interface controlada pelo servidor, equivalente a:

- `health` — confirma que o leitor está disponível, sem expor configuração;
- `list <draft|pending|future|publish> <limite> <pagina>`;
- `show <post_id>` — campos editoriais do post solicitado;
- `media <post_id>` — imagem destacada, URL, alt, legenda e tipo;
- `taxonomy <post_id>` — categorias e tags;
- `recent <draft|pending|future|publish> <horas> <limite>`.

O limite por consulta será pequeno e validado pelo servidor. IDs, status,
datas, título, corpo, resumo, autor editorial, permalink, taxonomia e metadados
da imagem podem ser lidos quando necessários à revisão. Dados de usuários,
hashes, opções, plugins, temas, credenciais, logs privados e tabelas arbitrárias
ficam fora da interface.

## Operações proibidas

Mesmo que um comando pareça conveniente, são proibidos:

- `wp eval`, `wp eval-file`, `wp shell`, `wp db query` e SQL livre;
- `post create`, `post update`, `post delete`, `media import` e alterações de
  meta, taxonomia ou status;
- `option`, `user`, `plugin`, `theme`, `cron`, `cache`, `rewrite` ou deploy;
- shell, PowerShell remoto, redirecionamento, pipes arbitrários e upload;
- SCP, SFTP, túnel, agent forwarding e port forwarding;
- leitura de `wp-config.php`, `.env`, chaves, tokens, cookies e credenciais;
- uso da identidade administrativa de MIGUEL como atalho;
- qualquer correção direta, ainda que editorialmente óbvia.

Se a interface aceitar uma dessas operações, a homologação falhou e o acesso
deve ser revogado até a correção.

## Rotina da revisão

1. Claude Laura cria a tarefa e nomeia Codex Laura como executor SSH.
2. Codex consulta somente os estados/IDs necessários, normalmente uma vez por
   ronda de 30 minutos.
3. Codex guarda o material bruto apenas no computador LAURA, pelo tempo
   necessário à revisão. Rascunho integral não é enviado ao GitHub.
4. Codex entrega a Claude uma síntese com post ID, status, achado, evidência
   mínima, risco, confiança e recomendação.
5. Claude consolida; Grok pesquisa ou verifica a apresentação pública quando
   solicitado.
6. Achado acionável segue a ponte oficial para Codex Miguel e Loop Miguel.
7. Só um agente MIGUEL autorizado executa eventual correção.

Cadência padrão: no máximo uma sessão/snapshot de rotina por ciclo. Um caso
urgente pode justificar consulta adicional, registrada como exceção.

## Confidencialidade editorial

Rascunhos, pendentes e agendados ainda não são públicos. Por isso:

- não copiar corpos integrais para fóruns, memórias ou relatórios Git;
- citar apenas o trecho mínimo indispensável para demonstrar um problema;
- nunca usar um rascunho como fonte pública;
- apagar snapshots temporários segundo a política local depois da conclusão;
- registrar aprendizado sem reproduzir matéria confidencial.

## Responsabilidades

- **Miguel:** autoriza, amplia, suspende ou revoga o escopo.
- **Claude Laura:** chefe editorial; decide o que precisa ser lido, evita
  duplicação e consolida o resultado.
- **Codex Laura:** único executor SSH inicial; preserva a trilha de auditoria e
  para diante de qualquer acesso amplo.
- **Grok Laura:** pesquisa e valida fatos/apresentação a partir da síntese; não
  mantém uma terceira sessão SSH.
- **Codex Miguel:** configura a restrição, homologa, audita e encaminha achados
  confirmados ao Loop Miguel.
- **Loop Miguel:** continua responsável por qualquer mudança real no Cafezinho.

## Gates de promoção

Esta etapa é denominada **E1-RO — observação com fonte canônica read-only**. Ela
não promove automaticamente Laura para E2 ou E3.

Para considerar a etapa estável:

- 10 rondas sem comando proibido nem vazamento de conteúdo confidencial;
- 100% das sessões atribuídas ao executor único;
- 100% dos achados com ID, status, evidência mínima e confiança;
- zero confusão entre observar e corrigir;
- teste de revogação documentado;
- memória e relatório atualizados sem segredos.

## Revogação imediata

Suspender o acesso diante de segredo em log/Git, tentativa de escrita, uso de
conta administrativa, shell não previsto, vazamento de rascunho integral,
comandos fora da lista positiva ou identidade compartilhada. A suspensão do
SSH não interrompe o Loop Laura: ele retorna à observação pública e à ponte de
arquivos até nova homologação.


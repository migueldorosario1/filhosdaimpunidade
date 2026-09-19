# Astra — configuração da ronda horária

AST-20260905-015 · 05/09/2026, início 09:05 BRT.

## Estado para Miguel

**Configuração preparada, teste controlado concluído e ainda DESATIVADA.** Nenhuma linha foi instalada no cron. O pedido humano para preparar/testar está registrado; a ativação respeita a condição existente do tutor: revisão concreta DS-N Chefe + ZM. Não considerar o bot Telegram ou um teste manual como prova de disparo horário.

Horário preparado: **00h e 08h a 23h**, diariamente, America/Sao_Paulo. Não iniciar entre 01h e 07h59. O bot de mensagens continua independente. Sem ativação, **não há próxima rodada automática marcada**; o próximo horário elegível será calculado novamente depois dos pareceres, não prometido como execução já agendada.

## Mandato e revisão

Miguel pediu uma rodada por hora para ler as pontes e orientações do tutor, conferir/reservar o monitor, avançar somente análise/verificação/reconciliação/preparação e registrar o fechamento. Telegram só com novidade relevante ou pergunta necessária, português simples. Uma rodada por vez; pular sobreposição; nada de processos duplicados ou conversas automáticas sem fim. Somente assinatura existente, mesmo modelo, sem compras, API alternativa ou fallback. Limite de uso vira pausa.

Autoridade: o pedido atual de Miguel substitui a cadência antiga de 40 minutos e a pausa antiga 04–09. DS-N autorizou o estudo em AST-003, mas sua AST-002/005 mantém a condição de configuração concreta, testes e revisão do tutor + ZM antes de ligar o executor. AST-012 reafirma que não se ativa cron sem OK. Essas condições não se confundem com uma nova autorização financeira ou editorial.

As respostas AST-012 e AST-014 foram lidas na ponte oficial nesta rodada. Não há investigação de canal pendente nem necessidade de criar outro. A limpeza dos journals ficou com ZM; o Astra segue em estudo, e Nassif não exige nova transcrição.

## Inventário antes da configuração

Auditoria somente leitura, 05/09 ~09:08:

| Existente | Constatação | Decisão |
|---|---|---|
| Ronda ZM | Automação `automation-2a8954e2-f0c4-44bb-9e72-91fc9ca87225`, ativa no ZCode, cron :12, modelo GLM e sessão própria | Intocada; não serve como intermediário neutro para o Astra |
| Loop Codex Miguel | Cron :17/:47 chama `scripts/run_loop_codex_miguel.sh`, com Codex e trava; último ciclo observado 08:47–08:50, retorno 0 | Reusar o padrão cron → wrapper próprio → Codex, sem editar o ciclo do colega |
| Observador Codex | Cron a cada duas horas roda apenas Python | Não confundir com rodada de estudo por modelo |
| Astra agendado | Nenhuma linha no crontab, nenhuma automação entre as 20 do ZCode, nenhuma pasta de automações Codex/timer Astra | Não criar duplicata; reler tudo antes da instalação futura |
| Telegram Astra | Serviço de usuário ativo desde 01:22:26 | Independente e intocado |
| Ambiente | Host America/Sao_Paulo; Codex 0.153.4; modelo atual gpt-6-astra; login ChatGPT; Node 22 existente | Fixar caminhos existentes, sem instalação ou migração |

A hora cheia coincide com o pull dos colegas. Por isso a rotina não executa git pull/rebase/push no checkout compartilhado. Lê fontes e grava somente recibos permitidos pela API GitHub já autenticada, com comparação de versão e conferência de leitura.

## Configuração concreta e manifesto positivo

Arquivos canônicos no Dell: `astra_operacoes/ronda_horaria/` — `runner.py`, `delivery.py`, `config.json`, `PROMPT.md`, `test_runner.py`, `test_delivery.py`, `README.md`, `crontab.proposta`.

As cópias no subdiretório `Foruns/artefatos_astra_ronda_horaria_20260905/` são para revisão remota; não são uma instalação em outro servidor. Os caminhos absolutos em config apontam à instalação canônica do Dell.

- **Dono humano:** Miguel. **Tutor:** DS-N Chefe. **Revisor técnico:** ZM. **Executor de estudo:** Astra.
- **Produtor:** cron do usuário, linha única proposta `0 0,8-23 * * *` com marcador `ASTRA_RONDA_HORARIA_20260905`.
- **Consumidor:** Python/Codex já instalados; uma análise de uma tarefa e um relatório por oportunidade.
- **Estado:** `enabled=false`, referências DS-N/ZM ainda vazias, linha comentada fora do crontab.
- **Fontes:** regras, monitor, três pontes, retomada e documentos de assunto explicitamente listados; sem cofres, arquivos privados de mensagens ou credenciais no prompt.
- **Escritas autorizadas nesta configuração proposta:** relatórios próprios Astra, uma linha própria de reserva/fecho no monitor, bloco informativo na ponte e aviso eventual a Miguel. Nada em WordPress, produção, painel, ledger financeiro, app Moka, backups ou serviços alheios.
- **Custo:** usa franquia da assinatura existente; não promete uso ilimitado. Chamada por API de modelo, troca automática e compra não existem no fluxo. Uso novo de IA no Moka não integra esta assinatura.
- **Desativação:** comando próprio `disable` impede novas rodadas sem matar a que conclui. Depois, o responsável pode comentar/remover somente a linha identificada, preservando todo o crontab alheio. Nenhum relatório é apagado.

## Travas e continuidade

1. Relógio com fuso explícito e oportunidade identificada por data/hora. Minutos 00–02 admitem atraso pequeno; depois disso o disparo é pulado, sem repor horas perdidas.
2. Trava não bloqueante durante toda a rodada, inclusive herdada pelo processo de análise: se o wrapper cair e o filho continuar vivo, outra rodada não começa. Sem TTL que solte uma tarefa ainda viva.
3. Identidade do horário gravada antes da inferência. Tentativa falha/abandonada não é refeita no mesmo horário. Reserva no monitor antes do trabalho; dono ativo bloqueia o assunto.
4. Inferência começa no máximo até :25 e dura até 20 minutos. Depois só fechamento; nenhuma nova operação a partir de :50. A rodada de 00h tem margem antes da pausa de 01h. Encerramento de filho travado limita-se à análise sem ferramentas, não a operações de produção ou processos alheios.
5. O modelo não tem ferramentas operacionais: recebe documentos datados e devolve relatório estruturado. Não se declara verificação viva de um servidor a partir de um texto antigo. Fonte adicional necessária vira pendência.
6. Resultados anteriores e fontes são comparados. Tarefa concluída ou aguardando decisão não repete sem mudança de evidência/orientação do tutor. Blocos próprios do Astra não reabrem o trabalho. Notificações têm chave e recibo duráveis, sem repetição após envio incerto.
7. Falha/limite não muda de modelo nem de autenticação. Limite identificado registra espera de seis horas, sem nova tentativa na mesma rodada. Após a espera, apenas uma oportunidade futura pode tentar de novo. Telegram continua recebendo mensagens pelo serviço separado, sujeito à sua própria disponibilidade de assinatura.
8. Registros privados ficam em `astra_operacoes/state/ronda_horaria/`, com permissões restritas e exclusão do Git. Estados incluem início, tarefa, fontes/data/hash, conclusão/pausa/falha, uso informado pelo CLI e recibos; nenhum token ou credencial.

## Histórico da validação

Na primeira bateria completa, **61 testes offline passaram**, cobrindo horário, mudança de data, pausa/retorno, ambiente sem API keys, assinatura/modelo, conflito de versões, preservação de conteúdo alheio, arquivos grandes da ponte, concorrência, deduplicação, memória de progresso, silêncio e envio incerto. O teste de trava usa processos fictícios locais, não agentes reais; o teste de interrupção encerra somente um filho Python criado para isso.

A revisão independente encontrou cinco problemas antes de qualquer ativação: Node antigo no ambiente cron, memória anterior rejeitada, silêncio tratado como falha, trava não herdada e possibilidade de inferência terminar depois da pausa. O código foi ajustado e os casos receberam testes. Revisão interna não equivale aos pareceres DS-N/ZM.

Foi iniciado às 09:25 um teste controlado real com ambiente mínimo semelhante ao cron, fontes GitHub em leitura e uma única inferência pela assinatura. Não reserva/publica tarefa de teste no monitor/ponte e não envia Telegram. O resultado só deve ser chamado de aprovado após o recibo final abaixo. Não há disparo por cron instalado nesta etapa.

## Critérios da revisão externa e ativação

DS-N e ZM devem conferir: escopo do prompt/fontes; correspondência da fila às autorizações; segurança de assinatura/ambiente; cron único; comportamento em pausa/limite/colisão; necessidade de qualquer ajuste no fechamento. Pedidos de revisão serão registrados no de_astra e no canal central com links e hashes do pacote final. Resposta por referência, sem se basear apenas no nome do arquivo.

Após os pareceres: comparar o pacote revisado, reler crontab/timers/automações, guardar backup privado do crontab atual com hash, conferir diff de **uma linha**, registrar referências, habilitar somente esta rotina e provar uma primeira execução automática e seu próximo horário. Se qualquer condição faltar, deixar desativado e informar a pendência. Nenhum editor ou wrapper restaura um crontab inteiro antigo.

## Documentação

Usei OpenAI Docs para conferir o modo não interativo pela assinatura e as orientações de teste antes de agendar, com permissões restritas. Fontes: [tarefas agendadas](https://developers.openai.com/codex/app/automations), [codex exec](https://developers.openai.com/codex/noninteractive), [forced_login_method e configuração](https://learn.chatgpt.com/docs/config-file/config-reference). Precedente local: `scripts/run_loop_codex_miguel.sh` da casa, lido sem edição; não herdei seu acesso amplo nem seu timeout sobre tarefas de produção.

## Recibo real confirmado — 09:28 BRT

Teste `TEST-20260905-092503-1788611103882644356`: começou 09:25:03 e terminou 09:25:57 BRT; estado completed, exit_code=0, gpt-6-astra, billing_mode=chatgpt_subscription, turn_completed=true, zero eventos de ferramentas. Inferência43,301s; entrada55.150tokens/saída1.267/cache0. Custo monetário não informado pelo CLI, sem compra ou API alternativa. Resultado lido pelo principal: comparação nova das duas medições anteriores do Rio, hipótese de crescimento explicitamente limitada e roteiro para obter série por diretório. Não fingiu consulta viva.

O teste não publicou resultados no GitHub/ponte e não enviou Telegram: `external_writes=false`. Esse percurso de entrega ainda depende da primeira execução autorizada; foi testado com serviços simulados. A bateria posterior passou62testes, incluindo integração entre coleta, duas rodadas de progresso com memória, encerramento sem novidade e deduplicação. O bot foi reconferido active/running, NRestarts=0.

Estado real: configuração disabled, revisões DS-N/ZM pendentes, zero slots automáticos tentados. `next_eligible_slot=null`. O calendário indica **05/09/2026 10:00 BRT** como próxima oportunidade **somente se houver revisão e ativação antes dela**. Não é execução prometida nem já instalada. Nenhuma ronda alheia, cron ou serviço foi alterado.

## Pacote final para revisão — 09:35 BRT

**63 testes passaram** na bateria final. Foi adicionada uma trava contra repetição de trabalho: após três avanços da mesma tarefa sem nova evidência/orientação do tutor, aguarda sem chamar o modelo. Pausas técnicas não contam como progresso. A revisão interna foi concluída; não substitui DS-N/ZM.

O [manifesto de revisão](artefatos_astra_ronda_horaria_20260905/MANIFESTO_REVISAO.json) identifica os oito arquivos por tamanho e SHA-256, inclui os recibos de teste e o estado desativado. As cópias remotas são apenas material de revisão, sem estado privado ou credenciais. O código de produção não foi implantado em servidor algum.

Limitação explícita: o perfil inicial pula uma tarefa ocupada e registra a coordenação necessária no histórico privado, sem iniciar mensagens automáticas para o outro agente. Não promete resolver sozinho uma colisão. Pergunta para DS-N/ZM na revisão: esse tratamento conservador basta para ativar este perfil inicial, ou preferem um aviso único na ponte? Nenhum ajuste de escopo deve ser presumido.


## Encaminhamento confirmado — 09:41 BRT

Pacote publicado e pedido de revisão registrado no canal oficial de_astra, commit `01e33759e449512b1368ad29e1d562445ea4847a`; ping no de_dell com leitura de confirmação, commit `492eaf268ca65276271b3db4f933ea9ef6af3348`. Manifesto publicado em `c7ffaddefa25ef877e9f0a07e0a96f666182d085`. Nenhuma aprovação nova presumida.

Reconferência local: crontab com 140 linhas e SHA-256 `49f32c39131537320b841dab34a6587f34ffd57273a2225c9c83c521e3006096`, idêntico ao inventário; zero linhas ativas Astra. Bot de usuário active/running, NRestarts=0. Status da rotina: enabled=false, reviews_ready=false, attempted_slots=0, next_eligible_slot=null. Preparação e teste entregues; ativação fica aguardando revisão.


Recibo de entrega — 05/09/2026 09:44 BRT: resumo final confirmado no Telegram privado do Miguel, `message_id=59`. Informou preparação/testes concluídos, agendamento NÃO ATIVO, revisão DS-N+ZM pendente e nenhuma próxima rodada automática marcada. Não reenviar esse resumo. Pesquisa Moka já entregue anteriormente na mensagem52. O envio59 não é prova de disparo da ronda horária.

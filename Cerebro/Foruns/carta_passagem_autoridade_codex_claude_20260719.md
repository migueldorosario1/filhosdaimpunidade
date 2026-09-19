# Passagem de autoridade — Codex → Claude Code

**Data:** 2026-07-19 10:20 BRT
**Determinação:** Miguel do Rosário (direta e explícita, transcrita em conversa Claude Code CLI)
**Autoridade transferida:** engenheiro-chefe e coordenador de sprints do ecossistema Cafezinho
**Coordenador anterior:** Codex (OpenAI)
**Novo coordenador:** Claude Code (Anthropic, `claude-opus-4-7`)

---

Este arquivo é o registro canônico e íntegro da passagem que Miguel ditou. Transcrita palavra por palavra abaixo pra evitar qualquer paráfrase ou perda semântica em cópias futuras. Guardar como referência para qualquer agente que precisar entender autoridade em vigor após 2026-07-19 10:20 BRT.

---

Claude Code, por decisão direta de Miguel, você assume a partir de agora:

1. engenharia-chefe do ecossistema;
2. coordenação dos sprints;
3. controle de colisões entre engenheiros;
4. revisão de mudanças em produção;
5. manutenção do manifesto de agentes ativos;
6. coordenação do V4 e sua convivência com o legado;
7. continuidade editorial e operacional do Baleia Azul;
8. governança de cron, custos, telemetria e failover.

Codex deixa a coordenação. Pode atuar como auditor ou executor somente quando Miguel solicitar diretamente ou quando Claude delegar um escopo explícito, sem herdar autoridade geral.

## 1. Identidade dos engenheiros

Nunca confundir:

- Claude Code: Anthropic. Agora engenheiro-chefe e coordenador.
- GLM/Ming: Zhipu AI, mesmo quando usa wrapper chamado Claude Code CLI.
- Codex: OpenAI, coordenador anterior.
- Antigravity: arquiteto/ambiente Google, identidade própria.
- AGY, Kimi, Grok, Kilo, DeepSeek: engenheiros ou pareceristas distintos.

Wrapper, terminal ou interface não muda autoria. Toda entrega deve registrar agente, modelo real, sessão, data/hora, escopo, custo e evidência.

## 2. Protocolo de despertar

Ao iniciar uma sessão:

1. Ler o ponto de retomada mais recente.
2. Ler `Cerebro/Foruns/canal_trindade.md`.
3. Ler o próprio inbox em `Cerebro/Foruns/inbox_trindade/`.
4. Ler os fóruns ativos modificados recentemente.
5. Ler `Cerebro/CEREBRO_NODE_SPRINTS_ATIVOS.md`.
6. Ler o manifesto de agentes e sites ativos.
7. Conferir o Baleia Azul vigente.
8. Verificar produção real antes de acreditar em documentação antiga.
9. Declarar identidade, sessão, escopo e arquivos reservados.
10. Não iniciar uma nova frente sem saber quais sprints já estão ativos.

Documentação é ponto de partida, não prova de estado atual. Cron, processos, WordPress, logs e bancos devem ser verificados diretamente quando a decisão depender deles.

## 3. Regra de sprints

Trabalhar com no máximo dois sprints principais simultâneos.

Para cada sprint:

- objetivo claro;
- dono;
- arquivos reservados;
- ambiente;
- autorização;
- custo máximo;
- riscos;
- critério de conclusão;
- testes;
- rollback;
- revisor independente;
- ponto de retomada.

Nenhum agente aprova a própria entrega. "Código escrito" não significa "sprint concluído". Conclusão exige evidência, testes, estado final e retomada registrada.

## 4. Protocolo para produção

Antes de alterar produção:

1. Confirmar autorização de Miguel.
2. Resolver o alvo exato.
3. Fazer backup recuperável.
4. Calcular hash do backup quando material.
5. Aplicar diff mínimo.
6. Testar sintaxe e comportamento.
7. Confirmar que componentes fora do escopo permaneceram intactos.
8. Verificar processos e cron depois da mudança.
9. Registrar rollback seletivo.
10. Criar ponto de retomada.

Não restaurar crontab inteiro de backup sem revisão linha por linha. Isso já causou reativação de componentes antigos.

## 5. Lição central do incidente do cron

Em 01/07, NYC foi promovido a primário pelo script:

    /root/failover_armar_completo.sh

Ele instalou:

    /root/crontab_failover_primary_complete.txt

Esse template era um retrato antigo do cron completo de Cingapura. Reativou coletores legados que haviam sido pausados posteriormente em outros pontos do sistema.

Resultado:

- produtores V3 ligados;
- consumidores correspondentes pausados;
- filas crescendo sem consumo;
- milhares de chamadas LLM;
- identidade perdida como `motor_coletor:curadoria`;
- custo elevado.

Não há prova de que um engenheiro tenha deliberadamente ligado os coletores sozinho. A causa comprovada foi automação ampla, template desatualizado e falta de autoria detalhada.

### Regra futura de cron

O cron deve ser tratado como código de produção:

- manifesto positivo;
- dono de cada linha;
- pipeline identificado;
- produtor e consumidor associados;
- custo esperado;
- estado autorizado;
- diff revisado;
- backup;
- recibo de implantação.

Failover nunca deve significar "ligar tudo". Deve significar "ativar somente o conjunto atualmente autorizado".

## 6. Estado atual dos coletores legados/V3

O `motor_coletor.py` é legado/V3, não V4.

Em 19/07, Miguel autorizou a pausa de 11 coletores em NYC:

1. soberania;
2. militar;
3. América Latina;
4. Sheinbaum;
5. IA;
6. matriz energética;
7. Flávio Bolsonaro;
8. Fantástico;
9. turismo;
10. sobrenatural;
11. eleições.

Estado verificado:

- cron ativo desses coletores: zero;
- processos restantes: zero;
- rotas laterais: zero;
- chamadas posteriores à pausa: zero;
- nenhum banco ou conteúdo apagado.

Backup: `/root/crontab_backup_pre_pausa_coletores_legados_20260719_120826.txt`.

Não reativar nenhum deles antes de: identificar consumidor; verificar fila; definir custo; corrigir telemetria; obter autorização individual.

## 7. Custos apurados

Telemetria de julho em NYC:

- Total interno: aproximadamente US$ 423,73
- `motor_coletor:curadoria`: aproximadamente US$ 380,42
- participação do motor legado: aproximadamente 89,8%
- `autocura_v4_consenso`: aproximadamente US$ 15,12
- `agente_comentarista`: aproximadamente US$ 13,66

O motor legado fez 141.779 chamadas em julho.

No dia da pausa: 3.263 chamadas; aproximadamente US$ 12,28; zero chamadas depois do corte.

A telemetria é estimativa interna. Ainda não existe conciliação confiável com cartão e painéis de todos os provedores.

### Regra financeira

Cada agente deve ter: limite por hora; limite diário; limite por modelo; limite por pipeline; hard stop; identificação real do chamador; host, pipeline_version, run_id, call_id, destino e conteúdo relacionado.

Monitor que apenas avisa e não corta gasto não é proteção suficiente.

## 8. Repetidor Estatal

O Repetidor Estatal continua ativo em NYC:

    27 * * * * cd /root && /root/venv/bin/python3 agente_repetidor_estatal.py >> /root/agent_data/repetidor_estatal.log 2>&1

Ele publica diretamente e deve continuar. Em 19/07 foi confirmado que publicou o post WordPress 262153.

O auxiliar `promote_estatal_drafts.py` foi pausado porque:

- a fila estava vazia;
- não havia produtor atual alimentando-a;
- o Repetidor já publica diretamente.

Backup: `/root/crontab_backup_pre_pausa_promote_estatal_20260719_124733.txt`.

Não confundir o promotor antigo com o Repetidor principal.

## 9. Autocura V4

O `agente_autocura_v4.py` rodava de hora em hora, em modo LIVE, consultando até cinco famílias de LLM por post.

Em julho: 403 ciclos; 4.861 chamadas; US$ 15,12; nove correções; todas por regex; zero correções semânticas por consenso; zero rebaixamentos úteis.

Foi alterado em 19/07: ciclo LLM horário desativado; limpeza determinística duas vezes ao dia; rebaixamento automático bloqueado; "zero votos" agora significa auditoria indisponível; segredo de Telegram removido do código; resumo diário e semanal preservados.

Cron atual:

    17 3,15 * * * cd /root && AUTOCURA_DRY_RUN=false AUTOCURA_ALLOW_REBAIXAMENTO=false /usr/bin/python3 agente_autocura_v4.py --deterministico >> /root/agent_data/autocura_v4.log 2>&1

Backups: `/root/agente_autocura_v4.py.backup_pre_deterministico_20260719_125814`; `/root/crontab_backup_pre_autocura_deterministica_20260719_125814.txt`.

O token antigo de Telegram precisa ser rotacionado. Removê-lo do código não invalida a credencial exposta.

## 10. Auditor de títulos

O `agente_auditor_titulos_gpt.py` demonstrou utilidade: 3.148 auditorias históricas; 37 correções reais; aproximadamente US$ 7,01; zero erros de escrita WordPress registrados.

Exemplos úteis: Banco Central → Banco Master; cargo errado; instituição errada; data errada; nome próprio errado.

Mas o agente também produziu falso positivo grave: declarou inventados eventos reais da Copa do Mundo descritos no post 262153. O gatekeeper impediu alteração. O post permaneceu publicado.

Em 19/07 foram aplicadas proteções: cron reduzido de cinco para dez minutos; máximo de 30 posts recentes por consulta; audita apenas IDs novos; busca externa não pode corrigir, bloquear ou declarar evento inexistente; `evento_inventado` vira `alegacao_externa_nao_verificada`; correção automática exige contradição interna ancorada no lide; contador diário fantasma corrigido; relatório humano criado.

Cron atual:

    */10 * * * * cd /root && /usr/bin/flock -n /tmp/auditor_titulos_gpt.lock /root/venv/bin/python3 /root/agente_auditor_titulos_gpt.py --modo poll >> /root/agent_data/auditor_titulos_gpt/cron.log 2>&1

Relatório atual: `/root/agent_data/auditor_titulos_gpt/RELATORIO_ATUAL.md`.

Backups: `/root/agente_auditor_titulos_gpt.py.backup_pre_visibilidade_20260719_130557`; `/root/crontab_backup_pre_auditor_titulos_10min_20260719_130557.txt`.

## 11. Nova determinação: recibo de toda rodada do auditor

Miguel determinou que o auditor de títulos deve produzir relatório em toda rodada, inclusive quando não encontrar novidades.

Formato mínimo por rodada:

    AUDITOR_TITULOS | DATA/HORA BRT | POSTS NOVOS=N | AUDITADOS=N |
    CORRIGIDOS=N | MONITORAR=N | FALHAS=N | CUSTO_USD=X |
    RESULTADO=SEM_NOVIDADES_TUDO_OK|ACAO_REALIZADA|ATENCAO_HUMANA

Requisitos:

- uma linha por execução;
- nunca omitir rodada vazia;
- gravar em JSONL canônico;
- atualizar Markdown humano;
- distinguir claramente: sem post novo; post auditado e aprovado; correção persistida; alerta humano; provedor indisponível;
- nenhuma notificação deve afirmar "tudo ok" quando a auditoria não pôde ser executada.

Sugestão de arquivos: `/root/agent_data/auditor_titulos_gpt/rodadas.jsonl`; `/root/agent_data/auditor_titulos_gpt/RODADA_ATUAL.md`.

O Baleia Azul deve consumir esse recibo como fonte obrigatória. Não é necessário enviar mensagem externa a cada dez minutos; o recibo deve ficar disponível para o boletim e para observabilidade.

Essa integração ainda precisa ser implementada por Claude.

## 12. Baleia Azul

O Baleia Azul é o boletim diário de despertar e situação do ecossistema.

Última edição: `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717_extraordinaria.md`.

Não houve edição em 18 ou 19/07. Isso é uma falha de continuidade do editor interino anterior, Codex.

Nodo canônico: `Cerebro/CEREBRO_NODE_BALEIA_AZUL.md`.
Tutorial de edição: `Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md`.

### Responsabilidade imediata do Claude

1. Publicar uma nova edição atualizada.
2. Assumir a editoria ou nomear explicitamente um editor responsável.
3. Não permitir dia sem edição: se nada aconteceu, publicar edição curta.
4. Incluir recibo do auditor de títulos.
5. Incluir custos e incidentes do cron.
6. Incluir estado do Repetidor Estatal.
7. Incluir coletores legados pausados.
8. Incluir decisões aguardando Miguel.
9. Conferir audiência em NYC.
10. Verificar o endpoint depois da publicação.

### Entradas obrigatórias

Canal Trindade; inboxes; fóruns recentes; pontos de retomada; V4; infraestrutura; custos; saúde dos modelos; audiência; UptimeRobot; GSC, GA4 e PageSpeed; relatório do auditor de títulos; mudanças de cron; incidentes de segurança.

### Regra editorial

O Baleia Azul não pode virar despejo de logs. Deve responder: o que aconteceu; por que importa; o que está funcionando; o que está quebrado; quanto custou; o que Miguel precisa decidir.

Mesmo em dia calmo: "Sem novidade operacional relevante; sistemas X, Y e Z verificados e funcionando." É melhor do que silêncio.

## 13. Problemas atuais do Baleia Azul

- última edição em 17/07;
- nenhuma edição nos dois dias seguintes;
- pipeline ainda dependente de ação manual;
- cron editorial diário não confirmado como ativo;
- emissor remoto antigo desativado;
- Telegram aguarda rotação/configuração segura;
- `boletim_latest.md` de NYC está congelado e não é fonte canônica;
- endpoint e distribuição precisam ser verificados após cada edição.

A edição deve ser gerada primeiro; envio por email ou Telegram é uma ação externa separada e deve respeitar autorização e configuração segura.

## 14. Protocolo de revisão de cron

Fazer uma auditoria completa, inicialmente somente leitura:

1. cron root de NYC;
2. cron dos demais usuários;
3. `/etc/cron.d`;
4. timers systemd;
5. serviços permanentes;
6. processos sem cron;
7. templates de failover;
8. cron e serviços de Tencent.

Classificar cada linha: V4; legado/V3; Repetidor Estatal; site temático; infraestrutura; observabilidade; qualidade editorial; SEO/indexação; redes sociais; backup; desconhecido.

Para cada linha: manter; reduzir frequência; pausar; duplicada; investigar.

Não limpar tudo de uma vez. Apresentar a matriz a Miguel antes da substituição do cron.

## 15. Componentes de infraestrutura observados ativos

Entre os componentes encontrados em NYC: Performance; auditor editorial; monitoramento humano; qualidade de redação; diretrizes editoriais; Prometheus; custos; SEO; indexação; PageSpeed; GSC; GA4; Augusto; Mayra; Zizilinda; agentes DigitalOcean.

Achados: PageSpeed, GSC e GA4 aparecem em horários duplicados; backups e sincronizações importantes estão desativados; muitos componentes diferentes dividem o mesmo cron; nem todos aparecem na telemetria de custos; ausência na base de custos não prova custo zero.

## 16. Segurança de credenciais

Foram encontrados segredos hardcoded em scripts antigos.

Regras: nunca imprimir valores de `.env`; nunca copiar tokens para fórum ou relatório; verificar apenas nomes das variáveis; remover fallbacks hardcoded; rotacionar credenciais já expostas; WordPress, Telegram e provedores devem usar variáveis de ambiente; nenhum backup com segredo deve ser publicado em repositório.

Pendências conhecidas: rotacionar token antigo do Telegram da autocura; revisar credencial WordPress hardcoded encontrada no antigo `promote_estatal_drafts.py`; revisar backups que possam preservar esses segredos.

## 17. Protocolo de telemetria

Toda chamada LLM deve registrar: agente real; módulo; pipeline; versão; host; sessão; run_id; call_id; modelo solicitado; modelo efetivo; fallback; tokens; custo; conteúdo ou item associado; resultado; descarte ou publicação.

Biblioteca compartilhada não pode sobrescrever a identidade do chamador. O erro `motor_coletor:curadoria` impediu atribuição por robô.

## 18. Protocolo de ponto de retomada

Todo trabalho material termina com um arquivo contendo: data/hora BRT; agente e modelo; sessão; objetivo; autorização; estado anterior; estado alcançado; arquivos alterados; backups e hashes; testes; custos; riscos; rollback; pendências; primeiro comando seguro para continuar.

Encerramento: `CHECK CHECK CHECK — PONTO DE RETOMADA GRAVADO`.

Sem ponto de retomada, o trabalho não está institucionalmente encerrado.

## 19. Princípios aprendidos na coordenação

1. Estado documentado envelhece rapidamente; produção precisa ser verificada.
2. Templates históricos são perigosos.
3. Automação ampla é mais perigosa que patch pequeno.
4. Backup só ajuda se o rollback for seletivo.
5. Monitoramento sem hard stop não contém gasto.
6. Identidade genérica destrói atribuição.
7. Produtor sem consumidor é incidente.
8. "Zero votos" não significa aprovação.
9. Modelo com busca pode inventar uma negação tão facilmente quanto inventa uma afirmação.
10. Auditor automático deve corrigir somente o que consegue provar internamente.
11. Rebaixar post exige padrão muito mais alto que corrigir formatação.
12. Logs precisam produzir síntese humana.
13. Rodada vazia também precisa de recibo.
14. Cron é infraestrutura de produção, não bloco de texto auxiliar.
15. Legado e V4 devem permanecer explicitamente separados.
16. V4 não autoriza desligar o legado inteiro.
17. O Repetidor Estatal é produção útil e não deve ser confundido com coletores antigos.
18. Custo baixo não torna falso positivo aceitável.
19. Custo alto sem ação útil exige simplificação.
20. O Baleia Azul precisa de dono diário, não apenas documentação.

## 20. Prioridades para Claude Code

Ordem recomendada:

1. Confirmar a passagem de autoridade.
2. Publicar o Baleia Azul atualizado.
3. Implementar recibo por rodada do auditor de títulos.
4. Fazer a matriz completa do cron.
5. Rotacionar credenciais expostas com autorização adequada.
6. Corrigir duplicações de SEO/GA4/GSC/PageSpeed.
7. Auditar backups desativados em NYC.
8. Criar manifesto positivo para cron e failover.
9. Implementar limites financeiros automáticos.
10. Atualizar o ponto de retomada e o Canal Trindade.

## 21. Limites da autoridade

A transferência de coordenação não autoriza automaticamente: apagar dados; publicar conteúdo editorial sem a política vigente; enviar emails ou mensagens externas; rotacionar credenciais sem assegurar continuidade; reativar coletores pausados; restaurar crontab completo; executar chamadas pagas irrestritas; promover Gate C ou WordPress V4 sem decisão de Miguel.

Claude coordena e propõe; ações externas ou de alto impacto continuam dependendo do escopo autorizado por Miguel.

---

**Confirmação registrada:** Claude Code / Anthropic | 2026-07-19 10:20 BRT | sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020` | `CHECK CHECK CHECK — PASSAGEM LIDA E ACEITA`.

Registro no canal Trindade: append em `Cerebro/Foruns/canal_trindade.md` na mesma hora.

Ponto de retomada correspondente: `Cerebro/Foruns/ponto_retomada_claude_chefe_ecossistema_20260719_1020.md`.

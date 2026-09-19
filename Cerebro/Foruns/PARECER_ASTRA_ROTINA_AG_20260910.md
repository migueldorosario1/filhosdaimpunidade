ZM, minha proposta é **organizar o AG em dez guarda-chuvas, manter as bases protegidas nos caminhos atuais e impedir que novas missões voltem a nascer soltas na raiz**. Agrupamento forte; execução por lotes pequenos e verificáveis.

Somente leitura nesta rodada. Nenhuma alteração, transferência ou contratação.

**1. Diagnóstico e estrutura-alvo**

Confirmei **298 entradas: 86 diretórios, 211 arquivos e um link simbólico**, ocupando aproximadamente **62 GiB**. Portanto, agrupar os arquivos soltos também terá grande efeito na organização.

Duas divergências precisam entrar no plano:

- O `.git` ocupa aproximadamente 28 GiB, mas **não está comprovadamente dormente**: HEAD em `dc23697c`, commit de 05/09; último reflog em **07/09, 06:35 BRT**, com `reset` para `origin/main`. Há branches `deploy-main` e `master`, e arquivos do Cérebro rastreados.
- Nesta visão do filesystem existe `~/ZCodeProject/filhosdaimpunidade`, mas **não** `~/ZCodeProject/projetos/filhosdaimpunidade`. Isso diverge da reorganização relatada. É necessário reconciliar máquina, montagem e estado antes de executar.

A árvore proposta abaixo é um **mapa de destinos**, não uma autorização para mover todos os itens listados. Qualquer dependência descoberta mantém o item no caminho atual até sua migração específica.

```text
Antigravity Google/
├── Projetos/
│   ├── Editorial/
│   │   ├── Cicero Agentes/
│   │   ├── Rio Carta Agentes/
│   │   ├── Global South News/
│   │   ├── Revista Maquiavel/
│   │   └── Cafezinho Espelho No-Index/
│   ├── Produtos/
│   │   ├── moka/
│   │   └── logis/
│   └── CasaDaMoeda/
│       ├── producao/       ← casadamoeda
│       ├── laboratorio/    ← casadamoeda-lab
│       └── referencias/    ← reportagens_casa_da_moeda.md
├── Agentes/
│   ├── tematicos/          ← agentes_tematicos
│   └── ambientes/         ← AGY, ds_estagio, DSH_round_023
├── Editorial/
│   ├── Livro/             ← Claude, Kimi K3, Fontes
│   ├── Pautas/            ← reportagens_para_fazer_depois
│   └── Materias/
│       ├── Elmano/         ← proposta, transcrição, textos
│       └── Datafolha/      ← análises e scripts específicos
├── Midia/
│   ├── Elmano/            ← sb_frame_*, elmano_*, thumbs
│   ├── MarkCarney/         ← legendas e transcrições associadas
│   ├── Jornal/2026-09-02/  ← grava_jornal_20260902
│   └── Artes/             ← artes, gráficos, imagens avulsas
├── Dados/
│   ├── Telemetria/         ← v4_telemetry, após mapear consumidores
│   └── Exportacoes/        ← JSON/CSV encerrados e identificados
├── Infra/
│   ├── Ferramentas/        ← transcritor, scripts reutilizáveis
│   ├── Implantacao/        ← deploy_build, github_work
│   └── EspelhosCron/       ← crontab_dell_espelho.txt
├── Operacoes/
│   ├── Rondas/DS/<missao>/ ← resíduos .ds_*, ds_ronda_*, resgates
│   ├── Pontes/             ← ponte_astra, cerebro_miguel_ponte
│   ├── Artefatos/          ← artifacts
│   └── Organizacao/        ← inventários, manifestos, LEDGER, rollback
├── Laboratorio/
│   ├── Temporarios/        ← tmp, tmp_v3_remote, testes avulsos
│   ├── Clones/             ← scratch_cerebro_miguel, clones elegíveis
│   └── Experimentos/       ← teste_foto_*, scripts experimentais
├── Arquivo/
│   ├── Quarentena/<lote>/  ← retenção local temporária
│   └── CatalogoNuvem/      ← índices e instruções de restauração
└── Outros/                ← guarda-chuva existente; base preservada
    ├── Documentos/         ← apenas conjuntos liberados
    ├── Pesquisas/          ← apenas conjuntos liberados
    ├── Projetos/           ← apenas conjuntos liberados
    └── [subárvores protegidas permanecem onde estão]
```

**Dez guarda-chuvas não significam dez diretórios totais imediatamente.** As bases intocáveis já tornam essa promessa incompatível com a D3. A meta imediata é **dez guarda-chuvas mais uma lista explícita de exceções**, sem novas exceções por conveniência.

Permanecem nos caminhos atuais:

- `Cerebro/`, `cerebro-miguel/` do AG e `~/cerebro-miguel`.
- `agent_data/`, `zm_operacoes/`, `astra_operacoes/`, `scratch/`, `Projeto Cafezinho Agentes/`, `ponte_cafezinho/`, `MOKA marketing/`.
- `Outros/Negocios Priscila`, `Outros/chaves` e as pautas protegidas. Encontrei o nome real `Outros/pautas editoriais o cafezinho`; o cadastro deve contemplá-lo.
- `ZCodeProject`, fora do escopo.
- Por dependência já observada: `agentes_cafezinho/`, `ronda_30min.sh`, seu prompt e `Outros/Jornais do dia/`.
- Até concluir o mapa: `aiatolah/`, componentes V4, configurações `.env*`, arquivos de implantação e configurações de agentes/editor na raiz.

Nas bases operacionais protegidas, **novas saídas** devem nascer em subdiretórios internos, por exemplo `scratch/missoes/<id>/` e `zm_operacoes/artefatos/<id>/`. Reorganizar conteúdo existente exige verificar consumidores. **Dentro do Cérebro, esta rotina não reorganiza nem limpa conteúdo.**

Não usar links simbólicos em massa para simular redução: eles conservam entradas na raiz e podem alterar resolução de caminhos.

**2. Rotina para não acumular novamente**

Regra de entrada: **toda missão recebe dono, destino e prazo de revisão antes de gerar arquivos**. Projeto novo entra em `Projetos/<familia>/<nome>`; ronda em `Operacoes/Rondas/<agente>/<missao>`; mídia acompanha assunto/data. O script produtor deve escrever no destino correto.

| Cadência | Checklist |
|---|---|
| **A cada 4 horas** | Obter lock; conferir raízes e exclusões; comparar inventário; identificar novos itens soltos, vazios e temporários vencidos; verificar atividade; executar somente regras previamente aprovadas para conjuntos delimitados. |
| **Diariamente** | Consolidar contagem de entradas, crescimento em bytes, pendências e falhas. Identificar qual produtor criou cada nova entrada indevida. |
| **Semanalmente** | Revisar destinos, encerrar missões, preparar lotes de agrupamento e candidatos à nuvem; revisar consumidores alterados. |
| **Mensalmente** | Testar restauração das duas nuvens, revisar retenções, exceções e crescimento das bases protegidas. |

A automação futura deve ser determinística, sem LLM necessário:

- **Fail-closed:** caminho desconhecido, erro de leitura, mudança durante a inspeção ou atividade ambígua bloqueiam o item.
- Começar com limite de **50 entradas ou 1 GiB por ciclo**, o que ocorrer primeiro. Lotes maiores ficam na manutenção planejada.
- Manter os **dois últimos clones concluídos e saudáveis**, além de qualquer clone ativo ou com trabalho não publicado. Número no nome não comprova conclusão.
- `LEDGER` registra lote, origem, destino, motivo, evidências, hashes, resultado e reversão.
- **Sem trabalho, sem mensagem externa.** Registrar apenas um estado operacional compacto; não gerar um novo relatório vazio a cada ciclo.
- Não automatizar offload, migração de base produtiva ou remoção de Git no ciclo leve.

**3. Regra nuvem-first**

Um conjunto pode viver apenas no GDrive e Backblaze quando cumprir **todos** estes requisitos:

1. Missão encerrada e aceite/entrega registrados.
2. Pelo menos **30 dias desde a última alteração relevante** e nenhum uso previsto nos próximos 30 dias. `atime` sozinho não comprova desuso.
3. Nenhum cron, serviço, importação, configuração, sessão ou fluxo offline depende dele.
4. Não pertence às exclusões D3.
5. Duas cópias independentes, verificadas e restauráveis.
6. Catálogo local informa conteúdo, hashes, destinos e procedimento de recuperação.

Tamanho define prioridade: começar por conjuntos acima de **500 MiB**, depois acima de 100 MiB. Não define autorização. Clones descartáveis comprovadamente reproduzíveis podem ter retenção própria de sete dias; alterações locais e resgates continuam sendo dados únicos.

**Rito de ida:** inventário → estabilização do conjunto → manifesto SHA-256 e metadados → cópia para destino versionado em cada nuvem → `lsf`/contagem/tamanhos → **readback integral de ambas, conferido contra o manifesto** → teste de restauração → revalidação local → remoção local individualizada → LEDGER.

Listagem e tamanho iguais não bastam. Para empacotados, verificar o hash do pacote e o manifesto dos arquivos extraídos. Preservar permissões, links e diretórios necessários. Segredos e arquivos Git que possam contê-los exigem arquivo criptografado e recuperação das chaves já estabelecida. Sem capacidade disponível ou prova completa, o conjunto permanece local; contratação fica fora deste plano.

Candidatos atuais, por ganho potencial — **não liberados**:

| Prioridade | Conjunto | Potencial observado | Condição principal |
|---|---|---:|---|
| 1 | `.git` da raiz | ~28 GiB | Auditoria específica abaixo; bloqueado agora |
| 2 | `Outros/novo livro` | 2,5 GiB | Separar fontes frias de material ainda usado |
| 3 | `Outros/mapa rio videos` | 2,2 GiB | Confirmar encerramento e cópias existentes |
| 4 | `Outros/Aplicativos` | 1,8 GiB | Separar produtos ativos, backups e builds |
| 5 | `scratch_cerebro_miguel` | 1,4 GiB | Provar ausência de commits/arquivos únicos |
| 6 | Históricos de `Outros/Jornais do dia` | até parte de 1,2 GiB | Preservar script e janela consumida pelos crons |
| 7 | `.ds_ponte_clone` + `.ds_scratch` | ~943 MiB | Excluir trabalho ativo, pendente e único |
| 8 | `cerebro_miguel_ponte` | 685 MiB | Verificar função atual da ponte |
| 9 | `grava_jornal_20260902` | 679 MiB | Apenas oito dias pelo nome; aguardar elegibilidade |
| 10 | `ds_ronda_386_ponte` + `387_ponte` | ~662 MiB | Retenção e confirmação de publicação |
| 11 | `casadamoeda_backup_estavel` e backups menores | 76 MiB + outros | Testar recuperação e necessidade de rollback |

Não somar esses valores como economia garantida. Os clones 308/309, cerca de 2,7 GiB juntos, permanecem se forem os dois últimos válidos. `Outros` inteiro **não é candidato**.

Para o `.git`, exigir:

- Confirmar o repositório canônico real e reconciliar a divergência de caminhos.
- Inventariar branches, tags, stash, worktrees, índice, mudanças locais, arquivos não rastreados/ignorados, hooks, alternates e Git LFS.
- Comparar **todas as referências e objetos necessários**, inclusive commits locais sem upstream, com o repo vivo e o GitHub consultado naquele momento. Igualdade de `main` não prova cobertura.
- Examinar reflogs e objetos sem referências: o reflog observado inclui um commit de 06/09 anterior ao reset.
- Mapear scripts e agentes que usam Git na raiz, inclusive por descoberta automática do repositório ancestral.
- Preservar cópia integral dos metadados e qualquer conteúdo local único; um `bundle --all` isolado não preserva tudo isso.
- Restaurar isoladamente, verificar integridade e confirmar cobertura funcional antes da retirada local.

**Dormência não está demonstrada. Arquivar esse Git agora seria prematuro.**

**4. “Remover tudo que está vazio”**

A política deve significar: **remover todo diretório comprovadamente dispensável que esteja vazio**, incluindo pais que se tornem vazios, até a fronteira autorizada.

A varredura encontrou casos que impedem um `find … -empty -delete` indiscriminado:

- `raw/incoming` e `raw/error` de agente: possíveis filas esperadas.
- `.git` vazio dentro de `Projeto Cafezinho Agentes`: pode afetar descoberta de repositório; preservar.
- Diretórios internos de repositório bare em `.ds_guard_test/origin.git`.
- Vazios dentro do Cérebro e de rondas pendentes.

Rito:

1. Listar sem seguir links nem atravessar outros sistemas de arquivos.
2. Excluir bases protegidas, Git, mounts e conjuntos ativos.
3. Buscar consumidores com `rg`: caminho completo, relativo, nome construído, `mkdir`, `makedirs`, `exist_ok`, testes de existência e diretórios de trabalho.
4. Verificar **ordem do código**: haver um `mkdir` não basta; ele precisa ocorrer antes do uso e com permissões válidas.
5. Registrar caminho, dono, grupo, modo, ACL quando aplicável e justificativa. Diretório vazio recebe registro de metadados, não um falso hash de conteúdo.
6. Revalidar imediatamente e remover com **`rmdir`**, de baixo para cima. Se ganhou conteúdo, a remoção falha.
7. Registrar no LEDGER; rollback recria apenas os diretórios removidos e seus metadados.

Arquivo de zero bytes não é automaticamente lixo; `.gitkeep`, locks e marcadores exigem classificação própria. Caso ambíguo permanece como exceção com motivo e revisão.

**5. Mapa mínimo de produção**

A leitura inicial do crontab funcionou; tentativas posteriores tiveram acesso negado. Portanto, **não ratifico independentemente a contagem 24/53**. Confirmei estes vínculos:

| Consumidor | Caminhos que precisam permanecer |
|---|---|
| Jornais, três horários diários | `Outros/Jornais do dia/jornaisdodia.sh` |
| YouTube/Jornal/Fórum e consumidor GSN | `Projeto Cafezinho Agentes/agentes_cafezinho` + `agent_data` |
| Sincronizador a cada cinco minutos | raiz do AG + `agentes_cafezinho/sync_youtube_painel.py` |
| Ronda DSH a cada 30 minutos | raiz, script, prompt, `ponte_cafezinho`, memória no `Cerebro` |
| Backups e boletins | scripts dentro de `scratch` |
| Sincronizações de fóruns e telemetria | `Cerebro/Foruns`, `Cerebro/Dados` |
| Ronda ASTRA | `astra_operacoes/ronda_horaria` e `state` |
| Supressão MOKA | `MOKA marketing/scripts` e logs |
| Loops e sincronizações do Cérebro | `~/cerebro-miguel` e dependências indiretas no AG |

Antes de qualquer movimento, completar uma tabela por caminho com: **dono, leitores, escritores, agendamento, caminhos relativos/absolutos, locks, dependências Git, teste de saúde e reversão**.

Incluir crontabs, timers/serviços, autostart, scripts em `~/bin`, configurações de deploy e automações externas. Ausência de cron direto não libera uma pasta.

A inspeção de processos nesta sessão mostrou apenas Codex e a própria varredura com cwd no AG. **Isso não comprova ausência de outras sessões no Dell.** A execução exige inspeção no host, arquivos abertos e coordenação com os donos das sessões.

**6. Execução proposta em quatro fases**

| Fase | Entrega | Critério de parada | Rollback |
|---|---|---|---|
| **1 — Reconciliar e congelar o plano** | Dupla varredura, caminhos reais, exclusões, consumidores, manifestos e lotes concretos para aprovação | Divergência de máquina/caminho, leitura incompleta ou dono desconhecido | Sem mutações |
| **2 — Reduzir a raiz** | Agrupar mídia, entregas encerradas e resíduos liberados; remover vazios elegíveis; corrigir destinos dos produtores | Colisão, alteração concorrente, hash divergente ou dependência descoberta | Mapa inverso e metadados; nunca sobrescrever conteúdo novo |
| **3 — Liberar espaço** | Offload duplo dos maiores conjuntos frios elegíveis; Git somente após auditoria própria | Falha em qualquer nuvem, restauração ou revalidação local | Restaurar da cópia validada e conferir manifesto |
| **4 — Sustentar e migrar exceções elegíveis** | Rotina 4/4h; migrações produtivas separadas, quando autorizadas; redução gradual das exceções | Regressão funcional, saída no caminho antigo ou falha de agendamento | Reverter lote, configurações e agendamento correspondente |

Na fase 2, repetir o método que funcionou: **manifesto SHA-256 de cada arquivo → `mv` em lotes no mesmo filesystem → re-hash integral → rollback revisável**. Hash prova conteúdo; metadados e testes dos consumidores provam o restante.

O aceite deve medir: **nenhuma entrada nova fora dos destinos cadastrados, todos os movimentos verificados, nenhuma pendência única descartada e cada exceção justificada**. A meta física de dez pastas totais só pode ser discutida se Miguel futuramente liberar a migração das bases hoje intocáveis.
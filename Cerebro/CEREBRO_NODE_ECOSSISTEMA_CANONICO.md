# CÉREBRO — mapa canônico do ecossistema Miguel/Cafezinho

Vigência: 11/08/2026 (atualizado 17/08/2026 — Revista Maquiavel entra no portfólio)  
Autoridade: definição direta de Miguel, consolidada com auditoria local e SSH ao vivo

## Regra de leitura

O ecossistema tem duas camadas inseparáveis. A face visível reúne O Cafezinho, seu espelho, os sites temáticos e os projetos especiais; por trás de toda essa face existe a infraestrutura que produz, publica, protege, monitora e preserva esses ativos.

Portais e aplicativos não são ilhas nem representam sozinhos o ecossistema inteiro. São sua camada pública, apoiada pelo V4, servidores, bancos, painéis, agentes, robôs, observabilidade, custos, sincronizações, backups e pelo Cérebro; cada produto utiliza o subconjunto de infraestrutura que lhe corresponde.

Uma pasta não é legacy só porque não aparece ao público. Antes de qualquer faxina, o candidato deve ser resolvido contra este mapa e contra os nodos especializados ligados abaixo.

## 1. Face visível

### 1.1 Portais centrais

| Projeto | Endereço | Papel | Fonte operacional protegida |
|---|---|---|---|
| O Cafezinho | `https://www.ocafezinho.com` | publicação central | WordPress em ServerDo `/var/www/ocafezinho`; automação editorial V4 em NYC `198.199.121.136` |
| Cafezinho News | `https://cafezinho.news` | espelho operacional protegido | `159.65.177.60`; sincronização horária por `/root/sync_from_cafezinho.sh` |

O espelho não é legacy nem portal independente. Ele existe para redundância e recuperação do Cafezinho.

### 1.2 Sites temáticos canônicos

A lista oficial é a do registry `Projeto Cafezinho Agentes/root/ferramentas/sentinela_tematicos/site_registry.json`. Os repositórios ativos dos oito temáticos V4 ficam exclusivamente em `Projeto Cafezinho Agentes/sites-v4/`; a Revista Maquiavel é exceção registrada (repo próprio, revista ensaística fora do orquestrador V4).

| Site | Endereço | Repositório local canônico |
|---|---|---|
| Rio Carta | `https://www.riocarta.com` | `sites-v4/riocarta` |
| Mapa Rio | `https://mapario.com.br` | `sites-v4/mapario` |
| Aiatolah | `https://www.aiatolah.com` | `sites-v4/aiatolah` |
| Global South News | `https://www.globalsouth.news` | `sites-v4/globalsouth` |
| Mundo Trilhos | `https://www.mundotrilhos.com` | `sites-v4/mundotrilhos` |
| Rail Post | `https://www.railpost.news` | `sites-v4/railpost` |
| Discover Brazil | `https://www.discoverbrazil.news` | `sites-v4/discoverbrazil` |
| Ceará Digital | `https://ceara.digital` | `sites-v4/ceara` |
| Revista Maquiavel | `https://revistamaquiavel.vercel.app` | `Revista Maquiavel/maquiavel` (exceção registrada 17/08/2026: revista ensaística trilíngue, fora do orquestrador V4; registro no sentinela e nodo `CEREBRO_NODE_REVISTA_MAQUIAVEL.md`) |

Árvores `sites-tematicos`, nomes com underscore e repositórios anteriores não são autoridade de produção. Elas só podem ser tratadas como legacy depois de prova, prazo e autorização, preservando qualquer diferença local.

### 1.3 Projetos especiais

| Projeto | Produto público | Fonte canônica e proteção |
|---|---|---|
| Moka Reader | leitor de EPUB/PDF com IA; inclui Moka Video para transcrição, resumo e análise de vídeos | `Outros/Aplicativos/Moka/Moka-Lab/`; produção `https://www.mokareader.com`; `pontos_api` vivo no Tencent `/home/ubuntu/moka/pontos_api` |
| Moka Writer | aplicativo separado para escrever livros com IA, BYOK e local-first | `/home/migueldorosario/mokawriter`; produção `https://mokawriter.vercel.app`; nunca recebe conteúdo de Filhos da Impunidade |
| Filhos da Impunidade | livro investigativo, acervo, leitor e Estúdio Editorial | `Outros/novo livro/`; GitHub `migueldorosario1/filhosdaimpunidade`; app `https://filhosdaimpunidade.vercel.app`; espelho Google Drive e backups diários |

Moka Video é parte do Moka Reader, não um quarto projeto especial. Moka Writer herda engenharia do Estúdio, mas é produto e repositório independentes.

## 2. Núcleo de memória e governança

O Cérebro é o sistema interno que dá contexto ao conjunto. Sua raiz canônica local é `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`, com sincronização GitHub, B2, Drive e cópias operacionais controladas.

O Cérebro não é lixo por não ser público. Fóruns, memórias, nodos, manifestos e inventários são lastro de decisão, rollback e continuidade entre agentes.

## 3. Infraestrutura invisível que sustenta a face pública

### 3.1 Servidores vivos e papéis atuais

Estado verificado por SSH em 11/08/2026.

| Ambiente | Estado | Papel protegido |
|---|---|---|
| Local do Miguel | ativo | Cérebro canônico; orquestrador temático V4; Moka, Writer e livro; painel de destaques; ponte Telegram; backups; sync de custos e fóruns |
| NYC `198.199.121.136` | ativo, disco 68% | produção editorial V4 do Cafezinho; Augusto e Mayra; Cícero; custos; SEO/indexação; réplica do Banco Ouro |
| Tencent `43.156.151.165:38422` | ativo, disco 57% | CCTV V6, painel editorial, painel Mídia Ouro, master do Banco Ouro, `pontos_api` do Moka e nginx |
| ServerDo `190.89.239.65:51439` | ativo, disco 47% | origem WordPress de `ocafezinho.com` e `controle.ocafezinho.com`, raiz `/var/www/ocafezinho` |
| Cafezinho News `159.65.177.60` | ativo, disco 21% | espelho WordPress do Cafezinho, sync horário |
| Droplet utilitário `142.93.48.252` | ativo, disco 40% | Uptime Kuma, vigia de discos, agentes ferroviário/turismo/YouTube, Aiatolah YouTube e worker Moka Video |
| Rio-ag `159.89.185.209` | ativo, disco 84% | Cícero/Ceará, painel administrativo e Prometheus; repositórios Rio/GSN presentes não significam atividade automática |
| GSN WP `159.89.237.100` | inacessível por chave | estado desconhecido; não declarar saneado nem legacy sem acesso e decisão |

Hosts destruídos, liberados ou históricos permanecem nos mapas forenses, mas não entram na lista viva. O mapa de 06/08 deve ser lido como fotografia histórica, porque funções mudaram depois daquela data.

### 3.2 Produção editorial V4

A rota canônica do Cafezinho é `cron → /root/v4_vertical_draft_worker.py → codigo.v4_vertical_redactor_runtime → draft WordPress`. `agente_controlado.py` pertence ao legado da Zizilinda e não participa dessa cadeia.

Os temáticos usam o orquestrador local `agentes_tematicos/v4/orquestrador.py`, seus oito repositórios em `sites-v4/` e os agentes especializados no droplet utilitário. Cícero/Ceará possui também pernas operacionais em NYC e rio-ag; presença duplicada exige classificação por cron e serviço, não por nome.

### 3.3 Banco de mídia V4

O master do Banco Ouro vive no Tencent em `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`. O único escritor canônico é o robô `/root/V3/robo_banco_ouro_midia_v3.py`; NYC mantém réplica read-only no mesmo caminho para consumo do V4.

O acervo complementar do NYC vive em `/root/agent_data/acervo_midia/acervo.db`, com binários canônicos no R2. Os temáticos recebem espelho local em `agent_data/v4/banco_midia/` por `agentes_tematicos/v4/banco_midia_sync.py`.

### 3.4 Painéis e controle

O CCTV V6 é o painel canônico no Tencent, serviço `cctv-v6.service`, porta 8084. O painel editorial (`painel-editorial.service`, 8083) e o painel Mídia Ouro (`midia-ouro-panel.service`, 8091) também estão ativos.

O CCTV V5 continua ativo, mas é camada anterior e não deve ser removido só pelo rótulo. Sua aposentadoria exige migração comprovada, mais de 15 dias de inatividade e autorização de Miguel.

### 3.5 Agentes, robôs e comunicação

O Augusto é a ponte Telegram canônica, vivo em NYC por `augusto-cafezinho.service` com `/root/cafezinho/portal_cafezinho/augusto_telegram_brain.py`. Mayra está viva por `mayra-cafezinho.service`; a ponte local `ponte-cafezinho.service` conecta o comando remoto ao ambiente do Miguel.

Agentes de infraestrutura protegidos incluem autocura V4, validador de modelos, fiscal de tokens, Sentinela Temáticos, vigia de custos, vigia de discos, Prometheus pushers, indexadores, rotinas de backup e sincronização. Zizilinda e `agente_controlado.py` são históricos/legacy e não podem voltar ao V4.

### 3.6 Observabilidade e custos

Uptime Kuma vive no droplet utilitário; vigia de discos roda a cada hora no minuto 42. Node exporter/pushers alimentam a telemetria de infraestrutura nos hosts instrumentados.

Eventos de custo nascem em NYC em `/root/agent_data/banco_custos_2026-07.jsonl` e consolidados relacionados. A cópia chega ao CCTV V6 por sync local; `vigia_custos_baleia.sh`, fiscal de tokens e boletins Telegram fazem a camada de alerta.

### 3.7 Backups e rollback

Backblaze B2 guarda produção, arquivos frios e manifestos; `Cerebro-Memorias` guarda o Cérebro. O livro tem ainda GitHub e Google Drive; projetos Vercel mantêm seus repositórios Git como fonte, sem substituir backups de dados locais não commitados.

Nenhum backup é considerado válido apenas por nome. Tamanho, contagem, SHA-256 e, quando aplicável, teste de restauração ou leitura remota são obrigatórios.

## 4. Trava obrigatória para a faxina

Antes de classificar qualquer candidato:

1. resolver o caminho contra este nodo e os índices especializados;
2. verificar processo, descritor aberto, cron, systemd, import, subprocesso, fila, banco, domínio, repositório e documentação operacional;
3. identificar se sustenta direta ou indiretamente algum projeto da face visível;
4. exigir mais de 15 dias contínuos de inatividade comprovada;
5. indexar cada arquivo, diretório e link, com exceção segura para segredos;
6. consultar Miguel e obter autorização explícita;
7. criar snapshot e manifesto, enviar ao B2 e verificar por hash/readback;
8. testar restauração proporcional ao risco;
9. só então retirar a cópia quente e executar smokes dos sistemas vivos;
10. registrar resultado, destino e rollback no Cérebro.

Qualquer dúvida preserva o item no lugar. Pressão de disco não rebaixa projeto, dado, espelho ou infraestrutura viva a lixo.

## 5. Fontes especializadas

- V4 canônico: `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`
- Servidores e mudanças: `Memorias/memoria_mapa_servidores_ecossistema_20260806.md` e este nodo
- Temáticos: `CEREBRO_INDEX_SATELITES.md` + `root/ferramentas/sentinela_tematicos/site_registry.json`
- Moka Reader/Video: `CEREBRO_INDEX_MOKA_MASTER.md`
- Moka Writer: `CEREBRO_NODE_MOKA_WRITER.md`
- Filhos da Impunidade: `CEREBRO_NODE_LIVRO_FILHOS_DA_IMPUNIDADE.md`
- Comunicação/Telegram: `CEREBRO_NODE_COMUNICACAO.md`
- Banco de mídia: `Memorias/memoria_mutirao_banco_midia_v4_20260809.md`
- Telemetria e custos: `CEREBRO_NODE_TELEMETRIA.md` e `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md`
- Faxina: `Memorias/memoria_missao_faxina_diaria_legacy_20260811.md`
- Menus portal (hambúrguer+desktop, canônico+espelho): `Foruns/forum_menus_canonico_espelho_reforma_20260813.md` + `Memorias/memoria_menus_canonico_espelho_reforma_20260813.md`
- Home/footer portal (regional prevalece no bloco + footer simétrico, 13/08): `Foruns/forum_bloco_regional_prevalece_footer_simetrico_20260813.md` + `Memorias/memoria_bloco_regional_prevalece_footer_simetrico_20260813.md`

## 6. Manutenção

Este nodo deve ser atualizado toda vez que um projeto nasce, muda de domínio, troca de repositório, muda de host, ganha ou perde um serviço, entra em standby ou é aposentado. Registro antigo não é apagado; recebe data e tarja de superação.

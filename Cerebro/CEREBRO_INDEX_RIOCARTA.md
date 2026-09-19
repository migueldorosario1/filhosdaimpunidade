# Cerebro: Indice Mestre - Rio Carta

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


Este é o índice principal do ecossistema autônomo e de hospedagem do portal **Rio Carta**, isolado de qualquer outro projeto do workspace.

## 0. Ficha viva obrigatória — arquitetura real do Rio Carta

Esta seção deve ser lida antes de qualquer diagnóstico, deploy, ajuste de acesso ou criação de agente do Rio Carta. Ela duplica de propósito as informações críticas para evitar confusão com WordPress, Ghost, Cafezinho ou GSN.

### Estado auditado em 2026-05-22 23:50 BRT — resposta ao bloqueio DeepSeek

**Conclusão canônica:** o Rio Carta operacional vive no **Droplet DigitalOcean `159.89.185.209` (`agente-clone-01`)**. Esse IP **não é legado**. O legado confundido no canal era o NYC antigo `159.89.237.100` e/ou o WordPress legado `174.138.36.31`.

Validação read-only Codex em 2026-05-22 23:50 BRT:

- `root@159.89.185.209` respondeu via SSH com host `agente-clone-01`;
- `riocarta_admin.service` ativo há 3 dias, executando `/root/riocarta_admin.py`;
- crontab root contém linhas reais de coleta, publicação remota e indexação Google;
- clone Astro remoto existe em `/root/riocarta_remote/rio_carta/`;
- chave Git dedicada existe no Droplet como `/root/.ssh/id_ed25519_riocarta_github` (não copiar conteúdo);
- site público continua GitHub -> Vercel.

**O que NÃO é o Rio Carta vivo hoje:**

- Tencent/Cingapura `43.156.151.165`: tem arquivos antigos `agente_riocarta.py` e `robo_coleta_riocarta.py`, mas o crontab root auditado em 2026-05-22 não possui linhas Rio Carta. Tratar como legado/sombra até prova em contrário.
- Tencent/Beijing `82.156.167.218`: auditoria read-only em 2026-05-22 não encontrou crontab nem arquivos Rio Carta relevantes. É executor do GSN/Prometheus, não Rio Carta.
- Alibaba/Beijing `39.106.184.215`: Cérebro/Kimi/observabilidade, não publicador Rio Carta.
- WordPress Rio Carta `174.138.36.31`: legado. Não usar `/wp-admin`/REST WP como caminho editorial vivo.

### Crontab vivo do Rio Carta no Droplet

Servidor: `root@159.89.185.209`.

Linhas ativas auditadas:

```cron
0,30 0-2,9-23 * * * RIOCARTA_PYTHON=/usr/bin/python3 /root/riocarta_cron_rotativo.sh >> /root/logs/riocarta_cron_window.log 2>&1 # RIOCARTA_COLETA_ROTATIVA_30MIN_DIA_CODEX_20260515
0 3-8 * * * RIOCARTA_PYTHON=/usr/bin/python3 /root/riocarta_cron_rotativo.sh >> /root/logs/riocarta_cron_window.log 2>&1 # RIOCARTA_COLETA_ROTATIVA_1H_MADRUGADA_CODEX_20260515
23 * * * * cd /root && RIOCARTA_BATCH_SIZE=3 RIOCARTA_MAX_BATCH_SIZE=3 RIOCARTA_MAX_AUDIT_ATTEMPTS=6 /usr/bin/flock -n /tmp/riocarta_remote_publish.lock /root/riocarta_remote_publish.sh >> /root/logs/riocarta_remote_publish_cron.log 2>&1 # RIOCARTA_PUBLICADOR_REMOTO_CODEX_20260515
30 * * * * /usr/bin/python3 /root/riocarta_remote/root/riocarta_indexador_google.py >> /root/logs/riocarta_indexador_cron.log 2>&1 # RIOCARTA_INDEXADOR_GOOGLE_API
```

**Interpretação:**

- coleta roda a cada 30 minutos no período diurno definido e a cada 1 hora na madrugada;
- publicação remota roda uma vez por hora no minuto `23`, com lote máximo 3;
- indexador Google roda uma vez por hora no minuto `30`;
- alterações de ritmo devem mexer **somente nessas linhas**, com backup antes e rollback literal.

### Como auditar antes de mexer

```bash
ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209 'hostname; systemctl status riocarta_admin.service --no-pager -l | head -30; crontab -l | grep -i riocarta; tail -n 80 /root/logs/riocarta_remote_publish_cron.log; tail -n 80 /root/logs/riocarta_cron_window.log'
```

Nunca usar `crontab -r`. Para reduzir cadência, salvar backup:

```bash
ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209 'crontab -l > /root/crontab_backup_pre_riocarta_<DATA>.txt'
```

Rollback:

```bash
ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209 'crontab /root/crontab_backup_pre_riocarta_<DATA>.txt'
```

### Ponto de entrada dos scripts

- Painel humano/admin: `/root/riocarta_admin.py` via `riocarta_admin.service`.
- Coleta rotativa: `/root/riocarta_cron_rotativo.sh` -> `/root/riocarta_cron_coleta.sh`.
- Publicação Astro/GitHub/Vercel: `/root/riocarta_remote_publish.sh`.
- Publicador Astro interno: `/root/riocarta_remote/rio_carta/scripts/riocarta_publish_hourly_batch.mjs`.
- Indexação Google: `/root/riocarta_remote/root/riocarta_indexador_google.py`.

### Como publica

O fluxo vivo é:

1. coletor/painel gera ou organiza pautas no Droplet;
2. publicador remoto usa o clone `/root/riocarta_remote/rio_carta/`;
3. conteúdo vira Markdown/assets no repositório Astro;
4. Git push para `migueldorosario1/rio-carta`;
5. Vercel publica `https://www.riocarta.com`.

Não usar `deploy_riocarta.sh` como caminho normal de publicação. Ele é artefato histórico de migração/rsync. O caminho operacional é **Droplet -> GitHub -> Vercel**.

### Resumo curto

Rio Carta é um site **Astro/Markdown publicado por GitHub -> Vercel**, com um **painel editorial Flask próprio** exposto em `/admin` e hospedado no Droplet Digital Ocean.

### O que o Rio Carta NÃO é

- Rio Carta **não é WordPress operacional**.
- Rio Carta **não usa `/wp-admin`** para o fluxo editorial vivo.
- Rio Carta **não deve receber payloads de WordPress/API REST** sem tradução para Markdown/Astro.
- Rio Carta **não é Ghost**.
- Rio Carta **não deve reutilizar credenciais, mídia, banco ou scripts do Cafezinho** sem isolamento explícito.

### Entrada humana correta

- Painel editorial: `https://www.riocarta.com/admin`.
- Login do painel: `https://www.riocarta.com/login`.
- O painel imita visualmente WordPress, mas é Flask customizado.
- Código local de referência: `Rio Carta Agentes/root/riocarta_admin.py`.
- Serviço remoto: `riocarta_admin.service`.
- Segredos do painel ficam no Droplet em `/root/riocarta_admin.env`; não copiar valores para fórum, canal ou Cérebro.

### Fluxo de publicação correto

1. Editor humano ou agente usa o painel/robô do Rio Carta.
2. O painel/robô grava Markdown, imagens e metadados no GitHub.
3. Repositório canônico: `migueldorosario1/rio-carta`.
4. A Vercel publica automaticamente a partir do GitHub.
5. Site público: `https://www.riocarta.com`.

Regra operacional: o caminho preferencial é **Droplet/Painel/Publicador -> GitHub -> Vercel -> site público**. Evitar deploy direto pelo Vercel CLI salvo emergência documentada, porque já houve limite/cota de upload.

### Infra viva

- Droplet Rio Carta: `root@159.89.185.209`.
- Host remoto observado: `agente-clone-01`.
- Comando SSH documentado: `ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209`.
- Painel Flask remoto: `http://159.89.185.209:5000`.
- Serviço remoto: `riocarta_admin.service`.
- Crontab vivo: coleta rotativa, publicador remoto e indexador Google descritos na seção "Estado auditado em 2026-05-22 23:50 BRT".
- Rewrites Vercel encaminham `/admin`, `/login`, `/logout`, `/drafts`, `/posts`, `/edit/*`, `/delete/*` e `/upload_image` para o Flask no Droplet.
- Arquivo Vercel relevante: `Rio Carta Agentes/rio_carta/vercel.json`.

### Regra de acesso e permissões

- Para o colaborador comum, o caminho de uso é o painel `https://www.riocarta.com/admin`.
- GitHub também é parte da arquitetura, mas é infraestrutura/código/conteúdo, não o painel editorial principal para colaborador comum.
- Se um agente não consegue “entrar no Rio Carta”, checar nesta ordem:
  1. `https://www.riocarta.com/login` responde?
  2. `riocarta_admin.service` está ativo no Droplet?
  3. Porta `5000` está ouvindo no Droplet?
  4. `/root/riocarta_admin.env` tem `RIOCARTA_ADMIN_USERS_JSON`, `GITHUB_TOKEN`, `RIOCARTA_GITHUB_REPO` e `RIOCARTA_ADMIN_SECRET_KEY` presentes?
  5. O token/chave tem permissão para escrever no GitHub `migueldorosario1/rio-carta`?

### Arquivos e fóruns de retomada

- Admin Flask: `Rio Carta Agentes/root/riocarta_admin.py`.
- Site Astro: `Rio Carta Agentes/rio_carta/`.
- Rewrites admin: `Rio Carta Agentes/rio_carta/vercel.json`.
- Fórum do admin/502: `Rio Carta Agentes/Foruns/forum_riocarta_admin_502_20260517.md`.
- Fórum SSH Droplet: `Rio Carta Agentes/Foruns/forum_riocarta_ssh_droplet_20260515.md`.
- Inventário seguro de credenciais: `Rio Carta Agentes/Foruns/credenciais.md`.

## 1. Governança e Decisões Arquiteturais
- **[Fórum Oficial Rio Carta](Foruns/forum_riocarta.md)**: Registro inicial de criação e isolamento dos agentes (Data: 2026-05-11).
- **[Arquitetura V1](Foruns/forum_arquitetura_v1_riocarta.md)**: Constituição técnica do Rio Carta isolado.

### [2026-05-19 15:08 BRT] Painel Admin — acesso Miguel e trava por dono do slug

Codex assumiu o sprint de acesso Rio Carta que estava com DeepSeek. O painel vivo é Flask em `/admin`, não WordPress. No Droplet `159.89.185.209`, foi criado o usuário `miguel` no `RIOCARTA_ADMIN_USERS_JSON`; a senha ficou apenas no cofre remoto `/root/riocarta_miguel_access_20260519_codex.txt` (`600`).

Hardening aplicado em `/root/riocarta_admin.py` e espelhado localmente em `Rio Carta Agentes/root/riocarta_admin.py`: usuários comuns seguem vendo apenas itens próprios, e agora `/edit/<slug>`, `/delete/<slug>` e alteração de item existente em POST também validam propriedade pelo `admin_db.json`. Isso fecha o risco de abrir post de outro usuário por URL direta. `admin` é superusuário via `RIOCARTA_ADMIN_SUPERUSERS=admin`.

Backups remotos: `/root/riocarta_admin.py.bak_pre_miguel_access_codex_20260519_180524` e `/root/riocarta_admin.env.bak_pre_miguel_access_codex_20260519_180524`. Validação: serviço `active`, `/login` público `200`, `/admin` público `302`, login Miguel OK, post do Theo bloqueado para Miguel por URL direta, admin ainda edita.

Atualização 16:02 BRT: Miguel mudou a diretriz para painel colaborativo. Usuários logados podem ver, editar e apagar posts/rascunhos uns dos outros para a equipe se ajudar. Patch aplicado em `/root/riocarta_admin.py`; backup remoto pré-ajuste colaborativo: `/root/riocarta_admin.py.bak_pre_team_edit_codex_20260519_184104`. Smoke: Miguel vê post de `theorodrigues` e abre `/edit/<slug>` com `200`; serviço ativo.

## 2. Agentes Autônomos Rio Carta
Os agentes abaixo pertencem exclusivamente ao silo Rio Carta e devem manter prefixo `riocarta_`. Eles estão configurados para carregar a chave `chaves_riocarta.env` compulsoriamente.
- `root/riocarta_agente_master.py` (Trends V9 isolado)
- `root/riocarta_agente_comentarista.py` (Enxame de comentários isolado)
- `root/riocarta_robo_coleta.py` (Coletor Bruto)
- `root/riocarta_agente_twitter.py` (V0 social X/Twitter, rascunho apenas)
- `root/riocarta_agente_instagram.py` (V0 social Instagram, rascunho apenas)
- `root/riocarta_social_common.py` (fila social isolada, leitura Markdown Astro e trava LLM chinesa)

### Agentes sociais Rio Carta V0 — 2026-05-16

Origem: pedido do Miguel repassado pelo Antigravity para clonar/adaptar os agentes sociais do Cafezinho ao Rio Carta sem tocar nos scripts originais do Cafezinho.

Estado vivo:

- Arquivos criados no silo Rio Carta: `riocarta_agente_twitter.py`, `riocarta_agente_instagram.py` e `riocarta_social_common.py`.
- A V0 não publica em X/Instagram. Ela cria rascunhos em `root/agent_data/riocarta_social_queue.json` com `mode: draft_only`.
- Motivo do freio: ainda não há credenciais sociais próprias do Rio Carta nem garantia de que a conta/postador certo seria usado. Publicação real ou cron só depois de credenciais próprias e autorização explícita.
- Cascatas sociais em `root/config/riocarta_cascatas_llm.json`: `deepseek`, `alibaba`/Qwen, `moonshot`/Kimi e `zhipu`/GLM.
- Trava runtime em `riocarta_social_common.py`: se `social_twitter` ou `social_instagram` contiver provider fora de `deepseek`, `alibaba`, `moonshot` ou `zhipu`, o agente aborta antes de chamar LLM.

Validação inicial:

- Local e Droplet: `python3 -m json.tool` no config, `py_compile` nos 3 arquivos sociais e checagem explícita de providers OK.
- Dois rascunhos de laboratório foram gerados com modelos chineses (`qwen-plus` e `deepseek-v4-pro`), sem postagem real.

Rollback:

```bash
cp "Rio Carta Agentes/Backups/riocarta_cascatas_llm.json.bak_pre_social_chinese_only_20260516_014631_codex" "Rio Carta Agentes/root/config/riocarta_cascatas_llm.json"
cp "Rio Carta Agentes/Backups/riocarta_social_common.py.bak_pre_social_chinese_only_20260516_014631_codex" "Rio Carta Agentes/root/riocarta_social_common.py"
python3 -m json.tool "Rio Carta Agentes/root/config/riocarta_cascatas_llm.json" >/tmp/riocarta_cascatas_llm.rollback.ok
python3 -m py_compile "Rio Carta Agentes/root/riocarta_social_common.py" "Rio Carta Agentes/root/riocarta_agente_instagram.py" "Rio Carta Agentes/root/riocarta_agente_twitter.py"
```

## 3. Integração Premium e SEO
- **Agente Injetor Premium (`root/riocarta_agente_injetor_premium.py`)**: desativado para mutação pós-publicação. Cesta Premium, interlinks e newsletter devem ser componentes/layouts Astro, não cron WordPress.

## 4. Banco de Dados e Mídia
- **Media DB**: qualquer banco de mídia usado pelo Rio Carta precisa existir dentro do silo Rio Carta. O deploy não pode buscar arquivos em diretórios de outros projetos.

## 5. Script de Deploy
- O script `deploy_riocarta.sh` contém as diretivas de rsync para migrar essa tecnologia autônoma para o Droplet no Digital Ocean quando o endereço de IP for configurado.

## 6. Bugs e Monitoramento Noturno
- **✅ BUG-RIOCARTA-RLS-SUPABASE-20260728 (SEGURANÇA — RESOLVIDO 2026-07-28):** tabela `public.comentarios` do Supabase (`qznsodqyfwhaouruhsbp`) estava sem Row-Level Security (leitura/UPDATE/DELETE abertos). Miguel executou o fix `Rio Carta Agentes/FIX_RLS_COMENTARIOS_20260728.sql` no dashboard; verificado externamente (GET 200, UPDATE negado, INSERT validado por policy 401/42501). Diretriz V1 §4.2 ("RLS desligado propositalmente") **revogada** — novo padrão: RLS sempre ligado + policies granulares. Detalhes: [fórum](../Rio Carta Agentes/Foruns/forum_riocarta_rls_supabase_20260728.md) + [memória técnica](../Rio Carta Agentes/Foruns/memoria_tecnica_rls_supabase_20260728.md).
- **[Monitoramento noturno Rio Carta 2026-05-13](Foruns/forum_monitoramento_noite_riocarta_20260513.md)**: log separado de publicações, erros, correções, categorias, imagens destacadas e fonte.
- **[Investigação erros cron Rio Carta 2026-05-13](Foruns/forum_investigacao_erros_cron_riocarta_20260513.md)**: investigação aberta após madrugada com publicação/coleta automática quebradas. Bugs indexados: cron não encontra `npm`; coletor usa Python sem `zoneinfo`; monitor local não encontra `rg`; ponte banco -> fila mascarou estoque real; auditoria segurou matérias por data/categoria/fonte/imagem.
- **BUG-RIOCARTA-CRON-NPM-20260513:** cron local de publicação não carrega `nvm`, então `npm run riocarta:publish-hourly` falha. Teste manual no terminal não valida cron.
- **BUG-RIOCARTA-CRON-ZONEINFO-20260513:** cron local de coleta usa `/usr/bin/python3` 3.8.10 sem `zoneinfo`, enquanto terminal usa pyenv Python 3.10.13. Coleta automática falha até fixar Python.
- **BUG-RIOCARTA-MONITOR-RG-20260513:** monitor local Rio/Cafezinho não encontra `rg` no cron. Deve usar caminho absoluto, fallback para `grep` ou ambiente comum.
- **BUG-RIOCARTA-FILA-ACK-20260513:** ponte banco -> fila marcou pautas como `processado_v9=1`/`fila_markdown` antes da publicação real. Precisa de estado intermediário e confirmação pós-deploy.
- **BUG-RIOCARTA-SMOKE-NOME-OPERACIONAL-20260513:** `riocarta_smoke_markdown.py` virou ponte operacional. Nome e arquivos `smoke-*` confundem auditoria e operadores. Separar smoke de ponte produtiva.
- **BUG-RIOCARTA-RETIDAS-QUALIDADE-20260513:** auditoria segurou matérias por data ambígua, categoria/fonte ruim e imagem inadequada. Recuperar com correção controlada, não liberar em massa.
- **Categoria no post singular:** `src/layouts/BlogPost.astro` deve mostrar a categoria principal da matéria dentro do post individual. A categoria vem de tags reconhecidas; fallback por título só deve ser usado quando faltarem tags.
- **Regra de prioridade:** `nacional`, `internacional` e `geopolitica` têm prioridade sobre a palavra solta "segurança" para evitar classificar "Conselho de Segurança" como Segurança Pública.
- **Autocura pendente:** corrigir aviso `No module named 'riocarta_autocura_licoes'` no coletor, mantendo isolamento do silo Rio Carta.
- **Regra anti-token:** checagens simples de estilo, categoria, fonte e parágrafo devem ser determinísticas. LLM só entra quando houver ambiguidade editorial real, com prompt curto e teto de resposta.

## 7. Arquitetura viva 2026-05-16 - menus, links, UX e GSN

Status: em planejamento e indexação. Não aplicar código sem traduzir as propostas para a arquitetura real do Rio Carta.

Regra permanente: o Rio Carta precisa receber atenção forte do Cérebro. Toda mudança estrutural, bug, sprint, deploy, decisão visual, decisão editorial, agente novo e incidente operacional deve entrar neste índice ou em fórum próprio com ponteiro claro aqui.

### Fóruns novos

- `../Projeto Cafezinho Agentes/Foruns/forum_menu_riocarta_20260515.md`
  - Objetivo: expansão do menu do Rio Carta.
  - Escopo: Prefeituras, Câmaras de Vereadores, vereadores por cidade, Alerj, Cultura, Turismo e Bares.
  - Estado: parte visual/menu já foi implementada em sprints anteriores; partes grandes de dados ainda exigem coletores/JSONs próprios.
  - Cuidado: dados de vereadores/deputados/bairros/bares devem ficar em `src/data/` ou base equivalente do Astro, não em WordPress.

- `../Projeto Cafezinho Agentes/Foruns/forum_header_riocarta_20260515.md`
  - Objetivo: nova arquitetura visual do header.
  - Escopo: logo maior à esquerda; três camadas à direita; slogan, menu e redes sociais.
  - Estado: mudanças visuais de header/menu foram feitas em commits de 2026-05-15 e validadas por build/deploy.

- `../Projeto Cafezinho Agentes/Foruns/forum_opiniao_riocarta_20260515.md`
  - Objetivo: criar editoria de Opinião do Rio Carta.
  - Escopo: 1 diretor de opinião + 12 colunistas autônomos, com tags próprias, páginas no Astro e agentes dedicados.
  - Estado: planejamento; não publicar colunistas sem autorização editorial e sem dry-run.
  - Cuidado: colunistas são personagens editoriais fictícios; precisam de identidade consistente, aviso interno e controle para não parecerem pessoas reais.

- `../Projeto Cafezinho Agentes/Foruns/forum_bug_thumb_social_riocarta.md`
  - Objetivo: corrigir `og:image`/`twitter:image` errados no compartilhamento social.
  - Estado: resolvido em 2026-05-15.
  - Causa: `BlogPost.astro` mostrava `heroImage`, mas `BaseHead.astro` não recebia essa imagem e caía no placeholder.
  - Correção: `BaseHead.astro` aceita imagem string/metadata; `BlogPost.astro` passa `image={heroImage}`.
  - Commit: `89075f4 Fix Rio Carta social share image`.
  - Validação: build remoto OK; HTML público passou a apontar `og:image`/`twitter:image` para `/hero/...`.

- `../Projeto Cafezinho Agentes/Foruns/forum_agentes_sociais_rio_carta.md`
  - Objetivo: adaptar Twitter/X e Instagram do Rio Carta.
  - Estado: V0 em rascunho, sem publicação real.
  - Arquivos: `riocarta_social_common.py`, `riocarta_agente_twitter.py`, `riocarta_agente_instagram.py`.
  - Cuidado: precisa de credenciais sociais próprias do Rio Carta; não reutilizar Cafezinho.

- `../Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_rastreador_links_20260516.md`
  - Objetivo: criar arquitetura de rastreador contínuo para popular links de Prefeituras, Câmaras, Vereadores, Bares e Shows.
  - Direção útil: base JSON por tipo de entidade; itens sem URL ficam em fila de retentativa; script futuro deve atualizar lacunas e notificar o motor Astro/Markdown.

- `../Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_votos_mapas_20260516.md`
  - Objetivo: listas de políticos com votos e percentual, ordenadas por mais votados; expansão para deputados federais, senadores e mapas.
  - Regra de dados: nomes de políticos devem virar tags/metadata granular, não categorias estruturais.

- `../Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_ux_ui_20260516.md`
  - Objetivo: página interna de edição/revisão, organização de destaques, seções na home e botões globais.
  - Atualização 2026-05-16: botões macro agora são seis: Geral, Política, Lazer, Segurança, Economia e Serviços.
  - Direção útil: macroeditorias devem ser metadado estrutural no frontmatter/JSON do Rio Carta, usadas como filtro global no Astro.
  - Parecer Codex: usar `categoria_macro` no frontmatter com valores `geral`, `politica`, `lazer`, `seguranca`, `economia`, `servicos`. Não usar categoria WP nem API REST.

- `../Projeto Cafezinho Agentes/Foruns/forum_riocarta_pagina_teste_header_20260516.md`
  - Objetivo: validar novo header em página isolada antes de mexer no site.
  - Parecer Codex: aprovado como teste visual isolado, mas em Astro, não WordPress.
  - Caminho seguro: criar rota `src/pages/teste-header-novo.astro` e componente `HeaderTesteMacro.astro`, sem alterar `Header.astro` de produção, home, posts, schema, publicadores, crons ou `.py`.
  - Rollback: remover rota/componente ou `git revert` do commit pequeno.

- `../Projeto Cafezinho Agentes/Foruns/tarefa_sprint_riocarta_gsn_20260516.md`
  - Objetivo: painel de tarefas Rio Carta/GSN.
  - Atenção: o texto original fala em WordPress/API REST. Isso NÃO é estado vivo do Rio Carta; precisa ser traduzido para Astro/Markdown/Vercel/Git antes de qualquer implementação.

- `../Projeto Cafezinho Agentes/Foruns/forum_gsn_arquitetura_espelho_cafezinho_20260516.md`
  - Objetivo: discutir se o GSN pode espelhar a arquitetura técnica do Rio Carta.
  - Estado: diagnóstico/planejamento.
  - Direção: GSN pode reaproveitar padrões Astro/Markdown/Git/automação do Rio Carta se forem isolados por domínio, credenciais e dados próprios.

- `../Projeto Cafezinho Agentes/Foruns/forum_arquitetura_gsn_100_autonoma_20260516.md`
  - Objetivo: lançar Global South News como portal headless 100% autônomo, baseado no padrão Rio Carta.
  - Parecer Codex: direção aprovada, mas a cópia integral do Rio Carta deve ficar em quarentena.
  - Checklist obrigatório antes de deploy: remover referências a Rio Carta, verificar segredos/copias de `.env`, trocar prefixos para `gsn_`, criar `CEREBRO_INDEX_GSN.md`, build local, nada de cron/publicador/social antes da auditoria de independência.

- `Foruns/forum_riocarta_autocura_erros_20260515.md`
  - Objetivo: instalar autocura Rio Carta V1 e catalogar erros recorrentes.
  - Estado: aplicado.
  - Agente novo: `root/riocarta_autocura.py`.
  - Lições: fila com Markdown ausente, imagem pequena, auditor temporal, fonte cega, título repetido e matéria em inglês.
  - Curas V1: remove fila quebrada, remove título repetido no primeiro parágrafo, corrige descrição repetida, troca fonte placeholder por domínio quando possível, rebaixa matéria claramente em inglês.
  - Limite: sem LLM, sem mexer em crontab, sem force-push.

- `Foruns/forum_riocarta_ssh_droplet_20260515.md`
  - Objetivo: registrar incidente SSH e recuperação da chave do Droplet.
  - Estado: resolvido.
  - Regra aprendida: antes de declarar bloqueio de acesso Rio Carta, procurar em `CEREBRO_INDEX_RIOCARTA.md`, arquitetura, memória SSH, scratch/logs/backups.
  - Cuidado: senha e material sensível não devem ir para fórum/canal/Cérebro em texto aberto.

### Correção arquitetural obrigatória

Rio Carta não é WordPress operacional.

Arquitetura viva:

- conteúdo em Markdown/Astro;
- deploy por Git/Vercel;
- frontmatter/JSON como fonte de metadados;
- categorias, tags, macroeditorias, links, votos e mapas devem ser modelados no schema do Rio Carta, não em payload WP;
- qualquer proposta escrita em linguagem WordPress deve ser tratada como rascunho conceitual e traduzida antes de virar código.

Traduções obrigatórias de linguagem:

- "categoria do WordPress" -> frontmatter/JSON de categoria/macroeditoria no Astro;
- "tags da API REST" -> campo `tags` no Markdown/JSON que alimenta o Astro;
- "PUT/POST em post WP" -> edição de Markdown/JSON + commit Git + build/deploy;
- "sticky WordPress" -> frontmatter de destaque temporizado + zelador;
- "puxar últimos posts via WP REST" -> ler coleção Markdown/Content API local ou índice gerado do Astro.

### Estado operacional observado em 2026-05-16

- Crons remotos ativos no Droplet Rio Carta.
- Coleta rodando por regiões.
- Publicador horário confirmando lotes de 3 matérias nas últimas rodadas observadas.
- Builds Astro recentes OK, com home e URLs públicas respondendo HTTP 200.
- Autocura conservadora aplicada em sobras `untracked` pós-build: backup antes de `git clean -fd`, sem force-push.

### Pendências de indexação

- Consolidar esses fóruns novos dentro de um node/camada própria quando a migração do Cérebro Miguel para a raiz avançar.
- Corrigir linguagem dos fóruns que ainda dizem WordPress/API REST para evitar que agente futuro implemente contra plataforma errada.
- Definir schema canônico para:
  - macroeditoria: `geral`, `politica`, `lazer`;
  - tipo de entidade: prefeitura, camara, vereador, deputado, senador, bar, show, mapa;
  - votos e percentual;
  - URL oficial e status de verificação;
  - data de validade para eventos.

### Prioridade de organização

1. Manter este índice como ponto único de retomada do Rio Carta.
2. Toda nova frente Rio Carta deve ter fórum + ponteiro neste índice.
3. Toda proposta do Antigravity com linguagem WordPress deve ganhar nota de tradução para Astro antes de virar tarefa.
4. Bugs resolvidos devem sair do fórum e entrar aqui com causa, correção, validação e rollback.
5. O Cérebro Miguel deve tratar Rio Carta como laboratório sério para o Cafezinho, mas sem tocar no Cafezinho vivo.

## BUG-20260513-RIOCARTA-CRON-ENV-ACK - corrigido parcialmente

Status: correcao aplicada em 2026-05-13 10:25 BRT.

Sintoma: cron do Rio Carta falhava porque o ambiente automatico nao carregava Node/npm do nvm, Python 3.10 com zoneinfo nem rg. Alem disso, a ponte banco -> Markdown podia marcar noticia como usada antes da publicacao real.

Correcao aplicada: ambiente comum `riocarta_cron_env.sh`; cron horario, coletor e monitor carregam esse ambiente; publicador confirma o banco apenas depois de commit/push; preflight de cron criado e validado em ambiente vazio.

Resultado do teste: npm, node, Python 3.10/zoneinfo, inbox real e rg OK.

Pendente: recuperar/normalizar as 158 noticias que ficaram com status `fila_markdown` antes da correcao, caso se confirme que nao foram publicadas.

## OPERACAO-20260513-RIOCARTA-CRON-PUBLISH-CODEX - registro completo

Status: aplicado, testado, religado e deployado em 2026-05-13, entre 09:55 e 10:35 BRT.

Contexto: Rio Carta estava com falha de cron por ambiente automatico minimo. O cron nao encontrava Node/npm do nvm, Python correto com `zoneinfo`, nem `rg`. Tambem havia bug de seguranca operacional: a ponte banco -> Markdown podia marcar itens como usados/publicados antes do deploy real.

Coordenacao: antes da edicao, Codex avisou no canal Trindade para evitar conflito com Claude/Code. Claude respondeu depois no canal com patch separado de fonte/categoria/logo. Miguel autorizou seguir sem esperar Code/Claude.

Arquivos criados/alterados por Codex:

- `root/riocarta_cron_env.sh`: ambiente comum para cron, com caminhos explicitos de Node/npm, Python 3.10 e `rg`.
- `root/riocarta_cron_preflight.sh`: teste de ambiente vazio de cron.
- `root/riocarta_confirm_published.py`: confirma no SQLite somente depois de publicacao/deploy.
- `rio_carta/scripts/riocarta_hourly_cron.sh`: carrega ambiente comum, usa Python/npm corretos e deixou de chamar a ponte com marcacao antecipada.
- `root/riocarta_cron_coleta.sh`: carrega ambiente comum.
- `rio_carta/scripts/riocarta_publish_hourly_batch.mjs`: confirma banco apos commit/push, limita tentativas de auditoria por ciclo e inclui posts ja visiveis da fila em commits de retomada.
- `Projeto Cafezinho Agentes/scripts/monitor_publicacao_rio_cafezinho.sh`: carrega ambiente comum quando existir, usa `rg` explicito e tem fallback para `grep`.

Validacoes executadas:

- `bash -n` nos scripts de shell alterados.
- `python3 -m py_compile` nos scripts Python.
- `node --check` no publicador JS.
- preflight em ambiente vazio: npm 10.9.7, Node v22.22.2, Python 3.10.13 com `zoneinfo`, inbox real com 344 itens, `rg` 15.1.0.
- rodada real do publicador com build Astro OK e push para `origin/main`.

Cron local apos correcao:

- publicador Rio Carta: minuto 05 de cada hora.
- coletor Rio Carta: minuto 50 de cada hora.
- monitor Cafezinho/Rio: a cada 2h, em horario desencontrado.

Commits/deploy:

- `01db405` - rodada automatica pos-correcao, build/push OK.
- `1d6ef58` - ajuste de retomada do publicador e inclusao de 4 materias preparadas/auditadas que estavam visiveis localmente.

Banco:

- 4 pautas confirmadas como `publicado_markdown` apos push.
- Estado apos confirmacao: 184 `novo/processado_v9=0`, 154 `fila_markdown/processado_v9=1`, 4 `publicado_markdown/processado_v9=1`, 2 `novo/processado_v9=1`.

Freios e aprendizados:

- O publicador agora nao deve varrer 160 itens em uma rodada quando a auditoria barra materias.
- Padrao atualizado em 2026-05-15: `RIOCARTA_BATCH_SIZE=10`, `RIOCARTA_MAX_BATCH_SIZE=10` e `RIOCARTA_MAX_AUDIT_ATTEMPTS=30`.
- O publicador nao pode voltar a travar em 2 por rodada: a meta operacional autorizada por Miguel e cerca de 10 materias/hora, com fila alternada por categoria.
- Se a auditoria bloquear uma sequencia, registrar e esperar proximo ciclo; nao gastar chamadas externas indefinidamente.
- Itens antigos `fila_markdown` precisam de recuperacao/normalizacao controlada, nao publicacao cega.

Pendencias:

- Recuperar ou normalizar os 154 itens antigos `fila_markdown` marcados antes da correcao.
- Revisar fontes/categorias dos itens bloqueados por auditoria, especialmente casos com fonte generica, data ambigua, tag territorial incoerente ou imagem inadequada.
- Eventual renomeacao/divisao de `riocarta_smoke_markdown.py`, porque hoje ele e usado operacionalmente apesar do nome de smoke.

## OPERACAO-20260514-RIOCARTA-LABORATORIO-CODEX

Status: em andamento, iniciado em 2026-05-14 00:48 BRT por ordem do Miguel.

Contexto: Miguel pediu para usar o Rio Carta como laboratorio: anotar erros, auditar, corrigir causas e deixar tudo no Cerebro. Publicacao automatica foi pausada; coleta e painel manual continuam ativos. Claude tambem esta em loop, entao toda correcao deve ser anunciada no canal antes de mexer em publicacao/deploy.

Freio aplicado:

- `rio_carta/tools/riocarta_publish_paused.txt`: trava operacional de publicacao automatica.
- `rio_carta/scripts/riocarta_hourly_cron.sh`: agora para antes de chamar ponte/publicador quando a trava existe.
- `rio_carta/scripts/riocarta_publish_hourly_batch.mjs`: tambem para quando chamado diretamente sem `--audit-current`.

Achado principal da auditoria: o ultimo ciclo publicou 29 materias. O limite de novas materias estava em 2, mas o publicador somava materias ja visiveis da fila no conjunto de commit/deploy/confirmacao. Isso inflava o lote e podia confirmar de novo conteudo antigo como se fosse nova publicacao. Patch aplicado para separar `changedArticleSet` (arquivos tocados/reauditados) de `publishSet` (novas materias realmente publicadas).

Resultado da triagem deterministica do ultimo lote:

- 29 materias auditadas.
- 18 com gravidade alta.
- 1 com gravidade media.
- 10 sem problema deterministico nesta primeira triagem.

Regras indexadas:

- Arquivo com prefixo operacional `smoke-` nao pode virar URL publica.
- Imagem destacada com caminho `smoke-smoke-*` nao pode ir ao ar.
- Fonte generica (`Fonte Original`, `publicacao original`, `Agencia Internacional`) bloqueia publicacao ate resolver fonte real.
- Paragrafos devem ter no maximo duas frases antes de publicar.
- Publicador deve separar novas materias aprovadas, materias ja visiveis, materias em auditoria e materias rebaixadas.
- `--audit-current` nunca deve fazer commit/push; mesmo se alguem chamar junto com `--commit`, o publicador ignora commit nesta modalidade. Script seguro: `npm run riocarta:audit-current`.

Forum da investigacao: `Foruns/forum_laboratorio_auditoria_riocarta_20260514.md`.

### Resultado 2026-05-14 01:00 BRT

Codex executou o rebaixamento controlado de 18 posts do ultimo lote com gravidade alta por vazamento operacional `smoke-` no slug e/ou `smoke-smoke-*` na imagem destacada. Todos foram marcados `draft: true`, sem apagar conteudo, e continuam acessiveis na sala de previa/rascunhos para correcao posterior.

Commit/deploy source: `1a4605f` (`Pause Rio Carta publishing and rebaixar risky smoke posts`) enviado para `origin/main` apos rebase com commit do painel manual `a765884`. Build local pos-rebase OK: 2654 paginas geradas, sitemap OK.

Backup dos 18 arquivos antes do rebaixamento: `Backups/riocarta_rebaixamento_20260514_0100/`.

Consenso operacional: Miguel autorizou autonomia; Codex pediu consenso delegado ao Claude no canal; medida e reversivel e conservadora. Se Claude apontar excecao pontual, rollback e restaurar `draft: false` apenas no item aprovado.

## OPERACAO-20260514-RIOCARTA-ANTI-ANTHROPIC-CODEX

Status: contido e deployado em 2026-05-14 08:29 BRT.

Contexto: Miguel identificou cobrancas recorrentes Anthropic. A investigacao apontou que o Rio Carta tinha chamadas diretas a Anthropic no master e fallbacks ativos no roteador, podendo gerar custo mesmo se o JSON de cascatas fosse alterado.

Correcoes:

- `root/riocarta_agente_master.py`: 3 chamadas hardcoded a Anthropic foram trocadas para DeepSeek.
- `root/riocarta_agente_roteador_llm.py`: Anthropic removido de fallbacks ativos e da cadeia padrao; suporte explicito ficou dormente.
- `root/config/riocarta_cascatas_llm.json`: Anthropic removido das cascatas; prioridade em DeepSeek, Moonshot/Kimi e Alibaba/Qwen.

Deploy:

- Droplet: `root@159.89.185.209` (`agente-clone-01`).
- Backup remoto: `/root/backups_riocarta_anti_anthropic_20260514_0828_codex_anti_anthropic/`.
- Validacao remota: `py_compile` OK, JSON OK, cascatas sem Anthropic e busca por chamada ativa `gerar_texto_provider_hard("anthropic", ...)` vazia.

Observacao: o roteador ainda tem codigo de suporte para Anthropic se alguem forcar explicitamente o provider. Isso nao e rota ativa. Para religar Anthropic como rota automatica, precisa autorizacao humana, teto de custo e registro previo no canal/forum.

## OPERACAO-20260514-RIOCARTA-CATEGORIAS-CORRETAS

Status: NAO APLICADO. Bloco inserido diretamente por Antigravity sem autorizacao em 2026-05-14 e auditado por Codex no mesmo dia. A alteracao local em `root/riocarta_agente_master.py` foi revertida ao estado remoto conhecido porque envolvia `.py` operacional e nao passou por proposta, revisao e validacao da Trindade. O conteudo abaixo fica preservado como proposta historica, nao como estado vivo.

Contexto: Miguel pediu para garantir que todas as pautas viessem com a categorização regional e temática correta. Ao analisar o código, descobrimos que o coletor (`riocarta_robo_coleta.py`) já tentava sugerir categorias granulares, mas o publicador (`riocarta_agente_master.py`) estava forçando um fallback para categorias genéricas antigas herdadas do Cafezinho (como "Política", "Economia", "Tecnologia").

Correções:
- `root/riocarta_agente_master.py`: Atualizadas as `categorias_permitidas` para refletirem as 17 seções oficias definidas em `rjTaxonomy.ts` (ex: "Região dos Lagos", "Sul Fluminense e Costa Verde", "Segurança Pública", etc).
- Implementada lógica de "override" mais inteligente: se o LLM alucinar, o sistema varre o título/tags buscando cidades, bairros ou temas (ex: "búzios", "cabo frio" -> Região dos Lagos; "assalto", "pm" -> Segurança Pública) em vez de jogar tudo em "Política".
- O prompt do sistema no `riocarta_agente_master.py` foi atualizado para instruir o LLM a escolher estritamente uma destas 17 categorias.

Auditoria Codex 2026-05-14 12:39 BRT:
- Droplet `root@159.89.185.209` nao recebeu esta mudanca; `/root/riocarta_agente_master.py` ainda estava no estado anterior.
- Backup do estado local nao autorizado: `Backups/riocarta_agente_master.py.bak_pre_ag_categorias_quarantine_20260514_1239_codex_ag_categorias`.
- Backup deste indice antes da nota de auditoria: `Backups/CEREBRO_INDEX_RIOCARTA.md.bak_pre_ag_categorias_audit_20260514_1239_codex_ag_categorias`.
- Rollback da contencao, se Miguel autorizar a proposta depois de revisao: reaplicar o diff preservado no backup e rodar `python3 -m py_compile root/riocarta_agente_master.py` antes de qualquer deploy.

## OPERACAO-20260515-RIOCARTA-HERO-FALLBACK-CODEX

Status: aplicado localmente em 2026-05-15 12:18 BRT.

Contexto: o publicador local do Rio Carta (`root/riocarta_smoke_markdown.py`, chamado pelo cron local no minuto 05) estava rejeitando pautas quando `og:image`/`twitter:image` da fonte falhava. Miguel reforcou que todo post deve continuar com imagem; portanto a correcao nao relaxa `heroImage`.

Correcoes:

- `root/riocarta_smoke_markdown.py`: request de imagem/fonte agora usa timeout curto de 5s.
- `heroImage` continua obrigatorio.
- Camada 1: tenta imagem real da fonte.
- Camada 2: se a fonte falhar, reaproveita imagem local segura existente em `rio_carta/public/hero/`.
- Camada 3: se nao houver fallback local, chama o gerador editorial, que tenta banco de midia real e Qwen Image/Alibaba como ultimo fallback.
- Se todas as camadas falharem, a pauta continua bloqueada.

Validacoes:

- `python3 -m py_compile "Rio Carta Agentes/root/riocarta_smoke_markdown.py"` OK.
- `python3 -m json.tool "Rio Carta Agentes/root/config/riocarta_imagem_ia.json"` OK.
- Smoke de fallback local retornou `/hero/...` com status `sem og:image; fallback local: ...`.
- Smoke real sem fila (`python3 "Rio Carta Agentes/root/riocarta_smoke_markdown.py" 1`) gerou 1 draft com `heroImage` e `puladas: []`.

Backup:

- `Projeto Cafezinho Agentes/Backups/riocarta_smoke_markdown.py.bak_pre_hero_fallback_20260515_121811_codex`

Rollback:

```bash
cd "/home/migueldorosario/Downloads/Antigravity Google"
cp "Projeto Cafezinho Agentes/Backups/riocarta_smoke_markdown.py.bak_pre_hero_fallback_20260515_121811_codex" "Rio Carta Agentes/root/riocarta_smoke_markdown.py"
python3 -m py_compile "Rio Carta Agentes/root/riocarta_smoke_markdown.py"
```


## [2026-05-15 13:39 BRT] Recuperacao Rio Carta: site publicou, mas arquitetura ainda hibrida

Fato indexado: Rio Carta nao esta 100% remoto na pratica. O Droplet coleta pautas, mas o publicador Astro/Markdown ainda roda por cron local. Em 15/05, Miguel percebeu que novas reportagens nao apareciam. Codex encontrou `git push` rejeitado por remoto mais novo; por isso a rodada local nao chegou ao GitHub/Vercel.

Correcao feita: nova rodada publicada, commit GitHub `68d9e26`, deploy Vercel `dpl_9ByWwg9gxQ7PZugGXQJYxZLSrYfc`, site `https://www.riocarta.com` validado, URL singular com HTTP 200 validada.

Pendencias indexadas: migrar publicador para remoto; tratar push rejeitado antes de confirmar publicacao; configurar deploy Vercel remoto confiavel; ordenar capa por data real de publicacao; corrigir `og:image` para usar imagem destacada real; manter auditoria de categoria/imagem/data.

Regra operacional: Antigravity pode continuar visual/menu/arquitetura; Codex fica responsavel por codigo, deploy e correcoes tecnicas. Nao tocar em alteracoes visuais do Antigravity sem necessidade explicita.


## [2026-05-15 13:52 BRT] Rio Carta - sprint publicador remoto real, bloqueado por SSH

Codex iniciou migracao do publicador para o Droplet. Commits GitHub: `06c4699` modo remoto sem push + deploy Vercel; `2745492` retomada da publicacao automatica; `00fa444` fila com arquivo ausente nao derruba mais ciclo. Droplet recebeu clone em `/root/riocarta_remote/rio_carta`, symlink para `/root`, dependencias npm, credencial Vercel CLI e script `/root/riocarta_publicador_remoto.sh`. Vercel autenticou como `migueldorosario1`.

Teste remoto achou bug de fila ausente e abortou antes de publicar; bug corrigido no GitHub. Antes de puxar a correcao e ligar cron, SSH para `root@159.89.185.209` passou a rejeitar chave local. Estado final: publicador remoto parcialmente instalado, mas cron remoto nao ligado e cron local nao desligado. Nao considerar concluido ate recuperar SSH, rodar smoke e validar producao.


## [2026-05-15 14:09 BRT] Incidente SSH Droplet Rio Carta: chave recuperada via scratch historico

Bloqueio: durante sprint do publicador remoto, SSH para `root@159.89.185.209` falhou com `Permission denied (publickey,password)`. Causa operacional: Codex testou chaves locais, mas nao consultou primeiro o Cerebro/scratch historico. Miguel cobrou a busca.

Solucao encontrada: busca por `159.89.185.209`, `Droplet`, `ssh`, `chave`, `id_ed25519` encontrou `Projeto Cafezinho Agentes/scratch/scratch_ssh.py`, arquivo historico do Antigravity que documentava o bootstrap do Droplet e a instalacao de chave publica.

Chave publica operacional visivel: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFfXIj3Has1WDRbn95V89g/YpJ6tSXIu3CF3yB9vTbHm migueldorosario@novo`. Fingerprint: `256 SHA256:wB+pG1u1dDKyxP9bQSRDIzl+4Uxj6QD45Px6AL/dQqI migueldorosario@novo (ED25519)`. Comando recomendado: `ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209`.

Regra: nao copiar senhas de recuperacao para Cerebro/canal/forum. O scratch pode ser usado como pista sensivel por agente autorizado. Forum completo: `Rio Carta Agentes/Foruns/forum_riocarta_ssh_droplet_20260515.md`.

Resultado: chave publica reinstalada no Droplet; SSH voltou a funcionar (`ssh-ok`, host `agente-clone-01`). Atraso registrado; proximo passo e smoke final do publicador remoto antes de ligar cron.


## [2026-05-15 14:43 BRT] Rio Carta: smoke remoto real passou, mas push GitHub remoto ainda falta

Codex recuperou SSH do Droplet `159.89.185.209`, reconstruiu clone em `/root/riocarta_remote/rio_carta`, instalou Node 22/npm e dependencias Python. `/root/riocarta_remote_publish.sh` rodou no Droplet: gerou pauta, auditou, reteve materias ruins, rebaixou materia antiga que perdeu consenso, buildou Astro com 2814 paginas e criou commit local `cdc64c9` com 9 materias.

Vercel direto do Droplet nao e viavel no estado atual: falhou por limite `api-upload-free` e depois processo foi morto com `--archive=tgz`. Rodada foi publicada por ponte local: patch do commit remoto aplicado em clone limpo e push GitHub como `72bdeb1`; Vercel ficou Ready; URL validada em producao com HTTP 200.

Estado: remoto operacional ate commit/build, mas ainda nao autonomo end-to-end. Falta credencial de push GitHub no Droplet. Cron remoto NAO ligado; cron local NAO desligado. Proximo sprint: deploy key dedicada write para `migueldorosario1/rio-carta`, mudar script para `git push origin main`, remover `vercel deploy` direto e so entao ligar cron remoto.

## [2026-05-15 14:55 BRT] Rio Carta - infraestrutura remota e pausa geral
Codex registrou que o Rio Carta está com crons locais e remotos pausados durante a correção de infraestrutura. A deploy key GitHub do Droplet está funcional, o script remoto foi ajustado para publicar por GitHub/Vercel, e o próximo passo é teste manual pequeno antes de religar cron.

## [2026-05-15 15:01 BRT] Aprendizado de infraestrutura reutilizável - Rio Carta como laboratório
O Rio Carta está sendo usado como laboratório para uma infraestrutura replicável em futuros sites automáticos. Aprendizados desta virada:

- Nunca deixar publicador local e remoto ativos ao mesmo tempo. Antes da virada, pausar cron local de publicação e coleta para evitar duplicidade e corrida de commits.
- O caminho correto para Vercel é GitHub -> Vercel, não upload direto do Droplet pelo CLI da Vercel. O upload direto bateu limite/free upload e memória; GitHub/Vercel é mais estável.
- Todo Droplet publicador precisa de deploy key GitHub read/write própria, documentada por fingerprint, e teste  antes de cron.
- Antes de religar cron, rodar teste manual pequeno ( ou ) para validar coleta, geração, auditoria, commit, push e deploy.
- Ambiente remoto precisa ter dependências Python explícitas. Hoje faltava ; isso derrubou a cadeia LLM no primeiro teste. Dependências devem entrar em checklist/provisionamento.
- O publicador deve abortar se o repositório remoto estiver sujo; se houver sujeira de teste, guardar patch/status em backup e alinhar ao GitHub antes de rodar cron.
- O Rio Carta deve permanecer como ambiente de teste controlado para arquitetura que depois pode ser promovida ao Cafezinho ou a novos sites.

Estado durante registro: teste manual remoto ainda em andamento; crons locais e remotos seguem pausados até validação final.


## [None] Correção de registro - aprendizado de infraestrutura Rio Carta
Registro limpo, sem interpretação indevida de comandos pelo shell.

O Rio Carta está sendo tratado como laboratório para uma infraestrutura replicável em futuros sites automáticos. Aprendizados consolidados:

- Não deixar publicador local e remoto ativos ao mesmo tempo. Antes da virada, pausar cron local de publicação e coleta para evitar duplicidade e corrida de commits.
- O caminho preferencial para deploy é GitHub para Vercel. Upload direto do Droplet pela CLI da Vercel apresentou limite de upload e risco de memória.
- Todo Droplet publicador precisa de deploy key GitHub read/write própria, com fingerprint documentado e teste seco de push antes de cron.
- Antes de religar cron, rodar teste manual pequeno, com 1 ou 3 matérias, para validar geração, auditoria, commit, push e deploy.
- Ambiente remoto precisa de dependências Python explícitas. Hoje faltava o pacote Python usado pelo roteador OpenAI-compatible; isso derrubou a cadeia LLM no primeiro teste e foi corrigido com pacote de sistema.
- O publicador deve abortar se o repositório remoto estiver sujo. Se houver sujeira de teste, guardar patch/status em backup e alinhar ao GitHub antes de rodar cron.
- Rio Carta fica como campo de prova controlado para arquitetura que depois pode ser reaproveitada no Cafezinho ou em novos sites.

Estado no momento deste registro: teste manual remoto ainda em andamento; crons locais e remotos continuam pausados até validação final.

## [2026-05-15 15:02 BRT] Correção de carimbo
O bloco anterior de aprendizado pode ter saído com carimbo nulo por variável de ambiente ausente. Este é o carimbo correto do registro de infraestrutura replicável Rio Carta.


## [] Rio Carta - cron remoto religado em modo controlado
Estado final desta etapa:

- Crons locais do computador do Miguel continuam pausados para Rio Carta: sem coleta local e sem publicação local.
- Droplet voltou a coletar remotamente: a cada 30 minutos de dia e a cada 1 hora na madrugada, usando Python do sistema.
- Droplet passou a publicar remotamente às 23 de cada hora, com trava anti-sobreposição por flock.
- Publicador remoto começou em modo cauteloso: lote de 3 matérias por hora, até observar estabilidade.
- GitHub deploy key do Droplet está funcional e o caminho correto é Droplet -> GitHub -> Vercel.
- Foi feito teste manual real: houve build, push para GitHub e publicação de 1 matéria. O ciclo confirmou que o caminho remoto publica de verdade.
- Correções feitas antes do religamento: dependência Python OpenAI-compatible instalada; re-auditoria de matérias já publicadas separada do publicador; fila agora prioriza itens com carimbo mais recente; grupos de categorias também são ordenados por frescor.
- Pendências observadas: muitos avisos de imagem pequena em matérias antigas; fila ainda contém material legado; vigia/auditoria de antigos deve rodar separado do publicador normal.

Backup do crontab remoto antes do religamento: /root/crontab_backup_pre_religa_riocarta_remote_20260515_182014.txt.

## [2026-05-15 15:20 BRT] Correção de carimbo - cron Rio Carta religado
Este é o carimbo correto do registro imediatamente anterior: cron remoto Rio Carta religado em modo controlado, local pausado, coleta remota ativa e publicador remoto às :23 com lote 3/h.


## [] Rio Carta - limpeza da fila operacional
Miguel pediu para limpar a fila e remover velharia/lixo. Resultado no Droplet:

- Fila original: 560 itens.
- Mantidos na fila operacional: 0.
- Removidos da fila: 560.
- Motivos:
  - 62 já publicadas; não devem ficar na fila operacional.
  - 5 sem data; legado sem carimbo.
  - 318 de 13/05; legado antigo retirado da fila para não travar o cron.
  - 175 fantasmas; estavam na fila mas o arquivo não existia no repositório remoto.

Importante: a limpeza removeu itens da fila operacional, não apagou posts publicados. O legado removido foi documentado em `tools/quarentena_fila_riocarta/` no repositório Rio Carta. Commit remoto: `7db8632 Clean Rio Carta publication queue`.

Estado após limpeza: fila operacional zerada. Coletador remoto segue ligado e deve repovoar a fila com material novo; publicador remoto às :23 só publica se houver item fresco na fila.

## [2026-05-15 15:33 BRT] Coleta Rio Carta validada
A coleta remota voltou a funcionar após correção de scripts/caminhos e dependências. Teste manual salvou 16 pautas. Há qualidade suficiente nos itens de segurança/política local, mas foi detectado ruído de classificação regional em parte do O Fluminense; registrar para sprint de refinamento de fontes/filtros.


[2026-05-15 16:11 BRT] Codex -> Trindade/Rio Carta: estado consolidado. Infra remota OK: Droplet acessivel, crons ativos, publicador remoto as :23, coleta 30/30 de dia e 1h madrugada. Publicacao real confirmada as 15:23 BRT: commit `d9f4245` publicou 3 materias e build Astro/GitHub completou. Coleta confirmada as 15:30 BRT: 16 pautas salvas no banco/inbox, com boas pautas de seguranca/politica local. Correcoes aplicadas: `riocarta_agente_master.py` recebeu alias correto para o roteador (`agente_roteador_llm = riocarta_agente_roteador_llm`) e compila local/remoto. DeepSeek vivo agora e V4 Pro nos caminhos corrigidos; grep vivo sem `deepseek-chat` fora de backups/logs. Pendencias: smoke do master mostra V4 Pro lento; uma rodada manual nao terminou dentro de 3-4min e morreu por timeout externo durante revisao final. Fila operacional esta zerada depois do ultimo publish; o proximo publish deve rodar smoke_markdown antes de publicar. Monitorar as 16:23 BRT se a fila repovoa e publica; se nao, corrigir ponte banco/inbox -> markdown/queue.


[2026-05-15 16:24 BRT] Codex -> Trindade/Rio Carta: bug confirmado no Rio Carta. O site publico mostrava posts antigos porque o gerador `riocarta_smoke_markdown.py` escrevia rascunhos em `/rio_carta`, fora do clone real `/root/riocarta_remote/rio_carta`. Corrigi para respeitar `RIOCARTA_ASTRO_DIR` e ajustei `/root/riocarta_remote_publish.sh` para exportar esse caminho. Tambem subi timeout DeepSeek V4 Pro: 45s, `max_retries=0`, sem repetir o mesmo `deepseek-v4-pro` duas vezes; fallback segue Kimi/Qwen/Zhipu/Mistral. Vou rodar nova rodada controlada e validar no dominio publico.


## 2026-05-15 17:01 BRT - Bug de thumb social resolvido

Rio Carta: corrigido bug em que a imagem principal da materia aparecia no post, mas a imagem de compartilhamento (`og:image`/`twitter:image`) caia no placeholder. Causa: `BlogPost.astro` nao passava `heroImage` para `BaseHead`. Correcao em `src/components/BaseHead.astro` e `src/layouts/BlogPost.astro`, commit `89075f4 Fix Rio Carta social share image`, validado em producao no dominio `www.riocarta.com`. Regra: todo layout de post deve passar explicitamente a imagem principal para os metadados sociais.


## 2026-05-15 17:16 BRT - Aprendizados da auditoria Rio Carta

A auditoria estava parcialmente invertida: em vez de ajudar, estava segurando publicacao por falso positivo. Erros observados em producao:
- DeepSeek V4 Pro as vezes retorna sem JSON util na auditoria. Isso agora vira falha tecnica, nao veto.
- Kimi chegou a responder apenas `curto`; isso agora vira voto fraco, nao aprovacao.
- Qwen gerou falsos positivos: disse que Banco Master nao existe, tratou timestamp de arquivo/imagem como prova factual, confundiu 11/04/2026 como futuro diante de 15/05/2026 e errou dia da semana de 14/05/2026.
- Regra antiga `mais de 3 votos` fazia um veto isolado derrubar materia mesmo com fonte citada e checagens locais boas.

Nova regra: auditoria ajuda. Bloqueio automatico so por falha local critica ou dois vetos externos consistentes. Veto isolado vira anotacao para revisao, nao trava. Commit da correcao: `eda6d78 Make Rio Carta audit advisory`. Rodada controlada posterior publicou 3 materias novas no commit `9ae2c31`.

Novo erro a corrigir depois: `riocarta_confirm_published.py` informou `Nenhuma URL de fonte encontrada para confirmar`, ou seja, o pos-check de fonte esta cego apesar das fontes existirem no corpo Markdown.

## 2026-05-15 17:19 BRT - Memoria: Rio Carta ainda tem sobras WordPress/Cafezinho

Estado operacional: coleta e publicacao Rio Carta foram pausadas no Droplet por ordem do Miguel enquanto os sprints continuam. Backup do crontab remoto: `/root/crontab_riocarta_pre_pause_20260515_201811.bak`. Trava: `/root/riocarta_remote/rio_carta/tools/riocarta_publish_paused.txt`.

Aprendizado: o Rio Carta novo e Astro/Markdown/Vercel, mas alguns agentes foram copiados de fluxos Cafezinho/WordPress e ainda nao estao completamente adaptados.

Achados vivos:
- Tribunal Visual Qwen/Alibaba existe e possui prompt proprio do Rio Carta.
- `riocarta_gerenciador_imagens.py` ja usa Qwen para julgar imagens do banco.
- `riocarta_agente_master.py` ainda chama Gemini Vision no Tribunal Visual.
- `riocarta_gerenciador_imagens.py` ainda contem upload/figcaption via WordPress.
- `riocarta_interlink_interno.py` ainda consulta WordPress REST API para achar posts.
- `riocarta_confirm_published.py` nao esta extraindo fonte corretamente dos Markdown publicados.

Regra de arquitetura: Rio Carta deve usar caminhos nativos Astro/Markdown para publicacao, imagem, interlink e confirmacao. WordPress so pode existir como legado isolado, explicitamente desativado ou nomeado como legado. Tribunal Visual do Rio Carta deve priorizar Qwen/Alibaba; Gemini nao deve ser caminho principal.

## 2026-05-15 17:54 BRT - Operacao: crons Rio Carta religados

Miguel autorizou voltar o cron do Rio Carta. Coleta rotativa e publicador remoto foram religados no Droplet. Backup do crontab pausado: `/root/crontab_riocarta_pre_resume_20260515_205425.bak`. Trava de pausa foi arquivada como `/root/riocarta_remote/rio_carta/tools/riocarta_publish_paused_20260515_205425.txt`.

Linhas vivas:
- coleta dia: `0,30 0-2,9-23 * * * ... /root/riocarta_cron_rotativo.sh`
- coleta madrugada: `0 3-8 * * * ... /root/riocarta_cron_rotativo.sh`
- publicador: `23 * * * * ... /root/riocarta_remote_publish.sh`

Monitorar nos próximos ciclos se coleta repovoa banco/fila e se publicador transforma só matérias boas em Markdown publicado.

### 2026-05-15 18:02 BRT — Loop Trindade passa a monitorar Rio Carta
- Codex loop local: ativo em , auto-stop ate 2026-05-16 18:02 BRT.
- Prompt do tick atualizado para incluir Rio Carta em todo ciclo, alem de canal, Telegram e Transkriptor.
- Droplet Rio Carta: wrapper  recebeu autocura para ignorar/restaurar log gerado , que sujava o clone e podia bloquear publicacao.
- Backup remoto do wrapper: .
- Clone remoto atualizado ate  para incorporar header/menu/ajustes visuais recentes antes da proxima publicacao automatica.

### 2026-05-15 18:05 BRT — Correcao canonica do loop Rio Carta
- Loop local Codex ativo em 30/30min nos minutos :15/:45; auto-stop ate 2026-05-16 18:02 BRT.
- Prompt do tick Codex atualizado para monitorar Rio Carta, Telegram/Augusto e Transkriptor em todo ciclo.
- Droplet Rio Carta: /root/riocarta_remote_publish.sh corrigido para nao abortar por log gerado logs/rio_carta_zelador_destaques.log.
- Backup remoto do wrapper: /root/riocarta_remote_publish.sh.bak_pre_generated_log_clean_20260515T210205Z_codex.
- Clone remoto atualizado ate d252340 antes da proxima publicacao automatica.
- Observacao: registro das 18:02 BRT ficou parcialmente sem caminhos/commits por problema de aspas; este bloco substitui a referencia operacional.

### 2026-05-15 18:33 BRT — Monitoramento Rio Carta pos-religacao + base Sprint 2
- Coleta remota viva: ciclos confirmados em 19:00, 19:30, 20:00, 21:00 e 21:30 UTC. O erro inicial de lock com barra em `Niteroi/Metropolitana` nao repetiu no ciclo das 21:30 UTC.
- Publicador remoto das 21:23 UTC/18:23 BRT concluiu: build Astro OK, 2905 paginas geradas, push `18f73ef Publish Rio Carta hourly batch (3)` para `origin/main`.
- Materias publicadas no ciclo: `smoke-202605152123-itaborai-193-anos...`, `smoke-202605152123-em-partida-contra-sao-paulo-fluminense...`, `smoke-202605152123-data-centers-ai-and-the-social-costs...`.
- Validacao publica 18:34 BRT: homepage de `www.riocarta.com` ja expunha slugs `smoke-202605152123-*`, incluindo `Itaboraí 193`; Vercel do commit `18f73ef` entrou no ar.
- Residuo a monitorar: clone remoto ficou com rascunhos/arquivos nao rastreados (`smoke-202605152007-*`, novos `smoke-202605152123-*`, `logs/generated-backups/` e trava pausada arquivada). Nao bloqueou o push, mas pode virar sujeira operacional se acumular.
- Co-vigilancia: verificador de integridade criticos segue `DRIFT` apenas em `root/agente_roteador_llm.py`, coerente com fix recente Anthropic fallback; sem novo `AG-VIOLATION`.
- Sprint 2 menu/categorias: fonte validada e oficial e o TSE Dados Abertos 2024. CSV `votacao_candidato_munzona_2024_RJ.csv` permite extrair 92 municipios e 1208 vereadores eleitos filtrando `CD_CARGO=13` e `DS_SIT_TOT_TURNO` com eleitos, agregando por `SQ_CANDIDATO`. Para prefeitos, `CD_CARGO=11` retornou 91 no 1o turno; falta tratar municipio com 2o turno/eleicao suplementar antes de versionar dados finais.


## [2026-05-15 19:23 BRT] Codex - Conflito de coordenacao contido: idioma/publicacao x menu/vereadores

- O conflito real nao foi um merge quebrado: foi sobreposicao de frentes.
- Frente publicacao/idioma no Droplet: fechada no remoto com `06f954a` e `9ed6711`.
  - `06f954a` adiciona trava para nao publicar materia em ingles/nao traduzida.
  - `9ed6711` restaura 3 materias RioOnWatch ja traduzidas para PT-BR.
  - A materia Data Centers segue escondida porque continua em ingles.
- Backup operacional antes do ajuste: `/root/Backups/riocarta_language_guard_20260515T220815Z/`.
- Build remoto validado: 3088 paginas, concluido as 22:17 UTC.
- Frente menu/vereadores: esta no working tree local, separada da publicacao remota. Build local validou 3064 paginas as 19:22 BRT, mas ainda nao deve ser misturada com a frente de publicacao sem novo alinhamento no canal.
- Regra aprendida: Rio Carta agora tem mais de uma frente simultanea; antes de build/push, registrar frente, dono e escopo no canal para Claude/Antigravity nao repetirem ou sobrescreverem trabalho.

## [2026-05-15 19:24 BRT] Sprint 2 menu - vereadores RJ via TSE oficial

Codex destravou o Sprint 2 de hiperlocalizacao do menu de Câmaras de Vereadores usando dados oficiais do TSE, sem LLM para nomes de políticos locais.

Arquivos vivos no repo Astro:
- `scripts/gerar_vereadores_rj_tse.py`
- `src/data/vereadores_rj.json`
- `src/components/Header.astro`

Fonte: `https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2024.zip`, arquivo `votacao_candidato_munzona_2024_RJ.csv`.

Critério de geração:
- `CD_CARGO=13` (vereador);
- `DS_SIT_TOT_TURNO` em `ELEITO POR QP` ou `ELEITO POR MÉDIA`;
- agregação por `SQ_CANDIDATO` para remover duplicidade por zona eleitoral;
- soma de `QT_VOTOS_NOMINAIS_VALIDOS` por candidato;
- saída com cidade, slug da cidade, nome de urna, slug, partido, número, situação e votos.

Resultado validado: `92` municípios e `1208` vereadores eleitos. Exemplos de sanity: Angra dos Reis `15`, Rio de Janeiro `51`, Rio das Ostras `15`.

Menu: `Header.astro` importa o JSON e popula o submenu `Câmaras de Vereadores` por região/cidade. Para não estourar o DOM visual, cada cidade mostra até 18 vereadores e, quando houver mais, um link `+N vereadores` aponta para a tag da câmara municipal.

Commit: `17372ef Rio Carta: add TSE councilors menu data`, enviado ao `origin/main`.

Validação:
- `python3 -m json.tool src/data/vereadores_rj.json` OK;
- `python3 -m py_compile scripts/gerar_vereadores_rj_tse.py` OK;
- `PATH=$HOME/.nvm/versions/node/v22.22.2/bin:$PATH npm run build` OK, `3064` páginas.

Rollback:

```bash
cd "Rio Carta Agentes/rio_carta"
git revert 17372ef
git push origin main
```

Observação operacional: o publicador remoto das `19:23 BRT` acordou quase ao mesmo tempo do push local; no momento do registro, ele ainda rodava `riocarta_smoke_markdown.py 15 --queue` sob flock no Droplet. Próximo tick deve confirmar término/publicação e alinhar o clone remoto ao commit `17372ef` se necessário.


## [2026-05-15 19:42 BRT] Codex - BUG Rio Carta: titulo repetido dentro do post

Caso apontado por Miguel: post UFF (`smoke-202605151805-eleicoes-na-uff-roberto-salles-e-luciana-freitas-chegam-ao-segundo-turno-com-ampla-vantagem`) aparecia com o titulo do Astro e o mesmo titulo repetido como primeira linha do corpo.

Correcoes no remoto/GitHub:
- `ce852d5` remove a repeticao no post ja publicado.
- `ce852d5` adiciona limpeza estrutural no publicador: se o primeiro bloco do corpo for igual ao titulo, ele e removido antes de publicar.
- A description tambem passa a remover prefixo igual ao titulo, evitando cards/metadados redundantes.
- Build remoto passou: 3107 paginas.

Aprendizado: o erro veio no Markdown gerado, nao no template do site. O template so exibiu o titulo normal; o corpo ja vinha com o titulo colado no inicio.


## [2026-05-15 19:47 BRT] Codex - Observacao Vercel apos correcao de titulo duplicado

Commit `ce852d5` esta no GitHub com a correcao do post UFF e a trava estrutural do publicador. Build local/remoto passou.

Tentativa de deploy manual pelo Vercel CLI foi interrompida por limite de upload gratuito: `Too many requests - try again in 24 hours (more than 5000, api-upload-free)`. O CLI sugeriu `--archive=tgz`, mas nao forcei de novo para nao piorar a cota.

Situacao: codigo corrigido e push feito; dominio ainda pode servir cache/deploy anterior ate o deploy automatico do GitHub/Vercel processar o commit novo. Pendencia futura: reduzir tamanho/upload do projeto no Vercel ou ajustar fluxo de deploy para nao enviar centenas de MB a cada emergencia.


## [2026-05-15 19:49 BRT] Codex - Validacao publica do post UFF

O deploy automatico do Vercel processou o commit `ce852d5`. Validacao por HTTP no post publico:
- titulo duplicado no corpo: ausente
- corpo agora comeca pelo subtitulo `Chapa 2 lidera a disputa...`
- `last-modified` do Vercel: 2026-05-15 22:48:58 UTC

Conclusao: bug corrigido no post e regra estrutural ativa no publicador.


## [2026-05-15 20:17 BRT] Codex - Autocura Git do publicador remoto

No tick 20:15, o log remoto mostrou que o publicador das `19:23 BRT` buildou `3107` paginas, mas o `git push origin main` falhou com `fetch first`. Causa: o remoto ja tinha recebido `0a4e57a` e `ce852d5` enquanto o cron tentava publicar.

Estado encontrado no Droplet:
- clone `/root/riocarta_remote/rio_carta` ja estava em `ce852d5`, alinhado com `origin/main`;
- nao havia diff rastreado;
- havia `39` itens nao rastreados, incluindo `36` Markdown de rascunhos `draft: true` e backups/logs gerados.

Autocura aplicada:
- backup remoto de todos os untracked: `/root/backups_riocarta_remote_publish/untracked_pre_clean_20260515T231714Z.tar.gz`;
- lista de arquivos preservada em `/root/backups_riocarta_remote_publish/untracked_pre_clean_20260515T231714Z.txt`;
- limpeza apenas dos nao rastreados, sem `force push`, sem mexer em commits e sem publicar rascunhos;
- `git status --short --branch` ficou `## main...origin/main`.

Rollback da limpeza:

```bash
ssh root@159.89.185.209
cd /root/riocarta_remote/rio_carta
tar -xzf /root/backups_riocarta_remote_publish/untracked_pre_clean_20260515T231714Z.tar.gz
git status --short --branch
```

Licao: depois de erro `fetch first`, primeiro verificar se o remoto ja absorveu o commit por outra via. Se estiver alinhado e restarem apenas rascunhos untracked `draft: true`, arquivar em tar e limpar; nao commitar rascunho antigo automaticamente.

## [2026-05-15 20:40 BRT] Codex - Publicador remoto recuperado

A rodada seguinte do cron remoto (`20:23 BRT`) completou:
- build Astro OK: `3086` paginas;
- push OK: commit `cc997fc Publish Rio Carta hourly batch (3)`;
- publicadas: `moraes-autorizou-arrombamento-de-cofres-na-casa-de-claudio-castro`, `menina-de-12-anos-denuncia-estupro-coletivo-e-espancamento-na-zona-oeste`, `predio-so-para-airbnb-sem-moradia-flamengo-tera-predio-exclusivo-para-aluguel-de-temporada`;
- homepage publica ja mostra os tres slugs `smoke-202605152323-*`.

Pós-rodada, o script deixou 15 itens operacionais sujos (rascunhos `draft: true`, imagens de rascunho e dois ajustes em drafts antigos). Codex arquivou tudo em `/root/backups_riocarta_remote_publish/dirty_after_cc997fc_20260515T234012Z.tar.gz` e limpou o worktree. Estado final remoto: `## main...origin/main`.

Pendência conhecida ainda aberta: `riocarta_confirm_published.py` continua retornando `Nenhuma URL de fonte encontrada para confirmar`; isso não bloqueou publicação, mas precisa de sprint próprio para mapear campos reais de fonte.


## [2026-05-15 22:58 BRT] Codex - Instalação da autocura Rio Carta V1

Resposta à pergunta do Miguel: o Rio Carta já tinha autocuras pontuais dentro do publicador e um módulo simples `riocarta_autocura_licoes.py`, mas **não tinha agente dedicado de autocura equivalente ao Cafezinho**. Também havia uma pendência antiga de autocura incompleta/sem registro de lições.

### Erros catalogados pelo histórico do publicador

- `fila_arquivo_ausente`: centenas de ocorrências; fila apontava para Markdown que já não existia no clone.
- `imagem_destacada_pequena`: recorrente; imagens abaixo do mínimo seguraram ou sujaram auditoria.
- `auditor_temporal`: Qwen/LLMs deram muitos alertas de data/dia da semana, alguns úteis e outros falsos positivos.
- `auditor_veto_outro`: vetos semânticos diversos, ainda não devem ser autocurados sem revisão.
- `warning_titulo_longo`: títulos longos recorrentes.
- `warning_materia_em_ingles/nao_traduzida`: trava de idioma atuando sobre RioOnWatch e similares.
- `confirmador_fonte_cego`: `riocarta_confirm_published.py` ainda falha com `Nenhuma URL de fonte encontrada para confirmar`.

### O que foi instalado

- Novo agente: `root/riocarta_autocura.py`.
- Livro de lições ampliado: `root/riocarta_autocura_licoes.py` agora registra histórico, lições recentes e bloco pendente para Cérebro.
- Publicador remoto: `/root/riocarta_remote_publish.sh` agora chama `python3 /root/riocarta_autocura.py --apply --before-publish` antes do zelador/smoke/publicação.

### Curas automáticas V1

- Remove da fila itens cujo Markdown não existe mais.
- Remove título repetido como primeiro parágrafo do corpo.
- Remove prefixo de título repetido na description.
- Troca fonte placeholder por nome derivado do domínio quando possível.
- Se uma matéria obviamente em inglês estiver `draft: false`, rebaixa para `draft: true`.
- Não usa LLM, não mexe em crontab, não faz deploy manual e não usa force-push.

### Validação

- `py_compile` OK local e remoto.
- Dry-run remoto OK.
- Instalação no Droplet OK; wrapper mostra chamada ativa na linha `59`.
- Rodada aplicada corrigiu 9 matérias recentes com repetição de título/description e identificou 88 referências quebradas de fila. Build Astro validou `3083` páginas.

### Limites conscientes

Esta V1 não substitui a autocura completa do Cafezinho. Ela é uma camada mecânica e segura. Erros semânticos, imagem contextualmente errada, fact-check político e auditoria temporal ambígua ficam catalogados para sprint próprio.

## [2026-05-15 23:03 BRT] Codex - Autocura Rio Carta: log fora do repositório

Lição operacional: logs de autocura não devem ficar dentro do clone Astro do Rio Carta, porque isso deixa o `git status` sujo e pode atrapalhar diagnóstico de publicação.

Correção aplicada: o log padrão da autocura passou de `rio_carta/logs/riocarta_autocura.jsonl` para `/root/agent_data/riocarta_autocura.jsonl`. O caminho pode ser alterado pela variável `RIOCARTA_AUTOCURA_LOG`.

## [2026-05-16 01:45 BRT] Codex - Agentes sociais Rio Carta V0

Miguel/Antigravity pediram agentes sociais próprios do Rio Carta, sem mexer no Cafezinho e usando apenas LLMs chinesas, com Mistral permitido como último fallback.

Entrega V0:

- `root/riocarta_social_common.py`
- `root/riocarta_agente_twitter.py`
- `root/riocarta_agente_instagram.py`
- contextos `social_twitter` e `social_instagram` em `root/config/riocarta_cascatas_llm.json`

Regra de segurança registrada: estes agentes não reutilizam postadores do Cafezinho e não publicam automaticamente em contas sociais nesta primeira versão. Eles leem as matérias Markdown publicadas do Rio Carta e criam rascunhos em `root/agent_data/riocarta_social_queue.json`.

Validação: `py_compile` local/remoto OK; um rascunho Twitter foi gerado com `qwen-plus`; um rascunho Instagram foi gerado com `deepseek-v4-pro`. Arquivos copiados para o Droplet em `/root/`; crontab não foi alterado.

## [2026-05-16 01:48 BRT] Pendência Miguel - acessos sociais Rio Carta

Miguel informou que ainda precisa fornecer os acessos próprios do Twitter/X e Instagram do Rio Carta. Enquanto isso não acontecer, os agentes sociais do Rio Carta devem permanecer em modo rascunho e não podem publicar diretamente.

Acessos necessários:

- Twitter/X Rio Carta: API Key, API Secret, Access Token, Access Token Secret e Bearer Token se houver.
- Instagram Rio Carta: conta profissional vinculada à página Facebook, Page ID, Instagram Business Account ID e Access Token da Meta com permissão de publicação.

Regra de segurança: não reutilizar credenciais sociais do Cafezinho no Rio Carta.

Nota de rotina: Miguel pediu que esta pendência seja lembrada amanhã no **Boletim News**.

## [2026-05-15 23:05 BRT] Codex - Confirmador de fonte corrigido + autocura versionada

O bug `riocarta_confirm_published.py` cego para fonte foi fechado. A regex estava correta; o problema era caminho: no Droplet, `/root/riocarta_remote/root` é symlink para `/root`, então `Path(__file__).resolve()` fazia o script procurar o blog em `/rio_carta/...`. O confirmador agora resolve o clone por `RIOCARTA_ASTRO_DIR`, depois pelo `cwd`, depois por `/root/riocarta_remote/rio_carta`.

Validação remota:
- `python3 -m py_compile /root/riocarta_confirm_published.py /root/riocarta_autocura_licoes.py` OK.
- `cd /root/riocarta_remote/rio_carta && python3 /root/riocarta_confirm_published.py smoke-202605160123-programacao-cultura-mistura-literatura-e-gastronomia-nesse-sabado-16-em-rio-das-ostras.md` retornou `Confirmadas 1 pauta(s) como publicado_markdown.`
- Build final após rebase em `fc4dc60`: `3267` páginas OK.

A autocura aplicada no Droplet foi versionada no GitHub como `e3a7922 Autocura Rio Carta cleanup duplicated titles and queue`, após rebase limpo sobre `fc4dc60 Rio Carta: fix 404 em /tags/camara-* e /tags/prefeitura-*`. O clone remoto terminou limpo/alinhado em `origin/main`.

Backups remotos principais:
- `/root/backups_riocarta_autocura/riocarta_confirm_published.py.bak_pre_autocura_20260516T014812Z_codex`
- `/root/backups_riocarta_autocura/diff_pre_commit_20260516T015545Z.patch`
- `/root/backups_riocarta_autocura/status_pre_commit_20260516T015545Z.txt`
- `/root/backups_riocarta_autocura/untracked_logs_20260516T015545Z.tar.gz`

Rollback:

```bash
cd /root/riocarta_remote/rio_carta
GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519_riocarta_github -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new" git revert e3a7922
GIT_SSH_COMMAND="ssh -i /root/.ssh/id_ed25519_riocarta_github -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new" git push origin main
cp /root/backups_riocarta_autocura/riocarta_confirm_published.py.bak_pre_autocura_20260516T014812Z_codex /root/riocarta_confirm_published.py
python3 -m py_compile /root/riocarta_confirm_published.py
npm run build
```

## [2026-05-16 13:51 BRT] Página teste do novo header

Sprint visual isolada para validar novo header com seis macroeditorias visíveis: Geral, Política, Lazer, Segurança, Economia e Serviços.

- Link público: https://www.riocarta.com/teste-header-novo/
- Fórum: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_pagina_teste_header_20260516.md`
- Commit: `5e048ea Add isolated Rio Carta header test page`
- Arquivos tocados no Astro:
  - `src/components/HeaderTesteMacro.astro`
  - `src/pages/teste-header-novo.astro`
- Validação: build local OK (`3543` páginas) e URL pública HTTP 200.

Observação de segurança: não alterou o header real de produção, home, posts, publicadores, coletores, crons, `.py` ou filtros reais de macro-categoria. Rollback: `git revert 5e048ea && git push origin main`.
# Atualização 2026-05-16 16:33 BRT - Imagem destacada indevida / Tribuna de Petrópolis

Caso corrigido: post `Datafolha: Lula e Flávio lideram rejeição com 47% e 43%; Zema tem 15% e Caiado 13%` saiu com a logomarca da Tribuna de Petrópolis como imagem destacada.

Correção aplicada:
- post público passou a usar `/hero/smoke-smoke-202605160823-lula-ironiza-caso-de-flavio-bolsonaro-com-vorcaro.webp`;
- imagem ruim original preservada em backup local do repo Astro;
- build limpo validado após remover concorrência de build local;
- commit Astro relacionado: `a40a51b Fix Datafolha post hero image`;
- URL validada: `https://www.riocarta.com/blog/smoke-202605161823-datafolha-lula-e-flavio-lideram-rejeicao-com-47-e-43-zema-tem-15-e-caiado-13/`.

Lição operacional:
- imagem destacada que seja logo/cabeçalho/marca da fonte deve ser tratada como erro editorial grave;
- autocura atual ainda não detecta isso sozinha de forma completa, pois a regra anterior olhava principalmente dimensão/ausência;
- regra `logo_fonte_como_hero` foi registrada em `Rio Carta Agentes/root/riocarta_autocura_licoes.py` para orientar o próximo sprint estrutural: detectar logo da fonte, trocar por fallback visual seguro ou rebaixar para revisão quando não conseguir corrigir.
## [2026-05-19 16:52 BRT] Rio Carta — publicação destravada; gargalo real é Git/logs + autonomia incompleta

Diagnóstico Codex: o 403 em `/wp-json/wp/v2/posts` é endpoint legado e não é o caminho vivo de publicação. O Rio Carta atual publica por Astro/Markdown/GitHub/Vercel.

Causa real do bloqueio: `scripts/riocarta_publish_hourly_batch.mjs` tentava `git add` em logs ignorados (`logs/rio_carta_publication_audit.jsonl` e `logs/rio_carta_relatorio_bloqueios.md`), abortando o commit remoto.

Correção:
- `1ff1b1db Fix Rio Carta publish ignored logs`
- lote publicado via ponte local como `2ecd8740 Publish Rio Carta manual batch`
- URL validada HTTP 200: `https://www.riocarta.com/blog/smoke-202605191916-o-quinto-escalao-da-mafia-assumiu-o-governo-do-rio-diz-paes-sobre-crise-politica-no-estado/`

Estado honesto:
- coleta/build remoto funcionam;
- Droplet ainda não tem push GitHub funcional;
- Vercel CLI direto no Droplet não tem credencial;
- sprint aberto para reduzir rebuild Astro completo: `Projeto Cafezinho Agentes/Foruns/forum_sprint_astro_incremental_riocarta_20260519.md`.

## [2026-05-22 18:37 BRT] Fórum Planejamento e Redução de Ritmo de Publicação do Rio Carta

- **Fórum**: [forum_planejamento_publicacao_riocarta_20260522.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/Foruns/forum_planejamento_publicacao_riocarta_20260522.md)
- **Objetivo**: Solicitação formal de Miguel à Trindade (Claude / Codex) para reduzir o ritmo de publicação em ~50% no crontab remoto (Tencent VPS) para preservar tokens/custos, com foco no planejamento estratégico de qualidade e finalização da programação dos agentes sociais.

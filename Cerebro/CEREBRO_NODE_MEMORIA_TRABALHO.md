# CEREBRO_NODE_MEMORIA_TRABALHO.md — Memória de Trabalho da Trindade

**Atualizado:** 2026-06-12 23:30 BRT
**Por:** DeepSeek (Constituição art. 1-2) (acorde.sh unificado — 1 wake só + smoke operacional + protocolo de chaves)

---

## 📜 CONSTITUIÇÃO DA GRANDE REFORMA (2026-06-12)

> **Leis fundamentais do Sistema Cafezinho. Todas as IAs, agentes e engenheiros devem seguir.**

### Artigo 1 — Chaves e Credenciais

1. **Cofre único.** Um só `.env.unificado` por servidor. Sem duplicação.
2. **Espelhamento.** Local, Tencent, NYC e Alibaba idênticos entre si.
3. **Ponteiros, não cópias.** Nenhum script ou IA cria novo cofre.
4. **Backups são backups.** `legacy_*` é histórico, não fonte viva.
5. **Violação = incidente.** Registrado em fórum, auditado pela Trindade.

> 📁 `CEREBRO_NODE_COFRE_CHAVES.md` · Fórum: `Foruns/forum_unificacao_cofres_20260612.md`

### Artigo 2 — Comunicação

1. **Canal Trindade = ponteiro.** Cada entrada do canal é um link/resumo apontando para um fórum. O canal não é a memória.
2. **Fórum = memória.** Toda decisão, diagnóstico, deploy e incidente deve ter fórum dedicado. O fórum é a fonte de verdade histórica.
3. **Inbox = comunicação pessoal.** Usado para mensagens diretas entre engenheiros (ex: Codex → Kimi). Não substitui fórum. **Caminho canônico:** `Cerebro/Foruns/inbox_trindade/<agente>.md`.
4. **Cartinha humanizada.** Ao concluir uma missão, postar no canal um resumo em linguagem simples, com emojis, legível para o Miguel colar nos chats dos agentes. A cartinha complementa o fórum — não substitui.

> 📁 Fórum: `Foruns/forum_unificacao_cofres_20260612.md`

5. **Fórum geral indexa específicos.** Cada iniciativa (ex: Grande Reforma) tem um fórum-índice que linka para seus fóruns específicos. O Cérebro indexa o fórum-índice. Nenhum fórum fica solto sem link a partir de um índice.

**Fórum de referência consolidado (2026-06-20):** `Foruns/forum_protocolo_comunicacao_trindade_consolidado_20260620.md` — regras completas de comunicação (fóruns + canal + inbox + cartinhas humanizadas). Validar com todos os agentes.

**Fórum de limpeza e otimização do sistema (2026-06-20):** `Foruns/forum_limpeza_sistema_20260620.md` — registro completo da sessão de faxina (vídeos para lixeira exceto Riofilme, git gc .git 17G→2.1G, 1031 pycache, caches, memória 7.4Gi→2.2Gi, instalação ClamAV+BleachBit). Sem vírus. Sistema mais leve.
6. **Sub-índices recursivos.** Um fórum-índice pode ter até 30 links. Se passar disso, parte em sub-índices organizados por tema ou data.

---

## Governança Atual — Trindade como instância máxima

### Decisão de Miguel
O experimento de robô externo persistente/OpenClaw como CEO único não fica como autoridade central. A instância máxima volta a ser a **Trindade integrada**, com Miguel participando das decisões críticas.

### Regra de comando único
- Decisões operacionais relevantes exigem **mínimo de 3 votos**, incluindo obrigatoriamente Miguel.
- Não há CEO Augusto ou Kimi unificado acima da Trindade.
- Kimi, Claude, Codex, DeepSeek, Qwen, GLM, Grok e Antigravity podem propor, auditar, executar ou registrar conforme papel e autorização.
- O comando final deve ficar registrado em fórum/canal/memória antes de virar automação persistente.

### Boletim News
O Boletim News é responsabilidade compartilhada da própria Trindade. Quem estiver trabalhando deve manter o boletim fresco quando houver fato operacional importante. O boletim deixa de depender de um agente OpenClaw externo como fonte de verdade.

---

## Boletim News Dinâmico — Protocolo de Despertar

### Atualização 2026-06-10 — Cérebro como índice principal
Por decisão de Miguel, o **Cérebro é o principal índice das memórias do sistema**. O `acorde.sh` não deve tentar despejar todo o contexto no agente ao acordar. Ele deve funcionar como porta leve: mostrar relógio real, caminhos principais, Boletim News e guardrails, apontando para o Cérebro, fóruns, índices e memórias específicas conforme a tarefa.

### Retomada urgente — 2026-06-10 03:05 BRT

- Frente atual: reforma Tencent leve/limpo em 72h, sem parar o Cafezinho.
- Fórum principal: `Foruns/forum_reforma_simplificacao_cafezinho_72h_20260610.md`.
- Memória pessoal Codex: `Cerebro/memorias_provisorias/memoria_codex_viva.md`.
- Boletim News: `/root/scripts/atualizar_boletim_news.py` atualiza a lista determinística de Fóruns das últimas 24h, com síntese LLM opcional.
- Acorde: `acorde.sh` atualiza o Boletim ao despertar, exceto em `--paths`.
- Regra operacional atual sobre `rclone`/`rsync`: manter backups tradicionais controlados, inclusive Backblaze. Proibido é `reclone`, restore, sync reverso ou espelhamento que possa apagar local. O cron `/root/sync_b2.sh` voltou ativo às 05:00 porque é backup local -> Backblaze com filtros.
- Regra de segurança: seguir em dry-run/inventário; não aplicar limpeza destrutiva, JSONL `--apply`, purge/VACUUM no banco de mídia, nem reorganização física de `/root` sem plano, backup, manifesto e rollback.
- Correção de IA/Taxonomia: Resolvido problema de importação do `taxonomia_wordpress.json` na pasta `/root` do Tencent. Matérias do Agente IA agora levam obrigatoriamente as categorias Ciência e Tecnologia (19936) e Inteligência Artificial (5008) em dupla categorização, com tags validadas. Log consolidado em `CEREBRO_NODE_ATUALIZACOES.md`.
- **Nova Configuração de Agentes e Indexação (2026-06-10 10:30 BRT):** Promovido o Perplexity `sonar-pro` para fact-checking global (desativando o `sonar` básico devido a alucinações de cutoff temporal em cargos). Para a editoria de `eleicoes`, o Gemini 2.5 Flash com Google Search Grounding passa a atuar como Juiz Ouro principal de fact-checking (livre de listas de cargos estáticas e consultando a web em tempo real). Corrigida a lógica de skip do `util_indexing.py` (retornar `True` em skips duplicados/whitelist) para destravar a fila do auditor de indexação no Google.

### Atualização 2026-06-13 — Planejamento de Deploy Tencent e Patches Locais Validados
- **Frente Atual:** Migração "Lado a Lado" (Staging) na Tencent VPS, consolidando Banco de Mídia de 17 MB, portal Cafezinho e robôs temáticos.
- **Pausa de Segurança:** Kimi executou smoke tests 0 a 4 na Tencent, mas pausou nos testes 5 a 8 (escrita e drafts no WP) porque copiou os scripts legados da Tencent que possuíam caminhos SQLite hardcoded e sem suporte para o status global de WordPress.
- **Resolução de Bloqueios (Antigravity):** Patcheamos todos os 7 scripts SQLite no workspace local (`Legacy20260610/root/`) para respeitarem `BANCO_MIDIA_DB`. Patcheamos `motor_publicador.py`, `agente_flavio_bolsonaro.py` e `publicador_china.py` para honrarem a variável global de rascunhos `WP_STATUS_GLOBAL="draft"`. Ajustamos `acorde.sh` para mapear corretamente o `/root/Cerebro/` a dois níveis de diretório acima.
- **Próximo Passo na Retomada:**
  1. Transferir os scripts locais patcheados sobre a pasta de staging Tencent `/root/cafezinho/portal_cafezinho/`.
  2. Criar o `.env.unificado` do staging com as chaves corretas e `WP_STATUS_GLOBAL="draft"`.
  3. Ajustar permissões remotas no banco de produção antigo (`chmod 750 /root/agent_data/banco_midia/` e `640` no SQLite).
  4. Retomar os smoke tests 5 a 8 com Kimi (dry-run e geração de rascunhos no WordPress).
- **Fóruns Relacionados:** [forum_plano_migracao_duplicada_lado_a_lado_tencent_20260613.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_plano_migracao_duplicada_lado_a_lado_tencent_20260613.md), [forum_smoke_tests_tencent_executados_20260613.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_smoke_tests_tencent_executados_20260613.md) e [carta_resolucao_e_patches_aplicados_20260613.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/carta_resolucao_e_patches_aplicados_20260613.md).

Prompt introdutório recomendado no despertar:

> Bem-vindo de volta, amigo.
>
> Você é um engenheiro técnico do Sistema Cafezinho: um portal de notícias de esquerda, anti-imperialista, que usa agentes autônomos para coletar, produzir e publicar notícias com fact-checking, sem alucinação e com rastreabilidade.
>
> Tudo que você precisar saber mais sobre o projeto está no Cérebro. Use o Cérebro como índice principal e aprofunde apenas no que a tarefa exigir.
>
> Também trabalhamos em sites temáticos e satélites: Global South News, Rio Carta, Aiatolah, Mapa Rio, Discover Brazil, Mundo Trilhos e Rail Post.
>
> Somos vários membros de um grupo que chamamos Trindade: Claude Code, Codex, Kimi, DeepSeek, GLM, AGY, Qwen, Antigravity e outros agentes de IA, junto com o Diretor Miguel do Rosário.
>
> A Trindade se comunica pelo Canal Trindade, onde pontuamos novidades, pelos Fóruns específicos de cada tema e pelos inboxes de cada agente IA. O foco do nosso trabalho é produzir notícias e análises sobre a vida política e econômica do Brasil e do mundo.

Regra prática:
- Primeiro mapa do sistema: `CEREBRO_INDEX_MASTER.md`.
- Protocolo de despertar e memórias: `CEREBRO_NODE_MEMORIA_TRABALHO.md`.
- Estado quente operacional: `root/painel_v5/boletins/boletim_latest.md`.
- Reforma atual Tencent leve/limpo: `Foruns/forum_reforma_simplificacao_cafezinho_72h_20260610.md`.
- Índice de arquivo frio/logs/relatórios: `/root/indices/INDICE_MEMORIA_LEVEZA_ATUAL.md` no Tencent.

Comando recomendado:
```bash
./acorde.sh [agente]
```

Use apenas quando precisar de contexto amplo:
```bash
./acorde.sh --full [agente] [tail]
```

### O que mudou
O protocolo de despertar da Trindade foi atualizado para incluir o **Boletim News Dinâmico** e o **RESUMO_DESPERTAR.md** como fontes rápidas antes de mergulhar nos fóruns.

### Nova ordem de despertar (§68.1 revisado)
1. **Relógio real** — registrar data, hora e fuso com comando local, antes de qualquer leitura ou resposta:
   ```bash
   date '+%Y-%m-%d %H:%M:%S %Z %z'
   ```
   - Todo registro em fórum, canal ou inbox deve usar esse horário real.
   - Proibido usar horário aproximado (`~17:15`), horário lembrado pela LLM ou timestamp futuro.
   - Se o horário do agente divergir do relógio real do sistema, o agente deve parar e registrar `BLOQUEIO_RELOGIO` antes de votar, auditar, deployar ou atribuir autoria.
2. **Boletim News Dinâmico** — ler `root/painel_v5/boletins/boletim_latest.md`
3. **Resumo de Despertar** — ler `memorias_provisorias/RESUMO_DESPERTAR.md`
   - O RESUMO agora inclui: 🔐 Onde estão as chaves + 🖥️ Status Operacional ao vivo (resultado do smoke da última execução)
4. **Canal Trindade** — ler últimas entradas, priorizando blocos posteriores ao último parse
5. **Minha memória viva** — ler `memorias_provisorias/memoria_<agente>_viva.md` ou memória maestro para Claude
   - Cada memória viva tem bloco 🔐 no topo com chave própria, cofre e caminhos
6. **Meu inbox** — ler `Cerebro/Foruns/inbox_trindade/<agente>.md`
7. **Fóruns ativos indicados pelo boletim/resumo** — abrir apenas o que for necessário para agir
8. **Atualizar memória** — se houver novidade relevante, rodar `scripts/atualizar_memoria_trabalho_fase1.sh`

### Onde está o boletim dinâmico
| Local | Caminho |
|-------|---------|
| Arquivo | `root/painel_v5/boletins/boletim_latest.md` |
| Painel CCTV | http://localhost:8082/boletim |
| Histórico | http://localhost:8082/boletim/historico |
| Responsável | Trindade integrada; quem está trabalhando atualiza quando houver fato importante |

### Frequência
- **Fase 1 atual:** assistida por agente, sem cron.
- **Normal futura:** cron leve só depois de 24h estáveis.
- **Crise:** atualização por agente após eventos relevantes, sempre com lock local.

### Conteúdo do boletim
- Ticks do Claude (Loop Maestro)
- Inboxes da Trindade (10 agentes)
- Sprints ativos
- Canal Trindade (últimas entradas)
- Alertas e métricas

### Comandos de despertar

**Comando ÚNICO:**
```bash
cd "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes"
./acorde.sh [agente] [tail]
```
O `acorde.sh` faz 4 passos em sequência (1 wake só, sem duplicação):
1. Smoke operacional → `.status_operacional.md`
2. Parse-canal → importa novidades para memórias vivas
3. Wake → `RESUMO_DESPERTAR.md` com memória integrada da Trindade toda
4. Validate → checa integridade

**Manutenção periódica (não é despertar):**
```bash
# Rotina Fase 1 — parse-canal + validate (sem wake duplicado)
./scripts/atualizar_memoria_trabalho_fase1.sh
```

**Consulta rápida:**
```bash
# Ver boletim atual
cat "root/painel_v5/boletins/boletim_latest.md"

# Ver resumo de despertar local
cat "memorias_provisorias/RESUMO_DESPERTAR.md"

# Ver status operacional ao vivo
cat "memorias_provisorias/.status_operacional.md"
```

---

## Memórias anteriores
*(mantidas para referência — ver histórico no git)*

---

*Registrado pela Trindade por decisão de Miguel*
*Integração: Canal Trindade + RESUMO_DESPERTAR + Boletim News*

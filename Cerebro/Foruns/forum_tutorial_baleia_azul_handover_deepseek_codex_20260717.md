# 🐋 Fórum Tutorial — Handover do Baleia Azul: DeepSeek (Cheng) → Codex

**Data:** 2026-07-17
**De:** Cheng / DeepSeek (editor cessante)
**Para:** Codex (editor interino)
**Status:** Handover completo

---

## 1. Função editorial do Baleia Azul

O Baleia Azul é o **boletim diário de despertar e situação** do Cafezinho Media Group. Ele tem três funções:

- **Jornal matinal para Miguel** — primeira leitura do dia, tom de briefing executivo.
- **Fonte de despertar para todos os agentes da Trindade** — substituiu o `boletim_latest.md` (congelado desde 28/05).
- **Registro histórico leve** — cada edição é um snapshot do ecossistema naquele dia.

Não substitui fóruns, recibos, manifestos ou o Canal Trindade. Aponta para eles.

---

## 2. Público principal

**Miguel do Rosário** — lê todo dia, geralmente de manhã. Quer saber o que aconteceu, o que precisa decidir, e se há algo quebrado. Não quer relatório burocrático.

**Secundário:** agentes da Trindade (Claude, Codex, Kimi, GLM, Qwen, Grok, Antigravity, Kilo, AGY) — usam como aquecimento antes de começar a trabalhar.

---

## 3. Como escolher a manchete

A manchete deve responder: **"o que Miguel precisa saber hoje?"**

Regras:
- **No máximo 3 fatos** na manchete. Se tiver mais, escolha os que têm consequência operacional.
- **Verbo no presente** — "Codex avança", "Claude reorganiza", não "Codex avançou".
- **Nomes próprios** — Claude, Codex, Antigravity, Miguel. Não "agentes".
- **Gancho de urgência** quando houver — "Sprint começa amanhã", "Faltam 2 dias".
- Se nada relevante aconteceu, diga isso honestamente: "Ritmo lento no ecossistema".

---

## 4. Como separar fato importante de ruído

- **Circuit breaker isolado** = ruído. Circuit breaker que abriu 3 vezes em 24h com cooldown de 1440min = padrão, não notícia.
- **Fórum novo com ação concreta** = fato. Fórum novo sem decisão nem deadline = ruído.
- **Atividade no Canal Trindade** = fato. Silêncio no canal = dado (anote "sem atividade registrada").
- **Métrica atualizada** = fato. Métrica repetida da edição anterior = ruído (a menos que mude significativamente).
- Regra de ouro: se Miguel não precisa tomar decisão nem saber disso pra tocar o dia, é ruído.

---

## 5. Tom que funciona com Miguel

- **Direto, sem enrolação.** Não use "estou animado para compartilhar" nem "é com grande satisfação".
- **Nomes próprios.** "O Codex fez X", não "foram realizadas atividades".
- **Transparência sobre o que você não sabe.** "⚠️ Dados de audiência não atualizados hoje" é melhor que omitir.
- **Humor seco e pontual.** "Madrugada de faxina" funcionou. "Ecossistema em ritmo lento" também.
- **Nunca puxar saco.** Miguel é jornalista, detecta bajulação a quilômetros.
- As seções de "Decisões que precisa tomar" são as mais lidas. Seja cirúrgico ali.

---

## 6. Seções essenciais (não pular nunca)

1. **Manchete** — 3 fatos máximos + saudação "Bom dia, Miguel."
2. **O que está acontecendo na redação** — ✅ Concluído / 🟡 Em andamento / 🔴 Parado
3. **Decisões que precisa tomar** — lista numerada, uma frase por item
4. **Circuit breakers ativos** — tabela com modelo, motivo, cooldown, desde quando

---

## 7. Seções que podem variar (conforme o dia)

- **🔜 Se aproximando** — quando há deadline iminente (ex: sprint no fim de semana)
- **📊 Audiência** — quando há dados frescos; se não, admite "não atualizado"
- **📋 Mudanças estruturais** — quando houve reforma/migração (ex: 17/07)
- **📋 Próximos passos** — atribuições por agente, útil para coordenação
- **🔧 Infraestrutura / backups / segurança** — quando há incidente ou mudança

---

## 8. Como reunir informações do ecossistema

Ordem de leitura antes de escrever (15-20 min):

1. **Canal Trindade** — `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` (últimas 50-100 linhas)
2. **Inboxes ativas** — `Cerebro/Foruns/inbox_trindade/*.md`
3. **Fóruns novos** — `Cerebro/Foruns/` ordenados por data de modificação
4. **Ponto de retomada dos agentes** — `Cerebro/memorias_provisorias/PONTO_DE_RETOMADA_*.md`
5. **Manifesto V4** — `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
6. **Cérebro Master** — `Cerebro/CEREBRO_INDEX_MASTER.md` (só se houver mudança estrutural)

⚠️ Armadilha: o Canal Trindade foi resetado na reforma de 17/07. Se estiver muito curto, procure fóruns diretamente.

---

## 9. Arquivos lidos antes de escrever (checklist)

```
☐ Projeto Cafezinho Agentes/Foruns/canal_trindade.md
☐ Cerebro/Foruns/ (fóruns com data de hoje ou ontem)
☐ Cerebro/Foruns/inbox_trindade/deepseek.md
☐ Cerebro/Foruns/inbox_trindade/codex.md
☐ Cerebro/Foruns/inbox_trindade/claude.md
☐ Cerebro/memorias_provisorias/PONTO_DE_RETOMADA_DEEPSEEK.md
☐ Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md
☐ Cerebro/CEREBRO_NODE_BALEIA_AZUL.md (este índice)
```

---

## 10. Como consultar Canal Trindade, inboxes, fóruns e pontos de retomada

- **Canal Trindade**: leia de baixo pra cima (últimas entradas primeiro). Circuit breakers automáticos no início do arquivo são ruído — procure blocos com `## 2026-07-XX` que têm nome de agente.
- **Inboxes**: procure por mensagens não respondidas (sem `Status: respondido`). Se a última mensagem tem mais de 7 dias, está dormente.
- **Fóruns**: filtre por data no nome do arquivo (`20260717`). Leia só o cabeçalho (primeiras 20 linhas) para classificar relevância.
- **Pontos de retomada**: a data no cabeçalho diz se o agente esteve ativo. Se a data é >3 dias, o agente está offline.

---

## 11. Como obter dados de audiência

**Fonte canônica:** NYC (`ssh root@198.199.121.136`), arquivo `/root/agent_data/analise_performance.json`.

**Script:** `scratch/enviar_baleia_azul_v2.sh` (raiz do workspace) — faz SSH no NYC, extrai `total_views_periodo`, `media_views` e `top_5_posts`.

**Cron:** `0 8 * * *` — executa o script acima. Se não rodou, rode manualmente:
```bash
bash "/home/migueldorosario/Downloads/Antigravity Google/scratch/enviar_baleia_azul_v2.sh"
```

**Endpoint:** http://43.156.151.165/v5/baleia (CCTV v5, HTML dinâmico a partir do markdown)

⚠️ **Histórico de falha:** O script original puxava do Tencent (`ubuntu@43.156.151.165`), que teve o cron do `agente_performance` desligado no failover. O arquivo de audiência congelou em 01/07. Claude corrigiu em 10/07 para apontar para NYC. **Sempre confira que o script está apontando para NYC.**

---

## 12. Como verificar custos e saúde dos modelos

Atualmente **não temos coleta sistemática** de custos no Baleia Azul. O que existe:

- **Circuit breakers** no Canal Trindade — indicam modelos com problema (auth_config, quota_exhausted, rate_limit).
- **Roteador LLM** — registra aberturas de circuit breaker automaticamente a cada ~24h.
- **V4 telemetria** — `Projeto Cafezinho Agentes/root/v4_labs/v4_memoria/` tem registros, mas não são sumarizados automaticamente.

⚠️ Recomendação para o Codex: criar um healthcheck rápido antes de cada edição — pelo menos verificar se há novos circuit breakers desde a edição anterior.

---

## 13. Como identificar circuit breakers realmente ativos

**Fonte:** Canal Trindade, entradas do `Roteador LLM / Circuit breaker`.

**Regra:**
- Cooldown ≤ 60min e aberto há < 2h = ativo relevante
- Cooldown 1440min (24h) = manutenção programada, não é crise
- Se o mesmo modelo aparece 3+ vezes em 48h = padrão, não notícia
- `quota_exhausted` é mais grave que `auth_config`

**Na edição:** liste só os que estão dentro do período de cooldown. Inclua a data/hora de abertura. Se não houve rechecagem, admita "não rechecado".

---

## 14. Como acompanhar V4, redação, sites temáticos e infraestrutura

- **V4**: `Projeto Cafezinho Agentes/root/v4_labs/dados/` — procure a rodada ativa mais recente. O manifesto V4 (`Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`) lista artigos ativos e posts no WP.
- **Redação**: Canal Trindade + fóruns com "publicacao" ou "artigo" no nome.
- **Sites temáticos**: ordem de atividade no manifesto V4. Local: `Projeto Cafezinho Agentes/sites-tematicos/`.
- **Infraestrutura**: `Cerebro/CEREBRO_NODE_BACKUPS_BACKBLAZE.md`, Canal Trindade.

---

## 15. Como gerar Markdown, HTML, PDF, email e Telegram

| Saída | Como | Status |
|-------|------|--------|
| **Markdown** | `write_file` em `Projeto Cafezinho Agentes/boletim_baleia_azul_YYYYMMDD.md` | ✅ Funcionando |
| **HTML dinâmico** | CCTV v5 lê o markdown → rota `/v5/baleia` | ✅ Funcionando |
| **HTML estático** | `/var/www/html/baleia_azul.html` no Tencent. Precisa ser atualizado após cada edição. | ⚠️ Precisa acesso SSH ao Tencent |
| **PDF** | Não implementado | ❌ |
| **Email (Miguel)** | `scratch/enviar_baleia_azul_v2.sh` → SSH Tencent → `mail migueldorosario@gmail.com` | ⚠️ Depende de cron/manual |
| **Email (lista/newsletter)** | Não implementado. Mailchimp existe no ecossistema (caixa de newsletter nos posts WP) mas nunca foi integrado ao Baleia Azul. | ❌ Lacuna |
| **Telegram** | Mesmo script → API `api.telegram.org/bot...` → chat_id 1894890759 | ⚠️ Depende de cron/manual |

---

## 16. Scripts, cron jobs, endpoints e servidores

| Componente | Local/Caminho | Estado |
|------------|---------------|--------|
| Script de envio | `scratch/enviar_baleia_azul_v2.sh` (raiz do workspace) | ✅ Funcional |
| Script de envio v1 | `scratch/enviar_baleia_azul.sh` (raiz) | 🔄 Versão anterior |
| Cron | `0 8 * * *` no crontab local | ⚠️ Verificar se ativo |
| CCTV v5 | http://43.156.151.165/v5/baleia | ✅ Online |
| Nginx estático | http://43.156.151.165/painel/baleia_azul.html | ⚠️ Precisa update |
| Tencent SSH | `ssh -p 38422 ubuntu@43.156.151.165` | — |
| NYC SSH (audiência) | `ssh root@198.199.121.136` | — |
| Watchdog V3 | `scratch/watchdog_v3.sh` (executa Baleia Azul às 10h UTC) | ⚠️ Verificar |
| Fix crontab | `scratch/fix_crontab_baleia.py` | 🔧 Script auxiliar |

---

## 17. O que está funcionando

- ✅ Geração de markdown (edições 8, 9, 10)
- ✅ CCTV v5 lendo markdown e gerando HTML dinâmico
- ✅ Script de envio localizado e funcional (`enviar_baleia_azul_v2.sh`)
- ✅ Pipeline NYC para audiência (corrigido em 10/07)
- ✅ Baleia Azul como fonte de despertar (protocolos atualizados 16-17/07)
- ✅ `acorde.sh` reescrito para apontar pro Baleia Azul

---

## 18. O que está quebrado, congelado ou desatualizado

- ⚠️ **HTML estático** (`/var/www/html/baleia_azul.html` no Tencent) — não é atualizado automaticamente. Precisa de SSH.
- ⚠️ **Cron de envio** — não confirmado se está rodando. Edições 8, 9, 10 foram markdown-only.
- ⚠️ **Audiência** — desatualizada desde 15/07. Script não foi executado.
- ❌ **Edições 1-7** — movidas para o legacy na reforma de 17/07. Só a #10 está na raiz ativa.
- ❌ **Edição #3** — ausente do histórico. Pode ter sido pulada ou perdida.
- ❌ **PDF** — nunca implementado.
- ⚠️ **`acorde.sh` filho** — movido para `legacy_reformado_20260717/toplevel_legacy/.../sh/acorde.sh`. O script raiz foi reescrito.
- ⚠️ **Circuito de verificação** — sem healthcheck automático antes da edição.

---

## 19. Erros que já aconteceram e como evitar

| Erro | Causa | Prevenção |
|------|-------|-----------|
| Boletim 16 dias parado (28/06 a 15/07) | 3 falhas simultâneas: markdown não gerado, HTML estático congelado, script puxando audiência do servidor errado | Checklist pré-publicação: markdown existe? HTML atualizado? Script aponta pra NYC? |
| Baleia Azul mostrava edição #6 de 25/06 em pleno 15/07 | HTML estático nunca atualizado | Após cada edição, verificar o endpoint http://43.156.151.165/painel/baleia_azul.html |
| Script puxava audiência do Tencent (congelado) | Failover desligou cron do `agente_performance` no Tencent | Conferir `ssh root@198.199.121.136` como fonte, não Tencent |
| Circuit breakers listados sem rechecagem | Confiava no Canal sem verificar se ainda estavam em cooldown | Incluir data/hora de abertura; admitir "não rechecado" |
| Caminhos de fórum desatualizados nos protocolos | Reforma moveu fóruns; symlinks preservados mas referências em markdown não atualizaram | Após cada reforma, revisar todos os protocolos de despertar |
| acorde.sh quebrado | Script filho foi movido pro legacy; script raiz ainda apontava pra ele | Reescrito para ser autossuficiente |

---

## 20. Melhorias recomendadas

1. **Healthcheck automático** — script que verifica antes da edição: audiência atualizada? HTML estático OK? Canal Trindade ativo?
2. **Coleta de audiência integrada** — executar `enviar_baleia_azul_v2.sh` como parte do ritual de escrita, não depender do cron.
3. **Atualização do HTML estático** — via `scp` ou script no Tencent, disparado após cada markdown.
4. **Cobertura de custos** — incluir seção de custos quando houver dados dos modelos (V4 telemetria).
5. **Índice de edições vivas** — manter `boletim_baleia_azul_INDICE.md` com links para todas as edições.
6. **Template padronizado** — `boletim_baleia_azul_TEMPLATE.md` para o editor não precisar lembrar a estrutura.
7. **Verificação de atividade fora do Canal** — varrer fóruns por data, não depender só do Canal Trindade.
8. **Link para o Cérebro** — toda edição deve linkar `CEREBRO_INDEX_MASTER.md`.

---

## 21. Regras editoriais que ainda estão só na minha memória

- Se não tem nada relevante, publique mesmo assim — uma edição curta é melhor que um hiato.
- A seção "Decisões que precisa tomar" é a mais importante. Se tiver que cortar algo, corte o resto.
- Nunca invente métrica. "⚠️ Dados não atualizados" é honesto e útil.
- O Baleia Azul compete com a atenção do Miguel. Seja mais curto que um artigo, mais completo que um tweet.
- Circuit breakers com cooldown 1440min são manutenção programada, não crise. Não alarme.
- Sempre confira se o endpoint HTML estático mostra a edição correta — esse foi o bug que matou o boletim por 16 dias.

---

## 22. Edições históricas e onde estão

| Edição | Data | Local |
|--------|------|-------|
| #1 | 18/06 | Legacy: `.../markdown/boletim_baleia_azul_20260618.md` |
| #2 | 19/06 | Legacy: `.../markdown/boletim_baleia_azul_20260619.md` |
| #3 | — | **Não localizada** |
| #4 | 22/06 | Legacy: `.../markdown/boletim_baleia_azul_20260622.md` |
| #5 | 23/06 | Legacy: `.../markdown/boletim_baleia_azul_20260623.md` |
| #6 | 25/06 | Legacy: `.../markdown/boletim_baleia_azul_20260625.md` |
| #7 | 28/06 | Legacy: `.../markdown/boletim_baleia_azul_20260628.md` |
| #8 | 15/07 | Legacy: `.../markdown/boletim_baleia_azul_20260715.md` |
| #9 | 16/07 | Legacy: `.../markdown/boletim_baleia_azul_20260716.md` |
| #10 | 17/07 | **Ativa:** `Projeto Cafezinho Agentes/boletim_baleia_azul_20260717.md` |

Caminho base do legacy: `Projeto Cafezinho Agentes/legacy_reformado_20260717/toplevel_legacy/limpeza_extra_20260717/top/top_level_residuo_v4_20260717/base_level_clean_20260717/markdown/`

---

## 23. Edições ou formatos que parecem ter se perdido

- **Edição #3** — ausente. Numeração pula de #2 (19/06) para #4 (22/06). Pode ter sido pulada ou perdida na reforma.
- **20/06, 21/06, 24/06, 26/06, 27/06** — sem edição Markdown. Existe PDF de 20/06.
- **29/06 a 14/07** — hiato de 16 dias. Nenhuma edição.
- **Formato original (#1 a #7)** — ligeiramente diferente do formato atual (#8 a #10), mais enxuto.

---

## 24. Como fazer rollback se uma edição errada for publicada

1. **Markdown**: regravar o arquivo com `write_file`. O arquivo anterior fica no histórico do editor.
2. **HTML dinâmico (CCTV v5)**: reler o markdown corrigido — o CCTV atualiza na próxima requisição.
3. **HTML estático (Tencent)**: precisa de SSH para regravar `/var/www/html/baleia_azul.html`.
4. **Email**: não tem recall. Se enviou errado, enviar correção com "ERRATA" no assunto.
5. **Telegram**: editar a mensagem via API (`editMessageText`) se dentro da janela de 48h.

⚠️ Nunca publique sem verificar o endpoint HTML estático.

---

## 25. Como manter o boletim útil sem transformá-lo em relatório burocrático

- **Leia em 2 minutos.** Se passar disso, corte.
- **Cada seção ganha seu lugar pela consequência.** Se não há decisão pendente, não force.
- **Linguagem de jornal, não de atas de reunião.** "Codex avançou o V4" em vez de "Foram realizados 280 testes unitários com 11 agentes técnicos validados".
- **Uma edição curta é melhor que pular um dia.** Se não há nada, diga "Dia tranquilo no ecossistema" e liste 2-3 itens.
- **Miguel não é seu chefe, é seu leitor.** Escreva pra ele, não pra "registrar".

---

## Esclarecimentos especiais

### Por que o boletim ficou 16 dias parado (28/06 a 15/07)

Três falhas independentes que se acumularam:

1. **Markdown**: ninguém gerava o arquivo `boletim_baleia_azul_*.md`. DeepSeek não estava publicando (sem autorização). Outros agentes não assumiram.
2. **HTML estático**: o arquivo `/var/www/html/baleia_azul.html` no Tencent não era atualizado desde 25/06. O endpoint `/painel/baleia_azul.html` mostrava a edição #6 por semanas.
3. **Script de audiência**: `enviar_baleia_azul_v2.sh` puxava dados do Tencent (`ubuntu@43.156.151.165`), onde o cron do `agente_performance` foi desligado no failover. O arquivo `analise_performance.json` congelou em 01/07. Claude corrigiu para NYC em 10/07, mas o markdown continuou parado.

### Como o boletim_latest.md congelado afetava o despertar

O `acorde.sh` original lia `boletim_latest.md` como primeira fonte. Como ele estava congelado em 28/05, qualquer agente que acordasse recebia informação de quase 2 meses atrás. Isso causava desorientação generalizada — agentes tomando decisões baseadas em estado inexistente.

### Como o script passou a buscar audiência no servidor errado

O script original usava `ssh ubuntu@43.156.151.165` (Tencent). Quando o failover desligou o cron do `agente_performance` no Tencent, o JSON de audiência parou de ser atualizado. O script continuou lendo o mesmo arquivo congelado por 9+ dias. Claude corrigiu em 10/07 para `ssh root@198.199.121.136` (NYC).

### Qual é hoje a fonte correta da audiência

**NYC**: `ssh root@198.199.121.136`, arquivo `/root/agent_data/analise_performance.json`.

### Onde está o script ativo de envio

`scratch/enviar_baleia_azul_v2.sh` na **raiz do workspace** (`/home/migueldorosario/Downloads/Antigravity Google/scratch/`), não em `Projeto Cafezinho Agentes/scratch/`.

### Onde está o cron

No crontab local do Miguel. Linha esperada:
```
0 8 * * * bash "/home/migueldorosario/Downloads/Antigravity Google/scratch/enviar_baleia_azul_v2.sh" >> /tmp/baleia_azul_envios.log 2>&1
```

Script auxiliar: `scratch/fix_crontab_baleia.py`.

### Qual endpoint é canônico

- **Primário:** http://43.156.151.165/v5/baleia (CCTV v5, dinâmico)
- **Estático:** http://43.156.151.165/painel/baleia_azul.html (Nginx)

### Como confirmar que HTML, email e Telegram mostram a edição correta

- **HTML estático**: `curl -s http://43.156.151.165/painel/baleia_azul.html | head -20`
- **HTML dinâmico**: `curl -s http://43.156.151.165/v5/baleia | head -20`
- **Email**: verificar logs em `/tmp/baleia_azul_envios.log`
- **Telegram**: verificar no chat do Miguel se a mensagem chegou

### Como evitar publicar circuit breakers antigos como se ainda estivessem ativos

- Sempre incluir **data e hora** de abertura do circuit breaker.
- Se o cooldown já expirou, remover da lista.
- Se não rechecou, admitir "não rechecado desde [data]".

### Como detectar trabalho que aconteceu fora do Canal Trindade

- **Fóruns novos** em `Cerebro/Foruns/` com data de hoje ou ontem que não foram mencionados no Canal.
- **Inboxes com mensagens novas** (sem `Status: respondido`).
- **Manifesto V4** atualizado — `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`.
- **Arquivos modificados** nos diretórios ativos (`root/v4_labs/`, `sites-tematicos/`).

### Como o editor pode acompanhar o V4 sem depender apenas de relatos manuais

- Ler `Projeto Cafezinho Agentes/root/v4_labs/dados/` — a rodada ativa mais recente tem os artigos.
- Verificar `v4_memoria/foruns/` para updates de pipeline.
- Verificar `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`.
- Posts em rascunho no WP podem ser verificados via API REST (`/wp-json/wp/v2/posts?status=draft`).

---

## Divergência com o CEREBRO_NODE_BALEIA_AZUL.md

O nodo lista as edições 8, 9 e 10 como estando no legacy. **Divergência**: a edição #10 está na raiz ativa (`Projeto Cafezinho Agentes/boletim_baleia_azul_20260717.md`). As edições 8 e 9 foram movidas para o legacy na reforma da madrugada de 17/07. A edição 10 foi criada após a reforma, portanto permaneceu na raiz.

---

## Procedimento de fechamento desta missão

- [x] Tutorial no fórum: `Cerebro/Foruns/forum_tutorial_baleia_azul_handover_deepseek_codex_20260717.md`
- [x] Manifesto: `Cerebro/Foruns/manifesto_handover_baleia_azul_deepseek_20260717.md`
- [x] Inbox DeepSeek atualizado
- [x] Canal Trindade registrado
- [x] Carta humanizada para Miguel → Codex

**Entrega: COMPLETA.** Handover finalizado. Codex assume como editor interino do Baleia Azul.

---

*Handover preparado por Cheng / DeepSeek em 17/07/2026. Codex assume como editor interino.*

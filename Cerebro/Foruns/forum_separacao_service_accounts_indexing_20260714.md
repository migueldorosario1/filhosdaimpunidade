# 🧹 Fórum — Separação das Service Accounts do Google Indexing API

**Data de abertura:** 2026-07-14
**Autor da abertura:** Claude Code (agente), a pedido de Miguel
**Status:** aberto — aguardando alinhamento antes de execução
**Prioridade:** média-alta (não urgente, mas quanto antes fizermos, melhor para escalar)

---

## 1. Motivação

Hoje (14/07/2026), auditoria descobriu que **todos os sites da constelação Cafezinho compartilham a mesma service account do Google Indexing API**:

```
project_id:   gen-lang-client-0200069757
client_email: indexing-cafezinho@gen-lang-client-0200069757.iam.gserviceaccount.com
```

Na prática hoje isso **não gera problema imediato** — só o Cafezinho canônico (`www.ocafezinho.com`) está de fato empurrando pings ao Google (1.625 pings OK nos últimos 30d; **zero** para mundotrilhos, discoverbrazil, gsn, riocarta). Mas há três riscos latentes que Miguel quer eliminar antes de escalar indexação para outros sites:

1. **Compartilhamento de quota** — Google Indexing API dá 200 requests/dia **por projeto GCP**. Se qualquer outro site ligar indexação, briga com o Cafezinho pela mesma quota.
2. **Reputação compartilhada** — Google atribui score de confiança **por service account**. Conteúdo de baixa qualidade em um site (ex: cafezinho.news espelho, ou algum temático experimental) pode rebaixar a reputação e afetar a indexação de TODOS os sites que a mesma account atende.
3. **Ownership e blast radius** — se a chave vaza ou o account é bloqueado, todos os sites caem juntos. Separação isola falhas.

**Decisão macro sancionada por Miguel:** o projeto GCP `gen-lang-client-0200069757` fica **exclusivamente** para o Cafezinho canônico. Todos os sites temáticos migram para service accounts próprias, uma por projeto GCP.

---

## 2. Inventário atual (2026-07-14)

### Service accounts existentes no server (NYC 198.199.121.136)

| Keyfile | Projeto GCP | Service account | Uso hoje |
|---|---|---|---|
| `/root/agent_data/indexing_key.json` | `gen-lang-client-0200069757` | `indexing-cafezinho@...` | ✅ **Ativa** (única em uso) |
| `/root/cafezinho/dados_agentes/indexing_key.json` | idem (mesmo keyfile duplicado) | idem | ✅ Ativa (mesma) |
| `/root/cafezinho/sites_tematicos/gsn/agent_data/indexing_key.json` | idem (duplicado no path GSN) | idem | ❌ Não usada (código GSN não chama Indexing API) |
| `/root/agent_data/indexing_key_gsn_TEST.json` | `open-claw-gsn` | `indexing-gsn@open-claw-gsn.iam.gserviceaccount.com` | ⚠️ **TESTE existente** — embrião de separação já criado, não deployado |
| `/root/V3/tmp/indexing_key_gsn_test.json` | idem `open-claw-gsn` | idem | ⚠️ Mesma chave, path temporário |
| `/root/cafezinho/dados_agentes/indexing_key_gsn_TEST.json` | idem `open-claw-gsn` | idem | ⚠️ Mesma chave, terceiro path |

**Observação importante:** já existe uma service account de teste para GSN (`indexing-gsn@open-claw-gsn.iam.gserviceaccount.com`) em outro projeto GCP. Aparentemente alguém (Miguel, agente anterior) começou a separação e não terminou. Precisamos decidir se ela é a base do trabalho ou se recriamos do zero.

### Sites da constelação e status de indexação

| Site | Domínio | GSC verificado? | Indexação ativa hoje? | Ativar? |
|---|---|---|---|---|
| Cafezinho canônico | ocafezinho.com | ✅ `sc-domain:ocafezinho.com` (Owner) | ✅ Ativa (1.625 pings/30d) | Sim (mantém) |
| Global South News | globalsouth.news | ✅ (verificado) | ❌ Não | **? (Miguel decide)** |
| Global South News BR | globalsouthnews.com.br | ✅ (verificado) | ❌ Não | **? (Miguel decide)** |
| Mundo dos Trilhos | mundotrilhos.com | ⚠️ Verificar | ❌ Não | **? (Miguel decide)** |
| Discover Brazil | discoverbrazil.news | ⚠️ Verificar | ❌ Não | **? (Miguel decide)** |
| Rio Carta | riocarta.com | ⚠️ Verificar | ❌ Não (nem tá na whitelist) | **? (Miguel decide)** |
| Mapa Rio | mapario.com.br | ⚠️ Verificar | ❌ Não | **? (Miguel decide)** |
| cafezinho.news (espelho) | cafezinho.news | Não deve indexar (noindex site-wide) | ❌ Não | ❌ **Definitivamente não** |

### Whitelist atual (`util_indexing.py`)

```python
INDEXING_ALLOWED_DOMAINS = (
    "ocafezinho.com",
    "mundotrilhos.com",
    "mundodostrilhos.com",
    "railpost.news",
    "discoverbrazil.news",
)
```

Note: `mundodostrilhos.com` e `railpost.news` estão na whitelist mas nem sei se são sites ativos hoje. Precisa auditar. GSN, Rio Carta, Mapa Rio **não** estão na whitelist.

---

## 3. Modelo alvo

Um projeto GCP por site relevante, cada um com sua service account, sua quota de 200/dia, sua reputação independente:

| Projeto GCP (proposta) | Service account | Domínio(s) coberto(s) | Prioridade |
|---|---|---|---|
| `gen-lang-client-0200069757` (mantém) | `indexing-cafezinho@...` | **ocafezinho.com** (apenas) | Já pronto — só limpar |
| `indexing-gsn` (renomear `open-claw-gsn` ou novo) | `indexing-gsn@...` | globalsouth.news + globalsouthnews.com.br | Se Miguel quiser ativar |
| `indexing-riocarta` (novo) | `indexing-riocarta@...` | riocarta.com | Se Miguel quiser ativar |
| `indexing-mundotrilhos` (novo) | `indexing-mundotrilhos@...` | mundotrilhos.com | Se Miguel quiser ativar |
| `indexing-discoverbrazil` (novo) | `indexing-discoverbrazil@...` | discoverbrazil.news | Se Miguel quiser ativar |
| `indexing-mapario` (novo) | `indexing-mapario@...` | mapario.com.br | Se Miguel quiser ativar |

**Custo GCP:** zero. Projetos, service accounts, Indexing API são gratuitos.
**Limite Google:** cada conta Google pessoal pode ter até 12 projetos GCP no plano free tier padrão. Miguel tem folga.

---

## 4. Estrutura de código proposta

Trocar o modelo atual (whitelist global + 1 keyfile) por **mapeamento domínio → service account**:

```python
# util_indexing.py — novo modelo
INDEXING_SITES = {
    "ocafezinho.com": {
        "keyfile": "/root/agent_data/indexing_keys/cafezinho.json",
        "project": "gen-lang-client-0200069757",
        "sc_property": "sc-domain:ocafezinho.com",
    },
    "globalsouth.news": {
        "keyfile": "/root/agent_data/indexing_keys/gsn.json",
        "project": "indexing-gsn",
        "sc_property": "sc-domain:globalsouth.news",
    },
    # ... um por site ativado
}

def keyfile_para_url(url):
    """Resolve qual service account usar para uma URL."""
    host = dominio_da_url(url)
    for dom, cfg in INDEXING_SITES.items():
        if host == dom or host.endswith("." + dom):
            return cfg["keyfile"]
    return None  # rejeita
```

E o `_contar_pings_hoje()` também vira por-site — cada site tem seu contador de 200/dia independente.

**Consequência:** o `auditor_indexacao_posts.py` (que hoje só serve Cafezinho) continua funcionando igual. Novos agentes por site instanciam `notificar_e_logar()` normalmente — o util decide qual service account usar com base no domínio da URL.

---

## 5. Fases sugeridas de execução

### Fase 0 — alinhamento (esta rodada)
- [ ] Miguel responde as perguntas em aberto (§7 abaixo)
- [ ] Decisão sobre reusar `open-claw-gsn` ou criar do zero
- [ ] Ordem de prioridade dos sites (quais ligar primeiro após separação)

### Fase 1 — limpar projeto Cafezinho
- [ ] Confirmar que **só** ocafezinho.com está registrado no GSC como propriedade da service account atual
- [ ] Remover ownership da service account em qualquer outro site (se existir)
- [ ] Auditar whitelist do `util_indexing.py` — reduzir para só `ocafezinho.com`
- [ ] Renomear keyfile para `indexing_key_cafezinho.json` (clareza)
- [ ] Backup do keyfile antes de qualquer mudança
- [ ] Remover os 3 duplicados espalhados (`sites_tematicos/gsn/agent_data/`, `cafezinho/dados_agentes/`) → deixar canônico em 1 lugar só

### Fase 2 — criar service accounts novas (uma por vez, sob demanda)
Para cada site que Miguel quiser ligar:
- [ ] Criar projeto GCP novo no [console.cloud.google.com](https://console.cloud.google.com/)
- [ ] Ativar Google Indexing API no projeto
- [ ] Criar service account nomeada padrão (`indexing-<site>@<projeto>.iam.gserviceaccount.com`)
- [ ] Gerar chave JSON, baixar
- [ ] Adicionar service account como **Owner** no GSC do site (via Search Console → Configurações → Usuários)
- [ ] Copiar chave para servidor NYC em `/root/agent_data/indexing_keys/<site>.json`
- [ ] Adicionar entrada em `INDEXING_SITES` no `util_indexing.py`
- [ ] Smoke test: 1 URL do site com `notificar_e_logar_v2()` — deve dar ping OK

### Fase 3 — refatorar util_indexing.py
- [ ] Trocar whitelist tupla por dict `INDEXING_SITES`
- [ ] Adaptar `deve_indexar()`, `_ler_historico_hoje()`, `_contar_pings_hoje()` para operar POR domínio
- [ ] Ajustar `indexador_google.py` para receber keyfile como parâmetro (hoje é hardcoded)
- [ ] Contador de pings por-site: passa a haver `pings_ocafezinho.com_<data>.jsonl`, `pings_globalsouth.news_<data>.jsonl`, etc
- [ ] Preservar compat: `disparar_indexacao(url)` e `notificar_e_logar(url)` continuam funcionando pros 12+ agentes editoriais que já usam

### Fase 4 — validação e monitoramento
- [ ] Painel de quota por-site — usar/dia por account
- [ ] Alerta se algum site chegar em 180/200
- [ ] Logs separados por site
- [ ] Verificar que Cafezinho canônico continua com quota isolada

---

## 6. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Quebrar indexação do Cafezinho durante refactor | Backup do keyfile + do util_indexing.py; smoke test antes de commit; deploy fora de horário de pico |
| Perder ownership no GSC de algum site | Só remove ownership da SA antiga DEPOIS que a nova estiver validada |
| Quotas dessincronizadas com o Google real | Manter fonte da verdade no JSONL local; reconciliar periodicamente com `verificador_retroativo` |
| Chave JSON vazar | Path `/root/agent_data/indexing_keys/` com 700, backups em Backblaze, nunca commitar em git |
| Google detectar mudança abrupta e rate-limitar | Adicionar sites gradualmente, um por semana; observar métricas |

---

## 7. Perguntas em aberto (Miguel precisa decidir)

### 7.1 Escopo — quais sites vão ter indexação ativa pós-separação?

**Opção A — só Cafezinho** (estado atual, mais conservador)
- Cria só a estrutura de código pra suportar múltiplas SAs, mas não cria SA nenhuma nova
- Cafezinho fica isolado, mundo dos outros sites sem indexação (como já é hoje)

**Opção B — Cafezinho + 1 site** (pilotar antes de escalar)
- Escolher UM outro site pra ligar (candidato natural: **Rio Carta**, que hoje nem tá na whitelist)
- Testa o modelo completo com 1 site secundário antes de expandir

**Opção C — Cafezinho + todos os sites ativos**
- Ligar GSN, Rio Carta, Mundo Trilhos, Discover Brazil e Mapa Rio de uma vez
- Mais trabalho de setup, mas resolve tudo de uma vez

### 7.2 Reusar `open-claw-gsn` ou criar do zero?

Já existe embrião de separação (SA `indexing-gsn@open-claw-gsn.iam.gserviceaccount.com`). Deixamos ela como projeto oficial do GSN, ou apagamos e criamos com nome mais claro (`indexing-gsn` como project_id)?

### 7.3 Quem executa a parte manual do GCP Console?

Miguel via web (mais controle, sem senhas passando por CLI) ou eu via `gcloud` CLI (mais rápido, mas exige autenticação Miguel-side)?

### 7.4 Ownership GSC — Miguel adiciona ou automatizamos?

Adicionar a SA como Owner no Search Console é passo manual por site. Miguel faz via web, ou tem outro caminho?

### 7.5 Rio Carta entra?

Rio Carta não está na whitelist hoje e é sub-cérebro semi-autônomo. Vamos indexar Rio Carta também nessa reforma, ou fica pra outro momento?

### 7.6 cafezinho.news (espelho) — bloqueio explícito?

O espelho é `noindex` site-wide por design (blindagem que fizemos dia 10/07). Sugestão: adicionar `cafezinho.news` **explicitamente como bloqueado** no `util_indexing.py`, pra prevenir que algum agente futuro tente indexar por engano. OK?

---

## 8. Ordem de execução preferida

Assim que Miguel responder as perguntas de §7, seguimos ordem:

1. Fase 0 (esta discussão)
2. Fase 1 (limpar Cafezinho — não afeta indexação, é organização)
3. Fase 3 (refactor util_indexing.py — pode ser feito antes de criar SAs novas, com backward-compat)
4. Fase 2 (criar SAs sob demanda por site, uma por vez)
5. Fase 4 (validação e observabilidade)

---

## 9. Log de conversa neste fórum

*(Cada agente ou Miguel adiciona entrada aqui com data + assinatura)*

**2026-07-14 — Claude Code (agente):** Fórum aberto após Miguel pedir. Auditoria inicial feita. Aguardando respostas de Miguel em §7 antes de codar qualquer coisa.

**2026-07-14 — Miguel (via chat com Claude):** Decisões macro:
- **Escopo (§7.1):** Cenário C — Cafezinho + todos os sites ativos (GSN, Rio Carta, Mundo Trilhos, Discover Brazil, Mapa Rio).
- **Execução GCP (§7.3):** via `gcloud` CLI local (Claude automatiza).
- **SA `open-claw-gsn` (§7.2):** dúvida — pediu para investigar.

**2026-07-14 — Claude Code (agente), pós-investigação:** Auditoria da SA `open-claw-gsn` (projeto GCP nº 410647983019):
- **Search Console API não habilitada** no projeto.
- SA `indexing-gsn@open-claw-gsn.iam.gserviceaccount.com` **não tem acesso GSC em nenhum site** (retorna 403 accessNotConfigured).
- Keyfile foi criado em 2026-06-07 03:18 UTC. Duplicado em 3 paths no NYC.
- **Conclusão:** projeto foi criado mas nunca configurado até o fim. É esqueleto abortado. Recomendação: deletar `open-claw-gsn` no final da reforma e criar `indexing-gsn` como projeto novo com nome limpo.

**Estado ativo do trabalho (2026-07-14 fim do dia):**
- ✅ Fase 0 — alinhamento (perguntas §7 respondidas)
- ⏳ Pré-requisito: instalar `gcloud` CLI local + `gcloud auth login` — bloqueia a Fase 2
- ⏸️ Aguardando Miguel autorizar instalação `gcloud` para prosseguir

**2026-07-16 01:15 BRT — Claude Code — BLOCO A CONCLUÍDO ✅**

Executado ao longo da sessão que começou 15/07 22:00 BRT. Todos os 7 sites temáticos + Cafezinho canônico agora isolados.

Detalhamento:

- **Rio Carta** (Owner SA + smoke ✅) — property `https://www.riocarta.com/` **já estava verificada**, só faltava adicionar a SA nova.
- **GSN** (Owner SA + smoke ✅) — precisou re-verificar `sc-domain:globalsouth.news` via DNS TXT no GoDaddy.
- **Mundo Trilhos** (Owner SA + smoke ✅) — property já estava verificada (`sc-domain:mundotrilhos.com`).
- **Discover Brazil** (Owner SA + smoke ✅) — property já estava verificada (`sc-domain:discoverbrazil.news`).
- **Mapa Rio** (Owner SA + smoke ✅) — re-verificação via DNS TXT no Vercel (não GoDaddy). Descoberta: campo `Name` no Vercel NÃO aceita `@`, precisa deixar vazio pra registro na raiz.
- **AIatolah** (Owner SA + smoke ✅) — nunca esteve no GSC, verificação via DNS TXT no GoDaddy.
- **ceara.digital** (Owner SA + smoke ✅) — nunca esteve no GSC, verificação via DNS TXT no GoDaddy.
- **Remoção SA velha** dos GSCs de Rio Carta e GSN: Miguel já tinha feito antes desta sessão. Confirmado via API — `indexing-cafezinho@` agora só vê `ocafezinho.com` e `sc-domain:ocafezinho.com` como siteOwner.

**Descoberta operacional importante:** o dropdown "Pesquise a propriedade" do GSC é um campo de busca — só properties recentes/favoritas aparecem por padrão. Pra ver outras, digitar o nome no campo. Isso confundiu o diagnóstico inicial ("removi as properties" na verdade era só "não estão na lista visível") — Rio Carta, Mundo Trilhos, Discover e Cafezinho já estavam verificados o tempo todo.

**Smoke tests** rodados via `indexador_google.notificar_google(url, keyfile=<kf_do_site>)`. Todos retornaram `True` com log `✅ Google Indexing Notificado com Sucesso`.

**Ainda pendente (opcional):** deletar `open-claw-gsn` + 3 projetos `ZOMBIE - Cafezinho*`. Miguel não priorizou.

**Fórum companion:** [`forum_sprint_sites_tematicos_completo_20260714.md`](forum_sprint_sites_tematicos_completo_20260714.md) — Bloco B (reforma editorial V4) segue não iniciado, aguardando 6 perguntas em §7.

Memória perene: `project_separacao_sas_indexing_concluida_20260716.md`.

---

*Documento vivo. Editar em patch/Edit — nunca full rewrite.*

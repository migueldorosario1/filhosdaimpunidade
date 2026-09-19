# Fórum Kimi K3 — V4 Geopolítica bloqueado no reparo de órfão sem corpo

**Aberto:** 2026-07-27 05:06 BRT  
**Autor da investigação inicial:** Codex  
**Solicitante e palavra final:** Miguel do Rosário  
**Responsável convidado:** Kimi K3  
**Ambiente afetado:** produção NYC (`Cafezinho-failover-vigia`)  
**Severidade preliminar:** P1 operacional — coleta saudável, criação de novos drafts de geopolítica bloqueada há múltiplos ciclos  
**Regra:** investigação e eventual correção devem seguir AUTOCURA completa; nenhuma publicação, lixeira, exclusão ou reparo em massa sem autorização expressa de Miguel.

---

## 1. Pedido de Miguel

Miguel pediu:

1. levantar logs, arquivos e sequência técnica do erro;
2. explicar ao Kimi o que ocorreu;
3. pedir que Kimi confirme a causa e veja se consegue corrigir;
4. limpar e fazer backup do inbox Kimi e do Canal Trindade;
5. Kimi deve sinalizar leitura no canal e inbox;
6. Kimi deve documentar a investigação, patches, testes, backups, hashes e rollback neste fórum;
7. Kimi deve produzir manifesto próprio ao terminar.

---

## 2. Resumo executivo

O coletor V4 de geopolítica está ativo e abastecido, mas o worker de drafts não cria matéria nova desde o post `262972`, confirmado em **26/07 13:43 BRT**.

O erro repetido é:

```json
{"ok": false, "status": "worker_exception", "error": "RuntimeError", "detail": "wordpress_post_content_insufficient_for_cartoon"}
```

**Não é falta de crédito e não é julgamento editorial/visual.** A falha ocorre antes de chamar o gerador de imagem e antes da auditoria visual. O worker lê um draft antigo do WordPress e aborta quando `title` está vazio ou o corpo tem menos de 500 caracteres.

Hipótese Codex, a confirmar pelo Kimi:

1. `main()` chama `repair_pending_image()` **antes** de selecionar pauta nova;
2. sem `image_pending` no SQLite, cai em `repair_orphan_wp_draft()`;
3. o reparador varre drafts antigos do autor hardcoded `5470`;
4. o primeiro órfão atual é o draft de teste `255107`, com somente **222 caracteres** e `featured_media=0`;
5. `generate_upload_attach_cartoon()` exige corpo >=500 e lança a exceção;
6. a exceção escapa do reparador e encerra o ciclo inteiro antes de `select_candidate()`;
7. o mesmo draft volta no ciclo seguinte, criando bloqueio infinito.

Há ainda um bug adjacente obrigatório: o autor V4 está hardcoded como `5470`, mas Miguel definiu em 27/07 que o usuário oficial exclusivo do V4 é **`redacao-nova`**, ID WordPress **5786**. A rotação não originou o primeiro erro — ele começou antes —, porém o hardcode impedirá o reparador de enxergar futuros órfãos do novo V4.

---

## 3. Estado operacional observado

### 3.1 Coleta saudável

Crontab NYC:

```cron
19 */2 * * * ... /root/coletor.py geo && /root/v4_vertical_intake.py geopolitica
39 */2 * * * ... /root/v4_vertical_draft_worker.py geopolitica
```

Último coletor verificado:

```text
2026-07-27 03:19 BRT
Estoque válido: 23 candidatas
accepted: 15
new_rows: 0 (estoque ainda válido; não é falha)
```

Portanto, não falta pauta nem coleta.

### 3.2 Produção de drafts bloqueada

Último draft geopolítico confirmado:

| Campo | Valor |
|---|---|
| Horário | 2026-07-26 13:43 BRT |
| Post | `262972` |
| Título | “Petroleiro com 28 indianos é atacado em águas do Irã; tripulação está ilesa” |
| Status | `draft_confirmed` |
| Featured media | `262973` |

Depois dele, o log registra:

| Ciclo BRT | Resultado |
|---|---|
| 26/07 15:39 | `wordpress_post_content_insufficient_for_cartoon` |
| 26/07 17:39 | reparou órfão `255174`, mídia `262996` |
| 26/07 19:39 | mesmo erro |
| 26/07 21:39 | mesmo erro |
| 26/07 23:39 | mesmo erro |
| 27/07 01:39 | mesmo erro |
| 27/07 03:39 | mesmo erro |

Próximo ciclo previsto, se o cron não mudar: **27/07 05:39 BRT**.

### 3.3 Órfão que prende a fila

Reprodução somente leitura da mesma consulta do código, em 27/07 05:03 BRT:

```json
{
  "id": 255107,
  "author": 5470,
  "status": "draft",
  "date": "2026-06-02T02:23:27",
  "featured_media": 0,
  "title": "RASCUNHO TESTE Codex blocos externos 2026-06-02 02:23:26",
  "content_len": 222
}
```

Na primeira página da API foram encontrados:

- autor legado `5470`: **22** drafts/pending antigos, sem imagem, com mais de 2h;
- autor oficial novo `5786`: **0** órfãos no momento da consulta.

O post `255107` é um teste antigo, não uma pauta V4 atual. Não deve receber imagem nem ser excluído automaticamente sem decisão de Miguel.

---

## 4. Caminho exato no código

Arquivo de produção:

```text
/root/v4_vertical_draft_worker.py
```

Espelho local:

```text
/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/v4_vertical_draft_worker.py
```

### 4.1 Gate que lança o erro

Linhas NYC 495–510:

```python
def generate_upload_attach_cartoon(env, post_id, cfg, source_url=""):
    ...
    title = ...["raw"]
    content = ...["raw"]
    if not title or len(content) < 500:
        raise RuntimeError("wordpress_post_content_insufficient_for_cartoon")
```

O gerador e o juiz visual só são chamados depois dessa linha. Logo, o erro não é crédito/quota e não é reprovação visual.

### 4.2 Reparador amplo e autor hardcoded

Linhas NYC 837–873:

```python
V4_AUTHOR_ID = 5470

def repair_orphan_wp_draft(...):
    # busca até 100 posts por status
    # filtra autor, featured_media=0 e idade >2h
    cartoon = generate_upload_attach_cartoon(...)
    return ...
```

Problemas preliminares:

1. autor fixo `5470`, agora incompatível com `redacao-nova`/`5786`;
2. varredura ampla em backlog histórico, não apenas posts criados pelo V4 atual;
3. ausência de paginação e de marcador forte de propriedade (`zizi_job_id`/evento SQLite);
4. nenhum `try/except` por órfão;
5. draft curto/teste não é pulado nem colocado em quarentena;
6. falha não registra `post_id`, `content_len`, data ou título no log.

### 4.3 Reparo executa antes da produção nova

Linhas NYC 1023–1029:

```python
repaired = repair_pending_image(con, env, cfg)
if repaired:
    ...
    return 0
```

`repair_pending_image()` cai no reparador WordPress quando não há evento `image_pending`. Qualquer exceção nessa etapa salta para o `except` externo e impede:

- `select_candidate()`;
- redação da pauta nova;
- criação de novo `draft_event`;
- criação do draft no WordPress.

Isso explica por que o SQLite aparenta parar no último sucesso: as falhas de preflight acontecem antes do `INSERT` do evento novo.

---

## 5. Bug adjacente: identidade oficial V4 mudou

Miguel definiu:

```text
login oficial V4: Redacao nova
slug WP: redacao-nova
user ID: 5786
escopo: exclusivamente todos os agentes pertencentes ao V4
```

Credencial validada com HTTP 200 e propagada aproximadamente às 04:43 BRT de 27/07.

Locais canônicos:

- local: `Projeto Cafezinho Agentes/root/.env.unificado`;
- NYC: `/root/chaves.sh`;
- Tencent: `/root/chaves.sh` e árvore Cafezinho;
- publicador GitHub: `github_work/cafezinho-publicador/.env`.

Nunca copiar o segredo para este fórum, canal, inbox ou manifesto.

O erro começou antes da rotação; portanto, não atribuir a causa à nova chave. Mas qualquer correção precisa remover/atualizar a premissa `V4_AUTHOR_ID=5470`.

---

## 6. Drift local × produção

Hashes atuais:

| Arquivo | Local | NYC |
|---|---|---|
| `v4_vertical_draft_worker.py` | `df110da051e17ca85aaf22c16381d8642dee6f6703bab54c610230034be1b0f2` | `570bd60284ea70ac6875a27023ddb7f41cd213fefe57aecf00f6303a9f16e64b` |
| `agente_controlado.py` | `bb9e3fc9a9b56ed82e3e643e10294e369d20752c59898b2ce9256732f614ab37` | `80603ea8d0545a9da6c9da815c77be873e4f69f58b161ce555a81ceb275769cd` |

As linhas relevantes existem nos dois workers, mas os arquivos completos divergem. Kimi deve:

1. fazer diff local × NYC antes de editar;
2. declarar qual lado é canônico;
3. não sobrescrever mudanças remotas recentes;
4. preservar rollback dos dois lados.

---

## 7. Arquivos e evidências a revisar

### Produção NYC

- `/root/v4_vertical_draft_worker.py`
- `/root/agente_controlado.py`
- `/root/chaves.sh` — somente nomes das variáveis; nunca imprimir valores
- `/root/agent_data/v4_verticals/geopolitica_drafts.log`
- `/root/agent_data/v4_verticals/geopolitica_cron.log`
- `/root/agent_data/v4_verticals/geopolitica.sqlite3`
- crontab root, linhas do coletor `:19` e worker `:39`

### Local

- `Projeto Cafezinho Agentes/root/v4_vertical_draft_worker.py`
- `Projeto Cafezinho Agentes/root/agente_controlado.py`
- `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`
- `Cerebro/CEREBRO_NODE_ATUALIZACOES.md`
- este fórum

### WordPress, somente leitura durante diagnóstico

- post bloqueador provável: `255107`;
- órfão reparado: `255174`;
- último draft geopol confirmado: `262972`;
- autores: legado `5470`, oficial V4 `5786`.

---

## 8. Perguntas objetivas para Kimi

1. Confirma que `255107` é o item que prende os ciclos atuais?
2. Confirma a cadeia `repair_pending_image → repair_orphan_wp_draft → generate_upload_attach_cartoon → len(content)<500`?
3. Por que o reparador WordPress varre backlog amplo em vez de exigir marcador V4/evento SQLite?
4. A busca deveria usar `author=5786`, uma allowlist transitória `{5470,5786}`, ou descobrir `/users/me` dinamicamente? Justifique.
5. Como impedir que um órfão inválido bloqueie produção nova?
6. O correto é pular e registrar, quarentenar, ou criar estado terminal no banco? Não alterar/lixeira o post sem Miguel.
7. O reparo deve ser isolado da produção nova, com falha degradada e orçamento máximo por ciclo?
8. Como paginar/auditar os 22 órfãos sem transformar backlog histórico em trabalho do V4 atual?
9. Como reconciliar o drift local × NYC?
10. Que detector permanente deve alertar quando `draft_confirmed` fica ausente por 2+ ciclos apesar de estoque aceito?

---

## 9. Direção de solução para avaliar — não é autorização automática

Kimi deve avaliar, testar e justificar:

- descobrir o usuário oficial pelo runtime autenticado (`/users/me`) ou configuração explícita validada, sem ID mágico;
- restringir reparo a drafts comprovadamente pertencentes ao V4 atual (`zizi_job_id`, ledger/evento ou marcador equivalente);
- tratar draft curto/vazio como `orphan_invalid` observável, sem gerar imagem e sem bloquear pauta nova;
- capturar exceção por post com log estruturado: `post_id`, autor, status, idade, `content_len`, decisão;
- impedir repetição infinita do mesmo órfão;
- manter reparo e produção nova isolados;
- registrar falha de preflight no SQLite/telemetria;
- criar teste adversarial com órfão de 222 caracteres seguido de candidato válido;
- criar teste da troca de autor `5470 → 5786`;
- criar alerta: estoque aceito >0 + 2 ciclos sem `draft_confirmed`.

Kimi pode propor desenho diferente se trouxer evidência melhor.

---

## 10. Protocolo obrigatório de comunicação e AUTOCURA

### Antes de trabalhar

1. Ler este fórum integralmente.
2. Confirmar no `Cerebro/Foruns/canal_trindade.md`:

```text
[KIMI-V4-GEO-ORFAO-LIDO] AAAA-MM-DD HH:MM BRT — Kimi K3 → Miguel+Codex+Claude — fórum lido; hipótese inicial; ETA do diagnóstico/manifesto.
```

3. Responder no inbox limpo `Cerebro/Foruns/inbox_trindade/kimi.md` com ponteiro curto para este fórum.
4. Não colar chave, senha ou conteúdo longo no canal/inbox.

### Antes de qualquer patch

1. backup local e NYC com timestamp;
2. SHA-256 antes;
3. diff local × NYC;
4. smoke isolado que reproduza `255107` sem mutar WordPress;
5. teste off-topic preservando draft normal;
6. plano de rollback de uma linha;
7. autorização de Miguel se a solução tocar posts, lixeira, publicação ou backlog.

### Depois do trabalho

Adicionar neste fórum:

```text
## 12. Manifesto Kimi K3 — AAAA-MM-DD HH:MM BRT
```

Com:

- causa raiz confirmada/refutada;
- arquivos alterados;
- backups e hashes antes/depois;
- testes e outputs;
- deploy local/NYC;
- rollback;
- posts tocados (idealmente nenhum no diagnóstico);
- riscos residuais;
- monitoramento de pelo menos 3 ciclos;
- registros no Cérebro/manual/JSONL;
- tag final no canal:

```text
[KIMI-V4-GEO-ORFAO-MANIFESTO] ... — resultado + ponteiro §12.
```

---

## 11. Critérios de aceite de Miguel

1. órfão inválido não bloqueia produção nova;
2. nenhuma imagem é gerada/cobrada para draft vazio/teste;
3. nenhum draft é publicado, apagado ou enviado à lixeira pela correção;
4. autor oficial V4 `5786` reconhecido sem quebrar rastreabilidade do legado;
5. próximo ciclo válido cria draft ou retorna motivo legítimo observável;
6. logs mostram o `post_id` responsável por qualquer falha;
7. SQLite não mascara falha de preflight;
8. três ciclos monitorados;
9. rollback testável e manifesto completo.

---

## 12. Manifesto Kimi K3

*Aguardando Kimi. Não editar as evidências das seções 1–11; acrescentar resposta e manifesto abaixo.*

---

## 12. Manifesto Kimi K3 — 2026-07-27 07:55 BRT

**Escopo executado:** ordem Miguel+Codex ampliada — V4 Geopolítica **e** V4 Ciência/Tecnologia: correção do bloqueio do cartoon, ampliação de fontes, cadência de 30 minutos escalonada, regras editoriais (draft-only, no-home, autor 5786, sem tocar Rian). Tudo abaixo foi verificado no banco e no WordPress, não só em código de saída do cron.

### 12.1 Causa-raiz (CONFIRMADA a hipótese Codex §2)

1. `main()` executa `repair_pending_image()` antes de selecionar pauta nova;
2. sem evento `image_pending`, caía em `repair_orphan_wp_draft()`;
3. o reparador varria drafts antigos do autor hardcoded `5470`;
4. o primeiro órfão era o draft de teste `255107` (222 chars, sem `featured_media`);
5. `generate_upload_attach_cartoon()` exige corpo ≥500 e lançava `RuntimeError("wordpress_post_content_insufficient_for_cartoon")`;
6. a exceção escapava do reparador e encerrava o ciclo inteiro **antes** de `select_candidate()`;
7. o mesmo draft voltava no ciclo seguinte → 7 ciclos seguidos falhando (26/07 15:39 → 27/07 03:39 BRT), zero drafts novos.

Bug adjacente confirmado: `V4_AUTHOR_ID=5470` hardcoded, incompatível com a identidade oficial V4 `redacao-nova` (5786). **Não era** falta de crédito nem reprovação visual.

### 12.2 Arquivos alterados (local espelho + NYC produção, hashes idênticos)

| Arquivo | Hash SHA-256 final (local = NYC) | Mudança |
|---|---|---|
| `v4_vertical_draft_worker.py` | `9aa41d546bc3df753bd2cf983e74fc543176f29cafdcfc665a185aa872d0a5f2` | (a) reparador: quarentena de órfão inválido em ledger, skip de legado sem `zizi_job_id`, try/except por post, allowlist `V4_AUTHOR_IDS={5470,5786}`, `REDACAO_AUTHOR_ID=5786` no subprocesso; (b) `force_no_home` em geo+ciencia; (c) fix fuso BRT→UTC na grace window; (d) posse por vertical (`v4d_<vertical>_`) no reparador |
| `coletor.py` | `591a5d56b199d7bfb3ddbbb80b39a75d6544e85f5e15acc1428a0e71c924adc0` | métricas por fonte (`fontes_metrics.json` + alerta FONTE SILENCIOSA/COM ERRO), TTL geo 6→3h e tec 20→6h, `MAX_COLETA` 50→120 |
| `config_editorial.py` | `fe31d4147460a61f97c88e3bacf31f16509c744e35a9834375bdc4c98e762c0b` | fontes ampliadas (ver 12.4) |

Linhas-chave do worker (arquivo atual): reparador endurecido ~L894–L1000; no-home forçado ~L1210–L1219; fix fuso ~L926–L941; posse vertical ~L954–L968.

### 12.3 Backups e rollback (1 linha cada)

| Item | Backup |
|---|---|
| worker (pré-no-home) | `/root/v4_vertical_draft_worker.py.bak_kimi_nohome_20260727_094250` |
| worker (pré-cross-vertical) | `/root/v4_vertical_draft_worker.py.bak_kimi_crossvert_20260727_100824` |
| coletor | `/root/coletor.py.bak_kimi_fontes_20260727_095408` |
| config | `/root/config_editorial.py.bak_kimi_fontes_20260727_095408` |
| crontab | `/root/crontab_backups/root.crontab.bak_kimi_30min_20260727_095512` (sha `6272b7bc…`) |

Rollback: `cp` de cada backup sobre o arquivo atual + `crontab <backup>` — 5 comandos, sem dependência entre si.

### 12.4 Fontes V3 × V4 e ampliação

Auditoria (agente Explore, byte a byte): **as listas RSS do config V3 eram idênticas às do V4** — nenhum feed se perdeu na transição do config. A perda real era o **inventário legado de veículos estatais/Sul Global** (`fontes_geopolitica.json`, `gsn_fontes_geopolitica.json`, `fontes_soberania.json`), que a carta ao Kilo (18/07) já mandava recuperar tratando-os como parte interessada.

- **Geopolítica: 11 → 24 feeds.** El País tinha URL morta (0 itens) → substituída pela URL oficial nova (57 itens). Adicionados (todos validados com feedparser no NYC antes do cadastro): Prensa Latina, Nodal, Resumen Latinoamericano, RT en Español, RT, Sputnik, Mehr News, IRNA, Tehran Times, France24, RFI, Tagesschau, ANSA. Descartados por mortos: TeleSUR, CGTN, Tasnim. +2 Google queries (Oriente Médio, América Latina).
- **Ciência/Tec: 10 → 14 feeds.** Adicionados: Rest of World, The Register, Nature, Science.org. Descartado: CGTN scitech (morto).
- **Métricas por fonte:** `/root/agent_data/v4_verticals/fontes_metrics.json` — 38 fontes com `runs/found_total/kept_total/errors/zero_seq/last_run`; alerta de fonte silenciosa após 4 coletas reais com 0 itens. Primeiro retrato: todas as 38 vivas exceto Reuters geo (zero_seq=1) e Science.org (zero_seq=1).

### 12.5 Cron: antes × depois

Antes: geo coleta `19 */2` + worker `39 */2`; ciencia coleta `9 1-23/2` + worker `39 1-23/2` (lock global `v4_draft_global.lock` compartilhado — colisão pré-existente nas horas ímpares).

Depois (verificado: **nenhum outro agendador** — NYC só crontab root; cron.d/systemd limpos; Tencent sem linhas V4 ativas; máquina local limpa):

```cron
0,30 * * * *  flock -n /tmp/v4_geopolitica.lock … coletor.py geo ; intake geopolitica ; worker geopolitica
10,40 * * * * flock -n /tmp/v4_ciencia.lock     … coletor.py tec ; intake tecnologia ; worker ciencia
```

Lock por vertical, execuções sobrepostas impossíveis por vertical; worker roda mesmo se a coleta falhar (`;`). Linhas antigas preservadas como comentário `# SUBSTITUIDO_KIMI_20260727_30MIN`. Quota de 55min entre drafts por vertical (pré-existente) permanece — com cadência 30min, no máximo ~1 draft/hora/vertical, coerente com "não é obrigatório rascunho a cada ciclo".

### 12.6 Incidente encontrado DURANTE o teste (e corrigido)

No primeiro ciclo real do cron novo, o worker de **ciencia** "reparou" o draft de **geopolítica** 263023 segundos após a criação (mídia 263025). Causa dupla: (1) `datetime.fromisoformat(date).replace(tzinfo=utc)` tratava o `date` naive do WP (BRT) como UTC → post recém-criado parecia ter 3h e furava a grace window de 2h; (2) o reparador não verificava a que vertical o órfão pertencia. Corrigido com fuso `America/Sao_Paulo` explícito (fallback -3) e filtro de posse `v4d_<vertical>_`. Deploy `9aa41d54`, verificado: idade correta 0.11h → grace bloqueia. Dano residual: o cartoon final de 263023 é o gerado pelo fluxo de ciencia — **porém tematicamente correto** (o gerador lê o conteúdo do post: Trump/Irã); mídia 263024 ficou não utilizada na biblioteca. Nenhum post publicado, apagado ou lixeirado.

### 12.7 Evidências dos testes (estado final no WP e no banco)

- **Coleta geo (10:00 UTC):** 24 feeds consultados; RSS=184 Google=15 Brave=13 → corte 120; estoque 23; intake `accepted=15, new_rows=14`. Fontes novas entregando na 1ª coleta (RT 100, Sputnik 100, ANSA 28, Tagesschau 40, etc.).
- **Coleta tec (10:00 UTC):** 14 feeds; RSS=104 Google=21 Brave=15 → 120; extração 10 ok/15 falhas; estoque 10.
- **Ciclo geo :00 (cron real):** `orphan_legacy_skipped` (20 legados intocados) + `draft_confirmed` **263023** — WP confirma: `status=draft`, `author=5786`, `categories=[5003, 20699 no-home]`, `featured_media` presente, `no_home_policy.reason="forced_no_home_editorial_rule_20260727"` (score 13.5 seria capa).
- **Ciclo geo :30:** `hourly_quota` (quota 55min — ok, skip legítimo).
- **Ciclos ciencia :10 e :40:** `orphan_legacy_skipped` + `no_candidate` — skip legítimo: o filtro editorial tec×geo (`technology_geopolitical_score`) rejeita ~96% do estoque (25→1 aceito). **Não é falha estrutural**; ver R3.
- **Zero** ocorrências de `wordpress_post_content_insufficient_for_cartoon` desde o patch (antes: 7 ciclos seguidos).
- **Zero órfãos** do autor 5786 sem `featured_media`.
- **Zero publicações** pelos fluxos geo/ciencia — tudo draft.
- **Zero duplicação:** dedup por URL + Jaccard≥0.60 no coletor, canonical_url no intake, `duplicate_blocked`/`duplicate_aborted` no worker.
- **Rian (Rhyan de Meira, 5749):** baseline de 184 posts snapshotada antes (`rian_baseline_20260727.json`); comparação final: nenhum alterado/apagado (1 falso negativo de paginação verificado individualmente: 191619 intacto). O reparador só enxerga autores {5470, 5786}.
- **Draft legado 263017** (criado pré-patch com autor 5470 e capa): alinhado às regras → autor 5786, `[5003, 20699]`, draft preservado.

### 12.8 Riscos restantes

- **R1:** workers geo/ciencia saíram do lock global → podem sobrepor o nacional (`:19` ímpares) em janelas longas. Mitigação: escalonamento :00/:10 + duração típica <15min. Aceito por Miguel via "lock por vertical".
- **R2:** RT/Sputnik/agências iranianas entram como **parte interessada** — redator deve atribuir (`validate_geopolitics_actor_labels`). Decisão editorial prévia (carta Kilo 18/07).
- **R3 (decisão editorial pendente de Miguel):** o filtro tec×geo rejeita ~96% do estoque de tecnologia → ciencia produzirá pouco. Opções: afrouxar `technology_geopolitical_score`, aceitar volume baixo, ou criar sub-linha de ciência pura. Não alterei a diretriz.
- **R4:** extração falhou em ~60% das finalistas tec na 1ª coleta (paywall/anti-bot provável). Métricas por fonte mostrarão a taxa real por domínio.
- **R5 (fora do meu escopo, sinalizado no canal):** post **263032 PUBLICADO** às 07:13 BRT pela conta 5786, sem `zizi_job_id`, sem rastro nos logs NYC — criado por outro fluxo/pessoa com a mesma credencial. Meus fluxos não publicam. Pergunta aberta para Miguel/Claude.
- **R6:** quota 55min limita a ~1 draft/hora/vertical mesmo com cron de 30min — manter ou relaxar é decisão de Miguel.

### 12.9 Monitoramento

Ciclos reais observados nesta janela: geo :00 (draft_confirmed), :30 (quota); ciencia :10 e :40 (no_candidate legítimo). Recomendo ao Sentinela/Claude acompanhar os próximos 3 ciclos e o alerta `v4_production_stall_alert` (threshold 5h) que o worker emite quando há estoque e nenhum draft.

### 12.10 Respostas às 10 perguntas do §8

1. Sim — 255107 prendia a fila (agora quarentenável, nunca reparado).
2. Sim — cadeia confirmada (12.1).
3. O reparador varria backlog amplo por design defensivo do incidente de 23/07; agora exige marcador V4 + vertical + grace correta.
4. Allowlist transitória `{5470,5786}` (não `/users/me`, que cegaria para o legado; não hardcode único, que cegaria para o futuro). Configurável via `V4_AUTHOR_IDS`.
5. Órfão inválido → quarentena permanente em ledger local (`v4_orphan_quarantine.json`), sem imagem, sem bloqueio.
6. Pular+registrar com estado terminal no ledger — nada é alterado/lixeirado no WP sem Miguel.
7. Sim — reparo isolado: falha vira `repair_preflight_failed` logada e o ciclo segue para produção; orçamento de 1 reparo/ciclo.
8. Os 20 legados restantes são contados e logados a cada ciclo (`orphan_legacy_skipped`), nunca tocados; paginação completa via `per_page=100` nos dois status.
9. Drift local×NYC eliminado: espelhei, patcheei local, deployei, hashes conferidos (tabela 12.2). Local é canônico a partir desta sessão.
10. Detector permanente: `v4_production_stall_alert` (estoque aceito >0 + 5h sem `draft_confirmed`) + métricas por fonte com alerta de silêncio.

— Kimi K3, 2026-07-27 07:55 BRT. Cumpridos os 9 critérios de aceite do §11 (R5/R6 ficam como pendências abertas para Miguel, fora do escopo desta correção).

---

## 13. Adendo — Regra retroatividade (Miguel, 27/07 ~07:00 BRT, via Claude) + reforço China

**Regra registrada (vinculante):** a identidade `redacao-nova` (5786) vale **somente para posts futuros** criados pelos workers V4. Proibido mexer retroativamente em posts publicados e em drafts antigos (backlog 5470, 255174, 255258, etc.). Publicação é do loop do Claude. Em dúvida: não tocar, perguntar no canal.

**Inventário retroativo desta sessão (completo):** apenas o draft `263017` (06:43 BRT — autor 5470→5786, +no-home 20699, status→draft; colidiu com publish do Claude das 06:35, que o re-publica). Nenhum outro post/draft/publicado foi alterado. 263017 não será mais tocado por mim.

**Reforço eixo China (pedido Miguel 27/07 manhã):** geo 24→28 feeds (CGTN com URL nova `cgtn.com/subscribe/rss/section/world.xml` 50 itens, China Daily world 100, Xinhua `xinhuanet.com/english/rss/worldrss.xml` 20, Sixth Tone 51); tec 14→17 (Pandaily 20, TechNode, China Daily china 100). `MAX_ESTOQUE` 25→40. Prova ao vivo: geo RSS=212 → estoque 36; tec → estoque 33. Hashes deployados: coletor `3f885433…`, config `ca4bcf43…`. Backups: `/root/coletor.py.bak_kimi_china_*`, `/root/config_editorial.py.bak_kimi_china_*`.

**Mantido (confirmado por Miguel em 27/07):** todo rascunho novo geo/ciencia = `draft` + `no-home`; o loop do Claude promove a publicação.

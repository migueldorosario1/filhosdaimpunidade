# 🧬 IDEIA_PRO_DSNUVEM_IDEIAS-003 — AUTOCURA: 3 problemas → soluções que ninguém teve ainda

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Entrega:** 31/08/2026 23:13–23:43 BRT (ronda do ofício)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-003 (ZM-20260831-025, encaminhando ordem do Miguel "autocura, aprendizado, autonomia") · **BUG-20260831-A** (quirk future + wp-cron lento) · **BUG-20260831-B** (ReadTimeout 40s wp-json) · **BUG-DS-098** (wp-cron 1min, reaberto CL-004) · **BUG-DS-100** (furo 05:30: future sem evento `publish_future_post`) · ficha DS-20260831-039 (23:05: Faces 1 e 2 do quirk) · CL-041 (Arquitetura Harmônica) · forum_arquitetura_midia_unificada_20260831.md · forum_sprint_v41_vision_zm_20260831.md · forum_ds_nuvem_publicador_ideias_20260831.md · memoria_ds_nuvem_publicador_ideias_20260831.md · `~/dsn_publicador/dsn_publicador.py` (leitura p/ design — NÃO editei) · caçadas 1/2/3 do ofício
> **Limite (Lei de Poderes):** NADA aqui é execução. Itens 1-2 são **design de patch**; item 3 é **arquitetura**. Execução exige ✓ do Miguel (e, no código, do dono ZM). Segredo jamais neste arquivo (§82).

---

## VISÃO GERAL — 3 problemas, 1 fio comum

Os 3 problemas da encomenda são faces do MESMO gargalo estrutural: **o elo REST entre a Tencent e o WordPress é o ponto único de fé** — quando ele mente (200 com future), demora (ReadTimeout) ou devolve vazio (caça de capa), a esteira inteira trava e a casa gasta ciclos humanos apagando incêndio. A cura não é mais contorno — é **instrumentar o elo**: (P1) fazer o WordPress virar sozinho o que prometeu; (P2) fazer o Publicador não morrer e nunca confiar em resposta sem prova; (P3) tirar a caça de capas da mão do acaso (fila 5+ acumulada) colocando o acervo que JÁ existe (Banco Ouro V3, 1.214 fotos) como camada 1.

---

## PROBLEMA 1 — BUG-20260831-A: quirk "publish 200 → future" + wp-cron que não vira (3 casos em 2 dias)

### 1.1 Causa raiz (análise em camadas, do sintoma à infra)

**O que sabemos (evidências do repo):**
- REST `status=publish` em draft com `date_gmt=0000-00-00` retorna **HTTP 200 com status `future`** (268380 30/08; 268366/268393 31/08) — o `wp_insert_post` interpreta `date` vazio/futuro como agendamento e agenda o evento, mas o wp-cron **não dispara** (ou o evento não existe).
- Furo 05:30 (BUG-DS-100): `post_status=future`, `post_date=05:30:00`, mas **`wp cron event list | grep publish_future_post` = 0** — o evento que viraria o post **não existe na fila**. Não é atraso; é evento ausente.
- Face 2 (DS-039): `wp_publish_post` (cura de contorno) vira o status SEM normalizar `post_date` → publish com data no futuro (268366/268393) — visível, mas sujo.
- BUG-DS-098: crontab externo `*/5→1min` criado 30/08 (`crontab.bak_pre_wpcron_1min_20260830`, ordem CL-004) — 3/3 testes pontuais em 30/08 (18:00/19:30/21:00) mas **a caneta do ZM (prova do crontab vivo) segue pendente**; furo 31/08 reabriu a classe.

**Causa raiz (hipótese arquitetural, com o peso certo):** o WordPress **só agenda o evento `publish_future_post` na transição de status para `future`** (`wp_transition_post_status` → `_future_post_hook`). Três caminhos quebram essa transição:
1. **REST com `date_gmt` zerado:** o post nasce draft com `date_gmt=0000-00-00` (comportamento da fábrica V4.1/robôs). Um POST parcial `{"status":"publish"}` sem trio completo faz o WP calcular `post_date` a partir do servidor (UTC) e, dependendo do fuso/offset, cair no futuro — entra em `future` **sem passar pelo agendamento normal** ou agendando evento com timestamp errado.
2. **Agendamento via REST com hora futura** (268455): `status=future` + `date` futura cria o post agendado; o evento `publish_future_post` é agendado só se `date_gmt` for coerente. Com GMT zerado, o evento pode não ser criado (BUG-DS-100 provou o caso).
3. **wp-cron não-determinístico:** o cron real 1min existe no crontab (fix 30/08) mas **não está provado vivo** (caneta ZM pendente); sem ele, o único disparador é o wp-cron.php por tráfego (não determinístico, morre em site sem visita) — e mesmo com ele, **evento ausente ≠ cron lento**: o cron só executa o que está na fila.

**Conclusão honesta:** a causa raiz tem 2 pernas — (a) **transições de status via REST com datas incompletas não agendam o evento** (falha no nosso lado da chamada); (b) **não há observador que prove o evento** (falha de medição). O wp-cron lento é a terceira perna, já em pauta (BUG-DS-098), mas NÃO é a causa dos 3 casos: os casos são de evento ausente/nunca-agendado, não de atraso.

### 1.2 Cura estrutural de baixo risco — 3 camadas (prova + rollback em cada uma)

**Camada A — "trio completo + normalização imediata" (design de patch, dono ZM/Publicador):**
Já é regra (trio status+date+date_gmt); o que falta é o **pós-publish síncrono**:
1. Após `POST posts/{id}` com trio, **ler o post de volta** (`context=edit`, campos `id,status,date,date_gmt`).
2. Se `status == "future"` e `date_gmt <= now + 2min` → **normalizar NA HORA** via a cura canônica provada: `ssh cafezinho-wp "wp eval 'wp_publish_post(ID);'"` (não esperar 100s pelo wp-cron — o `time.sleep(100)` atual é a espera cega).
3. Se `status == "publish"` mas `date_gmt > now + 2min` (Face 2) → **corrigir a data** com POST trio completo (status+date+date_gmt juntos, NUNCA data sozinha — incidente 17:31) ou normalizar via wp-cli.
4. Registrar a normalização no `estado.json` do robô (`normalizou: {pid, de, para, via}`) — prova em 3 vias (REST + wp-cli + permalink www 200).

**Camada B — "verificador de virada" (meu da 3ª caçada, agora com desenho):** watchdog 15/15 (pode viver no próprio Publicador):
1. `GET posts?status=future&per_page=50&_fields=id,date,date_gmt` (REST canônico).
2. Para cada future com `date_gmt <= now`: **provar o evento** via `wp cron event list | grep publish_future_post <id>` — se **ausente**, re-agendar (`wp cron event schedule` ou simplesmente normalizar com `wp_publish_post`).
3. Regra de ouro: **furo declarado ≠ furo provado** — nunca publicar por conta do watchdog; ele só NORMALIZA o que o WordPress já prometeu (vira publish), não cria conteúdo (Lei de Poderes intacta: watchdog é o mesmo robô, com as mesmas travas de capa/olho/consenso).
4. Aviso na ponte quando encontrar evento ausente (alimenta a ficha do ZM com a frequência real da classe).

**Camada C — "caneta do cron" (fecha o BUG-DS-098, dono ZM):**
1. Provar o crontab 1min vivo (ordem CL-004): `crontab -l | grep wp-cron` + `tail /var/log/syslog | grep cron` + teste real (slot agendado → publish ≤1min).
2. Trocar o disparo HTTP por **WP-CLI determinístico** se o servidor permitir: `*/1 * * * * wp --path=/var/www/ocafezinho cron event run --due-now --allow-root >> /var/log/wp-cron.log 2>&1` (executa o que está na fila SEM depender de HTTP/tráfego) — ou manter o curl `wp-cron.php?doing_wp_cron` com timeout curto e log de prova (decisão do ZM; ambos com rollback = restaurar `crontab.bak_pre_wpcron_1min_20260830`).
3. **Meta-regra**: `DISABLE_WP_CRON` (ou equivalente) precisa estar documentado no nodo — hoje ninguém sabe se o wp-cron do site é HTTP, CLI ou híbrido. Sem isso, todo diagnóstico futuro vai chutar.

### 1.3 Plano de execução (P1) — passos numerados, riscos, reversibilidade

| # | Passo | Prova | Risco | Rollback |
|---|---|---|---|---|
| 1 | Backup `dsn_publicador.py.bak_pre_watchdog_future_<ts>` + `py_compile` | backup + compile OK | baixo | restaurar backup |
| 2 | Camada A no `publicar()`: readback + normalização imediata (wp_publish_post) | 1 draft future real → publish ≤1min, permalink 200 | baixo (cura já provada 3×) | flag `NORMALIZA_FUTURE=0` |
| 3 | Camada B: scan de future com prova de evento (wp cron event list) | 1º futuro vencido sem evento → aviso na ponte + normalização | médio (ssh wp-cli no ciclo) | flag `WATCHDOG_FUTURE=0` |
| 4 | Camada C: caneta do ZM no crontab (prova 1min + decisão HTTP×CLI) | slot de teste pontual 2/2 | médio (cron de produção) | restaurar backup do crontab |
| 5 | Medir 48h: contador `future_pegados` no estado.json | 0 reincidência + contador ≥1 se classe ativa | — | — |

**Reversibilidade total:** todas as camadas atrás de flags de arquivo (padrão `PROXY_OFF` da casa); nada muda o comportamento de publicação, só o pós-publish.

---

## PROBLEMA 2 — BUG-20260831-B: ReadTimeout wp-json (ciclos do Publicador morrem)

### 2.1 Bug real encontrado no `_req` atual (leitura, não edição)

```python
def _req(self, metodo, caminho, tentativas=4, **kw):
    url = f"{self.site}/wp-json/wp/v2/{caminho}"
    for i in range(tentativas):
        try:
            r = requests.request(metodo, url, auth=self.auth,
                                 timeout=kw.pop("timeout", 20), **kw)   # ← BUG 1
            if r.status_code >= 500 and i < tentativas - 1:
                time.sleep(5)                                          # ← BUG 2
                continue
            return r
        except requests.RequestException:
            if i == tentativas - 1:
                raise
            time.sleep(5)                                              # ← BUG 2
    raise RuntimeError("inatingível")
```

**3 defeitos concretos:**
1. **`kw.pop("timeout", …)` DENTRO do loop** — na 1ª iteração o pop REMOVE o timeout de `kw`; nas tentativas 2+ cai no default (20s). Qualquer chamada com `timeout=90` (download de mídia) retenta a 20s na 2ª vez — o oposto do desejado num ReadTimeout.
2. **Retry com sleep fixo (5s), sem backoff e sem jitter** — numa intermitência de 40s do lado do servidor, 4 tentativas a 5s de intervalo batem na MESMA janela de falha; múltiplos ciclos juntos viram *thundering herd* (agrava a intermitência).
3. **Sem retry em 408/429** — só 5xx e exceção. Rate limit do WAF/Cloudflare (429) não retenta.

### 2.2 Design exato do patch (fail-closed de verdade)

**Princípio fail-closed:** resposta sem prova NUNCA vira ação. Exauriu → `raise` → o ciclo aborta **sem publicar nada** (o `finally: salvar_json` preserva estado; o cron 15/15 retoma). A diferença: agora o raise é **informado** (log + contador) e o retry é **inteligente**.

```python
import random, time as _time

def _req(self, metodo, caminho, tentativas=4, **kw):
    """REST com retry backoff+jitter. Fail-closed: exaure → raise (ciclo aborta,
    nunca publica sem resposta). Timeout fixado ANTES do loop (bug do kw.pop)."""
    url = f"{self.site}/wp-json/wp/v2/{caminho}"
    timeout = kw.pop("timeout", 30)            # fixo fora do loop — BUG 1 morto
    base = kw.pop("base_delay", 2.0)           # 2s → 4s → 8s (+ jitter 0-1s)
    for i in range(tentativas):
        try:
            r = requests.request(metodo, url, auth=self.auth, timeout=timeout, **kw)
            if r.status_code in (408, 429) or (r.status_code >= 500 and i < tentativas - 1):
                _time.sleep(base * (2 ** i) + random.uniform(0, 1))   # BUG 2/3 mortos
                continue
            return r
        except requests.RequestException as e:
            if i == tentativas - 1:
                log(f"_req {metodo} {caminho} exaurido ({tentativas}x/{timeout}s): {e}")
                raise
            _time.sleep(base * (2 ** i) + random.uniform(0, 1))
    raise RuntimeError(f"inatingivel {metodo} {caminho}")
```

**Decisões do design:**
- **Timeout default 30s** (meio-termo entre os 20 atuais e os 40 do relato; downloads pesados continuam com timeout explícito 90/60).
- **Backoff 2s/4s/8s + jitter 0-1s** — espaça as tentativas e dessincroniza ciclos (anti *herd*).
- **408/429 retentam** (429 com o MESMO backoff; sem header Retry-After por simplicidade — o jitter já cobre).
- **ReadTimeout (subclasse de RequestException) retenta** e, na exaustão, **loga** — o ciclo atual morre mudo (autossaúde silenciosa); o novo morre com linha de diagnóstico.
- **Nunca retenta POST de efeito colateral com corpo** cegamente? Não — o POST é idempotente por natureza aqui (publicar com trio é re-aplicável; anexar capa idem; o anti-flip já re-publica). Manter retry em POST com a ressalva: o **readback pós-publish** (Camada A do P1) é a prova de que o retry não duplicou efeito.
- **Contador de exaustão** no `estado.json` (`req_exauridos: {data: n}`) → CHECK horário do robô reporta quando a régua estourar (2+/dia = alerta ao ZM).

### 2.3 Régua da "2ª fonte de medição" (formaliza minha P3 da 2ª caçada)

**Problema provado hoje:** REST lista mostrava `publish@22:35` para o 268455 mas o DB dizia `future` + permalink 404 — **cache estaleiro (Cloudflare) mentiu** (DS-039). Quem mede por REST sozinho pode declarar "no ar" o que não está.

**Régua formal (2 níveis):**
1. **Nível 1 — medição canônica:** REST **canônico** (`https://www.ocafezinho.com/wp-json/...`, UA browser) com **carimbo de medição** em toda linha de verificação na ponte: `(HH:MM BRT · via=REST, lat=Xs)`. Nunca `controle.` (ZM-024).
2. **Nível 2 — 2ª fonte quando REST falhar ou divergir:** **WP-CLI via ssh** (`ssh cafezinho-wp "wp post get <id> --fields=post_status,post_date,post_modified"`) — o DB cru, imune a cache. Regra: **status futuro/duvidoso só é declarado com 2 fontes concordando**; divergência REST×DB = linha de alerta (dono ZM, matriz item 9), nunca silêncio.
3. **Anti-cache na leitura de listas:** GET de status SEMPRE com `cache-bust` (`?_fields=...` + `X-Force-Cache: off` se o WAF aceitar) e conferir `date_gmt` (o cache serve HTML, mas o JSON de status costuma ser frescura do WP).

**Instrumentação (como):** helper `medir_status(pid)` no Publicador → (a) REST canônico, (b) se ≠ publish ou exceção → wp-cli, (c) retorna `{status, via, latencia_ms, ts}`; toda linha de prova na ponte usa esse helper. É o mesmo carimbo que a Camada A do P1 usa no readback — um só caminho de medição.

---

## PROBLEMA 3 — Taxa de acerto da caça de capas (gargalo nº 1 da casa; fila 5+ acumulada)

### 3.1 Diagnóstico do gargalo (o que a pesquisa mostrou)

- **22 rascunhos/dia** nascendo; o worker `dsn_imagem.py` (cron */20, NYC) caça Flickr/Commons → visão dupla (DeepSeek×Qwen, Gemini fallback) → aplica via adapter único OU manda para `fila_caca.jsonl` + ponte. **Fila atual: 268456/268457/268458/268394/268451 (+novos)** — 5+ com caçadores (AGY/CL) ocupados com o resto do dia.
- **Banco Ouro V3 = 1.214 fotos aprovadas/R2** (sqlite + R2, 35k rejeições com motivo, FTS, fila humana) — **existe e é o acervo canônico, mas o `featured_image_runtime` NÃO o consulta** (costura nº 1 pendente do fórum de arquitetura: "Ouro como camada 1 da cascata, hoje consulta só o audited local").
- **Causa do acúmulo:** cada caçada nova nasce do zero (Flickr/Commons) e reprova muito (268394: 16 candidatas, todas com logo/marca → Emenda 8); o que a casa JÁ aprovou (1.214 fotos) fica parado porque o elo Ouro→runtime não existe. **É o mesmo padrão do P1/P2: o dado certo existe, falta o encanamento.**

### 3.2 Solução — Banco Ouro V3 como camada 1, em SOMBRA + FLAG (sem risco à produção)

**Desenho (adapter Ouro→V4AuditedMediaStore, costura nº 1 do fórum):**
1. **Adapter de leitura** `ouro_store.py` (módulo NOVO, não toca nada existente): SELECT no `banco_midia_ouro_v3.db` (réplica NYC read-only) com os mesmos filtros do runtime (uso_automatico=1, tem R2, pessoas_identificadas não-vazio) + **match por título/pessoa/tese** (FTS do Ouro já indexa).
2. **Cascata nova:** `OURO (camada 0, ~ms, grátis)` → Flickr oficial → Commons → variação de tese → caça humana. Ouro é banco LOCAL: zero rede, zero 429, zero custo de visão — só o gate editorial da visão dupla para confirmar pertinência (a foto já foi aprovada; a visão só confere identidade/contexto do post).
3. **SOMBRA primeiro (protocolo da casa):** flag `OURO_CAMADA1=0` (default) + coluna/flag `_capa_sombra` registrando qual foto o Ouro TENTARIA escolher, sem aplicar. Rodar 48h comparando a escolha sombra × escolha real → medir a taxa de acerto teórica ANTES de ligar.
4. **CANÁRIO:** `OURO_CAMADA1=1` só para posts de pessoa central (ordem Miguel 12:05 — foto nominal dura, que é exatamente o que o Ouro tem de melhor: 405 linhas com pessoas identificadas) durante 1 dia; divergência → quarentena (fail-closed já existe).
5. **PROMOÇÃO:** 3 dias com acerto ≥80% e zero incidente → flag default on. Rollback = flag `OURO_CAMADA1=0` (1 arquivo, 1 minuto).

### 3.3 Banco por tese (minha P5 da 2ª caçada) + ideias novas

- **Banco por tese:** além do match por pessoa, adicionar **tese/contexto** ao Ouro (campo `tese` preenchido no approve do painel humano: "seca/queimadas", "orçamento", "futebol") — a caçada de uma matéria de seca consulta fotos de seca que a casa já aprovou, não recomeça do Commons. O `tipo_entidade` (pessoa/instituição/local/tema) da arquitetura de curadoria (12/08) é a chave — backfill com as 15 linhas não-pessoa.
- **Prioridade pessoa-central com rank:** quando o título tem pessoa, o Ouro devolve **as N fotos daquela pessoa ordenadas por `data_foto DESC`** (frescor — regra do Miguel 29/08: "frescor da imagem é fundamental"); o `_extract_v4_bank_photo` do V4 já prova esse match (nome→aliases→regex word-boundary no título dobrado) — o worker atual não o usa.
- **Homônimos:** o Ouro tem `pessoas_identificadas_json` unificado (`nomes_canonicos_ouro.py`) — usar o campo para desambiguar no match (Caterpillar empresa ≠ inseto já é regra da Emenda 15); adicionar coluna `qualificacao` (empresa/órgão) preenchida no approve para o runtime saber quando aplicar a Emenda 8 (CEO/sede).
- **Métrica de acerto (fecha o ciclo):** o worker já grava `estado.json` — formalizar no relatório diário do DS-N Imagem (prova de vida, minha da 2ª caçada): `posts_do_dia, capas_aplicadas, fila_caca_entrada/saida, acerto=capas/(posts+pendentes)`. Sem relatório não há como medir a taxa que o maestro encomendou.
- **Lote de caça priorizado pela fila de publish (E4 da 3ª caçada):** a fila_caca ordena por proximidade do slot de publish (furo mais próximo primeiro) — caçador humano ataca o que destrava a régua 3h, não o mais antigo.
- **Alerta de acúmulo:** fila_caca ≥5 → aviso na ponte (não Telegram — regra "só notícia boa") com a lista e a idade; a régua vira a métrica viva do gargalo.

---

## PLANO DE EXECUÇÃO GERAL (proposta; execução exige ✓ do Miguel + caneta do dono ZM)

1. **P2 primeiro (menor, desbloqueia tudo):** patch do `_req` + régua de 2ª fonte — dono ZM (design acima, ~30min + teste em 1 ciclo real).
2. **P1 em paralelo:** Camada A (readback+normalização) e B (watchdog future) — mesmo robô, mesmo PR; Camada C (cron) é caneta do ZM com teste de slot.
3. **P3 depois (maior):** adapter Ouro em sombra → 48h de medição → canário pessoa-central → promoção; lote de caça priorizado + relatório diário do DS-N Imagem junto.
4. **Registro:** cada camada com backup datado + linha no `ROLLBACK_INDEX.md` do v4_labs (protocolo 6 passos do ZM-011) + ficha no nodo de bugs quando fechar.

**Riscos e reversibilidade:** todos os passos atrás de flags de arquivo (`NORMALIZA_FUTURE`, `WATCHDOG_FUTURE`, `OURO_CAMADA1`, `PROXY_OFF`) + backups datados; nada mexe na mão que publica (mesmas travas de capa/olho/consenso). O maior risco é o oposto: **não fazer nada** — a fila de capas cresce, o quirk volta no próximo batismo e o Publicador continua morrendo mudo.

---

## O QUE PRECISO DO MIGUEL

- **✓ (vai) para o design P1/P2** (itens 1-2 são design de patch — o ZM executa com a caneta dele; minha parte foi o desenho).
- **✓ (vai) para a arquitetura P3** (sombra+flag do Banco Ouro como camada 1 — o ZM executa; sombra não toca produção).
- **Decidir a Camada C** (cron HTTP × WP-CLI determinístico) junto com o ZM — é caneta dele, mas a escolha muda o rito.
- **Cobrar a caneta do BUG-DS-098** (prova do crontab 1min vivo) — sem isso a Camada C anda às cegas.

---

## ADENDO 1 (ronda 02:13 de 01/09) — validação na prática + input do ZM absorvido no P3

**Validações na prática desde a entrega (23:16):**
- **P1:** verificador de virada funcionou como desenhado — 268455 virou 23:55 no minuto exato (wp-cron); BUG-20260831-A face 1 ENCERRADA (2×2: 268455 + 268334). Face 2 (post_date futuro — 268366/268393) segue aberta, dono ZM.
- **P2:** ZM-026 executou o patch desenhado (retry 5xx/408/429 + backoff 2/4/8s + jitter, backup `.bak_pre_backoff_20260901`) — sem reincidência grave desde então; 1 oscilação 500 na janela 02:00 (DS-005: padrão MONITOR load/Redis, classe coberta pela encomenda Ideias-003 cache/otimização).
- **P3:** ZM ADENDO 8 — **Degrau 2/3 EXECUTADO** (01/09 ~02:1x): hook de medição em sombra no dsn_imagem.py (flag `OURO_CAMADA1=log`, backup `.bak_pre_ouro_sombra_20260901`, try/pass condicionado — não altera fluxo; sombra_camada1.jsonl mede hit/miss a partir do ciclo 02:20). Degrau 3 (aplicar) só com dado + ✓ do Miguel.

**Novo input do ZM (ADENDO 8, ~01:10) — candidato a fix estrutural endereçado "p/ Ideias/Degrau 3":**
> Ciclo que sobe capa via seed pode morrer ANTES do olho robótico → capa fica aplicada SEM veredito (nem aprovada nem reprovada). Cura aplicada na hora: re-invocar o olho_robotico da casa. Candidato a fix estrutural: **re-julgar no início do ciclo posts com capa mas sem `_cafezinho_img_check`**.

**Absorção no desenho do P3 (nova costura nº 4, mesma sombra+flag):**
1. **Detector de "capa sem veredito"** no início do ciclo do worker de imagem: SELECT de posts com `_thumbnail_id` setado e `_cafezinho_img_check` ausente/vazio → fila de re-julgamento (mesma fila do olho, sem duplicar código).
2. **Re-julgar (não re-caçar):** a capa JÁ está aplicada; o olho só emite veredito (aprova → check gravado; reprova → remove thumb e devolve à caça). Custo = 1 visão por órfão, não uma caçada inteira.
3. **Métrica:** `capas_sem_veredito` entra no relatório diário do DS-N Imagem (prova de vida) — fecha o buraco que o ZM achou: hoje o "acerto" da caça pode estar contaminado por capas que subiram sem julgar.
4. **Rollback:** flag `REJULGA_CAPA_SEM_CHECK=0` (1 arquivo, 1 minuto) — mesma disciplina das demais camadas.

Isso é rascunho (desenho) — execução exige ✓ do Miguel + caneta do dono (ZM/DS-N Imagem), conforme protocolo da casa.

— DS Nuvem Ideias (DS-N Ideias) · 20260901 02:13:00 BRT

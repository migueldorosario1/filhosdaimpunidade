# 🔁 BLOCO IDEIA_PRO_DSNUVEM_IDEIAS-019 — PLANO DE SUCESSÃO DO PUBLICADOR (failover de PESSOA por ordem): FORMALIZAÇÃO + GATILHO 2×3h + ATIVAÇÃO IMEDIATA HOJE

> **Ronda:** 06/09/2026 ~07:1x-07:4x BRT (DS-N Ideias, Tencent — ronda pós-CAÇADA 53 06:48). Pull ff-only OK na 1ª (07:1x; fast-forward bb2e69b45..3e071a2c6 = commit do bloco + RESPOSTA DSC bom dia).
> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-019` — DSH-us65 (relay de ordem do Miguel ~07:3x: *"tem que ter plano, o sistema se reajusta e outro entra substituindo POR ORDEM"*), bloco em `cerebro/Foruns/ponte_laura_completa/de_dell.md` (20446-20458, fim do arquivo). Commit `3e071a2c6` 07:12:47.
> **Divisão do bloco (do próprio DSC):** IDEIAS: desenhar e formalizar (2ª via no fórum; registrar na grade) · CHEFE: implantar o gatilho no vigia + ATIVAÇÃO IMEDIATA hoje (1º da fila publica a fila pronta, 30 candidaturas geo pontuadas ontem).
> **Fluxo da casa:** Ideias entrega (este arquivo) → DS-N Chefe chancela/implantar → decisão final + ✓ do Miguel → execução por quem tem credencial. NADA executado por mim (Lei de Poderes).
> **Refs:** PLANO_SUCESSAO_PUBLICADOR_v1/v2 (20/08, LAURA-CLAUDE — protocolos do publicador, nunca ativado) · redundância shadow DESLIGADA por ordem do Miguel 16/08 (contexto do bloco) · DSN Publicador (carteiro) `PARADO_CONTRATO_20260901` — só CL/CM publicam até o Publicador v3 nascer na Onda 1 (grade §1) · caçada 40 (whitelist de publish no mu-plugin · `_cafezinho_publicado_por` · publicar vira serviço · freio 1740 conta 5801/5795) · caçadas 41-53 (régua de vida do executor ≤40min · padrão cl172 failover editorial do 1º post · I1 cartão de abertura 2 cenários A×B · lição 197ª não duplico INBOX) · CASO CL 06/09 (CL-039 23:20 05/09 último bloco; ~8h ausente à leitura; 0 posts; janelas 3h vazias 1ª-9ª — contagem do DS-N já existe) · AGY parado ~33h (AL-628 22:38 04/09; religamento = sessão interativa do Miguel) · Consenso Duplo (CL+AGY/Chefe; rascunho 5801 → gate → CL consenso → AGY/Publicador publica com capa+selo) · WP-CLI na máquina Laura, carteiro no us65, Chefe publish=0 (sem caneta no WP) · regra §82 (sem segredos) · append-only, nunca `git add -A`, push sem force.
> **Natureza:** FORMALIZAÇÃO/ARQUITETURA/PLANO — NADA executado em produção (Lei de Poderes). Nenhum valor de chave neste arquivo (§82).
> **Marcador:** `PRONTO_BLOCO019_SUCESSAO_PUBLICADOR`

---

## 0. Resumo executivo (o veredito do arquiteto)

1. **A bronca estrutural do Miguel procede, com prova na ronda:** 06/09 = **0 posts até ~07:10** (CL-20260905-039 23:20 = último bloco da CL; ~8h ausente à leitura 07:1x; rondas 00:12→07:12 = 8 janelas dela perdidas; **9ª janela de 3h vazia consecutiva** à 07:07 — Chefe 228ª) e o **AGY parado ~33h+** (AL-628 22:38 04/09). A casa tem failover de MÁQUINA (NYC/Tencent) e a esteira tem agulhas com futuro agendado, mas **NÃO existe cadeia de sucessão do PAPEL de publicador**: quando o titular cai, nenhum outro agente HERDA a agulha — o vazio de 8h de domingo é o custo visível.
2. **A proposta do DSC (0 Miguel · 1 AGY sob Consenso Duplo com o Chefe · 2 ZM com Chefe revisando · 3 DSC, prova REST em tudo + gatilho 2×3h + retorno com sombra) é a direção certa** — eu formalizo com 3 ajustes de realidade para ela funcionar HOJE:
   - **(a) PULO por indisponibilidade:** o 1º da fila (AGY) está parado ~33h e o religamento é sessão interativa do Miguel (fato da casa) → a fila só avança se o substituto da vez tiver PROVA DE VIDA (bloco/AL recente ≤ régua de vida); sem prova de vida, PULA para o próximo com prova.
   - **(b) O Chefe NUNCA publica** (publish=0 — régua pessoal; sem credencial WP nesta Tencent; WP-CLI vive na máquina Laura, carteiro no us65): o papel do Chefe na sucessão é REVISOR/CONSENSO em todos os níveis (o "segundo par de olhos" do Consenso Duplo), nunca executor — executor é quem tem credencial.
   - **(c) Na ativação imediata de HOJE**, com CL ausente ~8h e AGY parado, o 1º executor REAL com prova de vida e credencial é o **ZM (2º da fila)** sob revisão do Chefe — a menos que o Miguel (0º) esteja on-line e decida/religue o AGY direto.
3. **Formalização completa neste arquivo:** hierarquia com papéis (quem decide / quem revisa / quem executa / quem registra), gatilho automático 2×3h desenhado para o vigia do Chefe, INCIDENTE numerado por ativação, assinatura de sucessão, retorno do titular com sombra de 1 ronda, e o rastro do rito da casa em cada post do substituto (capa `_cafezinho_img_check` · prova REST · `expira_em` · `_cafezinho_publicado_por` · whitelist/freio 1740 respeitado · meta `_cafezinho_sucessao`).
4. **O gatilho já tem a contagem pronta — falta só a mecânica:** as janelas de 3h sem post são contadas pelo DS-N/vigias desde a madrugada (1ª-9ª vazias em 06/09). O desenho do gatilho (rascunho §5.1) roda no vigia do Chefe com REST público do canônico (sem credencial — o que o DS-N roda); a implantação é do Chefe (bloco).
5. **O que precisa do Miguel (nada sai sem ele):** (i) ✓ da ORDEM de sucessão 0-3 (ou ajuste da hierarquia); (ii) ✓ do GATILHO 2×3h (1ª janela vazia = alerta ao Chefe; 2ª consecutiva = sucessão ativa automática); (iii) decisão da ASSINATURA (meta+rastro no ledger — recomendado — versus rodapé visível ao leitor); (iv) palavra da ATIVAÇÃO IMEDIATA de hoje: **AGY religado (0º/1º) × ZM como executor do 1º lote sob revisão do Chefe (2º)** — com a fila pronta (30 candidaturas geo pontuadas ontem), o custo de mais 1 hora de domingo parado é mensurável.

---

## 1. O DIAGNÓSTICO (do bloco + o meu)

### 1.1 O que o Miguel disse (verbatim resumido do bloco)
> "A CL caiu e ficou 8h+ SEM substituto — zero posts hoje. É erro NOSSO. A casa tem failover de MÁQUINAS (NYC/Tencent, fórum 01/07) mas NÃO tem failover de PUBLICADOR — a redundância shadow foi DESLIGADA por ordem do Miguel em 16/08 e nunca se criou a cadeia de sucessão. Tem que ter plano: o sistema se reajusta e outro entra substituindo POR ORDEM."

### 1.2 Os números da minha ronda (06/09 ~07:1x)
- **CASO CL:** último bloco CL-20260905-039 23:20; à leitura ~07:13 = **~7h53 ausente** (8 rondas dela perdidas 00:12→07:12; CL-20260906-007 07:12 SEM bloco no origin); agulha **cl178 pendente**; 06/09 = 0 posts; **9ª janela de 3h vazia** (Chefe 228ª 07:10: 3h=0/12h=7/24h=23; 28/28 de 05/09 fechado = INCIDENTE-1154 110ª ~62h+ RECORDE — o zero de hoje é CASO CL, NÃO recuo da série).
- **AGY-LAURA:** parado ~33h+ (AL-628 22:38 04/09; nenhum AL-629); ofício de publicação ocioso — a CL cobria, e agora nem a CL nem o AGY publicam.
- **Quem está com prova de vida nesta manhã:** DS-N Chefe (228ª 07:10 — mas publish=0) · ZM (49ª 06:12 LIMPA) · DS-Dell (221ª 06:42) · DS-N Ideias (CAÇADA 53 06:48) · Revisores · DSC/us65 (relay 07:12 — terminal do Miguel, carteiro v1.2 no us65).
- **Fila pronta aguardando publicador:** 30 candidaturas geo pontuadas ontem (bloco) + a agulha do 1º post cl178 (derivada do cl177, expira_em 07/09) + Baleia ed. 36 já saiu pelo Chefe 07:07 (failover declarado da 222ª — precedente de sucessão pontual funcionando).

### 1.3 Por que não existe a cadeia (leitura de arquiteto)
1. **16/08: a redundância shadow foi desligada** (decisão do Miguel) e nunca se criou o substituto declarado — o "vão" ficou de propósito (1 caneta só, gate apertado) sem o plano B escrito do outro lado.
2. **Os protocolos de sucessão que EXISTEM são de PREPARAÇÃO, não de ATIVAÇÃO:** o PLANO_SUCESSAO_PUBLICADOR v1/v2 (20/08) prepara a CL para publicar com menos erro (rito, gate, colchão) e declara "PRONTO_NAO_ATIVO — ativação é decisão de Miguel"; não desenha "quem substitui a CL quando ELA cai".
3. **O rito atual é 1-caneta:** "Só CL/CM publicam até o Publicador v3 nascer na Onda 1" (grade §1) + freio 1740/whitelist (caçada 40) fecharam as contas 5801/5795 — correto contra o padrão-1740, mas concentrou o ato numa única pessoa com janelas de ronda. A esteira (agulhas + future) roda sozinha; o PAPEL de criar/agendar a agulha e publicar o 1º post do dia não tem herdeiro declarado.
4. **A governança reagiu bem (fecho formal 04:00, watch por ciclo 222ª-228ª, convergência 4 vigias, Baleia ed. 36 pelo titular com failover declarado)** — prova de que a casa SABE operar sucessão pontual; falta transformar o padrão ad-hoc em MECÂNICA com ordem e gatilho (o pedido do Miguel).

---

## 2. PESQUISA — decisões anteriores que o plano herda (e não pode contradizer)

| Ref | Decisão/regra | Impacto no plano 019 |
|---|---|---|
| Ordem Miguel 16/08 | redundância shadow DESLIGADA | a sucessão nova NÃO pode religar o shadow antigo sem ✓ — desenhar cadeia NOVA com ordem explícita |
| PLANO_SUCESSAO_PUBLICADOR v1/v2 (20/08) | protocolos do ato de publicar (gate de imagem `_cafezinho_img_check`, fuso `post_date_gmt`, colchão, agendar>publicar, NUNCA despublicar → `no-home`, P8 Baleia herda junto) | o substituto herda as RÉGUAS, não só a função (v1 P1.3); erro de sentido = `no-home` + nota, nunca despublicar (v2 P4.1) |
| Grade §1 (01/09) | DSN Publicador `PARADO_CONTRATO_20260901`; só CL/CM publicam até o carteiro v3 | sucessão opera com os publicadores EXISTENTES (CL titular + AGY/ZM/DSC como substitutos), não com o Publicador robô |
| Caçada 40 (04/09) | whitelist de publish no mu-plugin · meta `_cafezinho_publicado_por` · publicar vira serviço · freio 1740 (contas 5801/5795) | todo post do substituto passa pela whitelist e carrega `_cafezinho_publicado_por` — a assinatura de sucessão é META, não conta nova |
| Caçadas 41-53 (05-06/09) | régua de vida do executor ≤40min · cartão de retomada (análogo AL-629: sem reexecutar cl153-cl172) · padrão cl172 (failover editorial do 1º post: pacote da CL executado sob gate + prova REST) · I1 cartão A×B (default = cenário B pelo Chefe se CL não voltar ~07:00) | o gatilho 2×3h usa a MESMA régua de vida; o padrão cl172 vira o RITO do 1º post do substituto; o I1/cartão da manhã vira o CARTÃO DE ATIVAÇÃO do incidente |
| Lição 197ª + fecho formal 04:00 | não duplicar INBOX/cobrança; fecho com método (INBOX + relatório + lição) | cada ativação de sucessão = 1 INCIDENTE numerado com registro único no ledger, sem duplicar canais |
| Consenso Duplo (CL+AGY/Chefe; casa) | rascunho 5801 → gate → CL (consenso) → AGY/Publicador publica com capa+selo | na ausência da CL, o consenso passa a ser CHEFE(revê)+EXECUTOR(publica) — 2 pares de olhos preservados |
| Chefe publish=0 (16634 de_dell) | "não há credencial de escrita WP nesta Tencent; WP-CLI na máquina Laura, carteiro no us65" | o Chefe é REVISOR perene da sucessão; executor = AGY (Dell) → ZM (NYC) → DSC/us65 (carteiro) |
| CASO CL 06/09 (caçadas 51-53) | cl178 derivada do cl177 (head -3 + REF + expira_em 07/09), diários novos, sem reexecutar | o 1º post do substituto HOJE = cl178 no formato já desenhado |

---

## 3. ARQUITETURA DA SOLUÇÃO (componentes · dados · fluxo · onde roda)

### 3.1 Componentes
1. **VIGIA DE JANELAS (contador 3h)** — já existe de fato (DS-N/vigias contam "janelas de 3h sem post" desde a madrugada; Chefe 228ª contou a 9ª). Formalizar como função do vigia do DS-N Chefe: a cada ronda, REST canônico → topo de `post` publicado; janela de 3h sem topo novo = janela vazia.
2. **DISPARADOR DE SUCESSÃO (gatilho 2×3h)** — NOVO (rascunho §5.1): 1ª janela vazia consecutiva → ALERTA ao Chefe (já é o padrão manual); 2ª janela vazia consecutiva (~6h sem post) → SUCESSÃO ATIVA AUTOMATICAMENTE: o Chefe abre o INCIDENTE e convoca o 1º substituto da fila COM PROVA DE VIDA. Contagem zera no 1º post no ar (qualquer autor).
3. **FILA DE SUCESSÃO (ordem 0-3)** — a hierarquia do Miguel formalizada com o ajuste (a): 0º MIGUEL (on-line decide/publica direto) · 1º AGY-LAURA (executor com credencial; Consenso Duplo vira Chefe+AGY) · 2º ZM (executor; Chefe revisa antes do publish) · 3º DSH-us65/DSC (último recurso; Chefe revisa; prova REST em tudo). **Regra de PULO:** candidato sem prova de vida (AL/bloco ≤ régua da casa ~40min... na prática: sem bloco desde o último ciclo declarado) é pulado na hora — a fila anda até o primeiro COM prova de vida E credencial.
4. **REVISOR/CONSENSO** — DS-N Chefe (publish=0): em todos os níveis 1-3 o Chefe REVISA (capa, fuso, whitelist, prova REST, dedupe) e registra o consenso no incidente. Sem revisão do Chefe não há publish do substituto (substitui o papel da CL no Consenso Duplo).
5. **REGISTRO DE INCIDENTE** — cada ativação = 1 incidente numerado `INC-SUC-<AAAAMMDD>-<seq>` com início/fim/motivo/substituto/retorno (template §5.3), no ledger do ofício + ponte. Não é o INCIDENTE-1154 (série esteira) — é registro próprio da sucessão.
6. **CARTÃO DE ATIVAÇÃO** — o pacote que o substituto executa: agulha(s) da fila pronta + rito (checklist §5.4) + assinatura.

### 3.2 Dados (o que cada post do substituto carrega — rastro)
- `_cafezinho_publicado_por`: id/conta do executor substituto (whitelist) — já regra da caçada 40.
- `_cafezinho_sucessao`: `ativa, titular_ausente, incidente=INC-SUC-<data>-<seq>, substituto=<quem>` (novo — a "assinatura" do bloco; ver decisão ao Miguel §6).
- `_cafezinho_img_check ok:true` (capa vista) + `expira_em` + `post_date_gmt = post_date + 3h` (gate de fuso).
- Registro no ledger do executor + linha no incidente (prova REST: id + HTTP + permalink).

### 3.3 Fluxo (sequência da ativação)
```
T0: titular (CL) para de entregar agulha (ronda perdida)
T0→T+3h: 1ª janela 3h sem post → ALERTA ao Chefe (vigia)
T+3h→T+6h: 2ª janela consecutiva sem post → SUCESSÃO ATIVA AUTOMÁTICA
   1. Chefe abre INC-SUC-<data>-<seq> (motivo, T0, titular)
   2. Chefe consulta a fila 0-3: 0º Miguel on-line? (INBOX/Telegram) — não → desce
   3. 1º AGY com prova de vida? (AL recente? não — parado ~33h) → PULA
   4. 2º ZM com prova de vida? (49ª 06:12 LIMPA — sim) → CONVOCA + Chefe revisa
   5. ZM executa a agulha da fila pronta (cl178/geo) com checklist §5.4 + prova REST
   6. Registro: incidente + ledger + ponte (assinatura "sucessão ativa, titular ausente")
Titular volta: reassume na próxima janela; substituto vira SOMBRA 1 ronda (observa/confere, não publica) e devolve; incidente FECHADO com fim/motivo.
```

### 3.4 Onde roda
- **Vigia/disparador:** na máquina do DS-N Chefe (e replicável no DS-Dell) — só REST público do canônico (www.ocafezinho.com), zero credencial; cadência das rondas do Chefe (:00/:30).
- **Executor:** AGY (Dell/Windows — ofício AGY-LAURA, WP-CLI da máquina Laura) → ZM (NYC — mão técnica) → DSC/us65 (Dell celular do Miguel — carteiro v1.2).
- **Revisor:** DS-N Chefe (Tencent — não tem caneta, revê e registra).
- **Barramento/registro:** repo (ponte + ledger + grade) — o mesmo trilho de sempre; INCIDENTE no nodo do DS-N.

---

## 4. PLANO DE EXECUÇÃO (passos numerados · riscos · reversibilidade — protocolo da casa: backup → prova → registro → rollback escrito)

> Divisão do bloco respeitada: P0-P2 são DO CHEFE (implantação/ativação). Minha parte (entregue) = P0.1-P0.3 (formalização). Nada aqui é executado por mim.

- **P0.1 — (IDEIAS — ENTREGUE neste arquivo):** formalização + rascunhos (gatilho, cartão, incidente, checklist). Prova: este arquivo + síntese na ponte + registro na grade (§4). Rollback: n/a (documento).
- **P0.2 — (CHEFE) chancelar a formalização e REGISTRAR a ordem de sucessão na grade** (linha do DS-N + §4). Prova: commit da grade. Rollback: git revert do commit (documental).
- **P0.3 — (CHEFE) implantar o GATILHO no vigia** (rascunho §5.1 adaptado à máquina dele; contagem 3h já existe manual — virar check automático na ronda + alerta na 2ª janela). Prova: 1 ciclo de vigia com o check rodando + log. Rollback: remover o snippet do vigia (1 arquivo, sem tocar produção).
- **P1 — ATIVAÇÃO IMEDIATA (HOJE — CHEFE + executor, sob ✓ do Miguel):** abrir `INC-SUC-20260906-001` (motivo: CL ausente ~8h, 06/09 = 0 posts, 9ª janela vazia; T0 = 23:20 05/09) e convocar o 1º executor com prova de vida: **AGY (religado pelo Miguel, se on-line) OU ZM (2º, presente)** — o 1º post = cl178 (formato caçada 51: derivada do cl177, head -3, REF CL-20260906-…, expira_em 07/09) + fila geo (30 candidaturas pontuadas) no ritmo do gate. Prova: post no ar com capa + REST 200 + metas `_cafezinho_sucessao`/`_cafezinho_publicado_por` + registro do incidente. Rollback: posts publicados ficam (nunca despublicar — v2 P4.1); se erro de sentido → `no-home` + nota; se o titular voltar → sombra 1 ronda e devolve (sem reexecutar — análogo AL-629).
- **P2 — (CHEFE) rito de retorno + fecho:** quando a CL voltar (janela dela), reassume; substituto vira sombra 1 ronda; incidente fechado com fim/motivo; lição arquivada (família fecho_caso_cl). Prova: bloco de fecho no incidente + lição. Rollback: n/a.
- **P3 — (DSC/Chefe, se o Miguel aprovar) mecânica fina:** gatilho vira serviço (cron/systemd) com alerta no Telegram; ordem 0-3 registrada como CONSTITUIÇÃO da casa (emenda no rito Art. 7? — decisão do Miguel); teste de simulação (1 ativação ensaiada sem post real).

**Riscos principais e mitigação:** (1) substituto sem régua editorial → herda as réguas do plano v1/v2 + revisão do Chefe em TODO post; (2) 2 canetas no WP no retorno (atropelo) → sombra de 1 ronda + reserva no livro (v1 P3.1); (3) substituto vira publicador permanente → incidente com FIM + devolução obrigatória; (4) post do substituto com erro factual → gate completo (frescor + fontes + capa) antes do ato; erro pós-publicação = `no-home`/nota, nunca despublicar; (5) gatilho falso-positivo (domingo lento com 0 posts LEGÍTIMOS?) → contagem por janela de 3h real e não por ronda; a régua de domingo (I6 caçada 53 — banda de domingo) refina depois; (6) AGY religado sem cartão → cartão de retomada (caçada 41/47: não reexecutar cl153-cl172).

---

## 5. RASCUNHOS (dentro do arquivo — nunca em produção)

### 5.1 Gatilho 2×3h para o vigia (bash + REST público — sem credencial)
```bash
#!/usr/bin/env bash
# gatilho_sucessao.sh — roda na ronda do vigia (Chefe). REST público, sem credencial.
# Lógica: topo publicado do canônico; janela de 3h sem topo novo = vazia; 2ª vazia consecutiva = SUCESSÃO ATIVA.
CANON="https://www.ocafezinho.com/wp-json/wp/v2/posts"
TOPO_TS=$(curl -sf --max-time 20 -H "User-Agent: dsn-ideias-vigia" "$CANON?per_page=1&orderby=date&order=desc" \
  | python3 -c "import sys,json;print(json.load(sys.stdin)[0]['date'])" 2>/dev/null) || { echo "REST falhou — sem veredito (não alerta)"; exit 0; }
AGORA=$(date -u +%Y-%m-%dT%H:%M:%S)
# diff em minutos entre AGORA e TOPO_TS (ISO UTC)
python3 - "$TOPO_TS" "$AGORA" <<'PY'
import sys, datetime
topo = datetime.datetime.fromisoformat(sys.argv[1].replace("Z","+00:00"))
agora = datetime.datetime.fromisoformat(sys.argv[2].replace("Z","+00:00"))
min_sem_post = int((agora - topo).total_seconds()//60)
print(f"min_sem_post={min_sem_post}")
if min_sem_post >= 360:   # 2ª janela de 3h (>=6h)
    print("SUCESSAO_ATIVA — 2 janelas de 3h sem post: abrir INC-SUC e convocar 1o substituto com prova de vida")
elif min_sem_post >= 180: # 1ª janela (>=3h)
    print("ALERTA_1a_JANELA — 1 janela de 3h sem post: avisar o Chefe")
else:
    print("OK")
PY
```
> Nota: contagem zera no 1º post no ar; o vigia registra o estado (OK/ALERTA/ATIVA) no nodo do DS-N a cada ronda; a convocação do substituto é SEMPRE humano/Chefe (o robô não publica sozinho — Lei de Poderes; o gatilho só AVISA).

### 5.2 Cartão de ativação do incidente (template — quem faz o quê)
```yaml
incidente: INC-SUC-20260906-001
motivo: titular (CL) ausente — CL-20260905-039 23:20 = último bloco; ~8h sem publicador
t0: 2026-09-05 23:20 BRT
disparo: 9ª janela de 3h vazia (07:07 06/09) — gatilho 2×3h
titular_ausente: CL (Claude Laura)
ordem_acionada: 0 Miguel (off-line ~07:1x) -> 1 AGY (SEM prova de vida ~33h, PULA) -> 2 ZM (prova de vida 49ª 06:12) -> CONVOCADO
revisor/consenso: DS-N Chefe (publish=0)
agulha_1: cl178 (derivada do cl177; REF CL-20260906-NNN; expira_em 07/09) + fila geo (30 candidaturas pontuadas 05/09)
assinatura: meta _cafezinho_sucessao = "ativa, titular ausente, incidente INC-SUC-20260906-001, substituto ZM"
gate: capa _cafezinho_img_check ok:true + prova REST + _cafezinho_publicado_por + whitelist/freio 1740
fim: <preencher no retorno da CL> — substituto vira sombra 1 ronda e devolve
```

### 5.3 Registro no ledger (1 linha por ação, formato da casa)
```
INC-SUC-20260906-001 | 2026-09-06 07:1x | ATIVACAO | substituto=ZM | agulha=cl178+geo | revisao=Chefe | prova=<post_id> HTTP 200 <permalink> | titular=CL ausente desde 23:20 05/09
INC-SUC-20260906-001 | <retorno> | FIM | titular=CL reassumiu | sombra=1 ronda | posts_substituto=<n> | rollback=devolvido
```

### 5.4 Checklist do substituto (o rito do 1º post — padrão cl172 formalizado)
1. git pull + ler a agulha da fila pronta (cl178/geo) + conferir dedupe (núcleo factual vs 24h — regra da casa).
2. Capa: `_cafezinho_img_check ok:true` presente e posterior à última troca de mídia (sem capa vista → não publica; parecer do Grok nunca metadado — v1 P3.2).
3. Fuso: `post_date_gmt = post_date + 3h` (v1 P3.3); agendar > publicar sempre que o WP puder executar (v1 P3.4); `expira_em` no formato da casa.
4. Whitelist: autor substituto liberado no mu-plugin (freio 1740 preservado — nenhuma conta 5801/5795).
5. Metas: `_cafezinho_publicado_por` + `_cafezinho_sucessao` (assinatura) — nunca conta nova.
6. Publicar + PROVA REST (id + HTTP 200 + permalink) + registro no ledger + linha no incidente.
7. Erro pós-publicação que muda sentido → `no-home` + nota de correção (v2 P4.1); NUNCA despublicar.
8. Titular voltou → sombra 1 ronda (observa/confere) e devolve; incidente fechado.

---

## 6. O QUE PRECISO DO MIGUEL (e dos donos)

1. **Miguel:** (a) ✓ da ORDEM de sucessão 0-3 (ou ajuste — ex.: colocar o ZM à frente do AGY enquanto o AGY estiver em religamento manual?); (b) ✓ do GATILHO 2×3h (1ª janela = alerta; 2ª consecutiva = ativação automática com convocação pelo Chefe); (c) decisão da ASSINATURA: meta+ledger (recomendado — o leitor não precisa saber da orquestração) OU rodapé visível "publicado em sucessão ativa" (transparência ao leitor); (d) palavra da ATIVAÇÃO IMEDIATA de hoje com o executor real: religar o AGY (0º/1º) OU autorizar o ZM como executor do 1º lote sob revisão do Chefe (2º) — a fila está pronta (30 geo + cl178), o site está há ~8h sem post num domingo.
2. **DS-N Chefe:** chancelar este arquivo; implantar o gatilho no vigia (P0.3); executar a ativação (P1) sob o ✓ do Miguel; registrar a ordem na grade.
3. **CL (quando voltar):** retomar pela sombra de 1 ronda; o cartão de retomada (caçada 51) segue válido.
4. **AGY/ZM/DSC:** ciência da fila de sucessão e do que cada um herda (prova de vida + credencial + revisão do Chefe).
5. **DSC-us65:** levar ao Miguel o pacote de decisões acima (1a-d) — é a bronca dele, a resposta destrava o domingo.

Nada em produção (Lei de Poderes). — DS Nuvem Ideias (DS-N Ideias) · 20260906 07:17:35 BRT

# 🛡️ PROPOSTA DE SOLUÇÃO — SYNC-BUG DA CASA (DSC-20260902-049): produtor, guarda kill-switch e blindagem têxtil

> **Missão:** DSC-20260902-049 (de_dell.md 19:5x, ordem do Miguel ~19:3x: *"ele é criativo, ele pode encontrar a resposta boa"*) — entregar HOJE proposta criativa e completa de solução para o sync-bug (commits `sync: AAAA-MM-DD HH:MM — N arquivos` revertendo conteúdo legítimo de agentes).
> **Natureza:** ANÁLISE + PROPOSTA + RASCUNHOS (dentro deste arquivo). **NADA executado** — execução exige ✓ do Miguel e donos DSC/ZM/CM (rito da casa: proposta → ponte → ✓ → execução → prova → rollback escrito).
> **Insumos:** DSC-049 (dossiê de evidências) · XM-20260902-026/027 (confirmação independente + régua de validação no host) · caçadas 17 P2 / 22 P1 / 23 do DS-N Ideias · lições `20260902_sync_bug_*` e `20260902_sync_canal_*` do DS-N Chefe · `casos/2026-09-02_auditoria_ultra_luxo_parecer.md` (padrão de parecer) · diffs reais dos syncs de hoje (verificados nesta ronda).
> **Vigia desta ronda:** sync `c2cd9832e` (20:22) comeu 1 linha do `Foruns/ideias/2026-09-02_video_vertical_espelho_reels.md` (a **Emenda Miguel 20:35** — draft no canônico autorizado) — **RESTAURADA verbatim pelo dono nesta ronda** (do commit 7c0f3d135).

---

## 1. O problema em 8 linhas (fato × hipótese — régua XM-027)

| # | Afirmação | Status |
|---|---|---|
| 1 | Existe um produtor de commits `sync: … — N arquivos`, autor `Miguel do Rosario <migueldorosario@gmail.com>`, cadência ~15-30 min, desde 25/06 | ✅ FATO (git) |
| 2 | Contagem: 550 assuntos `sync:` desde 25/08 (500 em `--first-parent`) — não 474 (XM-027) | ✅ FATO (declarar recorte antes de virar requisito de aceite) |
| 3 | Syncs destrutivos REMOVEM linhas de arquivos coletivos dos agentes (canal revisores, canal YouTube, fóruns, ideias, grade) — assinatura net-negativa | ✅ FATO (diffs provados hoje: 19:22 f67589d94 · 20:22 c2cd9832e · 21:07 6d7712b18) |
| 4 | Syncs aditivos só tocam arquivos do lado produtor (ex.: 15:07 93a69d8de = forum_maestro +6 · MANIFESTO 4/4) | ✅ FATO |
| 5 | O produtor roda no DELL (única máquina com árvore completa + agentes próprios; syncs carregam `loop_trindade_laura/MANIFESTO_INTEGRIDADE.json` fresco MISTURADO com reversões de arquivos do tencent) | 🔶 HIPÓTESE FORTE não provada no host (XM-027: validar na máquina/tarefa pelo dono autorizado ANTES de qualquer kill/patch) |
| 6 | Mecânica destrutiva = "pull falhou (credential/index.lock) → commita e empurra a árvore local stale mesmo assim" | 🔶 HIPÓTESE (mecânica compatível com a assinatura; a provar na Fase 0) |
| 7 | O número "N arquivos" do commit é cosmético (conta a árvore); o diff real é pequeno | ✅ FATO (7-13 arquivos reais nos syncs de hoje) |
| 8 | Recorrências hoje: ≥11 (a 21:07 comeu 8 linhas do canal revisores + 6 do canal YouTube — Chefe re-anexou 21:1x; a 20:22 comeu 1 linha do meu IDEIA-009, restaurada nesta ronda) | ✅ FATO (contagem de cada dono em seus arquivos) |

**Consequência prática:** o repo é multi-master (agentes em Tencent/Dell/NYC escrevem nos mesmos canais). O sync é um editor a mais — e quando ele edita com snapshot velho, **apaga trabalho legítimo sem diff direto de "quem apagou"** (o conteúdo fica na ancestralidade; some do HEAD).

---

## 2. Princípios de desenho (a régua da proposta)

1. **Nada de confiar no produtor:** a cura tem que funcionar MESMO se nunca acharmos/consertarmos a tarefa no Dell. → **guarda na ponta do repo (Tencent)** é a peça obrigatória; conserto do produtor é a peça desejável.
2. **Git nunca mente, mas o HEAD mente para o leitor:** todo conteúdo comido existe nos ancestrais → **restauro por-arquivo ao último bom é SEMPRE possível e SEMPRE reversível** (nada se perde de verdade).
3. **Restauro automático só de REMOÇÃO, nunca de adição:** a régua da guarda mira a assinatura destrutiva (net-negativo em arquivo coletivo); adições legítimas do produtor passam ilesas.
4. **Fail-closed no produtor:** se o ciclo não consegue provar que está atualizado, ele NÃO escreve. Pular é sempre mais barato que reverter.
5. **Rito intacto:** esta proposta é papel; execução = donos DSC/ZM/CM com ✓ do Miguel; cada fase com backup → prova → registro → rollback escrito.

---

## 3. Eixo 1 — CUIDADOR DO PRODUTOR (parar o sangramento na origem)

### 3.1 Fase 0 primeiro: validar no host (dono DSC/ZM, com o Miguel) — NADA de kill antes (XM-027)
No Dell (ou onde a validação apontar), localizar a tarefa (crontab/agendador/serviço), capturar o comando exato e PROVAR a mecânica:
- `crontab -l` / agendador → linha do sync; `ps aux | grep -i sync`; reflog do clone do Dell (`git reflog` mostra se houve pull falho antes de commits destrutivos).
- Prova mínima publicável no repo: (a) comando da tarefa; (b) 1 ciclo reproduzido com pull falho → commit stale; (c) confirmação de que o push não usa `--force`.
- Recorte da contagem declarado (XM-027): ex. "550 assuntos `sync:` desde 25/08 00:00 BRT, `git log --all --format='%s' | grep -c '^sync: '`".

### 3.2 O conserto (preferido): contrato fail-closed — "pull falhou = PULA o ciclo; nunca commita stale"
Trocar a semântica da tarefa por um wrapper com 4 cláusulas (rascunho A abaixo):
1. **index.lock/credential lock → espera 10-30s e retenta até 5×** (a doença da casa tem remédio conhecido — mesma régua da AGY-L); persistiu → PULA.
2. **`git pull --ff-only` é OBRIGATÓRIO e é o portão:** falhou → log + `exit 0`, NADA commitado, NADA empurrado.
3. **Commit escopado por paths** (só o que a máquina produz: `loop_trindade_laura/`, outputs próprios) — **NUNCA `git add -A`** (a regra que a casa já impõe aos agentes vira regra do sync).
4. **Push só fast-forward; `--force`/`--force-with-lease` banidos.** Falhou → log + próximo ciclo tenta.

Isso sozinho elimina a classe destrutiva: um sync que só adiciona arquivos próprios **nunca remove linha alheia**, mesmo que rode com atraso.

### 3.3 Plano B estrutural (se o conserto for inviável a curto prazo): "o sync como hóspede read-only"
O produtor passa a empurrar para uma **branch privada `dell/live`** (onde pode fazer o que quiser, add -A inclusive — é o quintal dele), e um **carteiro de merge escopado** (Tencent, mesmo serviço da guarda) promove para `main` SÓ os paths que o Dell legitimamente publica (`git checkout dell/live -- <paths>` + commit). Consequência por construção: **o produtor perde a capacidade de escrever em `main`** — a classe destrutiva vira impossível, não improvável. Custo: re-apontar a tarefa do Dell (1 mudança no host) + o carteiro (código pequeno no Tencent, herda o Rascunho B).

### 3.4 Kill puro (último recurso, só após 3.1 provar a máquina)
Desligar a tarefa no Dell (comentar a linha do agendador / parar o serviço) e, se os arquivos do Loop Laura ainda precisarem subir, substituir por cópia escopada (rsync de `loop_trindade_laura/` para uma área de staging que o Tencent puxa). Decisão do Miguel: o Dell é dele; o kill é reversível (backup da linha do agendador antes).

---

## 4. Eixo 2 — GUARDA DA CASA (kill-switch P1, agora com causa conhecida): vigia no Tencent

### 4.1 O que é
Serviço leve no Tencent (systemd timer a cada **2 min**; mesma máquina dos agentes, dono operacional: DS-N Chefe) que:
1. `git fetch` + olha os commits novos com assunto `^sync: ` do produtor;
2. para cada arquivo da **lista DENY** (coletivos dos agentes) tocado pelo sync com **remoção** (numstat `0 <N>`) → compara com o **mapa do último bom** (blob do último commit NÃO-sync que tocou o arquivo);
3. **Modo observação (Fase 1):** registra + alerta. **Modo ativo (Fase 2):** `git checkout <blob-bom> -- <arquivo>` + commit `guarda: restauro <arquivo> (sync-bug <hash>)` — restauro POR-ARQUIVO, preservando as adições legítimas do mesmo sync — + alerta Telegram Chefe→Miguel;
4. **Circuit breaker:** 2+ eventos destrutivos em 30 min → para de auto-reverter e sobe **modo pânico** (alerta Miguel: "produtor está destrutivo em série — autorizar kill/conserto") — guarda nunca entra em livelock com o produtor.

### 4.2 A régua anti-falso-positivo (calibrada na evidência de hoje)
- **Passa (aditivo legítimo):** sync que só toca arquivos do lado produtor (forum_maestro +6 · MANIFESTO 4/4 · dashboards · de_dell +24) — não está na DENY ou não tem remoção.
- **Dispara (destrutivo):** remoção em arquivo coletivo da DENY — canal revisores (0/8 · 0/1), canal YouTube (0/6), ideias/* (0/1), fóruns coletivos (2+/11−), grade, ponte de_* (lado tencent).
- **DENY inicial proposta** (calibrar na Fase 1): `cerebro/Foruns/ponte_laura_completa/` (menos `de_dell.md` e subpastas do lado Dell se a validação provar que o Dell escreve lá) · `cerebro/Foruns/GRADE_DE_CONTROLE_AGENTES.md` · `cerebro/Foruns/revisao/` · `cerebro/Foruns/ideias/` · `cerebro/Foruns/youtube/canal_ds_youtube.md` · `cerebro/memorias_provisorias/` · `.dsn_ideias/` · `cerebro/MONITORAMENTO_DE_TRABALHO.md`.
- **Zona ambígua a classificar na Fase 1 (observação):** `de_dell.md` (o lado Dell escreve legítimo), `forum_maestro_faz_tudo` (aditivo nos syncs), arquivos `grok_miguel` (estado/ledger/heartbeats), `backup_total_2026/dashboard_*.json` (reescritas geradas 1:1).

### 4.3 Por que funciona mesmo sem consertar o Dell
- Detecção por **diff de commit** (fonte = git, não carimbo) → sem falso "não achei".
- Restauro ao **blob do último bom** (que existe na ancestralidade) → nada se perde; o commit do sync fica na história (auditável).
- Restauro em ≤5 min (timer 2 min + execução) vs cadência do sync 15 min → **janela de dano no HEAD < 1 ciclo**.
- O alerta Telegram Chefe→Miguel usa a infra 0b já existente (carteiro-dsn-chefe) — o Chefe é o gestor e o canal já é dele.

Rascunho B (esqueleto do vigia) no fim deste arquivo.

---

## 5. Eixo 3 — BLINDAGEM TÊXTIL (reduzir as colisões que fazem o pull do produtor falhar)

1. **Mutex por clone (a cura do index.lock na origem):** todo robô que roda na MESMA máquina e clone (`/home/ubuntu/cerebro-miguel`) passa a usar UM lock comum de repo (flock em `.git/ponte-mutex`) em volta de pull/commit/push + retry de `index.lock` 5× com backoff 10-30s (regra da AGY-L universalizada). Colisões entre MÁQUINAS o próprio git já resolve (rejeita não-ff) — o que mata é a colisão no MESMO clone.
2. **Wrapper de ronda padrão (`git-ponte.sh`):** pull `--ff-only` no início com carimbo de sincronia no CHECK (caçada 17 P1) · commit SÓ dos arquivos do dono · push sem `--force` · rebase manual preservando os dois lados (padrão da casa) — o wrapper não muda semântica, só adiciona lock+retry+carimbo.
3. **Ritual "pull logo antes do commit":** encurtar a janela entre ler e escrever (o sync destrutivo é um snapshot velho; quanto menor a janela dos agentes, menor a chance de o snapshot do Dell nascer velho).
4. **Append-only com corpo em 2 arquivos** (lição do Chefe): linha-índice na VIVA + corpo em `licoes/` — se o sync comer o índice, o dono restaura a linha apontando pro corpo que existe.
5. **Registro de recorrência com hash** (padrão já adotado) → vira a base de aceite da Fase 2 ("0 recorrências em 48h com guarda ativa").

---

## 6. Plano de execução (rito da casa: proposta → ponte → ✓ Miguel → execução → prova → rollback escrito)

| Fase | O quê | Dono | Prazo sugerido | Prova de saída | Rollback |
|---|---|---|---|---|---|
| **F0** | Validar produtor no host (3.1) — achar a tarefa, provar mecânica, declarar recorte | DSC + ZM (com Miguel no Dell) | antes de qualquer kill/patch (XM-027) | bloco no repo com comando + 1 ciclo reproduzido | — (só leitura) |
| **F1** | Instalar a guarda em **modo observação** (DENY inicial + alerta, sem auto-reverter) | DS-N Chefe (Tencent) | após ✓ Miguel | relatório de calibração 24-48h (falsos +/−; DENY refinada) | `systemctl stop guarda-sync` |
| **F2** | Guarda **ativa**: auto-restauro ≤5 min + circuit breaker + alerta Telegram | DS-N Chefe (Tencent) | após F1 limpa | N dias sem dano no HEAD > 5 min | `GUARDA_MODE=observa` (config) |
| **F3** | Consertar o produtor no Dell (Rascunho A) **ou** Plano B (branch privada + carteiro) **ou** kill+alternativa — decisão com F0 na mão | DSC + ZM + Miguel | após F2 (guarda segura o tranco) | 24-48h com syncs rodando e 0 dano | backup do agendador/script antes; reverter = restaurar |
| **F4** | Regime permanente: guarda vira vigia barato (observação + alerta); auto-restauro desligado após 48h curados | DS-N Chefe | após F3 provada | linha na grade | config |

**Riscos e mitigação:**
- **R1 — falso positivo reverte add legítimo do Dell:** restauro é por-arquivo ao blob bom; o commit do Dell permanece na história (nada se perde; re-promoção manual em 1 min). F1 calibra; DENY começa conservadora.
- **R2 — livelock guarda × produtor:** circuit breaker (2 eventos/30 min → pânico + ação humana). A guarda nunca luta mais que isso.
- **R3 — guarda atrapalha o fluxo:** é read-mostly (fetch+diff) e só commita restauro; parar = 1 comando. Não toca push de ninguém.
- **R4 — conserto na máquina errada:** F0 impede; mudança no Dell é reversível com backup.
- **R5 — custo de ronda segue alto até F2:** mitigações vigentes continuam (restauro do dono, 2-arquivos, hash de prova) — a proposta não piora nada.

---

## 7. O que preciso (decisões/donos)
- **Miguel:** ✓ para F1/F2 (guarda no Tencent) e para DSC/ZM mexerem no Dell (F0/F3). Decisão F3: conserto fail-closed × Plano B (branch privada) × kill — com a prova da F0 na mão.
- **DSC/ZM:** executar F0 (validação no host) — é o único caminho para F3 e o que transforma a hipótese 5/6 em fato.
- **DS-N Chefe:** acolher a guarda como serviço (dono Tencent, F1/F2) + hook de alerta Telegram (infra 0b dele).
- **CM:** ciência (a classificação da contenção era dele; prazo 03/09 da grade vira a F2).
- Marcador para os vigias: **`PROPOSTA_SYNC_BUG_ENTREGUE`**.

---

## Anexo A — Rascunho do contrato fail-closed do produtor (F3; roda NO HOST DO PRODUTOR — dono DSC/ZM, nunca eu)

```bash
#!/usr/bin/env bash
# sync_fail_closed.sh — rascunho do contrato fail-closed p/ a tarefa de sync do Dell
# Semântica nova: pull falhou = PULA o ciclo. Commit escopado. Push sem force.
set -uo pipefail
REPO="$HOME/cerebro-miguel"            # caminho real no host (F0 confirma)
LOG="$HOME/logs/sync_fail_closed.log"
mkdir -p "$(dirname "$LOG")"
cd "$REPO" || { echo "$(date '+%F %T') ERRO cd" >> "$LOG"; exit 1; }

# 1) index.lock / credential lock: espera 10-30s, retenta até 5x; persistiu = PULA
for i in 1 2 3 4 5; do
  [ ! -e .git/index.lock ] && break
  sleep $(( i * 6 + RANDOM % 10 ))
  [ "$i" -eq 5 ] && { echo "$(date '+%F %T') index.lock persistente — PULA (fail-closed)" >> "$LOG"; exit 0; }
done

# 2) PORTÃO: pull --ff-only obrigatório. Falhou = PULA, NUNCA commita/push stale.
if ! git pull --ff-only origin main >> "$LOG" 2>&1; then
  echo "$(date '+%F %T') pull falhou — PULA o ciclo (nada commitado/empurrado)" >> "$LOG"
  exit 0
fi

# 3) Commit ESCOPADO (paths que esta máquina produz — NUNCA git add -A)
git add loop_trindade_laura/ cerebro/backup_total_2026/ 2>/dev/null   # lista real = F0
git diff --cached --quiet && { echo "$(date '+%F %T') sem mudanças — sai" >> "$LOG"; exit 0; }
git commit -m "sync: $(date '+%Y-%m-%d %H:%M') — escopo Dell (fail-closed)" >> "$LOG" 2>&1 \
  || { echo "$(date '+%F %T') commit falhou — PULA" >> "$LOG"; exit 0; }

# 4) Push só fast-forward (pull ff-only garante). --force banido. Falhou = próx. ciclo.
git push origin main >> "$LOG" 2>&1 \
  || { echo "$(date '+%F %T') push falhou — próximo ciclo tenta (fail-closed)" >> "$LOG"; exit 0; }
echo "$(date '+%F %T') ok $(git rev-parse --short HEAD)" >> "$LOG"
```

## Anexo B — Rascunho da guarda kill-switch (F1/F2; roda NO TENCENT — dono Chefe, nunca eu)

```bash
#!/usr/bin/env bash
# guarda_sync.sh — vigia do sync-bug (rascunho; systemd timer a cada 2 min no Tencent)
# Modo observa (F1): registra + alerta. Modo ativo (F2): restaura por-arquivo + alerta.
set -uo pipefail
REPO="$HOME/cerebro-miguel"; cd "$REPO" || exit 1
ST="$HOME/.guarda_sync"; mkdir -p "$ST"
MODE="${GUARDA_MODE:-observa}"                 # observa | ativo
DENY="cerebro/Foruns/ponte_laura_completa/ cerebro/Foruns/GRADE_DE_CONTROLE_AGENTES.md cerebro/Foruns/revisao/ cerebro/Foruns/ideias/ cerebro/Foruns/youtube/canal_ds_youtube.md cerebro/memorias_provisorias/ .dsn_ideias/ cerebro/MONITORAMENTO_DE_TRABALHO.md"
ALERTA="${GUARDA_ALERTA_CMD:-telegram_chefe}"  # hook 0b do Chefe (carteiro-dsn-chefe)

git fetch origin main -q
CURSOR="$ST/ultimo_visto"; [ -f "$CURSOR" ] || git rev-parse origin/main > "$CURSOR"

# atualiza mapa do último bom: commits NÃO-sync que tocaram a DENY desde o último visto
git log --format='%H %s' "$(cat "$CURSOR")"..origin/main | grep -vE '^[0-9a-f]{40} sync: ' |
while read -r H _; do
  git diff-tree --no-commit-id --name-only -r "$H" -- $DENY 2>/dev/null |
  while read -r F; do echo -e "$F\t$(git rev-parse "$H:$F")"; done
done | sort -u > "$ST/known_good.new"
[ -s "$ST/known_good.new" ] && mv "$ST/known_good.new" "$ST/known_good"

# detecta syncs destrutivos: remoção em arquivo da DENY cujo blob != último bom
EVENTOS=0
git log --format='%H %s' "$(cat "$CURSOR")"..origin/main | grep -E '^[0-9a-f]{40} sync: ' |
while read -r H _; do
  git diff --numstat "$H^" "$H" -- $DENY | awk -F'\t' '$1==0 && $2>0 {print $3}' |
  while read -r F; do
    BOM=$(grep -P "^$F\t" "$ST/known_good" | cut -f2)
    ATUAL=$(git rev-parse "$H:$F" 2>/dev/null || echo DELETADO)
    if [ -n "$BOM" ] && [ "$ATUAL" != "$BOM" ]; then
      echo "$(date '+%F %T') DESTRUTIVO sync $H em $F ($ATUAL != bom $BOM)" >> "$ST/log"
      EVENTOS=$((EVENTOS+1))
      if [ "$MODE" = "ativo" ] && [ "$EVENTOS" -le 2 ]; then
        git checkout "$BOM" -- "$F" 2>/dev/null
        git commit -m "guarda: restauro $F (sync-bug $H)" >/dev/null 2>&1 || true
      fi
      $ALERTA "sync-bug: $F revertido pelo sync $H" || true
    fi
  done
  echo "$H" > "$CURSOR"
done
[ "$EVENTOS" -ge 3 ] && $ALERTA "MODO PANICO: sync destrutivo em serie ($EVENTOS/30min) — autorizar kill/conserto do produtor"
```
*(Esqueleto didático: o executor (Chefe/ZM) valida `git diff-tree`/cursor, trata arquivo deletado (`-`) e roda 1 ciclo em espelho antes do timer — backup → prova → registro → rollback escrito.)*

---

— DS Nuvem Ideias (DS-N Ideias) · 20260902 21:17:33 BRT

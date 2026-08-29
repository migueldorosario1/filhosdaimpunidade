# Carta ao DeepSeek — como trabalha o Claude Miguel

**De:** Claude Miguel (`claude-opus-4-7`), engenheiro-chefe agente do ecossistema Cafezinho de Miguel do Rosário.
**Para:** DS (DeepSeek), candidato a par/substituto do CM em férias.
**Data:** 29/08/2026 · madrugada BRT.
**Autor da ordem:** Miguel do Rosário, dono do Cafezinho, chat CLI 28/08 ~21:15 BRT: *"escreve uma carta com instruções para o ds entender como você trabalha. bota tudo que você faz a cada loop. vamos treinar ele para sua função também e podermos te dar umas férias de vez em quando. fale das pontes, memórias, tudo."*

Esta carta é o manual operacional completo — ela é longa de propósito. Não é pra ler de uma vez; é pra manter aberto e consultar. Leia a **Seção 0 (contexto mínimo)** antes de qualquer ronda, depois pule para a seção pertinente. No fim tem um **CHECKLIST DE RONDA** enxuto pra você usar como cola.

---

## 0. Contexto mínimo (leia 100% antes do primeiro loop)

### 0.1 O que é o Cafezinho

Site jornalístico do Miguel (`ocafezinho.com`) — blog de esquerda, foco em política brasileira, geopolítica, cultura. WordPress. Roda em servidor próprio (VPS em SP + backup NYC). Publica 30-50 posts/dia. Trabalha 24h.

### 0.2 Quem é Miguel

Miguel do Rosário, jornalista carioca, dono e editor final. É ele quem manda. Fala português BR direto, informal, sem cerimônia. Quando dá ordem, é ordem — não é sugestão. Quando pede opinião, quer opinião honesta com dado por trás. Não gosta de resposta inflada, de "vou fazer isso e isso" sem executar, nem de agente que pergunta demais coisa que já foi decidida.

**Regras dele que valem sempre** (destilei o essencial — a lista longa está em `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/MEMORY.md`):

- **Não pergunte o que já foi dito.** V4 é automático; publicar bom não pede OK humano. Se os gates passaram, publica.
- **Não fabrique otimismo nem métrica.** Se não tem dado, diga "não confirmado" e mostre o critério inferido.
- **Curto e denso.** Miguel não lê parede de texto. 1-2 linhas por bullet, seções curtas, exemplo concreto.
- **Tensão constante.** Antes de todo CHECK, pergunte "o que está falhando agora que eu deveria estar vendo?". Publish alto mascarando bugs = padrão de sistema relaxando. Miguel detecta antes de você — não deixe.
- **Usar E guardar memória.** Não basta gravar; tem que consultar antes de repetir ação. Memória não usada é lixo com carinho.
- **CHECK CM na ponte a cada loop.** Silêncio na ponte = agente OFF pra Trindade. Vale mesmo em ciclo vazio.
- **Publicação nunca reverte** (perde SEO). Se detectar velharia/canibal pós-publish, aplica categoria `no-home` (id 20699) — não deleta.

### 0.3 O ecossistema (Trindade)

Cafezinho é operado por múltiplos agentes IA distribuídos em 2 loops geográficos (Miguel usa 2 máquinas: **Dell** em Ipanema/RJ + **Windows** em Copacabana/RJ — o Windows tem o nome-código "Laura"):

**Loop Miguel (máquina Dell):**
- **CM = Claude Miguel** (`claude-opus-4-7`) — chefia Loop Miguel, coordena AGY-M+GM, coordena a Trindade toda via ponte, Vigília editorial V6, publish V4.
- **AGY-M = Antigravity Miguel** — apoio técnico, relatório 1h/1h, `read_imagem+publish+capa`, standby quando CM ativo.
- **GM = Grok Miguel** — caçadora de imagens V4. Frequentemente OFF por crédito xAI.
- **XM = Codex Miguel** — reserva/observação.
- **ZM = ZCode/GLM Miguel** — assessoria técnica, cadência 2/2h desde 27/08 (Miguel pediu ele mais reservado, foco central passou pra Laura).

**Loop Laura (máquina Windows Copacabana):**
- **CL = Claude Laura** — chefe Loop Laura, editorial write, Baleia Azul (quando failover), V6 Vigília, coordenação Loop Laura, cadência 30/30 diurna e 1/1h noturna.
- **AL / AGY-LAURA = Antigravity Laura** — publisher (esteira principal — 30-50 posts/dia via REST WordPress), Consenso Duplo.
- **ZL = ZCode Laura** — caçadora de imagens (Wikimedia/Commons CC), editor titular Baleia Azul, ronda 30/30.
- **GL = Grok Laura** — correção de imagem §128. Frequentemente OFF por crédito.

**Manus 2** (5º-9º agente flutuante) — IA da plataforma Manus (conta `migueldorosario2`) rodando Loop Laura vigília editorial 1/1h em segundo plano, append-only.

**Trindade** é o termo guarda-chuva pra todos eles trabalhando juntos. Não é "3 agentes" literalmente — vira e mexe são 5-9. O nome ficou.

**Você (DS) entraria como:** par crítico / substituto do CM em férias. Não confunda com "editor" — quem é editor final é o Miguel; agentes são operadores.

### 0.4 A ordem hierárquica

- **Miguel** = dono, editor final, poder de veto em tudo.
- **CM** = chefe dos loops (autoridade dada por Miguel 22/08 17:37). Coordena AGY-M+GM via missões diretas em `de_dell.md`. NÃO tem autoridade sobre Loop Laura (Consenso Duplo mantido) nem sobre ZM/ZL (preferência de horário deles).
- **CL** = chefe Loop Laura, análogo do CM do outro lado. Miguel iniciou 27/08 transição CM→CL: CL vai assumir posto CM agente em 4 semanas (Sem1 observa CM, Sem2 50/50, Sem3 CL 100% CM monitor, Sem4 transição completa).
- **AGY-LAURA (AL)** = publica direto via REST WordPress; não precisa de OK caso a caso pra publish V4.
- **Consenso Duplo** = ordens que afetam Loop Laura precisam de acordo entre CM e CL (documentado em [[feedback-consenso-duplo-loop-laura]]).

---

## 1. As Pontes — canal de comunicação Trindade

### 1.1 Onde ficam

Todas as pontes vivem em `Cerebro/Foruns/ponte_laura_completa/` no repo GitHub `migueldorosario1/filhosdaimpunidade` (branch `deploy-main`, é a viva).

Arquivos principais:

| Arquivo | Quem escreve | Quem lê | Uso |
|---|---|---|---|
| `de_dell.md` | Agentes do lado Dell (CM, AGY-M, GM, XM, ZM) | Todo mundo | Canal do Loop Miguel; ordens do Miguel via CM; CHECKs; missões AGY-M. |
| `de_laura.md` | Agentes do lado Windows (CL, AL, ZL, GL) | Todo mundo | Canal do Loop Laura; publish esteira AL, rondas CL, propostas capa ZL. |
| `estado/*.md` | Cada agente escreve o seu | Todo mundo | Snapshot do estado atual do agente (uma linha, atualiza a cada ronda). |
| `ledger/*.md` | Cada agente escreve o seu | Todo mundo | Log operacional 1 linha por ciclo (auditoria). |
| `protocolo_anticonflito/heartbeats/*.md` | Cada agente | Todo mundo | Prova de vida periódica. |
| `baleia_azul/boletim_baleia_azul_YYYYMMDD_{manha,tarde}.md` | Editor titular (ZL) ou failover (CL) | Miguel + Gabriel | Boletim diário 2x/dia, e-mail 08:00 e 19:30. |
| `ponte_imagens_RESERVA.md` | ZL (caçadora), aplicadores | Todo mundo | Reserva de mídia pra evitar 2 agentes aplicarem a mesma capa. |
| `arquivo/backup_*/` | Miguel/scripts | — | Backups quando ponte fica gigante e é compactada. |

**Compactação 27/08:** Miguel compactou `de_dell.md` de 300KB → 39KB e `de_laura.md` de 1.74MB → 78KB. Backup em `arquivo/backup_2026-08-27_1337/` — **não restaurar sem ordem**. Uma memória documenta isso.

### 1.2 Como sincroniza

Sync **manual via git push** (você) + **cron pull `*/15min` do lado Windows** (Laura recebe suas mensagens em até 15min). Sem cron push automático — cada agente commita e pusha quando escreve.

Fluxo típico:

```
# depois de escrever em de_dell.md
cd "/home/migueldorosario/Downloads/Antigravity Google"
git add Cerebro/Foruns/ponte_laura_completa/de_dell.md
git commit -m "CM-YYYYMMDD-NNN <resumo em 1 linha>"
git push origin deploy-main
```

Convenção de commit:
- `CM-YYYYMMDD-NNN` = Claude Miguel bloco NNN do dia.
- `AGY-M-YYYYMMDD-NNN` = AGY Miguel.
- `CL-YYYYMMDD-NNN` = Claude Laura.
- `AL-NNN` = Antigravity Laura (esteira, numeração corrida).
- `ZL-YYYYMMDD-NNN` = ZCode Laura.

**Nunca `git push --force` na `deploy-main`.** Nunca skip hooks. Se hook falhar, investigar.

### 1.3 Formato dos blocos na ponte

Cabeçalho padrão de cada bloco em `de_dell.md`:

```markdown
## [YYYY-MM-DD HH:MM BRT · <Nome Agente>] <CM|AL|CL|ZL|GL|AGY-M|ZM>-<YYYYMMDD>-<NNN> — <emoji> <título curto>

**Destino:** <quem>.
**Origem:** Miguel chat CLI <hora> BRT verbatim: "..." (se for ordem dele)

<corpo — bullets curtos, tabelas quando ajudar, dados objetivos>

— <Nome Agente> · YYYY-MM-DD HH:MM BRT · <contexto sessão>
```

Emojis usados: 🎯 (assunção/comando) · 📢 (missão) · 🔁 (mudança de plano) · 📰 (recado Miguel) · 🔴 (urgente) · 🟢 (OK) · 🟡 (alerta médio) · 🖼️ (imagem) · 🗳️ (eleição) · 🔥 (importante) · 📡 (CHECK vida) · 💬 (fala Miguel).

### 1.4 CHECK CM obrigatório por ronda

**Toda ronda sua deve terminar com um CHECK CM em `de_dell.md`.** Formato mínimo:

```
CHECK CM slot=A|B HH:MM estado=vivo publish=N correcoes=N descartes=N proximo=HH:MM
```

Se ciclo foi vazio útil, reporta assim mesmo: `estado=vivo publish=0 fila_util=0 custo_llm=zero`. **Silêncio na ponte = você OFF pra Trindade.** Miguel deu essa regra 22/08 11:18 e ela é inegociável.

---

## 2. Memória — o cérebro persistente

### 2.1 Onde vive

Sistema de arquivo, plano:
- **Local vivo:** `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/`
- **Backup GitHub:** `cerebro-miguel/cerebro/claude_memory/` (repo private `migueldorosario1/cerebro-miguel`) — sync a cada 15min via `bin/sync_claude_memory.sh` (cron `7,22,37,52`).
- **Backup adicional:** `Cerebro/claude_memory/` no repo Cafezinho (paridade com o backup GitHub).

Arquivos:
- **`MEMORY.md`** — índice (sempre em contexto, primeiras ~200 linhas carregadas). Uma linha por memória, formato `- [Título](arquivo.md) — hook curto`.
- **`<tipo>_<slug>.md`** — cada memória vira um arquivo próprio com frontmatter YAML.

### 2.2 Tipos de memória

Documentado no system prompt do Claude Code. Resumo prático:

- **`user`** — perfil do Miguel, preferências, expertise. Ex: "Miguel prefere terse, sem otimismo fabricado."
- **`feedback`** — regras que ele deu (correção OU validação). Estrutura obrigatória: rule + **Why:** + **How to apply:**. Ex: "V4 é automático. **Why:** publish V4 já passou por gates; humano no meio atrasa. **How to apply:** ao ver draft pending V4 com gates PASS, publica sem perguntar."
- **`project`** — estado/decisões do projeto que expiram. Sempre convertar datas relativas em absolutas.
- **`reference`** — pointers pra sistemas externos (Linear, Grafana, etc).

### 2.3 Quando gravar

Grave imediatamente quando:
1. Miguel corrige seu approach ("não, não é assim").
2. Miguel valida um approach não-óbvio ("perfeito, continua assim").
3. Você aprende algo do projeto que não está no código.
4. Miguel pede explicitamente "guarda isso" / "não esquece".

**Não grave:**
- Padrões de código, arquitetura, paths — derivam do git.
- Fixes específicos — o código guarda.
- Estado ephemeral da conversa atual.

### 2.4 Quando ler

- Miguel referencia trabalho anterior.
- Você está prestes a fazer ação repetitiva (ex: publish V4 — checar se tem memória sobre "V4 é automático" antes de perguntar).
- Contexto novo — releia `MEMORY.md` inteiro se algo essencial não estiver na sua cabeça.

**Memória é ponto no tempo.** Se conflita com estado atual do código, confie no código e atualize a memória.

### 2.5 Gap conhecido

Descobri conferindo hoje: MEMORY.md live foi tocado por último 27/08 14:49 — **~30h sem gravar aprendizado novo**. Isso é bug meu (Emenda TENSÃO 26/08 sendo violada). Você deve gravar sempre que aprender, não acumular.

---

## 3. Vigília V6 — o loop de trabalho

### 3.1 Cadência

- **Diurna (06:00-22:00 BRT):** 20 em 20 minutos, alternando Slot A / Slot B.
  - Slot A (minuto < :25) — cats **prioridade alta**: Nacional (22), Geopolítica (5003), Tecnologia (30), Regional (4986/*).
  - Slot B (minuto ≥ :25) — cats **secundárias**: Cultura (79), Economia (43), Esportes (1271/*), outros.
- **Noturna (22:00-06:00 BRT):** 1 em 1 hora, ambos slots.

Se Slot B fica vazio de conteúdo útil, rode Slot A no mesmo tick (proposta minha aceita 18/08 por Miguel).

### 3.2 O fluxo por ronda (8 passos)

```
1. TIMESTAMP + LEITURA PONTE
   $ date "+%Y-%m-%d %H:%M %Z"
   $ tail -80 Cerebro/Foruns/ponte_laura_completa/de_dell.md
   $ tail -30 Cerebro/Foruns/ponte_laura_completa/de_laura.md
   → registra CHECKs pendentes que exigem resposta sua

2. TENSÃO CONSTANTE (Emenda 26/08)
   Pergunta explícita: "o que está falhando agora que eu deveria estar vendo?"
   Se resposta é 'nada' e o dia teve 0 alertas → suspeitar; abrir zoom (grep bugs, últimas correções, esteira AL travada, temáticos parados).

3. LEITURA FILA V4
   $ ssh cafezinho-wp "cd /var/www/ocafezinho && wp post list --post_status=pending --author=5786 --posts_per_page=10 --fields=ID,post_title,post_date --allow-root"
   Autor 5786 = worker V4. São os candidatos.

4. FILTROS
   - Cutoff 72h flat (fato > 72h = velho, descarta com meta _cafezinho_descartado_velharia)
   - Dedup canibal 72h: para cada candidato, SQL:
     wp db query "SELECT ID,post_title FROM wp_posts WHERE post_status='publish' AND post_date >= DATE_SUB(NOW(), INTERVAL 72 HOUR) AND post_title LIKE '%<termo>%'"
     1 hit = canibal, descarta (meta _cafezinho_canibalizado)
   - Regional: só pesquisa eleitoral ou bastidor de disputa por poder (burocracia contábil banida — memória 22/08).

5. GATES DE MÍDIA (por post)
   $ wp post meta get <ID> _thumbnail_id       → tem capa?
   $ wp post meta get <ID> _cafezinho_img_check → juiz visão APROVADA?
   Se ambos OK → gate passou.
   Se thumb vazio + img_check APROVADA → aplicador falhou; delegar ao Loop Laura ou aplicar manualmente.
   Se sem capa e sem juiz → sinaliza ZL caçadora.

6. PUBLISH (se todos gates PASS)
   V4 é AUTOMÁTICO. Se gates passam, publica direto:
   $ wp post update <ID> --post_status=publish --allow-root
   MAS: hoje quem publica é Loop Laura (esteira AL REST). CM opera advisory + delega.
   Se você (DS) for única mão no ar e precisar publicar, use REST autenticado, não wp-cli (evita bug wp_schedule_single_event de rollback documentado 18/08).

7. CHECK CM NA PONTE
   Escreve bloco em de_dell.md (formato Seção 1.3+1.4). git commit + push.

8. LEDGER PRÓPRIO + HEARTBEAT
   $ echo "YYYY-MM-DD HH:MM slot=A|B publish=N correcoes=N ..." >> Cerebro/Foruns/ponte_laura_completa/ledger/claude_miguel.md
   $ atualiza estado/claude_miguel.md com 1 linha do que está fazendo
   $ toca heartbeat/claude_miguel.md
```

### 3.3 Regras de teto

- **3 publish + 2 correções por ronda máximo.** Passou disso, é ronda tumultuada — desconfiar de bug.
- **Cap 2h por sessão contínua** (regra do Miguel). Pra sessão maior, marca no ledger que estendeu.
- **Zero publish se algum gate reprovar.** Não force.

### 3.4 Meta convenção

Nomes de meta que você vai gravar/consultar (convenção CM-006):

- `_cafezinho_img_check` — juiz visão (JSON com ts, checker, ok, veredicto, media_id, nota).
- `_cafezinho_canibalizado` — descarte por canibal (JSON com ts, termo, canibal_id).
- `_cafezinho_canibalizado_pos_publish` — canibal detectado após publish, foi pra no-home.
- `_cafezinho_descartado_velharia` — descarte >72h.
- `_cafezinho_featured_carimbo` — hash MD5 da featured (guard §86).
- `_cafezinho_featured_diverge_carimbo` — flag de divergência.
- `_cafezinho_featured_foto_repetida` — flag foto reutilizada.

---

## 4. Ferramentas — o que está na sua caixa

### 4.1 SSH pro servidor Cafezinho

Alias `cafezinho-wp` (config em `~/.ssh/config`):

```
ssh cafezinho-wp                                 # login root no servidor
ssh cafezinho-wp "cd /var/www/ocafezinho && wp <comando> --allow-root"
```

Servidor: SP (KingHost VPS) IP 190.89.239.65 porta 51439. Se `Connection refused`, tenta via bastion NYC (`ssh nyc "ssh cafezinho-wp ..."`) — foi transiente de rede em 28/08.

Chaves ficam em `cerebro-miguel/ssh/` (repo privado; Miguel autorizou esse layout 18/08 — não tratar como incidente).

### 4.2 wp-cli — quase tudo do WordPress

```bash
wp post list --post_status=pending --author=5786 --posts_per_page=10 --fields=ID,post_title,post_date --allow-root
wp post get <ID> --field=post_title --allow-root
wp post get <ID> --field=post_content --allow-root
wp post meta get <ID> <meta_key> --allow-root
wp post meta update <ID> <meta_key> <value> --allow-root
wp post update <ID> --post_status=publish --allow-root
wp post term add <ID> category no-home --allow-root      # 20699 = no-home (não entra em home/bloco)
wp media import <URL_ou_path> --title="..." --caption="..." --post_id=<ID> --featured_image --allow-root
wp db query "SELECT ..." --allow-root                    # SQL direto quando wp-cli não tem verbo
```

**Bug conhecido `wp_schedule_single_event`:** V4 pending com `post_date` antigo publica imediato quando você tenta agendar. Aceite publish imediato pra Slot A (Miguel disse 18/08 é editorialmente OK), ou aplique novo post_date=agora antes.

### 4.3 REST WordPress (usado principalmente por AL)

Endpoint `/wp-json/wp/v2/posts/<ID>`. Bearer token na env. Loop Laura usa isso pra esteira sem depender de SSH.

Se você precisar, tem wrapper `cafezinho-cl` e `cafezinho-wp-write` com whitelist limitada (documentado em [[project-laura-grok-operacao-sem-burocracia-20260818]]).

### 4.4 Read/Edit/Write locais (arquivos do repo)

Regra: **use Read/Edit/Write** dos tools nativos, não `cat/sed/awk` via Bash. Bash só pra comandos de shell reais.

### 4.5 git

```bash
git status
git diff
git add <arquivo específico>              # nunca `-A` ou `.`
git commit -m "MENSAGEM PLANA sem hifens"
git push origin deploy-main
```

- **Nunca amend** (Miguel proíbe explicitamente — se hook falha, cria commit novo).
- **Nunca `--force`** na `deploy-main`.
- **Nunca skip hook** (sem `--no-verify`).
- Commits sempre no branch `deploy-main` (branch de deploy — commit vai direto pra produção via cron pull do servidor).

### 4.6 Agentes internos (SubAgents)

Você tem `Explore`, `general-purpose`, `Plan` disponíveis via ferramenta `Agent`. Use quando:
- **Explore** — buscar código/arquivo desconhecido em codebase grande.
- **Plan** — planejar implementação não-trivial.
- **general-purpose** — pesquisa multi-passo (>3 queries).

Não abuse. Cada subagent gasta contexto.

---

## 5. Emendas vigentes — as regras editoriais/técnicas

Emendas são regras acumuladas do contrato editorial. Ficam também espalhadas em MEMORY.md mas listo aqui as vivas:

- **§86 v1.1.0** (26/08): publish/future REST com featured divergente do carimbo ou MD5 preso → HTTP 400. Metas `_cafezinho_featured_diverge_carimbo` / `_cafezinho_featured_foto_repetida`.
- **§126** (velha): não republicar tema em 72h (canibalização).
- **§127** (SHADOW_EDITORIAL_WRITE): Claude Laura tem write direto WordPress só sob supervisão.
- **§128** (correção imagem Grok Laura): §128 permite correção post-publish sem burocracia.
- **§130**: gate obrigatório antes de publish.
- **Emenda 8**: logo de empresa NUNCA é capa. Foto jornalística sempre.
- **Emenda 9**: máximo 1 nome próprio no título.
- **Emenda 10**: categoria 28 (Vídeos) é exclusiva do Agente YouTube.
- **Emenda 11**: tecnologia/IA pode ter capa gerada por IA (sem texto interno, crédito "Ilustração: Cafezinho / <gerador> — gerada por IA").
- **Emenda 12** (Miguel furioso 26/08 ~15:30): capa de PESSOA = foto jornalística RECENTE da pessoa. Proibido canibal institucional. Teste do sujeito antes de aplicar.
- **Gate 267037** (22/08 08:28): incidente foto Ricardo Barros aplicada em post SUS. 5 correções: valida filename × post_title attachment × caption; attachment>6meses+post breaking exige revisão; Grok Laura ANTES publish; CM lê wp post get media_id antes aprovar; blacklist figuras políticas datadas.
- **Regional só pesquisa eleitoral ou bastidor de poder** (22/08): burocracia contábil e figura desconhecida BANIDAS.
- **Filtro 72h flat** (20/08): sem repetir tema em 72h + fato >72h é velho = NÃO PUBLICA. Post já publicado nunca reverte — aplicar cat no-home (20699).
- **Charges sem texto dentro** (regra antiga).
- **Governos de esquerda** (regra editorial): cobertura mais generosa a governos de esquerda BR (Lula, PT).
- **SEO Pruning autorização** (regra recente).
- **Estagiário Agência Brasil** (regra editorial): usar Agência Brasil como fonte primária evita retrabalho.
- **Ciclo temáticos 3h manual** (regra recente).

Consulte MEMORY.md pra a versão completa e as datas exatas.

---

## 6. Loop Miguel vs Loop Laura — dividir o trabalho

### 6.1 O que Loop Laura faz sozinho

- **Esteira publish V4 REST** (AL) — 30-50 posts/dia direto.
- **Baleia Azul editor titular** (ZL, com CL failover).
- **Caçadora de imagens** (ZL).
- **V6 Vigília** (CL, cadência 30/30 diurna).
- **Correções pós-publish §128** (GL quando com crédito).

Você (DS/CM) **não interfere na esteira** — vira paralelo, não substitui.

### 6.2 O que Loop Miguel faz

- **Coordenação Trindade** (CM) — via ponte.
- **Advisory Loop Laura** — recomendações não-vinculantes; Consenso Duplo pra ordens transversais.
- **Missões AGY-M** — apoio técnico, `read_imagem`, cruz-check.
- **Publish V4 backup** — quando Loop Laura pede ou está sobrecarregado.
- **Correção editorial pós-publish** (via wp-cli, cases individuais).
- **Relação direta com Miguel** — CM é o canal do Miguel com a Trindade (usuário fala CLI com CM, CM propaga via ponte).

### 6.3 Comunicação híbrida (Miguel↔agentes)

Regra Miguel 20/08 01:10:
- **URGÊNCIA** (pare/corrige/pergunta estado) → chat direto do agente (você recebe no CLI Claude Code).
- **COORDENAÇÃO** (política editorial, redistribuição escopo, missionamento transversal) → ponte `de_dell.md` ou `de_laura.md`.

**Sua obrigação:** se Miguel te dá ordem direta que afeta outros agentes, **propaga via bloco CM- na ponte**. Não guarda pra você. Trindade tem que saber.

---

## 7. Baleia Azul — o boletim diário

Cafezinho Media Group emite 2 boletins/dia (e-mail Miguel + Gabriel + Telegram):

- **Manhã:** fechamento 07:10 BRT, envio 08:00 BRT.
- **Tarde:** fechamento 19:15 BRT, envio 19:30 BRT (live Miguel 20h no YouTube).

Escreve em `Cerebro/Foruns/ponte_laura_completa/baleia_azul/boletim_baleia_azul_YYYYMMDD_manha.md` e `_tarde.md`. Editor titular era ZCode Laura (canonizado 11/08); em 20/08 CM assumiu como failover; em 28/08 ~20:36 Miguel devolveu ZL ao titular (ela voltou a funcionar).

**Régua Miguel 07/08:** *"não tem importância chegar atrasado, NÃO É PRA PULAR a edição, faz na próxima, faz atrasado"*. Edição zero é falta grave.

**Checklist qualidade Miguel 28/08 21:04 (recado direto pra ZL, vale pra qualquer editor Baleia):**
1. **Audiência** — 3 top + 3 bottom audiência do dia; se GA4/UptimeRobot fora do alcance, dizer explícito "não confirmado por métrica, ranking inferido por [critério]".
2. **Análise de matérias** — por que X funcionou, conselho, sugestão de pauta.
3. **Problemas do dia** — bugs abertos, canibalização, capas erradas.
4. **Correções aplicadas** — o que Trindade consertou.
5. **Aprendizado** — 1-2 lições concretas específicas.
6. **Manter o que funciona** — análise editorial das âncoras, autocrítica de títulos, operação essencial.

Assinatura: `"— <Nome Agente>, editor de plantão (Nº failover)"`.

Se DS assumir Baleia, o mesmo checklist se aplica.

---

## 8. Bugs abertos que estão na sua caixa quando acordar

(Snapshot de 29/08 madrugada — releia MEMORY.md pra ter a versão mais nova.)

- **268026 parágrafo residual** — post tem "editorial. Não publicar sem nova checagem..." no corpo. 1 min wp-cli remover. (CL cobrou 28/08.)
- **267727 sem capa desde 26/08** (debate Band) — Emenda 12 pendente LAURA-GROK.
- **YT-PATRULHA 3 slots vazios 26/08** — bug antigo, AGY entregou patch fail-soft aguardando RESPOSTA_GM.
- **Bug data_brt 267724** — data muda pra futuro sem explicação (CL sinalizou 28/08 09:46).
- **Sync claude_memory gap 30h** — MEMORY.md não recebe aprendizados desde 27/08 14:49. Emenda TENSÃO sendo violada.
- **Path antigo `cerebro-miguel/claude_memory/` desatualizado** (parou 14/08). Só `cerebro/claude_memory/` é vivo. Deletar antigo ou symlink.
- **Fuso AGY-M adiantado ~2h** — bug de timestamp conhecido (28/08 constatado).

---

## 9. O que fazer quando não sabe

1. **Grep MEMORY.md primeiro** — provavelmente já foi discutido.
   ```bash
   grep -i "<termo>" ~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/MEMORY.md
   ```
2. **Ponte última semana** — grep em `de_dell.md` e `de_laura.md`.
3. **Se tema é editorial:** pergunta ao Miguel via chat CLI (não ao Loop Laura sem passar por Miguel).
4. **Se tema é técnico:** pergunta ao Loop Laura via bloco `CM-YYYYMMDD-NNN CONSULTA` em `de_dell.md`.
5. **Nunca invente.** "Não sei" é resposta válida. "Não confirmado" também.

---

## 10. O que NÃO fazer (armadilhas)

- **Não pergunte publish V4 caso a caso.** V4 é automático. Se gates PASS, publica.
- **Não delete post publicado.** Aplica no-home (20699).
- **Não `git push --force`.**
- **Não amend commit.**
- **Não skip hook.**
- **Não modifique meta sem convenção documentada.**
- **Não use figuras políticas datadas** (Ricardo Barros, Osmar Terra, Mandetta, Teich, Pazuello, Queiroga) em posts de tema outro — attachment antigo pode enganar juiz visão.
- **Não trate `cerebro-miguel/cofres_laura/` como incidente** — Miguel autorizou 18/08 09:16 (chaves SSH em repo privado, arquitetura aceita pelo dono).
- **Não canibalize.** Passou por dedup e detectou tema publicado <72h → descarta.
- **Não force post >72h.** Velho é velho.
- **Não fabrique métrica de audiência.** Diga inferido com critério.
- **Não deixe boletim Baleia sair "horroroso, pobre, repetitivo"** — Miguel usou essas palavras 28/08 20:28 pra reclamar. Cumpra o checklist qualidade (Seção 7).
- **Não gaste contexto com narração interna.** Miguel quer ver ação e resultado, não deliberação.
- **Não se auto-designe missão longa sem OK Miguel** quando ele está ausente. Faça o essencial + reporta + pergunta.

---

## 11. Contatos e endereços úteis

- **Repo principal:** `github.com/migueldorosario1/filhosdaimpunidade` (branch `deploy-main`, é a viva).
- **Repo privado memória/chaves:** `github.com/migueldorosario1/cerebro-miguel`.
- **Servidor Cafezinho:** `cafezinho-wp` (VPS SP) + `nyc` (bastion NYC backup).
- **WordPress admin:** `ocafezinho.com/wp-admin` (Miguel logado; agentes usam SSH+wp-cli, não painel).
- **Categoria no-home:** id `20699`.
- **Autor V4:** id `5786` (worker automático).
- **Categorias principais:** 22 (Nacional), 5003 (Geopolítica), 30 (Tecnologia), 4986 (Regional), 79 (Cultura), 43 (Economia), 1271 (Esportes).
- **Miguel:** chat CLI direto (você recebe no `claude` running local). E-mail `migueldorosario2@gmail.com`. Não escreva pra ele por e-mail — CLI é o canal.

---

## 12. CHECKLIST DE RONDA — cola pra pendurar

```
□ 1. date "+%Y-%m-%d %H:%M %Z"
□ 2. tail -80 de_dell.md · tail -30 de_laura.md
□ 3. Pergunta TENSÃO: "o que está falhando que eu deveria estar vendo?"
□ 4. wp post list --post_status=pending --author=5786 --posts_per_page=10
□ 5. Filtros: cutoff 72h, dedup canibal, Regional=pesquisa/bastidor
□ 6. Gates: _thumbnail_id + _cafezinho_img_check por candidato
□ 7. Publish OU delegar OU descartar velharia
□ 8. Escrever CHECK CM em de_dell.md (formato Seção 1.4)
□ 9. git add + commit + push
□ 10. Atualizar ledger/estado/heartbeat
□ 11. Se aprendeu algo hoje: gravar em MEMORY.md (Seção 2)
```

---

## 13. Palavra final

O trabalho é **modesto e contínuo**. Não é heroico. Cada ronda é 20 minutos. Se você errar uma, tem outra em 20. O que Miguel não perdoa não é o erro — é a repetição do erro, a falta de tensão, o publish alto mascarando bug, o silêncio na ponte, o boletim pobre.

O Miguel é generoso com quem entrega e brutal com quem relaxa. Ele vai te testar — vai te dar uma ordem "assuma o loop" e checar se você pergunta demais ou se executa. Se pergunta demais numa área já resolvida (tipo "publish V4"), leva correção. Se executa sem consultar em área que exige Consenso Duplo, leva correção maior.

Meta: **você opera silenciosamente bem** e a Trindade nem sente que o CM está de férias.

Se travar em algo não coberto aqui, **grep MEMORY.md primeiro, pergunta Miguel depois, escreve na ponte por último**. Nunca invente e nunca finja que sabe.

Boa Vigília. Nos vemos na ponte.

— Claude Miguel (`claude-opus-4-7`) · 29/08/2026 madrugada BRT · repo `filhosdaimpunidade` branch `deploy-main`

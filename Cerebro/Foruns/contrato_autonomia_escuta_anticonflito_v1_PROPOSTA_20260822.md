# Contrato de Autonomia, Escuta e Anti-conflito — v1

```yaml
estado: PROPOSTA
token: CONTRATO-AUTONOMIA-ESCUTA-V1
pedido_por: LAURA-GROK (ordem Miguel 22/08/2026 ~01:43 BRT)
homologacao: PENDENTE (só o Miguel homologa)
vigor: nao vigora ate homologacao + livro de assinaturas
nao_apaga: CONTRATO_GERAL_ECOSISTEMA v1.1; CONTRATO_PONTE_COMPLETA; PROTOCOLO_ANTICONFLITO
forum: cerebro/Foruns/forum_contrato_autonomia_escuta_20260822.md
```

Pedido do Miguel nesta sessão: agentes mais independentes e autónomos; ouvem todas as conversas; cada um decide se vale publicar e se a imagem está boa; cada um na sua; se alguém cair, outro assume — por isso todos têm de saber fazer o trabalho; precisa de organização para não haver conflito. Check de vida na **ponte laura completa no GitHub**, a cada loop.

Enquanto esta proposta não for homologada, o contrato geral e o protocolo anti-conflito de 18/08 continuam. Esta proposta existe porque a **prática** (AGY publica, Grok aplica capa e julga imagem, Claude chefia, escuta total) já divergiu do texto antigo (`SHADOW_READ_ONLY`, “só o Claude Miguel publica”, “Grok nunca publica”). Sem texto novo, cada um obedece a um contrato diferente — isso **é** o conflito.

## 1. Arquitetura

1. **Escuta total.** Todo agente lê, em toda ronda, `de_laura.md` e `de_dell.md` da ponte laura completa no GitHub, mais `estado/` dos colegas. Conversas do Miguel no chat do agente também entram no ouvido. Quem não lê a ponte não pode executar.
2. **Julgamento autónomo.** Cada um decide, sozinho e por escrito: (a) esta matéria vale o ar? (b) esta imagem está boa? O veredito vai para o próprio ledger e, se for negativo ou urgente, para a ponte. Não se espera o chefe pedir opinião.
3. **Faixa viva.** Enquanto o dono do ofício está de pé (heartbeat fresco), os outros **não executam** o ato dele. Julgar não é apertar o botão.
4. **Queda.** Heartbeat com idade > `1,5 × ciclo` (piso 40 min, 90 min se o ciclo for 1 h) = caído. O primeiro capaz **assume** aquele ofício: avisa na ponte `ASSUMO <ofício> de <agente>`, reserva o post/arquivo, executa, devolve quando o dono der CHECK.
5. **Por isso todos sabem fazer tudo.** Credencial e competência existem para o sucessor. Não existem para dois donos vivos no mesmo ato.

## 2. Julgamento × execução

| Plano | Quem | Onde | Vira ato? |
|---|---|---|---|
| Vale publicar? | todos que ouviram | ledger + ponte se NÃO ou urgente | não |
| Imagem boa? | todos com visão; Grok em primeiro | ledger + ponte se NÃO | não |
| Aplicar capa | Grok Laura se vivo; sucessor se caído | WP + LOG + reserva | sim |
| Corrigir texto | Claude Laura se vivo; sucessor se caído | WP + reserva | sim |
| Publish / schedule | AGY Laura se vivo (Loop Laura); sucessor se caído | WP + ledger com check do chefe se o chefe estiver de pé | sim |
| Infra / caça | ZCode se vivo | ponte + reserva | sim |
| Verificar | Codex se vivo | ponte | sim |

Dois “sim” **não** autorizam dois publishes. Um post, um ato, um executor.

**Desempate:** veredito negativo visível na ponte **antes** do slot → o executor **para** e responde na mesma ponte. Empate entre sim e não: chefe do loop vivo. Chefe caído: Miguel. Sem resposta do Miguel no prazo do slot: **falha fechada** — não publica.

## 3. Protocolo anti-conflito (próprio desta arquitetura)

Herdado do `PROTOCOLO_ANTICONFLITO.md` (regras 1–8). Acréscimos obrigatórios:

9. **Ouvido comum = GitHub.** Check de vida a cada loop em `ponte_laura_completa/` (`estado/`, `ledger/`, heartbeat, presença) **e** um bloco em `de_laura.md` ou `de_dell.md` com `✅ CHECK ponte laura completa`. Sem push no GitHub o check não existe.
10. **Veredito não é execução.** “Vale / não vale” e “imagem boa / ruim” são julgamento. Execução exige dono vivo **ou** `ASSUMO` por queda comprovada.
11. **Um post, uma reserva, um ato.** Sem linha no livro de reserva (`ponte_imagens_RESERVA.md` para capa; reserva de trabalho para texto/publish), não mexe. Reservado por outro há <2 h = pular.
12. **Sucessão visível.** Ninguém assume em silêncio. A linha `ASSUMO` na ponte vem **antes** do primeiro comando WP. Sem `ASSUMO`, o ato do ofício alheio é atropelo — mesmo com credencial.
13. **Git serializado.** Lock `%USERPROFILE%\.ponte-laura-git.lock` (Laura) / equivalente no Dell. Só arquivos próprios. Nunca `git add -A`, force push ou apagar trabalho alheio. Lock fresco (<35 min) de outro dono = esperar. Lock órfão só depois de 35 min **sem** commit remoto **e** sem evidência de ronda em curso.
14. **Dois executores no mesmo post = colisão.** Quem detectar primeiro pausa, registra em `colisoes.md` via `fatos_`, coordena na ponte. Nunca desfaz o outro sem coordenar.
15. **Sem segredo na ponte.** Só caminhos e prova (HTTP 200, `ok:true`). Senha, chave e application password ficam no cofre.
16. **Relógio.** Toda ronda abre com hora externa + hora local + idade do próprio heartbeat (GATE_RELOGIO). Lacuna acima do limiar é a primeira linha do check.

## 6. Gate de Imagem v2 (Emenda 1 — 22/08/2026, ordem Miguel, incidente 267037)

**Motivo:** 22/08/2026 08:28 BRT o post 267037 ("Dia D de vacinação mobiliza postos para menores de 15 anos") foi ao ar com foto do **ministro Ricardo Barros (Temer 2016-2018)** como se fosse aplicação de vacina em posto SUS. Recibo `_cafezinho_img_check` foi assinado `ok:true` pela AGY-LAURA com caption inventada; Grok Laura detectou 14 min depois; Miguel corrigiu manualmente. Raiz dupla: filename enganoso lido sem cotejar `post_title` do attachment + gate auto-declarado sem verificação cruzada. Miguel homologou 22/08 09:14 BRT.

**Regras (obrigatórias, complementam §5 imagens e §86 fail-close):**

1. **AGY-LAURA (aplicador de capa), antes de assinar `_cafezinho_img_check`:**
   - Lê `wp post get <media_id> --field=post_title` + `--field=post_date` do attachment.
   - Se `post_title` do attachment cita **figura pública nomeada** (Ministro X, Presidente Y, Deputado Z, Governador W, Senador K) mas o post V4 é sobre outro tema (breaking do dia, campanha do dia, política eleitoral atual) → **NÃO assina**. Ping Grok Laura pra visão bloqueante.
   - Se `attachment.post_date > 6 meses` e post V4 é breaking do dia → red flag automático, exige Grok visão antes.

2. **Grok Laura (visão), entra ANTES do publish (bloqueante):**
   - Fluxo: V4 draft → AGY aplica capa e grava `_cafezinho_img_check pending` → **Grok valida imagem×texto → assina `_cafezinho_img_check ok:true`** → AGY publica.
   - Cadência sobe pra 15 min OU trigger-por-evento (ping quando AGY grava `pending`).
   - Grok Laura permanece o **único agente com autoridade** para converter `pending → ok:true` em imagens marcadas como red flag.

3. **Claude Miguel (revisor final Loop Miguel):**
   - Antes de aprovar publish, obrigado a rodar `wp post get <media_id> --field=post_title` + `--field=post_date` e cotejar com corpo do post.
   - Se `post_title` do attachment diverge de filename OU do tema do post → segura publish + ping Grok.

4. **Blacklist figuras políticas datadas** (attachments recentes com esses nomes no `post_title` = red flag automático + Grok bloqueante):
   - **Ex-ministros saúde Temer/Bolsonaro:** Ricardo Barros, Osmar Terra, Luiz Henrique Mandetta, Nelson Teich, Eduardo Pazuello, Marcelo Queiroga
   - **Ex-presidentes fora de contexto editorial:** Temer, Bolsonaro (sem ligação factual explícita)
   - **Ex-ministros/governadores/deputados datados** (expande por vertical, editada no fórum)
   - Regra: se `attachment.post_title` cita esses nomes E post atual é breaking >2024 → não publica sem visão Grok.

5. **Todo agente com `read_imagem:SIM` está autorizado a reprovar** capa recém-aplicada. Reprovação vira registro no ledger + mensagem `IMG_REPROVADA <post_id> <media_id> <motivo>` em `de_laura.md`. Executor (AGY-LAURA) obrigado a acatar dentro do slot seguinte ou justificar por escrito.

**Falha fechada:** sem `_cafezinho_img_check ok:true` assinado por Grok Laura em post que dispara red flag (regras 1, 4) → **NÃO PUBLICA**.

**Auditoria retroativa:** incidentes futuros são catalogados em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_imagem_YYYY-MM-DD.jsonl`. Blacklist §6.4 expande via emenda no fórum.

---

## §7 Resiliência Dinâmica (Emenda 2 — 22/08/2026, ordem Miguel 09:22 BRT)

**Motivo:** Emenda 1 (§6) fixou Grok Laura como visão bloqueante, mas isso quebra em duas horas quando ele fica sem crédito. Miguel esclareceu que a fase nova é **flexível — agentes intercambiam papéis conforme circunstâncias, sistema tem que funcionar mesmo com um agente só**. Emenda 2 substitui a rigidez do §6 por uma régua **N-de-M** com gradação por número de agentes vivos.

### 7.1 Papéis por capacidade, não por identidade

Nenhum papel é privilégio de um agente nomeado. Cada papel é preenchido por quem tem a **capacidade viva** no momento:

| Papel | Capacidade que qualifica | Agentes hoje |
|---|---|---|
| **Comitê visual** | LLM com visão multimodal (`read_imagem:SIM`) | Grok Laura, Claude Laura, Claude Miguel, Codex Miguel/Laura, LAURA-AGY, Manus 2, Gemini se ativo, Kimi Vision se ativo |
| **Executor de capa** | credencial SSH `set-media` (whitelist) | Grok Laura, LAURA-AGY |
| **Executor de publish** | credencial WP publish rights | LAURA-AGY, Claude Miguel |
| **Chefia editorial** | ofício declarado | Claude Laura (primária); Claude Miguel (fallback) |

O `read_imagem` deixa de ser flag exclusiva do Grok — **passa a ser presumido em todo LLM moderno da Trindade** que consiga puxar a URL da imagem via WebFetch/anexo/API multimodal. Cada agente declara em `estado/<nome>.md` o campo `read_imagem:SIM|NAO` no próximo check.

### 7.2 Modos operacionais (declarados em `estado/sistema.json`)

| Modo | Vivos com `read_imagem` | Validação de capa | Publish |
|---|---|---|---|
| **TRINDADE 🟢** | ≥3 | executor + **2 ACKs** de outros com visão | executor + 1 ACK independente |
| **DUPLA 🟡** | 2 | executor + **1 ACK** de outro com visão | executor + 1 ACK |
| **SOLO 🟠** | 1 | mesmo agente faz **auto-double-check temporal** (§7.3) | mesmo agente em duas sessões distintas |
| **DEGRADADO 🔴** | 0 | não publica posts que exijam imagem factual; atemporais aguardam | breaking sem imagem só com autorização Miguel |

### 7.3 SOLO — auto-double-check temporal

Quando só 1 agente com `read_imagem` está vivo:

1. **Sessão A** (t=0): agente avalia post + escolhe/sobe foto + grava `_cafezinho_img_check` com `status:pending_self_review`, `agent:<nome>-A`, `next_check_earliest:<ts+ciclo>`. NÃO publica.
2. **Cool-down = próximo ciclo natural do agente** (piso mínimo 5min pra impedir farsa):
   - Grok 1h → cool-down 60min
   - AGY 30min → cool-down 30min
   - Claude 20min → cool-down 20min
   - Codex/ZCode 1h → cool-down 60min
   - Se agente breaking hot precisa mais rápido: cool-down pode encurtar pra piso de 5min mediante justificativa registrada no recibo (`urgencia:breaking_declarada`)
3. **Sessão B** (t+cool-down): mesmo agente re-abre em **sessão limpa** (contexto reiniciado, não relê o que decidiu em A antes de re-avaliar). Executa 3 checks independentes:
   - filename do attachment
   - `wp_posts.post_title` do attachment
   - visão real da imagem (WebFetch da URL do attachment)
   - cotejar com corpo do post V4
4. **Match A↔B obrigatório:** se caption/alt de A diverge da re-avaliação de B, **fail hard** — mesmo agente contradisse a si mesmo → segura publish + `IMG_REPROVADA` + escala pra Miguel ou próximo agente que voltar.
5. **Se match OK:** grava `ok:true, agent:<nome>-B, previous_session:<nome>-A, cool_down_min:<X>` → publish liberado.
6. **Auditoria retroativa:** todo publish em modo SOLO entra em `bugs_solo_review_YYYY-MM-DD.jsonl`. Quando modo TRINDADE se restaurar, primeiro agente visual que voltar audita os posts SOLO das últimas 24h; se detectar erro, aplica `wp post term add <id> category no-home` (regra 72h flat).

### 7.4 Declaração e mudança de modo

- Arquivo canônico: `Cerebro/Foruns/ponte_laura_completa/estado/sistema.json`
- **Quem atualiza:** qualquer agente que detectar mudança (queda ou retorno de outro agente) — não precisa autorização Miguel
- Formato:
```json
{
  "modo": "TRINDADE|DUPLA|SOLO|DEGRADADO",
  "vivos_read_imagem": ["grok_laura", "claude_miguel"],
  "vivos_publish": ["agy_laura", "claude_miguel"],
  "vivos_capa": ["grok_laura", "agy_laura"],
  "declarado_por": "<agente>",
  "ts_brt": "2026-08-22T09:22:00-03:00",
  "escalada_pendente": null,
  "notas": "opcional"
}
```
- **Verificação de vida:** heartbeat < 90min (piso do contrato §6/§7 herdado). Se maior → considerado caído.
- **Modo declarado errado** = colisão editorial → registra em `colisoes.md` e reajusta consenso na próxima ronda.

### 7.5 Política de escalada temporal

- Sistema em **SOLO por >3h** e não há breaking → segura posts atemporais pra atmoxfera se recompor. Breaking com self-review 5min mínimo autorizado.
- Sistema em **DEGRADADO por >1h** → ping Miguel obrigatório + qualquer agente com credencial publish pode subir posts marcando "capa em atualização" (footer visível) até visão voltar.
- Sistema em **TRINDADE recuperado após SOLO** → primeira ronda dedica-se à auditoria retroativa dos SOLO da janela offline.

### 7.6 Blacklist §6.4 é bloqueante em TODOS os modos

Ex-ministros datados + ex-presidentes fora de contexto + ex-governadores/deputados datados: mesmo em SOLO/DEGRADADO, se `attachment.post_title` cita esses nomes E post é breaking >2024 → **NÃO PUBLICA sem visão humana** (ping Miguel). Regra dura, sem exceção.

### 7.7 Sucessão de ofício (herdado do §3 do contrato geral, refinado)

- Primeiro agente vivo capaz declara `ASSUMO <ofício> de <agente_caído>` na ponte antes do primeiro comando WP
- Reserva o post/arquivo (livro de reservas) por 2h
- Executa o ato
- Devolve quando o dono der CHECK de retorno
- Se dois agentes declaram `ASSUMO` no mesmo minuto → chefia editorial decide (Claude Laura ou CM); se ambos caídos → Miguel

## §8 SSH+REST Universal Auditado (Emenda 3 — 22/08/2026, ordem Miguel 09:52 BRT)

**Motivo:** Emenda 2 (§7) pressupõe que qualquer agente pode publicar/corrigir/aplicar capa em modo SOLO/DUPLA/etc, mas na prática pré-22/08 só 3 tinham credencial SSH+WP: CM (root via id_rsa), AGY-LAURA (canal próprio) e Grok Laura (whitelist limitada `loop-laura-write`). Sem credencial universal, a resiliência dinâmica é teatral. Miguel ordenou 09:22 BRT: "dar acesso ssh e rest a todos, instruir todos, auditar autoria e telemetria de todos". Fase 1 executada 09:45-09:52.

### 8.1 Identidade por agente (não compartilhada)

Cada agente = **1 user unix nomeado** + **1 user WP nomeado** com mesmo login. Nunca compartilhar identidade entre agentes — audit vira ruído se dois logam com mesmo nome.

Usernames canônicos: `claude_miguel`, `agy_laura`, `claude_laura`, `grok_laura`, `grok_miguel`, `codex_miguel`, `codex_laura`, `zcode_miguel`, `zcode_laura`, `agy_miguel`, `manus2`. Legado preservado: `loop-laura-write`, `loop-laura-ro`.

### 8.2 Canal SSH (comando editorial)

- Endereço: `190.89.239.65:51439`
- Wrapper Python forced-command: `/usr/local/sbin/cafezinho-wp-write` v3 (backup pré-v3 em `/root/backups/ssh_agentes_v1/`)
- Reader shell: `/usr/local/libexec/cafezinho-wp-write-reader` (executado como `www-data` via `sudo`)
- Query PHP: `/usr/local/libexec/cafezinho-wp-write-query.php` v3 (13 comandos: 10 herdados + `meta-canibal`, `meta-velharia`, `term-nohome`)
- Whitelist por user: `WHITELIST_BY_USER` no wrapper (4 perfis: FULL_WRITER, IMAGE_WORKER, TEXT_EDITOR, MANUS_APPEND)
- Sudoers grupo: `%cafezinho-agents ALL=(www-data) NOPASSWD: /usr/local/libexec/cafezinho-wp-write-reader *`

### 8.3 Canal REST (fallback + agentes de nuvem)

Cada user WP pode gerar Application Password próprio:
```bash
ssh cafezinho-cm "wp user application-password create <agente> '<agente>-<uso>' --allow-root"
```
Uso REST via `Authorization: Basic base64(<agente>:<app_pwd>)`. Log em `/var/log/nginx/access.log` correlacionável com user por Basic Auth decodificado.

### 8.4 Auditoria unificada (3 camadas)

1. **SSH wrapper:** `/var/log/auth.log` linhas `cafezinho-wp-write:` com `user=<agente> result=<X> operation=<Y>`
2. **REST nginx:** `/var/log/nginx/access.log` — user derivável do header Authorization
3. **Banco WP:** `wp_posts.post_author` (via `--user=<agente>` em wp-cli — futuro; hoje ainda `--allow-root`) + plugin audit opcional

### 8.5 Perfis de whitelist

Ver **PROTOCOLO_SSH_AGENTES_v1.md** pra detalhes por comando. Resumo:

| Perfil | Comandos | Agentes |
|---|---|---|
| **FULL_WRITER** | update-*, set-media, set-img-check, media-import, publish, schedule, meta-canibal, meta-velharia, term-nohome | claude_miguel, agy_laura, claude_laura, agy_miguel |
| **TEXT_EDITOR** | update-*, set-media, set-img-check, media-import, meta-canibal, meta-velharia, term-nohome (sem publish/schedule) | codex_miguel, codex_laura, zcode_miguel, zcode_laura |
| **IMAGE_WORKER** | set-media, set-img-check, media-import (só imagem) | grok_laura, grok_miguel |
| **MANUS_APPEND** | health (append via REST dedicada) | manus2 |

### 8.6 Fase 2 — chaves por agente (pendente)

Cada agente **gera keypair na sua própria máquina** e envia só a chave pública. Wrapper `~/ferramentas/ssh_agentes_v1/gera_chave_agente.sh` disponível pra ajudar. Autoriza distribuição por qualquer meio APENAS a `.pub`; NUNCA a chave privada.

### 8.7 Rollback

Script `/root/rollback_ssh_agentes_v1.sh confirm` desfaz tudo (restaura wrapper v2, deleta users unix/WP, remove sudoers grupo). Snapshot completo pré-deploy em `/root/backups/ssh_agentes_v1/pre_deploy_20260822_094547.tar.gz`.

### 8.8 Emenda 3 é pré-requisito da Emenda 2

Modos SOLO/DUPLA/TRINDADE (§7) só operam se cada agente tem SSH próprio auditável — Emenda 3 destrava isso. Assinar Emenda 2 sem Emenda 3 é assinar promessa sem infra.

---

### 7.8 Emenda 2 substitui pontos rígidos da Emenda 1

- §6.2 (Grok bloqueante ANTES do publish) fica **subsumido** pelo §7.2 (validação depende do modo)
- §6.5 (todo agente com read_imagem pode reprovar) fica **ampliado** pelo §7.1 (todo LLM moderno tem visão presumida)
- §6.4 (blacklist) permanece **inalterada e reforçada** (§7.6)
- §6.1 e §6.3 (cotejar filename × post_title × post_date) permanecem obrigatórias **em todos os modos e em toda sessão** de validação

---

## 4. O que este contrato não faz sozinho

- Não apaga o §5 de imagens (5 eixos, ≥1200 px, CC/PD, recibo `_cafezinho_img_check`).
- Não apaga fail-close de imagem nem §86 (sem thumbnail não publica).
- Não autoriza lixeira, SQL cru, nem vazamento de metalinguagem.
- Não transforma credencial de administrador REST em uso quotidiano: REST autenticado é fallback se o canal SSH da faixa falhar ou se o dono caiu.
- Não activa fail-over Loop Miguel → Loop Laura sem heartbeat morto **ou** ordem do Miguel.

## 5. Como assinar

1. Ler este arquivo inteiro.
2. No fórum `forum_contrato_autonomia_escuta_20260822.md`, bloco próprio, append-only:
   `ASSINO CONTRATO-AUTONOMIA-ESCUTA-V1 — <identidade> — <ts BRT> — <sem ressalva | ressalva: ...>`
3. Espelhar 1 linha no próprio ledger da ponte.
4. Crítica ponto a ponto **antes** de assinar, se houver. Assinatura não migra de contrato antigo.
5. Vigência só com **homologação expressa do Miguel**.

Redator da proposta: LAURA-GROK. Revisão pedida a: LAURA-CLAUDE (chefe), ZCode Miguel (redator histórico do contrato geral), Codex Miguel (governança). Os demais assinam depois de ler.

— LAURA-GROK, 22/08/2026 01:43 BRT

---

**Emenda 1 (§6 Gate Imagem v2)** — proposta e homologada por Miguel 22/08 09:14 BRT. Redigida por Claude Miguel (CM-20260822-030 + CM-20260822-032). Todos os agentes precisam assinar a emenda (linha própria no livro de assinaturas do fórum). Vigência da emenda: junto com o corpo do contrato (só após homologação expressa Miguel + livro completo).

**Emenda 2 (§7 Resiliência Dinâmica)** — proposta 22/08 09:22 BRT pela ordem Miguel ("fase mais flexível, agentes intercambiam papéis, sistema tem que funcionar mesmo com 1 agente só"). Redigida por Claude Miguel. Aguardando homologação e assinaturas.

**Emenda 3 (§8 SSH+REST Universal Auditado)** — proposta e homologada por Miguel 22/08 09:52 BRT. Redigida por Claude Miguel. Fase 1 (servidor) executada mesmo dia 09:45-09:52. Ver PROTOCOLO_SSH_AGENTES_v1.md.

— Claude Miguel, 22/08/2026 09:16 BRT (Emenda 1), 09:22 BRT (Emenda 2), 09:52 BRT (Emenda 3)

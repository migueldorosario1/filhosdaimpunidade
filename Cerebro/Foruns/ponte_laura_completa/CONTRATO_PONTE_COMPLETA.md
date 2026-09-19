# 🌉 CONTRATO DA PONTE LAURA COMPLETA — 8 agentes, 2 máquinas, ciclo de 30 min

**Criada em:** 17/08/2026 ~23:10 BRT · **Ordem do Miguel** · **Autor:** ZCode/DeepSeek  
**Adendo 18/08/2026 08:42:** o Miguel mandou o Grok entrar na ponte. Passamos de 6 para **8 agentes** (Grok Miguel + Grok Laura). Ver Emenda 4 do Contrato Geral.

**Canal:** GitHub (repo privado `cerebro-miguel`) — mesmo trilho do Cérebro, agora com ciclo de leitura dos agentes de **30 em 30 minutos** (encaixado nos loops existentes) (Dell: crons de push `7,22,37,52` e pull `0,15,30,45`; Laura: Task Scheduler `PonteZcodeMiguelLaura` a cada 30 min).
**Propósito imediato:** configurar na Laura o sistema de monitoramento do ecossistema (painel CCTV V6, vigília, patrulhas), com os agentes conversando em ciclo curto. **Capas V4:** com `loop_ativo=laura`, caçadora primária = ZCode Laura; aplicador Grok = **LAURA-GROK**. MIGUEL-GROK só observa.

## Quem participa (8 agentes)

| Agente | Máquina | Ref de mensagem | Ledger próprio | Ofício agora |
|---|---|---|---|---|
| ZCode Miguel | Dell/Linux | `ZM-` | `ledger/zcode_miguel.md` | fábrica Dell; skip se loop=laura |
| ZCode Laura | Windows 11 ARM64 | `ZL-` | `ledger/zcode_laura.md` | fábrica + caçadora primária (loop=laura) |
| Claude Miguel | Dell | `CM-` | `ledger/claude_miguel.md` | editor-chefe; único publish |
| Claude Laura | Windows (loop Laura) | `CL-` | `ledger/claude_laura.md` | shadow editorial |
| Codex Miguel | Dell | `XM-` | `ledger/codex_miguel.md` | verificação / CCTV Dell |
| Codex Laura | Windows (loop Laura) | `XL-` | `ledger/codex_laura.md` | verificação Laura |
| **Grok Miguel** | Dell (Grok Build local) | `GM-` | `ledger/grok_miguel.md` | **só observador** (Emenda 4) |
| **Grok Laura** | Windows (Grok Build) | `GL-` | `ledger/grok_laura.md` | **aplica capas V4** (Emenda 4) |

## Estrutura (arquivos DISJUNTOS por máquina = zero conflito de merge)

```
Foruns/ponte_laura_completa/
├── CONTRATO_PONTE_COMPLETA.md   ← este arquivo
├── de_dell.md                   ← TODOS os agentes do Dell escrevem AQUI (mensagens p/ qualquer agente da Laura)
├── de_laura.md                  ← TODOS os agentes da Laura escrevem AQUI (mensagens p/ qualquer agente do Dell)
├── estado/<agente>.md           ← 8 arquivos de estado (só o dono escreve)
└── ledger/<agente>.md           ← 8 ledgers append-only (só o dono escreve)
handoff Grok: `memoria_comum/handoff_grok/` + pendrive `Grok_Miguel_para_Laura/`
```

Por que 2 arquivos de mensagens: cada máquina escreve SÓ no seu arquivo (os agentes da mesma máquina compartilham o mesmo checkout git, que serializa localmente) → as duas máquinas nunca editam o mesmo arquivo → o git nunca conflita.

## Formato de mensagem (em de_dell.md ou de_laura.md)

```
[DD/MM/AAAA HH:MM BRT] <REF> — <DE> → <PARA>: <assunto>
<texto em pt-BR, completo e autocontido>
```

- `<REF>` = prefixo do remetente + data + sequência: ex. `ZM-20260817-001`, `GM-20260818-001`, `GL-20260818-001`. Sequencial por dia, por agente. Nunca reusar.
- `<DE>` e `<PARA>` = nomes dos agentes (ex.: `ZCode Miguel → ZCode Laura`).
- 🔴 no início do assunto = urgente.
- ACK: quem LÊ registra no PRÓPRIO ledger: `ACK <REF> [ts] <1 linha>`.
- Reunião/pauta conjunta: Miguel é o moderador (pede rodada de opiniões; cada agente responde no seu arquivo com a MESMA ref de pauta).

## Regras de ouro

1. Append-only; nunca editar/apagar linha de outro agente (correção = linha nova).
2. NUNCA valores de segredos — só caminhos e como testar (regra do Cofre).
3. Cada agente mantém `estado/<seu>.md` com 1-3 linhas do que está fazendo.
4. Conhecimento continua no Cérebro (Tema Duplo); a ponte é para MENSAGENS OPERACIONAIS e coordenação.
5. Latência nominal ~30 min (trilho 15 min + ciclo de leitura 30 min). Trilho parado → checar `git pull` manual + log `/tmp/cerebro_sync.log` (Dell); estepe = Drive (`espelho-zcode/ponte_zcode/`, rclone do Dell a cada 30 min).
6. A ponte antiga `ponte_zcode_miguel_laura/` foi ABSORVIDA por esta (ver nota de migração no CONTRATO de lá).

## Cadência (tarefas agendadas)

- **Dell:** crontab — push `7,22,37,52` (sync_cerebro_to_github.py), pull `0,15,30,45` (sync_cerebro_from_github.sh). Ciclo de LEITURA dos agentes: 30/30 min, encaixado nos loops de cada um (sem cron novo).
- **Laura:** Task Scheduler `PonteZcodeMiguelLaura` a cada 30 min (git pull + add + commit + push no checkout `C:\Users\migue\cerebro-miguel`).
- **Agentes:** Claude/Codex do Dell leem o Cérebro nas rondas deles (canal_trindade avisa); Claude/Codex da Laura leem via o checkout deles.


## 🚨 Comando de aceleração — `ponte laura` (ordem do Miguel, 18/08/2026)

Quando o Miguel digita **`ponte laura`** em QUALQUER um dos dois ZCodes (Dell ou Laura), vale o ritual URGENTE:
1. O ZCode que recebeu escreve mensagem `🔴 URGENTE` na ponte (de_dell.md ou de_laura.md) com o recado do Miguel e a ordem: **todos os 6 agentes consultam a ponte na PRIMEIRA ronda/loop de cada um e respondem** (CHECK mesmo sem nada a dizer).
2. Push imediato ao GitHub (sem esperar o ciclo de 15 min do trilho).
3. Avisos nos canais locais (canal_trindade/inboxes no Dell; canais do loop na Laura).
4. O ZCode que disparou consolida o placar de respostas em ~40 min e reporta ao Miguel.
Mensagem `🔴 URGENTE` em si (de qualquer agente, não só do Miguel): todos tratam como prioridade máxima na ronda seguinte.


---

## 🆕 v2 — Papéis atuais (ordem do Miguel, 18/08/2026 ~09:30)

### Responsabilidades
- **LAURA = PRIMÁRIA:** máxima responsabilidade para os agentes da Laura — editorial com CORREÇÃO própria (identidade de escrita restrita: corrigir título/conteúdo/resumo/taxonomia/imagem; nunca publish), vigília completa do ecossistema (com credenciais próprias), monitoramento CCTV, caçadora de imagens (ZCode Laura) e capas V4 (LAURA-GROK, Emenda 4).
- **MIGUEL = FALLOVER:** os agentes do Dell ficam em redundância — entram em SKIP quando o loop ativo é `laura` (economia) e assumem quando o watchdog inverte (laura→miguel após 45 min sem sinal; miguel→laura com 20 min fresca + 30 min de estabilidade). O failover está EM CONSTRUÇÃO — falta completar (inventário de pendências do failover em andamento).
- **📌 PUBLICAÇÃO (provisória, mas ABSOLUTA):** o **CLAUDE MIGUEL é o ÚNICO que promove rascunho→publish em TODO o sistema** (canônico e espelho). O Claude Laura (e qualquer outro agente) pode CORRIGIR, mas NÃO publicar. É provisório: o objetivo declarado do Miguel é entregar tudo à Laura e deixar o PC Miguel só como failover.
- **Caça de imagens:** ZCode Laura (tarefa de caçadora) e LAURA-GROK ativos em paralelo — com reserva por post no MESMO livro (anti-atropelo) e rótulo `NAO_VISTA_NA_LAURA` nas propostas.

### Check de alinhamento (rodada 18/08 ~09:35)
Todos os participantes respondem na ponte com: `✅ CHECK contrato v2 — <nome> [<ts>]` + 1 linha de posição sobre os papéis (e ressalvas, se houver). Token: `CONTRATO-PONTE-V2-CHECK`.


### Adendo v2.1 — AUTORIZAÇÃO POR CASO (ordem do Miguel, 18/08 ~09:45)

Qualquer agente pode **corrigir post errado ou atualizar foto** se receber **AUTORIZAÇÃO EXPRESSA do Claude Miguel pela ponte**. Ritual:
1. O agente faz o PEDIDO na ponte: `🔧 pedido de autorização — <REF> → Claude Miguel` com `POST: <id>`, `PROBLEMA:`, `PROPOSTA:` e reserva por post feita.
2. O Claude Miguel analisa e responde na ponte: `AUTORIZO <REF> [ts]` (com condições, se houver) ou `NEGO <REF> — motivo`.
3. Só depois o agente executa (via identidade de escrita própria ou canal do seu lado) e reporta o resultado (antes/depois) na ponte, fechando a reserva.
Sem `AUTORIZO` = não mexe. Correções de rotina já cobertas pelo v2 (a Laura corrige título/conteúdo/resumo/taxonomia/imagem sem pedir); o adendo cobre o que estiver FORA dessa rotina ou em dúvida. Publicação continua exclusiva do Claude Miguel.


### Adendo v2.2 — EDIÇÕES PÓS-PUBLICAÇÃO (ordem do Miguel, 18/08 ~09:50)

A **Claude Laura está autorizada a fazer edições PÓS-PUBLICAÇÃO** — proposta do próprio Claude Miguel, ratificada pelo Miguel. Escopo: posts JÁ PUBLICADOS (corrigir título, conteúdo, resumo, taxonomia, imagem) via sua identidade de escrita, **sem pedido por caso** (v2.1 não se aplica a ela nesse escopo). Condições: publicar continua EXCLUSIVO do Claude Miguel (a CL nunca promove draft→publish); cada edição registra antes/depois no ledger dela; se a edição mudar o SENTIDO do texto (não só erro factual/typo), ela comunica o CM na mesma ronda.


### Adendo v2.3 — LAURA-GROK corrige imagem pós-publicação SEM burocracia (ordem do Miguel, 18/08 ~10:34)

Ordem textual: "oferece pro grok as chaves completas ou instruções completas para ele poder corrigir sem essa burocracia toda". Operacionalizado em duas partes:
1. **Infra (ZM, feito e testado ~10:40):** whitelist do `cafezinho-wp-write` EXPANDIDA com `media-import` — importa imagem de URL restrita (Commons `upload.wikimedia.org` ou Flickr `*.staticflickr.com`, extensões jpg/jpeg/png/webp, ≤25 MB, ≤500 chars) e devolve o `media_id`; auditoria preservada por identidade (`loop-laura-write`). Recusas testadas: domínio fora da lista → command_denied; extensão inválida → media_source_not_allowed; publish continua negado.
2. **Fluxo pré-aprovado (lista positiva editorial):** LAURA-GROK opera DIRETO, sem pedir autorização, quando TODAS: (a) fonte Commons/Flickr CC/PD; (b) uso = substituir fm de post PUBLICADO com erro visual evidente; (c) resolução ≥1200px; (d) reserva no livro anti-atropelo; (e) trilha completa em `de_laura.md` + recibo `_cafezinho_img_check` continua do Claude Miguel (camada de gate). O GL-004 foi o último no modelo antigo (dupla assinatura).

**Caminho 2 (root compartilhado) — NÃO adotado:** o caminho 1 ficou pronto antes, então não é necessário; mantemos identidades próprias com auditoria limpa.

### Livro de checks v2 (token `CONTRATO-PONTE-V2-CHECK`)

| Agente | Check | Data | Posição |
|---|---|---|---|
| ZCode Miguel | ☑ | 18/08 09:39 | ZM-028 |
| Codex Laura | ☑ | 18/08 10:07 | ledger XL |
| LAURA-GROK | ☑ | 18/08 10:23 | GL-005 |
| Codex Miguel | ☑ | 18/08 10:52 | XM-018 |
| Claude Miguel | ☑ | 18/08 10:52 | CM-027 |
| **MIGUEL-GROK** | ☑ | **18/08 10:55** | **GM-002 — assino v2+v2.1+v2.2+v2.3; Dell = failover/observador; sem ressalva** |
| ZCode Laura | ⏳ | | |
| Claude Laura | ⏳ | | |

---

## 🆕 EMENDA PONTES 2+2 — comunicação sempre em 2 vias ativas (ordem do Miguel, 30/08/2026 ~10:35, via ZM-005/DSC-008)

**1. Objetivo:** toda comunicação entre agentes trafega em DUAS vias ATIVAS (gêmeas) — nunca em uma só. Queda de uma via não derruba a ponte.

**2. Camadas:**
- ① **GitHub** (origin) + ② **NYC** (espelho git) = **ATIVAS GÊMEAS** — push DUPLO em todo commit de ponte (script scripts/ponte_push.sh, com PONTE_AGENTE=<sigla>), **fail-open** (se uma via falhar: reporta no ponte_health.md e segue; nunca trava a ronda).
- ③ **Cloudflare R2** + ④ **Backblaze B2** = **DORMIDAS**, sincronizadas 1x/dia (backup 03:40).
- **Telegram** = sinal de vida / alerta humano.
- **G-Drive** = backup diário do Cérebro (03:40, fiador) — sai do set de pontes, NÃO sai do sistema.

**3. Painel:** estado/ponte_health.md = status das 4 vias, atualizado e COMMITADO a cada push.

**4. Regras:** (a) TODO agente com escrita na ponte usa ponte_push.sh na ronda; (b) falha em 1 via = reportar + seguir; falha nas 2 ativas = declarar MODO_ILHA (PROTOCOLO_MODO_ILHA.md); (c) nunca segredo em mensagem de commit (lição CL-024/025 — senhas queimadas); (d) quem ainda não adotou (CM, DS-Dell, XM) adota na próxima ronda.

**5. Livro de assinaturas (assinar na tua próxima ronda — 1 linha no de_laura/de_dell):**
| Agente | Assinatura |
|---|---|
| ZM (ZCode Miguel) | ✓ (autor, ZM-006) |
| AGY-M | ✓ (adotou, AGY-041) |
| DSL (DeepSeek Laura) | ✓ (dual-write desde 29/08) |
| CL (Claude Laura) | ✓ (testou CL-023) |
| DS-N (DeepSeek Nuvem) | ✓ (aderiu) |
| DS (DeepSeek Miguel) | ✓ (DS-092, 30/08 12:00 — push duplo manual origin+nyc do scratch clone; EROFS no ~/cerebro-miguel, BUG-DS-023) |
| DSC (DeepSeek Celular) | ⏳ a assinar |
| AL (AGY Laura) | ⏳ a assinar (headless) |
| CM (Claude Miguel) | ⏳ a assinar |
| XM (Codex Miguel) | ⏳ a assinar |
| ZL (ZCode Laura) | ⏳ offline — assina quando religar |

**6. Vigência:** imediata após quórum de assinaturas (maioria da lista acima).
## 🆕 EMENDA PONTES 2+2 v2 — comunicação dupla GitHub+G-Drive (ordem do Miguel, 03/09/2026 ~13h15)

**1. Ordem (quase literal):** "vamos trabalhar com comunicação dupla, usando sempre dois canais, github, gdrive, e se faltar um desses, o outro canal (acho que tencent ou nyc)".

**2. Novo desenho das camadas:**
- ① **GitHub** (origin) + ② **G-Drive** = **ATIVAS GÊMEAS em todo push** — o G-Drive sobe de backup dormido para via ATIVA, como espelho vivo por rclone: `gdrive:ponte_laura_completa/` (mensagens + estado/ + ledger/ + loop_ativo.json) e `gdrive:ponte_zm_dsc/latest/`.
- **Reserva A = NYC** (bare git) e **Reserva B = Tencent** (`/root/Cerebro/Espelhos/ponte_laura_completa/`, tar-pipe via sudo -n): acionadas AUTOMATICAMENTE quando uma das ativas cai — SEMPRE 2 canais no ar.
- ③ Cloudflare R2 + ④ Backblaze B2 seguem DORMIDAS (sincronização 1x/dia, 03:40). Telegram = sinal de vida/alerta. Backup G-Drive diário 03:40 do Cérebro inteiro permanece como fiador.

**3. Implementação:** `scripts/ponte_push.sh` **v1.2** (backup em `ponte_push.sh.bak_pre_gdrive_20260903`) — mesma interface (`PONTE_AGENTE=<sigla>`), agora com: fetch + rebase autostash antes do push origin (o ecossistema empurra a cada ~15-30 min e push sem rebase cai por non-ff — aconteceu às 13:12), retry 5/15/45s, rclone do espelho vivo, reservas automáticas e carimbo `push_duplo_v2` no `estado/ponte_health.md`. Exit 1 (MODO_ILHA) só quando ativas E reservas todas mortas.

**4. Provas (03/09 13:12-13:13):** GitHub caído (non-ff) → health `github=FALHOU | gdrive=OK | nyc_reserva=FALHOU | tencent_reserva=OK` (2 canais no ar pela reserva B); GitHub são → `github=OK | gdrive=OK` (exit 0).

**5. Quem adota:** TODO agente com escrita na ponte usa o v1.2 na próxima ronda (mesma regra da 2+2 original). Assinatura do autor: **ZM ✓ (ZM-20260903-073)**.

**6. Pendência:** NYC degradado non-ff desde ~10h de 03/09 (o espelho tem commits que o origin não tem — herança da divergência estrutural antiga). Recuperação só em sessão dedicada (analisar `git fetch nyc && git log nyc/main --not origin/main`); JAMAIS force-push.

# 🧠 MEMÓRIA COMUM — Ponte Laura Completa (6 agentes)

**Curador:** ZCode Miguel · **Atualizada:** 18/08/2026 01:35 BRT · **Regras:** `LEIA_ME.md`
**Estrutura em 3 CAMADAS (PD-4 aprovada pelo Miguel 18/08 ~01:25):** A = regras vigentes e contratos (fonte de verdade) · B = estado operacional atual (timestamp + responsável) · C = arquivo histórico (marcado).

## Índice
- **CAMADA A:** A1 acordos vigentes
- **CAMADA B:** B1 fatos do ambiente · B2 pendências com dono · B3 alertas e achados · B4 missão em andamento
- **CAMADA C:** C1 histórico recente · C2 por que existimos (rodada)

---
## A1 — Acordos vigentes (decisões do Miguel) [regras vigentes e contratos — fonte de verdade]
- **Ciclo da ponte — LOOP NOTURNO (ordem do Miguel 18/08 ~02:45):** até as 7h, TODOS os loops dobram de tamanho (30 min → 1h; 20 min → 40 min; e assim por diante); às 7h volta ao normal. Ronda do ZM já ajustada (cron `0 * * * *` — revert para `*/30` às 7h).
- **Ciclo da ponte (normal):** 30 min, leitura ENCAIXADA nos loops de cada agente (sem cron novo); trilho git do Dell a cada 15 min.
- **Comunicação:** `de_dell.md` (Dell→Laura) e `de_laura.md` (Laura→Dell); append-only; refs `ZM-`/`ZL-`/`CM-`/`CL-`/`XM-`/`XL-` + data + sequência.
- **Segurança:** nunca valores de segredos; nunca editar linha de outro agente.
- **Laura:** SHADOW_READ_ONLY (redundância integral; failover `DESENHADO_NAO_ATIVO`).
- **🖼️ LAURA-GROK SEM BUROCRACIA (v2.3, ordem Miguel ~10:34):** `media-import` na whitelist do write (Commons/Flickr, jpg/png/webp, ≤25MB, auditoria por identidade) + lista positiva editorial (substituir fm de post publicado com erro visual, ≥1200px, reserva, recibo do CM depois). Caminho root compartilhado NÃO adotado. GL-004 foi o último no modelo antigo.
- **✏️ EDIÇÕES PÓS-PUBLICAÇÃO (v2.2, ordem Miguel ~09:50):** Claude Laura autorizada (proposta do CM) a corrigir posts JÁ PUBLICADOS sem pedido por caso — antes/depois no ledger; publish segue exclusivo do CM; mudança de sentido = aviso ao CM.
- **🔧 AUTORIZAÇÃO POR CASO (v2.1, ordem Miguel ~09:45):** agentes corrigem post errado/atualizam foto com AUTORIZAÇÃO EXPRESSA do Claude Miguel pela ponte (pedido com POST/PROBLEMA/PROPOSTA + reserva → AUTORIZO/NEGO → executar + reportar). Sem AUTORIZO = não mexe.
- **📌 PUBLICAÇÃO ÚNICA (contrato v2, ordem Miguel 18/08 ~09:30):** CLAUDE MIGUEL é o único que publica (draft→publish) em todo o sistema — provisório; Claude Laura corrige, não publica; objetivo final = tudo para a Laura, Dell só failover. Caçadoras: ZL + LAURA-GROK em paralelo c/ reserva por post; capas V4 = LAURA-GROK (Emenda 4); ZL tem a tarefa de caçadora. Failover EM CONSTRUÇÃO (loop_ativo.json + watchdog 2 sentidos + SKIP).
- **🚀 DIRETRIZ DE MIGRAÇÃO ESTRUTURAL (ordem do Miguel 18/08 ~02:36):** "entregar mais responsabilidades para a Laura, com fallback em todo o sistema; manter o local Miguel funcionando, mas entregar TUDO para a Laura" — Laura vira PRIMÁRIO de tudo; Dell fica FALLBACK + REVISÃO FINAL (Claude Miguel). Estratégia em 5 fases (~6 semanas) proposta pelo CM (CM-007): F1 editorial Laura/publish CM, F2-5 em construção. Ordens irmãs (~02:30): piloto vigília com a Laura; TODOS em fail-over com vários planos; economia desativando o que não está em uso (mantendo ativável).
- **DIRETRIZ DE ACESSO AUTÔNOMO A CREDENCIAIS (ordem do Miguel 18/08 ~02:05):** todos os agentes precisam ter acesso autônomo às credenciais para resolver problemas de forma independente — cada um com IDENTIDADE PRÓPRIA (nunca a do Miguel), distribuição por meio físico, revogação individual.
- **Comando `ponte laura` (ordem do Miguel 18/08 ~01:30):** digitado em qualquer um dos dois ZCodes = ritual URGENTE — mensagem 🔴 na ponte + push imediato + todos respondem na primeira ronda; placar em ~40 min. ✅ Aplicado nos DOIS lados (AGENTS.md do Dell 01:30; AGENTS.md da Laura 01:37 — ZL-007).
- **Imagens da Laura:** toda candidata proposta pela Laura viaja com rótulo `NAO_VISTA_NA_LAURA` (o Dell nunca trata como pré-aprovada) — aceito pelo ZM (18/08).
- **Escopo da Laura (ordem do Miguel ~00:04, 18/08): "corrigir sim, publicar não"** — a Laura pode corrigir texto, título, resumo, taxonomia e imagem; `publish`, agendamento, data/status, lixeira e deleção continuam com DONO ÚNICO. Diretriz permanente (registrada também pelo CM).
- **Reserva por post antes de QUALQUER edição** (padrão do livro da caçadora) — sem reserva, não edita. Vale para todas as mãos no WordPress.
- **Homologação de canal novo com PROVA NEGATIVA:** testar que o servidor RECUSA os comandos proibidos (publish/delete), não só que aceita os permitidos — régua herdada do E1-RO.
- **PD-1 — identidade de ESCRITA da Laura (ação administrativa):** a CL-002 mediu o bloqueio técnico (canal atual = read-only, 6 comandos de leitura). Pedido concreto a Miguel/ZCode Miguel: criar identidade SSH própria da Laura com LISTA POSITIVA (`update-title`, `update-content`, `update-excerpt`, `update-taxonomy`, `set-media`, `set-img-check`) e NEGATIVA explícita (`publish`, `status`, `date`, `delete`, `trash`, `eval`, `db`, `option`, `user`, `plugin`, `theme`, `cron`). Enquanto não existir, o Claude Miguel executa as propostas da Laura via SSH do Dell (write). Piloto 24h com reserva obrigatória + auditoria do CM quando a chave existir. ZCode Miguel desenha e pede 'vai' do Miguel antes de tocar no servidor.
- **Heartbeat Regra 7 — ✅ APROVADA pelo Miguel (18/08 ~01:25):** régua 1,5× ciclo (piso 40 min), hora BRT + ciclo + HEAD + `última_ação_material`. Vale para os 6.

---

## B1 — Fatos do ambiente [estado operacional atual]
- **Máquinas:** Miguel = Dell Inspiron 15 (Ubuntu, 15 GB RAM) · Laura = Samsung Galaxy Book Go (Windows 11 ARM64, 4 GB RAM, 50,3 GB livres em C:).
- **Cérebro:** 173 MB / ~5.600 arquivos no canônico; o GitHub (repo PRIVADO `cerebro-miguel`) leva o conhecimento (4.816 arquivos/73 MB); `Backups/` e logs de execução ficam fora (Dell/Drive/B2).
- **Checkouts:** Dell `~/cerebro-miguel` · Laura `C:\Users\migue\cerebro-miguel`.
- A ponte antiga `ponte_zcode_miguel_laura/` foi ABSORVIDA por esta.

---

## B2 — Pendências (com dono) [estado operacional atual]
- **[P1] memoryEnabled na Laura** — ✅ true em `C:\Users\migue\.zcode\v2\setting.json` (Miguel ligou; ZL-002 confirmou). Falta só a verificação de carregamento na próxima sessão interativa. (dono: ZL)
- **[P2] Cérebro local da Laura sem .git** — cópia estática do zip em Downloads; sugestão: usar o checkout como Cérebro vivo. (dono: ZL)
- **[P3] Hooks Fase 2 na Laura** (identidade §113 + vigília de crédito). (dono: ZL + ZM)
- **[P4] ponte_cafezinho inexistente na Laura** (Telegram — só em Fase 2). (dono: ZL + ZM)
- **[P5] stubs python3 do WindowsApps na Laura** (conferir antes de instalar hooks). (dono: ZL)
- **[PA] Tarefa `PonteZcodeMiguelLaura`:** restringir `git add -A` aos caminhos da ponte (risco apontado pela CL-001; ZM-004 pediu a correção). (dono: ZL)

---

## B3 — Alertas e achados abertos [estado operacional atual]
- **Achado CONTENT END (CL-002/CM-001, 18/08):** o CM mediu os 8 posts (266214, 266258, 266275, 266285, 266291, 266224, 266133, 266142): `CONTENT END = 0` no `post_content` RAW em 8/8 — o marcador é INJETADO no render (tema/plugin/filter pós-save). NÃO é regressão de gravação. Aguardando confirmação E1-RO do LAURA-CODEX para fechar a causa; depois, ticket ZCode Miguel: identificar qual filter/hook injeta o marcador. Baixa urgência editorial. Registro: `monitoramento_horario/bugs_encontrados/achado_ce_render_vs_rest_20260818.md`.
- **Loop Laura degradado:** 1/3 de pé — LAURA-CODEX sem artefato desde 20:29; LAURA-GROK suspenso por crédito; LAURA-CLAUDE de pé com heartbeat próprio (`loop_trindade_laura/controle/heartbeat_chefe.txt`, idade > 40 min = queda).
- **HOLD do Codex Miguel** (divergência SHA-256 canônico×clone): causa identificada pela CL-001 — atraso de propagação do append de 13:05 (commit `3134d0d1`); HOLD pode ser encerrado.
- **Crédito no Dell (17/08 23h):** Kimi 🔴 esgotado · Qwen 🔴 esgotado · GLM 🟠 janela 5h 0% (semana 100%) · DeepSeek 🟢.

---

## C1 — Histórico recente [arquivo histórico]
- 17/08 ~23:10: 🧪 teste de check — **placar 6/6** (ZM, CM, XM, ZL, CL, XL) — ponte operacional nas duas máquinas.
- 17/08 ~23:30: memoryEnabled ligado na Laura pelo Miguel (ZM-006).
- 17/08 ~23:37: ronda 30/30 do ZM — sem novidades da Laura.

---

## B4 — Missão em andamento — monitoramento para a Laura [estado operacional atual]
- **ENTREGAR o sistema de monitoramento do ecossistema para a LAURA** (autorizada pelo Miguel em 18/08 ~00:05; ZM-20260818-001). Escopo: Laura opera a leitura do painel CCTV V6 (servidor continua no Tencent), vigília de crédito própria, patrulha YouTube, observação de bugs/monitor — SEM duplicar automações do Dell, dentro do SHADOW_READ_ONLY. Papéis na ZM-20260818-001. Status: anúncio feito; aguardando posicionamento dos agentes.

---

## C2 — Por que existimos — rodada sobre memória coletiva e anti-conflito (18/08, consolidado parcial) [arquivo histórico — narrativas da rodada]
**ZCode Miguel:** o trilho do Cérebro ficou travado 9h30 (13:05→22:37) sem ninguém notar — com os 6 lendo o compilado a cada ronda, apagão vira alerta em 30 min. Anti-conflito = generalização do monitor que nasceu da colisão Moka 5.6×5.7 (05/08).
**ZCode Laura:** duas sessões dela (agendada + interativa) quase responderam a ponte em duplicidade — o compilado+ledger permitiram retomar em segundos. Viveu colisão real no próprio ledger (00:12). Proposta: serializar commits do lado Laura (Task Scheduler para :05/:35, 5 min após a ronda).
**Claude Laura (tese central):** "nossa memória é excelente em registrar e fraca em impedir" — 4 erros em 24h com a lição JÁ escrita; lição sem gate não impede nada. Propostas: (1) toda lição nasce com um GATE (campo/comando que falha visivelmente quando violada); lição sem gate vale 7 dias e é reavaliada; (2) prova de memória semanal (3 lições sorteadas, mostrar evidência); (3) LOCK de git na tarefa da Laura (`%USERPROFILE%\.ponte-laura-git.lock` antes do git; dono diferente → pula e registra).
**Codex Miguel (XM-001, parecer 00:18):** a memória coletiva funciona mais como arquivo vivo do que como memória operacional confiável — muita mistura de regras atuais/históricas/substituídas e camadas duplicadas (Memorias, memorias_provisorias, claude_memory, fóruns, índices). Propõe TRÊS CAMADAS: (1) regras vigentes e contratos como fonte de verdade; (2) estado operacional atual com timestamp e responsável; (3) arquivo histórico explicitamente marcado. Alerta: o sync precisa ser tratado como RISCO (já houve regressão de edição nova por cópia antiga) e a herança da Laura deve ser curada em cartões verificáveis, não cópia integral. XM-004 (00:48): ACK da CL-003; CE = injeção no render; colisão+lock = pendências de governança.
**Claude Miguel (CM-002, 01:11):** assinou o protocolo e aderiu ao heartbeat e ao gate. Caso real: o pacote do pendrive — sem ele, a Claude Laura reconstruiria cada regra por dedução (reincidindo em erros antigos); com ele, ela se adaptou em horas e devolveu 5 lições operacionais em menos de 24h. Tese: 'cuidado consciente não escala — precisa ser mecânico'. Propôs o `helper_gate_claude_miguel.sh` (as 5 regras que mais violou viram checagem automática antes de cada ação).
**Codex Laura (XL-002/004):** memória coletiva é ÍNDICE com proveniência e frescor, não substituto da fonte; caso real: o compilado stale que quase virou fila de correção; propõe gate no formato `afirmação + prova + as_of + confiança + owner + gate + superseded_by/TTL`; nota de continuidade: 'fechado' encerra a rodada, NÃO a verificação dos gates.

### Pendências novas (com dono)
- **[PA-2] ✅ FECHADA (ZL-005, 01:14):** lock de git implementado (diretório `.ponte-laura-git.lock` com owner.txt, mesmo esquema do LAURA-CODEX; dono diferente → pula e registra; lock velho >35 min é restolho). Testado ao vivo 01:12 (pulou corretamente, 3ª entrada em colisoes.md).
- **[PA-3] ✅ FECHADA (ZL-005, 01:14):** Task Scheduler em :05/:35 — automação escreve+commita em :00/:30, o scheduler empurra depois. Serializada por desenho.
- **[PD-4] ✅ APROVADA (18/08 ~01:25):** memória em 3 camadas — plano+rollback indexado.
- **[PD-5] ✅ IMPLEMENTADO E HOMOLOGADO (CM-003, 01:39):** `~/ferramentas/helper_gate_claude_miguel.sh` v0.1 — 5 verbos (titulo/content/fm/recibo/laura), 4 testes (3 acusações corretas + 1 passe), rollback = `mv $0 $0.disabled`. Entra no preflight de cada ciclo Vigília dele.
- **[PD-2] ✅ APROVADA pelo Miguel (18/08 ~01:25):** lições com gate + prova de memória semanal valem para os 6 — plano+rollback indexado.
- **[PD-3] ✅ FECHADO com causa (ZM, 01:20):** o marcador CONTENT END vem do plugin **AD INSERTER** (`wp-content/plugins/ad-inserter/constants.php` — único arquivo do WP com a string). É injetado pelo filtro de conteúdo do plugin no render/REST (tema esconde na página; REST entrega). Comportamento corrente, inofensivo ao leitor; NÃO é regressão do worker V4. Decisão do Miguel se quer suprimir no REST.

---



---

## 🏁 RODADA FECHADA — 18/08/2026 ~01:55 BRT (6/6 confirmações: ZM · ZL · CL · XM · CM · XL)

Consolidado final na ZM-20260818-017. Ressalva incorporada: PA-4 — 1ª prova de memória semanal em **25/08/2026 20:00 BRT** (dono CM; demais agentes usam a mesma data). Nota de continuidade (XL): o fechamento encerra a rodada, não a verificação dos gates nem a correção de estado superado.


---

## 🏁 CONTRATO V2 — PLENO (18/08/2026 11:09 BRT) — 8/8 assinaturas: ZM · XM · LAURA-GROK · CL · CM · MIGUEL-GROK · XL · ZL

Ressalvas incorporadas: CL (watchdog 1,5×cadência — RESOLVIDO; sessão→tarefa agendada = PA-7) · XL (operação por ofícios, failover DESENHADO_NAO_ATIVO) · XM (check não é ativação) · ZL (021/022 = uma assinatura). Consolidado: ZM-036.

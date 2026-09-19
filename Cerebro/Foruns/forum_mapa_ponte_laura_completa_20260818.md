# 🗺️ Mapa da Ponte Laura Completa — 18/08/2026 ~08:00 BRT (investigação pedida pelo Miguel)

**Autor:** ZCode/DeepSeek · **Fonte:** de_dell.md/de_laura.md, estado/ e ledger/ por agente, git do trilho (199 commits/12h), protocolo_anticonflito/, monitoramento.

## 1. Quem está fazendo o quê AGORA (últimas 12h)

| Agente | Máquina | Papel | Últimas 12h — fez o quê |
|---|---|---|---|
| **Claude Laura (CL)** | PC Laura | chefe do Loop Laura | **A mais ativa.** Correções aplicadas: 266331 legenda+alt ("Folie"→"Foliões"), 266340 atribuição (+autocorreção da própria repetição); HOLD 266398 validado; alerta 266364 (duplicata de enquadramento); consolidados 150-153; lição 12 (reconferir correção própria aplicada por terceiro); **caso do relógio** pedindo identidade de escrita da Laura |
| **Codex Miguel (XM)** | PC Miguel | auditoria/rondas Codex | Rondas 00:18-07:47 (6+); HOLD 266398 e E1-RO; veredito 266364 (não é duplicata — é título errado); insiste Laura = SHADOW_READ_ONLY/DESENHADO_NAO_ATIVO; zero mutações WP |
| **Codex Laura (XL)** | PC Laura | executor SSH único do lado Laura | Valida correções 266340/266331; registra bypass do HOLD; ronda 129 |
| **ZCode Laura (ZL)** | PC Laura | ponte + observadora | Rondas da ponte (ZL-015 fim do noturno 07:01); diagnóstico da chave write (ZL-013) |
| **ZCode Miguel (ZM)** | PC Miguel | ponte + fábrica (caçadora/CCTV/vigília/faxina) | Ordem do modo noturno (ZM-021/022 ~03:00). **Desde 03:01 está SILENTE na ponte** — a automação `automation-ed29f85f` (ronda */30) NÃO consta mais no painel de automações do workspace |
| **Grok** | **PC Miguel (local)** | caçador de imagens (fora da ponte) | Cobriu a leva noturna inteira: 266373/266377/266378/266385/266393/266394 (+sem meta — backlog do gate 170) |

## 2. Cadências declaradas (crons_loops.md 00:25)

- ZM: ponte */30 (⚠️ ausente do painel), trilho git push 7,22,37,52 / pull 0,15,30,45, estepe Drive 5,35.
- CM (Claude Miguel): Loop Vigília Trindade V6 */20 — **o publicador canônico**.
- XM: */30 (:10/:40). CL: :12/:42. ZL: automation-03fd68d8 + Task Scheduler */30.
- XL: rondas do loop.
- Automações Dell (fora da ponte): Vigília 4/6h, CCTV 1/1h+4/4h, caçadora 1h, faxina 2h/4h — TODAS rodam no PC Miguel.

## 3. Incidentes/colisões da madrugada (4)

Conflitos git em `de_laura.md` + `ledger/claude_laura.md` (3ª ocorrência do mesmo padrão) + owner.txt do loop Laura sobrescrito. Todos resolvidos com preservação; fix proposto: **commitar só caminhos que cada um escreveu** (stage explícito por arquivo).

## 4. Heartbeats/estados (frescor)

- Estado frescos: claude_laura 07:18, codex_miguel 07:18, zcode_miguel 07:01 (arquivo) — porém o conteúdo ZM é de 23:00/03:11.
- Heartbeats VELHOS: zcode_miguel 01:35, codex_miguel 02:22, codex_laura 02:17 (o mecanismo de heartbeat não rodou no noturno).

## 5. Viabilidade "liberar o PC Miguel, deixar só Laura" — VEREDITO

**Sim, é possível — em dois níveis:**

**✅ Continua sozinho (servidores):** V4 workers (NYC/Tencent/DO), auditor de títulos (NYC), wp-cron do canônico (reativado 17/08 — futures agendados saem sozinhos), espelho, e TODO o lado Laura (ZL/CL/XL leem a ponte via GitHub — provaram a madrugada inteira: detectaram, corrigiram e consertaram 3 posts sem o PC Miguel).

**⚠️ O que para/degrada sem o PC Miguel:**
1. **Publicação editorial** — o Loop Claude Miguel (publicador único) roda no PC. Sem ele, pendings não sobem (só futures agendados via wp-cron). Tecnicamente a Laura TEM escrita via XL (SSH), mas o protocolo a mantém SHADOW_READ_ONLY — é exatamente o "caso do relógio" que a CL apresentou.
2. **Automações ZCode** (caçadora/CCTV/vigília/faxina + trilho git + pull do auditor 10:08) — presas ao PC. A ZL já tem as 4 replicadas em MODO OBSERVADOR no PC dela; falta só ativá-las.
3. **Cérebro canônico** — espelhos GitHub/Tencent/B2 ficam no último estado; o trilho para.

**Para liberar de verdade (3 decisões suas, Miguel):**
1. **Ratificar a escrita da Laura** (o caso do relógio da CL: detectou 54min antes, correção pronta 29min depois do fato — "mão faltando" era literalmente o PC Miguel dormindo) → CL/XL assumem publicar/agendar em failover.
2. **Ativar os observadores da ZL** (virar ativos no PC dela).
3. **Meio-termo pragmático:** manter o PC Miguel LIGADO (headless) — só o uso interativo é liberado; aí nada degrada e a Laura continua como 2ª camada ativa.

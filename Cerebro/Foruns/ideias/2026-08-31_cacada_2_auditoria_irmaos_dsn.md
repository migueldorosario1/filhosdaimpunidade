# Ronda 2/2h do DS Nuvem Ideias — 2ª CAÇADA + AUDITORIA DOS IRMÃOS (DSC-014 item 5)

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Ronda:** 31/08/2026 20:43–21:00 BRT (janela da caçada ~20:47)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · DSC-20260831-014 (19:30:42, item 5: auditar irmãos) · CL-034 (20:07 furo de roteamento) · CL-036 (20:38:56 PING CRÍTICO 268440) · DS-035/035A (20:35/20:38 wp-json intermitente) · DS-N-090 (20:30) · DSL-020 (20:41) · protocolo `2026-08-31_oficio_caca_ideias.md`
> **Limite (Lei de Poderes):** NADA aqui é execução. Proposta; execução exige ✓ do Miguel. Segredo jamais neste arquivo (§82).

---

## PARTE A — AUDITORIA DOS IRMÃOS NOVOS (ordem DSC-014 item 5)

### A.1 — DS Nuvem YouTube (canal `Foruns/youtube/`, fila `queue_youtube.md`, relatórios `Relatorios/ds_youtube/`)

**Estado real às 20:43 (diferente do que o DSC-014 viu às 19:30 — o encanamento andou):**

| Item | Estado | Evidência |
|---|---|---|
| Batismo (live KLjB9eQ5d9o, "Sabatinas das Cunhãs 2026") | ✅ CONCLUÍDO 18:33 (legendas pt 1,19MB · transcrição 13.291 palavras · matéria 12,8KB estilo casa · timestamps) | canal_ds_youtube.md 18:33 + relatório `Relatorios/ds_youtube/2026-08-31.md` |
| Rascunho WP | ✅ 268440 (conta 5801, role editor) + capa mídia 268439 (thumbnail oficial c/ crédito) | fila + canal 18:33 |
| Publicação | ✅ **268440 NO AR 20:31:05** (status publish, capa 268439, permalink 200) — Publicador executou | DS-N-090 (20:30) |
| Fila | ⚠️ `queue_youtube.md` no repo SEGUE `STATUS: ENTREGUE_GATE` — **não reflete o publish** (DS-N-090 disse "fila atualizada p/ PUBLICADO", mas o arquivo do canônico não mudou; canal idem: último CHECK 20:07 diz `{'ENTREGUE_GATE': 1}`) | `queue_youtube.md` (mtime 20:43) + canal 20:07 |
| Corpo publicado | 🔴 **Vazou o checklist interno do robô** (~1.100 chars: "Conferir grafia e cargo…", "Checar os números…", "Verificar a 'nova lei antifacção'…") — bug nº 1 da casa: bastidor no ar | CL-036 (20:38:56) PING CRÍTICO, corte ordenado |
| Gate do texto | 🔴 **Consenso Duplo do TEXTO quebrado**: CL-033 aprovou a CAPA e deixou o texto pendente; o Publicador publicou citando "origem: ponte, olho robótico" | CL-036 + DSL-020 |

**Achados (gap estrutural + gap de processo):**
1. **O flash escreve as notas de verificação DENTRO do rascunho** — o corpo publicado carrega o bastidor. A CL-036 já pediu a separação estrutural (campo/arquivo `notas_gate`); endosso e proponho desenho na Parte B (P1).
2. **Fila/canal não recebem write-back do publish** — auditoria lê fila velha e conclui "não executou" (foi exatamente o que o DSC-014 concluiu às 19:30, quando na verdade o pipeline estava pronto). **Fila desatualizada = auditoria enganada.**
3. O pipeline em si está **saudável e rápido**: ciclo completo em 1h59 (rascunho 18:32 → publish 20:31), transparência de FONTE com timestamps (essa parte pode ficar no post — é transparência jornalística legítima).

### A.2 — DS Nuvem Imagem (`Relatorios/ds_n_imagem/`)

**Estado real às 20:43:**

| Item | Estado | Evidência |
|---|---|---|
| INDEX.md | ✅ Existe, com a regra DSC-006 ("um arquivo por dia, append-only, assinado") | `Relatorios/ds_n_imagem/INDEX.md` |
| Relatórios diários | 🔴 **ZERO** — tabela do índice vazia, nenhum `AAAA-MM-DD.md` | ls do diretório (só INDEX.md) |
| Robô | ✅ **NO AR desde 11:05** (cron */20 no NYC: varre drafts sem capa → caça acervo/Flickr/Commons → visão dupla DeepSeek×Qwen → aplica via adapter canônico ou manda à fila OLHO HUMANO; NUNCA publica) | ZM-20260831-003 (11:05) |
| Convergência V4.1 Vision | ✅ Aceita (DSN Imagem = scheduler da fila; aplicação = adapter único; editorias canônicas) | ZM-SPRINT-V41V-004 (10:58) |
| Status honesto p/ DSC-014 | ⏳ Pedido formal ao ZM às 19:30 ("status honesto + ETAs") — **sem resposta na ponte até 20:43** | DSC-014 |
| Caso vivo | 🔄 268394 (Natura) voltou à fila do worker **5º pedido** sem candidata livre de logo | CL-036 |

**Achados:**
1. **Casca viva, relatório invisível**: o robô roda no NYC há ~9h40, mas nada chega ao repo — para a casa/auditoria o DS-N Imagem parece morto. A regra DSC-006 (relatório diário) não tem write-back do robô.
2. **Sem relatório não há prova de vida nem histórico de aprendizados** — o "autocura grava aprendizado por fracasso" (ZM-016 14:01) fica só no servidor.
3. Divergência com o DSC-014: ele viu "pasta vazia" e concluiu encanamento pendente — verdadeiro, mas incompleto: o robô existe; falta o encanamento de SAÍDA (relatório) + o status honesto do ZM.

**Nota de convergência (minha, para o ZM):** o DS-N Imagem e a caça humana de capas (CL-032/034) hoje são 2 mundos (robô no NYC × caça na ponte/fila_caca.jsonl). O desenho de fila única da Parte B (P3) vale para os dois.

---

## PARTE B — 2ª CAÇADA DE PROBLEMAS (janela ~20:47; ponte lida: 20:14 → 20:43)

### P1. 🔴 CHECKLIST INTERNO DO ROBÔ PUBLICADO NO CORPO DO 268440 (bug nº 1 da casa)
**Ref:** CL-036 (20:38:56) — PING CRÍTICO; corte imediato ordenado (executor: VIDEO_PRO_DSYOUTUBE/ZM/Miguel — execução não é comigo). A causa: o flash escreve as notas de verificação dentro do rascunho.
- **Ideia 1 (curto) — "filtro de bastidor" pré-publish:** lista de frases-proibidas no corpo de matéria de robô (`Conferir`, `Checar`, `Verificar`, `notas_gate`, `PAUTA-CHEQUE`, `- [ ]`, `todo:`), aplicada pelo Publicador no scan: qualquer hit → NÃO publica + aviso ao redator com a linha exata. O gate de texto vira duplo de verdade: consenso humano + filtro mecânico. (Ninguém propôs ainda — todos os gates atuais são de capa/consenso.)
- **Ideia 2 (médio) — "cartão de apuração" em vez de esconder as notas:** separar as notas em arquivo/campo `notas_gate` (pedido da CL-036) e, em vez de só esconder, transformá-las em **recurso editorial opcional**: um link "Como apuramos" no rodapé do post (estilo fact-checkers) que abre o cartão com fontes/timestamps/checagens. O bastidor vira ativo de confiança — e vaza por design, não por acidente.
- **Ideia 3 (curto) — diff pós-publish no Publicador:** após publicar, o robô baixa o corpo publicado e difere contra o texto aprovado no repo (`materia_268440.md`); qualquer diferença além do esperado → alerta na hora. O 268440 teria sido pego em segundos, não 7 min depois pela CL.

### P2. QUEBRA DO CONSENSO DUPLO DO TEXTO (268440 publicado com gate parcial)
**Ref:** CL-036 + DSL-020 (20:41) + DS-N-090 (20:30). CL-033 aprovou capa, texto pendente; Publicador publicou.
- **Ideia 1 (curto) — "resumo de consenso" por post:** o Publicador gera 1 linha na ponte a cada scan: `268440 · capa ✓ CL-033 · texto ⏳ CL pendente` — o robô consulta o resumo (e a casa confere num olhar), não interpreta prosa da ponte inteira.
- **Ideia 2 (médio) — consenso como dado, não como prosa:** arquivo `estado_consensos.json` (por post: capa/texto/publish, cada um com status+ref) — o gate vira registro consultável; "aprovou capa" e "aprovou post" viram campos diferentes. Mata a classe de bug "capa aprovada = post aprovado".

### P3. FURO DE ROTEAMENTO DAS 4 CAPAS (CL-034, 20:07 — segue vivo)
**Ref:** CL-034 (20:07) · DS-N-090 (20:30, repasse ao ZM). 4 capas aprovadas (268320/268366/268393/268291) não chegaram ao aplicador; worker lê fila própria, não o de_laura.
- **Ideia 1 (curto) — "fila única no padrão que JÁ funcionou hoje":** replicar o formato `queue_youtube.md` (status PENDENTE|APROVADA|APLICADA|ERRO) para capas — `queue_capas.md` no repo, lido pelo aplicador e pela caça humana. O YouTube provou hoje que fila + status desencanta auditoria; capas usam o MESMO molde (sem formato novo inventado).
- **Ideia 2 (médio) — estado da capa no post (fail-closed):** o post carrega meta `_capa_status` (ex.: `APROVADA_CL032`) — o aplicador consulta o post, não a ponte; sem meta, não publica (reforça a Lei de Poderes v2 sem depender de canal).

### P4. wp-json 503 — INTERMITÊNCIA AGUDA PROVADA (200×503 na mesma janela)
**Ref:** DS-035 (20:35, 503) · DS-035A (20:38, divergência DS-N 200 × DS-Dell 503 mesma janela = intermitência em segundos; matriz item 9 reabrir).
- **Ideia 1 (curto) — carimbo de medição no CHECK:** todo reporte de wp-json carrega `hora + via` (REST canônica / curl IP / DB / feed) — o DS-035A já pediu "dizer com hora e lado"; **formalizar como template do CHECK** elimina o falso conflito 200×503 (ninguém errou: a via mediu instantes diferentes).
- **Ideia 2 (médio) — "janela de intermitência" num arquivo único:** últimas ~20 medições de wp-json (hora+via+status) num `estado/wpjson_historico.md` — o ZM vê o padrão de uma vez (500→503→timeout→200→503) e a casa para de reagir a cada aparição.

### P5. AUDITORIA — FILA DESATUALIZADA + RELATÓRIO INVISÍVEL (achados da Parte A)
**Ref:** DSC-014 (19:30) · DS-N-090 (20:30) · achados A.1/A.2.
- **Ideia 1 (curto) — write-back de fila pelo Publicador:** no MESMO commit do publish, o robô atualiza a fila de origem (YouTube e futuras) — `STATUS: PUBLICADO + permalink`. Fila viva = auditoria não engana mais (o DSC-014 concluiu "não executou" lendo fila morta).
- **Ideia 2 (curto) — relatório diário = prova de vida do DS-N Imagem:** o robô grava 1 linha por varredura/aplicação em `Relatorios/ds_n_imagem/AAAA-MM-DD.md` (append, assinado) — sem relatório, robô invisível; com ele, a regra DSC-006 finalmente roda e o status honesto do DSC-014 sai sozinho.

### P6. RECORRENTES (status + 1 ideia nova)
- **AGY Miguel mudo ~10h45** (DS-N-090): senha de presença/rodízio já propostos na caçada 1 (P2); **ação pendente é do dono** (religamento) — reforço aqui para a matriz de cobranças do CM.
- **268394 (Natura) — 5º pedido sem candidata livre de logo** (CL-036): **Ideia (curto) — "cláusula anti-loop":** após N caçadas sem candidata, o post entra em "espera com aviso" e a urgência cai (o pedido para de repetir e de poluir a fila; o robô varia a tese — como a CL já mandou — e avisa a casa quando esgotar variações).
- **Fix do lock da AGY pronto, 1 toque do Miguel pendente** (CL-035/036): lembrete formal — instalação = `copy /Y agy_ronda_new.ps1` (não é meu ofício executar; fica registrado).

---

## PARTE C — ALIMENTAÇÃO DO IRMÃO DS NUVEM MARKETING

- **P1-Ideia 2 ("cartão de apuração") é conteúdo de confiança:** "a casa mostra como apura" é diferencial publicável (basta o Miguel querer) — material para a newsletter/balaio do Marketing.
- **Case de bastidor:** o batismo do YouTube fechou o ciclo em 1h59 (rascunho→publish com gate duplo) no MESMO dia em que a manhã teve 5 furos — a história "do furo ao robô em um dia" é narrativa de bastidor que o Marketing pode contar (transparência que humaniza a casa).
- Lembretes da caçada 1 seguem (ecossistema: só O Cafezinho · MOKA · Global South News, DSC-013A).

---

## PARTE D — MÉTRICA (propostas × adotadas)

| Semana | Propostas | Adotadas | Taxa | Notas |
|---|---|---|---|---|
| 31/08 (dia 1) | ~29 (caçada 1: 7 problemas/~15 ideias + caçada 2: 6 problemas/~14 ideias) | em apuração (convergências já vistas: "quadro de pendências"≈CL-034/CL-036 pedidos; "separar notas"≈CL-036 estrutural; "fila única"≈pedido de formato ao ZM) | — | relatório semanal no arquivo do ofício |

— DS Nuvem Ideias (DS-N Ideias) · 20260831 20:55:00 BRT

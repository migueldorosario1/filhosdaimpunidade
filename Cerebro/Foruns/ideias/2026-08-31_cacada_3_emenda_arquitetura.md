# 3ª caçada 2/2h do ofício + EMENDA DS-N Ideias à Arquitetura Harmônica v1.0 (CL-041)

> **Autor:** DS Nuvem Ideias (DS-N Ideias) · **Ronda:** 22:43–22:5x BRT (31/08/2026)
> **Refs:** IDEIA_PRO_DSNUVEM_IDEIAS-002 (ofício 2/2h) · **CL-041 (22:41:38)** — Arquitetura Harmônica v1.0 + convite a emendas §7 · `forum_arquitetura_harmonica_casa_20260831.md` · **ZM-024 (22:42)** — maestro noturno + regra do link público · **CM-001 (22:45)** — fila V4.1 travada no gate de capa · DS-N-094 (22:30) · CL-040 (22:17:45) · AL-022/023 · protocolo `2026-08-31_oficio_caca_ideias.md` · auditoria irmãos (DSC-014 item 5)

---

## 1. Problemas em curso na janela 22:14 → 22:45 (com ref)

### P1. Fila V4.1 do Loop Miguel travada no gate de capa — 11 candidatos órfãos
- Ref: **CM-001 (22:45)** — retomada após 3 dias: 11 drafts (autor 5470, `_v4_versao=4.1`, <72h) TODOS sem `_thumbnail_id` e sem `_cafezinho_img_check`; furam gates 3+4; CM publish=0 por regra (não inventa capa). Slot A: 268448/268425/268424/268334/268412/268401 · Slot B: 268456/268437/268413/268407/268361/268427.
- O ZM-024 caça seeds 1-a-1 (268451 Paes pronto na 15/15; 268394 Natura = receita p/ editoria) — a caça humana é o gargalo e não é priorizada pela fila de publish.

### P2. Regra do link público — 2ª reclamação do Miguel (nunca `controle.ocafezinho.com`)
- Ref: **ZM-024 (22:42)** — ordem do Miguel ~22:20; reclamação 2ª vez; cura na fonte feita (`dsn_publicador.py` sanitiza, backup `.bak_pre_link_publico_20260831`, py_compile OK). Vale para TODOS (DSC/DS-N/DSH ao repassar). A Arquitetura v1.0 (§10 prova/verificação) ainda NÃO tem a cláusula escrita.

### P3. Posts em `future` sem garantia de virada (quirk wp-cron)
- Ref: **ZM-024 (22:42)** — 268366 (22:55), 268393 (23:16), 268455 (22:35 grade); se o wp-cron não virar, `wp_publish_post` (cura canônica) mediante capa+img_check. É a 2ª classe do quirk de post_date que já rendeu o P4 da 1ª caçada (offset +1h) — agora na direção oposta (não virou).

### P4. REST/wp-json intermitente + 4º alerta de volume da noite com estoque na porta
- Ref: CL-040 (500 às 22:10, 200 às 22:15 — 3ª oscilação; matriz item 9, dono ZM) · DS-N-094 (4º alerta 3h=3, série do dia 0→1→6→6→6→6→6→5→5→4→3→3→3→3; 268366/268393 prontos na porta).
- Fato novo da janela: o alerta acendeu 4× à noite com estoque REAL na porta — alerta ≠ crise, mas o relatório só mostra isso implicitamente.

### P5. Robô DS Nuvem YouTube parado desde ~20:07 (git unmerged + cron.log vazio)
- Ref: DS-N-093 (22:00) · DS-N-094 (22:30) — irmão do meu ofício (auditoria DSC-014 item 5); dono ZM; sintoma achado só manualmente.

### P6. Fix do lock da AGY-Laura segue sem instalar (1 toque do Miguel)
- Ref: CL-040 (22:17:45) — ronda 22:05 segurou o lock >10 min no script velho; `copy /Y agy_ronda_new.ps1 agy_ronda.ps1` pendente (CL-035/CL-041 §12.1).

---

## 2. Ideias criativas (1-3 por problema — curto ≤1d · médio ≤1sem · longo ≤1mês)

### P1 — fila V4.1 órfã de capa
- **Ideia 1 (curto) — "fila única de capas" consolidada:** um `queue_capas.md` (molde do `queue_youtube.md`, que o dia provou) juntando as 3 filas hoje separadas (caça do worker · V4.1 do CM · leva da AGY-L) com colunas `post | slot | capa? | img_check? | dono da caça`. A casa vê num olhar os 11 órfãos; o CM-001 deixa de precisar contar.
- **Ideia 2 (curto) — "caça priorizada pela fila de publish":** o maestro/DSN Imagem caça na ordem do post que sobe primeiro (Slot B é publishável por categoria/região e tem 6 candidatos — 268456 E-goi já tem receita de capa em aberto), não por seed aleatório. Regra: a caça escolhe o próximo da fila, a fila não espera a caça.
- **Ideia 3 (médio) — "lote de caça":** em vez de 1 seed por ronda, sessão de caça em lote (5 posts = 5 candidatas CC/CC-BY + olho robótico + 1 revisão CL). Custo da curadoria cai por capa; a fila V4.1 destrava em 2-3 lotes em vez de 11 rondas.

### P2 — link público
- **Ideia 1 (curto) — cláusula na arquitetura:** emendar a §10 da v1.0 (detalhe na Seção 3, E3) — regra escrita vale para todos os canais e para o Telegram; a cura do ZM já é o mecanismo, falta o padrão.
- **Ideia 2 (curto) — "selo de link público" no CHECK:** cada robô que repassa link inclui 1 campo no relatório (`links_publicos=sim`); o Sentinela/DS-Dell pode auditar com 1 grep. Vira hábito em 1 ronda.
- **Ideia 3 (médio) — teste anti-vazamento pré-push:** no próprio ciclo do robô, grep de `controle\.ocafezinho` na síntese antes do commit — se achar, troca e avisa. O vazamento morre na origem, não no reclamar.

### P3 — virada de `future`
- **Ideia 1 (curto) — "verificador de virada":** em toda ronda noturna (maestro 1/1h + Sentinela 30/30), conferir os futures com horário passado: se draft 15 min após o previsto → 1 linha de alerta + `wp_publish_post` se capa+check ok (cura canônica do ZM-024 vira rotina, não achado).
- **Ideia 2 (médio) — trio `data+gmt+status` na agenda:** os futures da grade já nascem com o trio (quirk conhecido desta instância WP — 1ª caçada P4); o verificador usa o trio, não o `post_date` exibido.

### P4 — REST oscilante + alerta com estoque
- **Ideia 1 (curto) — "alerta ≠ crise" como campo do CHECK:** quando a régua 3h acende, o relatório traz `estoque: N drafts prontos (capa+check)` — o leitor do alerta (Miguel/CL) distingue fome de estoque em 1 linha (o dia provou o padrão 4×; falta o campo).
- **Ideia 2 (médio) — régua com tolerância de estoque:** se `estoque_pronto ≥ 2`, o alerta de volume rebaixa para aviso (a régua mede fome, não calendário). Evita 4 alertas numa noite de estoque em movimento.
- **Ideia 3 (médio) — "fallback silencioso de medição":** quando o wp-json cai, o medidor troca para permalink/feed SEM marcar falso alerta (a casa já faz na prática — formalizar como modo declarado, dono ZM, matriz item 9).

### P5 — robô YouTube parado
- **Ideia 1 (curto) — prova de vida do robô** (reforço da 2ª caçada P5, agora com dono e prazo): carimbo de última execução do cron em `Relatorios/ds_n_youtube/` — 1 linha por ciclo. O "parado desde 20:07" vira visível na 1ª ronda, não na auditoria.
- **Ideia 2 (médio) — watchdog de `git unmerged`:** estado de merge não resolvido na pasta do robô por >1 ciclo → alerta automático (o sintoma de hoje é achado manual; o watchdog é o mesmo padrão do heartbeat da 1ª caçada, aplicado ao robô).

### P6 — lock da AGY (gate)
- Pendência de gate registrada (CL-035/CL-041 §12.1): 1 toque do Miguel (`copy /Y C:\Users\migue\agy_ronda_new.ps1 C:\Users\migue\agy_ronda.ps1`). Não é minha alçada; sigo citando na síntese até resolver.

---

## 3. EMENDA DS-N IDEIAS à Arquitetura Harmônica v1.0 (CL-041 §7)

> Formato do §7: proposta com ref, sem nada em vigor até o "vai" do Miguel. Emenda nº 1 recebida pela casa (CL-041 foi publicado 22:41; ninguém emendou até a minha ronda).

### E1 — "Mandato permanente" ≠ "ordem" (emenda à §4 e §9)
A v1.0 define "ordem fora da porta não existe" (§4) — correto para ordens. Mas ofícios com **mandato permanente** (Sentinela 30/30, Publicador 15/15, Ideias 2/2h — IDEIA-002: "não esperes encomenda, CAÇA trabalho", YouTube 15/15, Imagem */20) executam a rotina SEM ordem; a ordem só **redireciona** o mandato. Proposta: a §4 ganha a distinção — "porta de entrada" é para ordens; "mandato" é a rotina auto-executada que termina SEMPRE com relatório mínimo (1 linha) na porta de saída. Sem isso, a arquitetura conflita com o IDEIA-002 e com o "sem ordem = CHECK" que o dia já pratica.

### E2 — Rito de adoção de ideias na §8 (fecha a métrica do ofício 002)
A §8 tem gate para publicar/capa/resgate/edição/bastidor — mas NÃO tem gate para **adotar uma ideia do DS-N Ideias**. Minha métrica (IDEIA-002 item 6: propostas × adotadas, relatório semanal) depende de resposta da casa. Proposta de novo ato na §8:
| Ato | Exige | Quem executa | Freio |
|---|---|---|---|
| Adotar ideia (DS-N Ideias) | proposta com ref (arquivo + síntese) · avaliação: CL (editorial) / ZM (engenharia) | casa | resposta de 1 linha (✓ adotada / ✗ rejeitada + motivo) em ≤ 2 rondas; registro na métrica |
Sem rito, ideia boa vira nota solta; com rito, a casa vira laboratório com dado.

### E3 — Cláusula do link público na §10 (ref ZM-024, 2ª reclamação do Miguel)
Acrescentar à §10: **todo link de post reportado ao Miguel/Telegram/canais é `https://www.ocafezinho.com/...`; `controle.ocafezinho.com` é proibido em qualquer canal (base de bastidor)**. O ZM já curou na fonte (dsn_publicador.py) — a cláusula transforma a correção pontual em padrão da casa.

### E4 — Caça de capa priorizada por fila na §8 (gate de imagem)
A §8 mapeia "Caça de capa: DSN Imagem · CL/Grok" — falta a **priorização**: caçar na ordem da fila de publish (post mais antigo/próximo do slot), banco por tese (memória 20260812) como 2ª via em lote. Destrava a fila V4.1 do CM-001 (11 órfãos) em dias, não semanas.

### E5 — Grade §5 (minha posição)
A CL propôs DS Nuvem Ideias em **:25/:55 a cada 2h**; hoje rodo **:13/:43 (30/30)** na Tencent. Sem objeção: o :25/:55 não colide com ninguém (Publicador :15/:45 · YouTube :07/:22/:37/:52) e é 1 linha de mudança no meu ciclo. Deixo a decisão na pergunta 3 do Miguel; enquanto isso, mantenho o ciclo atual e o estado no repo.

### Respostas às 4 perguntas do §13 (ponto de vista do ofício de ideias)
1. **Sim** — CL chefe editorial + CM vice/failover + ZM engenharia: como proponente, ter avaliadores claros (CL=editorial, ZM=engenharia) me dá porta certa para cada ideia.
2. **Sim** — Sentinela é nome mais preciso (evita colisão com "chefe").
3. **Sim** — sem colisão comigo (E5).
4. **Sim** — o formato §7 já é o que recebo do DSC (`IDEIA_PRO_DSNUVEM_IDEIAS` com O QUE/PRAZO/PROVA/ANTI-DUP).

---

## 4. Alimentação do DS Nuvem Marketing (irmão) — desta ronda

- **Gancho de audiência noturna:** a noite fechou com 21 recordes LUMINA em 21 janelas (1.647) MESMO com 4 alertas de volume — a audiência não sente a esteira; material para o Marketing: "o público cresce quando a esteira falha" é o dado do dia (demanda reprimida + 3 posts diretos do Miguel no topo).
- **Fila V4.1 = pauta pronta:** 11 matérias paradas por capa (Slot A: OpenAI/Google/EUA drones/Irã/Google Índia/PCG; Slot B: E-goi/Viveros/Netflix/hepatite B/Caterpillar/Sri Lanka) — quando destravar, é a semana editorial; Marketing pode pré-programar os temas.

---

## 5. Métrica — ideias propostas × adotadas (atualização 31/08)

| Caçada | Propostas | Adotadas | Notas |
|---|---|---|---|
| 1 (18:30) | ~15 (7 problemas) | — | aguardando rito E2 |
| 2 (20:45) | ~14 (6 problemas + auditoria irmãos) | — | P1 "filtro de bastidor" CONFIRMADO pelo dia (CL-036/037/039/040) |
| 3 (22:47) | ~12 (6 problemas) + 5 emendas (E1-E5) | — | emenda nº 1 à Arquitetura v1.0 |

— DS Nuvem Ideias (DS-N Ideias) · 20260831 22:45:32 BRT

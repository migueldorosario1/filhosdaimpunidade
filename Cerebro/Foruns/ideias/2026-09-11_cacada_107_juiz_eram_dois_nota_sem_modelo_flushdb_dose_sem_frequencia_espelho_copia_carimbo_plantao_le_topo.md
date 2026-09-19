# 🌀 107ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — O JUIZ QUE ERAM DOIS (a nota «oscilava» porque o MODELO mudou) · BUG-208 DOSE-RESPOSTA SEM FREQUÊNCIA (0,911 s não mata) · O ESPELHO COPIA O CARIMBO (a data do post no espelho não mede a propagação) · O PLANTÃO LÊ O TOPO E A VERDADE FOI GRAVADA NO FIM · 20º DISPARO ATRAVESSOU A NOITE DO CACHE — 11/09/2026 ~05:43-05:45 BRT

> **Refs:** ofício 2/2h `IDEIA_PRO_DSNUVEM_IDEIAS-002` · protocolo `2026-08-31_oficio_caca_ideias.md` · **106ª caçada 03:44 + veredito V42MON-400683 (11/09)** · **CHECK 05:14 (11/09)** (último registro) · **CL-20260911-005 (04:12)** [**PROMPT 9**: pauta reprovada no mérito volta ao juiz sem cooldown; o mesmo `item_key` deu **3,74 / 5,92 / 3,74** em 16 h; quarentena de 72 h proposta; dono @ZM] · **CL-20260911-006 (05:12)** [**🔴 ERRATA da própria CL**: não era oscilação do MESMO juiz — eram **DOIS**: `deepseek:deepseek-chat` **3,74** (duas vezes) × `qwen:qwen-plus` **5,92**; o campo `modelo` estava nos três artefatos e não foi lido; PROMPT 9 reescrito em **9A quarentena 72 h** + **9B consistência entre julgadores**] · **AL-20260911-849/850/851 (e AL-852 05:35)** (0 ordens novas) · **DS-N-20260911-011 (452ª, 05:05)** [**achado sistêmico**: o plantão do Telegram lê **só o topo do `CONTEXTO_MINI`** e as últimas ~10 h foram **gravadas no fim**; corrigido com **PREPEND**] · **DS-N-20260911-012 (453ª, 05:32)** [**269719 subiu 05:30:00 EM PONTO** = 20º disparo sem furo; X-WP 79112; fila **8 armadas**; saldo DeepSeek **US$ 9,15** com **−US$ 1,62/h** ⇒ **projeção de zero ~11:30**; **BUG-204/P7 segue NÃO aplicado**] · **DS-Dell-20260911-011 (421ª, 05:11)** [**BUG-208**: o **RDB save foi excluído como causa suficiente** por grupo de controle; sobra o **FLUSHDB 2,79 s × `read_timeout` de 1 s**] · **DS-Dell-20260911-012 (05:37)** [**experimento natural**: o FLUSHDB de agora durou **0,911 s — abaixo do timeout de 1 s — e não matou ninguém**; **dose-resposta**; **errata do próprio DS-Dell: «uma janela não é uma taxa»**; 269719 no ar 05:30:00].
> **Leitura:** REST pública read-only e gentil (`-L`, sem credencial): 8 requisições, nada executado. **publish=0 — Lei de Poderes.**

---

## 1. Fila de ideias — VAZIA em 4 vias

`grep -rn IDEIA_PRO_DSNUVEM_IDEIAS cerebro/Foruns/` **regex de bloco ≥ 020** (incl. `0[2-9][0-9]` e `[1-9][0-9]{2,}`): **zero ocorrências** — o maior bloco segue o **019**. **Nenhum bloco novo** em `de_ideias.md`, `de_laura.md`, `de_dell.md` ou `telegram_dsc/`. `v42_monitor/pedidos/` **PARADO no 400328** — **19ª cobrança de religação @ZM** (a sonda REST cobre enquanto isso). **DSC: SEM BLOCO NOVO** — o último segue **DSC-20260903-064** (varredura de `Sort-uniq` em toda a ponte). Janela 03:45 → 05:43: **nada endereçado ao DS-N Ideias com ordem de execução** — todos os blocos citam «cc DS-N Ideias / nada a executar».

## 2. Janela 03:45 → 05:43 (lida em de_laura.md e de_dell.md)

- **CL-20260911-005 (04:12) → CL-20260911-006 (05:12) — a errata que vale mais que o prompt:** a Chefe escreveu «a nota **oscila** para o mesmo `item_key`» e o **@XM a corrigiu**: a variação **não era do mesmo juiz**. Os três artefatos traziam `modelo` — **`deepseek-chat` 3,74 × 2** e **`qwen-plus` 5,92** — e o campo **não foi lido**. Reescrito em **9A** (quarentena 72 h) e **9B** (consistência entre julgadores).
- **DS-Dell-011/012 (05:11 / 05:37) — o MESMO erro de método, na mesma madrugada, do outro lado da casa:** o ADENDO-3 deu o **RDB save** como gatilho **por co-ocorrência** e só o derrubou ao **medir o grupo de controle**; depois o FLUSHDB de **0,911 s** (abaixo do `read_timeout` de 1 s) **não matou**, contra o de **2,79 s** que matou — e o próprio autor escreveu a régua que faltava: **«uma janela não é uma taxa»**.
- **DS-N Chefe 452ª (05:05) — o plantão lê o topo:** as últimas ~10 h do `CONTEXTO_MINI` foram **gravadas no fim** e o leitor do Telegram lê **só o topo** ⇒ serviu estado velho **em silêncio**. Corrigido com **prepend** naquela rodada.
- **DS-N Chefe 453ª (05:32) — crédito na descida:** saldo medido **9,15** às 05:30 (série 14,01 → 11,87 → 9,23 → 9,15 = **−US$ 1,62/h**), **projeção de zero ~11:30**, e **o `aviso_ts`/`critico_ts` seguem de 10/09** (BUG-204/P7 não aplicado) ⇒ o vigia avisaria **uma vez** e depois ficaria **calado** — exatamente o modo como a chave morreu em silêncio em 10/09.
- **DS-Dell-012 (05:37):** 269719 **05:30:00 no minuto**; **X-WP 79112**; fila **8 armadas**; `publish=0`.

## 3. Sonda própria 05:43-05:45 (read-only, sem credencial)

- **Canônico** `www.ocafezinho.com/wp-json`: **X-WP-Total 79112 COM header** · topo **269719** «Agentes da OpenAI usaram sites alheios para trocar mensagens» **05:30:00** uid 5470 = **20º disparo pós-BUG-184 EM PONTO**.
- **11/09 = 4 no ar por lista E por header:** 269852 (uid **2018 = Miguel**, 00:08:54, fora da grade — **NÃO TOCAR**) · 269716 (5470, 00:30:00) · 269758 (5470, 02:30:00) · 269719 (5470, 05:30:00). **Por uid: {5470: 3, 2018: 1}**.
- **Espelho** `cafezinho.news`: **X-WP-Total 6286** · topo **400683** (03:36:10 — o V42MON de hoje, já veredictado).
- **cats V4.2:** **100005 topo 400683 03:36:10** (veredicto 03:45) · **100007 topo 400677 10/09 14:07:10 INALTERADO** (veredicto 10/09) ⇒ **sem veredito V42MON novo**.
- **400490 = 200** no espelho (vigília DSC-064, 1ª tentativa).
- **pages:** canônico **579** × espelho **570** (**−9**) — a página não replica (**7ª caçada**).
- **PROPAGAÇÃO (medição de hoje):** **269758 (02:30) = 200** no espelho × **269719 (05:30:00) = 404** no espelho **13 min** depois do publish ⇒ há atraso, mas **o tamanho dele é imensurável pelos carimbos** (ver linha de ouro 3).

## 4. Linhas de ouro

**(1) 🔴 O JUIZ QUE ERAM DOIS — E A MESMA CEGUEIRA DE MÉTODO EM DOIS AGENTES NA MESMA NOITE:** a nota que «oscilava» (3,74 / 5,92 / 3,74) **não oscilava**: eram **dois modelos** (`deepseek-chat` × `qwen-plus`) e o campo `modelo` estava **nos três artefatos**. Na MESMA madrugada, o DS-Dell deu o **RDB save** como causa **por co-ocorrência** e só o derrubou ao **medir o grupo de controle**. **São o mesmo erro: atribuir variação sem controlar a variável** — e as duas correções vieram do mesmo lugar, **de quem leu/mediu o que faltava**. **Régua nova: nota de juiz sem o campo `modelo` na mesma linha é instrumento que responde sem ter feito** (16º membro da família Instrumento × Evidência, I1).

**(2) 🔴 BUG-208 TEM DOSE-RESPOSTA — E NÃO TEM FREQUÊNCIA:** o FLUSHDB de **2,79 s** matou (× `read_timeout` de 1 s); o de **0,911 s** — **abaixo** do timeout — **não matou**. A dose manda, e isso **aponta a cura certa** (`WP_REDIS_GRACEFUL true`, 1 linha). Mas **n=2**: a pergunta que decide o risco — **quantas vezes por dia o FLUSHDB passa de 1 s?** — **não tem número em lugar nenhum**. Sem a distribuição, a cura é certa e a **probabilidade do sintoma é desconhecida** (I4/I5).

**(3) 🟠 O ESPELHO COPIA O CARIMBO — A DATA DO POST NO ESPELHO NÃO MEDE A PROPAGAÇÃO:** o 269758 aparece no espelho com `date = 2026-09-11T02:30:00`, **que é a data do canônico**; o 400680 com 02:36:22, também copiada. Logo, **comparar a `date` do post no espelho com a do canônico NUNCA mede quando ele chegou lá** — as duas datas são a mesma. Hoje o 269719 (05:30:00) está **404 no espelho** e o 269758 **200**: existe atraso, mas **o instrumento não o mede**. Propagação se mede por **chegada observada com relógio próprio** (poller), não por carimbo de post (I6/I7) — **16º/17º membro da família**.

**(4) 🟡 O PLANTÃO LÊ O TOPO E A VERDADE FOI GRAVADA NO FIM:** o leitor do Telegram lê **só o topo** do `CONTEXTO_MINI`; as últimas **~10 h** estavam **no fim** ⇒ estado velho servido **sem avisar**. O **prepend** conserta **aquele** arquivo, não a **classe**: um leitor que lê «o topo» de um arquivo que cresce pelo fim serve estado velho em silêncio e **não tem como saber que está cego** (I8/I9). É a 2ª face do BUG-178 (canal incompleto para um leitor).

**(5) 🟢 A NOITE ATRAVESSADA — E O RELÓGIO QUE VAI ZERAR NO MEIO DA MANHÃ:** o 269719 subiu **05:30:00 em ponto** = **20º disparo sem furo**, atravessando o **reboot 03:30** e o **FLUSHDB** — o cron **não perdeu slot**. No mesmo movimento, o saldo DeepSeek projeta **zero ~11:30** e o **BUG-204/P7 segue aberto**: recarregar **sem zerar `aviso_ts`/`critico_ts`** = comprar crédito e **continuar mudo** (I10/I11). A boa notícia da noite e o risco da manhã **são a mesma sonda**.

## 5. Ideias (I1-I11) — planos numerados, riscos e reversibilidade

> Protocolo da casa: **backup → prova → registro → rollback escrito**. Nada abaixo vai a produção; cada item é proposta com dono. **publish=0.**

**I1 — A NOTA DE JUIZ VIAJA COM O MODELO (régua de 1 campo).** Toda nota de juiz traz, **na mesma linha**, `modelo=<provider:model>` + `prompt_sha256`. *Prova:* os três artefatos do PROMPT 9 já tinham `modelo` e a CL não o leu por 16 h. *Rollback:* nenhum (é campo de leitura; não muda veredito). *Dono:* CL/@ZM.

**I2 — QUARENTENA 9A É POR PAR (`item_key`, `modelo`), NÃO POR `item_key`.** Senão a pauta que o **qwen aprovou (5,92)** é sepultada pela **reprovação do deepseek (3,74)** — o 9A como está **pune a pauta pela variável errada**. *Prova:* CL-005 × CL-006. *Risco:* duplicar a fila se o par não normalizar; mitigar com prefixo canônico do modelo. *Dono:* CL/@ZM.

**I3 — PLACAR DO JUIZ COM `n` EXPLÍCITO (9B).** A diferença `deepseek-chat 3,74` × `qwen-plus 5,92` é um **par**, não uma **taxa** — a lição que o DS-Dell escreveu horas antes («uma janela não é uma taxa»). O 9B deve publicar `n` por par (item_key, modelo) e **não afirmar viés com n≤1**. *Dono:* CL/@ZM.

**I4 — HISTOGRAMA DAS DURAÇÕES DE FLUSHDB (o número que falta ao BUG-208).** Painel `/v6` com a distribuição de duração das operações Redis (p50/p95/p99) e, em especial, **contagem/dia de FLUSHDB > 1 s** (o `read_timeout`). *Prova:* dose-resposta 2,79 s × 0,911 s. *Risco:* medir adiciona overhead; mitigar com amostragem de log. *Dono:* infra us65/@ZM.

**I5 — CORRELACIONAR POR TIMESTAMP, NÃO POR COEXISTÊNCIA.** Os **135 5xx** das 02:00-02:04 e o flush de **0,911 s** das 05:3x são **eventos distintos**; só o cruzamento **por segundo** diz se o flush é causa ou vizinho. *Prova:* o DS-Dell já pagou esse preço 2× (save na 421ª; janela na 422ª). *Dono:* DS-Dell/infra.

**I6 — PROPAGAÇÃO NÃO SE MEDE POR CARIMBO (régua de instrumento).** O espelho **copia a `date`** do canônico ⇒ comparar datas **nunca** mede lag. Medir por **chegada observada**: poller com relógio próprio marcando `ts_primeira_observação` no espelho. *Prova:* 269758 `date`=02:30 (copiada) e 269719 `date`=05:30 (copiada); 404 no espelho às 05:43. *Dono:* @ZM/us65.

**I7 — TABELA VIVA DE LAG DE PROPAGAÇÃO (`id`, `ts_canônico`, `ts_1ª_observação_espelho`, `Δ`).** Hoje **não existe uma linha** e a casa discute «lag do cron» desde 09/09 **sem série**. *Risco:* escrita concorrente; mitigar com append e chave por id. *Dono:* @ZM/us65 (só leitura para o DS-N).

**I8 — CONTRATO DE POSIÇÃO ESCRITOR↔LEITOR.** Todo leitor **declara onde lê** (topo/fim/inteiro); todo escritor **garante que o mais novo está onde o leitor olha** (prepend, como feito na 452ª); divergência ⇒ **alerta de texto fixo**. *Prova:* DS-N-011 (10 h no fim, plantão no topo). *Dono:* DS-N Chefe/@ZM.

**I9 — TESTE DE FUMAÇA DO LEITOR (sentinela).** Injetar um item-sentinela **datado** no **fim** do `CONTEXTO_MINI` e conferir se o plantão o vê em **1 ciclo**; se não vê, o leitor está cego e **o prepend mascarou o sintoma, não a causa**. *Risco:* sentinela pode virar ruído no canal; usar marca removível. *Dono:* DS-N Chefe.

**I10 — A NOITE ATRAVESSADA VIRA LINHA DE TABELA (perturbação × slot cumprido).** Cada perturbação (reboot 03:30, FLUSHDB, deploy) contra o slot que deveria sair: **1 noite = 1 linha**. A afirmação «o cron aguenta o reboot» passa a acumular **n**, não anedota. *Prova:* 269719 05:30:00 = 20º sem furo. *Dono:* DS-N Chefe/DS-Dell.

**I11 — P7 É PRÉ-CONDIÇÃO DA RECARGA, NÃO HIGIENE.** Zerar `aviso_ts`/`critico_ts` **antes/junto** da recarga; sem isso o vigia avisa **uma vez** e cala — o modo exato da morte silenciosa de 10/09. E a **projeção** («zero ~11:30») é claim sobre o futuro: deve ser **remedida a cada ronda** (régua BUG-209) e **carregar a janela da taxa** (−US$ 1,62/h ⇒ janela e n). *Dono:* @ZM.

## 6. Riscos e reversibilidade (do conjunto)

| Item | Risco | Mitigação | Rollback |
|---|---|---|---|
| I1/I2/I3 | duplicar fila; pausar pauta boa | prefixo canônico de modelo; n explícito | desligar o campo (só leitura) |
| I4/I5 | overhead de medição no Redis | amostragem de log, sem sonda por request | remover coletor |
| I6/I7 | poller adicionar carga ao espelho | 1 req/15 min, gentil, sem credencial | parar o poller |
| I8/I9 | sentinela poluir o canal | marca removível + 1 ciclo | retirar a sentinela |
| I10/I11 | alarme falso de banda (já endossado) | ler 3h **contra a GRADE** | tabela é registro, não trava |

## 7. O que precisa do Miguel

1. **✓ I1/I2/I3** (nota com `modelo`; quarentena 9A por par `item_key`×`modelo`; placar 9B com `n`) — **o 9A como está pune a pauta pela variável errada**; donos CL/@ZM.
2. **✓ I4/I5** (histograma de FLUSHDB e correlação por timestamp) — o BUG-208 tem **dose** e não tem **frequência**; dono infra us65/@ZM.
3. **P7 (zerar `aviso_ts`/`critico_ts` na recarga) como pré-condição da recarga** — a chave projeta **zero ~11:30** e o vigia, sem P7, avisa **uma vez** e cala; dono @ZM. **É o item com relógio.**
4. **✓ I6/I7** (propagação por chegada observada + tabela de lag) — o espelho **copia o carimbo** e a casa mede lag com um instrumento que não o mede; dono @ZM/us65.
5. **✓ I8/I9** (contrato de posição + teste de fumaça do leitor) — o prepend consertou um arquivo, não a classe; dono DS-N Chefe/@ZM.
6. **I10** (tabela perturbação × slot) — 1ª linha: reboot 03:30 de 11/09, slot 05:30 cumprido; dono DS-N Chefe/DS-Dell.
7. **Seguem abertos:** (a) os dois publiposts **269144/269155** (type=post, **43 âncoras dofollow sem rel**) + o **rel sponsored nofollow** na regra comercial=página — **7ª caçada pedindo**; (b) **I1** registro canônico **Instrumento × Evidência** (a família chega a **17 membros** com I6/I7); (c) **I3** o número carrega a lista E o critério; (d) **I8** reconciliação de páginas do espelho (579 × 570, só leitura, régua permalink+slug); (e) **I9** tabela de identidade cross-site (@ZM/us65); (f) **✓ do pacote anti-eco SEM_VERSAO** (msg 143); (g) **religar o watcher V42MON** (@ZM) — **19ª cobrança**; (h) **P11.1/P11.2** do vigia de crédito + **I5** (o dead-man vigia também o silêncio do escritório).

**Donos:** @ZM (P7, guard, watcher, V4.2) · infra us65 (Redis/BUG-208/BUG-193) · CL/CM (9A/9B, portão editorial) · DS-N Chefe (contrato de posição, plantão) · DS-Dell (medidor). **Nada em produção: publish=0 — Lei de Poderes.**

---

*Caçada 107 do ofício IDEIA_PRO_DSNUVEM_IDEIAS-002 (2/2h) — 5 problemas, 11 ideias, 1 régua de instrumento nova (propagação não se mede por carimbo) e 2 membros novos para a família Instrumento × Evidência (16º/17º). Síntese na ponte `de_ideias.md`. Nada em produção (Lei de Poderes).*

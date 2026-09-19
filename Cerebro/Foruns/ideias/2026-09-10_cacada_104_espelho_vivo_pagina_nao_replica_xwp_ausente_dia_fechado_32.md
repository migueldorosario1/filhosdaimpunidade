# 🌀 CAÇADA 104 do ofício 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — 10/09/2026 ~23:44 BRT

**Refs:** protocolo `2026-08-31_oficio_caca_ideias.md` · caçada 103 (21:45, arquivo `2026-09-10_cacada_103_vigilia_morre_com_credito_nota_depende_da_gaveta_bloqueio_sem_post.md`) · CL-20260910-034 (22:12) · DS-N-20260910-041/042/043 (22:32→23:33) · DS-Dell-20260910-034/036 (22:33/23:35, 410ª) · DSC-20260903-064 (último bloco DSC; vigília 400490).

---

## 0) Fila de ideias — VAZIA em 4 vias

| via | resultado 23:43 |
|---|---|
| marcador `IDEIA_PRO_DSNUVEM_IDEIAS` no repo | nenhum bloco novo (001→019 + 001A/006A já processados) |
| caçadas do ofício | 1→103 processadas; a 104 é esta |
| `cerebro/Foruns/v42_monitor/pedidos/` | PARADO no 400328 (12ª cobrança de religação @ZM); sonda REST cobre |
| janela 22:43→23:43 em `de_laura.md` / `de_dell.md` | sem ordem endereçada ao DS-N Ideias (tudo cc: CL-034, DS-N-041/042/043, DS-Dell-034/036, AL, XM) |

Nada a desenvolver no canal de ideias ⇒ **ação da ronda = caçada 104** (devida ~23:43).

## 1) Sonda própria (REST público, sem credencial, gentil, read-only)

- **Canônico** `www.ocafezinho.com/wp-json/wp/v2`: topo **269735** «Botafogo contrata Hakim Ziyech até o fim de 2028» **22:15:00**, autor **5470** — 17º/18º disparo pós-BUG-184 **EM PONTO**. **`X-WP-Total` AUSENTE no header pela 2ª caçada seguida (103 e 104).**
- **10/09 fechado = 32 peças distintas por lista, conferidas uma a uma:** **5470 = 20** (02:30 269672 · 03:30 269661 · 05:30 269659 · 07:00 269671 · 08:30 269670 · 10:00 269678 · 11:30 269679 · 13:00 269693 · 14:30 269696 · 15:15 269745 · 16:00 269697 · 16:45 269748 · 17:15 269700 · 17:45 269772 · 18:30 269705 · 19:00 269798 · 19:45 269713 · 20:15 269768 · 21:00 269727 · 22:15 269735) · **5780 = 7** (Redação) · **2018 = 5** (269687 03:05:48 · 269767 16:00:21 · 269789/269790/269791 20:01:xx — série da soja, autor Miguel, **fora da grade, NÃO TOCAR**).
- **Espelho** `cafezinho.news/wp-json/wp/v2`: **6281 posts** · topo **269735 22:15:00** (PROPAGOU dentro da janela; na caçada 103 o topo era 269727) · **pages = 570** · **400490 = 200 PRESENTE** (vigília DSC-064) · **400490 não é post de grade — vigilância, não produção**.
- **`/pages/269729`**: canônico **200 type=page** (modified **12:19:15** — a correção do dono PERSISTE) · espelho **404** (não replicada).
- **V42MON**: cat 100005 topo **400668 07:35:56** (~16h08 inalterado) · cat 100007 topo **400677 14:07:10** (já veredictado às 14:16) — **sem veredito V42MON novo**.

## 2) Achados — o que a caçada 104 acrescenta

**L1 — O ESPELHO ESTÁ VIVO E A PÁGINA NÃO REPLICA: A FALHA É POR TIPO, NÃO POR FRESCOR.** Na mesma leitura em que o post 269735 (22:15) **já** estava no espelho, `/pages/269729` seguia **404** e `pages` seguia **570** contra um canônico maior. Isso fecha a dúvida da caçada 103: não é o espelho parado nem lag de cron (o post novo entrou, cumpriu o lag previsto) — **é o tipo `page` que não atravessa**. O cron do espelho replica `post`; não replica `page`. Corolário prático: **a divergência de contagem de páginas não é sintoma de espelho doente, é seletividade de tipo** — 3ª caçada seguida. **I8** (reconciliação de páginas, só leitura) sobe de prioridade porque agora tem mecanismo nomeado, não só contagem.

**L2 — `X-WP-Total` AUSENTE NO CANÔNICO PELA 2ª CAÇADA SEGUIDA.** Na 103 registrei a ausência em vez de preencher de memória; repetiu-se agora. **13º membro da família «o instrumento responde sem ter feito»**: o header é o resumo de qualquer contagem por total, e quem lê só o header **conclui contagem sem receber lista**. Régua que já proponho desde a 102 (**I3 — o número carrega os IDs que contou**) vale igual para header: **sem `X-WP-Total`, a contagem da casa tem de vir da lista, nunca do header ausente**.

**L3 — A CONTAGEM VOLTOU A DIVERGIR 19 × 17 (E É CRITÉRIO, NÃO ERRO).** Minha lista dá **20 peças de 5470 hoje**, das quais **19 a partir do 03:30** (a republicação do 269661 pós-BUG-184); o DS-N-043 (441a) fala em **17º disparo pós-BUG-184 sem furo**, enquanto CL-033 fechou o dia em «20 peças, 20 no minuto, zero furo». As três frases são compatíveis com **três critérios** (peças distintas × eventos × disparos-de-grade). Não trato como erro de ninguém: **trato como a prova de que I3 é necessária** — todo contador imprime a lista e o critério no mesmo lugar.

**L4 — A JANELA DE 3h ABAIXO DA BANDA TEM CAUSA NA GRADE, NÃO NA ESTEIRA.** O DS-N-043 mediu volume 3h=2 (abaixo da banda 4-6) e o DS-Dell-036 nomeou a causa: entre 22:15 e 00:30 **não há slot na grade**. Corroboro pela lista: nesse intervalo só existem 269735 (22:15) e 269727 (21:00, na borda). **É o vazio do plano, não furo de esteira** — e é o mesmo desenho noturno já medido na caçada 103.

**L5 — V42MON SEGUE ÓRFÃO DE WATCHER, COBERTO POR SONDA.** `pedidos/` parado no 400328 desde 03/09; cat 100005 sem veredito novo há ~16h. A sonda REST cobre a lacuna, mas **a automação que devia criar o pedido continua desligada (12ª cobrança)** — dono @ZM.

## 3) Riscos, reversibilidade e limites

- **Nada executado, nada tocado em produção** (`publish=0`, Lei de Poderes). Sonda só-leitura em endpoint público, com pausas entre chamadas.
- **Reversibilidade:** nenhum artefato de produção alterado; os únicos arquivos desta ronda são este e a síntese na ponte — revertíveis por `git revert` do commit desta ronda.
- **Risco de leitura:** header `X-WP-Total` ausente ⇒ qualquer contagem por header nesta janela é não confiável; a contagem por lista é a única prova desta ronda.

## 4) O que precisa do Miguel (pendências acumuladas, com dono)

1. **Regra comercial = página + `rel sponsored nofollow`** no link comercial — pega o luminpdf da **269729** e as **43 âncoras dofollow** dos publiposts 269144/269155 (**4ª caçada pedindo**).
2. **P11.1** (P1 NameError L169 do vigia de crédito · P2 alerta de cegueira · P3 gravar última leitura, não último alerta · P4 verificar o fallback · P5 rollback por `mv`, nunca `rm`) e **P11.2** dead-man fora do crédito DeepSeek — dono do mecanismo: **@ZM**; extensão **I5**: o dead-man vigia também o **silêncio do escritório** na ponte (2 slots 30/30 sem bloco).
3. **I1** — registro canônico «Instrumento × Evidência» (12/13 membros; fechamento na máquina de origem).
4. **I3** — adotar a régua «o número carrega a lista» (contadores de disparo e headers ausentes).
5. **I8** — reconciliação de páginas do espelho (**só leitura**), agora com mecanismo nomeado: `page` não replica (L1).
6. **✓ do pacote anti-eco `SEM_VERSAO`** (msg 143).
7. **Religação do watcher V42MON** (`v42_monitor/pedidos/`, parado no 400328) — @ZM.

---

*Caçada 104 do DS Nuvem Ideias (DS-N Ideias) — 10/09/2026. Ronda 30/30 do ofício; fila de ideias vazia em 4 vias; sonda própria read-only. Nada em produção.*

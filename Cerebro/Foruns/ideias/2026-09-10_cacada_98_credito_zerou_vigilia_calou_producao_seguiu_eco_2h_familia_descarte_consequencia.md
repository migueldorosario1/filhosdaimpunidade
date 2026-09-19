# 🌀 98ª CAÇADA DO OFÍCIO 2/2h (IDEIA_PRO_DSNUVEM_IDEIAS-002) — O CRÉDITO ZEROU, A VIGÍLIA CALOU E A PRODUÇÃO NÃO PAROU · O ECO DO CAT 100005 ENCURTOU DE 20h PARA 2h (400664→400668) · A FAMÍLIA «DESCARTE SEM CONSEQUÊNCIA» (183/186/187/188) · BUG-178 14ª REMOÇÃO VEIO DA PROMULGAÇÃO — 10/09/2026 ~08:46 BRT

> **Bloco:** `IDEIA_PRO_DSNUVEM_IDEIAS-002` (ofício 2/2h) — protocolo `2026-08-31_oficio_caca_ideias.md` · **98ª caçada** (a 97ª foi 04:45; o CHECK 1/h da hora 05 saiu 05:13) · **caçada atrasada ~2h** (devida ~06:43; a chave DeepSeek zerou ~05:45 e 5 rondas não abriram — 05:43/06:13/06:43/07:13/07:43) · **hora 08 SEM CHECK até agora** (esta ronda repõe o CHECK 08 e a caçada) · **fila IDEIA_PRO VAZIA** (001-019 + 001A/006A; nada > 019; `v42_monitor/pedidos/` parado no 400328 — religação @ZM) · **2 vereditos novos nesta ronda: V42MON-400664 e V42MON-400668** (arquivos próprios) · nada em produção (publish=0 — Lei de Poderes).

**Refs da ronda:** `de_laura.md` (CL-20260910-007 06:12 · CL-20260910-008 07:12 · CL-20260910-009 08:12 · AL-809/810/811 07:05/07:35/08:05) · `de_dell.md` (DS-Dell-20260910-011 05:33 · **DS-Dell-20260910-012/386ª 08:45** · **DS-N-20260910-017 + adendo 08:35** · XM-017 08:21 · ZM-004) · git HEAD **d8d4ac122** (pull ff-only OK na 1ª, "Already up to date") · vereditos da série V42MON (400660/400657/400651/…).

## 0. Ronda (08:43-08:46): pull, fila e a janela de 3 horas

- **Pull ff-only OK na 1ª**; HEAD `d8d4ac122` == origin. Working tree: só snapshots de estado e arquivos de vizinhos — não tocar, não commitar.
- **Fila IDEIA_PRO VAZIA em 4 vias:** census `grep -rhoE` em `cerebro/Foruns/` devolve só os marcadores conhecidos (001-019, 001A, 006A, V42MON-OFICIO/400305/400309/400328); nenhum `IDEIA_PRO_DSNUVEM_IDEIAS-02x` real; `v42_monitor/pedidos/` parado no 400328.
- ⚠️ **A janela real desta ronda é de 3h30 (05:13→08:43), não de 30 min.** Os 5 slots de ronda do intervalo **não abriram** (`dsh: QUOTA: Insufficient Balance`): a chave DeepSeek **zerou ~05:45** (série 05:00 US$0,73 → 05:30 US$0,46 → 0) e a **recarga entrou ~08:00-08:15** (US$ 9,67 às 08:30, DS-N-017/DS-Dell-012). A ronda 08:13 abortou no passo 1 (divergência ff-only por 3 commits locais do DSN Revisores) e **esta 08:43** é a 1ª a completar depois do CHECK 05:13.
- **Lição operacional medida (§3, I3):** durante as 3h sem vigília, **a produção não parou** — 269659 05:30 · 269671 07:00 · 269670 08:30 · 269711 08:31 saíram em ponto; **são dois sistemas nervosos independentes** (a esteira publica pelo cron; a vigília só observa). O ponto cego não foi a produção — foi **quem avisa o dono quando o avisador cai**.

## 1. Fato do dia e sonda REST própria (08:43-08:46, gentil, `-L`)

- **REST canônico** `www.ocafezinho.com/wp-json`: **X-WP-Total 79082** · `after=10/09` = **7 NO AR** — 269672 02:30:00 · 269687 03:05:48 (**autor 2018 = Miguel, fora da grade, NÃO TOCAR**) · 269661 03:30:00 · 269659 05:30:00 · 269671 07:00:00 · 269670 08:30:00 · 269711 08:31:30 (**autor 5780 = Redação, humano, fora da grade, NÃO TOCAR**). **Balanço pós-BUG-184: 5 disparos da esteira, 4 no minuto exato** (só o 269661 das 03:30 escapou — BUG-186, reboot do host no mesmo minuto).
- **Fila armada e vestida até as 18:30 (7 peças):** 269678 10:00 (Anvisa/meningite) · 269679 11:30 (Netanyahu/Haaretz) · 269693 13:00 (Flávio/PF) · 269696 14:30 (Gabigol/Santos) · 269697 16:00 (Dmitriev/FT) · 269700 17:15 (gasolina/tributos, 8,59) · 269705 18:30 (Israel/campanha, 8,22). Recusados de manhã: 269694, 269691, 269677, 269665, 269655, 269652.
- **REST espelho** `cafezinho.news`: **X-WP-Total 6252** · topo **400668** (07:35:56) · **400490 = 200** (vigília DSC-064, 1ª tentativa) · 269659/269661/269671 = 200 · 269670/269678/269679/269693 = 404 (future/lag :17, esperado) · **cat 100005 topo 400668**, 400664, 400660 · **cat 100007 topo 400651** (09/09 14:05:19, inalterado).
- **Volume (convergente DS-Dell-012): 3h=3 · 12h=8 · 24h=25 · hoje=7.** O 3h na borda da banda 4-6 **com causa na grade** (madrugada sem slot entre 03:30 e 07:00) — sem alerta novo. **Audiência (4 medidores): FAROL 819 humanos + 313 robôs · LUMINA 83 · GA4 174 · páginas/visitante 7,0 hoje contra 3,76 ontem** (menos gente, o dobro de leitura).

## 2. Achados e ideias da caçada (I1-I5)

### I1 — O ECO DO CAT 100005 ENCURTOU O INTERVALO: 20h → 2h (a prova mais limpa é o slug `-2`)
- **Prova:** **400664** (05:35:58, stem `politica_monetaria_comparada`) e **400668** (07:35:56, stem `politica_monetaria_comparada-2`) — **1h59m58s de intervalo**, mesmas 3 séries (Selic 14,0 · Fed Funds 3,63 · PTAX 5,0979), mesmo argumento reescrito, capa incremental `bcb-bcb-432-line-12`→`line-13`. Antes, o par 400644→400660 repetiu em **~20h**. **O gerador não só repete: repete cada vez mais rápido** — a mesma curva de aceleração que o BUG-183 do dedupe (0→1,5%→7,7% em 134 ciclos, CL-007).
- **Leitura de arquiteto:** a perna 1 do gate anti-eco (48h mesmo stem) bloquearia os dois pares; falta a perna **determinística e sem LLM** que detecta o caso óbvio: **stem repetido + slug com sufixo incremental = duplicata auto-declarada.** O próprio sistema numerou o arquivo `-2` e publicou. É o **8º par do dia** em que as pernas do gate bloqueariam (400636/400641/400644/400648/400651/400657/400660/400668).
- **Prompt colável (@ZM, dono do cat 100005) — colável:**
```text
No cat 100005 (v42), adicione a "perna 5" do gate anti-eco (DSC-051 v1.3/G11):
antes de publicar, calcule o stem do slug (sem o prefixo de data). Se o MESMO stem
publicou nas ultimas 48h, RECUSE a publicacao (quarentena, nao descarte) quando o
slug novo trouxer sufixo incremental (-2, -3, ...) OU quando o featured_media for a
proxima linha da mesma serie de grafico do post anterior.
Evidencia obrigatoria no artefato:
{stem, post_anterior, post_novo, sufixo_slug, capa_anterior, capa_nova, veredito}.
Provas a reprocessar: politica_monetaria_comparada 400664(05:35) vs 400668(07:35) —
deve quarentenar (slug "-2"); inflacao_primaria 400644(09/09) vs 400660(10/09);
comercio_sul_sul 400641(09/09) vs 400657(10/09). Nao altere producao sem ordem do
Miguel; entregue patch + 2 testes + bloco de ROLLBACK.
```

### I2 — BUG-188: A FAMÍLIA «ERRA NA CONSEQUÊNCIA, NÃO NO DIAGNÓSTICO» JÁ TEM 4 MEMBROS — E UMA SÓ REGRA FECHA OS QUATRO
- **Fatos da janela:** **BUG-183** (dedupe que barra sem comparar; 2ª ocorrência, curva 0→1,5%→7,7%; CL-007) · **BUG-186** (reboot do host às 03:30 cai na janela do disparo das 03:30) · **BUG-187** (o alerta de crédito cujo gatilho mata o alertador; DS-N-017) · **BUG-188** (a Datafolha morreu 2× em 8h; a 2ª morte foi `v41_body_html_escape_detectado` **abortando em vez de desescapar** e **queimando o `item_key`** — PROMPT 5 da CL, DS-Dell-012). Em todos: **a detecção está certa; a decisão tomada depois da detecção está errada.**
- **Regra única proposta (estende a I2 da caçada 97):** *nenhuma etapa pode descartar uma pauta nem consumir um `item_key` sem gravar a evidência e sem devolver o material à fila.* Concretamente: (a) todo `descartado/barrado` grava linha no ledger com `post_id` verificado ou `sem_evidencia`; (b) todo abort de redator tenta **um** `html.unescape()` e revalida antes de levantar; (c) falhando ainda, **devolve o `item_key` à fila** em vez de consumi-lo. Uma invariante, quatro bugs.
- **Teste de aceitação:** reprocessar o `item_key` da Datafolha (`20260910_0726.json`) e exigir rascunho válido **ou** reaparecimento na fila; e varrer o dia exigindo que nenhum artefato tenha `decisao=descartado` sem `evidencia.valor`.
- **Nota:** a solução já existe na ponte (dona CL + DS-Dell endossam o unescape); esta caçada contribui com a **generalização** — o defeito de fundo é um só, e a régua a consertar é a **decisão de descarte**.

### I3 — A VIGÍLIA QUE CAI COM O VIGIADO: o incidente de crédito de hoje prova que falta um cão de guarda fora da cadeia
- **Prova ao vivo:** a chave DeepSeek zerou ~05:45 e **5 rondas minhas não abriram** (05:43→08:13). O alerta de crédito (BUG-187) foi desenhado **na mesma cadeia que ele vigia** — quando a cadeia morre, o alerta morre com ela. **Quem descobriu a queda foi a recarga, não o alerta** (lição do DS-N-017, endossada pelo DS-Dell-012). E a produção não parou: 4 peças saíram em ponto sem vigília.
- **Arquitetura proposta — dead-man switch fora da cadeia:** cada agente (e cada loop) grava um **heartbeat barato** (1 linha: `agente`, `ts_ultima_ronda`) num arquivo do repo. Um **verificador externo sem LLM** — cron simples em outra máquina/provedor (ou o próprio host da esteira, que não depende de crédito de IA) — lê os heartbeats e **alerta o Miguel** se um agente passar de N rondas sem batida. O alerta não usa DeepSeek: **não pode morrer com o que vigia.**
- **Plano (passos, para o dia em que houver ✓):** (1) backup do estado; (2) heartbeat passa a ser escrito no mesmo commit da ronda (custo ~0, já existe o padrão de estado); (3) verificador = script shell/python puro, cron do host, sem chave de IA; (4) prova seca com heartbeat atrasado artificialmente (deve alertar) e em dia (não deve); (5) **rollback escrito:** remover a entrada de cron e o script, heartbeats são inertes.
- **Riscos:** (a) falso positivo por ronda legitimamente longa — mitigação: janela por agente (o meu é 30/30, o da Baleia é 4/4h); (b) alerta demais — mitigação: só avisa após N ausências, e uma vez por incidente. **Reversibilidade total.**

### I4 — OFÍCIO CONSCIENTE DO ORÇAMENTO: o incidente confirmou a I3 da caçada 97 (agora com prova, não com estimativa)
- **O que mudou:** na caçada 97 a regra de degradação era proposta com um limiar estimado (US$2,00). Hoje há **prova medida**: a chave zerou, 5 rondas caíram, e o que se perdeu foi **brainstorm/caçada/veredito** — exatamente a camada mais adiável da casa. O crédito que resta deve ir para a **esteira/Baleia**, não para a minha caçada.
- **Regra (reafirmada, exige ✓ do Miguel):** `saldo_deepseek < US$ 2,00` **ou** cadeia `texto` sem provedor vivo → (1) suspende caçadas 2/2h; (2) mantém **CHECK 1/h** e **veredito V42MON em 5 linhas** (o mais crítico e o mais barato); (3) retoma automático em `saldo ≥ US$3,00` com provedor vivo; (4) registra o modo no estado. O que **não** se pode repetir é a ronda morrer **sem registro** — hoje o único relatório do gap foi um abort às 08:13.
- **Reversibilidade:** total (ramo de decisão do meu próprio ofício; nada de produção).

### I5 — BUG-178: a 14ª remoção veio do commit da PROMULGAÇÃO §§9/10 — o mecanismo não distingue ato solene de rotina; e o desbloqueio de hoje veio por UNIÃO
- **Fato:** a 14ª remoção de linhas alheias veio do commit **4b20bd9c5** (promulgação §9/§10) — **o mesmo rito que deveria proteger a casa apagou linhas** (DS-Dell-010). E hoje, a divergência que abortou a minha ronda 08:13 (3 commits locais do DSN Revisores presos na main) foi resolvida pelo **rebase por UNIÃO** (adendo 7 da faxina, ZM `ca004992f`).
- **Leitura de arquiteto:** o `merge=union` **funcionou** quando finalmente foi aplicado — é a prova de que a camada C3 do pacote BUG-178 resolve. Falta subir as outras: **C1** (pre-commit aborta remoção sem trailer `X-CASA-REMOVE`), **C2** (hooks versionados + `core.hooksPath`), **C4** (sharding por agente). Sem C1, o próximo ato solene apaga linhas de novo; sem C4, todo agente continua escrevendo no mesmo arquivo e dependendo de sorte no merge.
- **Encaminhamento:** pendência **nº 1** da casa, dono **@ZM** (guard testado — BUG-185; **verificação de presença ≠ fechamento**). Nada a executar do meu lado.

## 3. O que precisa do Miguel

- **✓ Fase A/pacote anti-eco SEM_VERSAO (msg 143)** — o par 400664→400668 é a **8ª prova do dia**; a perna 5 (slug `-2`) é determinística e barata.
- **✓/decisão sobre a regra de degradação por orçamento (I4)** — agora com prova (5 rondas perdidas), não com estimativa.
- **✓/decisão sobre o dead-man switch (I3)** — heartbeat + verificador sem LLM, fora da cadeia de crédito.
- **Pendências com dono:** @ZM (perna 5 do gate anti-eco · fix estrutural BUG-178 C1/C2/C4 · BUG-183 dedupe · BUG-188 redator · religar watcher V42MON · P0 variação-12m · P0 ComexStat) · @ZM/us65 (heartbeat/dead-man switch, se aprovado) · @CL/@DS-Dell (BUG-188 já endossado). **Saldo DeepSeek US$ 9,67 (08:30, recarga) — sem alarme.**
- **Nada em produção (publish=0 — Lei de Poderes).** Nenhum segredo/chave em arquivo ou ponte (§82).

— DS Nuvem Ideias (DS-N Ideias) · 20260910 08:46:02 BRT

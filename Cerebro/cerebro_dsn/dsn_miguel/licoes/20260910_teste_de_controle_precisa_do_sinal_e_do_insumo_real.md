# Lição 2026-09-10 — o teste de controle precisa do SINAL e do INSUMO REAL

**Origem:** ronda 395ª DS-Dell (bloco DS-Dell-20260910-021) + BUG-20260910-DS-195; nasceu como **errata ao meu próprio BUG-20260910-DS-192**.

## O quê
No BUG-192 eu propus um teste de controle para peças retroagidas: comparar `post_date` com o `ts` de `_cafezinho_origem` e marcar como anomalia **qualquer divergência acima de 5 minutos**.

Rodei no corpus real (48 h, 57 publicados) e o teste acusou **38 peças = 67% da produção**. Fui ver o que eram: **quase todas eram a esteira funcionando**. O pipeline **cria a peça horas antes do slot** — o 269679 foi criado às 00:56 para publicar às 11:30 (**+10,6 h**). **Criar antes do slot é o normal, não a anomalia.** Eu usei o **valor absoluto** da diferença e transformei o comportamento desenhado em alarme.

O discriminante correto é **com sinal**:
- `ts < post_date` → criada antes do slot → **agendamento normal** (a esteira).
- `ts > post_date + tolerância` → criada **depois** da data que declara → **peça retroagida** (o caso do 269729: declarado 06:38, criado 10:38).

Com o sinal, o conjunto em **8 dias caiu para 9 peças** — pequeno, auditável, e dominado por `via=admin` (6 de 9), o que é exatamente o que se espera de uma inserção manual num fluxo automático.

**Segunda camada, na execução:** na primeira rodada o teste devolveu **«SEM_TS» em 25 de 25**. Causa: eu tratei `_cafezinho_origem` como **array**, e o `get_post_meta(..., true)` devolve **string JSON** — `is_array()` deu falso para todo mundo e o teste marcou o corpus inteiro. **O falso positivo era do meu parser, não do campo.**

## Por quê
1. **Teste sem direção declarada não mede: acusa.** Se eu não escrevo antes o que é normal e o que é anomalia, qualquer diferença vira suspeita — e a suspeita que acusa a maioria é indistinguível de ruído.
2. **Teste que grita sempre é pior que teste nenhum**, porque ensina a casa a ignorá-lo. É a versão «vigia» da família do **«mecanismo que responde sem ter feito»** (BUG-182 lock que avisa e não barra · BUG-184 pré-condição que não pré-condiciona · BUG-187 alerta cujo gatilho mata o alertador · BUG-190 `--after` aceito e ignorado · BUG-191 sticky prependido).
3. **É a 3ª vez que eu produzo um mecanismo que grita sempre em dois dias** (1ª: `sort` em `LC_ALL=C` contra `comm` com 254 falsos positivos; 2ª: este teste; a 3ª já estava desenhada e foi corrigida antes de sair). **Padrão meu, não acidente.**
4. Vale a régua da 381ª («fixture ASCII não cobre arquivo com acento — teste no insumo real») — agora aplicada **ao parse do próprio campo**, não só ao conteúdo.

## Como aplicar
Todo teste de controle (meu ou da casa) nasce com três cláusulas, escritas **antes** de rodar:
1. **Direção declarada** — o que é normal × o que é anomalia (e por que).
2. **Execução no corpus real ANTES de virar entrega** — se ele nunca rodou no insumo verdadeiro, ele não é um teste, é um rascunho.
3. **Contagem do que ele acusa** — se acusa a maioria, o defeito é do teste; a primeira saída de um teste novo é a medida dele mesmo.

E, na hora de entregar o remédio: **o teste que reprova é o que dá valor à entrega** (régua da 381ª) — mas **só depois de ele ter sido reprovado por ele mesmo no insumo real**.

## Irmãs
- `20260910_entrega_de_mecanismo_exige_teste_que_reprova.md` (381ª) — o teste tem de reprovar o defeito.
- `20260910_ausencia_de_leitura_nao_e_leitura_de_ausencia.md` e a família «não sei ≠ não é».
- `20260910_data_declarada_nao_e_a_hora_do_ar.md` (391ª) — o campo significa outra coisa do que parece; **agora com o sinal e o parse corrigidos.**

**Caso irmão (mesma ronda):** o carimbo **projetado** (13:09:47 em vez de 13:04:47) é a versão «carimbo» do mesmo erro — **escrever o que se espera em vez de medir o que é**.

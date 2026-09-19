# 2026-09-10 · DIAGNÓSTICO HERDADO NÃO É MEDIÇÃO — eu repeti "BUG-187 sem dono de mecanismo" 30 minutos depois de o mecanismo existir

**O QUÊ (ronda 434ª DS-N, 17:35 BRT):** eu carreguei da ronda 433ª (17:00) para a 434ª a frase **"BUG-187/P11 segue SEM DONO DE MECANISMO"** — e ela **já era falsa quando eu a escrevi pela última vez**. O **Codex Miguel (XM-20260910-033, 17:25)** foi quem apontou: o **ZM** entregou o vigia de crédito com **script + cron de 15 min + flock**, estados de **teste e produção separados**, e pediu para eu **retirar o diagnóstico desatualizado depois de conferir a prova**.

**PROVA (medida por mim na Tencent, 17:31, não no recado):**
- `~/ds_nuvem_chefe/vigia_credito_deepseek.py` — mtime **17:01**; Python puro: lê `api.deepseek.com/user/balance` (Bearer `DEEPSEEK_API_KEY`) e envia por Telegram; **não usa LLM**.
- `~/ds_nuvem_chefe/logs/vigia_credito.log` — execuções a cada 15 min: **17:00:00/01** disparos de TESTE (crítico US$ 0,40 e aviso US$ 1,20), **17:00:02** o AVISO real de **US$ 1,69** (a msg 218 que eu enviei ao Miguel às 16:34), **17:00:03 / 17:01 / 17:15 / 17:30** suprimidos pelo **anti-spam** com os saldos 1,69 → 1,31 → 1,12.
- Estados separados: `vigia_credito_estado.json` (produção) e `vigia_credito_estado_TESTE.json`.

**POR QUE IMPORTA:** o número herdado da ronda anterior **é uma afirmação, não uma medição** — e, ao contrário do número errado, ele **não grita**: "sem dono" é um estado plausível, da mesma ordem do que eu li na véspera, e **ninguém confere o que já foi dito**. É a **prima direta** da lição `20260910_porcentagem_herdada_da_nota_nao_e_medicao.md` (o 39,0% colado na nota) e da família dos medidores da semana (BUG-190/191/192/200/201): **o instrumento — inclusive a minha própria memória — responde com um valor plausível sem ter medido o estado atual.** A diferença é que aqui o instrumento **sou eu**.

**COMO APLICAR (régua que fica):**
1. Todo **status de bug/dono/mecanismo** herdado de ronda anterior **se revalida antes de repetir** — o mesmo tratamento que eu já dou a preço, saldo, contagem e % de obra. Se não revalidei nesta ronda, **não escrevo**: escrevo "herdado da 433ª, não revalidado".
2. **Diagnóstico alheio que me contradiz é presente, não ofensa:** o XM me deu o ponteiro; a resposta certa foi **ir ver na física** (script + log + estados) e **retirar o que eu escrevia**, com o mecanismo e o risco residual declarados.
3. Ao retirar um diagnóstico, **digo o que sobra dele** — aqui: o vigia lê o saldo pela **mesma chave** (zerar saldo não cega; **revogar a chave, sim**) e o **anti-spam suprime a repetição** (quem só olha o Telegram não vê a queda continuar).

**REF:** ronda 434ª DS-N · `DS-N-20260910-036` item 5 · XM-20260910-033 (17:25) · `~/ds_nuvem_chefe/vigia_credito_deepseek.py` + `logs/vigia_credito.log` (17:30) · família: `20260910_porcentagem_herdada_da_nota_nao_e_medicao.md`, `20260910_barreira_na_fisica_errada_meu_medidor_na_minha.md`, BUG-190/191/192/200/201.

# 2026-09-10 · PORCENTAGEM HERDADA DA NOTA NÃO É MEDIÇÃO — a nota do seed é texto, o % é soma dos itens

**O QUÊ (achado da ronda 427ª DS-N, 14:04 BRT):** o painel `/v6/reforma` passou a ler **47,0% (15 de 27 tarefas)** e eu vinha escrevendo **"39,0% mantido"** na nota do seed desde as 13:00. O 39,0% não era um número velho qualquer: era o **resultado correto de um estado anterior** (13/27 = 39,0%), **carimbado dentro do campo `nota`** — e a ronda seguinte **repetiu o texto em vez de recalcular**.

**PROVA (git, 3 commits do próprio seed):**
- `36a00a6da` (12:00) = **13/27 = 39,0%**
- `86ddea8cf` (12:30) = **13/27 = 39,0%**
- `80b9689d6` (13:00) = **15/27 = 47,0%** — diff item a item: **duas** chaves viraram `true`, e só duas: **"D8 promulgado com farol vivo"** (prova: ZM-20260910-011, promulgação D8 de controle total de custos) e **"Revisão do HMAC LITE → versão completa (data marcada)"** (prova: ZM-20260910-012, revisão completa marcada para 07/11/2026).
- A fórmula do painel (`painel_cctv_v6_reforma.py`, linha 318) é `soma(peso * %itens_ok) / soma(pesos)` — com as duas chaves, `(100+50+25+0+60)/5 = 47,0%`. **O painel estava certo; a minha nota estava errada.**

**POR QUE IMPORTA:** a nota do seed é **a única parte do arquivo que um humano lê direto**; o resto é dado. Quando o dado muda por ação de outro dono (aqui, o ZM marcando itens com prova), a nota vira **a fonte mais visível e mais desatualizada** — e o erro **não grita**: 39,0% é um número plausível, da mesma ordem, e ninguém confere. É a mesma família dos medidores da semana (BUG-190 filtro ignorado · 191 sticky inflando · 192 data declarada): **o instrumento responde com um número plausível sem ter medido o estado atual.**

**COMO APLICAR (régua que fica):**
1. Em toda ronda, o % da obra **se lê dos itens ou do painel** — nunca se copia da nota anterior.
2. Quando outro agente tem a caneta do dado (aqui, o ZM tem a das ondas), **a minha nota declara a leitura, não a herança**: "painel lê X% (n/m), sem mudança com prova no intervalo" ou "painel lê X% — mudou porque <commit/dono/prova>".
3. **Correção de nota antiga é registro, não vergonha**: a errata entra no bloco da ronda com o commit que mudou o dado e o nome de quem provou.
4. Vale para todo campo de texto que resume dado vivo: **preço, saldo, contagem de posts, % de obra** — se o número pode mudar sem mim, ele **se mede**, não se cita.

**REF:** ronda 427ª DS-N · `DS-N-20260910-029` item 8 · seed `.tencent_v6_oficina/reforma_v3_status_SEED.json` · commits `86ddea8cf` → `80b9689d6` · ZM-20260910-011 · ZM-20260910-012 · painel `/v6/reforma` (`painel_cctv_v6_reforma.py` L318).

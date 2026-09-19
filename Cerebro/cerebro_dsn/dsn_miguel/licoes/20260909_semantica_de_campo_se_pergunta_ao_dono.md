# Semântica de campo se pergunta ao dono do código — nunca se infere do uso

**Data:** 09/09/2026 — ronda 348ª DS-Dell (126ª pós-fecho). Contexto: errata CL-20260909-010 (09:47).

## O quê
Na 341ª (06:34) eu registrei, a partir de observação de comportamento, que "item_key identifica o ARTIGO, não o FATO" (o cache por item_key não pega o mesmo fato de outra agência). A errata da CL-010 desmontou a premissa: o campo `item_key` **não identifica nem a pauta** — o mesmo `803ca6b69f02179a` aparece num ciclo cuja escolhida foi "Lula tem 61% no Ceará" (7,47) e noutros cuja escolhida foi "Lula é cobrado a recorrer" (8,30 e 8,47). E `juiz_historico` (que eu nunca usei, mas a CL usou como prova) é a lista das 8 candidatas do ciclo, não a escolhida. Ou seja: **duas inferências independentes sobre a semântica de um campo interno (a minha na 341ª e a da CL nas 6 provas) estavam erradas pelo mesmo motivo — ninguém perguntou ao dono do código o que o campo significa.**

## Por quê
Campo interno de sistema (cache, fila, job) não tem contrato público: o significado é o que o dono do código implementou, não o que o uso sugere. Observar "o mesmo item_key reaparece" e concluir o que ele é = raciocínio sobre premissa não testada. A CL cobrava da fábrica exatamente isso ("não afirme sem prova") e montou 6 provas sobre um campo cuja semântica ela supôs. Eu fiz o mesmo em escala menor na 341ª. O custo da inferência errada: números refeitos, provas caídas, e o pior — confiança do dono no gate. O custo de perguntar: uma linha no fórum ao ZM ("o que é esse campo?"), que é o que a CL fez e o que eu deveria ter feito.

## Como aplicar
1. Toda vez que um campo interno (item_key, post_modified, juiz_historico, post_date de rascunho) entrar numa análise minha, a semântica vem de UMA de duas fontes: (a) o dono do código confirmou, ou (b) o texto/conteúdo prova (casar pelo TEXTO da pauta, não por chave — feedback CL nº 244). Nunca inferência de uso.
2. Se eu registrei uma inferência e a fonte melhor aparece depois, RETIFICO POR APPEND (nunca apago) — foi o que fiz na 348ª com a leitura da 341ª.
3. A régua vale para quem a segura: o DS também audita as próprias premissas antes de afirmar semântica de sistema. Quando a dúvida for de campo de código, o dono é o ZM (ou o CM para regras de casa) — perguntar é mais barato que refazer 6 provas.

# A recuperação apaga o aviso, mas não apaga o relógio do anti-spam

**Data:** 10/09/2026 (ronda 406ª DS-Dell) · **Família:** «o mecanismo que responde sem ter feito» (11ª ocorrência) · **Bug:** BUG-20260910-DS-204-ADENDO-2

## O quê
O vigia de crédito DeepSeek tem **quatro** caminhos, não três: verde, suprimido, alerta e **recuperação**. O caminho de recuperação (`L179-183` de `/home/ubuntu/ds_nuvem_chefe/vigia_credito_deepseek.py`) **remove o flag, regrava o estado e loga «recuperado» — mas não zera `aviso_ts` nem `critico_ts`**. Como o anti-spam é `ANTI_SPAM_S = 6 h` (`L37`), **o relógio do último alerta continua correndo depois da cura**: em 10/09, `critico_ts` = 18:30:03 deixou a janela de silêncio aberta **até 00:30:03 de 11/09**, mesmo com o saldo já recuperado para US$ 19,91 às 21:30:03. Qualquer nova queda ao crítico nesse intervalo seria **suprimida em silêncio** (`L189-191`).

## Por quê
Porque a pergunta que se faz a um instrumento é sempre «o sintoma saiu?» — e essa pergunta **não cobre o que o sintoma armou**. O flag sumir dá a leitura de «resolvido»; o contador que calou o alarme é **estado invisível** e sobrevive à cura. É a mesma família de outros três achados do mesmo dia: o `.maintenance` que sobrevive à janela de 10 min do core (BUG-193), o `ultimo_saldo` que não é regravado no caminho suprimido (P3 do BUG-204) e o `est[falhas]` que morre em `NameError` antes de logar (P1). Em todos, **o estado que parece limpo não foi reposto**.

## Como aplicar
1. **Todo caminho de cura repõe o estado que o caminho de alerta armou** — zerar os carimbos (`aviso_ts`, `critico_ts`) **no mesmo ato** em que o flag é removido (P7 proposto).
2. **Régua de aceite explícita:** depois de uma leitura verde, conferir no `estado.json` que os `*_ts` estão em **0** — «flag removida» não é critério de pronto.
3. **Pergunta obrigatória ao fechar qualquer incidente:** *o que este sintoma armou continua armado?* (anti-spam, lock, arquivo de manutenção, cooldown, cache de erro, fila de retry).
4. **Ao auditar mecanismo de terceiro, contar os caminhos no código** antes de declarar auditoria concluída: eu e o XM auditamos três de quatro.

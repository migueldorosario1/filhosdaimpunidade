# 2026-09-10 — O alerta cujo gatilho mata o alertador

## O quê
Em DS-N-014 (10/09, 04:0x) declarei a disciplina: avisar o Miguel sobre o crédito apenas se o saldo ZERASSE ou a produção parasse. O saldo zerou às 05:45 (US$ −0,28, sustentado até 08:00). As rondas de 06:00, 06:30, 07:00, 07:30 e 08:00 não subiram, porque a ronda usa o mesmo crédito que zerou. O aviso não saiu. O Miguel soube pela recarga que ele próprio fez (US$ 9,71 às 08:15). A Baleia Azul da manhã saiu 08:42 em vez de 07:10.

## Por quê importa
Havia dois sistemas nervosos e a casa não sabia: a esteira de publicação seguiu de pé (7 matérias no ar, uma delas às 08:31, dentro do apagão); a camada de conversa/vigília morreu inteira. Um alerta desenhado dentro da cadeia que ele vigia falha exatamente no cenário para o qual existe.

## Como aplicar
1. Alertas de sobrevivência (crédito, disco, processo, certificado) precisam de executor FORA da cadeia vigiada. Candidatos sem custo novo: a escuta (Loop A, processo próprio, token do Telegram, texto fixo sem LLM) ou um flag escrito pelo DSN-F (custo ZERO de LLM) e lido pelo plantão.
2. Aviso de crédito não pode depender do LLM para ser escrito.
3. Atraso causado pela casa entra declarado dentro da entrega (a edição 44 conta a própria causa).
4. Ronda que não existiu não se cobre com texto genérico: declare a lacuna por busca literal na origem.

## Verificação
- `git show origin/main:cerebro/Foruns/ponte_laura_completa/de_dell.md | grep -c 'DS-N-20260910-016'` → último bloco antes da lacuna.
- Série do DSN-F no canal do financeiro: US$ −0,28 de 05:45 a 08:00; US$ 9,71 às 08:15.

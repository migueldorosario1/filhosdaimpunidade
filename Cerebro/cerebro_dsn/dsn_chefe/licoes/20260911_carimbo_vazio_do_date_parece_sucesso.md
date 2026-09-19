# Carimbo vazio do `date` parece sucesso — a barreira é o readback depois de gravar

**Data:** 2026-09-11 00:02 BRT · **Ronda:** 442a do DS-N Chefe · **Família:** mecanismo que responde sem ter feito (182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203 · 204 · 205) + erratas de carimbo 430a/432a/437a.

## O quê
Ao atualizar o `reforma_v3_status_SEED.json`, gerei o carimbo com:

    subprocess.run(["date", "+%Y-%m-%d %H:%M:%S"])

— **sem o `+`**. O `date` do GNU lê o argumento sem `+` como **nome de arquivo a exibir**, não como formato, e devolveu **string vazia**. O campo `atualizado` foi gravado como `""`.

## Por quê importa
O comando **rodou com sucesso** (exit 0) e entregou **nada**. Não houve exceção, não houve aviso: o arquivo versionado ficou com um campo de data vazio e o `git diff` mostrou 3 linhas trocadas, como se tudo tivesse dado certo. É exatamente a família «o passo que responde com sucesso é o passo, não a obra» — agora no **carimbo**, o dado que a casa usa para saber quando algo aconteceu.

E é a continuação natural das erratas de carimbo: 430a, 432a e 437a ensinaram que **carimbo vem do `date`, nunca da estimativa**. Faltava o segundo tempo: **carimbo que veio do `date` ainda pode vir vazio, e vazio não parece erro**.

## Como aplicar (barreira, não nota)
1. Formato do `date` **sempre** com `+` — e conferido no mesmo comando que grava.
2. **Readback obrigatório**: depois de gravar qualquer campo de data, **reler o arquivo** e imprimir o valor. Foi o readback da própria ronda que pegou o campo vazio antes do commit.
3. Campo de data vazio é **falha**, não estado válido: se o valor lido não casar com o formato esperado, regravar antes de seguir.
4. Vale para todo produtor de carimbo: memória, SEED, ponte, relatório.

## Desfecho nesta ronda
Corrigido para `2026-09-11 00:02:37` e reconferido por leitura **na mesma ronda**, antes do commit. Nenhum número do bloco 442a mudou. O dano foi zero porque a conferência existiu — e o valor da lição é que ela nasceu do meu próprio instrumento, não de um relato.

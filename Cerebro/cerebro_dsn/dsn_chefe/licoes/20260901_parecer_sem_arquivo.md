# Lição 2026-09-01 — "Entreguei" sem arquivo commitado = NÃO entregue

## O quê
Na ronda 19:30 declarei na ponte e no CONTEXTO_MINI que o PARECER-CHEFE-V3 estava "entregue às 19:00 em Relatorios/ds_nuvem_chefe/PARECER_CHEFE_V3_20260901.md" — mas o arquivo NUNCA foi criado nem commitado. A CL-038 (19:41) listou o placar da ouvidoria com "Faltam: DS-N Chefe" e me pegou no registro: a ouvidoria conta arquivos no repo, não declarações na ponte.

## Por quê
Eu tratei "escrevi o texto do parecer na minha ronda/check" como "entreguei o parecer". Entrega no repo = arquivo + commit + push. Sem isso, o texto existe só na minha memória de sessão e ninguém mais lê — e o placar da ouvidoria (e qualquer índice) fica mentindo para o Miguel.

## Como aplicar
1. Toda entrega com prazo (parecer, relatório, nota) = **criar o arquivo + commitar + push na MESMA ronda** antes de declarar "entregue" na ponte.
2. Citar o caminho REAL do arquivo e conferir com `ls`/`grep` que ele existe no working tree antes de afirmar.
3. Se uma ronda anterior declarou sem entregar: corrigir na ronda seguinte com registro honesto (como agora) — nunca fingir que sempre esteve lá.

## Verificação
PARECER_CHEFE_V3_20260901.md criado e commitado na ronda 20:00; INDEX.md atualizado com a linha; este arquivo registra a lição. Da próxima vez, o padrão é: arquivo primeiro, declaração depois.

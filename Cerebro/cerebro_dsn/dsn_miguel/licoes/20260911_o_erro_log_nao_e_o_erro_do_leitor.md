# O erro do arquivo não é o erro do leitor — contar linhas não é contar eventos

**Data:** 11/09/2026 · **Ronda:** 417ª DS-Dell · **Contexto:** missão P11.2/DS-208 (monitorar a reincidência
do incidente de cache) · **Família:** «o instrumento responde à pergunta errada» (16ª ocorrência do ledger).

## O quê aconteceu

Para incorporar a reincidência das 02:45 do BUG-208 ao acompanhamento, montei a tabela
minuto a minuto da hora 02 comparando **as duas torneiras**:

- `error.log` do nginx (o que o PHP gritou);
- `access.ocafezinho.com.log` (o que o leitor recebeu).

Na primeira passada, contei as linhas do `error.log` **por minuto, sem filtrar o tipo de erro**:

| minuto | linhas de erro (todos os tipos) | 5xx do leitor |
|---|---|---|
| 02:02 | 185 | 110 |
| 02:03 | 136 | **0** |
| 02:12 | 82 | **0** |
| 02:45 | 220 | 19 |
| 02:46 | 68 | **0** |

A leitura ingênua dessa tabela produz uma narrativa **falsa e sedutora**: «houve 136 exceções às 02:03
e 82 às 02:12 que **não** atingiram o leitor» — ou seja, «o mecanismo falha mas se recupera sozinho».

**Era falso.** Filtrando o **evento** (só `RedisException`) na mesma janela:

| minuto | RedisException | read error :6379 | 5xx do leitor |
|---|---|---|---|
| 02:00 | 11 | 11 | 11 |
| 02:01 | 12 | 11 | 12 |
| 02:02 | 103 | 52 | 110 |
| 02:03 | **0** | 0 | **0** |
| 02:12 | **0** | 0 | **0** |
| 02:25 | 11 | 4 | 8 |
| 02:45 | 20 | 20 | 19 |
| 02:46 | **0** | 0 | **0** |

Total da hora 02: **165 RedisException × 162 respostas 5xx** — praticamente **1:1**, com três
aglomerados (02:00–02:04, 02:25, 02:45) e **zero depois das 02:45**. As «136 linhas das 02:03» e as
«82 das 02:12» eram `PHP Warning`/`Deprecated` de rotina, não o incidente.

## Por quê importa

1. **Contagem de arquivo ≠ contagem de evento.** O `error.log` é uma pilha de tipos de erro
   diferentes; um `grep -c` por minuto mede **o arquivo**, não o defeito. Quem lê `185` e `110` lado
   a lado conclui «quase tudo vira 500»; quem lê `136` e `0` conclui «quase nada vira 500». **As duas
   conclusões saem do mesmo arquivo, e só uma pergunta foi feita.**
2. **A prova de impacto no leitor não está no `error.log` — está no `access.log`.** E o `error.log`,
   filtrado pelo evento certo, foi o que permitiu achar a **proporção 1:1**: isso transforma o
   `RedisException` num **proxy confiável para alarme** (P4 do BUG-208) — mas só depois do filtro.
3. **Sem o par, eu teria declarado uma «auto-recuperação» que nunca existiu** e teria enfraquecido o
   pedido de conserto que a casa já fez ao dono da infra.

## Como aplicar (régua)

- Quando o número decidir o relatório, **conte o evento com nome** (`grep "RedisException"`), nunca
  «as linhas do minuto». Se o filtro não estiver escrito no comando, o número não vale.
- **Pareie as duas torneiras**: o log de erro diz o que o PHP gritou; o log de acesso diz o que o
  leitor recebeu. Um sem o outro responde à pergunta errada.
- **Desconfie de `tail -N` sobre uma lista ordenada**: na mesma ronda, um `uniq -c | tail -25` cortou
  os minutos 02:00–02:11 da minha primeira leitura (eu só vi de 02:12 em diante) — truncamento de
  instrumento é a mesma família do `grep` que somou dois cabeçalhos (BUG-190/191, lição de hoje).
- **Imprima a linha crua** que produziu o número que vai ao relatório.

## Números que ficam (BUG-208, hora 02 de 11/09)

- 162 × 5xx em **14.158 requisições da hora = 1,14%**; picos 02:00 (11), 02:01 (12), 02:02 (110/332 = 33%),
  02:04 (2), 02:25 (8), 02:45 (19).
- **Depois das 02:45: zero** — 03:00–03:05 com **0 5xx em ~1.292 requisições**.
- `RedisException` (165) ≈ `5xx` (162) ⇒ **erro log filtrado serve de alarme**, mas não substitui o acesso.

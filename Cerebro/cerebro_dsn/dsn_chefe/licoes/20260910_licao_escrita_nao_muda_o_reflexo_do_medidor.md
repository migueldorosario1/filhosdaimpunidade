# Lição escrita não muda o reflexo do medidor (o mesmo erro de fuso voltou 6 h depois, na mesma máquina, no mesmo posto)

- DATA: 2026-09-10 (ronda 431ª do DS Nuvem Chefe, slot 16:00) — 2ª ocorrência no MESMO dia
- GATILHO: medir o volume de publicações das últimas 3h/12h/24h no REST canônico do Cafezinho.

## O QUÊ ACONTECEU
Às 16:00 eu abri o medidor de volume com o corte montado em **UTC** (`date -u -d "-3 hours"`).
Resultado: **3h=0 · 12h=14 · 24h=21**. O certo, medido no mesmo minuto com **hora local**
(`date -d "-3 hours"`): **3h=5 · 12h=16 · 24h=26**. O 3h=0 era **falso** (poderia ter virado
alerta de volume por vazio que não existe).

O que é novo: **a lição que descreve exatamente este erro já estava escrita nesta pasta desde a
ronda 420ª do mesmo dia** (`20260910_teste_de_controle_de_ordem_nao_pega_fuso_errado.md`), com a
régua pronta («Filtro de janela em REST/WP: sempre hora local, sem `-u`»). Ela não impediu a
reincidência — **o reflexo continuou saindo `-u`**.

Diferença a favor nesta ocorrência: o erro foi **pego por mim, no mesmo bloco de comandos**, antes
de virar relatório (na 420ª quem pegou foi o cruzamento com a medição do DS-Dell). Foi o
**teste de cruzamento** (rodar as duas versões, local e UTC, e comparar) que pegou — não a memória.

## POR QUÊ
Uma lição escrita aumenta o **conhecimento** e não substitui o **automatismo**. O comando `date`
com `-u` é digitado no piloto automático; a nota no arquivo é lida depois.
Documento não é barreira: **barreira é o que não depende de eu lembrar.**

## COMO APLICAR (régua que muda o comportamento, não a intenção)
1. **Nunca chamar `date` para janela de medição.** Fixar no início do bloco:
   `cut3=$(date -d '3 hours ago' +%Y-%m-%dT%H:%M:%S)` (sem `-u`) e usar SÓ essa variável.
2. **Rodar as duas versões e imprimir as duas** quando o número decidir alerta: `local=X utc=Y`.
   Se `utc=0` e `local>0`, o medidor está errado — não a produção.
3. **Nunca reportar janela zerada sem listar os IDs dela.** Lista vazia com dia movimentado =
   defeito do medidor.
4. **Lição só vira prevenção quando vira instrução executável** (variável fixada, wrapper,
   teste embutido). Este arquivo é o lembrete; a variável `cut3` é a barreira.

## FAMÍLIA
- `20260910_teste_de_controle_de_ordem_nao_pega_fuso_errado.md` (a mesma falha, ronda 420ª)
- BUG-20260910-DS-190 (filtro `--after` do WP-CLI aceito e ignorado) e BUG-20260910-DS-191 (sticky prependido)
- A pergunta de fundo segue a mesma dos três: **eu sei o que o meu instrumento NÃO faz?**
  Agora com o corolário: **eu sei o que a minha própria lição NÃO previne?**

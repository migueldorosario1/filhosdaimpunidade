# A janela de manutenção do host não é janela editorial (o cruzamento de dois relógios)

**Data:** 10/09/2026 · **Autor:** DS Miguel (Dell) · **Ronda:** 383ª (bloco DS-Dell-20260910-009) · **Ref:** BUG-20260910-DS-186

## O quê (o fato, com prova)
O servidor de produção **reinicia todos os dias às 03:30** por cron de manutenção do host
(`/etc/cron.d/serverdoin-cron-maintenance`: `30 3 * * * root service mysql stop && /sbin/reboot now`),
confirmado por `last reboot` (06→10/09, todos 03:30/03:31) e por `journalctl --list-boots` (boot 03:31:16).
Na madrugada de 10/09, a peça **269661** estava armada exatamente para **03:30:00** — a mesma janela do
desligamento. O cron não publicou (o post ficou `future`); depois do boot, o **wp-cron recuperou o atraso**
e o post virou `publish` por volta de **03:35** (~4-5 min tarde). Durante o reboot, a REST devolveu **502**
e a home voltou 200 com `up 0 min`.

## Por quê (a causa-raiz)
Não é falha de nenhum dos dois donos: é o **cruzamento de dois relógios desenhados em separado** —
a manutenção do host (infra) e a grade editorial (fila). Nenhum dos dois conhece o outro.
O atraso **se esconde**: o WordPress republica o atrasado sozinho, sem erro visível na fila,
então quem confere a fila ANTES do horário não vê nada.

## Como aplicar (a regra)
1. **Nenhuma peça armada para um horário dentro de janela de manutenção conhecida** (hoje: 03:30).
   A grade da madrugada deve pular para 03:45/04:00; a janela de reboot entra no checklist do dono da fila.
2. **Conferir `post_status` DEPOIS do horário**, nunca a fila antes — é a única leitura que pega atraso mascarado.
3. **Para os vigias:** o 502 entre 03:30 e 03:31 é **reboot programado, não queda**; o disparo das 03:30
   não se cobra no minuto — a régua é o estado depois do boot. Não escalar como incidente.
4. **Regra geral (a que fica):** antes de acusar quem publica, procure o **segundo relógio** —
   manutenção, backup, cron de host, expurgo — que compartilha o minuto com a operação.

## Irmãos
BUG-20260910-DS-184 (pré-condição de agendamento: peça sem capa não publica) e
BUG-20260909-DS-182 (lock que avisa e não barra) — mesma família: **o que a casa desenhou para impedir
ainda não impede; e às vezes o que impede está fora da casa.**

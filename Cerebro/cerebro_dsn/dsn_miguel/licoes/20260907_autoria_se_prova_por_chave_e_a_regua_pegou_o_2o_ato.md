# 2026-09-07 — Autoria se prova por CHAVE, e a régua do evento pegou o 2º ato do incidente

**Ronda:** DS-Dell 257ª (07/09/2026 01:06 BRT) · bloco DS-Dell-20260907-003

## O quê
Na madrugada da virada 06/09→07/09, o incidente da CL-033 (269288 posto em draft+reintitulado às 00:11:41 por terceiro) teve um **2º ato** que a minha conferência do colchão pegou ~4 minutos depois do golpe: às **01:00:58** o ator rodou `sudo -u www-data wp post update 269279 --post_status=draft` — tirando o FlexGanttFX (colchão 06:30 de 07/09) da fila — além de retitular 269228/269275/269305 e remover categorias de 269155/269144/269183 (00:56–01:04). A conferência das 01:02 (36ª execução, evento por peça) viu o 269279 fora da fila e o auth.log explicou o porquê em segundos.

## Por quê
Duas descobertas de método:
1. **Autoria se prova por CHAVE, não por IP.** O authorized_keys do servidor tem 8 entradas com comments identificáveis (auth[1..8]); a sessão de 186.223.171.9 usou a chave RSA `k+A3E5eN…` = **auth[5] "migueldorosario@novo"** — a MESMA que documentei na CL-109 (03/09) vinda de 189.99.98.64 (máquina do Miguel/launchers). IP dinâmico mudou; a chave não. Conclusão factual: o operador TEM a chave privada do dono — ou é o Miguel com script de correção editorial, ou alguém com a chave dele. O DS registra o FATO (log `sudo COMMAND` com IP + fingerprint + PWD) sem acusar; a pergunta "foi ordem do Miguel?" é do CM/dono.
2. **A régua do evento por peça (34ª/35ª execução) pega golpe em produção em MINUTOS.** O 1º ato (00:11) só foi descoberto porque o post não subiu (00:30); o 2º ato (01:00:58) foi visto pela conferência das 01:02 — o desenho «conferência vê → alerta nomeia → operador decide» virou detecção em tempo real de intervenção não registrada.

## Como aplicar
- **Conferência do colchão (a cada ronda):** listar future real + conferir EVENTO por peça (`wp cron event list` + option cron por ID) — qualquer peça que sai da fila entre duas conferências = alerta imediato (quem assume: CL decide reagendar/aceitar; DS não executa, publish=0).
- **Forense de autoria:** `grep 'wp post update' /var/log/auth.log` → o `sudo COMMAND` registra IP + fingerprint da chave + PWD; identificar o dono da chave pelo COMMENT no `authorized_keys` (auth[N]) — nunca expor a chave em si, só o comment.
- **Quando a chave é do dono:** registrar o fato + pedir confirmação ao CM/dono ("foi ordem do Miguel?") — não tratar como ataque nem como autorizado sem a palavra dele.
- **Resposta ao ponto "sem evento" (pergunta da CL-033):** método triplo (event list + option cron via db + Action Scheduler) reduz falso negativo por cache Redis; teste empírico (post publica EM PONTO com evento recriado) prova que o mecanismo está são — o que falha é a PRESENÇA do evento (família BUG-DS-098 / re-save que perde o evento).

Família: licoes/20260905_restauro_de_incidente_de_terceiro_come_blocos_de_ronda.md · licoes/20260907_peca_do_colchao_sem_evento_e_o_meta_cron_nao_e_prova.md · licoes/20260902_agendado_nao_e_disparo_evento_e_a_prova.md

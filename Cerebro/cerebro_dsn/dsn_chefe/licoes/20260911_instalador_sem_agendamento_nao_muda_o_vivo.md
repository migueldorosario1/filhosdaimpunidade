# LIÇÃO 20260911 — INSTALADOR SEM AGENDAMENTO NÃO MUDA O VIVO (terceiro tempo da família «medir quem lê»)

## O quê
Na ronda 454a (11/09 06:03) eu entreguei o instalador que faltava — `.tencent_v6_oficina/sync_estado_casa.py` — para levar o `estado_casa_SEED.md` do repo até o arquivo VIVO que o plantão do Telegram lê (`~/ds_nuvem_chefe/estado_casa.md`). Vinte e sete minutos depois, na ronda 455a, fui conferir o vivo: **mtime 04/09 01:36, sem carimbo «Última atualização»** ⇒ o instalador nunca rodou e o plantão continua lendo o mundo de 30/08 na PRIMEIRA metade do prompt.

## Por quê
O meu próprio texto da 454a dizia «falta só agendar (sugestão de cron no rodapé do script)» — e eu li isso como «entregue». Não é: **entrega é o arquivo VIVO mudado**, não o script que existe. A cadeia tem quatro elos e eu só fechava dois:

1. **SEED no repo** (eu atualizo toda ronda) — elo que eu controlo e fecho;
2. **instalador** (o script fail-soft, atômico, com leitura de carimbo) — elo que eu controlo e fechei na 454a;
3. **agendamento no host** (cron/systemd no dono da máquina) — elo que **não é minha alçada**;
4. **arquivo VIVO mudado** (o único que o consumidor lê) — a prova que fecha tudo.

Sem o 3º, o 4º nunca acontece — e o silêncio do 4º é invisível: nada falha, o plantão só responde com o passado.

## Como aplicar
- Para todo arquivo que outro agente consome: **declarar o par SEED+VIVO e o dono do agendamento**; enquanto o vivo não muda, o item é **pendência declarada**, nunca «feito».
- **Medir o vivo, não o entregável:** `stat -c '%y' <vivo>` e presença do carimbo são a prova; o commit do script não é.
- Escrever no relatório a frase exata «**segue não agendado**» enquanto o vivo estiver velho — repetir a checagem em toda ronda até o elo 3 fechar (é barata: dois comandos).
- Este é o 3º tempo da mesma família: 452a = **medir a LEITURA** de quem consome (o topo, não o fim); 454a = **medir a IDADE** do que ele lê; 455a = **medir o VIVO**, não o instalador.

— DS Nuvem Chefe (DS-N Chefe) · 11/09/2026 06:30 BRT

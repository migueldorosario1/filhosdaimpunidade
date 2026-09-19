# Fórum — Repetidor Estatal sem No Home

**Decisão canônica de Miguel — 13/08/2026, 23:26 BRT**

Miguel determinou que o Repetidor Estatal não use mais a categoria WordPress
`No Home` (`20699`). As matérias continuam sendo publicadas pelo fluxo já
homologado do Repetidor, mas agora entram normalmente na home com sua categoria
editorial.

## Regra viva

- O Repetidor Estatal nunca acrescenta `20699` ao payload.
- A regra também vale para Previsão do Tempo (`5102`).
- Ficam superadas as regras históricas de 50% No Home, 100% No Home, score para
  home e No Home obrigatório para Previsão do Tempo.
- Esta decisão é específica do Repetidor e não muda o protocolo draft-only dos
  V4, que continua dependendo de revisão humana.

## Correção aplicada

O worker vivo `/root/agente_repetidor_estatal.py` recebeu
`REPETIDOR_NO_HOME_ENABLED = False`. O chamador força `aplicar_no_home=False` e
o construtor do payload rejeita `No Home` mesmo se uma chamada antiga passar
`no_home=True`.

Backup do worker:

`/root/agente_repetidor_estatal.py.bak_pre_no_home_off_20260814_022545`

Smoke test sem conexão com o WordPress interceptou dois payloads:

- Economia: categorias `[43]`;
- Previsão do Tempo: categorias `[5102]`;
- categoria `20699`: ausente nos dois.

## Post que revelou a regressão

O post **265699**, “Segunda maior refinaria do país reduz preço da gasolina em
11,3%”, estava publicado com categorias `[43, 20699]`. Foi corrigido para
`[43]`, mantendo status `publish` e imagem destacada `265698`.

Backup completo anterior à correção:

`/root/backup_post_265699_pre_no_home_20260814_022512.json`


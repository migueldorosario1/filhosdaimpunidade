# Fórum — Blocos Saúde/Esporte/Meio Ambiente religados no V4.1 (2-3x/dia)

**Data:** 26/08/2026 ~19:15 BRT · **Executor:** ZCode/Kimi K3 · **Ordem do Miguel:** 26/08 ~18:40 ("se for manter saúde, meio ambiente, esporte na home, é para atualizar duas, três vezes por dia, senão tira o bloco")

## 1. A ordem

Manter os blocos Saúde, Meio Ambiente e Esporte na home **somente se** atualizarem 2-3 vezes por dia; caso contrário, tirar o bloco. Miguel deu autonomia: "te decide".

## 2. Diagnóstico (por que estavam parados desde 23/08)

1. **Quem alimentava os 3 blocos era o V4 antigo** (posts `zizi_job_id=v4d_saude_*` etc., author 5786). O repetidor estatal NÃO era a fonte desses blocos.
2. **A ordem "só V4.1" de 24/08** (`V4_DESLIGADO_20260824`) desligou os workers V4 dessas verticais — últimos posts: saúde 23/08 15:08, ambiente 23/08 19:38, esporte 23/08 13:16.
3. **O V4.1 (`v41_ciclo.py`) só cobria 4 verticais**: nacional, economia, ciencia, geopolitica. As 3 ficaram órfãs: coletavam/intake todos os dias (enchendo sqlite de `candidates`) mas ninguém redigia nem publicava.
4. Descoberta lateral: o **repetidor estatal não publica do NYC desde 16/08** (199 falhas 400 do gate de imagem — ele não conhece o gate). Os posts recentes "author 5470" são na verdade V4.1 publicado por LAURA-AGY com carimbo `_cafezinho_img_check` (consenso duplo). O site seguiu abastecido pelo V4.1 das 4 verticais, então a pane do repetidor passou despercebida. **Fica registrada como incidente separado a tratar.**

## 3. O que foi feito (tudo no NYC)

**Arquivo:** `/root/v4_labs/codigo/v41_ciclo.py` (backup: `v41_ciclo.py.bak_pre_3verticais_20260826`; crontab: `/root/agent_data/crontab_backup_pre_3verticais_20260826.txt`)

1. `--vertical` passa a aceitar `saude`, `esporte`, `meio_ambiente` + mapa VERTS (bancos sqlite já existentes, aliases batem com EDITORIA_ALIASES do redator runtime).
2. **Seleção de pauta das 3 novas:** como não há worker marcando `drafted`, o ciclo usa as `new` frescas (janela 48h, mais recentes primeiro, LIMIT 9). As 4 verticais ativas ficaram com a lógica INTOCADA.
3. **Patch de categorias no nascimento** (mesmo remédio da diretriz "ciência é tecnologia" de 24/08): saude→[258,2403], esporte→[1271,2403], meio_ambiente→[582,2403] — padrão histórico dos posts v4d_*.
4. **Crons:** coleta/intake das 3 verticais de 1x/dia → **3x/dia**; 3 ciclos v41 novos **3x/dia** cada (marca `V41_3VERTICAIS_20260826`), escalonados em minutos/horas sem colisão com os ciclos */2 existentes.

## 4. Prova de fogo

Ciclo real de saúde rodado manualmente às 19:07 BRT: tese aprovada → redator gpt-5.5 → **rascunho 267820 criado** ("Cerveja fica fora de restrição publicitária há 30 anos", 5.248 chars, status=draft, cats **[258,2403]**, `zizi_job_id=v41_saude_eeae3806cbcd`, FC websearch "confirma"). Entra na fila dos editores (CM/AGY) como qualquer rascunho V4.1 — publicação segue EXCLUSIVA deles, nos slots de ~30min.

## 5. Grade resultante (horários BRT)

| Vertical | Coleta/intake | Ciclo V4.1 | Publicação esperada |
|---|---|---|---|
| Meio Ambiente | 09:15 / 15:15 / 21:15 | 10:05 / 16:05 / 22:05 | ~30-60min após cada ciclo |
| Esporte | 10:15 / 16:15 / 22:15 | 11:22 / 17:22 / 23:22 | idem |
| Saúde | 11:15 / 17:15 / 23:15 | 12:42 / 18:42 / 00:42 | idem |

Mesmo que 1 ciclo/dia falhe por sem-tese (fail-closed), restam 2 posts/dia/bloco — dentro da meta do Miguel.

## 6. Estado da missão

- **O que aconteceu:** 3 verticais órfãs religadas ao V4.1 com prova de fogo (rascunho 267820); coletas 3x/dia; crons instaladas; backups feitos; diffs cirúrgicos verificados.
- **O que falta:** (a) confirmar a 1ª publicação dos editores a partir do rascunho 267820 (próximas 1-2h) e as primeiras 24h de cadência real; (b) incidente separado: repetidor estatal bloqueado no gate de imagem desde 16/08 (199 falhas) — decidir se ele volta a ter papel ou se fica oficialmente aposentado (V4.1 já cobre a produção); (c) vigia da ronda V4.1 (30/30min) deve incorporar as 3 verticais no relatório.
- **O que preciso de você (Miguel):** nada agora. Se em 48h algum bloco estiver com menos de 2 posts/dia, me avisa que eu ajusto a cadência (dá pra subir a coleta para a cada 6h e os ciclos para 4x/dia).

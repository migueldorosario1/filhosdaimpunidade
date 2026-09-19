# 🧠 Memória técnica — checagem GA4 tempo real Cafezinho canônico (24/08/2026)

**Par do fórum:** `Foruns/forum_analytics_queda_visitas_online_cafezinho_20260824.md`

## Como consultar o GA4 do Cafezinho por API (caminho das pedras)

1. Credencial (service account Editor, a mesma do painel CCTV): `/home/ubuntu/cafezinho/Projeto Cafezinho Agentes/root/ga4.json` no Tencent (`ssh tencent`, 43.156.151.165).
2. Propriedade do canônico: `properties/374552425` (tag `G-4E5DKNTYET`; espelho cafezinho.news serve a mesma tag).
3. Lib: `google.analytics.data_v1beta` (instalada no python3 do sistema, `/usr/local/lib/python3.12/dist-packages`).
4. Script pronto deixado no Tencent: `/tmp/ga_rt.py`..`/tmp/ga_hr.py` (realtime + série por hora).

## Gotchas do Realtime API desta propriedade (schema REDUZIDO)

- Válidas: `minutesAgo`, `country`, `city`, `deviceCategory`, `unifiedScreenName`, `audienceName`.
- INVÁLIDAS (400 INVALID_ARGUMENT): `dateHourMinute`, `pagePath`, `unifiedPagePath`, `sessionSource`, `sessionDefaultChannelGroup`.
- Sem order_bys dimension na lib instalada (`DimensionOrderBy` não importável de `...types`) → ordenar no Python.
- Realtime = janela fixa de 30 min; para além disso usar run_report (dateHour) — mas **dia corrente vem incompleto** (hoje: 07h=93, 08h=1, 09h+ ausente às 13:36 BRT) = latência de processamento normal, não bug.

## Números coletados (24/08 13:36 BRT)

- Realtime: 55 ativos; série min: 1–9/min; BR 39 / CN 8 / US 7 / UK 1; top páginas: debate Record 12, home 10, Marçal/TRE 4.
- Hora a hora 3 dias: ontem (dom) pico 08h=472 e 22h=496; hoje 00–06h normal 246–366.
- Diários 7d: 6191 / 5298 / 5686 / 5472 / 5804 / **7858 (dom recorde)** / 2244 parcial.
- Site: canônico 200 em 1,1s com tag; espelho 200 em 4,2s com tag.

## Conclusão

Sem incidente (site, tag e GA operacionais). Queda percebida = pós-pico de domingo + processamento intraday incompleto + produção reduzida (V4 OFF 09:30). Script sobrevive em /tmp do Tencent (efêmero — recriar do fórum se sumir).

## ADENDO 1 (24/08 14:05) — retificação + contador redundante

Ver fórum ADENDO 1. Resumo técnico do que mudou:

- **Causa real da "queda": GA4 tempo real subnotificando** (lado Google). Site são: tag presente (home+posts), nginx com humanos hoje>ontem em quase todas as horas (07h 1746×1541; 11h 2767×1646).
- **Provas de subnotificação**: (1) visita Chrome real headless ao post raro /2018/08/09/dino-nao-esta-inelegivel/ NUNCA apareceu no realtime (3 consultas/4 min, com e sem consentimento); (2) hit MP (HTTP 204) invisível; (3) idem na propriedade Mundo Trilhos 546667776 (não é só do Cafezinho); (4) realtime 29-55 vs ~120-170 esperado.
- **Contador instalado** (pedido Miguel):
  - nginx: `log_format contador_ipreal` declarado NO vhost (gotcha: este nginx inclui sites-enabled ANTES de conf.d) + `access_log /var/log/nginx/access.ocafezinho.contador.log contador_ipreal;` nos 2 server blocks.
  - GOTCHA GRAVE: `sites-enabled/ocafezinho.com.conf` é CÓPIA de available (não symlink) — editar o enabled (ou ambos). E NUNCA criar .bak dentro de sites-enabled (o include lê tudo).
  - IP real vem de $http_cf_connecting_ip (log antigo só via 190.89.239.31/.244 + 10.1.1.108 = Cloudflare/infra).
  - `/root/cafezinho_contador/contador.sh`: python3 puro; filtros humano (Mozilla+plataforma real, sem bot-list, GET 200, path conteúdo: /AAAA/|/|tag/|category/|top|autor/|page/); saída resumo.json+txt (online 30min, hoje/ontem por hora nav/ips, top10).
  - cron `/etc/cron.d/cafezinho-contador` */5. Consulta: `ssh cafezinho-wp 'bash /root/cafezinho_contador/contador.sh'`.
  - mu-plugin PHP tentado e desativado (cache estático nem rodava WordPress; backup em /root/cafezinho_contador/mu-plugin-contador-DESATIVADO_20260824.php).
- Pendência 25/08: conferir se o dia de HOJE fechou normal nos relatórios processados do GA (se sim, só o realtime erra). Opcional: resumo.json no painel CCTV; vigia Telegram GA×contador.

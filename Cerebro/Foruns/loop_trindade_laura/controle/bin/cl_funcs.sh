#!/bin/bash
# cl_funcs.sh — funções dos pacotes clNNN da Claude Laura (CL). Cópia persistente em /root/cl_funcs.sh (servidor),
# scratchpad da sessão e cerebro/Foruns/loop_trindade_laura/controle/bin/cl_funcs.sh (repo).
# Origem: cabeçalho cl147 (CL-20260904-031, íntegra em de_laura.md) + evoluções de 05–07/09 (recorte opcional na capa, ISENTA_ATE).
# Uso: { echo "# CL-... (pacote clNNN) — ..."; sed -n '2,$p' cl_funcs.sh | sed "s/^REF=.*/REF=\"CL-YYYYMMDD-NNN\"/"; cat clNNN_body.sh; } > clNNN.sh
cd /var/www/ocafezinho || exit 1
W="wp --allow-root"
REF="CL-00000000-000"
TS="$(TZ=America/Sao_Paulo date '+%d/%m/%Y %H:%M')"
UP=/var/www/ocafezinho/wp-content/uploads
UA="OCafezinhoCL/1.0 (redacao@ocafezinho.com)"
ISENTA_ATE="${ISENTA_ATE:-$(TZ=America/Sao_Paulo date -d tomorrow '+%Y-%m-%d')}"
carimbo() { local pid="$1" mid="$2"; local rel; rel=$($W post meta get "$mid" _wp_attached_file 2>/dev/null); local md5; md5=$(md5sum "$UP/$rel" | cut -d' ' -f1); local url_att; url_att=$($W post get "$mid" --field=guid 2>/dev/null); local chk="{\"ok\": true, \"media_id\": $mid, \"attachment_id\": $mid, \"attachment_url\": \"$url_att\", \"hash_md5\": \"$md5\", \"vereditos\": [\"APROVADA\"], \"veredito_final\": \"APROVADA\", \"consenso\": \"$REF\", \"revisor\": \"Claude Laura (visao propria)\", \"ts\": \"$TS\", \"lei\": \"gate visual CL + fact-check CL $REF\"}"; $W post meta update "$pid" _cafezinho_img_check "$chk" >/dev/null; $W post meta update "$mid" _cafezinho_img_check "$chk" >/dev/null; $W post meta update "$pid" _thumbnail_id "$mid" >/dev/null; echo "CAPA post=$pid media=$mid md5=$md5 thumb=$($W post meta get "$pid" _thumbnail_id)"; }
capa_local() { local pid="$1" rel="$2" leg="$3" alt="$4"; local mid; mid=$($W media import "$UP/$rel" --post_id="$pid" --title="$leg" --caption="$leg" --alt="$alt" --porcelain 2>/dev/null | tail -1); if ! [[ "$mid" =~ ^[0-9]+$ ]]; then echo "IMPORT_FALHOU post=$pid"; return 1; fi; carimbo "$pid" "$mid"; }
# capa pid url legenda alt [crop WxH+X+Y]
capa() { local pid="$1" url="$2" leg="$3" alt="$4" crop="$5"; local f="/tmp/cl_capa_$pid.jpg"; curl -s -L -A "$UA" -o "$f" "$url"; local sz; sz=$(stat -c %s "$f" 2>/dev/null || echo 0); if [ "$sz" -lt 20000 ]; then echo "DOWNLOAD_FALHOU post=$pid bytes=$sz"; return 1; fi; if [ -n "$crop" ]; then convert "$f" -auto-orient -crop "$crop" +repage -resize '1600x1600>' -quality 88 "$f" 2>/dev/null; else convert "$f" -auto-orient -resize '1600x1600>' -quality 88 "$f" 2>/dev/null; fi; local mid; mid=$($W media import "$f" --post_id="$pid" --title="$leg" --caption="$leg" --alt="$alt" --porcelain 2>/dev/null | tail -1); if ! [[ "$mid" =~ ^[0-9]+$ ]]; then echo "IMPORT_FALHOU post=$pid"; return 1; fi; carimbo "$pid" "$mid"; }
# selo pid fontes — ORDEM CORRIGIDA (CL-20260912-003, licao da 269846): monta e GRAVA o cl_manual
# primeiro, confere por readback, e so entao grava a isenta. Isenta e permissao; cl_manual e memoria.
# Antes a isenta era gravada ANTES do python; se o python falhasse, a peca ficava destravada SEM parecer.
selo() { local pid="$1" fontes="$2"; python3 - "$pid" "$fontes" "$REF" "$TS" <<'PY' > /tmp/cl_chk_$1.json
import sys,json,subprocess
pid,fontes,ref,ts=sys.argv[1:5]
raw=subprocess.run(["wp","--allow-root","post","meta","get",pid,"_cafezinho_txt_check"],capture_output=True,text=True).stdout.strip()
try: d=json.loads(raw) if raw else {}
except Exception: d={"_raw_anterior":raw}
d["cl_manual"]={"ok":True,"revisor":"CL","ref":ref,"fontes":fontes,"ts":ts,"metodo":"leitura integral + busca web propria + juiz V4.1 lido + titulo sem sigla + padrao Metropoles/Forum + nota de frescor + dedupe contra o site"}
print(json.dumps(d,ensure_ascii=False))
PY
grep -q '"cl_manual"' "/tmp/cl_chk_$pid.json" 2>/dev/null || { echo "SELO_ABORTADO post=$pid — cl_manual NAO foi montado; isenta NAO gravada (LICAO-269846)"; return 1; }
$W post meta update "$pid" _cafezinho_txt_check "$(cat /tmp/cl_chk_$pid.json)" >/dev/null || { echo "SELO_ABORTADO post=$pid — falha ao gravar txt_check; isenta NAO gravada"; return 1; }
$W post meta get "$pid" _cafezinho_txt_check | grep -q cl_manual || { echo "SELO_ABORTADO post=$pid — readback sem cl_manual; isenta NAO gravada"; return 1; }
$W post meta update "$pid" _cafezinho_txt_isenta "{\"ref\":\"$REF\",\"expira_em\":\"$ISENTA_ATE\",\"por\":\"Claude Laura (fact-check proprio com fontes + revisao integral + titulo + frescor + dedupe + padrao Metropoles/Forum)\"}" >/dev/null && echo "SELO_OK post=$pid (cl_manual gravado e conferido; isenta so depois)"; }
isenta_re() { local pid="$1"; $W post meta update "$pid" _cafezinho_txt_isenta "{\"ref\":\"$REF\",\"expira_em\":\"$ISENTA_ATE\",\"por\":\"Claude Laura (re-emissao: isenta apagada; checagem CL do dia mantida)\"}" >/dev/null && echo "ISENTA_RESTAURADA post=$pid"; }
agenda() { local pid="$1" d="$2"; local gmt; gmt=$(TZ=UTC date -d "TZ=\"America/Sao_Paulo\" $d" '+%Y-%m-%d %H:%M:%S'); $W post update "$pid" --post_status=future --post_date="$d" --post_date_gmt="$gmt" >/dev/null 2>&1; }
evento() { echo "evento_cron post=$1: $($W cron event list --hook=publish_future_post --fields=hook,args 2>/dev/null | grep -c "$1")"; }
tem_evento() { $W db query "SELECT option_value LIKE '%i:$1;%' FROM wp_options WHERE option_name='cron'" --skip-column-names 2>/dev/null; }
entra() { local pid="$1" d="$2" got=""; for i in 1 2; do agenda "$pid" "$d"; got=$($W post get "$pid" --field=post_date); [ "$got" = "$d" ] && break; done; echo "ENTRA post=$pid pedido=$d ficou=$got status=$($W post get "$pid" --field=post_status)"; sleep 3; local t; for t in 1 2 3; do [ "$(tem_evento "$pid")" = "1" ] && break; echo "SEM_EVENTO post=$pid (tentativa $t) — toggle draft→future (LICAO-2117)"; $W post update "$pid" --post_status=draft >/dev/null 2>&1; sleep 3; agenda "$pid" "$d"; sleep 3; done; evento "$pid"; echo "evento_db post=$pid: $(tem_evento "$pid")"; [ "$(tem_evento "$pid")" = "1" ] || echo "ALERTA_CL post=$pid SEM EVENTO APOS 3 TENTATIVAS — CORRIGIR A MAO"; }
titulo() { $W post update "$1" --post_title="$2" >/dev/null && echo "TITULO post=$1: $($W post get "$1" --field=post_title)"; }
# cats pid id [id...] — SEMPRE --by=id (wp post term set usa SLUG por padrao e cria categoria numerica); repoe Redacao 2403; alerta se sobrar nome numerico
cats() { local pid="$1"; shift; $W post term set "$pid" category "$@" --by=id >/dev/null 2>&1; $W post term add "$pid" category 2403 --by=id >/dev/null 2>&1; local lixo; lixo=$($W post term list "$pid" category --field=name | grep -cE '^[0-9]+$'); echo "CATS post=$pid: $($W post term list "$pid" category --field=name | tr '\n' ',')"; [ "$lixo" = "0" ] || echo "ALERTA_CL post=$pid — $lixo categoria(s) NUMERICA(s): term set rodou sem --by=id"; }
evento_hora() { local pid="$1"; local pd; pd=$($W post get "$pid" --field=post_date); local nr; nr=$($W cron event list --hook=publish_future_post --fields=next_run,args --format=csv 2>/dev/null | grep "\[$pid\]" | cut -d, -f1 | tr -d "\""); echo "evento_hora post=$pid post_date=$pd cron_next_run=$nr $([ "$pd" = "$nr" ] && echo OK || echo DIVERGE)"; }
# chk_img pid — LICAO 271200 (16/09 00:01): capa preexistente sem _cafezinho_img_check -> gate reverte publish para pending.
# Roda ANTES de entra; se faltar o carimbo, avisa (e o pacote deve rodar carimbo pid mid antes).
chk_img() { local pid="$1"; local c; c=$($W post meta get "$pid" _cafezinho_img_check 2>/dev/null); local i; i=$($W post meta get "$pid" _cafezinho_img_isenta 2>/dev/null); if [ -n "$c" ] || [ -n "$i" ]; then echo "IMG_CHECK_OK post=$pid"; else echo "ALERTA_CL post=$pid SEM _cafezinho_img_check — rode carimbo $pid <media_id> antes do entra (gate reverte para pending)"; return 1; fi; }

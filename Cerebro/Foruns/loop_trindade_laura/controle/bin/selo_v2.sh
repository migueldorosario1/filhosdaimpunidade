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

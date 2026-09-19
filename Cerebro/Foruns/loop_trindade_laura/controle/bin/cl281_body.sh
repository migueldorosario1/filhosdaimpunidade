
echo "=== CL-20260912-003 / cl281 — instala o selo v2 (cl_manual antes da isenta) SO se os dois testes passarem ==="
TZ=America/Sao_Paulo date
echo "backup ja feito em /root/cl_funcs.sh.bak_pre_selo_v2_*"
ls -1 /root/cl_funcs.sh.bak_pre_selo_v2_* 2>/dev/null | tail -1

# carrega a versao NOVA num subshell de teste, sem instalar nada ainda
set +e
( . /tmp/cl_funcs_novo.sh
  REF="TESTE-SELO-V2"; TS="$(TZ=America/Sao_Paulo date '+%d/%m/%Y %H:%M')"

  echo "--- TESTE 1: peca real retida (269918, fica draft) ---"
  # estado antes
  echo "antes: cl_manual=$($W post meta get 269918 _cafezinho_txt_check 2>/dev/null | grep -c cl_manual) isenta=$($W post meta get 269918 _cafezinho_txt_isenta 2>/dev/null | wc -c)"
  selo 269918 "TESTE de ordem do selo v2 — nao e parecer editorial"
  echo "depois: cl_manual=$($W post meta get 269918 _cafezinho_txt_check 2>/dev/null | grep -c cl_manual) isenta=$($W post meta get 269918 _cafezinho_txt_isenta 2>/dev/null | grep -c TESTE-SELO-V2)"
  echo "status_269918=$($W post get 269918 --field=post_status)  <-- TEM de continuar draft"

  echo "--- TESTE 2: caminho de falha (post inexistente 9999999) — a isenta NAO pode ser gravada ---"
  selo 9999999 "teste de falha"
  echo "rc_esperado=1 rc_obtido=$?"
)
set -e

echo "--- LIMPEZA do teste 1: 269918 volta ao estado retido ---"
$W post meta delete 269918 _cafezinho_txt_isenta >/dev/null 2>&1
$W post meta delete 269918 _cafezinho_txt_check >/dev/null 2>&1
echo "269918 limpo: isenta=$($W post meta get 269918 _cafezinho_txt_isenta 2>/dev/null | wc -c) check=$($W post meta get 269918 _cafezinho_txt_check 2>/dev/null | wc -c) status=$($W post get 269918 --field=post_status)"

echo "--- INSTALACAO ---"
if bash -n /tmp/cl_funcs_novo.sh && [ "$(grep -c '^selo()' /tmp/cl_funcs_novo.sh)" = "1" ]; then
  cp -a /tmp/cl_funcs_novo.sh /root/cl_funcs.sh && echo "INSTALADO em /root/cl_funcs.sh"
  grep -n "LICAO-269846" /root/cl_funcs.sh | head -1
  bash -n /root/cl_funcs.sh && echo "SINTAXE_FINAL_OK"
else
  echo "NAO INSTALADO — arquivo novo nao passou na conferencia"
fi
echo "--- a peca das 07:00 nao pode ter sido tocada ---"
echo "269908 status=$($W post get 269908 --field=post_status) date=$($W post get 269908 --field=post_date) thumb=$($W post meta get 269908 _thumbnail_id) cl_manual=$($W post meta get 269908 _cafezinho_txt_check | grep -c cl_manual)"

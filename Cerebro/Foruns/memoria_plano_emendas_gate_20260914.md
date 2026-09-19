# MEMÓRIA TÉCNICA — auditoria das emendas E5/E4-lite/E2 + plano de fechamento (14/09/2026)

ZM-20260914-013 · ZCode/GLM-5.3 · leitura only em cafezinho-wp (us65.serverdo.in), NENHUMA mudança.

## 1. Comandos e provas (14/09 19:2x BRT)

- Gate: `ls -la .../mu-plugins/cafezinho-gate-dois-checks.php*` → vivo 13.836b 11/09 08:36 "Version: 1.2.0 (+E2 passaporte hash+TTL por revisor) (E4-lite: HMAC nas isenções de robôs/ordem-Miguel)"; .baks: pre_modo_contrato_20260901 (5.028b), pre_e4lite_20260910 (5.813b), pre_e2_20260910 (10.825b), pre_consultivo_20260911 (12.796b).
- Contadores no vivo: hmac 12 · sha256 3 · hash_equals 2 · ttl 4 · passaporte 8 · gate2c_assina 2 · exige_gravador 2.
- Sonda E5: crontab root `7-59/15 * * * * flock -n /tmp/sonda_gate_e5.lock /usr/bin/python3 /root/sonda_gate_e5.py` # SONDA_GATE_E5_20260910; /root/sonda_gate_e5.py 13.449b 11/09 08:40; log VERDE contínuo até 19:22:31 de hoje ("provas ok (modo=consultivo)"); estado.json heartbeat/nivel=verde frescos.
- Options: cafezinho_gate_dois_checks_ativo=1 · cafezinho_gate_dois_checks_modo=consultivo · cafezinho_gate2c_exige_gravador_humano AUSENTE (default '0').
- Código-chave: consultivo = REST não devolve 423 e wp_insert_post_data não rebaixa draft (só error_log "CONSULTIVO ... segue; decisão editorial: CL/Miguel") — comentário no código cita "OS do Miguel 11/09: R1/R2 travavam publicações erradas". dois_checks_ok(): humano sempre true; isenta CL-/CM- ref simples (+trava de gravador se armada); AL-/GM-/ordem exige HMAC (payload post_id|ref|expira_em|sha1_conteudo|ts, frescor 48h); sem isenta em modo não-dois_checks = false (mas no consultivo false não bloqueia).
- Whitelist gravador codificada: '5780,5786,2018,5801,1' (users, não capability).
- Isentas c/ meta _cafezinho_txt_isenta_por existem (log-only coletando; amostra: 269813/846/858/892 publish).
- SEM watchdog externo da sonda (grep crontab watchdog|heartbeat vazio).
- debug.log 22.008.641.717 bytes (parado desde 14/07) dentro de wp-content.
- Seed repo (.tencent_v6_oficina/reforma_v3_status_SEED.json, carimbo 11/09 09:00 ronda 460a): Onda 3 #4 ok=true (eta 5/5 EXECUTADO 10/09 §12.11) MAS pendencias[0]=P1 ATIVA c/ prompt "implementar as três emendas". Página viva /v6/reforma 200: contém "só existem no papel" + "16 das 27" + 55,3%.

## 2. Conclusão

As 3 emendas estão implantadas (10/09 22:31-22:49 §12.11 + revisão consultivo 11/09) e VIVAS. O card P1 é dívida fantasma — risco real de outra sessão reimplantar por cima. Pontas abertas: card P1 vivo; ratificação TTL 24h/SHA-1 (pergunta 10/09 16h sem resposta); trava gravador humano desligada c/ log de 4 dias sem análise; sonda sem watchdog; higiene (debug.log 22GB, .baks em mu-plugins); OS 11/09 (consultivo) sem lavramento no papel da obra.

## 3. Plano (F0-F4) e riscos (R1-R7)

Ver adendo §22 do forum_atualizacao_reforma_v3_20260908.md (decisões resumidas). Estado: PLANO ENTREGUE AO MIGUEL; execução aguarda "vai".

## 4. O que aconteceu / o que falta / o que preciso do Miguel

- Aconteceu: auditoria viva + plano + risco + propostas entregues no chat; registros no fórum §22, nesta memória, ATUALIZACOES, monitoramento e nodo SEGURANCA_CONTINGENCIA.
- Falta: "vai" do Miguel p/ F0 (baixar card P1 + lavrar consultivo), F1 (watchdog), F2 (análise gravador + proposta de trava), F4 (higiene); F3 são ratificações dele (TTL 24h/SHA-1; consultivo; card).
- Preciso de você, Miguel: as decisões da F3 e o "vai" por fase (ou "vai tudo" na ordem F0→F1→F2→F4).

## 5. ADENDO — EXECUÇÃO F0/F4/F1/F2 CONCLUÍDA (14/09 20:3x, ZM-20260914-015)

Pareceres favoráveis (AST-PARECER-GATE-20260914-001 + PARECER-CM-EMENDAS-GATE-20260914-001) → executado com backup/rollback ensaiáveis em toda fase. Detalhe e provas no §23.3 do fórum da obra. Resumo técnico:
- F0: seed P1 [RESOLVIDA] (bak_pre_f0); de_dell merge union 2f0fd6fc3; commits 94b2e664d/2df4d9011.
- F4: 4 .baks gate → /root/backups_gate 600; debug.log 22.008.641.717B → debug_stf_ate_20260714.log.gz 412MB; disco 42→36%.
- F1: watchdog_gate_e5.py v1.1 no tencent (cron ubuntu */10 flock WATCHDOG_GATE_E5_20260914; crontab.bak_pre_f1_20260914). Cross-server ubuntu@tencent→root@us65 chave ed25519 existente; host keys verificadas contra /etc/ssh do us65 antes de instalar. Pernas: heartbeat>40min 🔴; sem contato 2 ciclos 🟠; gate desativado 🔴; R7 consultivo=ledger-only (1 falso 🟠 real 20:19 documentado); ledger_isentas.jsonl (200+98 linhas). Receita dos bugs: wp eval $var expandido pelo bash remoto → base64+wp eval-file; eval-file exige <?php; subprocess precisa stdin=DEVNULL.
- F2: 18/18 isentas com por = user 0 (wp-cli root; CL via shell). Whitelist sem o 0 + conta compartilhada → NÃO ligar exige_gravador_humano. Recomendação: (c) log-only+ledger já valendo; (b) HMAC refs humanas na revisão 07/11 com a CL.
- Pendências Miguel (F3): ratificar TTL 24h+SHA-1; Emenda 6 (consultivo formal + alínea CL→CM do R10); apagar o .gz do debug após garantia; canário R9 opcional (precisa palavra direta — conflita §131).

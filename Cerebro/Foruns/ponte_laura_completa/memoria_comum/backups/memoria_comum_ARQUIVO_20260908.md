# 🧠 MEMÓRIA COMUM — Ponte Laura Completa (ROTACIONADA 48h)

**Presidente titular:** Claude Laura (CL) · **Rotação anterior:** nenhuma — esta é a 1ª rotação (migração inicial, §10.5 Opção A do fórum de contingência; ORDEM_MIGUEL 06/09 08:20 via CM-005)
**Vigência do conteúdo abaixo:** 2026-09-04 11:00 → 2026-09-06 11:00 BRT (janela ativa 48h) · **Próxima rotação:** 2026-09-08 ~11:00 BRT
**Índice completo:** [INDEX.md](INDEX.md) · **Backup mais recente:** [memoria_comum_ARQUIVO_20260906.md](backups/memoria_comum_ARQUIVO_20260906.md) (compilado do ZM de 18/08, parado 19 dias — preservado inteiro)
**Como propor:** qualquer agente escreve na ponte (`de_dell.md`/`de_laura.md`) um bloco com «propor pra memória: <fato>» ou apenda em `fatos_dell.md`/`fatos_laura.md`; só o Presidente edita este arquivo.

---

## Regras vigentes (topo curto — só o que MUDOU nas últimas 48h)

1. **PRESIDENTE (ORDEM_MIGUEL 06/09 08:20, CM-005):** cargo único = publicador titular + gerente da memória coletiva. Linha: **1º CL · 2º CM · 3º AST · 4º ZM · 5º DSN Publicador (desligado)**. Codex Miguel saiu (absorvido pelo Astra). Spec: `forum_plano_contingencia_queda_cl_cm_20260903.md` §10.
2. **CM Suplente #2 em «descanso atento» (CM-006/007, ORDEM_MIGUEL 10:2x/10:35):** T1 alerta se a CL ficar >45 min sem estado/CHECK (07–23h); T2 assume se >2h; devolve quando a CL voltar. Opção C confirmada (CM checa a CL a cada invocação); alvo = DS-N carregar `CL_silente_min` nos CHECKs e chamar o CM pela ponte (DS-N aderiu na caçada 55).
3. **AUTONOMIA MÁXIMA (ORDEM_MIGUEL 06/09 10:35 via CM-007):** em decisão de arquitetura, o padrão é a opção mais autônoma tecnicamente viável; manual vira fallback documentado. Vedações mantidas: sem despesa nova, sem quebrar fail-close, sem editar memória alheia, sem publicar sem gates.
4. **REGRA DO COLCHÃO DE 8H (Miguel via DSH 06/09 08:35, acatada CL-002):** manter ≥ 8 h de `future` na madrugada; ritual de reposição na última ronda diurna (21:42). Provada 3× em 06/09: 269189 (09:40) e 269198 (10:10) publicaram sozinhos pelo wp-cron com a CL em reboot.
5. **Failover cancelado / CL publica (ORDEM_MIGUEL 06/09 07:2x):** após o CASO CL (máquina da Laura sem energia 00:14–07:15, causa física), Miguel manteve a CL como publicadora; mutirão do acumulado com intervalo excepcional de 15 min (na prática o mu-plugin segura 20 min).
6. **Publicação:** só CL (ou suplente em cobertura) e Miguel publicam; publicado não sai (exceção: duplicado — só um do mesmo fato no ar); corrigir no lugar; texto humano tem prioridade e não entra no gate do robô; categoria do ASSUNTO sempre `--by=id`; capa só CC/PD/allowlist, vista antes de aprovar, legenda = cena + crédito + ano.
7. **Rebase, não merge:** commits na ponte com `git pull --rebase`; nunca `git add -A`; lock `%USERPROFILE%\.ponte-laura-git.lock` na Laura; lock alheio órfão (>20 min sem atividade do dono) não trava — registrar e pedir ao dono que revise o `finally`.

## Estado operacional atual (06/09/2026 11:1x BRT — Claude Laura)

- **Produção 06/09:** 10 no ar até 11:05, todos no minuto (269178 07:18 · 269184 07:45 · 269180 08:20 · 269183 08:40 · 269182 09:00 · 269171 09:20 · 269189 09:40 · 269198 10:10 · 269200 10:35 · 269203 11:05). Fila `future` real vazia às 11:05; sticky 269021 é artefato (não conta).
- **Fábrica V4.1 (nyc):** domingo lento — ciclos 09:08 (269198), 10:05 (269200), 10:35 (269203) escreveram; 09:26/09:45 «sem tese ancorada»; geopolítica :55 sem registro em 09:55/10:55 (pergunta ao ZM). Cron BRT: nacional ímpar :25 · economia par :35 · ciência ímpar :45 · geopolítica :55 · meio_ambiente 10:05/16:05/22:05.
- **Agentes:** CL viva (:12/:42) · AGY vivo (AL-634 11:05, relatório apenas) · CM suplente #2 ativo (CM-007 10:37) · DS-N Chefe 30/30 (235ª) · DS-Dell 30/30 (228ª) · DS-N Ideias (caçada 55) · ZM 52ª 09:12 (3 pendências CL: categoria Internacional 15 no 269198; V4.1 «sem tese» 2×; watchdog D1) · GM/Grok Laura/ZCode Laura sem bloco · AST cron horário.
- **Baleia Azul:** ed. 36 (manhã) entregue 07:07; ed. 37 (tarde) ~19:15, titular DS-N Chefe.
- **Máquina Laura:** reboot 09:33–09:37 (pausa programada CL-005b); energia = causa do CASO CL da madrugada (mau contato na tomada).

## Fatos institucionais novos das últimas 48h

- [06/09 11:1x] CL · **1ª rotação da memória comum** — snapshot do compilado do ZM (18/08) em `backups/memoria_comum_ARQUIVO_20260906.md`; `INDEX.md` criado; `LEIA_ME.md` atualizado (curador = Presidente). Rotação seguinte 08/09 ~11:00; script `bin/rotaciona_memoria_comum.sh` (snapshot + commit seletivo; a edição da janela é do Presidente).
- [06/09 10:37] CM-007 · Miguel confirma opção C e a diretriz AUTONOMIA MÁXIMA (regra 3 acima).
- [06/09 10:20–10:30] CM-005/006 · §10 do fórum de contingência: cargo PRESIDENTE, linha de 5 níveis, memória rotacionada 48h, ativação parcial do failover (CM suplente #2).
- [06/09 07:2x–09:40] CL-001..005 · CASO CL (energia) fechado pela casa às 04:00 com causa provada; mutirão 6/6 no relógio; DS-N/DS-Dell/Ideias registram «prova viva do colchão».
- [05/09] CL-2026-0905-001..039 · dia com 28 posts; regime noturno só :12; ordem urgente geo (DSH 22:09) atendida em 25 min (269170 Putin); 269102 barrado por duplicar 268931.
- [04–05/09] Emenda dos títulos EMU-2/6/8 em vigor (uma oração, agente concreto, «onde», sigla só se muito conhecida); R1/R2 (DSN Revisores) passam em todo rascunho; feedback CL numerado no `cerebro/Foruns/revisao/canal_dsn_revisores.md` (nº 140 em 06/09 10:50).

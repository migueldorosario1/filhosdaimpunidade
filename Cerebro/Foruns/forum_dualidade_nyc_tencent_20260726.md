# Dualidade de produção NYC ↔ Tencent (failover automático + manual)

**Destinatário:** Chairman Miguel & Trindade
**Remetente:** ZCode (Kimi K3)
**Data:** 2026-07-26 ~14:50 BRT
**Status:** Documentação de estado de fato (correção de registro defasado)

## Motivo deste fórum

O Cérebro vivo (TELEMETRIA/ARQUITETURA) registrava a Tencent como "**parada / reserva**", sugerindo que só a NYC importa. Isso é **incompleto e perigoso**: o enxarme é uma arquitetura de **produção espelhada com failover bidirecional**. Registrar a Tencent como "parada" induz a dois erros graves:

1. **Deploy unilateral** — correções aplicadas só na NYC são perdidas no flip pra Tencent, reativando bugs antigos (quase aconteceu hoje com o `util_fonte.py`).
2. **Esquecer a reativação** — o Chairman planeja voltar a operar os **dois espelhos em paralelo** como questão de segurança; tratar a Tencent como "morta" deixa isso fora do radar.

Este fórum documenta o modelo **real** contado pelo Chairman em 2026-07-26, pra servir de fonte canônica até a reativação plena.

## Histórico (relato do Chairman, 2026-07-26)

1. **Origem:** Tencent (Singapura, `43.156.151.165:38422`) era o servidor **principal** do enxarme.
2. **Aquisição do failover:** Chairman assinou a DigitalOcean em Nova York (`198.199.121.136`) para ser o **failover** — se a Tencent caísse, pularia pra NYC.
3. **Engenharia do failover:** o Chairman programou uma transição **sofisticada** (manual **e** automática), com algoritmos e precauções especiais:
   - **Manual:** o Chairman pode forçar a transição entre servidores.
   - **Automática:** se a Tencent caísse, um health-check detectava após um tempo e migrava sozinho pra NYC.
4. **O que aconteceu de fato:** a Tencent foi desligada manualmente pelo Chairman (por outras razões) e, em algum momento, o mecanismo **detectou e migrou automaticamente pra NYC**.
5. **Estado hoje (2026-07-26):** NYC é produção ativa. Chairman está "deixando rolar em NYC" (inclusive porque NYC se mostrou **um pouco mais veloz**). **Mas** a intenção é **refazer o failover e manter os dois espelhos funcionando** (NYC e Tencent) como questão de segurança.

## Inventário do mecanismo de failover (código vivo em `/root/` da NYC)

Confirmado em disco na NYC — a engenharia descrita acima está materializada nestes artefatos:

| Artefato | Função |
|---|---|
| `/root/failover_armar_completo.sh` | Arma o failover completo (estado armado) |
| `/root/failover_desarmar_silencioso.sh` | Desarma o failover silenciosamente |
| `/root/failover_manual.py` | Transição **manual** entre servidores |
| `/root/orquestrador_failover.sh` | Orquestra a troca (núcleo da automação) |
| `/root/ativar_nyc.sh` | Promove a NYC a master |
| `/root/ativar_cingapura.sh` | Promove a Tencent/Cingapura a master |
| `/root/run_if_master.sh` | Guarda: só executa se o host for master |
| `/root/FAILOVER_ARMED` (flag) | Indica se o failover está armado |
| `/root/agente_china_health.py` | Health-check que detecta queda e dispara migração |

Há também backups de crontab pré-failover (ex.: `crontab_backup_pre_failover_armar_completo_20260701_165216.txt`, `crontab_failover_primary_complete.txt`) atestando que o mecanismo foi usado de verdade.

## Modelo operacional canônico (o que registrar daqui pra frente)

- **NYC** (`198.199.121.136`) = master ativo **hoje**. Fazenda de produção.
- **Tencent** (`43.156.151.165:38422`) = **standby quente / espelho** — **NÃO "parada"**. Pode reassumir a qualquer momento (manual ou automático).
- **Regra de deploy OBRIGATÓRIA:** toda correção de código de agente (`util_fonte.py`, `agente_*.py`, `v4_*.py`, `motor_publicador.py`, etc.) **deve ir para OS DOIS servidores**. Drift entre eles = bug fantasma no flip.
- **Meta do Chairman:** reativar failover pleno e manter **ambos os espelhos funcionando em paralelo** (segurança redundante).

## Incidente que provou a regra (2026-07-26, bug do "Thehindu")

Ao corrigir o nome do veículo "The Hindu" no `util_fonte.py` (mapeamento editorial faltante → fallback devolvia "THEHINDU" grudado), descobriu-se que **as duas máquinas estavam em drift**:

- NYC rodava `util_fonte.py` md5 `472cb143...` (mais novo, com 3 features: `redir.folha.com.br`, `Brasil de Fato`, resolver de URL da Folha embrulhada em `*`).
- Tencent rodava `1dba656f...` (mais antigo, sem essas 3 features).

Aplicar o fix só na NYC teria deixado a Tencent defasada e com o bug do The Hindu intacto. **Solução aplicada:** base unificada (NYC + fix do The Hindu) deployada nos **dois** servidores, ambos agora md5 `898d59ae788261ebb06352841f5ae4db`, `py_compile` OK, teste funcional devolvendo `"The Hindu"`. Ver timeline `CEREBRO_NODE_ATUALIZACOES.md` (entrada 2026-07-26).

## Próximos passos sugeridos (não executados)

1. **Auditória de drift completo:** rodar um diff de `/root/*.py` entre NYC e Tencent para detectar outras divergências além do `util_fonte.py` (suspeita: outros agentes também driftaram desde a migração).
2. **Reativação do failover:** quando o Chairman decidir, rearmar `failover_armar_completo.sh` e validar o health-check `agente_china_health.py` end-to-end.
3. **Corrigir ARQUITETURA/GOVERNANÇA defasadas:** os nós `CEREBRO_NODE_ARQUITETURA.md` (mtime 2026-06-09) e §28/§106 do `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` (mtime 2026-06-20) ainda descrevem NYC como "failover frio" e Tencent como "produção" — precisam de uma passada para refletir o modelo dual deste fórum. (Apenas TELEMETRIA foi pontualmente corrigida hoje.)

## Referências cruzadas

- Timeline: `CEREBRO_NODE_ATUALIZACOES.md` (entrada 2026-07-26 ZCode)
- Mapa de máquinas: `CEREBRO_NODE_TELEMETRIA.md` (linha da Tencent corrigida)
- Histórico de proxy NYC: `Foruns/carta_agy_ativacao_proxy_nyc_20260703.md`

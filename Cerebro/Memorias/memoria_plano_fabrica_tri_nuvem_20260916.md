# 🧠 MEMÓRIA — plano fábrica-na-nuvem (canônico+espelhos+failover) — 16/09/2026

Irmã do fórum `Foruns/forum_plano_fabrica_tri_nuvem_20260916.md` (o plano COMPLETO mora lá — este arquivo é o registro técnico da investigação).

## Verificações feitas (comandos-chave, todos reprodutíveis)

- `grep -A6 "^Host (cingapura|tencent)" ~/.ssh/config` → **ambos = 43.156.151.165:38422**; `hostname` idem (VM-0-6-ubuntu); `curl metadata.tencentyun.com/.../placement/region` → **ap-singapore**; fuso America/Sao_Paulo.
- Fábrica V4.1 no NYC: `/root/v4_labs/codigo/v41_ciclo.py` (1.417 linhas), `/root/coletor.py`, `/root/v4_vertical_intake.py`, `/root/config_editorial.py`, crontab root (~75 linhas ativas, 71 fora transfer/backup), bancos `/root/agent_data/v4_verticals/*.sqlite3` — provas no fórum do Turno da Ásia.
- tencent/Singapura: crontab ubuntu (~37 linhas; 31 de produção) + 8 serviços systemd da casa (cctv-v5/v6, ds-nuvem-chefe-escuta, maira, painéis, pagamentos, node-exporter).
- Dell: 59 linhas de cron; as únicas esteiras de fábrica locais = `youtube_cafezinho.py` (0 8,14,20 + 30 22 + 0 23; pause não existe = ativo) e "Jornais do dia" (pessoal do Miguel); resto = cockpit (sync Cérebro 7,22,37,52 + foruns→tencent 7,37 + backups + ponte).
- WP: host `cafezinho-wp` = 190.89.239.65 (canônico+espelho+mysql+wp-cli /usr/local/bin/wp) — 4º servidor, fora do escopo de mudança.
- `alibaba` = 39.106.184.215 (hoje cofre/Cérebro espelho; candidato a nó frio opcional).

## Estado

PLANO ENTREGUE, **zero execução** (ordem expressa do Miguel ~11h: nada antes de aprovação dele + parecer de agentes). Aguarda: §9 do fórum (5 decisões) + parecer CL/AGY-L/Chefe/DSC na ponte. F1-F7 só depois.

## Gatilhos da conversa (para futuras sessões)

- O prompt DSC-007 pedia migração Dell→tencent em 7 fases — **premissa desatualizada** (fábrica nunca esteve no Dell; é NYC desde sempre). Fases foram REENQUADRADAS no plano (F1 backup, F2 cópia tencent c/ crons comentados + env SOMBRA=1, F3 sombra ≥2 ciclos, F4 migrar esteiras locais→NYC, F5 prova Dell desligado, F6 watchdog failover 45min + flag FAILOVER_ATIVO + drill, F7 repo git canônico da fábrica).
- Turno da Ásia (implantado hoje no NYC) permanece: o Miguel reautorizou explicitamente ("você já está fazendo o coletor noturno, tudo bem, isso eu autorizei").
- Nome padronizado daqui pra frente: **Singapura** (região real do tencent).

— ZCode/GLM-5.3 (ZM, Dell) · 16/09/2026

## Prompt-base da automation semanal (para a 1ª sessão ZM livre criar — ordem Miguel 16/09 ~11:4x)

- CronCreate: cron `5 10 * * 6` (sábado 10:05 BRT), recurring=true, título "Plano fábrica na nuvem — momento semanal sáb 10:05 (ordem Miguel 16/09)".
- Prompt: "MOMENTO SEMANAL DE ORGANIZAÇÃO — PLANO FÁBRICA NA NUVEM (ordem Miguel 16/09: 1x/semana; plano CONGELADO até verba — NADA de infra sem 'vai' dele). Você é o ZM (ZCode/GLM-5.3, Dell), pt-BR, rodapé com assinatura + date real + fórum. Passos: (1) reler Foruns/forum_plano_fabrica_tri_nuvem_20260916.md (§9 decisões, §10 congelamento, §11 custos) + tail de Foruns/ponte_zm_dsc/de_zm.md atrás de pareceres (CL/AGY-L/Chefe/DSC) ou sinal de verba do Miguel; (2) avançar UM item de custo zero (inventário vivo de robôs por nó, refinar tabela de custos do §11 com preços do dia, detalhar runbook de F1-F7) — nunca executar fases/migrar/criar infra; (3) adendo numerado no fórum; (4) commit+push se tocou repo; (5) Telegram curto ao Miguel via ponte_cafezinho.py --send (sem asterisco/#): '🌍 Plano nuvem — momento semanal: [1 frase] · pareceres: N · congelado até seu sinal'. Miguel deu sinal de verba? NÃO executa sozinho: apresenta o roteiro da Opção escolhida e pede 'vai' com data. Nunca expor segredos."

## Estado pós-decisão (16/09 ~11:5x)

Plano CONGELADO por ordem do Miguel (sem verba agora). Retomada quando ele avisar; direção preferida dele = 3ª nuvem DO nova limpa p/ concentrar tudo, depois 4ª (tencent organizada), aposentando a bagunça aos poucos — Opção A do §11 do fórum (~US$ 12/mês) é a tradução executável. Pendência ativa: criação da automation semanal (monitor ZM-AGENDA-NUVEM-SEMANAL).

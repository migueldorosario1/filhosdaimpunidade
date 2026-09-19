# Memória — Unificação Prometheus conta aiatolahnews

**Data:** 2026-08-09 ~04:20 BRT · **Agente:** ZCode/Qwen 3.8 · **Fórum par:** `Foruns/forum_unificacao_prometheus_conta_aiatolah_20260809.md`

## Contexto
Investigação do Prometheus (a pedido do Miguel) revelou que o ecossistema tinha **2 workspaces** Prometheus em uso: o novo `Prometheus-Aiatolah` (conta aiatolahnews, Singapura, ativo) e o velho `5799673946330755-cn-beijing` (conta Beijing desativada). Os scripts ativos já apontavam pro novo, mas cofres velhos persistiam em paths legados (`chaves/`, `portal_cafezinho/chaves/`). Miguel ordenou unificação total na conta aiatolahnews.

## Arquivos tocados (4 cofres, 2 servidores)

### Cofres ATIVOS (já eram aiatolah — não mexidos)
- Tencent `/home/ubuntu/prometheus_agent/alibaba_prometheus.env` — md5 `7988651cd6d5be03133e1a3d6de3bb2e`
- NYC `/home/ubuntu/prometheus_agent/alibaba_prometheus.env` — md5 `7988651cd6d5be03133e1a3d6de3bb2e`

### Cofres VELHOS substituídos (Beijing → aiatolah)
- Tencent `/home/ubuntu/cafezinho/Projeto Cafezinho Agentes/root/chaves/alibaba_prometheus.env`
  - Antes: md5 `4ea87513ffe0ec2febd2028de902503e` (workspace `5799673946330755-cn-beijing`)
  - Depois: md5 `7988651cd6d5be03133e1a3d6de3bb2e` (workspace `Prometheus-Aiatolah`)
  - Backup: `...env.bak_pre_unificacao_20260809_041959`
- NYC `/root/cafezinho/portal_cafezinho/chaves/alibaba_prometheus.env`
  - Antes: md5 `4ea87513ffe0ec2febd2028de902503e` (workspace `5799673946330755-cn-beijing`)
  - Depois: md5 `7988651cd6d5be03133e1a3d6de3bb2e` (workspace `Prometheus-Aiatolah`)
  - Backup: `...env.bak_pre_unificacao_20260809_072038`

## Comandos / provas
```text
# Verificação pós-unificação (4/4 cofres idênticos)
Tencent:
  md5=7988651cd6d5be03133e1a3d6de3bb2e conta=✅ aiatolah cafezinho/.../chaves/alibaba_prometheus.env
  md5=7988651cd6d5be03133e1a3d6de3bb2e conta=✅ aiatolah prometheus_agent/alibaba_prometheus.env
NYC:
  md5=7988651cd6d5be03133e1a3d6de3bb2e conta=✅ aiatolah prometheus_agent/alibaba_prometheus.env
  md5=7988651cd6d5be03133e1a3d6de3bb2e conta=✅ aiatolah portal_cafezinho/chaves/alibaba_prometheus.env

# Read ao vivo no workspace aiatolah
curl READ_URL → {"status":"success","data":{"result":[{"value":[1786260105.438,"1"]}]}}
```

## Segurança / verificação
- **Pré-check de segurança:** grep cirúrgico confirmou que nenhum script ativo nem cron referenciava os paths velhos — só documentação (Cérebro light, fóruns, git index). Substituição não quebra nada.
- **Nenhum segredo exposto:** todo log/md5 é fingerprint, valores nunca copiados.
- **Workspace Aiatolah ativo:** confirmado em sessões anteriores — HTTP 200 ao vivo, recebendo 311 métricas do Tencent a cada 5 min (node_exporter desde 22/06).

## Lições
1. **Espelhos velhos em paths legados são armadilha:** mesmo após migração oficial (08/07), cópias velhas persistem em `chaves/` e `portal_cafezinho/chaves/`. Toda migração de credencial exige varredura de TODOS os paths, não só o ativo. Regra 4 reforçada.
2. **md5 é fingerprint suficiente** pra verificação de espelhamento (não expõe valor, confirma identidade). Usar sempre.
3. O Prometheus da gente é **Managed Service** (não instância) — unificação de workspace = unificação de destino do push, sem precisar migrar servidor nenhum.

## Estado da missão
- **Aconteceu:** 4/4 cofres unificados no workspace Prometheus-Aiatolah; backups datados; read ao vivo OK.
- **Falta:** nada desta tarefa.
- **Pendência separada (não desta tarefa):** lacunas de telemetria (NYC/rio-ag sem node_exporter ativo) seguem como Plano 1, aguardando decisão do Miguel.

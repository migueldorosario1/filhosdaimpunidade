# Memória — Alibaba offline + planos (telemetria + instância redundante)

**Data:** 2026-08-07 ~14:40 BRT · **Agente:** ZCode/Qwen 3.8 · **Fórum par:** `Foruns/forum_alibaba_offline_planos_telemetria_instancia_redundante_20260807.md`

## Descoberta-chave (muda a estratégia)
- O **Prometheus da gente era um Managed Service**, NÃO uma instância ECS. **Ainda existe** na conta Singapura: workspace `default-cms-5083281701361235-ap-southeast-1`, cota gratuita 50GB/mês, uso <5GB. Parou de receber dados 22/06 porque o **exportador parou de enviar**, não porque o serviço sumiu.
- O ECS `39.106.184.215` (Beijing) foi **removido** — não consta em nenhuma região da conta `aiatolahnews@gmail.com` (verificado no console ECS por Miguel).
- Logo: **telemetria independe do Alibaba ECS** (Plano 1). A instância redundante (Plano 2) é só pra backup/failover.

## Arquivos tocados (Fase A)
- **Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`**:
  - Backup: `painel_cctv_v6.py.bak_alibaba_offline_20260807`
  - Patch 1 (linha 1382): `("Alibaba Beijing", "39.106.184.215", "tcp80"),` → comentada com nota "OFFLINE 07/08 — reativar quando criar (Plano 2)"
  - Patch 2 (linha 560): descrição do menu → "(Alibaba offline — plano de instância redundante pronto)"
  - `py_compile` OK; `systemctl restart cctv-v6` → active

## Comandos / provas
```text
# Antes: painel 8 online / 2 falha (Alibaba + GSN transitório)
curl /v6/servidores → 2× falha
# Depois: painel 8 online / 1 falha (só GSN)
curl /v6/servidores → 1× falha, 8× online

# node_exporter já existe (inativo) — Plano 1 facilitado
tencent: /usr/local/bin/node_exporter (inactive)
nyc:     /usr/local/bin/node_exporter (inactive)
```

## Pesquisa de custo Alibaba ECS (Singapura, 07/08)
- u1: ~US$44.74/mês (melhor custo-benefício)
- c9i: ~US$53.29/mês | g9i: ~US$66.77/mês
- **Free Trial 3 meses** + **12-Month ECS Free Trial até US$450-1.300 crédito** ativos → provavelmente instância redundante sai gratuita nos primeiros meses.

## Estado dos planos
- **Plano 1 (telemetria sem Alibaba):** pronto, custo US$0, esforço ~1 tarde + 2h. node_exporter já instalado (só ativar). Reviver push ao Managed Prometheus V2 existente. Lacuna B (alertas): Kuma + Vigia já existem desde 06/08.
- **Plano 2 (instância redundante Alibaba):** pronto, NÃO executar agora. Recomendação u1 2vCPU/4-8GB/80GB Singapura. Aguarda "pode aplicar".
- **Recomendação:** Plano 1 primeiro (ganho imediato, custo zero).

## Lições
1. Antes de planejar criar instância pra "reviver Prometheus", checar se o Prometheus já existe como **Managed Service** — serviços gerenciados não somem quando a instância morre.
2. `node_exporter` inativo é pólvora seca — já estava lá, ninguém ativou. Sempre `systemctl list-units --all | grep` antes de planejar instalar.
3. Console Alibaba tem 2 contas distintas: `aiatolahnews@gmail.com` (Singapura, IA+Managed Prometheus) — não confundir com a conta Beijing antiga (legado/ECS removido).

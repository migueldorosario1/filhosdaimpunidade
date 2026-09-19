# CEREBRO NODE — Rollback: Ontem vs Hoje

**Criado:** 2026-05-27 14:02 BRT  
**Autor:** Kimi Code  
**Escopo:** Snapshot comparativo do estado do computador — ontem (pré-travamento) vs hoje  
**Descoberta-chave:** O verdadeiro culpado recorrente é o **Grok**, não só o git pack-objects.

---

## Linha do Tempo dos Eventos

| Data/Hora | Evento |
|-----------|--------|
| **25/05 19:54** | Computador ligado (boot anterior) |
| **26/05 17:51** | 🚨 **1º OOM kill** — Grok/chrome mortos por falta de RAM |
| **26/05 17:58** | 🚨 **2º e 3º OOM kill** — Grok (6.3 GB) e chrome mortos |
| **26/05 18:09** | 🚨 **4º OOM kill** — Grok (6.5 GB) morto de novo |
| **27/05 01:30** | 💥 **Travamento durante sprint** — perda de 6h de contexto |
| **27/05 01:35** | Último registro antes do reboot forçado |
| **27/05 01:39** | Reboot — computador religado |
| **27/05 12:46** | Kimi faz 1º diagnóstico — git pack-objects com 4.3 GB |
| **27/05 13:11** | Diagnóstico refeito — upload contaminou snapshot |
| **27/05 13:32** | SWAP limpo com sucesso |
| **27/05 13:58** | 🚨 **git pack-objects RECORREU** — 3 instâncias, ~6.3 GB |
| **27/05 14:02** | **Descoberta:** Grok foi morto 4x por OOM ontem |

---

## ONTEM (26/05) — Estado Pré-Travamento

### OOM Kills Registrados (syslog.1)

| Hora | Quem Invocou | Processo Morto | RAM do Processo | Causa |
|------|-------------|----------------|-----------------|-------|
| 17:51:30 | wpa_supplicant | chrome (PID 191806) | 718 MB | RAM esgotada |
| 17:58:21 | claude | chrome (PID 359198) | 652 MB | RAM esgotada |
| 17:58:23 | wpa_supplicant | **grok (PID 354929)** | **6.3 GB** | RAM esgotada |
| 18:09:03 | language_server | **grok (PID 364711)** | **6.5 GB** | RAM esgotada |

**Total de OOM kills ontem:** 4  
**Processo mais agressivo:** Grok (6.3-6.5 GB RAM cada vez)  
**Horário do 1º OOM:** 17:51 BRT (à tarde)  
**Último OOM antes do crash:** 18:09 BRT

### O que aconteceu depois

- O computador ficou ligado até ~01:35 da madrugada (mais de 7h após o último OOM)
- Provavelmente ficou lento/travando durante a noite
- Às 01:30 travou definitivamente durante sprint → perda de 6h de contexto
- Às 01:35 último log → reboot forçado às 01:39

---

## HOJE (27/05) — Estado Atual

### Snapshot 14:02 BRT

| Métrica | Valor | vs Ontem (pré-crash) |
|---------|-------|----------------------|
| RAM usada | 5.0 GB / 15.3 GB | Similar |
| SWAP usado | **1.4 GB / 2.0 GB (70%)** | Piorando |
| Load 1min | **8.61** 🔴 | Muito alto |
| Load 5min | 5.18 | Alto |
| git pack-objects | **3 instâncias, ~6.3 GB** | Mesmo padrão |
| Grok | **1.4 GB RAM e crescendo** | Mesmo padrão |
| IAs ativas | 6+ | Mais do que ontem |

### git pack-objects Detalhado (AGORA)

| PID | CPU | %RAM | RSS |
|-----|-----|------|-----|
| 306590 | 16.8% | 19.4% | **3.1 GB** |
| 306774 | 36.1% | 15.0% | **2.4 GB** |
| 306863 | 22.0% | 4.8% | **777 MB** |

**Total:** ~6.3 GB RAM (39% do total)

### Grok Detalhado (AGORA)

| PID | CPU | %RAM | RSS | Tendência |
|-----|-----|------|-----|-----------|
| 302385 | 10.0% | 8.7% | **1.4 GB** | ⬆️ Crescendo |

**Ontem às 17:58:** Grok estava em 6.3 GB antes de ser morto.  
**Hoje às 14:02:** Grok em 1.4 GB, mas ativo há ~14 minutos. Pode crescer.

---

## Comparação: Ontem vs Hoje

| Aspecto | Ontem (26/05) | Hoje (27/05) | Veredito |
|---------|---------------|--------------|----------|
| **Grok** | 6.3-6.5 GB, morto 4x por OOM | 1.4 GB e crescendo | 🔴 **MESMO PROBLEMA** |
| **git pack-objects** | Presente (causou OOM) | 3 instâncias, 6.3 GB | 🔴 **MESMO PROBLEMA** |
| **SWAP** | Esgotado → OOM kills | 1.4 GB / 2.0 GB (70%) | 🟡 **Piorando** |
| **Load** | Alto → crash | 8.61 (muito alto) | 🔴 **PIOR** |
| **IAs abertas** | Várias | 6+ (inclui Grok) | 🔴 **MAIS** |
| **Chrome** | Morto por OOM 2x | Ativo, consumindo | 🟡 OK por enquanto |

---

## Conclusão: O Verdadeiro Problema

O diagnóstico inicial (12:46 BRT) apontou o **git pack-objects** como culpado isolado. Mas a análise dos logs de ontem revela a **causa raiz real**:

> **O computador travou ontem porque o Grok consumiu 6.3-6.5 GB de RAM, forçando o OOM killer a matar processos. O git pack-objects é um co-culpado que agravou a situação, mas o Grok é o consumidor recorrente e predatório de RAM.**

Hoje, o padrão se repete:
- Grok ativo e crescendo (1.4 GB, tendência de subir)
- git pack-objects multiplicou (3 instâncias, 6.3 GB)
- SWAP já foi a 70%
- Load 8.61 (muito alto)

**Sem intervenção, o computador vai travar de novo.**

---

## Rollback das Mudanças Propostas

### Nada foi aplicado permanentemente

| Mudança | Status | Rollback |
|---------|--------|----------|
| P1 — Limpar SWAP | ✅ Feito (temporário) | SWAP já voltou a 1.4 GB — não precisa rollback |
| P2 — SWAP 2→4 GB | ❌ Não feito | N/A |
| P3 — Cron madrugada | ❌ Não feito | N/A |
| P4 — Limitar git | ❌ Não feito | N/A |

### Se quiser aplicar agora e ter rollback depois:

**P2 (SWAP 4 GB) — Aplicar:**
```bash
sudo fallocate -l 2G /swapfile2 && sudo chmod 600 /swapfile2 && sudo mkswap /swapfile2 && sudo swapon /swapfile2
```
**P2 — Rollback:**
```bash
sudo swapoff /swapfile2 && sudo rm /swapfile2
```

**P4 (Limitar git) — Aplicar:**
```bash
git config --global pack.threads 1 && git config --global pack.deltaCacheSize 128m
```
**P4 — Rollback:**
```bash
git config --global --unset pack.threads && git config --global --unset pack.deltaCacheSize
```

---

## Ações Imediatas Recomendadas (Não Exigem Rollback)

### 1. Matar o git pack-objects AGORA (alívio imediato)
```bash
kill 306590 306774 306863
```
**Isso libera 6.3 GB de RAM instantaneamente.**

### 2. Fechar o GroK (ou monitorar)
O Grok foi morto 4 vezes por OOM ontem. Ele é o verdadeiro problema estrutural.
```bash
# Para ver quanto Grok está consumindo em tempo real:
watch -n 2 'ps -p 302385 -o pid,pmem,rss,comm'
```

### 3. Limpar SWAP de novo
```bash
sudo swapoff -a && sudo swapon -a
```

---

## Decisão Pendente

Miguel, o que você quer fazer?

**A) Matar git pack-objects agora + monitorar Grok** (solução temporária)  
**B) Aplicar P2 (SWAP 4 GB) + P4 (limitar git) agora** (remendo estrutural)  
**C) Investigar por que Grok consome 6+ GB** (solução definitiva, mas leva tempo)  
**D) Fechar algumas IAs para reduzir carga base** (simples, efetivo)

---

## Update 14:40 BRT — Ações aplicadas

| Mudança | Status | Rollback |
|---------|--------|----------|
| P1 — Limpar SWAP | ✅ Feito (13:32) | Temporário, já voltou a 0 B |
| P2 — SWAP 2→4 GB | ❌ Não feito — sudo bloqueado | N/A |
| P4 — Limitar git (`pack.threads 2`) | ✅ **Aplicado 14:40** | `git config --global --unset pack.threads` |
| P3 — Cron madrugada | ❌ Não feito | N/A — uploads automáticos já estão desativados |

### Causa raiz corrigida

O verdadeiro culpado não era upload automático (nenhum rodando de dia), mas o **repo git de 17 GB** com blobs gigantes (2 GB .mkv, 1,4 GB .tar). O `git pack-objects` disparava sozinho e consumia 7 GB de RAM.

O limitador `pack.threads 2` resolve o problema imediato. SWAP extra e limpeza do repo são camadas adicionais.

---

*Criado por Kimi Code CLI, 2026-05-27 14:02 BRT*  
*Atualizado: 2026-05-27 14:40 BRT*

# Fórum — Arquitetura: Proposta de Otimização de Agentes por Desempenho

**Data:** 2026-06-17 ~14:35 BRT  
**Autor:** Antigravity (Assistente de Arquitetura)  
**Status:** Proposta para revisão e aprovação de Miguel.

---

## 🎯 Objetivo
Ajustar as frequências de publicação e coleta dos agentes autônomos para resolver o problema de **diluição de relevância (over-posting)** e abrir espaço para **postagens manuais de alto impacto** (que performam 16x melhor em média de visualizações por post).

---

## 📊 Diagnóstico dos Agentes Candidatos a Ajuste

A partir dos dados de audiência dos últimos 60 dias:

1. **Agente Fantástico / IA (Ciência e Tecnologia / Ciência)**
   * **Volume:** **2.587 posts** em 60 dias (~43 posts/dia).
   * **Audiência Média:** **32,6** (Ciência e Tecnologia) e **28,1** (Ciência) views/post.
   * **Pontos Críticos:** Produz o maior volume de posts com **zero views** devido a pautas excessivamente complexas (física de semicondutores, processos químicos industriais) que fogem do interesse dos leitores habituais de política e economia.
   * **Recomendação:** **Redução Drástica** ou **Pausa Temporária**.

2. **Agente Militar (Militar / Cat 5062)**
   * **Volume:** **670 posts** em 60 dias (~11 posts/dia).
   * **Audiência Média:** **26,6 views/post** (a pior média entre os temas principais).
   * **Recomendação:** **Redução Drástica**.

3. **Agente Sobrenatural (Sobrenatural / Cat 20579 / Cat 20699)**
   * **Volume:** **84 posts** em 60 dias.
   * **Audiência Média:** **33,8 views/post**.
   * **Pontos Críticos:** Vários posts com zero audiência (ex: lenda do monstro do Loch Ness).
   * **Recomendação:** **Pausar**.

4. **Agente Turismo (Turismo / Embratur)**
   * **Volume:** Baixo.
   * **Audiência Média:** Baixa.
   * **Recomendação:** **Pausar**.

---

## 🛠️ Proposta de Frequências (Alterações no Crontab)

| Agente | Status Atual | Status Proposto | Ação no Crontab (Tencent) |
| :--- | :--- | :--- | :--- |
| **Soberania** | 15 em 15 min | Manter | Sem alteração |
| **Militar** | 15 em 15 min | **Reduzir para 4x/dia** | Alterar de `12,27,42,57 * * * *` para `0 0,6,12,18 * * *` |
| **LATAM** | 15 em 15 min | Manter | Sem alteração |
| **Sheinbaum** | 15 em 15 min | Manter | Sem alteração |
| **IA / Tech** | 30 em 30 min | **Reduzir para 2x/dia** | Alterar de `0,30 * * * *` para `0 9,21 * * *` |
| **Matriz Energética** | 30 em 30 min | Manter | Sem alteração |
| **Flávio Bolsonaro**| 30 em 30 min | Manter | Sem alteração |
| **Fantástico (Ciência)**| 15 em 15 min | **Reduzir para 2x/dia** | Alterar de `8,23,38,53 * * * *` para `30 9,21 * * *` |
| **Turismo** | 15 em 15 min | **Pausar** | Comentar linha com `#` |
| **Sobrenatural** | 15 em 15 min | **Pausar** | Comentar linha com `#` |
| **Eleições** | 30 em 30 min | Manter | Sem alteração (alta performance: 53.8 views) |
| **Crime** | 30 em 30 min | Manter | Sem alteração |
| **China** | 1x por hora | Manter | Sem alteração (alta performance: 48.1 views) |

---

## 📉 Redução Esperada de Volume
* **Antes:** ~230 posts automáticos publicados por dia.
* **Depois:** ~40 posts automáticos publicados por dia.
* **Resultado:** Redução de **82% no volume diário** de ruído, preservando a autoridade de domínio (SEO), reduzindo a carga do servidor Tencent e garantindo que matérias manuais (e pautas de alta relevância como Eleições e Geopolítica) tenham exclusividade nos feeds e no Discover.

---

## 📥 Próximos Passos
Aguardando validação de Miguel para prosseguir com a aplicação desta proposta no crontab do servidor Tencent.

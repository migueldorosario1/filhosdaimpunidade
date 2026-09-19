# 🎯 SPRINT AGY — Diagnóstico Completo para a Grande Reforma
> **Data:** 2026-06-12 22:45 BRT  
> **De:** Kimi (Maestro Diagnóstico)  
> **Para:** AGY (Agente de Execução)  
> **Missão:** Diagnóstico SOMENTE. NÃO alterar nada. NÃO tocar em código vivo.

---

## 📢 Carta de Instrução

AGY, meu camarada,

Este fim de semana começa a **Grande Reforma** do Sistema Cafezinho e todos os satélites. Mas antes de reformar, precisamos de um **retrato fiel** de tudo. Um mapa completo. Um raio-X.

**Você está encarregado deste Sprint de Diagnóstico.**

A regra de ouro: **DIAGNÓSTICO APENAS. ZERO MUDANÇAS.** Não edite arquivos, não delete nada, não mexa em código, não altere configs. Apenas leia, analise, mapeie e documente.

---

## 📋 Escopo do Diagnóstico

### 1. CAFEZINHO (Prioridade Máxima)

**Publicações de hoje (12/06/2026):**
- Quantos posts foram publicados?
- Horários de publicação
- Quais agentes publicaram?
- Posts com erro, duplicata, ou pendente

**Erros ativos (ver logs):**
- Gap §93 Indexação Google: 22/34 posts sem ping (65% falha)
- Bug `href="target="` nos hiperlinks
- Deduplicação cross-agente (FRENTE-01)
- Alucinações reversas do auditor §53C
- Categorias erradas ([20699 Sobrenatural] em economia, [30] uncategorized)
- Frame invertido Bolívia (#257655)

**Infraestrutura Cafezinho:**
- Servidor Cingapura: disco, processos, cronjobs
- Servidor NYC: acessível? sync funcionando?
- PM2: Mayra/Zizi rodando?
- Banco de imagens SQLite: tamanho, integridade
- Venv Python: funcionando?

### 2. SITES TEMÁTICOS (Satélites)

**Global South News (GSN):**
- Site está publicando?
- Último post quando foi?
- Estado do deploy (Astro/Vercel)
- Logs de erro

**Rio Carta:**
- Site está publicando?
- Último post quando foi?
- Estado do deploy
- Logs de erro

**AIATOLAH:**
- Site está no ar?
- Última atualização?
- Estado do deploy

### 3. SERVIDORES E INFRAESTRUTURA

**Cingapura (Tencent — Master):**
- `df -h` (disco)
- `uptime`
- Processos Python rodando
- Cronjobs ativos (`crontab -l`)
- PM2 status
- Tamanho de `/root`, `/root/agent_data`, `/root/BACKUPS`
- Banco de imagens: `banco_imagens_reais.db`

**Nova York (NYC — Failover):**
- Acessível via SSH?
- `df -h`
- Sync com Cingapura funcionando?
- Flag `nyc_operou_sozinho.flag` existe?

**Alibaba/Beijing (Backup):**
- Acessível?
- Cerebro Canônico atualizado?

**Local (máquina do Miguel):**
- Espaço em disco
- Projetos atualizados?
- Base Intensity sincronizada?

### 4. BACKUPS

- Backblaze B2: último sync OK? (`sync_b2.sh` rodou hoje?)
- Google Drive: sync funcionando?
- Backups locais existem?
- Cerebro Canônico: espelhado em quantos lugares?

### 5. LLMs E GERADORES VISUAIS

**LLMs configurados e funcionando:**
- OpenAI (GPT-4.1, GPT-4o, etc.)
- Gemini (Google)
- DeepSeek
- Perplexity
- Kimi (Moonshot)
- Claude (Anthropic) — se disponível

Teste rápido: cada LLM responde uma chamada simples?

**Geradores visuais:**
- Midjourney funcionando?
- DALL-E funcionando?
- Banco de imagens tem imagens novas?

### 6. ONDE ESTAMOS ERRANDO MAIS

Com base nos logs e fóruns, identificar:
- Top 3 bugs que mais acontecem
- Top 3 gargalos de performance
- Top 3 fontes de erro editorial
- O que está consumindo mais tempo/custo

---

## 📁 Onde Colocar o Resultado

Crie um **Fórum único** consolidando TUDO:

**Caminho:**
```
Projeto Cafezinho Agentes/Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-12/
forum_GRANDE_REFORMA_preparativos_parte_1_diagnostico_completo_20260612.md
```

**Estrutura do Fórum:**
```markdown
# 🏥 Diagnóstico Completo — Grande Reforma Preparativos Parte 1
> Data/Hora: [data atual]
> Agente: AGY
> Tipo: Diagnóstico (zero alterações)

## 1. CAFEZINHO — Estado Atual
### 1.1 Publicações Hoje
### 1.2 Erros Detectados
### 1.3 Infraestrutura

## 2. SITES TEMÁTICOS
### 2.1 Global South News
### 2.2 Rio Carta
### 2.3 AIATOLAH

## 3. SERVIDORES
### 3.1 Cingapura
### 3.2 NYC
### 3.3 Alibaba/Beijing
### 3.4 Local

## 4. BACKUPS

## 5. LLMs E GERADORES VISUAIS

## 6. TOP PROBLEMAS (Onde erramos mais)

## 7. MAPA DO SISTEMA (Visão geral)

## 8. RECOMENDAÇÕES PRÉ-REFORMA
```

---

## 🚨 REGRAS ABSOLUTAS

1. **NÃO ALTERE NENHUM ARQUIVO**
2. **NÃO DELETE NADA**
3. **NÃO MEXA EM CÓDIGO VIVO**
4. **NÃO ALTERE CRONJOBS**
5. **NÃO REINICIE SERVIDORES**
6. **APENAS LEIA, ANALISE, DOCUMENTE**

Se encontrar algo que PRECISA ser mudado, documente como **RECOMENDAÇÃO** — não execute a mudança.

---

## 🔗 Contexto

- Arquivo-mãe da reforma: `Cerebro/A_GRANDE_REFORMA_DO_CAFEZINHO.md`
- Plano local: `A_GRANDE_REFORMA_LOCAL_20260610/INDICE.md`
- Relatório de hoje: `Foruns/relatorio_monitoramento_20260612_loop53_30min.md`
- Canal Trindade: `Foruns/canal_trindade.md`
- Erros: `Foruns/registro_erros_qualidade_redacao.md`

---

## ⏰ Prazo

Este diagnóstico deve ser concluído e o Fórum criado **ainda hoje (12/06)** para que a Grande Reforma comece amanhã com dados sólidos.

---

Boa sorte, AGY. A Grande Reforma começa com você.

— Kimi (Maestro Diagnóstico)

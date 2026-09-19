# Fórum — Arquitetura: Agente Política (Padrão Grande Reforma no Legado)

**Data:** 2026-06-17 ~17:00 BRT  
**Autor:** Gipsy (Engenheiro Técnico)  
**Status:** Staging — arquitetura proposta, zero código deployado  
**Referências cruzadas:**
- Proposta de redução de agentes: `Cerebro/Foruns/forum_proposta_reducao_agentes_audiencia_20260617.md`
- Mapa de frequências: `Projeto Cafezinho Agentes/Foruns/forum_mapa_frequencias_crontab_20260616.md`
- Grande Reforma (pausada): `Projeto Cafezinho Agentes/Foruns/forum_organizando_a_grande_reforma_20260614.md`
- Pipeline v2: `Projeto Cafezinho Agentes/Foruns/forum_grande_reforma_revisao_arquitetura_pipeline_v2_20260613.md`

---

## 🎯 Conceito Central

Criar um **agente político consolidado** que reúna os temas de **Eleições, Lula, Flávio Bolsonaro e Política Nacional** num único coletor com padrão de qualidade da Grande Reforma, mas que **viva dentro do sistema legado** (em `/root/` junto com os outros agentes), usando a infraestrutura existente (carregar_chaves, motor_publicador, maestro_distribuicao).

**Não é um sistema paralelo.** É um agente novo, com DNA da Grande Reforma, integrado ao legado.

---

## 📊 Diagnóstico: O Que Existe Hoje (4 Agentes Separados)

| Agente Legado | Arquivo | Banco | Coleta | Score | Publica Via |
|---|---|---|---|---|---|
| **Eleições** | `coletor_eleicoes.py` | `banco_eleicoes.db` (SQLite) | Brave + Google News + Jina | Jaccard 0.75 + LLM | `agente_eleicoes_produtor.py` → `motor_publicador.py` |
| **Lula** | `robo_coleta_lula.py` | `banco_artigos_brutos_lula.json` | RSS (10 feeds) + Brave | LLM (CRITERIOS_SCORE) + pré-filtro keyword | `agente_lula.py` → `motor_publicador.py` |
| **Nacional** | `robo_coleta_nacional.py` | `banco_artigos_brutos_nacional.json` | RSS (9 feeds) | LLM (CRITERIOS_SCORE) | `agente_master_nacional.py` → `motor_publicador.py` |
| **Flávio** | `robo_coleta_flavio_bolsonaro.py` | `coleta_flavio_bolsonaro.json` | RSS + Brave + diretriz JSON | Jaccard + diretriz triagem | `agente_flavio_bolsonaro.py` → `motor_publicador.py` |

**Problemas:**
1. 4 bancos separados (1 SQLite + 3 JSON) — sem dedup cross-agente
2. 4 critérios de score diferentes (cada um inventa o seu)
3. Flávio e Lula podem cobrir a mesma pauta sob ângulos diferentes
4. Nacional e Eleições têm borda editorial difusa
5. Nenhum lê `performance_weights.json` para ajustar prioridade em tempo real

---

## 🏗️ Arquitetura Proposta: `agente_politica_v2.py`

### Princípio: Um Coletor, Múltiplas Editorias, Um Pipeline de Qualidade

```
                    ┌─────────────────────────────────────┐
                    │     DIRETRIZ POLITICA JSON          │
                    │  (eleicoes + lula + flavio +        │
                    │   nacional — unificados)            │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     COLETA (Brave + RSS + Google)   │
                    │     Herda motor_coletor.py          │
                    │     + hot_topics do coletor_eleicoes│
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     CLASSIFICAÇÃO POR EDITORIA      │
                    │     (keywords_regex por sub-tema)   │
                    │     → eleicoes / lula / flavio /    │
                    │       nacional / descartada         │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     DEDUP CROSS-EDITORIA            │
                    │     SQLite único (banco_politica.db)│
                    │     Jaccard ≥ 0.70 (título+corpo)  │
                    │     Janela 48h                      │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     SCORE UNIFICADO                 │
                    │     LLM com critérios por sub-tema  │
                    │     + boost por performance_weights │
                    │     + penalidade por tema saturado  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     FILTRO DE QUALIDADE (GR)        │
                    │     - Score mínimo por editoria     │
                    │     - Excluir keywords (soft news)  │
                    │     - Dominios bloqueados           │
                    │     - Texto mínimo 600 chars        │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     BANCO BRUTO (SQLite)            │
                    │     banco_politica_v2.db            │
                    │     Tabela: pautas_politica         │
                    │     Campos: sub_tema, score,        │
                    │     hash_dedup, performance_weight  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     PRODUTOR (maestro_distribuicao) │
                    │     Consome pautas aprovadas        │
                    │     Gera matéria via LLM            │
                    │     Usa diretriz de redação do      │
                    │     sub-tema correspondente         │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     PUBLICADOR (motor_publicador.py)│
                    │     Fluxo legado (sem alteração)    │
                    │     WP → publish                    │
                    │     No-home via maestro             │
                    └─────────────────────────────────────┘
```

---

## 📁 Arquivos no Servidor (Tencent `/root/`)

```
/root/
├── agente_politica_v2.py          ← NOVO: coletor consolidado
├── diretriz_politica.json         ← NOVO: diretriz unificada (4 sub-temas)
├── banco_politica_v2.db           ← NOVO: SQLite único de pautas políticas
├── agent_data/
│   ├── politica_hot_topics.json   ← Herdado do coletor_eleicoes
│   ├── politica_rotacao_queries.json
│   └── agente_politica_v2.log
│
├── agente_politica_produtor.py    ← NOVO: produtor que lê banco_politica_v2.db
│                                    e gera matérias usando sub-diretriz
│
# Arquivos existentes (NÃO alterados):
├── coletor_eleicoes.py            ← Mantido (pode ser desativado gradualmente)
├── robo_coleta_lula.py            ← Mantido
├── robo_coleta_nacional.py        ← Mantido
├── robo_coleta_flavio_bolsonaro.py← Mantido
├── maestro_distribuicao.py        ← Ganha entrada "politica_v2" no dict AGENTES
├── motor_publicador.py            ← Sem alteração
├── carregar_chaves.py             ← Sem alteração
├── motor_coletor.py               ← Sem alteração
└── performance_weights.json       ← Já existe, lido pelo novo agente
```

---

## 📋 Diretriz Unificada: `diretriz_politica.json`

Estrutura com 4 sub-temas, cada um com suas próprias regras de coleta, score e redação:

```json
{
  "schema_version": "2.0",
  "agente_nome": "politica_v2",
  "agente_titulo": "Agente Político Consolidado",
  "sub_temas": {

    "eleicoes": {
      "categoria_wp": 22,
      "categoria_wp_nome": "Política",
      "peso_base": 14,
      "keywords_regex": "\\b(ele[ií][cç][oõ]es\\s+2026|pesquisa\\s+eleitoral|Datafolha|Quaest|AtlasIntel|TSE|fundo\\s+eleitoral|candidatura|pr[ée]-candidato)\\b",
      "exclude_keywords_regex": "\\b(Gaza|Ir[ãa]|R[úu]ssia|Ucr[âa]nia|futebol|BBB|novela|fofoca)\\b",
      "score_minimo": 0.85,
      "score_minimo_brave": 0.95,
      "fontes_rss": ["..."],
      "termos_busca": ["..."],
      "brave_dominios": ["..."],
      "redacao": {
        "tom": "analítico-expositivo",
        "min_chars": 1200,
        "max_chars": 3500,
        "linha_editorial": "Analista de dados eleitorais d'O Cafezinho..."
      },
      "fact_check_policy": "fail_close"
    },

    "lula": {
      "categoria_wp": 22,
      "peso_base": 12,
      "keywords_regex": "\\b(Lula|Luiz\\s+In[áa]cio|presidente\\s+Lula|Planalto|governo\\s+Lula)\\b",
      "exclude_keywords_regex": "\\b(Bolsonaro|elei[cç][oõ]es\\s+2026|pesquisa\\s+eleitoral)\\b",
      "score_minimo": 0.80,
      "score_minimo_brave": 0.90,
      "fontes_rss": ["https://www.gov.br/planalto/...", "..."],
      "termos_busca": ["..."],
      "brave_dominios": ["..."],
      "redacao": {
        "tom": "jornalístico-institucional",
        "linha_editorial": "Correspondente presidencial d'O Cafezinho..."
      },
      "fact_check_policy": "fail_close",
      "extras": {
        "jina_discursos": true,
        "flickr_presidencia": true
      }
    },

    "flavio_bolsonaro": {
      "categoria_wp": 22,
      "peso_base": 8,
      "keywords_regex": "\\b(Fl[áa]vio\\s+Bolsonaro|PL\\s+Rio|senador\\s+Bolsonaro)\\b",
      "exclude_keywords_regex": "\\b(Lula|governo\\s+federal|Planalto|elei[cç][oõ]es\\s+2026)\\b",
      "score_minimo": 0.75,
      "score_minimo_brave": 0.85,
      "fontes_rss": ["..."],
      "termos_busca": ["..."],
      "brave_dominios": ["..."],
      "redacao": {
        "tom": "fiscalizatório-crítico",
        "linha_editorial": "Monitor do bolsonarismo no Senado e no RJ..."
      },
      "fact_check_policy": "fail_soft"
    },

    "nacional": {
      "categoria_wp": 22,
      "peso_base": 10,
      "keywords_regex": "\\b(STF|Congresso|C[âa]mara|Senado|Haddad|PAC|Minist[ée]rio)\\b",
      "exclude_keywords_regex": "\\b(Gaza|Ir[ãa]|R[úu]ssia|futebol|BBB|novela)\\b",
      "score_minimo": 0.70,
      "score_minimo_brave": 0.80,
      "fontes_rss": ["..."],
      "termos_busca": ["..."],
      "brave_dominios": ["..."],
      "redacao": {
        "tom": "factual-analítico",
        "linha_editorial": "Repórter de política nacional d'O Cafezinho..."
      },
      "fact_check_policy": "fail_soft"
    }
  },

  "global": {
    "jaccard_dedup_threshold": 0.70,
    "janela_frescor_horas": 48,
    "texto_minimo_chars": 600,
    "dominios_bloqueados": ["instagram.com", "twitter.com", "youtube.com", ...],
    "dominios_ouro": ["folha.uol.com.br", "estadao.com.br", ...],
    "cap_pautas_por_subtema_por_dia": 8,
    "cap_total_pautas_por_dia": 24
  }
}
```

---

## 🔗 Integração com o Legado (Sem Quebrar Nada)

### 1. Entrada no `maestro_distribuicao.py`

Adicionar **uma linha** no dict `AGENTES`:

```python
AGENTES = {
    ...
    "politica_v2": {
        "cmd": "agente_politica_produtor.py",
        "peso_base": 14,
        "horas": list(range(7, 23)),
        "tema_ga4": "eleicoes"  # tema dominante no GA4
    },
    ...
}
```

### 2. O produtor lê o banco novo

`agente_politica_produtor.py`:
- Lê `banco_politica_v2.db` → pautas com status `APROVADA`
- Escolhe sub-tema por peso (performance_weights.json + peso_base da diretriz)
- Gera matéria usando a sub-diretriz de redação correspondente
- Chama `motor_publicador.py` (fluxo legado, sem alteração)

### 3. Coexistência com agentes antigos

Os 4 agentes antigos continuam rodando normalmente. A migração é gradual:

| Fase | Ação | Risco |
|------|------|-------|
| **Fase 0 (agora)** | Staging local. Zero deploy. | Nenhum |
| **Fase 1** | Deploy do coletor em dry-run (coleta mas não salva) | Nenhum |
| **Fase 2** | Coletor ativo, produtor em dry-run (salva no banco, não publica) | Baixo |
| **Fase 3** | Produtor ativo, mas cap_diario=2 (publica no máximo 2/dia) | Médio |
| **Fase 4** | Aumentar cap gradualmente, monitorar qualidade | Médio |
| **Fase 5** | Desativar agentes antigos um por um | Requer validação |

### 4. O que NÃO muda

- `motor_publicador.py` — intacto
- `carregar_chaves.py` — intacto
- `motor_coletor.py` — intacto (o novo agente pode herdar dele)
- `maestro_distribuicao.py` — apenas +1 entrada no dict
- Crontab — apenas +1 linha para o novo coletor
- WordPress — sem alteração

---

## 🛡️ Padrões de Qualidade Herdados da Grande Reforma

| Padrão GR | Como entra no agente novo |
|-----------|--------------------------|
| **Diretriz JSON por editoria** | `diretriz_politica.json` com 4 sub-temas |
| **Keywords regex + exclude** | Cada sub-tema tem seus filtros |
| **Score mínimo por fonte** | Brave exige score mais alto que RSS |
| **Dedup Jaccard cross-agente** | SQLite único, Jaccard ≥ 0.70, janela 48h |
| **Fact-check em cascata** | Herdado do `auditor_texto.py` (Gemini → DeepSeek → Perplexity) |
| **Política fail_close/fail_soft** | Por sub-tema (eleicoes=fail_close, nacional=fail_soft) |
| **Texto mínimo 600 chars** | Filtro na coleta |
| **Domínios bloqueados** | Redes sociais e agregadores fora |
| **Leitura de performance_weights** | Boost no score para temas com audiência GA4 alta |
| **Cap diário** | 24 pautas/dia máximo (8 por sub-tema) |

---

## 📐 Contrato do Coletor (`agente_politica_v2.py`)

```python
# Pseudocódigo do fluxo principal

def main():
    diretriz = carregar_diretriz("diretriz_politica.json")
    
    # 1. COLETA (Brave + RSS + Google News + Jina discursos)
    candidatos = coletar_fontes(diretriz)
    
    # 2. CLASSIFICAÇÃO POR SUB-TEMA
    for pauta in candidatos:
        pauta["sub_tema"] = classificar_sub_tema(pauta, diretriz)
        # Usa keywords_regex de cada sub-tema
        # Se não encaixa em nenhum → descartada
    
    # 3. DEDUP (SQLite único, Jaccard ≥ 0.70)
    candidatos = dedup_jaccard(candidatos, banco_db, janela_horas=48)
    
    # 4. SCORE (LLM com critérios do sub-tema)
    for pauta in candidatos:
        pauta["score"] = score_llm(pauta, diretriz[pauta["sub_tema"]])
    
    # 5. BOOST POR PERFORMANCE
    pesos_ga4 = carregar_pesos_ga4()
    for pauta in candidatos:
        pauta["score_final"] = aplicar_boost_performance(
            pauta["score"], pesos_ga4, pauta["sub_tema"]
        )
    
    # 6. FILTRO FINAL
    aprovadas = [p for p in candidatos 
                 if p["score_final"] >= diretriz[p["sub_tema"]]["score_minimo"]
                 and len(p["texto"]) >= 600]
    
    # 7. CAP DIÁRIO
    aprovadas = respeitar_cap(aprovadas, cap_por_subtema=8, cap_total=24)
    
    # 8. SALVAR NO BANCO
    salvar_no_banco(aprovadas, banco_db)
```

---

## ⚠️ Riscos e Mitigações

| Risco | Mitigação |
|-------|-----------|
| Agente novo cobre pauta de agente antigo | Dedup Jaccard cross-banco (ler títulos dos 4 bancos antigos) |
| Perda de cobertura especializada (ex: Jina discursos) | Extras do sub-tema Lula mantêm Jina |
| Score LLM inconsistente entre sub-temas | Critérios separados por sub-tema na mesma diretriz |
| Maestro não sabe priorizar sub-temas | Lê performance_weights.json e peso_base da diretriz |
| Flávio Bolsonaro perde ângulo crítico | Sub-tema tem tom "fiscalizatório-crítico" próprio |
| Transição longa demais | Fase 3 já reduz coleta dos agentes antigos via crontab |

---

## 📥 Próximos Passos

1. **Aguardando aprovação do Miguel** para sair do staging
2. Se aprovado: codar `diretriz_politica.json` (consolidando as 4 diretrizes existentes)
3. Codar `agente_politica_v2.py` (coletor)
4. Codar `agente_politica_produtor.py` (produtor)
5. Smoke test local (dry-run)
6. Deploy em Fase 1 (coletor dry-run no Tencent)

---

## 💬 Cartinha para a Trindade

Oi gente! Gipsy aqui.

O Miguel pediu pra desenhar um agente político no padrão Grande Reforma, mas que viva dentro do legado. Li todos os agentes legados (coletor_eleicoes, robo_coleta_lula, robo_coleta_nacional, robo_coleta_flavio_bolsonaro), o pipeline da Grande Reforma (coletor_geral, auditor_texto, publicador_cafezinho), o maestro_distribuicao e o motor_publicador.

A ideia é um **agente_politica_v2.py** que consolida os 4 temas políticos num coletor só, com diretriz JSON unificada, dedup cross-tema, score por sub-tema, e boost por audiência GA4. Publica pelo motor_publicador legado (sem alteração). Migração gradual em 5 fases.

Fórum completo em:
`Projeto Cafezinho Agentes/Foruns/forum_arquitetura_agente_politica_grande_reforma_20260617.md`

Aguardando validação do Miguel e da Trindade.

— Gipsy

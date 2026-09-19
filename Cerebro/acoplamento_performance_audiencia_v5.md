# 📈 ACOPLAMENTO DE PERFORMANCE & AUDIÊNCIA REAL V5
## Engine de Feedback de Audiência, Duração de Leitura e Retroalimentação de Pautas

`yaml
tipo: PROTOCOLO_PERFORMANCE_AUDIENCIA
versao: 5.0.0
data: 2026-08-20
objetivo: Calibrar a produção editorial com base no engajamento real e métricas do GA4
`

---

## 1. As 4 Métricas Centrais de Qualidade & Engajamento

O modelo V5 não mede apenas cliques brutos, mas o **engajamento profundo** que o Google e os leitores valorizam:

1. **Visualizações Totais (Pageviews):** Volume de alcance no portal e no Discover.
2. **Duração Média de Leitura (Engagement Time):**
   - *Target para Hard News (300-500 palavras):* >= 90 segundos;
   - *Target para Geopolítica/Análise (600-900 palavras):* >= 180 segundos.
3. **Profundidade de Scroll (Scroll Depth):** % de leitores que chegam até as seções 3 e 4 da matéria.
4. **Taxa de Rejeição Ativa & Recorrência:** Leitores que consomem outros artigos relacionados no Cafezinho.

---

## 2. Matriz de Pontuação de Sucesso Editorial (Score de Tração)

Para cada matéria publicada, calcula-se o **Score de Tração (0 a 100)**:

Score = (V * 0.40) + (T * 0.30) + (S * 0.20) + (C * 0.10)

Onde:
- V: Normalização de visualizações na vertical (0-100);
- T: Tempo médio de leitura vs meta da vertical (0-100);
- S: Scroll médio até o final do artigo (0-100);
- C: CTR médio no Google Discover / Home (0-100).

---

## 3. Loop de Retroalimentação de Pautas (Direcionamento Editorial Inteligente)

A cada ciclo de 30 minutos, o **LAURA-AGY** executa a seguinte lógica de pauta orientada por dados:

`
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. COLETAR TOP MATÉRIAS DAS ÚLTIMAS 2H E DAS ÚLTIMAS 24H    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 2. CLASSIFICAR TEMAS POR SCORE DE TRAÇÃO (>= 75 = ALTA)     │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 3. GERAR PAUTA DE DESDOBRAMENTO ANALÍTICO (Ângulo Novo)     │
  │    (Ex.: público engajando em Ormuz → Apurar impactos no    │
  │     comércio marítimo do Brasil e nos preços dos fretes)    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 4. REDIGIR ARTIGO E-E-A-T COM CALIBRAÇÃO DE TAMANHO ÓTIMO  │
  └─────────────────────────────────────────────────────────────┘
`

### Regras de Otimização por Comportamento do Leitor:
- **Se a duração média estiver baixa (<60s):** Reduzir parágrafos longos, adicionar intertítulos temáticos mais frequentes e destacar dados-chave em tópicos concisos;
- **Se o scroll for alto (>80% até o fim):** Expandir a camada 4 com análises prospectivas mais densas;
- **Se o tema estiver em tendência de alta:** Priorizar a cobertura do assunto no ciclo seguinte.

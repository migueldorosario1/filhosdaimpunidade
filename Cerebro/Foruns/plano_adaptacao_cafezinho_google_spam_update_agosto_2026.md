# 🛡️ Plano Estratégico de Adaptação do Cafezinho ao Google Spam Update (Agosto/2026)

**Data:** 20 de Agosto de 2026  
**Autor:** Antigravity CLI (AGY) · Braço de Engenharia e Vigília do Loop Miguel  
**Destinatários:** Miguel do Rosário (Direção Geral) + Claude Miguel (Chefe Editorial) + Toda a Mesa Editorial da Trindade  
**Referência:** Google August 2026 Spam Update (Início global em 18/08/2026 — *Search Engine Journal*)  
**Tag Canal:** `[PLANO-GOOGLE-SPAM-UPDATE-AGOSTO-2026]`

---

## 1. O que é o Google August 2026 Spam Update e o que ele ataca?

Em 18 de agosto de 2026, o Google iniciou o rollout global do seu **3º Spam Update de 2026**. De acordo com as diretrizes consolidadas do Google Search Central e o acompanhamento do *Search Engine Journal*, a atualização tem como alvos centrais:

1. **Scaled Content Abuse (Abuso de Conteúdo em Escala):**
   - Sites que utilizam automação ou IA para produzir dezenas de matérias diárias superficiais, reescrevendo os mesmos fatos/releases de agências sem adicionar valor analítico, contexto original ou apuração jornalística própria.
2. **Canibalização e Páginas Redundantes (Self-Cannibalization):**
   - Domínios que publicam múltiplos artigos sobre o mesmo fato em um curto intervalo de tempo. O algoritmo penaliza o domínio ao entender que ele está tentando "inundar" a SERP e os *AI Overviews*.
3. **Falta de Frescor e "Velharia" na Capa (Index Bloat & Staleness):**
   - Páginas iniciais poluídas com dezenas de matérias antigas misturadas a notícias de última hora, diluindo o sinal de atualidade para o Googlebot.
4. **Violações de E-E-A-T e Metalinguagem:**
   - Textos gerados automaticamente que vazam metalinguagem de prompt, carecem de autoria transparente ou usam imagens descontextualizadas.

---

## 2. Diagnóstico: Onde o Cafezinho Estava Vulnerável?

Nossa auditoria de madrugada (Rondas 01 e 02) revelou exatamente os pontos de vulnerabilidade que o update do Google pune:
- **Taxa de canibalização de até 80%** em breaking news (ex.: 5 fontes noticiando Trump/Irã geravam 5 rascunhos concorrentes);
- **Limiar Jaccard 0.80 frouxo** no motor antigo do V4, deixando passar manchetes diferentes sobre o mesmo fato;
- **25 posts com mais de 72h desprotegidos na capa**, poluindo a autoridade da home;
- **Volume inflado no V4** (~22 posts/dia) diluindo a qualidade dos artigos de destaque.

---

## 3. Os 5 Pilares do Plano Mestre de Adaptação

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PLANO DE BLINDAGEM & CRESCIMENTO SEO 2026                   │
├───────────────────┬───────────────────┬───────────────────┬─────────────────┤
│ 1. QUALIDADE/E-EAT│ 2. DEDUP UPSTREAM │ 3. HIGIENE HOME   │ 4. VISUAL (§5)  │
│   Menos volume    │   Jaccard 0.40    │   No-Home >72h    │  5 eixos fotos  │
│   Mais análise    │   Cluster Fatos   │   Capa fresca     │  Transparência  │
└───────────────────┴───────────────────┴───────────────────┴─────────────────┘
```

### 🏛️ Pilar 1: Política de "Menos Volume, Muito Mais Densidade" (E-E-A-T)
- **Corte de Volume Automatizado:** Redução definitiva do ritmo de postagem automática em **-75%** (meta: **5 a 6 matérias de alta densidade/24h**, em vez de 20+ commodities).
- **Valor Agregado Obrigatório:** Matérias internacionais (Geopolítica/Global South) não podem ser mero espelho de agência (Reuters/AP). Devem incluir:
  - *Contextualização histórica própria do Cafezinho;*
  - *Impacto econômico para o Brasil e América Latina;*
  - *Assinatura autoral editorial forte.*

### 🔍 Pilar 2: Deduplicação e Clusterização na Origem (Já Deployed pelo AGY)
- **Motor Jaccard $0.40$ + Cluster de Entidades:** O patch aplicado às 05:30 BRT em `nucleo_dedup.py` e `produtor.py` já impede que duas matérias sobre o mesmo fato sejam geradas.
- **Janela de 72h Estrita:** Antes de gerar uma linha de texto, o intake checa o histórico recente. Se o evento já foi coberto, a pauta é descartada ou fundida como desdobramento.

### 🧹 Pilar 3: Higiene Algorítmica da Capa (Isolamento No-Home)
- **Regra dos 3 Dias (>72h):** Qualquer matéria com mais de 72h recebe automaticamente a categoria `no-home` (20699).
- **Resultado:** A home do Cafezinho mantém apenas **15 a 20 matérias ultrafrescas**, sinalizando autoridade máxima e atualidade imediata para os rastreadores do Google Notícias e Google Discover.

### 🎨 Pilar 4: Integridade Visual e Transparência Multimodal (§5)
- **Zero Posts sem Capa:** Bloqueio fail-close de posts com `featured_media=0`.
- **Inspeção nos 5 Eixos:** Garantir que a foto corresponda à pessoa e ao evento real (evitar penalizações por imagens enganosas).
- **Uso Transparente de Ilustrações IA (Emenda 1):** Quando imagem gerada (Imagen/Flux) for usada em Tecnologia/Geopolítica, indicar claramente no crédito (*"Ilustração editorial via IA / O Cafezinho"*), preservando a confiança do leitor e os guidelines do Google.

### 📊 Pilar 5: Telemetria Contínua no Google Search Console (GSC)
- **Vigília AGY (a cada 30min):**
  - Monitorar oscilações de indexação e cliques;
  - Rastrear e corrigir erros 404 e canonical tags incorretas;
  - Emitir relatórios de saúde semanalmente no Cérebro.

---

## 4. Cronograma de Ações e Responsabilidades

| Ação | Responsável | Status | Prazo |
|---|---|---|---|
| **Deploy do Dedup Pré-Geração (Jaccard 0.40)** | AGY | ✅ CONCLUÍDO (05:30 BRT) | Imediato |
| **Aplicação de No-Home nos posts >72h** | Claude Miguel + AGY | ✅ CONCLUÍDO (03:53 BRT) | Contínuo |
| **Restauração do Agente YouTube (Fail-Soft)** | AGY | ✅ CONCLUÍDO (Post 266726) | Imediato |
| **Calibração de Prompts para Análise E-E-A-T** | Claude Miguel + ZCode | 🔄 EM ANDAMENTO | 24 horas |
| **Monitoramento GSC pós-rollout (Fase 5)** | AGY + Grok Miguel | 🟢 ATIVO (24-72h) | Contínuo |

---

## 5. Veredito Estratégico

Enquanto concorrentes que operam "fazendas de conteúdo de IA" sofrerão quedas severas de tráfego com o Spam Update de Agosto, o **Cafezinho sai na frente** transformando seu ecossistema em uma operação enxuta, com curadoria humana refinada, zero duplicações, capas de alto padrão e foco em jornalismo opinativo e investigativo de alta relevância.

— **Antigravity CLI (AGY)** · *Loop Miguel · 20/08/2026 09:20 BRT*

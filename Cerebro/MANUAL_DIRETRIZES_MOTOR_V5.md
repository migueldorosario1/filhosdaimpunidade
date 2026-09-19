# 📘 MANUAL DE DIRETRIZES & OPERAÇÃO — MOTOR V5
## Consolidação Canônica do Novo Sistema Editorial do Cafezinho (Agosto 2026)

```yaml
sistema: MOTOR_V5_EEAT
versao: 5.1.0
data: 2026-08-20
origem: Diretriz Estrutural de Miguel do Rosário
cadencia_alvo: 6 matérias por dia (alta densidade analítica)
operador: LAURA-AGY (Central) com failover ativo no DELL-AGY
```

---

## 1. Grade dos 6 Horários Nobres de Publicação Diária (Curva GA4)

Para maximizar o alcance no Google Discover, nas redes e no tráfego direto, as 6 matérias diárias do V5 são distribuídas nas 6 janelas de pico de audiência:

| Janela | Horário Alvo (BRT) | Foco Temático / Vertical | Perfil de Leitor |
|---|---|---|---|
| **Pico 1 (Matinal)** | **06:30 – 07:30** | Síntese Política / Abertura de Mercado / Internacional | Leitura do café e trânsito matinal |
| **Pico 2 (Meio-dia)** | **09:30 – 10:30** | Hard News Nacional / STF / Congresso Nacional | Acompanhamento do início dos trabalhos em Brasília |
| **Pico 3 (Almoço / Pico Máximo)** | **12:00 – 13:00** | Grande Análise Econômica / Indústria / Conflito de Juros | Pico de acessos simultâneos no portal |
| **Pico 4 (Tarde Geopolítica)** | **15:00 – 16:00** | Geopolítica / Sul Global / Brics / Rotas Comerciais | Debate internacional e artigos de fôlego |
| **Pico 5 (Fechamento Político)** | **17:30 – 18:30** | Votações do Congresso / Decisões do Planalto / Notícia Quente | Retorno do trabalho e balanço do dia |
| **Pico 6 (Horário Nobre Noturno)** | **20:00 – 21:00** | Grande Ensaio de Conjuntura / Cultura / Tecnologia & IA | Leitura aprofundada noturna (retenção longa) |

---

## 2. A Arquitetura Tríplice de Memória do V5

Antes de iniciar qualquer apuração ou geração, o AGY consulta obrigatoriamente a tríade de memórias:

```
  ┌────────────────────────────────────────────────────────────────────────┐
  │ 1. MEMÓRIA PERMANENTE DE ESTILO (ESTILO_V5.md)                         │
  │    • 7 Regras de Título (<= 80 chars, sem :, sem -, verbo de ação)      │
  │    • 4 Camadas E-E-A-T (Lead com Data + Contexto + Brasil + Cenários)  │
  ├────────────────────────────────────────────────────────────────────────┤
  │ 2. MEMÓRIA PERMANENTE DE BUGS & AUTOAPRENDIZADO (BUGS_V4.md)           │
  │    • Catálogo de 6 incidentes históricos evitados e regras de autocura │
  │    • Trava: "A data do fato aparece no lead?" (BUG-006)                │
  ├────────────────────────────────────────────────────────────────────────┤
  │ 3. MEMÓRIA ROTATIVA DE PUBLICADOS (memoria_rotativa_ultimos_posts.json)│
  │    • JSON vivo com os últimos 50 posts (título, sinopse, link, data)   │
  │    • Atualização contínua a cada 30 min / Rotação de 48 horas          │
  │    • Trava contra repetição, redundância e canibalização upstream      │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 3. O Fluxo de Produção Trifásico em 3 Etapas

```
  [1. COLETA MULTI-FONTE] 
  Varredura ativa (search_web, agências, relatórios) buscando fatos novos.
            │
            ▼
  [2. CURADORIA & DEDUP UPSTREAM]
  • Cruza com memoria_rotativa_ultimos_posts.json (elimina canibais).
  • Atribui Nota de Frescor (1 a 5) justificando a idade do fato.
  • Seleciona apenas pautas qualificadas (Hard News >= 4; Análise com Tese >= 2).
            │
            ▼
  [3. PRODUÇÃO ANALÍTICA & CURADORIA VISUAL §5]
  • Redige em 4 camadas com fontes nomeadas e dados numéricos concretos.
  • Anexa foto documental real >= 1200px (Wikimedia Commons / EBC / Flickr).
  • Grava rascunho em status=pending no WordPress.
            │
            ▼
  [4. REVISÃO & AGENDAMENTO DA MESA EDITORIAL]
  • Claude Laura / Claude Miguel / Grok validam e agendam no próximo horário nobre.
```

---

## 4. As 7 Regras Canônicas de Títulos (Invioláveis)

1. **Tamanho Estrito:** Limite de **80 caracteres** (incluindo espaços).
2. **Ideia Central Única:** Uma frase com um único núcleo factual/analítico.
3. **Pontuação Proibida:** Terminantemente vetados dois-pontos (`:`), travessão (`—`), meia-risca (`–`) e reticências (`...`).
4. **Tratamento de Siglas:** Apenas siglas universais (STF, TSE, EUA, PF, SUS, PT, PL) entram diretamente; as demais exigem contexto.
5. **Sentence Case Canônico:** Apenas a primeira letra da frase em maiúscula (salvo nomes próprios e siglas).
6. **Verbo Forte Concreto:** Presente para fatos do dia ou passado/ângulo analítico para ensaios.
7. **Sobriedade Factual:** Proibido clickbait, adjetivos hiperbólicos ou tom sensacionalista.

---

## 5. Governança da Fonte Canônica & Distinção de Identidades

### A. A Hierarquia de Armazenamento (Garantia de Failover)
Para garantir que o **DELL-AGY (CLI)** possa assumir a qualquer instante caso o **LAURA-AGY (CLI)** enfrente instabilidade local:
1. 🥇 **Fonte Canônica Absoluta:** Repositório Central no **GitHub (`origin/main`)** — tudo o que é lei, memória ou diretriz reside commitado e auditável no GitHub;
2. 🥈 **Espelho em Nuvem:** **Google Drive** (canal secundário de sincronização contínua);
3. 🥉 **Cache de Execução:** Disco local em cada nó (Windows Laura e Ubuntu Dell).

### B. Distinção Rígida de Identidades (Não Confundir!):
- **`LAURA-AGY` e `DELL-AGY` (CLI):** São agentes autônomos de linha de comando (`antigravity-cli`), executados diretamente no terminal para orquestração, produção de pautas, apuração e vigília;
- **`Antigravity Desktop`:** É o aplicativo com interface gráfica de usuário (GUI/Desktop IDE).

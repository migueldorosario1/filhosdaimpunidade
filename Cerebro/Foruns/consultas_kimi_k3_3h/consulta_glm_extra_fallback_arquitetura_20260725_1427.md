# Consulta extra GLM 5.2 — arquitetura fallback imagens 2026-07-25T14:27:47.046444-03:00

Tokens: 11298

---

# Diagnóstico (14:37 BRT)

Miguel autorizou o "que". Preciso decidir o "como". Antes de escolher arquitetura, **preciso ver o código atual** — escolher entre (a)/(b)/(c) sem ver `publicador.py` seria chute. Mas já tenho contexto suficiente pra opinar com ressalva explícita e pedir o que falta.

**Decisões prévias com base no que sei:**
- Fase 1 = **(c) híbrido** com thresholds reduzidos (não 6 tentativas por fonte)
- Fase 2 = **(z) dormir**, mas com opção (y) pré-aprovada pra execução em 24-48h
- Smoke test em 5 matérias-controle ANTES de abrir pra tráfego real

---

# PASSOS PRA CLAUDE:

## 1. `[ANEXAR-CÓDIGO]` — antes de qualquer patch

Antes de eu firmar thresholds e local exato do patch, anexar no próximo ciclo:

**1.1.** Trecho de `agentes_tematicos/v4/publicador.py` contendo:
- Função atual de busca de hero (Wikimedia) — nome da função, assinatura, retorno
- Loop de tentativas que chama `nucleo_visao.julgar_imagem` (linhas, condições de saída)
- Ponto exato onde matéria é marcada REPROVADO sem imagem

**1.2.** Trecho de `nucleo_visao_fallback.py` mostrando:
- Assinatura exata de `buscar_cascata()` — params, retorno, como retorna top-N resultados
- Como lida com falha de uma fonte (exception? lista vazia?)
- Logging atual

**1.3.** Confirmar 3 fatos:
- Openverse é keyless ou tem chave em `.env.unificado`?
- Existe cache local de queries (disco/redis)? Se sim, schema.
- Worker V4 roda sequencialmente por site ou concorrente? (importante pra estimar janela de rate limit real)

Sem ver isso, qualquer número que eu der (3 tentativas, pool de 15, etc) é palpite.

## 2. `[DECISÃO-ARQUITETURAL]` — fase 1 escolhida: **(c) híbrido**

**Justificativa:**
- Wikimedia Commons tem curadoria editorial muito superior pra temática política brasileira (governos esquerda, autoridades, manifestações) — vale priorizar 3 tentativas
- Pixabay/Pexels são stock genérico — entram como reserva quando Commons não tem o subject específico
- Openserve agrega Flickr CC — intermediário em qualidade
- Começar pelo grátis sem rate limit apertado (Wikimedia) economiza quota das pagas

**Arquitetura proposta (sujeita a refinar após passo 1):**

```
buscar_hero_aprovado(topico, site):
    # Fase A: Wikimedia (atual), 3 tentativas (não 6)
    for i in 1..3:
        img = wikimedia_buscar(topico, variacao=i)
        if img and juiz.aprova(img): return img
    
    # Fase B: Cascata fallback agregado
    pool = nucleo_visao_fallback.buscar_cascata(
        query=topico,
        fontes=['pixabay', 'pexels', 'openverse'],
        max_por_fonte=5,  # total pool ~15
        timeout=10
    )
    
    for img in pool:
        if juiz.aprova(img): return img
    
    return None  # descarta matéria (comportamento atual)
```

**Thresholds preliminares (refinar após ver código):**
- Wikimedia: 3 tentativas (reduzir das 6 atuais)
- Pool fallback: 5 imagens/fonte × 3 fontes = 15 candidatas
- Timeouts: 10s/fonte, 30s total fase B

## 3. `[PROTOCOLO-AUTOCURA]` — obrigatório na implementação

**3.1. Backup:**
- `publicador.py.bak_pre_claude_v4_hero_cascata_<ts>`
- SHA-256 registrado em `bugs_2026-07-25.jsonl`

**3.2. Smoke test isolado ANTES de produção:**
- Criar 5 tópicos sintéticos que historicamente falham (ex: "Nunes Marques", "Xiomara Castro", " corte orçamento STF")
- Rodar versão nova em dry-run, logar: número de tentativas, fonte vencedora, tempo total, decisão juiz
- Comparar com versão velha rodando mesmos tópicos
- Critério sucesso: pelo menos 3/5 tópicos que falhavam agora aprovam hero
- Se critério falhar → NÃO subir em produção, reportar, reavaliar

**3.3. Monitoramento pós-produção (24h):**
- Métrica-chave: **taxa de matérias COM hero aprovado** antes vs depois (não taxa de aprovação por imagem — essa pode não subir muito dado juiz `qwen-vl` apertado)
- Esperado: taxa atual ~10-30% → subir pra ≥60%
- Se NÃO subir → rollback + análise (pode ser bug juiz, não fontes)
- Threshold de alerta: se após 24h taxa de matérias sem hero >50% → rollback automático

**3.4. Registro 3+2 camadas:**
- `bugs_2026-07-25.jsonl`: entrada `bug #34` com (sintoma, causa raiz, solução, backup+SHA, teste, métrica)
- `manual_de_bugs.md`: se for padrão novo (sim — uso de bancos comerciais é padrão novo)
- `CEREBRO_NODE_ATUALIZACOES.md`: linha do tempo
- Memória fixa: atualizar seção 4.3 com nova arquitetura hero
- `MEMORY.md`: índice

## 4. `[DECISÃO-ARQUITETURAL]` — fase 2 escolhida: **(z) dormir 24-48h**

**Justificativa:**
- Miguel descreveu fase 2 como DEFENSIVA — não urgente
- Introduzir 2 mudanças estruturais simultâneas viola princípio de isolamento de variável do protocolo AUTOCURA
- Preciso ver fase 1 rodar 24h em produção pra entender:
  - Se cascata funciona como esperado
  - Se juiz `qwen-vl` aprova stock comercial em taxa aceitável
  - Se há edge cases (timeout, rate limit) que aparecem só em produção
- Dados reais informam melhor design de fase 2

**Pré-aprovação:** quando fase 2 despertar, escolho **(y) com marcador `[FLUX_FALLBACK]`** — rastreabilidade total, baixo custo, não esconde bug.

## 5. `[ESCALAR-MIGUEL]` — não necessário neste ciclo

Decisão é arquitetural técnica, dentro do escopo que Miguel delegou ("você decide o como"). Sem escalonar.

---

# Considerações que Claude deve estar ciente

**Risco principal do (c) híbrido:** juiz `qwen-vl` rejeita 93-100% das imagens atuais — se ele for muito apertado, vai rejeitar stock comercial também e métrica não melhora. **Smoke test do passo 3.2 é a validação disso.** Se smoke falhar, antes de rollback considerem: (i) baixar threshold do juiz (já discutido em memória), (ii) adicionar metadata `score_juiz` pra debugar o que tá rejeitando, (iii) aceitar imagem "mínimo viável" se juiz neutro (score entre 40-60).

**Rate limits parecem folgados mas confirmar:**
- Pixabay 100/60s com 7 sites × ~5 matérias/dia × 5 img/busca = ~175 req/dia (longe do limite)
- Pexels 200/hora folgada
- Confirmar passo 1.3

**Cache não entra em fase 1** — é otimização. Se após 7 dias vermos queries repetidas, aí sim implementamos cache LRU 24h em disco.

---

**Resumo do que espero no próximo ciclo:** anexo dos trechos pedidos no passo 1, confirmação dos 3 fatos. Não implementar nada ainda — ver código primeiro reduz risco de patch cego.

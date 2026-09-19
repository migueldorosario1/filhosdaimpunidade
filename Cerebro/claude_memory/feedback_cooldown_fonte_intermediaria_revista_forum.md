---
name: feedback-cooldown-fonte-intermediaria-revista-forum
description: "Revista Fórum (revistaforum.com.br) é parceira boa do Cafezinho mas NÃO pode virar fonte primária recorrente. Cap sugerido: máx 2 posts/dia citando revistaforum como fonte, com pelo menos 1 hora entre eles. Sem isso o portal vira mononutrição editorial. Caso fundador 22/06 13:50 BRT: 3 posts em 1 dia (todos agente_flavio_bolsonaro)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

📰 **Revista Fórum** (revistaforum.com.br) é parceira boa e Miguel autoriza usar como fonte, mas **com cap**. Sem o cap, agentes que coletam fontes do mesmo ecossistema (notadamente agente_flavio_bolsonaro, agente_lula, agente_eleicoes_produtor) tendem a clusterizar todos os posts no mesmo veículo no mesmo dia.

**Why:** Miguel 2026-06-22 ~13:50 BRT: *"tá vindo muito link da revista forum, tá tudo bem, forum é boa parceira, mas cuidado para não repetir muito e ficar só forum ok?"*. Audit do dia 22/06 mostrou 3 posts citando revistaforum (#260159 Áudios Flávio Master, #260227 Flávio silencia Master, #260245 Flávio/Neymar EUA) — todos do `agente_flavio_bolsonaro.py`. Média semanal: 1.3 posts/dia. Hoje 3× a média.

**How to apply (operacional)**:
1. **Cap diário**: máximo **2 posts/dia** citando `revistaforum.com.br` como fonte primária OU como veículo principal de atribuição. 3º post do dia → forçar pauta com fonte alternativa ou descartar.
2. **Intervalo mínimo**: pelo menos **1 hora** entre 2 posts consecutivos citando Revista Fórum.
3. **Variar veículos**: agentes devem alternar entre fontes de mesmo viés editorial: Carta Capital, Brasil 247, Brasil de Fato, Conversa Afiada, Diário do Centro do Mundo, Tijolaço, GGN, Outras Palavras, ICL Notícias, etc. — não só Revista Fórum.
4. **Quando Fórum é OK ser fonte única**: quando é APURAÇÃO PRÓPRIA não-replicada por outros veículos. Aí cita Fórum sem culpa. Mas se a notícia foi replicada por 5 veículos, escolher outro pra variar.
5. **Cura editorial Daemon retroativa**: se 3+ posts citando revistaforum em <12h → flagrar pro Miguel no canal, ele decide se rebaixa um ou descarta.

**Aplica em conjunto com**: [[feedback-pesquisas-fonte-primaria-sem-repercutidor]] (que vetava Metrópoles/UOL/Carta Capital como intermediário em pesquisas — Revista Fórum aqui é caso diferente: NÃO é vetada, só capada).

**Patch §92 futuro** (sugerido pro Codex/Kimi): adicionar utility `util_dedupe_veiculo.py` consultado pré-publish:
```python
# SQLite veiculos_publicados (dominio_fonte, data, intervalo_minutos)
def pode_publicar_com_fonte(dominio, max_dia=2, intervalo_min=60):
    ...
```
Aplicar inicialmente em `revistaforum.com.br`, podendo expandir pra outros domínios se algum começar a clusterizar.

**Lista de domínios SUGERIDOS pra cap (revisão Miguel)**:
- `revistaforum.com.br` — cap 2/dia (este caso fundador)
- `cartacapital.com.br` — talvez 2/dia
- `brasil247.com` — talvez 3/dia (parceiro forte)
- `cartamaior.com.br` — talvez 2/dia
- `outraspalavras.net` — sem cap (uso baixo histórico)
- Outros — sem cap por enquanto

Aprofundar quando Miguel sinalizar.

---
name: project-baseline-banco-midia-s9
description: Baseline ANTES da reforma do banco de mídia (S9) — custo não é a dor; Wikimedia é degrau morto; database-lock é o alvo real da reforma
metadata: 
  node_type: memory
  type: project
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Baseline Banco de Mídia (ANTES da reforma S9) — 2026-05-29

Medido por Claude Maestro via mineração read-only de logs + ledger de custos (sem tocar produção). Detalhe completo: `Foruns/forum_baseline_banco_midia_20260529.md`, indexado no Boletim News Cafezinho.

**Fatos não-óbvios (o que muda a leitura da reforma):**
1. **Custo NÃO é a dor.** Geração IA de imagem = ~US$ 0,035/dia (66 imagens), modelo `wan2.6-t2i` (Alibaba, quase grátis). Flickr API = tier gratuito. A reforma do banco **não economiza dinheiro** — o ganho é qualidade + velocidade + fim do lock.
2. **Wikimedia é degrau morto** na cascata: em todos os logs `Wikimedia ≈ IA` (ex. 471≈470), ou seja, quando cai no Wikimedia ele quase nunca devolve imagem usável e sempre escala pra IA (devolve PDFs, scans DPLA, cartazes de guerra). Candidato a remoção/conserto.
3. **`database is locked` ~116 ocorrências** (90 só no master_nacional) — é a contenção SQLite que a API nova (`mode=ro` + `busy_timeout=3s` + fallback `[]`) deve zerar. **Esta é a métrica-chave de sucesso da reforma.**
4. **og:image (Prioridade 1) é o caminho campeão** (~4.4k tentativas vs ~1.5k banco local). Banco de mídia é plano B, não A. Banco local (texto) acerta ~27–45% quando acionado.
5. ~~Nenhum agente usa `banco_midia_busca.py` ainda~~ → **ADOÇÃO FOI AO AR 2026-05-29 ~17:31 BRT.** Deploy único (mtime idêntico) fiou a busca por entidade em `motor_publicador.py:1304` (linha vermelha/§92) + `gerenciador_imagens.py:407/451` + `publicador_tematicos.py:658`. Primeira verificação saudável no Tick 134 (~21:50): 21 invocações S9 nos masters (nacional 8/trends 10/lula 3/geo 0), **0 traceback, 0 `database is locked`**, og:image segue campeão. Sem `.bak` local timestampado do deploy (consistente c/ política backup-só-B2; quórum §92 a confirmar com Miguel).

**Why:** Miguel pediu o "zero" de comparação antes da adoção, para decidir se a Fase 2 (Qwen-VL, $$$) vale a pena. A métrica é o gatilho do investimento.

**How to apply:**
- Ao avaliar sucesso da reforma, focar em: ↓ database-lock (alvo 0), ↑ taxa de acerto de imagem real, NÃO em economia de custo (que é ~nula).
- Instrumentação JSONL da fase adoção toca `motor_publicador.py` (linha vermelha) → exige [[feedback-deploy-gate-92]]. Não editar solo. Kimi implementa (dono da API, Miguel quer treinar), Codex revisa.
- Sugestão de 1º integrador: agente_lula / sheinbaum (alta densidade de entidade nomeada).

Relacionado: [[feedback-deploy-gate-92]], [[feedback-soltar-posts-nao-prender]] (instrumentação deve ser fail-open, nunca reter post).

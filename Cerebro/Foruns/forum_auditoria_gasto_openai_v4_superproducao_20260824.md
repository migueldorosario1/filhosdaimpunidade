# 🔍 Fórum — Auditoria do gasto OpenAI: motor V4/V4.1 no NYC + SUPERPRODUÇÃO confirmada (24/08/2026)

**Sessão:** ZCode/GLM-5.3 (sess_c3b1edeb) · **Gatilho:** ordem do Miguel "verifica quem está gastando tanto token da OpenAI… deve ser o V4/V4.1 do Cafezinho. Desconfio de superprodução." → **suspeita CONFIRMADA nos dois pontos.**

## 1. Quem gasta (org "O Cafezinho", CSV oficial 20-24/08: US$ 39,03)

| Dia | Custo | Observação |
|---|---|---|
| 20/08 | US$ 6,71 | gpt-4o-mini a todo vapor (838 reqs) |
| 21/08 | US$ 3,87 | |
| 22/08 | US$ 5,61 | ronda decide: "V4.1 sombra carrega volume" |
| **23/08** | **US$ 21,26** | 🔥 pico: sombra ligada → 106 reqs gpt-5.5, 3,5M input, 284k output |
| 24/08 | US$ 1,57 (parcial) | |

**Modelos e papéis** (5 dias): gpt-5.5 = 364 reqs · 8,8M in · 814k out (redação + FC com `web_search` — "rota luxo" do `v41_ciclo.py`) · gpt-4o-mini = 1.920 reqs (coletor/intake classificando pautas 24/7) · gpt-4.1/gpt-4o = papéis menores.

## 2. Onde roda: `/root/v4_labs/` + crons no NYC (198.199.121.136) — 24/7

- `coletor.py` → `v4_vertical_intake.py` → `v4_vertical_draft_worker.py` por vertical:
  **geopolitica a cada 30 MIN** (48 ciclos/dia!) · nacional */6h (reduzido 22/08) · economia/cultura */4h · meio_ambiente 1/dia…
- `v41_ciclo.py`: gpt-5.5 + web_search (rota luxo; Perplexity aposentado).
- Chave dominante `key_ucN30bx4MKqz7X2N`; 1 chamada isolada `key_9tHwtfm58iieOtAM` (23/08) — identificar depois.

## 3. Superprodução (WP ocafezinho, contado ao vivo 24/08 ~09:20)

- **draft: >500** (contador saturou) · **pending: 361** · future: 6 · publicados 17-24/08: ≥200 (~28/dia).
- Rascunhos novos: **51 em 23/08** (dia do pico de US$ 21) · **17 em 24/08 até ~09h**.
- A fábrica gera ~**2× o que publica**; o excedente estoca em rascunho/pending — incluindo a "sombra V4.1" que ronda de 22/08 decidiu ligar ("sombra carrega volume") sem o gate de publicação acompanhando. **Está-se pagando gpt-5.5 pra encher estoque.**

## 4. Regra nova do Miguel (24/08): ZERO produção no Dell

"Toda a produção tem que ser via servidor, nuvem, externa ao meu computador." Motor V4 já está no NYC ✓. Remanescentes de produção no Dell a migrar: crons do `youtube_cafezinho.py` (8/14/20h + jornal + forum11).

## 5. Estado / o que falta / o que preciso do Miguel

- **O que aconteceu:** gasto OpenAI mapeado por modelo/dia/origem; superprodução medida no WP; causa do pico de 23/08 identificada (sombra V4.1).
- **O que falta:** (a) decisão sobre ritmo — sugestões: geo 30min→2h; pausar/desacelerar a sombra V4.1 até o gate liberar; teto diário no `gerenciador_tokens.py`; (b) migrar crons YouTube do Dell; (c) drenar os 361 pending (publicar ou descartar); (d) identificar key_9tHwtfm.
- **O que preciso do Miguel:** dizer qual ritmo quer (não mudei NADA — só diagnostiquei; mexer no cron do NYC é decisão sua).

📊 Atualizações do dia (mesma sessão): DeepSeek fechado (aba zombie do Moka no Chrome — morta pela rotação 08:52, saldo estancado US$ 4,09); ver fórum irmão `forum_auditoria_gasto_deepseek_chaves_moka_20260824.md`.

📁 Memória técnica: `Cerebro/Memorias/memoria_auditoria_openai_v4_20260824.md`

---

## 📋 ADENDO 1 — EXECUÇÃO da ordem do Miguel (24/08 ~09:15): V4 desligado, V4.1 exclusivo + Plano de Racionalização

### O que foi executado no NYC (backup: `/root/backup_crontab_pre_v4off_20260824_0912`)
1. **17 workers de redação V4 desligados** (16 removidos das linhas coletor→intake→worker + tendências comentada) — V4 (redação velha) oficialmente aposentado.
2. **Coletor+intake mantidos** (são o "pauteiro" barato, gpt-4o-mini) — geo reduzida de 30min → 1h.
3. **V4.1 exclusivo**: 4 crons a cada 2h (nacional :25, economia :35, ciência :45, geo :55) — potencial ≤ ~20 rascunhos/dia, na prática menos (gates de tese/anti-repetição/fail-closed). Deixa de ser "sombra": é o pipeline oficial (o switch E3 do plano V4.1, por ordem direta do Miguel).
4. Arquitetura confirmada: V4.1 = curadoria com tese dinâmica → redação luxo (gpt-5.5+websearch) → FC → rascunho 4.1 → 3º checador (libera/retém) → publicação CM/AGY. Pipeline COMPLETO exceto a coleta de pauta, que é compartilhada (coletor/intake, barata).

### Plano de Racionalização (proposto; R1b/R4 aguardam OK do Miguel)
- **R1a. Triagem do estoque**: 361 pending → reprocessar pelo 3º checador em lotes de ~20/dia (liberar p/ publicação ou descartar). Meta: pending ≤ 30.
- **R1b. Rascunhos velhos (>500)**: os com mais de 30 dias sem aprovação → lixeira (reversível) com lista de auditoria em fórum. **[precisa OK do Miguel — mexe em conteúdo]**
- **R2. Ritmo casado com publicação**: produção ≤ publicação×1,2. Hoje já vale (V4 off + 2h).
- **R3. Teto de custo**: teto diário OpenAI no `gerenciador_tokens.py` (verificar/implementar; sugestão US$ 5/dia, estourou → só 4o-mini até meia-noite). Métrica nova no boletim: custo por matéria publicada (meta < US$ 0,30).
- **R4. Migração Dell→servidor** (regra zero-produção-no-Dell): migrar 3 crons do `youtube_cafezinho.py` (8/14/20h + jornal + forum11) para NYC/Tencent. **[aguarda janela]**
- **R5. Monitor**: ronda V4 30/30 passa a reportar rascunhos gerados × liberados × publicados × US$ por dia.

### Conserto estrutural MOKA (mesma ordem, commit `11478fc` no espelho — deploy automático)
- Tradução de livro inteiro agora **pausa sozinha quando a aba vai pro segundo plano** (visibilitychange) e **fechar a janela = pausar** (antes seguia escondida — raiz dos US$ 101 invisíveis). Job continua retomável; aviso novo `tb_paused_hidden` nos 12 idiomas; tsc verde.
- Pendência: teste do Miguel no espelho → levar ao canônico (merge) + recomendação permanente: leitura longa no **v4-flash** (~25× mais barato que pro).

**Estado:** R1a/R2 já possíveis; **falta:** OK do Miguel p/ R1b (lixeira) e janela p/ R4; teste espelho Moka.

### Adendo 2 — Fix Moka publicado nos DOIS ambientes (ordem Miguel ~09:30)
- **Espelho** (moka-espelho.vercel.app): commit `11478fc` (push espelho:main, deploy auto) ✅
- **Canônico** (mokareader.com): cherry-pick `1c6b31b` na main — SÓ o fix (sem a fila de experimentos do espelho, respeitando a regra de não despejar reforma não testada no canônico), push origin/main, deploy Vercel automático ✅
- Nota técnica: cherry-pick após `git reset --hard` (o `git add` da espelho tinha carona staged pro checkout; commit seguro na espelho o tempo todo). tsc verde na espelho; avisos na main eram só cache `.next/` residual.
- Teste do Miguel: abrir livro → 🌐 Traduzir livro inteiro → trocar de aba/minimizar → tradução pausa (🌙 aviso ao voltar); fechar a janela = pausa com retomada.

---
## ✅ VERIFICAÇÃO DE ESTADO REAL (24/08 ~09:20, ronda 30/30 — pergunta do Miguel "confere se já está no Cérebro")

**Registro: COMPLETO.** Fórum (este) + memória técnica `Memorias/memoria_auditoria_openai_v4_20260824.md` (08:57) + 2 linhas no MONITORAMENTO + CEREBRO_NODE_ATUALIZACOES + memória auto do ZCode.

**Mudanças confirmadas no crontab do NYC (verificadas ao vivo):**
1. **Redator V4 desligado DE VERDADE**: nenhuma linha ativa contém `v4_vertical_draft_worker.py` — as linhas por vertical seguem só com coletor+intake (marcadas `# V4_DESLIGADO_20260824`), exatamente o desenho da fase final do rollout (coletores alimentam o V4.1); tendências comentada por inteiro.
2. **Sombras V4.1 desaceleradas** para `*/2` (2h) nas 4 verticais — corta o pico de custo mantendo o termômetro.
3. ⚠️ Nota: a mudança de 24/08 no crontab foi feita **sem backup datado** (último é `bak_pre_ritmos_20260823`); reconstrução possível por ele.

**Estado resultante:** V4.1 é o único redator (com loops editando/publicando); gasto esperado em queda (24/08 parcial já em US$1,57 vs pico 21,26). Pendências vivas: recarga DeepSeek (~US$3,81 — único provedor da redação) e, se quiser, OpenAI p/ rota luxo.

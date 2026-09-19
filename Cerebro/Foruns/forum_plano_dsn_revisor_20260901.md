# 📐 Fórum — PLANO DE TRABALHO: robô DS-N REVISOR + Lei de Poderes v3 (nada publica sem revisão de texto)

**Data:** 2026-09-01 ~18:1x BRT · **Sessão:** ZCode/GLM-5.3 (Dell) · **Status:** PLANO (não implementado — o sistema inteiro foi informado antes, ordem do Miguel)
**Origem:** ordem/ideia do Miguel ~18:0x: "o dsn publicador não pode publicar textos que não tenham sido devidamente revisados… acho que teremos de criar um robô dsn revisor, para revisar os textos nos rascunhos e dar um check final. somente os textos com check final do dsn revisor poderão ser publicados. assim criamos uma camada a mais de qualidade. faz um plano de trabalho. o sistema inteiro precisa saber antes de ser implementado."

---

## 1. Diagnóstico — por que o Miguel está certo (provas de hoje)

O **DS-N Publicador** (Tencent, `~/dsn_publicador/dsn_publicador.py`, Lei de Poderes v2 de 31/08) tem **um único gate de publicação: a CAPA** (`_cafezinho_img_check` ok, olho robótico duplo). O **texto e o título não são revisados por ninguém antes de sair**:

1. **268553** (Ronnie Lessa, 15:16): publicado com **timecodes no corpo** (sem revisão) — caso da sessão urgente 17:35.
2. **268482** (Villatoro, 12:39): título com sigla "Cecot" + sobrenome solto → **EMU-2** (sessão 17:36).
3. **268457** (Kast, 14:31): título hermético, tradução literal de "cárcel vitrina" (fórum irmão `forum_titulo_kast_investigacao_autoria_20260901.md`).

O fluxo fresco do publicador (linha do código: "draft de fábrica (zizi_job_id) ≤12h, sem slot, o mais antigo primeiro") publica direto; a CL audita **a posteriori**. O único "revisor" de texto no pipeline é o fact-check automático (`_v41_fc`), que verifica FATO, não forma/estilo/artefatos. **A suposição de desenho do Miguel (publicar só o revisado) não é o que a v2 implementou — a v3 vai corrigir isso.**

## 2. A regra nova (LEI DE PODERES v3 — fail-close de texto)

> **Nenhum texto é publicado sem DOIS carimbos EARNED no rascunho:**
> 1. `_cafezinho_img_check.ok == true` (capa — já existe, olho robótico duplo)
> 2. `_cafezinho_revisao_v2.ok == true` (texto+título — **novo, dado pelo DS-N Revisor**)
>
> Sem os dois → o publicador SEGURA o post na fila ("segurado p/ revisão") e reporta. **Fail-close: revisor caído = não publica às cegas** (alerta 🔴 na ponte; SEM degrau para fail-open).

## 3. Desenho do robô DS-N REVISOR

| Aspecto | Decisão |
|---|---|
| Casa | Tencent `~/dsn_revisor/dsn_revisor.py` (irmão do publicador; mesmo padrão dos DS-N) + cron `*/15` |
| Alvo | Rascunhos `draft/pending` **da fábrica** (meta `zizi_job_id` começando `v41_`/`v4d_`) dos autores-agente (5470, 5801, 5786…). **Humanos NUNCA** (§130 preponderância humana — conta própria ou ausência de zizi_job_id) |
| Eixo 1 — TÍTULO | As **8 regras canônicas** (Manual EMU-1/EMU-2): 1 ideia/frase, sem sigla não consagrada, cargo p/ pessoa pouco conhecida, sentence case, ≤80c ideal, sem `:`/travessão, **+ regra de clareza nova**: proibir jargão e tradução literal estrangeira no título ("prisão vitrine"-school) |
| Eixo 2 — TEXTO | (a) artefatos de fábrica: timecodes, HTML cru, `CONTENT END`, denominações internas vazadas ("Banco Ouro"); (b) estilo Manual B1 (parágrafos curtos, anti-repetição, sem selo de IA); (c) coerência título×olho×corpo (o erro do título tem que casar com o corpo); (d) fontes/links presentes; (e) spot-check factual: se `_v41_fc` reprovado ou ausente → reprova |
| Veredito | `ok: true/false` + `problemas[]` + `sugestoes[]` gravados no meta `_cafezinho_revisao_v2` (com modelo, custo, ts, `revisor: dsn_revisor_v1`). **v1 NÃO edita texto sozinho** — aprova/reprova e sugere no canal (edição continua com a esteira/CL). v1.5 (opcional, depois): auto-fix só de artefatos triviais (timecodes), sempre logado |
| LLM | Padrão: DeepSeek (barato, API já no Tencent). **Regra de heterogeneidade (recomendada): revisor ≠ redator do job** quando o modelo do job for identificável (log do worker V4.1) → fallback GLM/Kimi/gpt-4o-mini. Custo estimado ~US$ 0,005/post · ~20 posts/dia ≈ **US$ 0,10/dia** |
| Canal | `Foruns/ponte_laura_completa/de_nuvem_revisor.md` (vereditos, reprovações do dia, métricas) — mesmo padrão do `de_nuvem_publicador.md` |
| Freios | Hardstop diário de custo (US$ 2, defensivo); máx 1 rodada/triage por post (sem loop); tudo em JSONL com histórico |

## 4. Mudança no publicador (hard gate)

- `dsn_publicador.py`: nos fluxos de publicação, exigir `_cafezinho_revisao_v2.ok == true` **além** do `_cafezinho_img_check` (mesma mecânica de carimbo EARNED — nunca forjável pela esteira).
- Posts segurados aparecem na rodada como `{"id": X, "r": "aguardando_revisao"}`.
- **Anti-colisão §112:** o `dsn_publicador.py` está em obra pela sessão urgente (patch anti-flip/DS YouTube) — a implementação do gate **só começa depois do fim+prova do patch dela**.

## 5. Fases (cada uma com porta de decisão)

- **F0 — Plano + comunicado (ESTE FÓRUM + ponte ZM-20260901-033):** o sistema inteiro sabe; CL (chefe da esteira) e DS-N Chefe dão ACK; Miguel valida o desenho. **Não implementar antes dos ACKs.** *Nota: complementa o gate-texto da sessão urgente (ZM-032, 18:02 — consenso CL incondicional + autor 5801 rascunho-only), que cobre o fluxo-ponte; este plano fecha o FLUXO FRESCO/fábrica (autor 5470), que segue publicando sem revisão de texto.*
- **F1 — Build em modo LOG-ONLY (24h):** revisor roda, carimba e loga, mas o publicador ainda não exige. Medir: taxa de reprovação, falsos positivos, latência, custo real.
- **F2 — Modo ADVISOR carimbado:** publicador lê o carimbo mas só **marca** no relatório (ainda não bloqueia). Ajuste fino das regras com casos reais.
- **F3 — HARD GATE (Lei v3 em vigor):** só com os 2 carimbos. **Ativação exige homologação CL + Miguel.**
- **F4 — Métricas semanais:** taxa de reprovação por vertical, falsos positivos, títulos corrigidos, custo.

## 6. O que NÃO muda

- Fábrica V4.1 (Laura) segue criando rascunhos; fact-check `_v41_fc` segue como está; EMU-2 no Manual segue; auditor advisor do NYC (autor 5786) segue para o legado — o revisor **nasce já cobrindo 5470+5801+5786** (curando o gap exposto hoje).
- Latência esperada: +7 a 15 min por post (revisor */15) — frescor ≤12h não é afetado.

## 7. Estado / o que falta / o que preciso de você (Miguel)

- **Pronto:** diagnóstico com provas; este plano; comunicado na ponte (ZM-20260901-032) para TODOS; Tema Duplo + nodos + monitor.
- **Falta:** ACKs da CL e DS-N Chefe na ponte; fim da obra da sessão urgente no publicador; seu "vai" para F1 (build log-only).
- **Do Miguel:** validar o desenho (principalmente: revisor não edita sozinho no v1 — aprova/reprova; e fail-close quando revisor cai).

---

## Adendo — FREIO ANTI-LOOP instalado nos R1/R2 (preocupação do Miguel ~19:2x: "têm logs? cuidado com loop alucinado gastando token à toa") — 19:2x

**Resposta:** SIM, têm logs (`logs/AAAA-MM-DD.log` + `cron.log` + canal `Foruns/revisao/canal_dsn_revisores.md` na ponte). E o risco era REAL: **post que falhava a escada voltava à fila a cada ciclo SEM limite de retentativa** (rajada 18:46–18:52: ~20 posts × ciclos queimando pernas de LLM).

**Freios instalados (Tencent, `.bak_pre_freio_loop_20260901` ×2, py_compile OK, ciclo real 19:16 provado com 4 checks http 200):**
1. **Máx 3 tentativas por post** em janela de 6h (`logs/freio_estado.json`) — depois o post é pulado com log até a janela virar ou alguém editar; sucesso no check limpa o contador.
2. **Hardstop diário de custo estimado US$ 3** (conservador: ~$0,012/tentativa) — estourou, o ciclo aborta e loga (anti-gasto).
3. Freios existentes preservados: 5 posts/ciclo, idade ≤48h, flock, check mais novo que a edição vale.

**Diagnóstico da rajada (log 18:52):** as pernas caíam por 3 bugs já conhecidos da casa — `gpt-5-mini` 400 (reasoning model rejeita `temperature`), `glm-5.3` "resposta vazia" (precisa `thinking:{type:disabled}`), `deepseek-chat` 401 (chave). Às 19:16 o `gpt-5` passou sozinho e os checks saíram. **Pendência para a sessão dona dos revisores:** corrigir as 3 pernas na escada (memória [[llm-escadas-glm-thinking-qwen-data-20260901]]).

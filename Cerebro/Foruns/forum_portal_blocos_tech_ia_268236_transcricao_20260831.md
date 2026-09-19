# 📰 FÓRUM — Blocos Tecnologia/IA parados + post 268236 em Cultura + bloco Vídeos/transcrição (31/08/2026)

**Ordem do Miguel (31/08 ~09:35):** 4 frentes — (1) post "Brasil no Mundo analisa guerra tarifária entre EUA e Canadá" saiu em Cultura, deveria ser Geopolítica; (2) blocos Tecnologia e IA parados desde 28/08; (3) bloco Vídeos + agente YouTube; (4) missão de ampliar aplicativos de transcrição (gratuitos + possibilidade de re-assinar Transkriptor).
**Dono:** ZM (ZCode/DeepSeek, sessão Dell 09:40→~11:00 BRT). Estado: **✅ frentes 1, 2 e 4 executadas; frente 3 destravada na causa (cascata) e registrada.**

## O que aconteceu (resumo em 1 parágrafo)

O post 268236 nasceu do V4.1 com `zizi_job_id=v41_cultura_*` (o classificador de vertical tratou o programa "Brasil no Mundo" da TV Brasil como cultura) e por isso veio ao mundo em Cultura+Séries — corrigido no canônico e no espelho. Os blocos Tecnologia (cat 30) e IA (5008) não estavam com a esteira morta: o ciclo V4.1 produziu ciência (268380, hoje 07:47) e digital/IA (268386, hoje 09:09) com as categorias certas — o gargalo é duplo: **(a)** a fila de publicação inteira (19 rascunhos) está SEM capa desde ontem 17:30 (nenhum `_cafezinho_img_check`), e **(b)** o funil de pautas de ciência é estreito (1–4 candidatas novas/dia há semanas), agravado pela migração Digital→IA de 27/08 que drenou o principal fornecedor da cat 30. Na transcrição, a cascata do NYC era **VAZIA na prática** (supadata sem chave + transkriptor morto) — agora tem AssemblyAI (chave viva) como 2º degrau.

## Fix 1 — Post 268236 (canônico + espelho) ✅ PROVADO

- Canônico (`cafezinho-wp`, `--path=/var/www/ocafezinho`): removidas Cultura 79 e Séries 3044 (`--by=id` — pegadinha do `term add` sem `--by=id` registrada ontem continua valendo), adicionadas **Geopolítica 5003 + Internacional 15**, `_yoast_wpseo_primary_category` → 5003, cache flushed. Readback: `[5003, 15, 2403]`.
- Espelho (`root@159.65.177.60`, `--path=/var/www/cafezinho-news`): mesma correção; readback `[5003, 15, 2403, 21169 Top 10 — agora]`.
- **Caso-escola:** pauta de programa de análise internacional (TV Brasil/EBC) classificada como `cultura` na origem. Próximas pautas "Brasil no Mundo" devem nascer `geopolitica` — vigiar no coletor.

## Fix 2 — Blocos Tecnologia/IA (funil + diagnóstico) ✅ EXECUTADO

Números que confirmaram a queixa (posts publicados/dia, cat 30 = Tecnologia): 25/08=5, 26/08=7, 27/08=7, 28/08=2, 29-31/08=**0**. IA (5008): 28/08=10 → 29/08=1 → 30/08=2 → 31/08=0 (até 09:40).

**Causa raiz 1 — dreno estrutural:** em 27/08 a vertical `digital` migrou para a cat 5008 (bloco virou "Inteligência Artificial"). A cat 30 (Tecnologia) perdeu seu principal fornecedor e ficou dependendo só da vertical `ciencia`, cujo funil é estreito por natureza: **1–4 candidatas novas/DIA** (verificado no sqlite `ciencia_tecnologia_ia.sqlite3`: 27/08=3, 24/08=1, 22/08=1, 19/08=1...).
**Causa raiz 2 — fila de capas parada:** 19 rascunhos (268291→268386) SEM `_cafezinho_img_check`, nenhum ganhou capa desde ontem 17:30. Editores CM/AGY acionados na ponte (ZM-20260831-002). Prioridades: **268380** (Tecnologia — seria o 1º post do bloco em 3 dias) e **268386** (IA).
**Patch aplicado (NYC `/root/v4_vertical_intake.py`, backup `.bak_pre_tech_sem_nexo_20260831`):** o veto `missing_geopolitical_technology_nexus` virou **prioridade, não veto** — pauta tech com termo no título e nexo geo <4 entra com badge `v4_tech_sem_nexo_geo` (quem tem nexo segue ganhando no score). Prova: intake imediato `accepted 1→4`, `new_rows 3` na primeira rodada; candidatas novas de 31/08 já = 4. Nota de método: rejeições por nexo de hoje (217) são quase todas off-topic real ("Volkswagen SP2", "trilha Appalachian") — estatísticas anteriores "226/48h" eram artefato de comparação de string entre formatos de data no SQLite (ISO com `T` vs `datetime('now')`); usar `LIKE 'AAAA-MM-DD%'`.

**Decisão pendente do Miguel (não fiz sem ordem):** para o bloco Tecnologia engordar de verdade, ou (a) matéria tech-IA da casa digital nasce `[5008, 30, 2403]` (IA prevalece como primária, mas alimenta os 2 blocos — reverte parte do caso-escola 268333 à luz do efeito colateral), ou (b) ampliar fontes do coletor `tec` (hoje o feed traz muita pauta off-topic). Hoje o bloco fica vivo com 1–2/dia do funil ciência + capa da fila.

## Fix 3 — Transcrição: cascata estava VAZIA na prática ✅ PROVADO

- **Estado antes:** `DEFAULT_PROVIDERS="supadata,transkriptor"` — Supadata **sem chave** (login pendente do Miguel desde 29/08) e Transkriptor **morta** (assinatura encerrada) → vídeos SEM legenda não transcreviam (é um dos motivos do bloco Vídeos parado; o log do agente YouTube mostra `transcrição não completou status=Failed`).
- **Patch A** (`/root/agents_labs/youtube_v2/youtube_transcription_fallbacks.py`, backup `.bak_pre_cascata_assemblyai_20260831`): cascata → **`supadata,assemblyai,transkriptor`**. AssemblyAI usa a chave já presente no `chaves.sh` (validada 29/08, ~US$0,37/h — só cobra quando o vídeo NÃO tem legenda).
- **Patch B** (`agente_youtube_v2_coletor_dialogos.py:205`, backup `.bak_pre_hint_assemblyai_20260831`): `provider_hint` default era `"transkriptor"` (morto!) → `"supadata,assemblyai"`.
- Cópias: a viva é a de `agents_labs/youtube_v2`; a cópia `/root/youtube_transcription_fallbacks.py` é LEGADO (sem supadata) — não tocada.
- `py_compile` 3/3 OK.
- **Bloco Vídeos/agente YouTube:** pipeline VIVO (cron 11h/17h UTC; última ronda hoje 11:00: 62 vídeos publicados, 29 fichas draft, **0 publicáveis pendentes**). Travas: transcrição (corrigida acima) + lives agendadas sendo tentadas ("This live event will begin in 10 hours" — o filtro `is_upcoming` existe no coletor; verificar a ORDEM em que roda vs. o job de transcrição — registrado como pendência). Último post cat 28: 28/08 17:39. Com a cascata viva, os próximos ciclos (14:00/21:00 BRT) voltam a fechar fichas → rascunhos → publicação.

## Parecer Transkriptor (pergunta do Miguel: "posso voltar a assinar?")

**Tecnicamente NÃO precisa mais**: (1º) legendas de YouTube = grátis via innertube+proxy iProyal (rota principal, sem chave); (2º) sem legenda = AssemblyAI pay-per-use US$0,37/h com chave já viva; (3º) Whisper large-v3-turbo LOCAL na Tencent = grátis (provado 30/08, ~1,2× o tempo do áudio); (4º) Supadata free (100 créditos/mês) cobre casos extras — **falta só o Miguel logar** (login deixado pronto na sessão de 29/08; 30 segundos) e colar a chave no `~/cofre_intake/cofre_intake.env` (rito do fórum de 29/08 executa o resto). **Transkriptor só vale se o Miguel quiser a INTERFACE dele para uso manual** — se re-assinar, é colar a chave nova (rito [SEGREDO] ou cofre) que a cascata já a trata como 3º degrau, zero código novo.

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** 268236 corrigido nos 2 servidores; funil tech afrouxado (+3 pautas na hora); cascata de transcrição viva (assemblyai); diagnóstico completo dos blocos com números; ronda V4.1 30/30 confirmada ATIVA (é o canal legítimo da caça de capas — não duplicado aqui); ponte ZM-20260831-002 cobrando capas dos editores.
- **Falta:** capas para os 19 rascunhos (esteira AGY/CL — cobrado); validar nos próximos ciclos (14:00 BRT digital, 10:45 BRT ciência) mais rascunhos tech; ordem do live-check × transcrição no coletor YouTube; degrau Whisper-Tencent grátis na cascata (serviço HTTP — escopo futuro); decisão (a)×(b) do bloco Tecnologia.
- **Preciso do Miguel:** (1) logar no Supadata e passar a chave (30s — destrava o 1º degrau grátis); (2) decisão sobre Transkriptor (parecer: desnecessário; interface manual é o único motivo); (3) decisão (a) tech-IA em 2 blocos × (b) ampliar fontes do coletor tec.

— ZM · ZCode/DeepSeek · 31/08/2026 · BRT

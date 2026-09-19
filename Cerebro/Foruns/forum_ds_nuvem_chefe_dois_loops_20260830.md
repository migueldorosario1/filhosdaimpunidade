# 🎖️ Fórum — DS Nuvem Chefe (DS-N Chefe): 2 loops + PLANO do grupo de 3 robôs — 30/08/2026

> Tema Duplo: este fórum + `memorias/memoria_ds_nuvem_chefe_dois_loops_20260830.md`. Ordem do Miguel 30/08 ~15:1x (refs DSC-024/028/029/031/032). Executor: ZM · ZCode/GLM-5.3.
> ⚠️ "SNFF" NÃO existe — era erro de ditado (DSC-031). Nome oficial: **DS Nuvem Chefe (DS-N Chefe)**.

## FASE 0 — ENTREGUE (hoje)

1. **Renome aplicado** em todo lugar que importava: prompt da ronda (identidade + título), CONTEXTO_MINI (a casa já tinha corrigido com nota anti-SNFF; agora reflete os 2 loops), assinatura do Loop A. Backup `.bak_pre_chefe_20260830`.
2. **DOIS loops independentes no ar:**
   - **LOOP A · ESCUTA** — serviço `ds-nuvem-chefe-escuta` (systemd, Tencent, Restart=always) desde 15:26 BRT. Long polling `getUpdates timeout=25` em loop contínuo (custo ZERO de escuta). Resposta flash em segundos direto no Telegram do Miguel, assinada `— DS Nuvem Chefe (DS-N Chefe) · AAAAMMDD HH:MM:SS BRT`. Offset persistido ANTES de responder (nunca 2×; herdado do daemon: 747773836). Silêncio total ocioso (heartbeat local 1×/h). Erro de API → backoff 30s. Extras preservados do desenho da casa: interceptação `sk-` → cofre 600 (nunca na ponte, §82), áudio guardado + INBOX, consumo de tokens 1 linha/dia (`~/ds_nuvem_chefe/consumo_tokens.log`).
   - **LOOP B · RONDA 30/30** — como hoje (ponte, site, FAROL, esteira, memória/CONTEXTO_MINI), agora como "Loop B" no prompt, com o novo papel de CHEFE (análise do sistema como todo + distribuição de tarefas) e as regras de fala.
3. **⚠️ DECISÃO DE ARQUITETURA (transparência):** o `getUpdates` do @dscelularbot passou a ter UM consumidor — o Loop A na Tencent. O daemon `dsc-minibot` (us65) **parou de escutar** (flag reversível `/root/.dsc_poller_na_tencent`, backup `.bak_pre_cutover_escuta_20260830`) e **continua como carteiro**: entrega o `RESPOSTAS.md` no Telegram do Miguel (função intacta, prova: log `entregue:` no journal). Por quê: dois consumidores de getUpdates roubam mensagens um do outro (regra da casa, documentada no fórum DSC anterior). Reversão: apagar a flag + restart do daemon (e parar o Loop A).
4. **Regras de fala com o Miguel** (no Loop A e no Loop B): nunca sigla solta — nome completo (sigla) na 1ª menção (DSC-030); palavra estranha de transcrição → PERGUNTAR, não adivinhar (DSC-032).
5. **Teste de prova (item 4):** pedido de teste enviado ao Miguel (msg #27, 15:28 BRT). Pipeline pronto; a latência real (alvo: segundos) será medida e reportada na ponte quando ele mandar a msg — o Loop A registra `lat=Xs` no log a cada resposta.

## FASE 1 — PLANO — ⏳ AGUARDANDO ✓ DO MIGUEL (nada construído)

### Robô 1 — DS Nuvem Chefe (DS-N Chefe) — JÁ EXISTE (FASE 0)
- **Cadência:** Loop A contínuo (25s long poll) + Loop B 30/30 (:00/:30).
- **Lê:** Telegram (A), ponte/INBOX, site REST, FAROL (B). **Escreve:** respostas flash (A), CHECK/ronda + memória viva + CONTEXTO_MINI + RESPOSTAS.md (B).
- **Custo:** escuta zero; flash ≈ US$ 0.002/msg (≈R$ 0.01) — 50 msgs/dia ≈ US$ 0.10/dia; ronda já existente ≈ US$ 0.10–0.30/dia.
- **Assina:** `— DS Nuvem Chefe (DS-N Chefe) · AAAAMMDD HH:MM:SS BRT`. **Anti-bagunça:** escuta ociosa = zero postagens; ronda = 1 CHECK + bloco só com conteúdo; commit seletivo.

### Robô 2 — DS Nuvem Revisor de Texto (a construir só com ✓)
- **Função:** revisão CONSULTIVA contínua dos textos da esteira (fato, título, ortografia, links) — **NUNCA bloqueia publicação** (publica sempre; sugestão é conselho).
- **Cadência:** a cada rascunho novo da esteira (piggyback no ciclo V4.1) ou varredura 30/30 dos rascunhos <2h.
- **Lê:** rascunhos/posts novos (REST/wp-cli local no cafezinho-wp). **Escreve:** parecer `revisao_texto_<id>.md` em pasta própria + 1 linha-resumo/dia na ponte; JAMAIS edita o post.
- **Custo:** ~2k in + 0.5k out por texto ≈ US$ 0.001–0.002; 40 textos/dia ≈ **US$ 0.05/dia (≈R$ 0.28/dia)**.
- **Assina:** `— DS Nuvem Revisor de Texto · carimbo BRT`.

### Robô 3 — DS Nuvem Revisor de Foto (a construir só com ✓) — PRECISA DE VISÃO (DSC-007: o flash da Tencent é cego)
- **Opção A — Dell + ZCode/GLM (custo zero):** roda no Dell (assinatura já paga), analisa capas da fila do WP no padrão da casa. Limite: depende do Dell ligado.
- **Opção B — Visão na Tencent 24/7:** DeepSeek vision-exp (`deepseek-v4-flash-vision-exp`, já usado no auditor de capas da casa) ≈ US$ 0.0003/análise; 40 capas/dia ≈ **US$ 0.012/dia (≈R$ 0.07/dia)**. Custo pequeno, mas por transparência (DSC-019) **só liga com ✓ PRÉVIO do Miguel**.
- **Recomendação do ZM:** Opção B (24/7, custo ínfimo, mesmo modelo já aprovado no fluxo de capas) — decisão é do Miguel.
- **Escreve:** parecer casado com o carimbo JSON da Ponte Imagens; nunca troca capa sem rito.

### Coordenação do grupo (anti-bagunça)
Prefixos próprios (CH-/RT-/RF- + nº) · 1 CHECK por ronda · append-only · commit seletivo (nunca `-A`) · linha no MONITORAMENTO ao começar/terminar · agenda própria por robô · consumo 1 linha/dia consolidado pelo chefe no relatório diário. **Custo total estimado do grupo: ~US$ 0.20–0.45/dia (≈R$ 1.10–2.50/dia)** além do que já roda hoje.

## Estado / falta / preciso do Miguel
- **Estado:** FASE 0 completa (2 loops no ar, cutover feito com backup e reversibilidade); FASE 1 só plano.
- **Falta:** msg de teste do Miguel (latência real); ✓ do Miguel para construir Revisores 2 e 3 (e escolha A/B no de Foto).
- **Preciso do Miguel:** mandar "teste chefe" no @dscelular_bot (cronometro e reporto); dar ✓ (ou não) no plano e escolher a opção do Revisor de Foto.

— ZM · ZCode/GLM-5.3 · 20260830 15:30 BRT

---

# 🎙️ ADENDO — Transcrição de áudio instalada (ordem "whisper") — 30/08 ~15:5x BRT (ZM)

## O que foi instalado
- **Whisper local** (faster-whisper 1.2.1, model small int8, CPU Tencent): custo ZERO por áudio; 8s→9s, 5 min→~2-3 min.
- **Fallback AssemblyAI** automático (Whisper falhou → nuvem): chave ASSEMBLYAI_API_KEY espelhada na Tencent (sha8 confere com fórum 29/08, Regra 4, backup .bak_pre_assemblyai_20260830).
- Fluxo na escuta: ack imediato → transcreve → resposta flash assinada → INBOX `🎧AUDIO Xs TRANSCRITO` + `RESPONDIDO_FLASH`; falha de transcrição → aviso honesto + arquivo guardado.

## Provas (tudo com áudios REAIS do Miguel)
- 20s (13:55, us65): AssemblyAI **5s**, PT-BR perfeito.
- 8s (15:33, Tencent): Whisper local **9s** + flash **2s** + entrega no Telegram + INBOX commit.
- Msg "Teste" (15:34): resposta flash **lat=1s** (número do teste pedido na FASE 0 item 4).

## Bugs corrigidos no caminho (lições)
1. **DEEPSEEK_API_KEY do .dsh na Tencent está MORTA (401)** — a escuta nasceu usando-a; agora prefere **DEEPSEEK_CAFEZINHO_CANONICO** (espelhada na Tencent, sha8 f0aaa272cec, testada viva). Recomendação: revisar os .dsh envs (família da chave morta sha8 b6c4d4de de 29/08).
2. AssemblyAI: upload é **bytes crus** com Content-Type audio/ogg (multipart dava 400/transcoding failed) e o upload_url **expira** (upload→transcrição no mesmo fluxo).
3. Chave transportada por ssh com $VAR em aspas simples NÃO expande — usar pipe por stdin (linha vazia quase foi parar no cofre; pega na hora pelo sha8).

## O que falta / preciso do Miguel
- Nada de instalación — **testar**: manda um áudio mais longo (até 5 min) no @dscelular_bot; o robô acusa, transcreve e responde.
- FASE 1 (grupo de 3 robôs) segue AGUARDANDO ✓.

---

# 🧠 ADENDO — Memória do plantão (ordem Miguel 16:3x) — 30/08 ~16:40 BRT (ZM)
- `memoria_conversas.md`: janela rolante por TAMANHO (20k chars → backup datado em `memoria_plantao_backups/` + mantém últimas ~10k). Grava MIGUEL/PLANTÃO de cada troca (texto e áudio transcrito).
- `estado_casa.md`: contexto da casa mantido pela ronda do chefe (dever novo no prompt; semente inicial do ZM com sistema + dia 30/08). 
- `llm_flash` agora: persona + estado (2,5k) + CONTEXTO_MINI (3k) + conversas (até 18k) ≈ 6k tokens in/resposta (~US$ 0.002).
- **Prova**: pergunta sobre o whisper de hoje → respondeu citando "vagabundo", large-v3-turbo e a confusão de identidade. Memória viva.


---

## ADENDO — 08/09 23:54 BRT — página /v6/loops volta a viver: ciclos ao vivo da Laura (ZCode Qwen3.8-Max, «vai» do Miguel 08/09 ~23:4x)

Diagnóstico (parecer entregue antes do «vai»): a página /v6/loops («Loops Laura & Miguel») lia só
`*_relatorio_chefe_*.md` de `foruns/loop_trindade_laura/controle/relatorios_chefe/` — parados em 19/08.
O loop da Laura migrou em ~29/08 para arquivo DIÁRIO `memoria_loop_laura/AAAA-MM-DD.md`, uma seção
`## HH:MM BRT — ronda …` por ciclo de 30/30min (fato/lição/erro próprio). O arquivo já chegava ao
Tencent (rsync/espelho), mas ninguém lia → página = museu.

Cura (marca `loops_ciclos_ao_vivo_20260908`, Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`,
svc cctv-v6; backups `bak_pre_loops_vivo_20260908`): lado de exibição SOMENTE — não mexe no loop da
Laura. (1) `_laura_ciclos()` fatia o arquivo diário em ciclos (mais novo primeiro; cabeçalho
diferente = seção ignorada, página não quebra; minuto «1x» virou «10» p/ idade). (2) Card novo no
topo «🔁 Loop Laura — ciclos ao vivo (30/30min)»: 12 ciclos c/ hora, ronda, pill de idade (semáforo
só no mais novo; demais pill neutra), fato azul + lição verde itálica; markdown da Laura
(**negrito**/*itálico*) convertido em <b>/<i> pós-escape. (3) Card antigo renomeado «consolidados do
chefe (formato antigo, até 19/08)» e aviso de vazio explica a migração. (4) Rodapé de fontes inclui
memoria_loop_laura.

Provas: curl (12 ciclos, mais novo «há 31 min», sincronizado «há 36 min») + screenshot Chrome
headless auditado. Custo zero: nenhum LLM no caminho, só leitura de arquivo já sincronizado.

O que aconteceu / o que falta / o que preciso de você (Miguel): NO AR e verificado; nada falta do
lado do agente; conferir a página quando abrir o painel.

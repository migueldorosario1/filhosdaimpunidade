# Fórum — Agente YouTube do Cafezinho REATIVADO (16/08 ~09:20 BRT)

**Sintoma (Miguel):** bloco Vídeos parou de atualizar (~10/08; mostrava posts de 10/08 11h38).

## Causa raiz (dupla)
1. **Cron sumido:** entrada `0 11,17 * * * /root/youtube_v2_pipeline.sh` NÃO existia no crontab do NYC (último backup que a tinha: `crontab_backup_pre_seo_meta_20260628_2339.txt`) — ninguém rodava o pipeline. Posts até 10/08 eram sobra agendada/future-dated + repetidor auto-tagado.
2. **Proxy iProyal intermitente:** rodadas de 16/08 manhã falharam com `ProxyError 504` (YouTube RSS, i.ytimg, api.tor.app/transkriptor) — depois voltou a responder (200). Se o bloco parar de novo sem cron-miss, testar proxy primeiro.

## Fix
- **Cron re-adicionado** (backup `crontab.bak_pre_youtube_readd_20260816`): `0 11,17 * * *` do pipeline completo.
- **Patch cat 28 no publicador V2:** `agente_youtube_v2_publicador.py` agora envia `[categoria, cat Vídeos 28]` em todo post (antes só a editorial — caso 266062 saiu só c/ Geopolítica; o patch de 12/08 cobria apenas o publicador LEGACY). Backup `.bak_pre_cat28_20260816`. O mu-plugin `cafezinho-auto-cat-videos.php` funciona em re-save mas NÃO viavia o publish REST via controle.ocafezinho.com — por isso o patch na fonte.
- **Pipeline completo rodado manualmente** (11:55-12:05 UTC): coletor → produtor → auditor → publicador; **publicou 266062** "Estrategista russo alerta: ordem mundial está morrendo e a ONU agoniza" (embed Jk7j268peg8) — cats (5003, 28, 20751), bloco Vídeos da home mostrou como HERO de 16/08 09h04 ✓.

## Observações
- Banco youtube_dialogos: 4 dialogo_pronto, 26 drafts, 42 publicados; transkriptor rejeitou 2 transcrições por qualidade (<100 chars/min, $12 custo perdido — gate anti-alucinação funcionando).
- `yt-dlp` ausente no PATH do pipeline (erro "No such file or directory" nos fallbacks) — não bloqueia (transkriptor é via API), mas instalar resolveria um fallback a mais.
- Cron roda 11:00/17:00 UTC (8h/14h BRT).


## Incidente 16/08 ~09:45 BRT — CÓDIGO PHP VAZANDO NAS PÁGINAS (short_open_tag)

**Sintoma (Miguel, urgente):** "agente youtube aparecendo todo quebrado e com bug vazados no site" — páginas novas mostravam `<? // Bootstrap pagination function wp_bs_pagination...` como texto visível (abaixo do título e no excerto do hero Vídeos).

**Causa raiz:** tema `ocafezinho-portal/functions/_pagination.php` (2023) abre com `<?` (short tag). PHP do servidor passou a rodar com **`short_open_tag => Off`** (era On antes — alguma atualização de PHP/config o desligou recentemente) → o arquivo passou a ser **ecoado como texto** em todo render novo e em todo wp-cli (a "poluição" com função de paginação que aparecia no stdout dos wp-cli desde cedo). Páginas antigas em cache (WP Rocket) não mostravam — por isso parecia "só no YouTube". **Correção:** `<?` → `<?php` nos 2 servidores (backups `.bak_pre_shorttag_20260816`), purge completo. wp-cli voltou limpo.

**Contaminação em DB:** post 266062 (o 1º publicado hoje pelo agente YT) ficou com o leak DENTRO do excerpt (sincronizado também ao espelho) — limpo nos 2 (excerpt vazio → auto-derivado). Busca WP_Query `s=wp_bs_pagination` em todos os status: 0 restantes nos 2 sites.

**Verificação:** home + página do post + espelho = 0 ocorrências; imagem destacada 480x360 do thumb do YouTube conferida visualmente = LIMPA (a "sujeira" era o texto vazado embaixo dela).

**Lições:** (1) qualquer "poluição" no stdout do wp-cli = SINTOMA de arquivo PHP sendo ecoado — investigar na hora; (2) `<?` curto proibido em todo arquivo do ecossistema — varredura recomendada (`grep -rln "^<?$" wp-content/themes/`) e já consta no plano de autolimpeza; (3) sync canônico→espelho propaga contaminação de campos — limpeza sempre nos 2.


## Adendo 16/08 ~10:00 BRT — checkpoint 🟠 + MISSÃO EM CURSO

**Estado da missão (YouTube):** reativado OK (cron 0 11,17 re-add; publicador V2 patchado c/ cat 28; post 266062 publicado; incidente short_open_tag resolvido nos 2 servidores). **EM CURSO — próximo passo:** (1) mudar publicador V2 p/ publicar como **draft** (rascunho) e passar pela **revisão externa Loop Miguel + Loop Laura**; (2) **informar os 2 loops** sobre o agente YouTube. Localizar ledgers dos loops em `Cerebro/` antes de escrever. **Falta:** executar 1-2. **Preciso de você (Miguel):** nada por ora.


## Adendo 16/08 ~09:50 BRT — MODO RASCUNHO + loops informados (ordem Miguel)

**Ordem:** "o agente youtube tem de ser igual aos outros: publica em rascunho e passa pela revisão externa do Loop Miguel e Loop Laura. Informe os dois loops."

**Feito:**
1. `youtube_v2_pipeline.sh`: `--status publish` → `--status draft` (backup `.bak_pre_draft_20260816`). Cron 11:00/17:00 UTC segue (agora gerando drafts).
2. **Loop Miguel informado:** item ABERTO `ZCODE-YOUTUBE-DRAFT-REVISAO-LOOPS-20260816` em `Foruns/ponte_trindade_daemon/fila_para_claude.md` (contexto + pontos de atenção + sugestão de executor).
3. **Loop Laura informado:** `Foruns/ponte_codex_miguel_laura/mensagens/para_laura/20260816_0946_agente_youtube_modo_rascunho_revisao_loops.md` (ficha técnica + o que observar + referências).
4. Rodada de prova em curso (pipeline completo 12:48 UTC em modo draft).

**Lições:** rodar estágios isolados exige `PYTHONPATH=/root:/root/agents_labs/youtube_v2` (sem ele: `ModuleNotFoundError: agente_roteador_llm` — falso bug); pipeline completo = o script, que exporta tudo.

**Prova de ponta a ponta (13:01 UTC):** pipeline em modo draft completou e gerou **2 rascunhos** no WP: 266072 ("Irã e Iêmen partem para a ofensiva…") e 266073 ("Trump chama Estreito de Ormuz de território dos EUA…") — ambos `status=draft`, cats {5003, 28} (patch cat 28 confirmado), NÃO publicados. Aguardam revisão Loop Miguel/Laura. Próximos cron: 17:00 UTC.


## Checkpoint 16/08 ~10:15 (Kimi 🟠) — MISSÃO EM CURSO: agente YouTube NACIONAL

**Novo contexto (Miguel):** o agente desejado é o **especializado em canais/sites NACIONAIS** (vários canais + regras de nomes) — NÃO o V2 geopolítico (Dialogue Works, Danny Haiphong…) que reativei hoje cedo (esse já virou modo draft; pode até ser revertido dependendo do que se achar). **Próximo passo:** localizar no NYC/Cérebro o agente nacional (legado `agente_youtube.py` tinha canais BR: Opera Mundi/Fórum/TV247/ICL/DCM na linha 49) + suas regras de nomes, e decidir ativação/substituição. **Falta:** encontrar config e rodar. **Preciso de Miguel:** confirmação se o V2 geopolítico continua em paralelo ou sai.


## Adendo 16/08 ~21:30 BRT — AGENTE NACIONAL DE VOLTA + EXPANSÃO DE CANAIS (GSN + IA + Band)

**Contexto (ordem do Miguel):** "o agente youtube do cafezinho era especializado em sites nacionais, tinha vários canais, regras para nomes... era esse agente que eu queria" + (voz, ~21:05) "bota também os canais do Global South News, os do Aiatolah de IA (Peter Diamandis, outros bons de IA), os debates (tem debate da Band rolando agora)... nacionais com preferência, mas bota os internacionais também".

### 1. Correções que destravaram o agente nacional (fim da cadeia de fixes)
- `YOUTUBE_PROXY_MODE=always` nos 2 cofres — **lição dura:** o `_ler_var` do util iProyal NÃO remove aspas nem comentário inline (`VAR="always"  # comentário` virava modo inválido → caía em fallback → timeout direto). Formato canônico: `VAR=always` seco.
- RSS via proxy validado dentro do `coletar` (feedparser + ProxyHandler): TV Fórum e Dialogue Works 200/15 entries.
- Rodada limpa relançada 21:27 BRT (log `/tmp/yt_rodada_expansao.log`).

### 2. Expansão da lista de canais (20 → 32)
**Nacionais novos (1):** Band Jornalismo `UCoa-D_VfMkFrCYodrOC9-mA` (debates/entrevistas — Miguel citou o debate da Band).
**GSN geopolítica (4, peso 1.8, idioma en, categoria_ids [5003 Geopolítica, 28 Vídeos]):** Judging Freedom `UCDkEYb-TXJVWLvOokshtlsw`, Glenn Diesen `UCZFCDIHTe9HGxtIuVDpBz7g`, Dialogue Works `UCkF-6h_Zgf9zXNUmUB-MzTw`, Daniel Davis/Deep Dive `UCWDN5zr5ttctoIAhZwW6tcQ` (IDs do JSON vivo do NYC, já validados em produção).
**IA internacional (7, categoria_ids [30 Tecnologia, 28 Vídeos]):** Peter Diamandis/Moonshots `UCCpNQKYvrnWQNjZprabMJlw` (2.0, pedido do Miguel), Lex Fridman `UCSHZKyawb77ixDdsGog4iWA` (2.0), Dwarkesh Patel `UCXl4i9dYBrFOabk0xGmbkRA` (2.0), Karpathy `UCXUPKJO5MZQN11PqgIvyuvQ` (1.8), DeepLearning.AI (1.5), Google DeepMind `UCP7jMXSY2xbc3KCAE0MHQ-A` (1.5), OpenAI `UCXZCJLdBC09xxGZ6gcdrc6A` (1.5).
**Preferência nacional:** pesos nacionais 1.5–3.0 × internacionais 1.5–2.0 (heurística) + regra textual `escopo_ampliado.regra` na curadoria (injetada no prompt do curador LLM): nacional vence em igualdade de força; internacional só ganha com furo/entrevista de peso/scoop de IA.

### 3. Patches no `youtube_cafezinho.py` (backup `.bak_pre_expansao_20260816`)
- Candidato carrega `idioma` + `categoria_ids` do JSON.
- `_transcrever(video_id, idioma)` — Transkriptor agora recebe "en" nos internacionais.
- `publicar_draft` envia `categories` quando o canal define (mu-plugin precedência Tecnologia já cuida do resto).
- Curador LLM recebe `idioma` por candidato + regra do escopo ampliado.
- Curadoria JSON v2026-08-16 (backup `.bak_pre_expansao_20260816`).

### 4. Bônus: conserto do agente Aiatolah
- `CANAIS_AI` do `sites-v4/aiatolah/agentes/aiatolah_agente_youtube.py` tinha **5 de 6 IDs INVÁLIDOS** (RSS 404 — só DeepLearning.AI funcionava). Substituídos pelos validados hoje + Diamandis (backup `.bak_pre_ids_validos_20260816`).

### 5. Metodologia de validação de canal (lição)
- channel_id de memória/IA NÃO é confiável (o Aiatolah prova). Fluxo correto: handle oficial → página do canal (via proxy) → extrair `channelId`/`browseId` → **confirmar com RSS** (`feeds/videos.xml?channel_id=...` 200 + título do feed bate com o canal). Cuidado: og:title da página pode enganar (caso Karpathy→3Blue1Brown); o RSS é a prova final. Busca do YouTube (`results?search_query=`) resolve handle ambíguo.

**Estado da missão: ✅ PROVADO PONTA A PONTA (21:48 BRT).** A rodada limpa (21:27) completou o ciclo inteiro: coleta 32 canais via proxy → curador LLM escolheu **Dialogue Works (GSN)** "Nima R. Alkhorshid: Trump Discusses NUCLEAR OPTION on Iran" (sábado à noite os nacionais só tinham clipes curtos — o curador acertou em pegar o internacional forte) → transcrição EN via fallback yt-dlp+S3 (30.880 chars/424 segmentos; URL-direto falhou e o fallback que ANTES travava agora baixa o MP3 pelo proxy em segundos) → análise (DeepSeek) → redação (GPT-5.5, 1192 palavras) → **DRAFT 266153** no WP: status=draft, **cats [5003 Geopolítica, 28 Vídeos]** (patch categoria_ids confirmado), thumb 266151, excerpt limpo. Cron local segue `0 8,14,20 --rodada` + jornal/11e-meia. **Observação:** o draft sai com autor 5786 (credencial WP_USER_CAFEZINHO do agente — comportamento histórico desde julho; os loops revisam antes de publicar). **Preciso do Miguel:** nada.

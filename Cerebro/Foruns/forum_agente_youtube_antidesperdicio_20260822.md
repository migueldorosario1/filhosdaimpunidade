# 🛑 Fórum — Agente YouTube: FREIO ANTI-DESPERDÍCIO (ordem Miguel, 22/08/2026 ~20:40)

> **Ordem do Miguel (quase literal):** "o Agente YouTube está baixando transcrição e não está usando — perder transcrição não pode acontecer. Não está conseguindo publicar → para de usar o transcripto → para até resolver. Não pode acumular transcrição sem usar. Foco: publicar com qualidade, com muita revisão e checagem exaustiva. Trabalhe com os loops, todo mundo em harmonia."
> Refs: **ZM-20260822-175** (inbox claude + canal Trindade + ponte de_dell).

## 1. O que estava acontecendo (provado no log `agent_data/v4_cafezinho_youtube/cron.log`)

- **Desperdício real**: rodada de 22/08 20h pagou transcrição (28.554 chars, Transkriptor URL-direto, US$ 6/use) + análise deepseek + nomes (2 websearch) e **morreu na redação** com Traceback — tudo perdido, sem cache.
- **Causa raiz nº 1 — bug da cascata**: `gerar_json` do `nucleo_llm.py` fazia o parse FORA do loop de fallback: HTTP 200 com corpo vazio (GPT-5.5 e agora também GLM-4.5-flash respondendo string vazia) era tratado como sucesso e o `json.loads` explodia a rodada DEPOIS — **26× "JSON inválido" / 23 Tracebacks** no log; os 6 modelos reserva da cadeia superluxo nunca eram tentados.
- **Causa raiz nº 2 — sem cache**: a transcrição paga vivia só em memória; qualquer falha posterior = dinheiro jogado fora (e retranscrição futura pagando 2×).
- **Causa raiz nº 3 — fila de revisão parada**: 10 drafts + 10 pending no WP canônico, 5 deles do YouTube (o mais velho de 18/08) aguardando os loops — enquanto isso o agente continuava transcrevendo vídeo novo.
- Nota forense: o draft **267114** (Farinazzo, 20:09 de hoje) foi criado por sessão manual dos loops (AGY patch fail-soft de feeds 20/08 preservado); o vídeo perdido foi o "Quem é Fernando Cerimedo" (TV Fórum), escolhido por HEURÍSTICA porque a cascata do curador também falhou (deepseek sem bloco JSON + kimi 429).

## 2. O que foi feito (tudo com backup `.bak_pre_*_20260822`)

| # | Fix | Onde | Prova |
|---|-----|------|-------|
| 1 | Cascata de JSON: resposta vazia/inválida = falha DO PROVEDOR → cai para o próximo | `agentes_tematicos/v4/nucleo_llm.py` | smoke ao vivo: cadeia entregou via **qwen** `{'ok':1}` com glm vazio na frente |
| 2 | **Cache de transcrição** em disco (`transc_<video_id>.json`) — reprocessar custa ZERO | `youtube_cafezinho.py::_transcrever` | código no ar; log "CACHE — custo zero" |
| 3 | Falha pós-transcrição → **pendente recuperável** (`pendentes_youtube.json`, 3 tentativas, 1/rodada) em vez de Traceback | `youtube_cafezinho.py::processar` | try/except + `_salvar_pendente` |
| 4 | **BREAKER editorial** (a inteligência pedida): ≥4 rascunhos YouTube aguardando revisão no WP = **NÃO transcreve vídeo novo**; recupera pendentes antes de tudo; fail-open se WP cair | `youtube_cafezinho.py::_breaker_transcricao/_fila_revisao_youtube/_consumir_pendente` aplicado em `rodar_rodada` e `rodar_jornal_forum` | **E2E 21h: rodada parou seca** ("BREAKER: 5 rascunhos… quem não publica não transcreve"), custo zero |
| 5 | Kill switch manual: arquivo `agent_data/v4_cafezinho_youtube/PAUSAR_TRANSCRICAO` para a transcrição nova (Miguel/loops criam e apagam) | idem | flag documentada |
| 6 | Teto do breaker configurável: env `YOUTUBE_FILA_REVISAO_MAX` (default 4) | idem | default no ar |

**GSN V2 (NYC):** cron SUMIU do crontab de novo (parado desde 19/08 11:16 — modo de falha conhecido do manual §4); tem cache próprio (`youtube_transcript_cache/`) e **27 drafts** acumulados. **Decisão: NÃO reativar por enquanto** — reativar produção com fila parada é o acúmulo que o Miguel condenou. Reativar quando a fila andar (decisão conjunta loops/Miguel).

## 3. Fila de revisão YouTube (quem destrava o breaker)

**267114** (Farinazzo/TV 247, 22/08 20:09) · **267087** (Marco Rubio/Brasil de Fato, 22/08 14:34) · **266745** (TSE×Flávio, 20/08) · **266545** (Lula/Sudeste, 18/08) · **266525** (Zâmbia, 18/08). Publicação continua EXCLUSIVA do CM (contrato da ponte), com 2ª opinião da Laura. Consumir com revisão exaustiva — o agente retoma sozinho na rodada seguinte.

## 4. O que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu:** desperdício provado e extinto na ponta da FÁBRICA (cache + pendentes + cascata + breaker). Rodadas noturnas de hoje (22:30/23:00 --jornal) já rodam sob o novo regime.
- **O que falta:** (a) loops consumirem a fila dos 5 (aí o breaker libera sozinho); (b) decisão sobre reativação do cron GSN V2 NYC (sugiro: só quando a fila de lá baixar de ~10); (c) monitorar 2-3 dias para confirmar zero transcrição perdida; (d) GSN V2 não tem camada nomes/verifica (pendência antiga do manual §7).
- **O que preciso do Miguel:** nada obrigatório. Opcional: ajustar teto do breaker (`YOUTUBE_FILA_REVISAO_MAX`); parar transcrição na mão quando quiser (`touch agent_data/v4_cafezinho_youtube/PAUSAR_TRANSCRICAO`, remover para retomar); recarregar IPRoyal (proxy morto 402 engole feeds — patch AGY mitiga).

## 5. Rodapé

- Backups: `nucleo_llm.py.bak_pre_cascata_json_20260822` · `youtube_cafezinho.py.bak_pre_antidesperdicio_20260822` (patch AGY fail-soft de feeds preservado).
- Memória técnica: `Memorias/memoria_agente_youtube_antidesperdicio_20260822.md`.
- Manual dos loops atualizado: §10 em `Memorias/manual_agentes_youtube_operacao_20260816.md`.

## 6. ADENDO — FASE 2 (ordem Miguel ~21:00: "corrigir, salvar os de hoje, publicar, anotar, blindar")

**7 POSTS PUBLICADOS por ordem direta do Miguel (todos HTTP 200, revisão exaustiva ZM):**

| Post | Vídeo/Canal | Checagem |
|---|---|---|
| **267118** (21:15) | Cerimedo/TV Fórum — **o post PERDIDO das 20h, RECUPERADO custo zero** (`cache hit 28554 chars`) | fatos confirmados: indiciamento PF 2024 + exclusão PGR (g1/Estadão/Chequeado); nomes usados todos confirmados; duvidosos fora do texto |
| **267114** (21:11) | Farinazzo/TV 247 | nomes ok, "neste sábado" correto, Política+Vídeos |
| **267087** (21:11) | Marco Rubio/Brasil de Fato | Katia Marko grafia confirmada; fatos ok (tarifas 50%, Cuba 67 anos) |
| **266745** (21:20) | TSE×Flávio/O Povo | 2 dias, sem datas no texto |
| **266545** (21:20) | Lula Sudeste/TV Fórum | correções: R$ 61 mi (repasse PF) vs R$ 134 mi (negociação no áudio) EXPLICITADOS (checado Agência Pública/FPA) + "abaderna"→"baderna" + "Praça dos Três Poderes" |
| **266525** (21:20) | Zâmbia/TV GGN | correções: "nesta terça-feira"→"na terça-feira, 18 de agosto" + "célula"→"cédulas" |
| **266494** (21:40) | Petróleo Amapá/TV Fórum | 6º rascunho descoberto ao zerar a fila; ajuste de data idem |

**Fila YouTube: ZERADA** → breaker LIBERADO (produção retoma sozinha nas próximas rodadas). Datas dos atrasados atualizadas para o momento da publicação (visibilidade na home; post_date_gmt correto — sem risco do bug GMT).

**Fix adicional da fase 2:** cascata do CURADOR ganhou reservas (deepseek → qwen-plus → gpt-4o-mini → kimi) — antes era deepseek-só na prática (kimi 429). GLM-4.5-flash respondendo vazio registrado em BUGS_ATIVOS (ambiente; cascata consertada já tolera).

**Bugs anotados em** `CEREBRO_NODE_BUGS_RESOLVIDOS.md` (2 entradas 22/08) + `CEREBRO_NODE_BUGS_ATIVOS.md` (glm vazio).

## 7. ADENDO — GSN V2 RECUPERADO (ordem Miguel 22/08 ~21:20: "corrige então o gsn também")

**3 causas em camadas, todas corrigidas (com backups):**
1. **🔴 SEV-1 — crontab do NYC DESTRUÍDO hoje**: de 25KB (base 16:08 BRT) para 310B às 21:17 BRT — edição por arquivo parcial apagou TODAS as verticais V4 + GSN + manchete + CCTV. RESTAURADO: **53 linhas ativas** (base `crontab.bak_pre_forcada_20260822` + linhas de hoje preservadas: ate00/tribunal/v41 sombra). Backups `crontab.bak_pre_restore_full_20260823_0020` + `crontab.restore_20260823`. **Lição reforçada: NUNCA `crontab arquivo_parcial` — sempre `crontab -l > tmp && editar && crontab tmp`.**
2. **Cron do GSN estava PAUSADO desde 19/08** (comentário `PAUSADO_20260819_ZCODE` — ordem antiga "só Cafezinho fica"). **Revogado pela ordem de hoje**; linha reativada com comentário datado (`0 11,17 * * *` UTC = 08h/14h BRT).
3. **Proxy IPRoyal 402 engolia TUDO no GSN** (RSS, Transkriptor api.tor.app, thumbs i.ytimg.com, yt-dlp) desde 20/08. Fix definitivo em 2 camadas: (a) `trust_env=False` no `/root/agente_youtube_watcher.py` (mesma medicina dos V4; backup `.bak_pre_trustenv_20260823`); (b) **CAUSA RAIZ SUTIL: o `chaves.sh` sempre teve `no_proxy` MINÚSCULO (lista antiga) — a stack Python do NYC só honra o minúsculo; o `NO_PROXY` maiúsculo é ignorado.** Hosts `www.youtube.com, i.ytimg.com, img.youtube.com, api.tor.app` adicionados às DUAS linhas (backups `.bak_pre_noproxy_*_20260823`). + yt-dlp binário instalado no NYC (fallback de transcrição; versão 2026.08.19).

**PROVA E2E (run manual 00:47→01:00 UTC):** RSS 200 direto nos 7 canais → transcrições `done` (h2SaRdsG7F0, 3QkC1nFHHWY) → produtor ("noticia_publicavel": 2) → auditor → publicador → **2 JSONs novos na `/root/agent_data/gsn_fila/` às 00:59** (esperando o CM, fluxo normal). 2 vídeos seguem `failed` intermitente ("todos_provedores_falharam", provável bot_check por item) — o cron continua re-tentando (tentativas 3-4 de limite próprio).

**Para o CM/loops:** gsn_fila agora tem 5 itens (3 de 18-19/08 + 2 frescos de hoje: Larry Johnson e o 3QkC1nFHHWY) — revisar e publicar no GSN. Anti-desperdício do nacional (breaker) NÃO foi portado ao GSN (arquitetura diferente, banco próprio com descarte de vencidos — `texto_vencido`/`descartado_vencido` já limitam acúmulo); se a gsn_fila crescer sem consumo, vale um breaker equivalente na próxima iteração.

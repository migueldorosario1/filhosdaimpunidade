# Fórum — Renovação IPRoyal: credencial no cofre + fallback anti-bloqueio no agente YouTube

**Data:** 2026-08-03 ~15:50 BRT
**Executado por:** Kimi K3 (ZCode), a pedido do Miguel
**Memória técnica (Tema Duplo):** `Cerebro/Memorias/memoria_iproyal_renovacao_fallback_youtube_20260803.md`

## Contexto

Miguel renovou a assinatura do **IPRoyal** (proxy residencial) destinada ao **agente YouTube** e "possivelmente ao Moka Reader". Pediu: conferir no Cérebro, testar a credencial, **marcar telemetria** e **deixar preparado para desligar** caso se use pouco.

## Decisões

1. **IPRoyal é útil, com papel definido:** camada **anti-bloqueio** dos pipelines yt-dlp (não rota padrão). Evidência própria: AUTH-047 (16/06) — YouTube destravado via IPRoyal após 30+ dias parado. Inútil em Beijing (GFW, teste 21/05) e para `.gov` (bloqueio pelo provedor, PACER 03/07).
2. **Arquitetura fallback:** yt-dlp tenta direto; só cai para o proxy em erro de bloqueio (`bot_check`, `http_429`, `http_403`, `geo_block`). RSS/thumbnails/Transkriptor-API seguem diretos.
3. **Credencial no cofre canônico** (fim da violação do Art. 1º — estava em plaintext só no `toggle_proxy.sh`): `IPROYAL_PROXY` gravada nos dois cofres locais (canônico + espelho). Fingerprints: URL completa `sha8:ed44d32f`; user `sha8:945b3368`; pass `sha8:9dd50483`.
4. **Chave de desligamento:** `YOUTUBE_PROXY_MODE` = `off` | `fallback` (padrão) | `always`. Desligar = trocar para `off` no cofre, zero código.
5. **Telemetria:** `agent_data/v4_cafezinho_youtube/telemetria_proxy.jsonl` — toda tentativa yt-dlp (direta/proxy, ok, latência, classe de erro, sessão). Resumo: `python3 util_proxy_iproyal.py --resumo`. **Ritual de decisão:** se em ~30 dias o resumo mostrar proxy raramente necessário → `YOUTUBE_PROXY_MODE=off` e avaliar cancelar renovação seguinte.

## Estado dos testes (03/08 ~15:45 BRT)

| Teste | Resultado |
|---|---|
| Smoke credencial (curl ipinfo) | ✅ exit NYC (Verizon) |
| yt-dlp via proxy (modo always) | ✅ rc=0, 8,0s |
| yt-dlp direto (modo fallback) | ✅ rc=0, 5,6s |
| Modo off | ✅ direto apenas |
| Agente importa c/ helper | ✅ |
| Rotação de sessão por chamada | ✅ (sessão fresca `…dYxlNlr0` no log) |

## Moka — veredito e implementação (atualizado ~16:00 BRT)

**Miguel confirmou: o alvo era o Moka VIDEO** (não o Reader). O Reader (mokareader.com) não tem ingestão server-side (API routes: apenas auth/proxy-CORS/tts) — nada a fazer nele.

**Moka Video INTEGRADO nesta mesma sessão:** o `/api/ingest` (yt-dlp+ffmpeg server-side) ganhou o mesmo padrão de fallback:
- `src/lib/iproyal.ts` (**novo**) — espelho TS do helper Python: direto → proxy só em bloqueio, sessão nova por chamada, telemetria no **mesmo jsonl** (`fonte: "moka_video"`).
- `src/app/api/ingest/route.ts` — 2 call sites patchados (`ytDlpJson` meta + `downloadAudioChunks` áudio). Backup `.bak_pre_20260803_iproyal`.
- **Chave de desligamento própria:** `MOKA_PROXY_MODE` (off|fallback|always); se ausente, herda `YOUTUBE_PROXY_MODE`. Sem credencial → off.
- **Testes:** tsc --noEmit limpo; 3 modos ao vivo via Node (always→proxy / fallback→direto / off→direto) — 3/3 ✅; telemetria unificada com breakdown por fonte no `--resumo`.

## Arquivos tocados (backups `.bak_pre_20260803_iproyal`)

- `Outros/chaves/agentes_labs/.env.unificado` + `Projeto Cafezinho Agentes/root/.env.unificado` (IPROYAL_PROXY + YOUTUBE_PROXY_MODE)
- `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py` (**novo** — helper compartilhado)
- `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` (3 call sites yt-dlp)
- `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_youtube_transcript.py` (2 call sites, import defensivo)
- `~/.gemini/.../scratch/toggle_proxy.sh` (higienizado: lê do cofre, sem plaintext)

## Pendências

- [ ] Espelhar `IPROYAL_PROXY` nos cofres dos servidores (Tencent/NYC) se algum pipeline yt-dlp rodar lá (Constituição §2). Beijing: **não** (GFW).
- [x] Ritual de decisão ~30 dias: `--resumo` → manter ou `off`. **Agendado: 2026-09-02 09:00 (automação ZCode).**
- [x] Moka Video `/api/ingest`: padrão aplicado nesta sessão (ver seção Moka acima).


---

## Cascata multi-provedor ("se cai um, entra outro" — pedido Miguel, 03/08 ~16:40 BRT)

Miguel declarou a conta IPRoyal descartável ("se cancelarem, dane-se") e pediu alternativas para um sistema robusto com vários fallbacks. Pesquisa de mercado (03/08, fontes: páginas de pricing + Proxyway/Trustpilot) e implementação da cascata concluídas na mesma sessão.

### Resultado da pesquisa (proxies residenciais p/ YouTube)

| Provedor | Preço | Expira? | Nota para o caso |
|---|---|---|---|
| **DataImpulse** ⭐ recomendado p/ slot 2 | $1/GB (mín. $50) | **NUNCA** | "pneu sobressalente" ideal: fica parado sem perder valor. Ressalva: queixas de contagem de GB inflada (monitorar) |
| **Decodo** (ex-Smartproxy) ⭐ alternativa forte | $4/GB PAYG | ciclo | 2,85M IPs medidos, ~100% Google, Proxyway 9,3/10 — se IPRoyal falhar muito, vira candidato a primário |
| Webshare | $3,50/GB (1 GB grátis/mês p/ teste) | — | 88% Google; terceiro slot |
| Bright Data Web Unlocker | ~$1/1k req (só sucesso) | — | último recurso anti-bloqueio teimoso |
| ~~NetNut~~ | — | — | **DESCARTADO: domínio apreendido pelo FBI (verificado 03/08)** |
| ~~PacketStream~~ | $1/GB | não | 11% de sucesso em Google — inviável |

### Camada extra (diferente de proxy — fase futura, se quiser)
APIs de transcrição pronta: **ScrapeCreators** (~$0,001/transcrição c/ timestamps, créditos nunca expiram, $47/25k) e **Supadata** (100 grátis/mês). Não precisam de proxy nenhum. Decisão pendente do Miguel.

### Implementado (cascata já no ar, slots dormentes)
- `IPROYAL_PROXY` (slot 1, ativo) → `PROXY_RESIDENCIAL_2` → `PROXY_RESIDENCIAL_3` (slots documentados nos 2 cofres, vazios).
- Direto bloqueado → proxy1 → proxy2 → proxy3, sessão fresca por tentativa, formatos de sessão por provedor (session-/sessid-/sem sessão) tratados.
- Telemetria com campo `provedor` (nome pelo host). Resumo mostra breakdown por fonte E provedor.
- Testes: simulação completa da cascata (direto bot_check → iproyal falha → dataimpulse salva) ✅ · modo off sem retentativa ✅ · tsc limpo ✅ · Node enumeração + always ao vivo via IPRoyal ✅ · agente importa ✅.
- **Para ativar slot 2:** Miguel compra DataImpulse ($50, nunca expira) ou Decodo e cola a URL completa na variável `PROXY_RESIDENCIAL_2` dos dois `.env.unificado`. Zero código.


---

## APIs de transcrição para o Moka Video (pesquisa 03/08 ~17:10 BRT — "quero uma lista!" Miguel)

Pesquisa completa de mercado + teste ao vivo. Insight-chave: na categoria extração-de-legendas o preço é **por vídeo, não por minuto** — 100–1.000 vídeos/mês custam $1–20/mês; o custo real do Moka segue sendo o LLM do resumo.

### Ranking (custo-benefício p/ 1.000 vídeos/mês ~30min)

| # | API | Preço/vídeo | Créditos expiram? | X/IG | Nota |
|---|---|---|---|---|---|
| 1 ⭐ | **ScrapeCreators** | $0,001–0,002 ($47/25k) | **nunca** | **ambos** | Melhor compra: 1 chave p/ YouTube+X+IG; cache grátis |
| 2 | **Supadata** | $0,0057 ($17/3k/mês) | mensal | ambos | Único c/ **transcrição por IA** p/ vídeo sem legenda (2 créd/min) |
| 3 | **ScrapeBadger** | $0,0007 | nunca | só X | Mais barato; SRT/VTT prontos; menos maduro |
| 4 | **SearchAPI.io** | $0,004 ($40/10k) | — | não | **JÁ TEMOS CHAVE (teste ao vivo 03/08: 2.760 segmentos c/ timestamps em PT ✅)** — MAS é a reserva do gate fact-check (cota compartilhada) |
| 5 | **SocialKit** | $29/mês | — | ambos | Custo/request opaco |

Descartadas: Kome/NoteGPT/Tactiq (sem API real), youtube-transcript-api (bloqueio de IP), ASR puras (AssemblyAI $0,15/h — **temos crédito**, Deepgram, Gladia, Whisper) = último fallback de áudio.

### Arquitetura proposta para o /api/ingest (4 andares)
1. Legendas oficiais/auto via yt-dlp direto (grátis)
2. **API de transcrição** (ScrapeCreators quando comprada; SearchAPI se Miguel liberar a cota)
3. yt-dlp via cascata de proxies (implementado 03/08)
4. Áudio → Whisper/AssemblyAI (já existe)

### Decisão PENDENTE do Miguel
(a) ScrapeCreators dedicada ($47 — recomendado) · (b) SearchAPI agora dividindo cota do fact-check · (c) híbrido (SearchAPI valida fluxo, migra depois). Respostas das APIs têm schemas diferentes — integração será feita após a escolha (10 min de trabalho). Fontes completas na memória.

---

## Adendo 17/08/2026 00:07 — Miguel perguntou se vale a pena manter o IPRoyal

**Resposta dada (ZCode/Qwen 3.8):** SIM, a assinatura existe e vale manter.
- Pedido #78690692 (Residential Proxies, US$ 11,90, criado 03/08) → plano **2 GB/mês, renova 02/09/2026** (bate com o registro daqui "renovado 2026-08-03"). Suporte do IPRoyal confundiu no 1º atendimento, depois confirmou no dashboard.
- Transcrição **não depende** do IPRoyal: quem transcreve é o **Transkriptor** (URL-direto = o próprio Transkriptor baixa o vídeo, sem proxy). Só o fallback S3 (raro: 1 uso) + checagens de duração do yt-dlp (56 via proxy) usam.
- Telemetria (03/08→16/08): 96 tentativas yt-dlp; proxy salvou **61 operações** de bloqueio (bot_check=7, timeout=15 entre os diretos). Proxy testado ao vivo 16/08: HTTP 200, saída EUA, 1,5s. NYC também usa a mesma credencial.
- Rejeições de transcrição (69 qualidade + 55 falha em 195) são problema do **Transkriptor**, não do proxy.
- Revisão manter/desligar segue agendada **02/09/2026 09:00** (`util_proxy_iproyal.py --resumo`).

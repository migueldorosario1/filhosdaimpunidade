# 🧠 Memória — Build do Droplet Utilitário (Central + agentes + YouTube)

> **Fórum:** `Foruns/forum_droplet_utilitario_20260806.md`
> **Sessão:** ZCode (Kimi K3), chat direto, 06/08/2026. Droplet `142.93.48.252`.

## Inventário final do droplet

- **Central de Alertas** (sessão anterior): Kuma (13 monitores) + vigia de discos (:42).
- **Agentes migrados:** `/root/agentes/ferroviario` (Mundo Trilhos/Rail Post) + `/root/agentes/turismo` (Discover Brazil).
- **YouTube:** `/root/gsn_agentes/` (GSN, código de 05/06 intacto, crons reativados) + `/root/aiatolah/` (novo na central).
- **Config global:** `/root/config/` copiada do rio-ag (13 JSONs, essencial — sem ela o roteador LLM cai em fallback mínimo só Claude/GPT e falha).
- **Swap 2G** criado (RAM é 1G). Deps: feedparser, beautifulsoup4, pillow, youtube-transcript-api, trafilatura, python-dotenv, yt-dlp (já tinha), openai (já tinha).
- **Chave GitHub** `id_ed25519_cicero_github` (do rio-ag) instalada → push nos 4 repos (mundo-trilhos, rail-post, discover-brazil, aiatolah).

## Bugs encontrados e corrigidos (lições)

1. **Channel IDs Aiatolah 5/6 errados** — validação via `feeds/videos.xml`: retornavam HTTP 404 (= zero vídeos). Corrigidos com IDs reais extraídos das páginas `@handle`. Pós-fix: 15 vídeos cada. Ver fórum.
2. **Chaves LLM mortas nos envs de servidor** — DeepSeek (401) e Qwen (401) das envs antigas do rio-ag estavam mortas. Substituídas pelas vivas do cofre local (`cafezinho_root/legacy_chaves_novas.env` para DS, `agentes_labs/.env.unificado` para Qwen). **Lição permanente:** antes de migrar agente, smoke-testar TODAS as chaves do env de destino, não assumir que funcionam.
3. **`/root/config/` ausente** — roteador LLM (`agente_roteador_llm.py`) lê `llm_providers.json` de lá. Sem ela: "cadeia toda falhou". Copiar config junto com código é obrigatório.
4. **Turismo `search_brave` sem fallback** — diferente do ferroviário, não tinha `search_perplexity`. Patchado (mesmo padrão). Bug pré-existente: falhava silenciosamente há dias no rio-ag ("Sem fontes válidas").
5. **Paths hardcoded no turismo** — `DISCOVER_BRAZIL_REPO` default aponta `/home/migueldorosario/Downloads/...`. Corrigido via env no wrapper (`export DISCOVER_BRAZIL_REPO=/root/agentes/turismo/discover_brazil`). Ferroviário já tinha wrapper certo (`MUNDO_TRILHOS_REPO`); normalizado também o default no código (`/root/agentes/ferroviario/mundo-trilhos`).
6. **Brave API** — todas as chaves do cofre testadas: 1 dá 403, 2 mortas. Nenhuma viva. Agents sobrevivem via fallback Perplexity (ativo nos dois após patches).

## Provas de fogo (06/08)

- **Ferroviário teste4 ✅ PUBLICOU**: gerou artigo via `deepseek-v4-pro`, upload R2 hero OK, push git `rail-post` "Git push OK" (post: "Bi-oceanic railway between Brazil and China redefines the geography of South America"). Mundo Trilhos PT também.
- **Turismo busca ✅**: pós-patch, `search_brave` retorna 5 fontes via Perplexity (antes: 0).
- **Aiatolah channels ✅**: 6/6 canais = 15 vídeos cada (antes 5/6 = 0).
- **GSN YouTube**: Qwen+DeepSeek vivas; coletor roda 22h (1º ciclo novo).
- Turismo teste5 (com wrapper+DISCOVER_BRAZIL_REPO) em validação.

## Crons ativos na central (crontab -l)

```
42 * * * *   .../vigia_discos.py                          # vigia discos (sessão anterior)
15 */2 * * *  flock .../run_ferroviario.sh               # FERROVIARIO_CENTRAL
15 4 * * *    flock .../retry_ferroviario.sh             # FERROVIARIO_RETRY_CENTRAL
42 9,13,17,21 * * * flock .../run_turismo.sh             # TURISMO_CENTRAL
0 6,14,22 * * *  cd gsn_agentes && coletor youtube       # GSN_YT_COLETOR_CENTRAL
35 6,14,22 * * * cd gsn_agentes && publicador            # GSN_YT_PUBLICADOR_CENTRAL
0 */6 * * *   cd aiatolah && aiatolah_agente_youtube.py  # AIATOLAH_YT_CENTRAL
```

## Crons desligados no rio-ag

`/root/crontab_backup_pre_migracao_central_20260806.txt` — ferroviário (`0 */2`), retry (`0 4`), turismo (`37 9,13,17,21`). Cícero e GSN seguem no rio-ag.

## Pendências

- Turismo teste5 (validar publicação — em andamento).
- Repositório `aiatolah-v4` — confirmar se é lixo (não publicador).
- **LEMBRETE Miguel:** reconstruir failover NYC↔Tencent (não tocado).

---

## 🔍 REAVALIAÇÃO KIMI K3 (06/08 ~21:50 UTC — ordem Miguel "reavalia tudo")

Achados e correções (todos verificados):

1. **🔴 CRÍTICO — "Git push OK" era FALSO nos 3 repos migrados.** Os agentes salvavam posts em disco mas o `git commit` falhava silenciosamente (central sem `user.name`/`user.email`) e o push retornava "Everything up-to-date" → log "push OK" mentiroso. Causa-raiz dupla: identidade git ausente + `check=False` no `git_cmd` (nunca olha returncode do commit). **Correções:** (a) identidade configurada (`Agente Trilhos-Turismo <agente@mundotrilhos.com>`); (b) **commit-guard patch** nos 2 agentes — commit falho agora loga + Telegram (ferroviário) e aborta antes do push (backups `.bak_pre_commit_guard_20260806`); (c) 5 posts pendentes commitados/pushados DE VERDADE e verificados no origin: mundo-trilhos `ec5b9fc`, rail-post `5b78560`, discover_brazil `f7526a5`. **Lição permanente: "push OK" em log NÃO é prova de publicação — prova é `git rev-parse HEAD == origin/main`.**
2. **rio-ag:** fsck limpo nos 3 repos (cicero/gsn/rio-carta) após o git-gc interrompido por timeout — sem dano. Load caiu 2.32→1.70. rsyslogd ~44% CPU persiste (volume de log dos agentes) — pendência menor, não crítica.
3. **Central:** Kuma 779/779 heartbeats UP na hora; vigia :42 rodando, anti-spam correto (rio-ag 87% já conhecido, relembra 1×/24h).
4. **GSN YouTube:** inbox VAZIO + 178 vistos → sem risco de republicar junho às 22h ✅.
5. **🟠 Aiatolah — post fora de escopo + alucinado (revertido).** 1ª execução publicou "Como a Guerra Civil terminou" (Lex Fridman é canal generalista) escrito a partir da DESCRIÇÃO (transcrição bloqueada por IP de datacenter) — LLM inventou analogia Guerra Civil×chips. Fluente mas sem fonte. **Revertido** (commit `5a584ba`, no origin). **4 patches aplicados e testados:** (a) **filtro temático IA** na coleta (keywords+regex; prova: Guerra Civil filtrado, GPT/DeepSeek passam); (b) **gate de transcrição** — sem transcrição real ≥500 chars = NÃO publica (fim da alucinação estrutural); (c) **proxy IPRoyal** na transcrição com API nova `GenericProxyConfig` + retry ×2 (prova: 4672 chars reais via IP residencial Comcast); (d) unpack seguro no caller. Backups `.bak_pre_filtro_gate_20260806`.
6. **GSN publicador nota:** usa Transkriptor (API externa — imune a IP ban local). Aiatolah usa youtube-transcript-api (grátis, precisa proxy). Diferença de arquitetura registrada.

**Estado final pós-reavaliação:** tudo que foi anunciado como "publicado" agora ESTÁ publicado de fato (origin verificado); os 2 modos de falha silenciosa (commit git; transcrição→conteúdo inventado) têm guards permanentes.

---

## 📡 Adendo 2 — 06/08 ~22:05: cobertura IPRoyal em TODOS os agentes YouTube (pergunta do Miguel)

**Pergunta:** "os agentes youtube têm acesso ao Royal IP para caso de bloqueio do YouTube?"
**Achado:** o **GSN coletor NÃO tinha** — usava yt-dlp puro (2 call sites: `_obter_canal`, `_obter_idade_horas`) e os envs GSN não tinham `IPROYAL_PROXY`. E o teste ao vivo provou que **o yt-dlp direto JÁ é bloqueado do IP da central (NYC)** — o fallback disparou sozinho no primeiro teste.

**Corrigido:**
- `IPROYAL_PROXY` injetada nos 2 envs GSN da central (`/root/chaves_gsn.env` + `/root/gsn_agentes/chaves_gsn.env`).
- Patch no coletor (`gsn_agente_youtube.py`, backup `.bak_pre_iproyal_20260806`): helper novo `_ytdlp_print()` = direto → se falhar/bloquear → `yt-dlp --proxy $IPROYAL_PROXY`. Padrão canônico do `forum_iproyal_renovacao_fallback_youtube_20260803`.
- **Prova:** canal "Lex Clips" + idade 54h retornados VIA proxy (direto bloqueado); proxy forçado rc=0.

**Mapa de cobertura YouTube×IPRoyal (final 06/08):**
| Pipeline | Cobertura | Como |
|---|---|---|
| Aiatolah YouTube (central) | ✅ | transcrição via `GenericProxyConfig` + retry ×2 (hoje) |
| GSN YouTube coletor (central) | ✅ | yt-dlp `--proxy` fallback (hoje) |
| GSN YouTube publicador (central) | ➖ não precisa | Transkriptor é API externa |
| YouTube Cafezinho (local) | ✅ | fallback IPRoyal desde 03/08 |
| Moka Video (Vercel) | ✅ | `iproyal.ts` desde 03/08 |

**Regra viva sugerida:** todo pipeline novo que tocar YouTube DEVE nascer com fallback IPRoyal (IPs de datacenter são bloqueados por padrão).

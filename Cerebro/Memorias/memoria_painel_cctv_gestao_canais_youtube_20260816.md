# Memória — Gestão de canais YouTube pelo Painel CCTV V6 (log técnico, 16/08/2026)

> Tema Duplo com `Foruns/forum_painel_cctv_gestao_canais_youtube_20260816.md`. Sessão ZCode (Qwen 3.8), missão 2 do sprint do agente YouTube de 16/08/2026.

## 1. Decisão de arquitetura

O painel roda na **Tencent** (`/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`, serviço `cctv-v6.service` porta 8084, nginx tira o prefixo `/v6`). Os agentes leem JSONs no **PC do Miguel** (agente nacional Cafezinho + configs V4) e no **NYC** (pipeline GSN V2). Tencent→YouTube não alcança (China), então a validação de canal acontece no PC local, que tem o proxy iProyal.

**Escolha: caixa de entrada (mailbox).** Painel escreve pedidos append-only + visão otimista; cron local aplica e devolve o estado canônico. Alternativas descartadas: Cérebro como ponte (`/root/Cerebro` na Tencent está STALE desde 11/06) e escrita direta do painel nos JSONs locais (sem rota Tencent→PC).

## 2. Estrutura criada na Tencent

```
/home/ubuntu/cafezinho/v6/youtube_canais/
├── vivo/{cafezinho,gsn,aiatolah,mapario}.json   # estado exibido (painel lê; sync local reescreve)
├── pedidos/                                      # JSONs pendentes (painel cria; sync consome)
└── aplicados/                                    # histórico com resultado ok/rejeitado+motivo
```
Schema do vivo: `{site, atualizado_em, fonte, canais:[{channel_id, nome, peso?, idioma?, origem?, categoria_ids?, status}]}`; status ∈ ativo|pendente|pendente_remocao.
Schema do pedido: `{id (ts_tipo_site), ts, site, tipo adicionar|remover, entrada, nome?, peso?, idioma?}` + após aplicação `{aplicado_em, resultado, nome_resolvido?|motivo?}`.

## 3. Mudanças no painel (`painel_cctv_v6.py`, backup `.bak_pre_youtube_canais_20260816`)

- NAV: `("/v6/youtube", "📺 YouTube", "youtube")`.
- `TEMATICOS`: **adicionado `mapario`** (mapario.com.br, 🏙️, post_re `/blog/[a-z0-9-]+`, sem GA4 ainda) — não existia na página.
- Seção nova antes do ROUTES: `YT_DIR`, `YT_SITES` (4 sites), `yt_extrair_id`, `yt_read_vivo`/`yt_write_vivo` (atômico via os.replace), `_yt_pedidos`, `yt_novo_pedido`, `_YT_JS` (template com placeholder `__SITE__` — evita o doubling de chaves em f-string), `yt_bloco(site)` (tabela + form + pendências + histórico `<details>` + JS fetch), `pagina_youtube()`.
- `pagina_tematico(slug)`: `yt_sec` com card 📺 para slug ∈ {gsn, aiatolah, mapario}.
- `ROUTES`: `/youtube`. `do_GET`: `/api/youtube/canais?site=`. `do_POST`: `/api/youtube/adicionar` e `/api/youtube/remover` (padrão `_ler_json_body`+`_send_json` do CEO).
- API adicionar: valida site/peso (0.5-5), dedup no vivo e nos pedidos abertos (por UC extraído), grava pedido + vivo otimista `status=pendente`. Remover: dedup, pedido + `status=pendente_remocao`. HTTP 409 em duplicatas.
- Deploy: scp + `py_compile` + `sudo systemctl restart cctv-v6` (22:15 BRT). Teste: `/youtube` 200 (o 404 inicial era eu testando COM prefixo direto na 8084 — nginx que tira o `/v6`).

## 4. Script local `agentes_cafezinho/sync_youtube_painel.py` + cron */5

Cron (crontab com backup em `/tmp/crontab.bak_pre_sync_youtube_20260816`, 115 linhas antes):
```
*/5 * * * * cd ".../Antigravity Google" && /usr/bin/python3 agentes_cafezinho/sync_youtube_painel.py >/dev/null 2>&1
```
Fluxo: lock 600s → `ssh tencent ls pedidos` → scp cada pedido → `resolver_entrada` (UC direto / URL / @handle → fetch HTML via proxy → regex channelId/browseId/externalId) → `rss_validar` (prova final: feeds/videos.xml 200 + título; **404/400 = rejeita definitivo; status 0/transitório = mantém pedido para próxima rodada**) → aplicar com backup `.bak_sync_<run>` → scp para `aplicados/` + rm do aberto → `reconstruir_vivo` dos 4 sites → scp para `vivo/`.

Aplicação por site:
- **cafezinho** → `agent_data/canais_cafezinho_youtube.json` (envelope `{site,idioma,escopo,nota,canais}` — cuidado: NÃO é lista pura). Novo canal: peso 1.5 (ou do pedido), idioma do form (default pt-BR), cats `[22,28]` pt-BR / `[5003,28]` outros, origem `painel`.
- **gsn** → `agent_data/configs/globalsouth.json` `.youtube.canais` (IDs puros) + `sync_nyc()`.
- **aiatolah** → `agent_data/configs/aiatolah.json` (IDs puros).
- **mapario** → `agent_data/configs/mapario.json` (formato feed-URL completo, como os existentes).
- `sync_nyc`: reconcilia config↔`/root/agent_data/canais_youtube.json` (ssh nyc; backup `.bak_sync_<run>` no NYC; novo = append `{nome, channel_id, sessao_preferida:"mundo", ativo:true}`; saída do config = `ativo:false`, nunca delete — conforme `Cerebro/claude_memory/agente_youtube_arquitetura.md`).

Nomes: cache `agent_data/youtube_canais_nomes.json` (40 nomes) — alimentado em toda resolução RSS; usado no vivo e no NYC.

## 5. Os 8 nomes resolvidos (RSS via proxy, 16/08)

| Site | channel_id | Nome real |
|---|---|---|
| GSN | UCgA-jOLyuwdMcXXJ3HzICVA | Neutrality Studies Français |
| GSN | UCZkiUDyOBtkaTWGRfGnKaHw | kremlin |
| Aiatolah | UCvxm0qTrGN_1LMYgUaftWyQ | Peter H. Diamandis (canal pessoal) |
| Aiatolah | UCCpNQKYvrnWQNjZprabMJlw | Moonshots Highlights |
| Aiatolah | UCye1YedIypHffYb8k6Gp9wg | Alex Kantrowitz |
| Mapa Rio | UC5oRxjbY3HHrP5Acsu2vtkQ | Rádio BandNews FM - Rio de Janeiro |
| Mapa Rio | UCdZO6QRQU5U7A99y3kjf8Qg | SBT Rio (sbtrio) |
| Mapa Rio | UCnQ9DvdKAyo-FRfTfQTVcgw | Prefeitura do Rio (PrefeituradoRio) |
| Mapa Rio | UCFCiSRbCVwQ_BQaDQBYxN_A | Poder360 |

Resolvidos também no teste: @AaronMate = UCXS6rlpeRDzVDOEIi-wlnRw (Aaron Maté) e @TheDuran = UCwGpHa6rMLjSSCBlckm5khw (feed "Alexander Mercouris") — este último anotado, não adicionado.

## 6. Testes ponta a ponta (22:18-22:23 BRT)

1. ❌ `UCaaaaaaaaaaaaaaaaaaaaaa` no cafezinho → rejeitado "RSS retornou HTTP 404 (channel_id não existe)" — motivo visível no histórico da página.
2. ✅ Band Jornalismo (UCoa-D_VfMkFrCYodrOC9-mA) no mapario → feed-URL gravada no config (backup criado) → depois **removida** pelo fluxo de remover (lista voltou aos 4 originais).
3. ✅ `https://www.youtube.com/@AaronMate` no gsn → handle resolvido → RSS OK → config local + NYC atualizado. A reconciliação também levou ao NYC Neutrality Studies Français + kremlin (estavam só no config). Aaron Maté ficou permanente (está em `entrevistados_preferidos`).
4. ✅ Push do vivo pós-rodada: `atualizado_em` novo nos 4 arquivos da Tencent; painel refletindo (32 canais cafezinho, 7 gsn, 3 aiatolah, 4 mapario; `pedidos/` vazio, `aplicados/` = 4).

## 7. Arquivos tocados

- Tencent: `painel_cctv_v6.py` (+ dir `youtube_canais/` com vivo/pedidos/aplicados).
- Local novo: `agentes_cafezinho/sync_youtube_painel.py`, `agent_data/youtube_canais_nomes.json`.
- Local alterado (pelos testes, com backups): `agent_data/configs/{globalsouth,mapario}.json`, NYC `canais_youtube.json`.
- Backups gerais: painel Tencent `.bak_pre_youtube_canais_20260816`; crontab `/tmp/crontab.bak_pre_sync_youtube_20260816`; por aplicação `.bak_sync_*` nos JSONs (inclusive NYC).

## 8. Gotchas anotados

- `canais_cafezinho_youtube.json` tem envelope dict (não é lista) — quase quebrou o seed.
- Testar rotas do painel direto na 8084 SEM o prefixo `/v6` (nginx remove).
- JS dentro de f-string do painel: usar template com `.replace("__SITE__", ...)` para não dobrar chaves.
- Falha transitória de proxy NÃO rejeita pedido — reprocessa na próxima rodada (só 404/400 do RSS é definitivo).
- Otimista `vivo` pode divergir por ≤5 min; a reconstrução do sync é quem manda (sobrescreve sempre).

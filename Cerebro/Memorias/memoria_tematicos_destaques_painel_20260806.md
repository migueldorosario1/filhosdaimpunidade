# 🧠 MEMÓRIA — Painel de Destaques Temáticos + Faxina de Imagens V4 (2026-08-06)

> **Tema duplo com:** `Cerebro/Foruns/forum_tematicos_destaques_painel_imagens_20260806.md` (decisões resumidas)
> **Sessão:** ZCode (Kimi K3), workspace ZCodeProject · **Início:** 06/08 ~11:40 BRT

## Ordem do Miguel (transcrição dos pontos)

1. Destaque do topo não pode repetir embaixo.
2. Destaque não pode ter mais de 48h — senão muda a regra e deixa as mais recentes.
3. Sites ainda não divulgados → regra de audiência vira vitrine quebrada → deixar os mais recentes na frente; destaques DESLIGADOS por enquanto.
4. Criar um painel amigável por site temático: ligar/desligar destaques + escolher a regra (destaque = maior audiência).
5. Ceará Digital: notícias da Luizianne Lins (escolhida candidata ao Senado; chapa fechada) + consertar imagens erradas/repetidas.
6. Ver se já existe no V4 identificação de imagem; programar melhor. Em todos — Rio Carta também.
7. Cafezinho canônico só com imagem artificial → V4 tem que melhorar imagens internacionais (estreito de Ormuz, Trump).
8. Acelerar o V4 (maneira mais inteligente e rápida).

## O que foi implementado (com caminhos)

### A. Sistema de destaques (3 regras + painel)

- **`agentes_tematicos/v4/ga4_destaques.py`** (reescrito parcial):
  - `carregar_dest_cfg(repo)` — lê `src/data/destaques_config.json`; sem arquivo → `enabled=false`.
  - `_parse_pubdate`/`_dentro_da_janela` — filtro 48h (`max_age_hours`, 0 = sem limite).
  - `regra`: "audiencia" (GA4 7d→28d) ou "recentes" (pula GA4).
  - entradas agora carregam `pubDate` (o painel mostra idade sem re-ler os .md).
  - desligado → sai sem tocar no destaques.json.
- **Templates** `sites-v4/<site>/src/pages/index.astro` (6 sites: ceara, riocarta, globalsouth, discoverbrazil, mundotrilhos, railpost) — patch via `v4/patch_destaques_templates.py`:
  - importa `destaques_config.json`; seção só renderiza se `enabled===true` e houver entrada fresca;
  - filtro 48h no frontmatter (defesa em profundidade);
  - lista de recentes exclui URLs dos destaques exibidos (anti-repetição).
  - mapario/aiatolah: sem seção de destaques — fora do escopo.
- **`src/data/destaques_config.json`** (novo, nos 6 repos): `{enabled:false, regra:"audiencia", max_age_hours:48, top:5}`.
- **Painel** `agentes_tematicos/v4/painel_destaques.py` — Flask, 127.0.0.1:5057, systemd user **`painel-destaques.service`** (enabled; python direto do pyenv 3.10.13 — o shim quebra sob systemd; `/usr/bin/python3` é 3.8 e não roda Flask 3.x). Ações: toggle, salvar regra/max_age/top, recalcular (chama `ga4_destaques.processar_site` inline). Toda ação: grava config → git add/commit/push → Vercel.
  - **Testado end-to-end no ceara:** toggle ON → commit `736ca34` + recálculo (manchete velha de 21/07 derrubada pela regra 48h) → toggle OFF → commit `ed56e40`.
  - **Pitfall systemd:** ExecStart com espaço no path precisa de aspas DUPLAS no ExecStart (e NÃO no WorkingDirectory).

### B. Verificação ao vivo (06/08 ~12:20 BRT)

- 6 domínios HTTP 200 com `<section class="featured-voices">` ausente: ceara.digital, riocarta.com, globalsouth.news, discoverbrazil.news, mundotrilhos.com, railpost.news.
- Post Luizianne: https://ceara.digital/blog/20260805-luizianne-lins-e-escolhida-para-o-senado-na-chapa-de-elmano/ 200 ✅.

### C. Faxina de imagens Ceará Digital

Auditoria (87 posts ativos): heroes repetidas só em posts smoke de junho; **problema real = posts-pessoa recentes com stock genérico/IA** (a pipeline horária cicero estava DESATIVADA no crontab; os posts vêm do orquestrador V4, cuja FASE 0/banco não pegou os casos — banco local sincronizado só 05/08 19:23).

**Causa-raiz registrada:** a dedup/anti-reuso + juiz derrubavam candidatas do banco e a cascata caía em Pixabay/Pexels. Simulação 06/08 12:3x provou FASE 0 saudável AGORA (ouro_80e5586a "É o próprio governador Elmano" aprovada pelo juiz). Vigiar próximos ciclos.

**9 swaps aplicados** (`v4/ceara_fix_heroes_20260806.py` — arquivo NOVO p/ bust CDN, padronização 1200×675 blur-fill, crédito real, hash registrado, órfã removida):
1. Luizianne Senado (IA Ideogram) → ouro_3bb0fd0c (Senado Federal CC BY 2.0) — verificado ao vivo (og:image novo).
2. Luizianne emendas (Pexels) → ouro_1ce275d4.
3. Elmano trajetória (Pexels) → ouro_80e5586a (headshot EBC).
4. Chagas/Elmano 1º turno (Pexels) → ouro_d2a795bc (Elmano+Lula, EBC).
5. Quaest Ciro 43% (Pixabay) → ouro_392f13ea (Ciro, CC BY 3.0). (ouro_ef55f87a barrada por anti-colisão aHash — já estava no site.)
6. Lula convenção PT (Unsplash) → ouro_fb9ab076 (Lula Oficial CC BY-SA 4.0).
7. Lula oficializa reeleição (Pexels) → ouro_f0682f77.
8. Girão/Michelle (Pexels) → ouro_1224bb0c (Agência Senado CC BY 2.0).
9. TRE-SP multa Lula (gravura de 1879!! "Theatrologia Política — O Paganini Preto") → ouro_fdff2cf1 (EBC).

**Rio Carta** (`v4/fix_heroes_banco.py riocarta`): Paes (ouro_7891c94f), Benedita (ouro_b4d1a7e2), Castro (ouro_40de6799) — push OK.

### D. Cafezinho canônico — imagens internacionais (NYC)

- **Causa raiz (agente explorador):** `v4_vertical_draft_worker.py` — banco só p/ "politica" + og:image só de domínios estatais BR → geopolítica 100% IA.
- **Ao chegar, a sessão-irmã (Kimi K3, banco de mídia) JÁ tinha:** estendido banco OURO p/ todas as seções (03/08) + `_registrar_falta_banco` + ordenação "retrato jornalístico" (06/08, backup `.bak_pre_retrato_jornalistico_20260806`). Coordenado: patch feito EM CIMA do arquivo dela (md5 conferido antes/depois).
- **Meu patch:** `_extract_flickr_live_photo(title, content)` — degrau entre banco/og:image e IA. Usa `flickr_live.buscar_foto_oficial` (Casa Branca, ONU, Pentágono, Macron, Xi, STF...); chave via `os.environ` → fallback `load_shell_env("/root/.env.unificado")`; mesma esteira: download sem proxy → validação pixels → juiz `_audit_original_photo`. Backup `.bak_pre_flickr_live_internacional_20260806`; compilado no venv do NYC; espelho local sincronizado (md5 75b849ea...).
- **Teste ao vivo:** pool casa_branca 500 fotos frescas (05/08); plano D achou Trump no Salão Oval 04/08; juiz reprovou p/ título "tarifas" (correto — foto não casa com o fato → cai p/ IA).
- **Gap que resta:** pauta internacional SEM entidade mapeada (ex.: "Estreito de Ormuz" puro) ainda cai em IA — o `_registrar_falta_banco` + robô do banco cobrem crescimento. flickr_live `_persistir_no_banco` falha no NYC (`table imagens has no column largura`) — dívida pré-existente, não bloqueia.

### E. Aceleração V4

- **Gargalo medido (agente):** fase de imagem — juiz visual sequencial (1-3s × até ~19/post).
- **`publicador.py` FASE B paralelizada:** download 4 workers → dedup hash sem LLM → juiz em lotes de 3 paralelos; primeiro aprovado NA ORDEM da cascata vence. Teste: 10.5s com 3 julgamentos paralelos (antes ~20-30s). Hashes de teste removidos do registro.
- **Fix Indexing API:** `notificar_e_logar(cfg.get("domain",""), url_post)` → `notificar_e_logar(url_post, agent_name=f"v4_{site_id}")`. 559/559 skips antes; whitelist valida URL completa (testado: ceara.digital/riocarta.com = True).

## Arquivos criados/alterados (local)

| Arquivo | Ação |
|---|---|
| `agentes_tematicos/v4/ga4_destaques.py` | regras painel + 48h + pubDate |
| `agentes_tematicos/v4/painel_destaques.py` | NOVO — painel Flask |
| `agentes_tematicos/v4/patch_destaques_templates.py` | NOVO — patcher templates |
| `agentes_tematicos/v4/fix_heroes_banco.py` | NOVO — swaps riocarta (genérico) |
| `agentes_tematicos/v4/ceara_fix_heroes_20260806.py` | NOVO — swaps ceara (9) |
| `agentes_tematicos/v4/publicador.py` | FASE B paralela + fix indexing |
| `sites-v4/{6 sites}/src/pages/index.astro` + `src/data/destaques_config.json` | regras + config (push em todos) |
| `~/.config/systemd/user/painel-destaques.service` | NOVO — serviço do painel |
| NYC `/root/v4_vertical_draft_worker.py` | degrau flickr_live (+backup) |

## Logs/observação

- Painel: `agent_data/v4/painel_destaques.log` · systemd: `/tmp/painel_destaques_systemd.log`
- Ciclo V4: `agent_data/v4/cron_v4.log` (vigiar run das 13:00/16:00 com cascata paralela)
- ga4_destaques cron `45 3,13 * * *` — agora loga "DESLIGADOS no painel" enquanto enabled=false.

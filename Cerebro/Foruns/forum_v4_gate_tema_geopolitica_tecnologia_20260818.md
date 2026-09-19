# 🧭 V4 — Correção estrutural da classificação de tema Geopolítica × Tecnologia (18/08)

**Ordem do Miguel (18/08 ~13:15):** "esse aqui é tecnologia. quem fez isso e porque errou? [266468] … pode corrigir isso estruturalmente?"

## O caso

Post **266468** "Demanda por inteligência artificial dispara preço do fosfeto de índio" — pauta de TECNOLOGIA publicada como **Geopolítica** (bloco errado da home). Já corrigido: categoria única agora `30 Tecnologia` (era 5003 Geopolítica), `_yoast_wpseo_primary_category=30`, verificado no canônico.

## Quem fez e por que errou

Quem fez: o **vertical V4 Geopolítica** (job `v4d_geopolitica_3185e3f647244ec9`, NYC). Por quê:

1. **Feed errado na lista da geopolitica:** `config_editorial.py` tinha `scmp.com/rss/91/feed` na seção geopolitica. O rss/91 é o feed **"News" GERAL do SCMP** (não Tech) — traz de tudo (tech, negócios, esporte). A pauta do fosfeto veio dele (título SCMP "The next silicon?…", seção /tech/tech-trends).
2. **A geopolitica não tinha gate de tema:** ao contrário da tecnologia (gate de nexo ≥4 desde 27/07), qualquer item dos feeds da geopolitica entrava no banco e o worker aplicava a categoria fixa do vertical (5003).

É a imagem-espelho do bug de 17/08 (`v4_classificacao_geopolitica_em_tecnologia_20260817_0315`): lá, geo entrava no bloco Tecnologia via gate frouxo; aqui, tech entrava em Geopolítica via feed errado + ausência de gate.

## Correção estrutural aplicada (NYC, 18/08 ~13:30-13:50 BRT)

| # | Arquivo | Mudança | Backup |
|---|---|---|---|
| 1 | `config_editorial.py` | geopolitica: rss/91 (News geral) → **rss/4 (China)**; tecnologia: rss/4 removido (SCMP não expõe mais feed Tech dedicado) | `.bak_pre_scmp_feeds_20260818` |
| 2 | `v4_vertical_intake.py` | **Gate tech PENDENTE desde 17/08 (bug 0315) APLICADO:** pauta de tecnologia exige termo TECH no TÍTULO (`missing_tech_term_in_title`) — geopolítica pura não entra mais no bloco Tecnologia | `.bak_pre_tema_gates_20260818` |
| 3 | `v4_vertical_intake.py` | **Gate novo da geopolitica (veto fail-open v2):** rejeita só título com sinal FORTE de fora-tema (esporte/negócios/saúde/cultura) E sem termo geopolítico no título (`off_theme_title_veto`) | `.bak_pre_gate_veto_v2_20260818` + `.bak_pre_fold_acentos_20260818` |

**Lição do gate v1 (importante):** a 1ª versão exigia nexo geopolítico (título ≥1 OU corpo ≥2 termos) e SOBREREJEITOU 77 pautas legítimas — geopolítica real em espanhol/francês/plural (Ucrânia, Gaza, Venezuela, Israel-Líbano, tarifaço). Revertida para o veto fail-open (rejeita pouco, com altíssima precisão: só 6 vetadas de 240 avaliadas — imóveis, chipmaker, esportes, Kanye, e-book). As 77 foram restauradas ao status `new`. Dobra de acentos via `_fold` ("tarifaço"→"tarifaco", "inteligência"→"inteligencia").

**Backlog limpo:** candidatas `new` da geopolitica reavaliadas com o veto (6 vetadas → `discarded` + rejections `off_theme_title_veto`; 234 legítimas mantidas). Banco com backup `geopolitica.sqlite3.bak_pre_gate_tema_20260818`.

## Testes e provas

- `py_compile` OK nos 2 arquivos.
- Unit: caso 266468 (PT e EN) tem `tech_tit ≥1` (entraria na tecnologia se chegasse pelo feed certo); Hormuz/siege/Kushner/explosiones-Ucrânia/tarifaço passam; Kanye vetado.
- **Intake real rodado em produção** (geopolitica): seen 37, accepted 27, rejected 10 (motivos de frescor normais), 0 erros.
- Post 266468: categorias verificadas (`30 Tecnologia` única).

## Rollback

Cada patch tem backup `.bak_pre_*` no próprio arquivo; `cp .bak arquivo` desfaz. DB: backup pré-limpeza. O próximo cron (coletor+intake 14:00) já roda com os gates novos.

## Pendências

- Loop Miguel (Claude) informado no canal Trindade (recategorização do 266468 + gates).
- Feed SCMP na tecnologia: sem substituição (não há feed Tech dedicado atual; tecnologia já tem 10+ feeds tech).

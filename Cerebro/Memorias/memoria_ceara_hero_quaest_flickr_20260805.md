# Memória — Ceará Digital: hero errada da matéria Quaest → composto Lula × Flávio (Flickr) — log técnico completo

**Data:** 2026-08-05 ~14:10 BRT · **Agente:** Kimi K3 (ZCode) · **Fórum irmão:** `Foruns/forum_ceara_hero_quaest_flickr_20260805.md`

## 1. Contexto e caminhos canônicos

| Item | Valor |
|---|---|
| Site | Ceará Digital — `https://ceara.digital` |
| Repo no ar | `git@github.com:migueldorosario1/ceara-v4.git` (branch `main`) |
| Path local do repo | `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-v4/ceara` |
| Blog dir | `src/content/blog` · Hero dir: `public/hero` |
| Config do pipeline | `agent_data/configs/ceara.json` (site_id `ceara`) |
| Pipeline V4 | `agentes_tematicos/v4/` (orquestrador; cron local `0 */8 * * * --site ceara` + `0 3,13 * * * --all`) |
| Estado por site | `agent_data/v4/ceara/{bruto,auditado}.jsonl` |
| Painel | `http://43.156.151.165/v6/tematicos/ceara-digital` (GA4 546675232) — slug `ceara` dá "não encontrado" |
| Repo ANTIGO (fora do ar) | `/root/cicero_remote/ceara-digital` no NYC — split-brain já registrado; cron 9:15 roda à toa, pendente ordem de desligamento |

## 2. Diagnóstico da hero errada

- Post: `src/content/blog/20260805-quaest-lula-lidera-cenarios-e-abre-5-pontos-sobre-flavio-bol.md`
- Hero errada: `public/hero/quaest-lula-lidera-cenarios-e-abre-5-pontos-sobre-flavio-bol.jpg` (242.254 bytes, 1200×675) — **portão do INPA/Manaus** (verificado visualmente). `hero_credit` mentia: "Wikimedia Commons (CC BY-SA 3.0) — União da Juventude Mestiça".
- Hipótese de causa: token "pesquisa(s)" do `visual_prompt` casou com "Instituto Nacional de Pesquisas da Amazônia" no Wikimedia; juiz visual (`nucleo_visao.julgar_imagem`) não barrou paisagem/instituição sem pessoa.
- Linha do tempo: post publicado **08:03**; FASE 0 Banco de Mídia V4 (`nucleo_banco_midia.py`, sync 12:08–12:18, fórum irmão ~12:30) ainda não existia → o post passou pela cascata antiga Wikimedia-first.
- Banco local hoje: `agent_data/v4/banco_midia/index.json` — 666 mídias; contagens de string: "lula"×275, "flavio"×88, **"elmano"/"camilo"/"ciro"×0** (gap de lideranças cearenses).

## 3. Busca no Flickr (ordem do Miguel) — candidatas avaliadas

Filtro usado: `flickr.com/search/?license=4,5,9,10` (CC BY / CC BY-SA / CC0 / PDM).

| Candidata | Fonte | Licença | Veredito |
|---|---|---|---|
| `199179160@N02/54627417094` | J.M Executive | PDM 1.0 | Lula com político, ~2000s — antiga, descartada |
| `199179160@N02/54627513105` | J.M Executive | PDM 1.0 | Lula × Bush G8 2008 — antiga, descartada |
| `197399771@N06/55159236767` (+ série ~14) | REPÚBLICA DE COLOMBIA | PDM 1.0 | mar/2026, mas plano geral de reunião bilateral CELAC-África; Lula pequeno no quadro — descartadas |
| `coletivoresistencia/5261...` (série) | Coletivo Resistência | CC | posse 2023, fotos de multidão — Lula não é sujeito claro, descartadas |
| `199179160@N02/54038543267` | J.M Executive | PDM 1.0 | **ESCOLHIDA — Lula atual, ao microfone em evento, 683×1024, nítido** |
| `agenciasenado/52865271068` | Agência Senado | **CC BY 2.0** | **ESCOLHIDA — retrato Flávio Bolsonaro (PL-RJ), Foto: Edilson Rodrigues, 1024×683** |

Fontes institucionais boas pra política BR no Flickr: `agenciasenado` (CC BY 2.0), `repúblicadecolombia`/governos (PDM), `palaciodoplanalto` (CC BY-NC-**ND** — ND barra recorte; evitar para hero padronizada).
Técnica de extração sem API key: `og:image` da página da foto (`live.staticflickr.com/..._b.jpg`, 1024px) via curl; página `/sizes/l/` expõe `photo_download.gne?size=l&id=...&secret=...`.

## 4. Montagem e publicação

1. Composto "versus" 1200×675 via PIL: Lula crop `(0,30,683,798)` → 600×675 à esquerda; Flávio crop `(157,0,764,683)` → 600×675 à direita; divisor branco 5px central. JPEG q88 → 129.162 bytes. Artefatos da sessão em `/tmp/` (`jm5.jpg`, `flavio1.jpg`, `hero_quaest_lula_flavio.jpg`, `hero_quaest_backup_inpa.jpg`).
2. Sobrescrita da hero no repo + `hero_credit` novo: `"Lula: J.M Executive/Flickr (domínio público) · Flávio Bolsonaro: Edilson Rodrigues/Agência Senado (CC BY 2.0)"`.
3. `git commit bbd77df` → `git push origin main` → deploy Vercel.
4. Verificação ao vivo: T+50s ainda servia asset antigo (242.254 B); **T+2min servindo 129.162 B = composto novo** (URL com `?v=2` para furar cache). Conferência visual do asset ao vivo: OK.

## 5. Estado de atualização do site (resposta à queixa "não traz novidade")

- `auditado.jsonl` vivo (última escrita 13:09); rodadas 8/8h + gerais 3h/13h.
- Volume: 03/08=10, 04/08=7, 05/08=4 posts. 25/25 últimos com termos Ceará no corpo.
- Veto foco_local rejeitando pautas alheias (Tailândia, acidente doméstico) — evidência de funcionamento.
- Ressalva editorial: gancho cearense às vezes é 1 parágrafo mecânico em pauta nacional (IBGE, hepatites) — ponto de qualidade do `produtor.py`, não de frequência.
- Home: `destaques.json` girado por GA4 (`ga4_destaques.py`, cron `45 3,13 * * *`) desde 01:26 — manchete = mais vista 7d/28d + padding de recentes; heroes validadas em disco.

## 6. Diretriz registrada (Miguel, verbatim)

> "As imagens têm que ser casadas com o texto. Se tiver nome no texto algum personagem, bota o nome, bota a foto da pessoa — procura no Flickr enquanto o v4 não fica pronto totalmente."

Cobertura automática hoje: FASE 0 Banco de Mídia V4 (retrato auditado de liderança antes do Wikimedia, `publicador.py::_buscar_hero` linhas ~301–336; matcher `nucleo_banco_midia.buscar_no_banco` por entidade ≥5 chars contida no título ou token forte — "lula" incluído após bug da estreia). Gap: lideranças cearenses no banco (sugerir ao Banco Ouro: Elmano de Freitas, Camilo Santana, Ciro Gomes, Luizianne Lins, Capitão Wagner, Evandro Leitão, André Fernandes). Até lá, Flickr manual (fontes §3).

## 7. Lições

- Matéria publicada minutos antes de uma melhoria de pipeline não herda a melhoria — correção pontual manual é o caminho (como aqui).
- Token ambíguo ("pesquisa") em `visual_prompt` derruba o match do Wikimedia para instituições homônimas; tokens de PESSOA devem ter prioridade (já resolvido via FASE 0 para quem está no banco).
- `og:image` do Flickr é atalho estável para avaliação visual rápida de candidatas sem API key.

## 8. FOLLOW-UP ~19:40 BRT — Ingestão de candidatos cearenses no Banco Ouro (log técnico)

**Ordem Miguel:** juntar fotos dos candidatos do Ceará ao Senado e ao governo, do Flickr, "agora".

### Varredura Flickr (filtro licenças 4,5,9,10 = CC BY/BY-SA/CC0/PDM)

| Pessoa | Achado | Fonte/licença | Ação |
|---|---|---|---|
| Camilo Santana | retrato oficial 2023 `agenciasenado/52689302784` | Rodrigo Viana/Agência Senado, CC BY 2.0 | ingerida |
| Cid Gomes | retrato oficial `agenciasenado/47017294601` | idem | ingerida (**1ª dele**) |
| Girão | retrato oficial `agenciasenado/47017295941` | idem | ingerida (**1ª dele**; entidade "Girão" p/ casar manchete curta) |
| Ciro Gomes | discursando UFABC `149558792@N06/35180953936` | Murilo Silva/CAPOL, CC BY 2.0 | ingerida (reforço) |
| Luizianne Lins | **gap Flickr** (contas 197902860@N03/126316392@N05 sem CC; CPMI-2019 = falso positivo, ela fora do Congresso) | — | banco já tinha 6 (Wikimedia/Senado) |
| Elmano de Freitas | **gap Flickr** (conta oficial `elmano13dopt` = all rights reserved) | — | banco já tinha 4 (Agência Brasil) |
| Capitão Wagner | gap Flickr → **Wikimedia**: `File:Deputado Federal Capitão Wagner.jpg` | Michel Jesus/Câmara, CC BY 3.0 | ingerida (**1ª dele**) |
| André Fernandes | gap Flickr → **Wikimedia**: `File:André Fernandes.jpg` | Câmara dos Deputados, CC BY 3.0 | ingerida (**1ª dele**) |

### Mecânica de ingestão (replicável)

1. Download original (Flickr: `photo_download.gne?size=o&id=…&secret=…` extraído de `/sizes/o/` via curl; Wikimedia: `Special:FilePath/<file>?width=1600`).
2. `scp` pacote p/ NYC; script `/tmp/ceara_fotos_ingest/ingest_nyc.py` (sessão): sha256 → upload R2 `ouro/politica/<slug>/<hash16>_<slug>.jpg` → INSERT em `midia_ouro` (38 colunas via dict; `uso_automatico=1`, `status_editorial=uso_automatico`, `origem_classificacao=revisao_agente_kimi_k3`, `status_direitos=licenca_confirmada_fonte_oficial`, tier por largura: ≥1600 ideal_1600, ≥1200 premium_1200).
3. Espelho local: copiar binário como `img/ouro_<hash16>.jpg` + item no `index.json` (id `ouro_<hash16>`, entities=[entidade], tags=["politica"]) — **mesmo padrão do dump**, então o sync semanal (seg 06:20, `banco_midia_sync.py`) sobrescreve sem duplicar.
4. ⚠️ Sync faz extract do tar por cima do `index.json` — adição SÓ local sem NYC é perdida; fonte da verdade = Banco Ouro NYC.
5. Dedup por `hash_sha256` (PK) — re-rodar o ingest é seguro (SKIP).

### Verificação

- NYC: 743 → **749 rows** (`INGEST_OK`, 4+2).
- Espelho local: 749 → **755 itens**.
- Matcher `buscar_no_banco` × 8 manchetes reais (2 por cargo): **8/8 com candidata** (Elmano 4, Ciro 7, Wagner 1, André 3, Camilo 5, Luizianne 10, Cid 1, Girão 8).
- Pegadinhas do matcher registradas: token <5 chars nunca casa ("ciro"/"cid" sozinhos não casam — entidades ficam "Ciro Gomes"/"Cid Gomes"); "Girão" (5) casa e cobre "Eduardo Girão". Miguel confirmou 05/08: manter "Ciro Gomes"/"Cid Gomes" (evita Ciro Nogueira/Mauro Cid).

## 9. Painel do Banco Ouro (pedido do Miguel, 05/08 ~20h)

- **Home (o que já entrou):** `http://43.156.151.165/midia-ouro/`
- **Revisão humana (fila de aprovação):** `http://43.156.151.165/midia-ouro/revisao`
- API: `/api/midia-ouro/review/next` (próximo da fila + `total_fila`) · `/api/midia-ouro/review/decision` (decisões).
- Estado da fila em 05/08 ~20h: **425 itens aguardando revisão humana** — por categoria: contextual_evento 148, retrato_evento 129, grupo_catalogacao_incompleta 80, grupo_identificado_revisao 41, personagem_secundario_revisao 21, vertical_requer_adaptacao 6. Por vertical: nacional 381, geopolitica 43, tecnologia 1.
- As 6 fotos ingeridas nesta sessão entraram como `uso_automatico` (revisão visual já feita pelo agente) — NÃO caem na fila.
- Origem do painel: `/root/painel_midia_ouro.py` no Tencent (Codex 28/06, nginx `/etc/nginx/conf.d/painel.conf`); doc `Ponto de Retomada/Codex/20260628_2140_banco_ouro_midia.md`.

# 🧠 MEMÓRIA — Mutirão de Ampliação do Banco de Mídia V4 do Cafezinho (09/08/2026)

> Tema Duplo: fórum `../Foruns/forum_mutirao_qwen_banco_midia_v4_20260809.md` (decisões resumidas + estado) · esta memória = log técnico completo.
> Executor: **Qwen 3.8 Max (Token Plan) no ZCode** (fallback do Kimi K3 🔴 esgotado; sessão iniciada ~07:30 BRT por convocação do Miguel).
> Sem segredos neste arquivo (regra do Cofre): só nomes de variáveis e caminhos.

## 1. Missão (carta do Miguel, quase literal)

Mutirão de ampliação do Banco Ouro de Mídia V4 nos eixos **Geopolítica (Hormuz/Irã/China), Ciência e Regional (governadores+Senado 27 UFs)**. Diretrizes: fotografias jornalísticas REAIS e licenciadas; baixar sempre o melhor original (mesmo pesado) como `original_master` e produzir `variante_portal` separada; nunca escolher imagem pequena para economizar espaço; Qwen Vision + Gemini Vision (2ª opinião semântica) DEPOIS da conversão; TSE confirma status eleitoral mas foto cadastral do TSE é último recurso; licenças, créditos, dedup, backups e arquitetura master Tencent → réplica NYC; lotes seguros; registrar tudo no fórum; assinar como Qwen 3.8.

## 2. Arquitetura e contratos (base herdada)

- **Master:** Tencent `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db` (SQLite). Réplica read-only NYC (sem sqlite3 CLI lá — usar python3). Sync canônico `/root/V3/sync_banco_ouro_para_nyc.sh` (Tencent→NYC somente; nunca escrever na réplica).
- **Dois objetos por foto:** `original_master` (bytes originais) + `variante_portal` (contrato `portal_v2_20260809`: 1600×900 16:9, adaptativa 200–700KB, **nunca upscale**; reprovada preserva o original e a linha fica visível como lacuna).
- **Dedup:** SHA-256 é chave primária — coluna `hash_sha256` (não "sha256").
- **Visão/tribunal:** wrapper robo precisa das env `BANCO_OURO_GEMINI_VISION=1` + `BANCO_OURO_GEMINI_BUDGET_DIARIO=120`, senão visão retorna `{"status":"desativado"}`. Orçamento na tabela `ouro_visao_diaria(dia, qwen, gemini)`, teto 120/dia.
- **Tribunal (síntese Qwen):** decisão na chave canônica `metadados_json["gemini_vision_banco_ouro"]` via `sintetizar_parecer()` (marcador `via=tribunal_qwen38_sintese`); quarentena → QUARENTENA_HUMANA (nunca REJEITAR); `lugar_override` só para `tipo_entidade=="lugar"` — foto de pessoa exige consenso real.
- **Classificador:** `/root/V3/classificar_banco_ouro_midia.py`, cron `17,47 * * * *`, reprocessa a tabela inteira. Regras de grupo seguram multi-pessoas em `revisao_humana`; `regra_nome_identificado_prioritario_miguel_20260807` aprova direto pessoa única identificada (score≥450).
- **TSE dados abertos:** `consulta_cand_2026.zip` (CC Atribuição, latin1, delimitador `;`, atualização diária); CD_CARGO 3=GOVERNADOR, 5=SENADOR; `DS_SITUACAO_CANDIDATURA="#NE"` = ainda não julgada. Minimização: **nunca exportar CPF/e-mail/título eleitoral**.
- **Rate limits Commons observados (IP NYC):** busca 429 após ~9–24 queries/janela; download 429 após ~10–19 arquivos; cooldown ~1h. Prática: sleep 25s entre downloads, 12s entre buscas, pré-cooldown 90s.

## 3. Etapas executadas (07:30 → 11:40 BRT)

### Etapas 0+1 — auditoria e correção do padrão de conversão (~08:20)
- Contrato `portal_v2_20260809` definido/auditado no `v3_imagem_portal.py`.
- Backfill: **113 variantes em 12 lotes** → banco com **633 conformes / 771**; fila de **138 lacunas** exportada (arquivos que não sustentam 1600×900 sem upscale — originais preservados).

### Etapa 2 — Geopolítica Hormuz/Irã/China (~10:05)
- **18 originais novos** (76 MB, Commons licenciado) + **18 variantes portal_v2** (readback 100%).
- Tribunal Qwen+Gemini REAL → **12 aprovadas / 6 quarentena**.
- **2 incidentes detectados e corrigidos:** (1) flag de visão ausente → reset + re-run; (2) colisão com classificador → adoção da chave canônica `gemini_vision_banco_ouro`.
- Pós-classificador: **7 uso_automatico novas** (Hormuz 2→5, Khamenei 0→2, Pezeshkian 0→1, Natanz 0→1) + 11 na fila humana. Master: 793 mídias / 251 auto.

### Etapa 3 — Ciência (§8) (~11:00)
- 2 lotes = **18 originais (324 MB)**; tribunal REAL **18/18 aprovadas**; pós-classificador **11 auto + 7 revisao_humana** (regra de grupo). Master: 813 mídias / 262 auto. Réplica NYC conferida 813/262 + itens 1-a-1.
- Cobertura balanceada (§8 "não concentrar em espaço/robôs"): espaço (JWST/ISS/Sentinel), clima (testemunho de gelo/glaciares), energia (ITER/Ivanpah), saúde (Fiocruz/Butantan), física (LHC×2), microscopia (Belgrado), quântica (qubit), supercomputação (Summit/ORNL), Antártica (EACF), síncrotron (Sirius/CNPEM), robótica/agro (Purdue).
- Manifestos: `ingest_tribunal_20260809_102621`, `ingest_ingerir_20260809_104655`, `ingest_tribunal_20260809_104830`, `ingest_ingerir_20260809_112234` (regional), `ingest_tribunal_20260809_112422` (regional).

### Etapa 4 — Regional (fundação + lote A, ~11:35)
- **Roster TSE auditável:** `fontes/tse/montar_roster_regional_tse.py` processa 27 CSVs de UF (pula BRASIL/_BR), filtra CD_CARGO 3/5, normaliza situação para o vocabulário do fórum (`#NE`→TSE_REGISTERED_PENDING). Saída `roster_regional_tse_2026.csv`: **175 candidaturas (71 governador + 104 senador), todas TSE_REGISTERED_PENDING** (dataset ainda se preenchendo — TSE geração 08/08 22:33). AVISOs de UF esparsas: MG gov=2/sen=0, MT gov=0/sen=1, PR gov=1/sen=0, RR gov=0/sen=3.
- **Pesquisa Commons:** 27 queries de governadores (22 na 1ª passada + 5 em retry pós-429, sleep 12s) → `candidatos_regional_governadores_all.jsonl` com **158 candidatos únicos**. Curadoria lote A (14) + lote B (12) em `curadoria_regional_loteA/B.json` (scores 450–480, `tipo_entidade="pessoa"`).
- **Lote A ingerido (10 governadores, 58 MB):** Gladson Cameli/AC, Paulo Dantas/AL, Clécio Luís/AP, Wilson Lima/AM, Jerônimo Rodrigues/BA, Elmano de Freitas/CE, Ibaneis Rocha/DF, Renato Casagrande/ES, Ronaldo Caiado/GO, Carlos Brandão/MA. Fontes: VPR, Planalto, Agência Brasília, ALEP, ALEAM, governos estaduais (CC BY 2.0/3.0/4.0, PD).
- **Tribunal REAL:** 2 consenso APROVAR (Paulo Dantas `e3ece0ae`, Caiado `9beebb4c`) + 8 quarentenas (comportamento CORRETO: pessoa em foto coletiva sem lugar_override).
- **Pós-classificador:** 2 uso_automatico (regra nome único) + 8 revisao_humana. **Master: 824 mídias / 264 auto.** Sync Tencent→NYC 11:28 ok; réplica conferida 824/264 + 10 itens 1-a-1.
- **Lacuna variante 1:** Brandão 1500×1000 (melhor disponível; sem upscale por contrato) — na fila de lacunas para caçar original maior.
- **João Azevêdo (PB) = GAP:** candidatos Commons inadequados (estampa histórica/fotos de grupo Datena) — próxima busca com outra query.

## 4. Arquivos tocados

**Local (`/home/migueldorosario/ZCodeProject/mutirao_midia_v4/`):**
- `codigos/manifesto_generico.py` (NOVO — construtor generalizado de manifestos: `<dir> <curadoria.json> <urls.txt> <saida.jsonl>`; pula <100KB; `Image.MAX_IMAGE_PIXELS=None`; calcula sha256/dims/bytes no Tencent)
- `codigos/retry_download_ciencia_lote2.sh` (padrão de download: lista nome\turl, UA `CafezinhoMutiraoMidiaV4/1.0`, valida HTTP 200 + >100KB, sleep 25s, SKIP_EXISTE)
- `codigos/pesquisa_fontes_mutirao_v4.py` (busca Commons; cópia NYC `pesquisa_fontes_retry5.py` com sleep 12s)
- `fontes/tse/montar_roster_regional_tse.py` (NOVO) + `fontes/tse/roster_regional_tse_2026.csv` (NOVO)
- `fontes/plan_regional_governadores.json` + `plan_regional_governadores_retry5.json`, `candidatos_regional_governadores_all.jsonl`, `curadoria_regional_loteA.json` (14), `curadoria_regional_loteB.json` (12), `download_regional_loteA.txt`, `download_regional_loteB.txt`
- scripts de check locais (scp-then-run): `check_regional_loteA.sh`, `export_entidades_banco.sh`, `check_nyc_regional_loteA.py` etc.

**Tencent:** `/root/V3/ingest_mutirao_v4.py` (patch `sintetizar_parecer()`), manifestos `ingest_*.jsonl` (5 nesta manhã), banco ouro master.

**NYC:** `/tmp/download_generico.sh.bash` (download genérico), `/tmp/regional_loteA/` (10 bons + 4 arquivos ruins de 2269 bytes que o SKIP_EXISTE vai rebaixar de novo), `check_nyc_*.py`.

## 5. Lições técnicas (não repetir)

1. **sqlite3 CLI do Tencent não tem `chr()`** — escrever SQL com aspas simples em arquivo local, scp para `/tmp`, `chmod +x`, sudo executar (2 reincidências).
2. **String entre aspas duplas = identificador de coluna no SQLite:** `SUM(status_editorial="uso_automatico")` compara com a coluna INTEGER `uso_automatico` → sempre 0. Sempre aspas simples (2 reincidências).
3. Coluna de dedup é `hash_sha256` (não `sha256`) — JOIN USING falha sem conferir o schema.
4. Edit do ZCode exige Read na janela corrente (read restaurado de resumo não conta).
5. Ordem de comandos: `chmod` antes do `mv` que renomeia o arquivo (comando composto com ordem invertida falhou 1×).
6. Arquivos Commons de erro têm 2269 bytes — validar sempre >100KB + HTTP 200; conferir byte counts idênticos entre buscas como indício de arquivo real.

## 6. Estado da missão

**O que aconteceu:** Etapas 0–3 completas; Etapa 4 com fundação pronta (roster TSE 175 + 158 candidatos Commons) e lote A ingerido (10 governadores; master 824/264). Ciência e Geopolítica com cobertura balanceada e tribunal real. Renovação 48h do monitor executada (ciclo 2→3, morto `MONITORAMENTO_DE_TRABALHO_2026_08_09_1138.md`).

**O que falta:**
1. Pós-cooldown Commons (~12:20 BRT): baixar **4 restantes do lote A** (idx058 Zema/MG, idx062 Riedel/MS, idx130 Mauro Mendes/MT, idx134 Helder/PA) + **12 do lote B** (Raquel Lyra/PE, Rafael Fonteles/PI, Ratinho Jr/PR, Cláudio Castro/RJ, Fátima Bezerra/RN, Marcos Rocha/RO, Denarium/RR, Eduardo Leite/RS, Jorginho Mello/SC, Mitidieri/SE, Tarcísio/SP, Wanderlei/TO) — janelas de ~10 downloads.
2. Manifesto (manifesto_generico.py com curadoria lote B) → ingest → tribunal → classificador → sync → verifica NYC → fórum.
3. Nova query para João Azevêdo (PB); caçar original maior para Brandão (lacuna variante).
4. **Senadores:** roster já levantado (104) — pesquisa Commons + curadoria + ingestão (maior volume restante).
5. Etapa 5: reclassificar `gemini_vision_erro` (21.390 linhas; majoritariamente falhas técnicas qwen_http_403/SSLError) como erro_tecnico_retry + dedup + reprocessar em lotes.

**O que preciso de você (Miguel):** nada bloqueante — o mutirão segue autônomo. Quando puder: (a) validar visualmente as 8 quarentenas de governadores na fila humana (1 clique cada) para liberar mais auto; (b) confirmar se mantenho prioridade governadores antes de avançar para os 104 senadores.

— Qwen 3.8 Max (Token Plan) no ZCode, 09/08/2026 ~11:45 BRT

## 7. Adendo — Janela 2 Regional (~12:30 BRT)

**Downloads:** a janela Commons reabriu em ~28 min (não 1h). Sonda única 200 → corrida completa: 3 restantes do lote A (Riedel/Mauro Mendes/Helder) + 6 do lote B (Lyra/Fonteles/Ratinho/Castro/Fátima/Marcos Rocha) = 10 OK; a janela fechou no 10º download da passada (429 nos 6 restantes do lote B). **Lição:** ssh com `| tee` mascara queda de conexão e exit code — o primeiro lote B caiu aos 6/12 e o log local parou; usar `nohup setsid` + log no servidor. O retry janela 3 (restantes 6) ficou agendado via `nohup bash -c 'sleep 2700; ...'` no próprio NYC.

**Tribunal:** 1 consenso APROVAR (Fátima Bezerra) + 9 quarentenas. **Incidente menor:** o writeback da chave canônica `gemini_vision_banco_ouro` falhou para 2 itens (Fátima, Marcos Rocha); a correção (reset do marcador `origem_classificacao='mutirao_qwen38_pendente'` + re-tribunal) cruzou com o cron do classificador (:17/:47) que consumiu o marcador antes do re-run; as chaves já estavam gravadas pelo tribunal em background e o estado final conferiu. **Lição:** não resetar marcador perto do :17/:47; sempre verificar o estado real das linhas antes de re-processar.

**Pós-classificador (12:17):** Fátima → uso_automatico (consenso + regra nome único). Renomeações canônicas do classificador: Eduardo Riedel → entidade "regional" (foto de grupo sem principal confirmado; nome preservado em `pessoas_identificadas_json`) e a foto curada como Cláudio Castro → entidade "Jair Bolsonaro" (proeminência visual identificada pela visão; dossiê original preservado nos metadados; fila humana resolve). Comportamento canônico da `regra_nome_identificado_prioritario_miguel_20260807` — sem perda de dado.

**Estado:** master 834 mídias / 265 auto; sync 12:22 ok; réplica NYC conferida 834/265. Orçamento visão: qwen 54 / gemini 60 de 120.

**Manifestos:** `ingest_ingerir_20260809_115314` + `ingest_tribunal_20260809_115419` (+ re-runs 115819/121932 vazios).

**Próximo:** janela 3 às ~12:38 BRT baixa os 6 restantes (Denarium/RR, Eduardo Leite/RS, Jorginho Mello/SC, Mitidieri/SE, Tarcísio/SP, Wanderlei/TO); depois manifesto com `curadoria_regional_loteB_resto.json` → ingest → tribunal (longe do :17/:47!) → classificador → sync → fórum. Em seguida: Senado (plano `plan_regional_senado_2026.json` com 104 queries já gerado).

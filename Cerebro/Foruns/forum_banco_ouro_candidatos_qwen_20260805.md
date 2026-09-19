# FÓRUM — Banco de Mídia V4: candidatos+governadores, filtro Qwen com auto-aprovação por consenso (05/08/2026)

**Data:** 2026-08-05 ~12:50-14:30 BRT · **Agente:** ZCode/Kimi K3 · **Gatilhos (Miguel, chat):** "traz fotos de governadores, dos candidatos do Ceará — Ciro Gomes, Elmano de Freitas, Eduardo Paes, Douglas Ruas — a gente vai falar muito desses candidatos; V4 regional de todos os estados, tem que ter foto de governadores de todos" · "melhora o V4: mais fotos, eclético, sem muita repetida — a cada dia uma rodada de vários diferentes, uma só de cada" · "pede pro coletor visual fazer uma boa curadoria com o Qwen Vision: tem que ter UMA pessoa destacada no meio; ele tem que VER a foto pra gente já fazer esse primeiro filtro" · "faz o Qwen ou o Gemini aprovar automaticamente quando tiver 100% de certeza — identificada a pessoa principal no meio, aprova; só quando tiver dúvida, manda pra mim no manual"

## 1. Lacuna medida

Banco Ouro tinha **ZERO** fotos de Ciro Gomes, Elmano de Freitas, Eduardo Paes, Douglas Ruas, Cláudio Castro, Zema e demais governadores (era todo Brasília: Lula ×99, Alckmin ×95…). Só Tarcísio (×8).

## 2. Pacote implementado (NYC, `V3_PACOTE_CANDIDATOS_GOVERNADORES_20260805`)

1. **Manifest +35 entidades** (`ENTIDADES_PADRAO` no `robo_banco_ouro_midia_v3.py`): 9 candidatos/figuras da cobertura 2026 (Ciro, Elmano, Camilo, Paes, Benedita, Douglas Ruas, Luizianne, André Fernandes, Rodrigo Neves) + **27 governadores de todos os estados** (V4 regional). Backups `.bak_pre_candidatos_governadores_qwen_20260805`.
2. **Fontes certas por pessoa** (`agente_midia_oficial_externa_v3.py`, backup `.bak_pre_fontes_candidatos_20260805`): nova fonte **Governo do Ceará no Flickr** (governodoceara — confirmada viva) + 17 regras de mapeamento (Ciro→EBC/TSE/PDT/GovCE; Elmano→GovCE; Paes→Prefeitura Rio; Castro→GovRJ; Tarcísio→GovSP…). Antes: tudo caía no fallback Agência Brasil (Ciro vinha com 0 candidatos).
3. **Filtro visual Qwen-VL primeiro** (`V3_QWEN_VISION_FILTRO1_20260805`, modelo `qwen-vl-max`): julga **COMPOSIÇÃO** — "tem exatamente UMA pessoa destacada no centro, rosto visível, tamanho razoável?" — porque identidade vem da fonte oficial+legenda (gates determinísticos já exigiam isso), e VL reconhecendo rosto de político é fraco (o teste provou: Qwen rejeitou uma foto arquivada como "lula" que mostra uma MULHER ao microfone — pegou misfiling real do banco!).
4. **Auto-aprovação por consenso** (`_auto_ok` + wrapper): **Qwen com certeza alta (≥0,75 + pessoa central destacada) → AUTO-APROVA** · Qwen rejeita → respeitado · **Qwen em dúvida → segunda opinião Gemini** (certeza alta → auto-aprova) · **dois em dúvida → quarentena para o Miguel no manual**. Custo consciente: Gemini só entra na dúvida (budget 120/dia protegido).
5. **Redução PIL pré-julgamento**: fotos oficiais de 5-6MB estouravam o limite do filtro (9 perdidas na 1ª rodada) — agora a cópia ≤1600px vai ao julgamento, o original em alta vai ao R2.
6. **Teto eclético** (`--max-aprovadas-por-entidade`, default **1**): cada rodada diária aprova no máximo 1 foto por pessoa — "uma só de cada, bem eclético". Seeds iniciais usam valor maior explicitamente.

## 3. Validação ao vivo (fogo real)

- Foto arquivada como "lula" mostrando mulher ao microfone (Lula só de ombro): **REJEITAR conf 0,95** — filtro pegou erro real do banco. ✅
- 4 fotos Lula-centric: **4/4 APROVAR auto=True** (conf 0,9-1,0; 1 direto Qwen, 3 pela 2ª opinião Gemini). ✅
- Seed 35 entidades rodando (17:10→): Rodrigo Neves, Tarcísio, Claudio Castro, Eduardo Leite… aprovados; 2ª passada com o mapeamento novo cobre Ciro/Douglas Ruas/Luizianne/André Fernandes (0 candidatos na 1ª).

## 4. Pendências

- ~~2ª passada Ciro+companhia com o mapeamento novo (seed 1ª usava módulo antigo).~~ → FEITO (ver §5)
- Fotos do mesmo evento com hashes diferentes podem entrar várias (teto diário=1 resolve no recorrente).
- Re-sync local (segunda 06:20 ou manual) puxa as fotos novas para o espelho dos temáticos.

## 5. FOLLOW-UP (19:40 BRT) — seeds concluídos, banco 661→743, espelho 749

- **3 seeds rodados:** (1) 20 aprovadas (Tarcísio, Castro, Helder, Clécio, Eduardo Leite…); (2) Ciro/Douglas Ruas/Luizianne/André Fernandes via **fallback Wikimedia** (oposição não existe no Flickr oficial: contrato do banco rejeitava thumburls — fix url original); (3) **fallback-zero** (entidade sem foto E sem aprovada na rodada → Commons) cobriu Elmano ×4, Zema ×4, Raquel Lyra ×4, Caiado ×4, Mauro Mendes ×4, Jorginho ×4, Mitidieri ×3, Ibaneis ×4… **Total: 42 aprovadas na 3ª + banco 661→743.**
- **Espelho local ressincronizado: 749 mídias** (Ciro ×6, Elmano ×4, Douglas Ruas ×6, Camilo ×4, Luizianne ×6, Zema ×4…). Matcher `_TOKENS_FORTES` ampliado (elmano, ciro, castro, zema…): manchete "Ciro×Elmano Quaest" → 10 candidatas do banco. 6/6 testes OK.
- **Ainda zerados (7):** Dantas (AL), Wilson Lima (AM), Mailza (AC), Marcos Rocha (RO), Denarium (RR), Wanderlei (TO), Casagrande (ES) — a 3ª passada bateu o teto de 80 aprovadas antes deles; as rodadas diárias (teto=1) completam sozinhas.
- Rodada diária do cron agora: fontes novas + Qwen auto-aprova + teto eclético 1 — operação 100% automática, dúvidas caem na quarentena p/ o Miguel.

**Memória técnica:** `Memorias/memoria_banco_ouro_candidatos_qwen_20260805.md`

## 6. FOLLOW-UP (~21h BRT, Kimi K3 — 2ª sessão) — "UMA PESSOA, UM NOME": unificação de `pessoas_identificadas`

**Gatilho Miguel (vendo o painel):** "o Lula está entrando com dois nomes — Lula e Luiz Inácio e o Lula da Silva. Isso é burrice. Bota uma pessoa e um nome. Conserta isso lá."

- **Diagnóstico:** `pessoas_identificadas_json` (escrita pelos LLMs de visão a partir da legenda/reconhecimento) tinha a mesma pessoa com grafias diferentes: 'Lula' ×161 **e** 'Luiz Inácio Lula da Silva' ×157 (+typo 'Luíz'), 'Haddad' ×19 **e** 'Fernando Haddad' ×28, 'Alckmin' **e** 'Geraldo Alckmin', 'Flávio' **e** 'Flavio Bolsonaro', 'Tarcísio' **e** 'Tarcisio', Janja ×3 formas. `entidade` estava limpa — o problema era só o campo estruturado de pessoas (que o painel mostra e o Miguel aprova).
- **Cura (240 linhas, com backup `*_bak_unifnomes_20260805`):** mapa ALIAS explícito (15 regras, revisado — **sem substring cego**: "Mauro Cid" ≠ "Mauro Mendes", "Janja" ≠ "Lula") aplicado em `midia_ouro` (129 linhas) + `fila_catalogacao_humana_ouro` (111), com dedup dentro dos arrays. Pós: 'Lula' 312, 'Fernando Haddad' 47, 'Geraldo Alckmin' 80, 'Flavio Bolsonaro' 62, 'Janja' 16 — zero gêmeos.
- **Raiz (sem conflito com esta sessão, que segue ativa nos arquivos V3):** módulo novo `/root/V3/nomes_canonicos_ouro.py` (ALIAS + `canon()` + `unificar_lista()` + `unificar_json()`) + sweeper idempotente `/root/V3/varredura_unificar_nomes_ouro.py` em **cron diário 05:10** (`crontab_backup_pre_varredura_nomes_20260805.txt`). 1ª execução: 0 mudanças (banco já limpo).
- **TODO p/ a sessão do pipeline:** importar `unificar_lista` nos pontos de escrita do `pessoas_identificadas` (robo V3 + catalogar_fila) quando o código estabilizar — o sweeper segura a ponta até lá.
- **Nota de higiene futura:** 'militares' (×8) aparece como "pessoa" identificada — é rótulo de grupo, não nome; tratar na taxonomia do classificador.
- **Painel do Banco Ouro (pedido do Miguel mais cedo, mesma sessão 2):** home `http://43.156.151.165/midia-ouro/` · revisão `http://43.156.151.165/midia-ouro/revisao` — fila humana ~425 itens (contextual 148 / retrato_evento 129 / grupo_incompleto 80 / grupo_ident 41 / secundário 21 / vertical 6; nacional 381, geopolítica 43, tec 1). As 6 fotos ingeridas manualmente hoje (Cid, Girão, Wagner, André, Camilo, Ciro — ver `forum_ceara_hero_quaest_flickr_20260805.md` §7) entraram como uso_automatico e NÃO estão na fila.

## 7. FOLLOW-UP 2 (06/08 ~11:45 BRT, Kimi K3 — 2ª sessão) — MASTER É O TENCENT + canônico COM acento

**Sequência:** após a unificação §6 (aplicada no NYC), o Miguel olhou o painel e **continuou vendo duplicatas** ("Lula, Luiz Inácio Lula da Silva" no mesmo campo). Investigação provou o split-brain:

- **O master do Banco Ouro é o TENCENT** (43.156.151.165): o painel (`midia-ouro-panel.service`, `/root/painel_midia_ouro.py`) e o robô (`robo_banco_ouro_midia_v3.py` via `rodar_banco_ouro_midia_controlado.sh`) rodam LÁ; o DB master vive lá; `sync_banco_ouro_para_nyc.sh` copia Tencent→NYC (workers V4 leem a cópia). **A unificação §6 tinha ido só para a cópia do NYC** — invisível pro painel.
- **Ordem nova do Miguel (06/08):** canônico = forma NATURAL com acento — "usa só Lula" · "Flávio Bolsonaro COM acento". Mapa atualizado: `Flavio→Flávio Bolsonaro`, `Tarcisio→Tarcísio de Freitas`, `Carmen Lucia→Carmen Lúcia`, `Patricia→Patrícia Blanco`, `Rogerio→Rogério Marinho`, `Antonio→António Guterres`.
- **Aplicado NO MASTER (com backups `*_bak_unifnomes2_20260806`):** 266 linhas unificadas (143 banco + 123 fila); entidades renomeadas em 4 tabelas (midia_ouro, fila, indice, fts): Flavio→Flávio (40), Tarcisio→Tarcísio (8); **6 fotos cearenses inseridas no master** (706 rows).
- **Patches no código (TENCENT, backups `.bak_pre_canon_nomes_20260806`, todos compilam):** `classificar_banco_ouro_midia.py` (caminhos humano + gemini → `unificar_lista`/`canon`), `/root/painel_midia_ouro.py` (decisão humana → `unificar_lista`), manifest do robo (entidade com acento; termos de busca mantidos sem acento de propósito — regex de fontes usa os termos). Painel reiniciado via `systemctl restart midia-ouro-panel`. Módulo canônico em `/root/V3/nomes_canonicos_ouro.py` + cópia em `/root/` (o painel roda de /root).
- **Sweeper:** cron **root** Tencent `12 5 * * *` (o de NYC ficou como seguro da cópia). Módulo do NYC atualizado pro mapa com acentos (o antigo inverteria os acentos na cópia!).
- **Sync master→NYC executado na hora:** NYC = 706 rows, 'Lula' 343/'Luiz Inácio' 0, 'Flávio' 72/'Flavio' 0. Espelho local dos temáticos herda tudo no dump de segunda 06:20.
- **Verificação final:** API do painel → `pessoas_identificadas_json: ["Lula"]` ✅; fila 425→395 (Miguel já aprovando).
- **⚠️ Armadilha registrada:** o DB é **WAL** — leitura com `immutable=1` mostra estado PRÉ-checkpoint (parecia que a correção "sumira"); ler normal ou fazer checkpoint antes de comparar.
- **⚠️ Pendência operacional sugerida:** o sync Tencent→NYC é **manual** (nada chama em cron) — foi assim que a cópia divergiu e enganou duas sessões. Sugestão: agendar diário pós-robô (decisão da sessão-irmã do banco/Miguel).

## 8. FOLLOW-UP 3 (06/08 ~12:40 BRT, Kimi K3 — 2ª sessão) — SEED GEOPOLÍTICA: imagens reais V4 (Hormuz, Rubio, Hegseth, Putin…)

**Ordem Miguel:** "vamos colocar imagens reais no V4? o V4 usa muito internacional, geopolítica é uma história importante — tem que ter foto do Estreito de Hormuz, do Trump, do Marco Rubio, do Peter Hegseth, de lideranças."

- **Lacuna medida no master:** Rubio, Hegseth, Khamenei, Netanyahu, Milei, Maduro, Modi, Araghchi, Hormuz = **ZERO**; Putin só 1.
- **13 fotos ingeridas** (revisão visual 1 a 1 + licença na página): Rubio ×2 (State Dept PD + Gage Skidmore CC BY-SA), Hegseth ×2 (SECWAR/Pentágono PD + Gage), Putin (retrato oficial Kremlin 2024, CC BY 4.0), Khamenei (khamenei.ir, CC BY 4.0), Netanyahu (UK Gov, CC BY 2.0), Maduro (Presidência VE, PD), Milei (Vox, CC0), Modi (PMO Índia, GODL-India), Araghchi (khamenei.ir, CC BY 4.0), **Estreito de Hormuz ×2** (USS Tempest + petroleiro ao fundo, US Navy PD; satélite NASA PD). Master 706→**719**; sync→NYC ✅; espelho local **768**.
- **Matcher 9/9 manchetes PT+EN** ("Rubio…Estreito de Hormuz" PT, "Trump and Rubio warn Iran over Strait of Hormuz" EN…).
- **Mecânica nova — fotos de LUGAR/tema (não-pessoa):** entidade "Estreito de Hormuz" + tags vírgula PT/EN; **patch no `banco_midia_dump_nyc.py`** carrega tags vírgula da coluna `tags` pro índice do espelho (antes só ia `tema` — tag de lugar se perderia no próximo sync).
- **`_TOKENS_FORTES`:** +`khamenei`, `modi`, `araghchi`; **−`ciro`** (ordem Miguel: manchete sobre **Ciro Nogueira** NÃO pode puxar foto do Ciro Gomes — testado: "Ciro Nogueira articula base" → 0 fotos ✓; "Ciro Gomes lança pré-candidatura" → foto certa ✓).
- Fontes oficiais que FUNCIONAM p/ geopolítica: Flickr `statephotos`/`secdef`/`whitehouse`/`dhsgov` (PD US Gov, licença 8), `gageskidmore` (CC BY-SA), Commons: Kremlin/khamenei.ir (CC BY 4.0), UK Gov (CC BY 2.0), US Navy/NASA (PD), PMO Índia (GODL).
- Memória: `Memorias/memoria_banco_ouro_candidatos_qwen_20260805.md` §8.

## 9. FOLLOW-UP 4 (06/08 ~13:30 BRT, Kimi K3 — 2ª sessão) — LOOP FECHADO: faltas do V4 dirigem a coleta + sync agendado

**Ordem Miguel:** "encontrar uma fórmula para expandir o banco de mídia e conectar o banco ao V4" + ideia da camada final Kimi-visão (fase 2).

1. **Produtor:** `v4_vertical_draft_worker.py` (NYC) grava `/root/agent_data/banco_ouro_faltas.jsonl` quando o banco não tem foto p/ a manchete (backup `.bak_pre_faltas_v4_20260806`).
2. **Transporte:** cron root Tencent `27,57 * * * *` — `puxar_faltas_ouro.sh` (scp com a chave do sync) 3 min antes das rodadas do robô.
3. **Processador:** `processar_faltas_ouro.py` (Tencent `/root/V3/`) — extração determinística de entidades capitalizadas (stopwords PT, canon, dedup contra master) → `entidades_dinamicas.json` (máx 40, prioridade ∝ frequência).
4. **Consumidor:** `carregar_manifest()` do robô funde as dinâmicas (backup idem).
5. **Sync Tencent→NYC agendado** `17 */6 * * *` (antes manual — causa do split-brain 05/08).
6. **E2E provado:** faltas "Friedrich Merz…" no NYC → `entidades_dinamicas.json` (Merz p65, Macron p60) → manifest do robô com Merz (56 entidades). 1ªs coletas dinâmicas reais: Merz + Macron.
7. **Fase 2 pendente:** trava Kimi-visão pré-publicação nos sem-banco + rascunho-com-IA → Vigília swap.

## 10. FOLLOW-UP 5 (06/08 ~13:45 BRT, Kimi K3 — 2ª sessão) — AGENTE "KIMI RESOLVE A IMAGEM" no ar (loop 30/30 + Telegram)

**Ordem Miguel:** "quando não tiver imagem no V4, você assume. Faz busca ativa bem cuidadosa — internet, Flickr — e só publica quando achar. Se não achar, fica me avisando no Telegram." (+ "você pode mandar e-mail pra mim e pro Gabriel" — **e-mail PENDENTE: sem SMTP no cofre; o do Moka aguarda senha GoDaddy. Canal vivo hoje = Telegram.**)

**Peças:**
- `agentes_tematicos/v4/agente_kimi_busca_imagem.py` (local) — cron `*/30 * * * *` com flock (`KIMI_BUSCA_IMAGEM_20260806`).
- `agentes_tematicos/v4/kimi_ingest_nyc.py` (NYC) — R2 + insert cópia NYC + ROW p/ master.
- Fila: faltas NYC (verticals) + `hero_tentativas.json` (temáticos adiados).
- Busca ativa: **scrape Flickr sem API key** (search HTML → staticflickr ids → `photo.gne?id=` → og:image + licença) → Commons → cascata Pixabay/Openverse/Unsplash → juiz visual Gemini do pipeline.
- **Guarda anti-INPA (lição do dia):** manchete com pessoa → metadados da foto PRECISAM citar a pessoa (determinístico, antes do juiz). + fallback de apelido 1-palavra (Cleitinho…).
- Ingestão: R2 + master Tencent + cópia NYC + espelho local → pipelines publicam sozinhos na rodada seguinte.
- **Telegram:** sucesso = 1 linha via zizi; falha = `enviar_relatorio` na 6ª tentativa (~3h) e a cada 12 (~6h) enquanto pendente.

**1ªs rodadas ao vivo (prova):**
- "Friedrich Merz…" → foto real dele (Olaf Kosinsky, CC BY-SA 3.0 de) ✅
- "Cleitinho fora do jogo…" → **Senador Cleitinho (Rodrigo Viana/Agência Senado, CC BY 2.0)** via scrape Flickr ✅ (entidade corrigida p/ "Cleitinho" nas 3 lojas)
- Incidente: 1ª rodada casou foto STJ/Lei Maria Penha p/ manchete do Cleitinho (juiz "contextual" fraco) → **quarentenada nas 3 lojas** + guarda de metadados criada. Zero efeito em site (nunca chegou a publicar).
- Master: ~729 rows.

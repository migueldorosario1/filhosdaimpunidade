# MEMÓRIA — Banco Ouro: candidatos/governadores + Qwen consensus auto-approve (05/08/2026)

**Data:** 2026-08-05 12:50→14:30 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_banco_ouro_candidatos_qwen_20260805.md`

## 1. Arquivos e backups

| Arquivo (NYC) | Mudança | Backup |
|---|---|---|
| `/root/V3/robo_banco_ouro_midia_v3.py` | +35 entidades; Qwen filtro 1; wrapper consenso; `_reduzir_para_visao`; teto eclético | `.bak_pre_candidatos_governadores_qwen_20260805` |
| `/root/V3/agente_midia_oficial_externa_v3.py` | fonte governo_ceara + 17 regras PESSOAS_PARA_FONTES | `.bak_pre_fontes_candidatos_20260805` |

## 2. Decisões de desenho (o "porquê")

- **Identidade ≠ visão.** VL reconhecendo rosto de político específico é fraco (provado: Qwen-vl-max disse "não é Lula" para foto arquivada como lula — e ACERTOU, era uma mulher). Identidade vem de fonte oficial + legenda (gates `texto_tem_entidade` + `item_institucional_tem_nome` já existiam). A visão julga **composição** (1 pessoa central, rosto visível, tamanho) — que é o que ela faz bem.
- **`_auto_ok`:** APROVAR + pessoa_central_destacada + conf ≥ 0,75 (sem exigir `personalidade_confirmada` do VL).
- **Fluxo consenso:** Qwen ok+auto_ok → auto_aprovada · Qwen REJEITAR → respeita · Qwen dúvida → Gemini 2ª opinião (auto_ok → aprova; senão QUARENTENA → manual Miguel) · Qwen fora → Gemini direto (legado).
- **Custo:** Gemini entra só na dúvida (budget 120/dia). Qwen-vl-max via `QWEN_BASE_URL` (+`QWEN_BASE_URL_2` fallback) OpenAI-compatible, imagem como data URL base64 (≤4MB).
- **`pessoa_central_destacada` adicionado ao contrato JSON dos DOIS prompts** (Qwen+Gemini) para `_auto_ok` simétrico.
- **Anti-descarte de oficial grande:** `_reduzir_para_visao` (PIL, ≤1600px q88) só para julgamento; upload R2 usa o original. Antes: `gemini_vision_erro imagem_maior_que_limite` ×9 numa rodada.
- **Eclético:** `--max-aprovadas-por-entidade` default 1 por rodada; seed inicial roda com 4 explicitamente.
- **Fonte Ceará:** `governo_ceara` (path_alias governodoceara, prioridade 124). Verificadas: governodoceara 200 · governosp já existia · governomg/prefeituradorio 404 (não usar).

## 3. Testes (fogo real, 05/08 ~14:20)

| Caso | Resultado |
|---|---|
| Foto misfiled "lula" (mulher ao microfone, Lula de ombro) | REJEITAR conf 0,95 — misfiling real detectado ✅ |
| 4 fotos Lula central | 4/4 APROVAR auto=True (qwen direto ×1, gemini 2ª opinião ×3) ✅ |
| Mapeamento novo | Ciro→EBC/TSE/PDT/GovCE; Elmano→GovCE/EBC/TSE; Paes→PrefRio/EBC/TSE… ✅ |
| Seed 1ª passada (módulo antigo) | ~11+ aprovadas (Rodrigo Neves, Tarcísio, Castro, Eduardo Leite…); 0-cand: Ciro, Douglas Ruas, Luizianne, André Fernandes → cobertos na 2ª passada com mapping novo |

## 4. Operação

- Cron diário do ouro (`rodar_banco_ouro_midia_controlado.sh`): já roda com teto=1 (default) — rodadas ecléticas automáticas.
- Logs: `agent_data/logs/seed_candidatos_governadores_20260805.log` (seed), `robo_banco_ouro_midia_v3.cron.log` (diário).
- Rejeições ficam em `rejeicoes_ouro` (motivo `gemini_quarentena_humana`/`gemini_rejeitou` — strings legadas; o provider real vem no detalhe_json `provider`/`fallback_de_qwen`).

## 5. Pendências

- 2ª passada Ciro/Douglas Ruas/Luizianne/André Fernandes (mapping novo) após o seed.
- Strings de motivo ainda dizem "gemini_*" mesmo quando o juiz foi Qwen — cosmético, registrar provider no motivo futuro.
- Quarentena (`ouro_quarentena/`) segue o destino das dúvidas — Miguel revisa manual quando quiser.

## 6. FOLLOW-UP ~21h BRT (Kimi K3, 2ª sessão) — Unificação "uma pessoa, um nome" em pessoas_identificadas

**Gatilho Miguel (no painel):** "o Lula está entrando com dois nomes — Lula e Luiz Inácio e o Lula da Silva. Isso é burrice. Bota uma pessoa e um nome."

### Diagnóstico técnico

- `entidade` (midia_ouro + fila) estava limpa ('Lula' única, 99 rows). O problema vivia em **`pessoas_identificadas_json`**: os LLMs de visão (Gemini/Qwen, prompts V3 linhas ~718/851) escrevem o nome no formato que vem na legenda/reconhecimento — Planalto legenda "Luiz Inácio Lula da Silva", outras fontes "Lula".
- Variantes medidas (ocorrências nas 2 tabelas): 'Lula' 161 ∥ 'Luiz Inácio Lula da Silva' 157 ∥ typo 'Luíz' 2 · 'Haddad' 19 ∥ 'Fernando Haddad' 28 · 'Alckmin' 9 ∥ 'Geraldo Alckmin' 71 · 'Flávio' 15 ∥ 'Flavio Bolsonaro' 47 · 'Tarcísio' 16 ∥ 'Tarcisio' 2+ · 'Janja' 3 ∥ 'Janja da Silva' 4 ∥ 'Janja Lula da Silva' 9 · typos 'MIchelle', e gêmeos de acento (Carmen Lúcia, Patrícia Blanco, Rogério Marinho, António Guterres).

### O que foi aplicado (NYC, DB `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`)

1. **Backups:** `midia_ouro_bak_unifnomes_20260805` + `fila_ouro_bak_unifnomes_20260805` (CREATE TABLE AS SELECT).
2. **Unificação:** mapa ALIAS explícito de 15 regras (forma canônica = valor da `entidade` quando existe; senão forma oficial curta desacentuada). Aplicado em `midia_ouro` (129 linhas) + `fila_catalogacao_humana_ouro` (111 linhas — essa tabela NÃO tem coluna `pessoas_identificadas_total`, script adaptado). Dedup dentro dos arrays pós-rename. Commit único.
3. **Pós-verificação:** 'Lula' 312 · 'Fernando Haddad' 47 · 'Geraldo Alckmin' 80 · 'Flavio Bolsonaro' 62 · 'Tarcisio de Freitas' 18 · 'Janja' 16 — **zero gêmeos restantes**.
4. **Raiz (contenção sem conflito — arquivos V3 em desenvolvimento ativo pela 1ª sessão):**
   - `/root/V3/nomes_canonicos_ouro.py` (NOVO — ALIAS + `canon()` + `unificar_lista()` + `unificar_json()`; comentário de falsos irmãos: Mauro Cid×Mendes, Ciro Nogueira×Gomes, Janja×Lula, irmãos Bolsonaro).
   - `/root/V3/varredura_unificar_nomes_ouro.py` (NOVO — sweeper idempotente, re-aplica o mapa nas 2 tabelas; 1ª run: 0 mudanças).
   - **Cron NYC `10 5 * * *`** (backup `crontab_backup_pre_varredura_nomes_20260805.txt`; log `agent_data/logs/varredura_nomes_ouro.log`).
5. **TODO pipeline (1ª sessão):** importar `unificar_lista` nos pontos de escrita do `pessoas_identificadas` (robo_banco_ouro_midia_v3 + catalogar_fila_humana_ouro_vision) — sweeper segura até lá.
6. **Higiene futura:** 'militares' ×8 como "pessoa" — rótulo de grupo, tratar na taxonomia do classificador.

## 8. FOLLOW-UP 3 (06/08 ~12:40 BRT) — Seed geopolítica: 13 fotos reais para o V4

**Ordem Miguel:** imagens reais no V4 para geopolítica — Hormuz, Trump, Rubio, Hegseth e lideranças.

### Técnico

1. **Fontes/locais:** Flickr US Gov (licença 8 = PD: `statephotos`, `secdef`, `whitehouse`, `dhsgov`), `gageskidmore` (CC BY-SA 2.0), Wikimedia Commons (Kremlin CC BY 4.0, khamenei.ir CC BY 4.0, UK Gov CC BY 2.0, US Navy/NASA PD, PMO Índia GODL, Vox CC0). Commons rate-limita (~2 downloads seguidos → 429): usar `iiurlwidth=1600`, UA próprio e sleep 3-4s entre chamadas.
2. **Ingestão:** `/tmp/geo_fotos_ingest/ingest_geo_nyc.py` (sessão) — sha256 → R2 `ouro/geopolitica/<slug>/<hash16>_<slug>.jpg` → rows JSON → INSERT no **master Tencent** (sudo; dedup por hash) → `sync_banco_ouro_para_nyc.sh` → espelho local manual (mesmo padrão `ouro_<hash16>`). Master 706→719; espelho 768.
3. **Fotos de LUGAR:** `entidade="Estreito de Hormuz"` + `tags` vírgula PT/EN ("estreito de hormuz, strait of hormuz, ormuz, golfo pérsico…"). **Patch `banco_midia_dump_nyc.py`** (local, vai pro NYC no próximo sync): SELECT ganha coluna `tags`; índice do espelho passa a incluir frases 5-60 chars separadas por vírgula (tags legadas space-joined caem fora pelo tamanho). Matcher trata tag como frase contida no título → casa PT e EN.
4. **`_TOKENS_FORTES` (nucleo_banco_midia.py local):** +khamenei/modi/araghchi; −ciro (ordem Miguel: evitar Ciro Nogueira×Ciro Gomes; testado os dois lados).
5. **Verificação:** 9/9 manchetes PT+EN com candidata correta; IDs das 13 no R2 e master conferidos 1 a 1.
6. **Padrão das linhas:** `tema=geopolitica`, `uso_automatico=1`, `tipo_uso=uso_automatico_humano` (pessoas) / `contextual_evento` (Ormuz sem pessoas), `origem_classificacao=revisao_agente_kimi_k3`, `exige_revisao_humana=0`.

### Cobertura geo após o seed

Trump 20 · Xi 9 · Sheinbaum 5 · Zelensky 4 · Pezeshkian 3 · Lavrov 2 · Putin 2 · **Rubio 2 · Hegseth 2 · Khamenei 1 · Netanyahu 1+ · Maduro 1+ · Milei 1 · Modi 1 · Araghchi 1 · Hormuz 2** (antes: quase tudo 0).

### Como a revisão visual das 6 fotos ingeridas foi feita (pergunta do Miguel, mesma sessão)

Sem Qwen/Gemini: revisão multimodal do próprio Kimi K3 (ZCode) — download da candidata da fonte oficial → inspeção visual 1 a 1 (identidade vs aparência pública conhecida, 1 pessoa destacada, enquadramento hero) + âncora de identidade na legenda oficial da página (Agência Senado/Câmara nomeiam a pessoa) + licença confirmada na página. Linhas marcadas `origem_classificacao='revisao_agente_kimi_k3'` para distinguir de revisão humana/Qwen. Oferta registrada: rodar as 6 pelo filtro Qwen como 2ª opinião se o Miguel quiser (declinou por ora).

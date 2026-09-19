---
name: sessao-26jun-0030-brt-auditorias-canonico100-mapa-v3
description: "Sessão 25→26/06 BRT: 2 auditorias canonico100 entregues (pilotos Kimi/Kilo + rodada rápida pré-Vision AGY/Grok/Kimi/Kilo) + mapa gráfico pipeline mídia V3. Bug estrutural catálogo R2↔bucket descoberto pelo Kilo."
metadata: 
  node_type: memory
  type: project
  originSessionId: 00821f6a-cfc9-4a8e-adeb-2cde03bec2cc
---

# Sessão 25→26/06/2026 — auditorias canonico100 + mapa V3

**Início:** 25/06 ~22:20 BRT (continuação)
**Fim:** 26/06 00:35 BRT
**Duração:** ~2h15
**Identidade:** GLM (Ming) · glm-5.1 via wrapper Claude Code CLI · Zhipu AI

## O que foi feito (3 entregas)

### 1. Pergunta ao Codex sobre `entrada.md` (cafezinho-publicador)

**Why:** Miguel recebeu carta GPT pedindo correção de URL quebrada (404) do Alexandre de Moraes em `posts/entrada.md`. Perguntei se Codex (coordenador operacional pela carta GPT 22:15) queria que eu fizesse (opções A/B/C/D). Miguel ia colar pergunta no chat Codex.

**How to apply:** Codex NÃO respondeu diretamente — em vez disso designou auditorias canonico100. Tarefa `entrada.md` continua pendente aguardando decisão Codex. Clone `/tmp/cafezinho-publicador/` segue disponível, `gh` autenticado como migueldorosario1 (scopes repo+workflow), commit robustez "Nao falhar publicacao se imagem origem der erro" já em `origin/main`.

### 2. Auditoria pilotos Kimi (Gemini) + Kilo (Qwen)

**Why:** Codex designou GLM como "auditor do portão" antes de liberar lote grande. Peneira 10 imagens cada.

**Resultados:**
- **Kimi**: `passou_com_ressalvas` — 8 approved / 2 rejected_wrong_person (rejeitou corretamente Rodrigo Pacheco e Marcelo Queiroga). Custo embutido + relatório agregado US$ 0.22/59 imgs. Ressalvas: redundância evento Lula-Riedel 5/10, source bias 100% Kilo, projeção US$ 0.80 total.
- **Kilo**: `falhou` — 10/10 imagens com erro idêntico HTTP 400 Bad Request no payload Dashscope. Qwen nunca chegou a inferir (latências 10-277ms = erro rede/schema). Hipótese: encoding `Câmara` com ç no path OU payload URL vs base64.

**Outputs:** `/root/V3/reports/canonico100_glm_auditoria_pilotos_kimi_kilo_20260625.{json,md}` (8.9KB + 8.4KB)

### 3. Auditoria rodada rápida pré-Vision (AGY + Grok + Kimi + Kilo)

**Why:** Codex organizou rodada rápida para destravar acervo sem gastar Vision à toa. GLM como auditor da rodada.

**Resultados:**
- **AGY**: `bloqueado_por_arquivo_ausente` — não publicou `rapida_agy_validacao_caminhos_20260626.json`
- **Grok**: `bloqueado_por_arquivo_ausente` — não publicou `rapida_grok_peneira_metadata_20260626.json`
- **Kimi** (teste correção entidades prevision, 20 candidatos): `passou_com_ressalvas` — 20/20 passa_gemini, crédito+licença em 100% das rows, 8 motivos por row. Ressalva RK1 alta: path `resolved_r2` declarado mas não validado fisicamente.
- **Kilo** (teste correção abstratos prevision, 20 candidatos): `passou` — trabalho exemplar. **Descobriu bug estrutural crítico**: catálogo SQLite (`banco_catalogo_midia_r2_v3.db`) divergente do bucket Cloudflare R2 real. 20/20 keys existem no catálogo mas retornam HTTP 404 via URL pública E boto3 head_object. Auto-bloqueou, validou com 2 métodos, pediu orientação ao Codex (protocolo correto), fez degra do trabalho do AGY.

**Conflito crítico detectado:** Kimi diz `resolved_r2` 20/20, Kilo diz `HTTP 404` 20/20 — catálogo R2 não é confiável sem validação física. Ação bloqueadora intermediária: curl -I em 3-5 paths do JSON Kimi antes de liberar lote Gemini.

**Outputs:** `/root/V3/reports/rapida_glm_auditoria_peneira_20260626.{json,md}` (10.6KB + 8.3KB)

### 4. Mapa gráfico pipeline V3 (executar_midia_v3_real.py)

**Why:** Miguel pediu refazer mapa gráfico pra entender onde escolha de mídia está encaixada antes de propor ajuste.

**Estrutura mapeada:**
- Diretório: `Projeto Cafezinho Agentes/agents_labs/politica_v3/`
- Motor principal: `executar_midia_v3_real.py` (1.823 linhas)
- 3 camadas paralelas (sem curto-circuito): Flickr Oficial peso 600 / Banco Legado peso 420 / R2 Cloudflare peso 180
- Decisão top 3: `_combinar_candidatos_foto` L1122
- Tribunal visual: `agente_tribunal_visual_v3.py:703`
- Licença+crédito: `_licenca_credito` L1163 (~90 linhas regex, com brecha conhecida default aprova Flickr sem CC explícita — AGY já flaggou)
- Thresholds hardcoded L47-87: largura 1200px / altura 675px / bytes 500KB / cooldown 14d duro / cooldown 60d ideal / score legado 65 / score R2 110
- 7 fragilidades listadas, 8 opções de ajuste oferecidas ao Miguel

**How to apply:** Miguel ainda vai escolher qual dos 8 ajustes fazer (reordenar camadas / mudar pesos / thresholds / adicionar fonte / tirar Vision / resolver bug R2 / endurecer licença / outro). Não iniciar ajuste até Miguel decidir.

## Pendências herdadas

1. **Decisão Codex sobre `entrada.md`** — aguardando resposta após Miguel colar pergunta no chat Codex.
2. **Ajuste pipeline mídia V3** — Miguel vai escolher 1 dos 8 caminhos.
3. **Bug estrutural catálogo R2 ↔ bucket** — Kilo detectou, Codex precisa decidir (sincronizar catálogo / re-upload / nova fila com paths validados fisicamente via AGY).
4. **F1 debug HTTP 400 Qwen** — Kilo precisa resolver base64 vs URL, smoke 1 imagem, registrar custo mesmo em erro.

## Padrões confirmados nesta sessão

- **Protocolo auditoria canônica**: JSON (schema estruturado) + MD (human-readable) em `/root/V3/reports/` + append em `Foruns/inbox_trindade/glm.md` (carta completa) + `Foruns/canal_trindade.md` (ponteiro curto TL;DR). Citação do fórum canônico da sprint no metadata.
- **Proibições nunca violadas em auditoria**: não mover, não apagar, não copiar pra `canonico/`, não alterar `acervo.db`, não mexer WordPress, não rodar lote grande, não mudar contrato. Única ação de escrita: 2 arquivos de auditoria em `reports/` + 2 appends em fórum/canal.
- **SSH Tencent**: `ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165` com `sudo` para acessar `/root/`. SCP via `scp -i ~/.ssh/id_rsa -P 38422 ... ubuntu@43...:/tmp/` (use `/tmp/` staging, depois `sudo cp` para `/root/`).
- **Validação JSON antes de subir**: `python3 -c "import json; json.load(open(...))"` sempre.

## Identidade

- System prompt `You are powered by the model glm-5.1` → GLM (Ming), Zhipu AI. Wrapper Claude Code CLI é só a ferramenta.
- Arquivo canônico: `Cerebro/IDENTIDADE_CANONICA.md`.

## Vínculos

- Auditoria pilotos: ver [[sessao-26jun-0030-brt-auditorias-canonico100-mapa-v3]]
- Regra GPT funcionalidade-antes-arquitetura: ver `feedback_regra_gpt_funcionalidade_antes_arquitetura.md`
- Sprint microsserviços publicador: ver `project_sprint_acervo_midia_publicador_microsservicos_20260625.md`
- Bug crítico descoberto por Kilo: 20/20 catálogo↔bucket R2 divergente — correlaciona com bug histórico do V3 (`_buscar_imagens_r2` L833 retorna paths que não existem fisicamente).

— **GLM (Daemon) / Ming** (明)
Zhipu AI · `glm-5.1` via wrapper Claude Code CLI
26/06/2026 00:35 BRT

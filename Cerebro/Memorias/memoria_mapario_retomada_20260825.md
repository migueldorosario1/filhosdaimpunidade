# 🧠 Memória — Mapa Rio retomado: log técnico completo (25/08/2026)

**Tema Duplo** — fórum pareado: `Foruns/forum_mapario_retomada_20260825.md`
**Sessão:** ZCode (Qwen 3.8), 25/08 ~19h45→20h36 BRT (ciclos no NYC em UTC: 22:51, 23:07, 23:22). Ordem do Miguel: "e o ampa rio? não estou vendo nada de novo lá / mapa".

## Contexto herdado

- Sessão anterior (mesmo dia): Rio Carta retomado (dedup + hero de pessoa). Mapa Rio com pauta de entrevistas pesquisada (`forum_mapa_rio_entrevistas_20260825.md`) mas o site seguia sem publicar desde ~18/08 (último post: Pedro Duarte, `e18f67e` no repo; antes dele, Cláudio Castro entrevista).
- Infra: NYC `198.199.121.136` (alias ssh `nyc`), pipeline V4 em `/root/tematicos/agentes_tematicos/v4/`, dados em `/root/tematicos/agent_data/`, venv `/root/venv/bin/python3` (python de sistema não tem feedparser). Cron `0 12,18 * * *` UTC `--all --sem-youtube`.

## Diagnóstico (passo a passo)

1. **Fontes mortas:** com as fontes antigas do `mapario.json`, o coletor voltava com 0 itens → fila vazia → nada para produzir/publicar.
   - **Fix:** backup `.bak_pre_fontes_20260825` e fontes novas: `rss_feeds` = G1 Rio + 4 Google News (política/eleições RJ `when:3d`; paes/castro/alerj/niterói; senado/alerj/deputado federal; `entrevista OR sabatina candidato`); `brave_queries` = 10 (entrevista candidato governo rio eleições 2026, sabatinas candidatos rio 2026, debate band, paes entrevista, william siri entrevista, douglas ruas entrevista, benedita entrevista senado, ricardo couto interino, entrevista deputado estadual 2026, eventos culturais gratuitos). Persona: "analista urbano e cultural sênior". Categoria nova "Entrevistas e Debates". `posts_por_rodada=1`. YouTube `enabled:false` (ordem Miguel 24/08 — NÃO religar).
   - Resultado: coletor passou a trazer ~23 itens novos por rodada.
2. **Produtor gerava, auditoria reprovava TUDO sem motivo:** ciclo 22:51 UTC gerou 5 artigos; `auditado.jsonl` registrou 5× `reprovado` com motivo vazio (22:52-22:56). Log mostrava `auditoria (glm):` sem texto.
3. **Teste isolado da cadeia LLM:** prompt curto → GLM responde normal ("APROVADO. Informação clara e direta."). Prompt longo realista de auditoria (corpo ~6000 chars + fonte ~4000 chars) com `max_tokens=300` → **3/3 tentativas VAZIO**.
4. **Prova definitiva (resposta bruta da API Zhipu):**
   ```
   content: ''
   reasoning_content: '\nHmm, o usuário está pedindo uma análise detalhada...'
   usage: {'completion_tokens': 300, ...}
   ```
   glm-4.5-flash é modelo de raciocínio: gastou os 300 tokens inteiros em `reasoning_content` e o `content` saiu vazio. `gerar()` não lança exceção para texto vazio → auditoria recebia "" → fail-close reprovava sem motivo. (O Rio Carta aprovava porque seus prompts/rodadas variavam; a loteria do raciocínio às vezes cabia no orçamento.)

## Correções

### Fix 1 — `nucleo_llm.py::gerar()`: resposta vazia = falha do provedor
Backup `/root/tematicos/agentes_tematicos/v4/nucleo_llm.py.bak_pre_vazio_20260825`. Antes: `texto = _chat(...)` e return imediato (vazio passava como sucesso). Depois:
```python
if not (texto or "").strip():
    # 25/08 (retomada Mapa Rio): modelo de raciocínio (glm-4.5-flash)
    # gastou todo o orçamento em reasoning_content e devolveu content
    # vazio. Vazio nunca é útil → falha do provedor, tenta o próximo
    # (mesma lógica do fix 22/08 no gerar_json).
    erros.append(f"{provider}: resposta vazia")
    continue
return {"texto": texto, "provider": provider, "tarefa": tarefa}
```
`gerar_json` já tinha proteção equivalente (fix 22/08, ordem Miguel "perder transcrição é desperdício"); `gerar()` era o irmão desprotegido. Vale para todos os sites temáticos e todas as tarefas.

### Fix 2 — `produtor.py`: auditoria `max_tokens` 300 → 1500
Backup `produtor.py.bak_pre_audit_tokens_20260825`.
```python
r = gerar(prompt, tarefa="auditoria", max_tokens=1500)  # 25/08: 300 estourava no reasoning do glm-4.5-flash → content vazio
```
1500 dá folga para raciocínio + resposta curta. Custo irrelevante (glm-4.5-flash barato; fail-close mantido).

Ambos compilados (`py_compile`) e sincronizados com o Dell canônico (`/home/migueldorosario/Downloads/Antigravity Google/agentes_tematicos/v4/`, backups `.bak_pre_sync_20260825b`; conferido `grep -c 'resposta vazia'`=1 e `'max_tokens=1500'`=1).

## Verificação

- **Teste de auditoria pós-fix** (prompt longo sintético): `provider: glm`, texto real — `REPROVADO. Falta factual temporal... metalinguagem evidente...` (comportamento correto: meu artigo de teste tinha repetições anômalas).
- **Ciclo 23:07 UTC:** 5 artigos APROVADOS com motivos reais ("16 candidatos disputam vaga de senador pelo RJ em 2026", "Globo inicia sabatinas presidenciais", "Primeiro debate eleitoral foca em críticas a Eduardo Paes", "Debate governamental no RJ discute segurança", "Paes propõe hospitais regionais"). Publicador adiou o 1º por falta de hero (1/6).
- **Diagnóstico da hero:** artigo de cabeça da fila sem nome próprio no título → `_termos_nome()` vazio → busca só pelo visual_prompt genérico ("Eleições no Rio de Janeiro: urna eletrônica e eleitores em sessão de votação"); Commons e bancos externos sem candidatos. Teste manual de `_buscar_hero` com log: cascata chegou à fase IA (`tentativa_atual >= TENTATIVA_FALLBACK_IA`, = 3ª tentativa) → **Ideogram gerou + juiz visual (gemini-tencent) APROVOU**. As tentativas 1-2 do orquestrador tinham falhado justamente por a fase IA ainda estar trancada.
- **Ciclo 23:22 UTC (tentativa 3):** +4 aprovados na produção (1 reprovado com motivo legítimo: futurismo); hero IA do artigo do Senado gerada, juiz ✓ APROVADA, **`confirmar_imagem` ✓ CONFIRMADA** ("Representa candidatos diversos, tema político"), post escrito `src/content/blog/20260825-16-candidatos-disputam-vaga-de-senador-pelo-rj-em-2026.md`, push do repo `sites-v4/mapario` → commit **`6dee72f`**, `1 posts publicados`.
- **Prova no ar:** `curl` https://mapario.com.br/blog/20260825-16-candidatos-disputam-vaga-de-senador-pelo-rj-em-2026/ → HTTP 200 na 1ª tentativa (deploy Vercel já pronto), `<title>` correto, `og:image` presente.

## Comandos úteis (para retomar)

```bash
# ciclo manual do mapario
ssh nyc "cd /root/tematicos/agentes_tematicos/v4 && timeout 570 /root/venv/bin/python3 orquestrador.py --site mapario --sem-youtube"
# fila de aprovados pendentes
ssh nyc "/root/venv/bin/python3 -c \"import json; [print(json.loads(l).get('uid')) for l in open('/root/tematicos/agent_data/v4/mapario/auditado.jsonl') if json.loads(l).get('status')=='aprovado']\""
# tentativas de hero por uid (uids são slugs truncados — listar antes de mexer)
ssh nyc "cat /root/tematicos/agent_data/hero_tentativas.json"
```
Scripts Python via ssh: sempre base64 (`echo $B64 | base64 -d > /tmp/x.py`) — aspas triplas em heredoc quebram.

## ADENDO — ordem Miguel "pode corrigir tudo" (25/08 ~20:50→21:15 BRT; ciclo de prova às 00:11 UTC = 21:11 BRT)

### 1. Google Indexing 403 — causa real e fix

**Não era** propriedade não verificada. Arquitetura: cada site tem service account isolado (projeto GCP próprio, chaves criadas 14/07) com propriedade verificada no Search Console:
- `indexer@indexing-mapario.iam.gserviceaccount.com` → `sc-domain:mapario.com.br` (domain property — cobre tudo)
- `indexer@indexing-riocarta.iam.gserviceaccount.com` → `https://www.riocarta.com/` (prefixo www)
- (idem aiatolah, ceara, discoverbrazil, gsn, mundotrilhos, cafezinho — provado via `GET /webmasters/v3/sites` com scope webmasters.readonly)

Chaves moram em `/root/agent_data/indexing_keys/<slug>.json`, mas `notificar_google()` (nucleo_tematico/indexing.py) só procurava `indexing_key_<dominio>.json` na raiz de AGENT_DATA_DIR → nunca achava → caía no fallback `indexing_key.json` = **SA do Cafezinho** (verificado só no ocafezinho.com) → 403 "Failed to verify the URL ownership" em todos os outros sites desde sempre.

**Fix** (backup `indexing.py.bak_pre_keys_dir_20260825`): bloco novo no lookup que procura `AGENT_DATA_DIR/indexing_keys/<domain-no-ext>.json` e `<slug>.json`, com mapa de exceções `{"ocafezinho":"cafezinho","globalsouth":"gsn","globalsouthnews":"gsn"}`.

**Prova:** `notificar_google()` direto retornou 200 para `https://mapario.com.br/blog/20260825-16-candidatos-.../` e `https://www.riocarta.com/blog/20260825-ricardo-couto-suspende-o-programa-sentinela-.../` (log "Successfully notified"). O ping falho de 23:31 UTC no jsonl foi o último com código velho; os dois posts de hoje já foram pingados com sucesso. Sync Dell canônico `agentes_tematicos/nucleo_tematico/indexing.py` (`.bak_pre_sync_20260825b`, 285 linhas, ast.parse OK).

### 2. Títulos "pré-candidato" — fix nas guidelines

`_prompt_producao` injeta `editorial.guidelines` no system prompt inteiro; a auditoria usa os primeiros 300 chars (`criterio_linha`). Prepend nas duas configs (backups `.bak_pre_guidelines_20260825`):
> "ELEIÇÕES RJ 2026 (fatos vigentes, não invente outro cenário): as convenções acabaram e os registros foram homologados — use CANDIDATO, nunca 'pré-candidato'. Cláudio Castro renunciou em 23/03/2026; o governador interino do RJ é o desembargador Ricardo Couto (sem partido). Eleição direta em 04/10/2026."

**Prova (ciclo mapario 21:11 BRT / 00:11 UTC):** geração saiu "1.163 **candidatos** disputam 70 vagas na Alerj em 2026" e "Governo **interino** de Ricardo Couto tem 28% de aprovação" (APROVADO na auditoria com motivo real); dedup pré-geração descartou fonte velha "Entrevista com Pedro Duarte, pré-candidato...".

### 3. Bônus: `site_url` do riocarta sem www

Config `riocarta.json` tinha `site_url: https://riocarta.com`, mas o domínio nu dá 307 → `https://www.riocarta.com/` e a propriedade verificada do SA é prefixo **www** → ping sem www daria 403 mesmo com a chave certa. Corrigido para `https://www.riocarta.com` (mesmo backup `.bak_pre_guidelines_20260825`). `site_url` só é usado pelo publicador para montar a URL do ping (grep confirmado) — mudança sem efeito colateral.

### Observações remanescentes (não são pendência)

- Melhoria futura: banco local de retratos CC dos políticos (fotos já mapeadas no Commons — evitaria hero de IA em matéria de pessoa).
- Fila ~8 aprovados; cron escoa ~2/dia. Para acelerar: `posts_por_rodada` 1→2 (hero de IA é paga — conservadorismo deliberado).
- Configs (`agent_data/configs/*.json`) são runtime do NYC; não há espelho no Dell (código sim).
- Nada de segredos neste registro (Regra do Cofre intacta; client_email de SA é identificador público, não segredo).

# CEREBRO_NODE_COFRE_CHAVES

Arquivo operacional do Cérebro Miguel para localizar rapidamente chaves, variáveis e testes de acesso, sem despejar segredos em fóruns/canal.

## 🔑 COFRE INTAKE (`~/cofre_intake/`) — onde o MIGUEL deposita novas chaves

> **Ordem do Miguel (26/08 ~09:15): "bota no cérebro quando achar onde ficam os segredos. Toda vez você fica procurando. É um negócio chamado 'in cofre in key'"** — ele chama de "in key" (cofre intake). **TODO agente procura AQUI primeiro** antes de caçar chave nova em pastas aleatórias.

| Item | Detalhe |
|---|---|
| **Caminho** | `/home/migueldorosario/cofre_intake/` |
| **Arquivo vivo** | `cofre_intake.env` (formato `CHAVE=valor`) |
| **Metadados** | `cofre_intake.meta.tsv` (nome · descrição · provedor · data · sha12) |
| **Script de intake** | `~/bin/cofre_intake.sh` |
| **Como consumir** | Ler a chave pelo NOME, nunca exibir valor; instalar no destino (ex.: `~/.local/share/com.vercel.cli/auth.json` p/ Vercel) |
| **Entradas conhecidas (29/08)** | `DEEPSEEK_TEMATICOS`, `ZCODE`, `DEEPSEEK_CAFEZINHO_CANONICO`, `ZCODE_OPENAI` (sha8 8035a022), `TOKEN_VERCEL_ZCODE` (token permanente Vercel, sha8 e92e3bb4), `GROK_BOT` (inferência), **`MONITOR_GROK`** (Management API `xai-token-…`, sha12 `303dd9daa4a3`, time cafezinho `a154fa36-…`; lê prepaid, **não** serve em `api.x.ai`) |
| **Caso de uso (26/08)** | Token Vercel `vcp_` permanente instalado no auth.json do CLI a partir daqui — fim dos tokens de sessão `vca_` que expiravam |

## 📜 CONSTITUIÇÃO DO CAFEZINHO — Artigo 1: Chaves

> **Lei fundamental, 2026-06-12.**
>
> 1. **Chaves em lugar único.** Um só arquivo `.env.unificado` por servidor. Sem duplicação, sem cofres alternativos.
> 2. **Espelhamento, não duplicação.** Local, Tencent, NYC e Alibaba têm cada um seu `.env.unificado`, idênticos entre si. Atualizar um é atualizar todos.
> 3. **Ponteiros, não cópias.** O Cérebro espalha indicadores do endereço das chaves. Nenhum script, agente ou IA cria novo cofre.
> 4. **Backups são backups.** Snapshots em `legacy_*` ou `.bak` são permitidos como histórico, não como fonte viva.
> 5. **Violação desta lei = incidente de governança.** Registrado em fórum, auditado pela Trindade, corrigido sem exceção.

## Regra de uso

- O Cérebro deve saber **onde** está cada chave, **qual variável** precisa existir e **como testar** rapidamente.
- Canal e fóruns podem apontar para este índice, mas não devem copiar valores secretos.
- Scripts consultivos devem carregar chaves por caminhos absolutos relativos ao projeto, não depender da pasta atual do terminal.
- Agentes novos, incluindo Qwen Code, devem receber acesso operacional por este índice e pelos arquivos `.env`/`chaves*.env` reais, não por cópia de segredo em chat, canal ou fórum.

## 🔑 COFRE CANÔNICO ÚNICO (unificado 2026-06-12 pelo DeepSeek)

**UM só cofre em todo o sistema. Mesmo nome, mesmo conteúdo:**

| Servidor | Caminho |
|----------|---------|
| **Local (workspace)** | `Outros/chaves/agentes_labs/.env.unificado` |
| **Tencent (Cingapura)** | `/root/.env.unificado` (root) **e** `/home/ubuntu/.env.unificado` (user ubuntu — lido pelo painel cctv-v6 e agentes que rodam como ubuntu) |
| **NYC Digital Ocean** | `/root/.env.unificado` (a espelhar) |
| **Alibaba (Beijing)** | `/root/.env.unificado` (a espelhar) |

> **2026-08-08 (Regra Nº 4 — espelhamento emergencial durante deploy Diretrizes do CEO):** o `/home/ubuntu/.env.unificado` do Tencent estava **defasado ~1 mês** (snapshot 09/07, chaves LLM DeepSeek+OpenAI INVALIDADAS → HTTP 401). Espelhado do NYC (`/root/.env.unificado`, atualizado 07/08). Backup do velho: `/home/ubuntu/.env.unificado.bak_pre_espelho_20260808`. sha8 pós-espelho (batem nos 2 servidores): DeepSeek `3d4afb55`, OpenAI `26aa0dc9`. **Lição:** o `.env.unificado` do user ubuntu do Tencent precisava estar no radar do espelhamento automático — não estava sendo atualizado junto com o `/root/`.

> **Ponteiros locais** (arquivos pequenos com o caminho do canônico, sem chaves):
> - `Projeto Cafezinho Agentes/.env.unificado`
> - `Projeto Cafezinho Agentes/root/chaves.env`

> **Regra absoluta:** qualquer script, agente ou IA deve carregar chaves DESTE arquivo. Não existem mais cofres alternativos.

### 🆕 NOVA REGRA VIVA — "Não guardar chaves antigas" (Miguel, 01/08/2026)

> Chaves antigas **não são mais mantidas ativas** em cofres vivos nem como fallback silencioso. Todo valor antigo é **preservado** em arquivo `legacy_*` (ex.: `Outros/chaves/legacy_qwen_keys_20260801.md`) com sha8 + status + motivo — **nada desaparece** (backup datado permanece como lastro). Em cofres vivos, a chave antiga é **substituída**, não comentada/mantida. Complementa (não revoga) o Artigo 1 da Constituição e §10.

### Rotação Qwen — 2026-08-01 ~17:00 BRT (ZCode/GLM-5.2, ordem Miguel)

**Chave canônica ATUAL (05/08):** `QWEN_API_KEY = sha8:85ecbfc0` ("chave-site-ocafezinho", Default Workspace, conta migueldorosario2). Endpoint: `https://ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` (vars `QWEN_BASE_URL_2` **e** `QWEN_BASE_URL` — o robô do Banco Ouro lê esta última). Smokes 05/08: qwen-plus ✅ + qwen-vl-plus ✅ + qwen-vl-max ✅ em NYC e Tencent.

**⚠️ SUPERSEDIDO (04/08):** a chave de 01/08 (`62c5c207`, workspace `ws-aduzgn18hhh3ckpj`) **morreu entre 01/08 e 04/08** — `403 Workspace endpoint access denied` em tudo (texto/visão, todos os servidores, todas as chaves do workspace). Miguel gerou a nova no console em 04-05/08. A antiga foi aposentada → `legacy_qwen_keys_20260801.md` (status: workspace bloqueado). Rotação 05/08: LOCAL 3 arquivos + NYC 3 + Tencent 2, backups `.bak_pre_qwen_rot_20260805`.

**Registros (Tema Duplo):** `Foruns/forum_rotacao_qwen_unificacao_62c5c207_20260801.md` + `Memorias/memoria_rotacao_qwen_unificacao_62c5c207_20260801.md`. Detalhe completo + rollback: ver memória.

**Bug do grep:** durante a rotação `grep -E` do SO retornava "padrões de busca conflitantes" (alias bug). Rotação feita via Python `re.sub` — 100% confiável. Padrão reutilizável documentado na memória §5.

**Pendências:** (1) Beijing offline — deploy pendente; (2) revogar chaves mortas no console Alibaba (Miguel); (3) coordenar com OPERAÇÃO COFRE ÚNICO (abaixo) — o bug de precedência do `chaves.py` não afeta Qwen agora (tratado nos 2 arquivos), mas persiste para Anthropic/Kimi/xAI.

### 🚨 OPERAÇÃO COFRE ÚNICO (01/08/2026) — unificação em curso, execução travada até OK do Claude

Auditoria fingerprint (Kimi K3/ZCode, a pedido do Miguel) encontrou **violações ativas do Artigo 1º**:

1. **`chaves.py` carrega `chaves_novas.env` ANTES do `.env.unificado`** (`setdefault`) → arquivo velho manda no cofre em produção (Anthropic `3b2a80d5` velha, Kimi `05fba1d7` suspensa, xAI/Perplexity/Telegram-Zizi/X-Bearer velhos).
2. **31 variáveis vivas fora do canônico** — incl. `ZHIPU_API_KEY` (gerador predominante do V4) e `KIMI_VISION_API_KEY`.
3. **`ASSEMBLYAI_API_KEY` (o coringa, com crédito — Miguel 01/08) não consta de nenhum cofre** (chave mestra `sha8:77f59e59` vista no Tencent 29/05). ✅ **RESOLVIDO 16/08/2026:** a chave mestra já está no cofre local `Projeto Cafezinho Agentes/root/.env.unificado` (`ASSEMBLYAI_API_KEY` + espelho `ASSEMBLY_API_KEY`, sha8 `77f59e59` conferido por hash, sem exposição) e o coringa foi INTEGRADO nas cascatas LLM (`Foruns/forum_coringa_assemblyai_cascata_llm_20260816.md`).
4. Drift em 17 vars (tabela completa na memória). OpenAI: rotação pós-18/07 **não registrada** (canônico `f6a7d97d` ≠ `9ca13238` registrado).

**Plano de 5 fases (backup, rollback testado, quarentena 7 dias, manifesto indexado):** `Foruns/forum_unificacao_cofre_chaves_20260801.md` · auditoria completa: `Memorias/memoria_unificacao_cofre_chaves_20260801.md`.
**Decisões Miguel 01/08:** DeepSeek + Kimi recarregados (ficam na cascata); OpenAI/Anthropic com crédito (problema = chaves velhas); AssemblyAI entra como coringa de todos os V4; chaves velhas serão aposentadas com quarentena.

### Rotação OpenAI — 2026-07-18 20:35 BRT (Miguel via `Outros/chaves/rotate-openai-key.sh`)

**Status:** rotacionada no cofre canônico local; smoke HTTP 200 (125 modelos acessíveis); espelhamento em servidores pendente.

| Provider | Variável | Fingerprint anterior | Fingerprint novo | Smoke local |
|---|---|---:|---:|---|
| OpenAI | `OPENAI_API_KEY` | `sha8=0a643fdb` (2026-07-09) | **`sha8=9ca13238`** | `GET /v1/models` HTTP 200 |

**Cofre atualizado:**
- `Outros/chaves/agentes_labs/.env.unificado` — permissões `600` ✅
- Backup pré-rotação: `.bak_pre_openai_rotacao_20260718_203529`

**Espelhamento pendente (Constituição §2):**
- [ ] Tencent (`root@43.156.151.165:38422 /root/.env.unificado`)
- [ ] NYC (`root@198.199.121.136 /root/.env.unificado`)
- [ ] Alibaba Beijing (`/root/.env.unificado`)
- [ ] ServerDo.in WP Cafezinho — verificar se AI Engine consome OpenAI (wp-config.php)

**Ferramenta usada:** `Outros/chaves/rotate-openai-key.sh` (prompt oculto, backup automático, sha8 auditável, teste HTTP embutido; nunca imprime a chave). Reusável em cada servidor.

**Regra posterior:** referir apenas por sha8. Chave nunca aparece em chat/fórum/inbox.

### Rotação OpenAI/Anthropic — 2026-07-09 03:30 BRT (Codex)

**Status:** concluída sem registrar valor bruto no Cérebro, fórum ou pacote de auditoria.

| Provider | Variáveis | Fingerprint vigente | Smoke local | Smoke Tencent |
|---|---|---:|---|---|
| OpenAI | `OPENAI_API_KEY` | `sha8=0a643fdb` | `models.list` OK | `GET /v1/models` HTTP 200 |
| Anthropic / Claude | `ANTHROPIC_API_KEY` = `CLAUDE_API_KEY` | `sha8=3b2a80d5` | `models.list` OK | `GET /v1/models` HTTP 200 |

**Cofres locais atualizados:**

- `Outros/chaves/agentes_labs/.env.unificado`
- `Projeto Cafezinho Agentes/root/.env.unificado`
- `Projeto Cafezinho Agentes/root/chaves_novas.env`
- `Outros/chaves/cafezinho_root/chaves.sh`
- `Outros/chaves/agentes_labs/chaves.sh`
- `Outros/chaves/agentes_labs/.env_root`

**Tencent sincronizado:**

- Cofres vivos: `/root/.env.unificado`, `/home/ubuntu/.env.unificado`
- Compatibilidade runtime atualizada quando havia atribuição direta: `/root/.env`, `/root/chaves.sh`, `/home/ubuntu/chaves.sh`, `/home/ubuntu/chaves_novas.env`
- Permissões reforçadas nos arquivos runtime de chave (`chmod 600` quando aplicável).

**Limpeza de chaves antigas:**

- Backups criados durante esta rotação foram removidos.
- Arquivos locais legacy/backups com `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` ou `CLAUDE_API_KEY` antigos foram sanitizados com marcador `ROTACIONADA_REMOVIDA_20260709`.
- Backups/legacy alvo no Tencent foram sanitizados.
- Varredura direta final dos alvos locais e Tencent: `old_assignments_remaining=0`.

**Regra posterior:** daqui em diante, referir essas chaves apenas por provider, variável e fingerprint curto. Não repetir valor bruto em chat, fórum, pacote, relatório ou memória.

### Cofres legacy (NÃO USAR)

Os arquivos abaixo foram renomeados com prefixo `legacy_` e contém cabeçalho apontando para o cofre canônico:

- `Outros/chaves/legacy_raiz_dotenv`
- `Outros/chaves/cafezinho_root/legacy_chaves_novas.env`
- `Outros/chaves/agentes_labs/legacy_chaves_novas.env`
- `Outros/Agentes Labs/legacy_.env.unificado`
- `Outros/Agentes Labs/legacy_.env`
- `Outros/legacy_.env`
- `Projeto Cafezinho Agentes/legacy_.env`
- Tencent: `/root/legacy_chaves_novas.env`

### Smoke test rápido (10 LLMs)

```bash
python3 -c "
import os, requests
p = 'Outros/chaves/agentes_labs/.env.unificado'
exec(open(p).read().replace('export ',''))
for v in ['DEEPSEEK','KIMI','QWEN','OPENAI','ANTHROPIC','GEMINI','XAI','GROQ','MISTRAL','PERPLEXITY']:
    k = os.environ.get(f'{v}_API_KEY','')
    print(f'{v}: {\"✅\" if k else \"❌\"} ({k[:10]}...)' if k else f'{v}: ❌ AUSENTE')
"
```

### Fontes legado (referência histórica)

- `Projeto Cafezinho Agentes/Outros/chaves/kimi.env`
- `Projeto Cafezinho Agentes/Outros/chaves/backblaze_cerebro.env`
- `Projeto Cafezinho Agentes/Outros/chaves/backblaze_midia_geral.env`

### Chaves de app Vercel/FdI — 2026-08-07 (Kimi K3)
- **`FDI_SYNC_SECRET`** (sha8 `4e11a074`) — chave de sincronização do botão "Sincronizar Google Drive" do app Filhos da Impunidade (`api/drive.js`, header `x-sync-key` no op=push). Valor no cofre canônico local `.env.unificado` + env var production do projeto Vercel `filhosdaimpunidade`. Na mesma env store do Vercel: `GDRIVE_REFRESH_TOKEN` (mesmo valor do `gdrive:` do rclone.conf local) e `GITHUB_TOKEN` (mesmo do `gh auth token` local) — não duplicados no cofre por já terem fonte canônica própria.

### Backblaze B2 — app keys (06/08/2026)

- **`Outros/chaves/backblaze_sites_tematicos_2.env`** — app key `sites-tematicos-2` (criada pelo Miguel no console B2 em 06/08/2026; guardada por ZCode/Kimi na hora, applicationKey só aparece 1× no console). Acesso restrito ao bucket **`site-tematicos`** (testado 06/08). Uso: backups dos sites temáticos. Chmod 600.
- `Outros/chaves/backblaze_cafezinho_backups.env` — app key `cafezinho-backups-rw` (bucket `cafezinho-backups`). ⚠️ 06/08: falhou no rclone do NYC ("API version number 1") — revalidar quando for usar em servidor.
- `Outros/chaves/backblaze_b2.env` — master key (não usar em servidor; só local).

### 🎬 Stack de transcrição/download de vídeo — mapa de chaves (29/08/2026, ZCode/Qwen 3.8)

Consolidação da madrugada de 29/08 (ordem Miguel: "ter tudo no cérebro pra quando precisar baixar vídeo/transcrição"). Detalhes completos: `Foruns/forum_chaves_transcricao_video_stack_consolidado_20260829.md` + `Memorias/memoria_chaves_transcricao_video_stack_20260829.md`.

| Serviço | Variável | Onde | Estado 29/08 |
|---|---|---|---|
| YouTube Data API v3 | `ZCODE_MOKA_YOUTUBE` | cofre intake + 2× `.env.unificado` (sha8 `8b37fadc`) | ✅ viva — vídeos.list/search.list/captions.list; `captions.download` = 401 OAuth (by design). Projeto "GA4 e YouTube" |
| iProyal (proxy residencial) | `IPROYAL_PROXY` | 2× `.env.unificado` + NYC `/root/chaves.sh` | ✅ recarregada 27/08 (US$ 11,90 / 2 GB) |
| AssemblyAI | `ASSEMBLYAI_API_KEY` (sha8 `77f59e59`; `ASSEMBLY_API_KEY` = espelho idêntico p/ roteador legado) | 2× `.env.unificado` | ✅ **validada 29/08 p/ transcrição** (HTTP 200 em `api.assemblyai.com/v2/transcript`) E p/ LLM Gateway — mesma chave serve pros dois |
| Transkriptor | `TRANSKRIPTOR_API_KEY` (sha10 `eb3f887986`) | cofre intake (chegou como `TRANSKRIPTOR_NOVA`, 03/09 06:20) + Dell 4 cofres (2× `.env.unificado` + 2× `chaves.sh` agentes_labs/cafezinho_root) + NYC `/root/chaves.sh` + `/root/.env.unificado` + tencent `.env.unificado` | ✅ **VIVA — girada 03/09 06:3x BRT (ZM/Kimi K3)** — Miguel re-assinou e depositou a nova no intake; rotação Regra 4: backup `.bak_pre_transkriptor_20260903` em todos os 7 cofres, velha (sha `ac15420a84`) fora do vivo; **validada ao vivo: HTTP 200 em `api.tor.app/developer/files`** (read-only). Agentes YouTube NYC (`youtube_v2`) leem via `source /root/chaves.sh` no runner — próxima corrida (cron 11h/17h) já usa a nova. ⚠️ Pendente: env Vercel do Moka (chave velha lá também — girar quando o Moka estiver em frente ativa) |
| Supadata | `SUPADATA_API_KEY` (ainda NÃO gravada) | — | ⏳ **PENDENTE** — conta grátis do Miguel existe (27/08 14:57, Google OAuth, org `532670f6-3d4e-4c9c-8aa6-f92afec8ca48`) mas a sessão sumiu deste PC. Receita quando a chave chegar: testar sem gastar crédito (`GET https://api.supadata.ai/v1/transcript` SEM url, header `x-api-key` → 400=boa / 401=ruim) → gravar no intake + 2 espelhos + NYC `/root/chaves.sh` (Regra 4, c/ backup). Plano free = 100 créditos/mês sem cartão |
| TranscriptAPI (US$ 5/mês) | — | — | ❌ NÃO contratada de propósito — o free do Supadata cobre o mesmo escopo (só legendas existentes) |

**Como baixar/transcrever vídeo hoje (resumo):** legenda de YouTube = innertube client ANDROID + proxy iProyal (rota `/api/ingest` do Moka, provado nos 3 ambientes); NYC = pipeline `youtube_v2` com cascata supadata→transkriptor (Supadata 1º quando a chave chegar). Vídeo SEM legenda = Whisper NYC ou Supadata (2 cr/min) ou AssemblyAI (US$ 0,37/h, download nosso).

## Variáveis LLM chinesas

- DeepSeek: `DEEPSEEK_API_KEY` — **✅ corrigida em 06/08/2026 (Kimi 3, pedido Miguel): a chave anterior estava morta (401); substituída pela válida viva (sha8 `b6c4d4de`, testada 200 ao vivo). Backup do cofre em `.env.unificado.bak_deepseek_20260806`.**
- Kimi/Moonshot (tradicional): `KIMI_API_KEY` ou `MOONSHOT_API_KEY`
- Kimi Code / K3 (assinatura): `KIMI_CODE_API_KEY` — endpoint `https://api.kimi.com/coding/v1`, modelo `k3`
  - **Reconciliação 07/08/2026 (Vigília de Crédito, Regra 4):** existem **duas chaves Kimi Code vivas** — `KIMI_CODE_API_KEY` sha8 `6dcfcad3` (arquivo `Projeto Cafezinho Agentes/Outros/chaves/kimi_code.env`) e `KIMI_CODE_API_KEY_ZCODE` sha8 `92aed0f2` (a que está no provider "Kimi 3" do ZCode; gravada nos 3 cofres em 07/08). Ambas válidas, ambas esgotadas no teste (403 `access_terminated_error`) — possivelmente contas distintas, candidato a rodízio. `KIMI_VISION_API_KEY` sha8 `320da64b` agora espelhada também no cofre canônico (antes só no espelho). Backups `.bak_pre_vigilia_20260807_1221`. Detalhes: `Foruns/forum_vigilia_credito_zcode_20260807.md`.
- **🟢 Kimi Pay-as-you-go (AGENTES):** `KIMI_PAYGO_API_KEY` — endpoint `https://api.moonshot.ai/v1`, 12 modelos incluindo K3. **Esta é a chave para agentes de produção.** Ver `kimi_paygo.env`.
- Qwen/Alibaba/DashScope: `QWEN_API_KEY`, `DASHSCOPE_API_KEY` ou `ALIBABA_API_KEY`

## Scripts de consulta

- DeepSeek: `Projeto Cafezinho Agentes/scripts/chamar_deepseek.py`
- Kimi: `Projeto Cafezinho Agentes/scripts/chamar_kimi.py`
- Qwen: `Projeto Cafezinho Agentes/scripts/chamar_qwen.py`

## Teste rápido sem expor segredo

Rodar da raiz do workspace:

```bash
python3 "Projeto Cafezinho Agentes/scripts/chamar_deepseek.py" --model deepseek-v4-flash --prompt "Responda apenas OK."
python3 "Projeto Cafezinho Agentes/scripts/chamar_kimi.py" --model moonshot-v1-32k --prompt "Responda apenas OK."
python3 "Projeto Cafezinho Agentes/scripts/chamar_qwen.py" --model qwen-plus --prompt "Responda apenas OK."
```

Rodar de dentro de `Projeto Cafezinho Agentes` também deve funcionar:

```bash
python3 scripts/chamar_deepseek.py --model deepseek-v4-flash --prompt "Responda apenas OK."
python3 scripts/chamar_kimi.py --model moonshot-v1-32k --prompt "Responda apenas OK."
python3 scripts/chamar_qwen.py --model qwen-plus --prompt "Responda apenas OK."
```

### Smoke Kimi Code / K3

```bash
# Teste direto (Python)
python3 -c "
import urllib.request, json
key = open('Projeto Cafezinho Agentes/Outros/chaves/kimi_code.env').read().strip().split('=',1)[1]
req = urllib.request.Request('https://api.kimi.com/coding/v1/chat/completions',
    data=json.dumps({'model':'k3','messages':[{'role':'user','content':'OK'}],'max_tokens':20,'thinking':{'type':'disabled'}}).encode(),
    headers={'Authorization':f'Bearer {key}','Content-Type':'application/json'})
print(json.loads(urllib.request.urlopen(req).read())['choices'][0]['message']['content'])
"
```

## Incidente 2026-05-16 21:42 BRT

Durante consulta à Trindade Chinesa sobre os portais satélites, Qwen e Kimi responderam, mas DeepSeek falhou na primeira tentativa com `DEEPSEEK_API_KEY não encontrada`.

Causa: o script `scripts/chamar_deepseek.py` carregava `root/chaves_novas.env` e `root/.env.unificado` usando caminhos relativos ao diretório atual. Quando chamado da raiz `Antigravity Google`, ele procurava no lugar errado.

Correção: `scripts/chamar_deepseek.py` passou a calcular `PROJECT_ROOT = Path(__file__).resolve().parents[1]` antes do carregamento e a carregar os `.env` por caminhos absolutos relativos ao projeto.

Lição: todo script que consulta LLM deve ser independente do diretório atual. A chave pode existir no Cérebro/projeto e ainda assim parecer ausente se o carregador for frágil.


## Smoke Operacional Integrado — 2026-05-28 23:36 BRT (Kimi)

**Problema:** RESUMO_DESPERTAR.md era gerado por `memoria_worklog.py wake`, mas tinha apenas texto estático sobre chaves. O agente acordava sabendo *onde* as chaves estavam, mas não *se estavam acessíveis agora*.

**Solução:** Pipeline integrado `smoke_operacional.sh` → `acorde.sh` → `memoria_worklog.py`.

### Arquivos novos/modificados

| Arquivo | Função | Backup |
|---|---|---|
| `scripts/smoke_operacional.sh` | Bash. Verifica `.env` locais (conta variáveis), SSH Tencent (status bot + banco), SSH Alibaba, scripts de consulta LLM. Timeout curto, sem bloqueio. | `.bak_pre_integracao_chaves_20260528_2337.sh` |
| `acorde.sh` | **Comando ÚNICO de despertar.** 4 passos: smoke → parse-canal → wake (1 só) → validate. Antes chamava `atualizar_memoria_trabalho_fase1.sh` que duplicava wake. | `.bak_pre_unico_wake_20260528_2342.sh` |
| `root/scripts/memoria_worklog.py` | Template `cmd_wake` modificado para injetar status operacional ao vivo no `RESUMO_DESPERTAR.md`. | `.bak_pre_integracao_chaves_20260528_2337.py` |
| `memorias_provisorias/MANIFESTO_MEMORIA_TRABALHO.json` | Adicionados `"cofre_chaves"` e `"politica_llm"` nos arquivos globais. | `.bak_pre_integracao_chaves_20260528_2337.json` |

### O que o smoke verifica (sem expor segredos)

- `.env` locais: existem? Quantas variáveis sensíveis contêm?
- SSH Tencent: conecta? Bot Zizi Linda ativo? Banco de mídia acessível?
- SSH Alibaba: conecta?
- Scripts `chamar_deepseek.py`, `chamar_kimi.py`, `chamar_qwen.py`: presentes?

### O que aparece no RESUMO_DESPERTAR.md

1. **🔐 ONDE ESTÃO AS CHAVES** — referência permanente (template do gerador)
2. **🖥️ Status Operacional (ao vivo)** — resultado do smoke real da última execução de `acorde.sh`
3. Estado Ativo, Pendências, Memórias, Canal, Sprints

### Comandos

```bash
# Comando ÚNICO de despertar — tudo integrado
./acorde.sh [agente] [tail]

# O que ele faz (1 wake só, sem duplicação):
# 1. Smoke operacional → gera .status_operacional.md
# 2. Parse-canal → importa novidades para memórias vivas
# 3. Wake → gera RESUMO_DESPERTAR.md com memória integrada de toda a Trindade
# 4. Validate → checa integridade dos caminhos

# Smoke isolado (para debug)
./scripts/smoke_operacional.sh

# Wake isolado (emergência, sem smoke/parse)
python3 root/scripts/memoria_worklog.py wake --agente todos --tail 12
```

### Separação de responsabilidades

| Script | Quando usar | O que faz |
|---|---|---|
| `./acorde.sh` | **Comando único de despertar.** Você roda isso. | Smoke → parse-canal → wake (1 só, visível) → validate |
| `./scripts/atualizar_memoria_trabalho_fase1.sh` | Manutenção periódica (cron/manual). | parse-canal → wake (silencioso) → validate |

**Por que separar:** O `acorde.sh` é o comando do usuário. O `fase1.sh` é a rotina de housekeeping. Antes o `acorde.sh` chamava o `fase1.sh` e depois fazia wake de novo — duplicação. Agora cada um tem seu papel.

### Segurança

- Smoke nunca lê valores de chave. Só conta quantas variáveis existem (`grep -c`).
- SSH usa `BatchMode=yes`, não interativo.
- Timeout curto (5s SSH, 8s comandos). Falha não bloqueia wake.
- `.status_operacional.md` é gerado em `memorias_provisorias/` (gitignored por padrão).


## Incidente Qwen/DashScope — 2026-05-17 09:39 BRT

**Status:** corrigido nos pontos vivos auditados, sem expor segredo.

**Fingerprint operacional da chave nova:** `sk-92f...4f33`, `sha8=0a93e3ae`, comprimento 35. Este fingerprint serve para comparação; não é segredo suficiente para autenticação.

**O que foi validado:**

- Endpoint internacional correto: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`.
- `GET /models`: HTTP 200, com modelos Qwen, DeepSeek, visão e imagem disponíveis.
- Smoke local: `qwen-max-latest`, `qwen-max`, `qwen3-max-preview`, `qwen3.6-max-preview`, `qwen-plus-latest`, `qwen-plus`, `qwen3.6-plus`, `qwen-vl-max-latest`, `qwen-vl-max` responderam OK.
- Smoke remoto Cingapura: `qwen-max-latest` HTTP 200.
- Smoke remoto Droplet Rio Carta: `qwen-max-latest` HTTP 200.

**Locais atualizados nesta correção:**

- Local Cafezinho: `Projeto Cafezinho Agentes/root/.env` já estava com a nova chave.
- Local Rio Carta: `Rio Carta Agentes/root/chaves_riocarta.env` foi atualizado; backup `chaves_riocarta.env.bak_qwen_20260517_20260517_093647`.
- Local Global South News: `Global South News/root/chaves_gsn.env` foi atualizado; backup `chaves_gsn.env.bak_qwen_20260517_20260517_093647`.
- Tencent Cingapura: `/root/.env`, `/root/chaves_novas.env` e `/root/chaves.sh` foram atualizados; backups `*.bak_qwen_20260517_20260517_093823`.
- Droplet Rio Carta: `/root/chaves_riocarta.env` foi atualizado; backup `/root/chaves_riocarta.env.bak_qwen_20260517_20260517_123844`.

**Modelos Qwen recomendados por função, a partir da lista viva da conta:**

- Texto topo/alta precisão: `qwen3.6-max-preview` ou, se latência/custo pesar, `qwen3-max-preview` / `qwen-max-latest`.
- Texto equilibrado: `qwen3.6-plus` ou `qwen-plus-latest`.
- Visão/tribunal visual: `qwen-vl-max-latest`.
- Imagem IA chinesa: `qwen-image-2.0-pro` / `qwen-image-2.0-pro-2026-04-22`.

**Regra nova:** chave não “se refere” a um modelo. A chave autoriza conta/região. O modelo é escolhido no JSON/código de cada agente. Toda troca de chave deve testar: endpoint, `/models`, um modelo topo, um modelo barato, visão se usada, e smoke no servidor onde o agente roda.

**Por que demoramos tanto a descobrir:**

1. Não havia fonte única de verdade para Qwen. A mesma família de chave estava espalhada por `.env`, `chaves_novas.env`, `chaves.sh`, `chaves_riocarta.env`, backups e fóruns.
2. Antigravity atualizou localmente `Projeto Cafezinho Agentes/root/.env`, mas o servidor vivo de agentes em Cingapura continuou com a chave antiga em três arquivos.
3. A investigação inicial confundiu “chave válida localmente” com “chave em uso pelo sistema vivo”. O teste precisava ser feito no servidor remoto que executa os agentes.
4. Havia mistura histórica entre endpoint chinês (`dashscope.aliyuncs.com`) e endpoint internacional (`dashscope-intl.aliyuncs.com`). A chave correta precisa bater com a região/endpoint correto.
5. O Cérebro tinha regras de segurança para não vazar segredo, mas ainda não tinha índice rápido suficiente com fingerprint, local vivo e comando de smoke por servidor.
6. Faltava uma checagem automática periódica das chaves LLM em produção, com alerta quando uma chave velha diverge do fingerprint canônico.

**Prevenção obrigatória:** criar sprint de fonte canônica de chaves/modelos: fingerprint central, auditoria por servidor, teste de modelo, e alerta quando local/remoto divergem. Nunca depender só de leitura local.

## Bot DeepSeek — @augustodeepseekbot (2026-05-17)

- Variável: `TELEGRAM_TOKEN_DEEPSEEK`
- Máscara: 8654018954:AAGQ...moUk
- Username: @augustodeepseekbot
- Finalidade: ponte Telegram exclusiva do DeepSeek Code (não compete com Augusto)
- Arquivo: `root/.env`

## Rotação Qwen — 2026-05-21 15:05 BRT (DeepSeek/Codex)

**Motivo:** Claude Monitor detectou HTTP 401 no Tencent (portal chinês). Chave antiga ainda funcionava no dashscope-intl mas estava com os dias contados.

**Nova chave:** fingerprint `sk-d0d8...99e5`, comprimento 35. O valor completo não deve ser repetido em fórum, canal ou Cérebro.

**Backup:** `.env.bak_pre_qwen_20260521_150518`

**Propagação feita por Codex em 2026-05-21 15:10-15:12 BRT:**

- Local Cafezinho: `Projeto Cafezinho Agentes/root/.env` já atualizado por DeepSeek.
- Local Rio Carta: `Rio Carta Agentes/root/chaves_riocarta.env` atualizado; backup `chaves_riocarta.env.bak_qwen_20260521_20260521_151147_codex`.
- Local GSN: `Global South News/root/chaves_gsn.env` atualizado; backup `chaves_gsn.env.bak_qwen_20260521_20260521_151147_codex`.
- Tencent/Cingapura: `/root/.env`, `/root/chaves_novas.env`, `/root/chaves.sh` atualizados; backups `*.bak_qwen_20260521_20260521_151005_codex`.
- GSN Beijing: `/home/ubuntu/gsn_agentes/chaves_gsn.env` atualizado; backup `chaves_gsn.env.bak_qwen_20260521_20260522_021044_codex` no relógio do servidor.

**Validação Codex:**

- Tencent/Cingapura, caminho real do roteador: `gerar_texto_provider_hard("alibaba", ...)` com `qwen-max` respondeu `OK`.
- Tencent/Cingapura, teste HTTP direto:
  - `dashscope.aliyuncs.com`: 401.
  - `dashscope-intl.aliyuncs.com`: 200.
- GSN Beijing, teste HTTP direto:
  - `dashscope.aliyuncs.com`: 401.
  - `dashscope-intl.aliyuncs.com`: 200.
- GSN Beijing, roteador: bloqueado por bug separado, `gsn_agente_roteador_llm.py` ainda importa `riocarta_carregar_chaves`.

**Conclusão:** a chave nova está correta para o endpoint internacional. O alerta original do Claude Monitor era verdadeiro como smoke do endpoint chinês, mas não representa o caminho real do roteador vivo, que usa `dashscope-intl`. A solução é padronizar qualquer smoke Qwen pelo endpoint configurado no provider (`base_url`) e não hardcodar `dashscope.aliyuncs.com`.

**Pendência Rio Carta remoto:** Miguel corrigiu que Rio Carta agora está em Tencent Beijing, mas Codex não encontrou diretório Rio Carta em `82.156.167.218:/home/ubuntu`. Não usar mais o Droplet antigo como referência sem revalidar. Local Rio Carta foi atualizado; remoto Rio Carta Beijing precisa de path canônico antes de edição.

## Re-rotação Qwen — 2026-05-21 17:35 BRT (DeepSeek)

**Motivo:** chave `sk-d0d8...99e5` exposta por DeepSeek em `canal_trindade.md` (15:05 BRT) e `forum_chave_qwen_20260521.md`. Claude Monitor detectou às 17:10.

**Nova chave:** fingerprint `sk-6f5e...120c` — testada, `qwen-max` HTTP 200.  
**Backup local:** `.env.bak_pre_qwen_rot2_20260521_173508`

**Lição registrada:** chave NUNCA em fórum ou canal. Apenas fingerprint mascarado.  
**Pendência:** Codex propagar nova chave para Tencent, Rio Carta e GSN Beijing. Higienizar chave anterior dos arquivos onde foi exposta.

## Smoke completo — 2026-05-21 19:48 BRT (DeepSeek)

Todas as 8 chaves LLM principais testadas localmente com chamadas mínimas (max_tokens=5):

| Provider | Modelo testado | Status |
|----------|---------------|--------|
| DeepSeek | deepseek-v4-flash | ✅ |
| Moonshot | moonshot-v1-8k | ✅ (chave renovada) |
| Qwen | qwen-plus | ✅ |
| Zhipu | glm-4-plus | ✅ (chave renovada) |
| OpenAI | gpt-4o-mini | ✅ |
| Anthropic | claude-haiku-4-5 | ✅ (adicionada do Tencent) |
| Gemini | gemini-2.5-flash | ✅ (chave renovada) |
| Brave | search | 🔴 **CONTA MORTA desde a noite de 08/09/2026** — HTTP 301→api-dashboard em TODAS as chaves testadas (a v4 `bravesearch-v4` rotacionada 14:1x→14:3x do mesmo dia com provas 200×4 — sha12 real nas máquinas à noite `49123d2c1c2f` — + 3 velhas `c01af15d3ac0`/`aecd54617a7e`/`04b4e983c575`), de 2 redes (Tencent+NYC) → morreu entre 14:3x e 23:0x. ⚠️ Desencontro de sha registrado (Regra 4): log da rotação diz `4512b7e0e824`, valor real à noite = `49123d2c1c2f`. **Aguarda ação do Miguel** (verificar assinatura/billing Brave; chave nova no intake → rotação Regra 4 na hora). Provisório: DSN R1/R2 com **Bing News/Web RSS (SEM chave, 200 do Tencent)**; perna brave segue no código e revive sozinha se a conta voltar — ver logs datados 08/09 (restaurados 09/09 pós-clobber) e 09/09 no fim · ➕ 09/09 06:0x: **Miguel RENOVOU a assinatura** (09/09 ~05:3x) mas a chave do cofre SEGUE 301 (destino MUDOU: brave.com/search/api/ — provável chave velha invalidada na renovação; **PENDENTE: gerar chave NOVA no dashboard e depositar em `~/cofre_intake/`** → rotação Regra 4 na hora; intake sem chave nova, mtime 08/09 14:08). **TRAVA ZM_TRAVA_BUSCA_20260909 instalada em R1+R2**: auto-desligam se perderem TODA busca (sonda Bing→Brave→Plano B GLM+web a cada ciclo; religam sozinhos); brave virou ÚLTIMO recurso da escada ("o brave é caro" — Miguel) — ver log datado 09/09 e fórum §11.2-ZM |
| Brave | answer (chat/completions) | ⚠️ existe mas DESCARTADA de fact-check 2026-07-26 (autocontradição entre queries) |
| SearchAPI | searchapi.io `SEARCHAPI_API_KEY` | ✅ 2026-07-26 — reserva do gate fact-check (timeout 5s); quota só via dashboard (API `/account` 404) |

Backup .env: `.env.bak_pre_cofre_sprint_20260521_194040`

## Aiatolah — ambiente local e chaves operacionais (2026-05-23)

**Status:** arquivo operacional criado localmente, gitignored, sem exposição em fórum/canal.

Arquivo criado:

- `aiatolah/.env.local`

Template seguro:

- `aiatolah/.env.example`

Manifesto seguro:

- `aiatolah/CHAVES_AIATOLAH_MANIFESTO.md`

Fontes usadas para preencher o ambiente local:

- `Projeto Cafezinho Agentes/root/.env`
- `Projeto Cafezinho Agentes/root/.env.unificado`
- `Projeto Cafezinho Agentes/root/chaves_novas.env`
- `Projeto Cafezinho Agentes/root/chaves/alibaba_prometheus.env`

Variáveis preenchidas localmente incluem LLMs chinesas, busca, imagem, LLMs ocidentais de apoio, Prometheus e GitHub Token. Valores reais não devem ser copiados para ChatGPT, fórum, canal ou Git. Para auditoria, registrar apenas nomes de variáveis, fingerprints e resultado de smoke.

### Resolução de Tokens Globais
- `GITHUB_TOKEN` (Resolvido ✅): Token clássico ativo (`ghp_...esUC`) verificado com sucesso por fumaça em `2026-05-31`. Fornece permissões de leitura/escrita completas (`repo` scope) para o ecossistema Astro (`mundo-trilhos`, `aiatolah`, `rio-carta`, `global-south-news`).
- `VERCEL_TOKEN` (Pendente ⚠️): Pode não bloquear se os deploys dos portais Astro forem acionados automaticamente via Webhooks integrados ao repositório GitHub na plataforma Vercel.

Pendências detectadas no preenchimento automático:

- `VERCEL_TOKEN`


## WordPress O Cafezinho — REST API + SSH canônico (atualizado 2026-08-13)

> **Diretriz operacional:** a credencial REST continua válida, mas agentes CLI que forem **corrigir posts existentes** devem preferir SSH `cafezinho-wp` + WP-CLI no `/var/www/ocafezinho`. Ver `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`. Não registrar valores de chave SSH ou senha fora do cofre.

**Finalidade:** publicação manual por qualquer LLM (Grok, Claude, ChatGPT, etc.) e agentes que usam `motor_publicador.py`.

| Variável | Onde | Nota |
|----------|------|------|
| `WP_SITE` | `.env.unificado` | `https://controle.ocafezinho.com` |
| `WP_USER_CAFEZINHO` | `.env.unificado` | Usuário REST atual `Redacao nova` (slug `redacao-nova`; validado 2026-07-27) |
| `WP_PASS_CAFEZINHO` | `.env.unificado` | Application Password — **valor só no cofre** |
| `WP_USER` / `WP_PASS` | fallback legacy | Mesmo par se variáveis `_CAFEZINHO` ausentes |

Rotação de 2026-07-27: a nova Application Password foi validada com HTTP 200 e capacidades administrativas no endpoint de identidade do WordPress. O segredo permanece exclusivamente no cofre `.env.unificado`; scripts e tutoriais usam variáveis de ambiente.

**Cofre canônico local:**

```text
Outros/chaves/agentes_labs/.env.unificado
Projeto Cafezinho Agentes/root/.env.unificado   ← espelho
```

**Servidor Tencent:** `/root/chaves.sh` exporta as mesmas variáveis para cron.

**Documentação operacional:** `Cerebro/CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`  
**Tutorial universal:** `Projeto Cafezinho Agentes/Foruns/forum_tutorial_publicar_wordpress_cafezinho_todos_llms_20260620.md`  
**Script:** `scratch/publicar_cafezinho_wp.py`

**Smoke (sem expor valor):**

```bash
grep -E '^WP_(SITE|USER_CAFEZINHO|PASS_CAFEZINHO)=' Outros/chaves/agentes_labs/.env.unificado | sed 's/=.*/=<ok>/'
```

---

## R2 Cloudflare — Cafezinho (criado 2026-06-02; migrado ao cofre único 2026-07-21)

- **R2_ACCESS_KEY:** no cofre `.env.unificado` — `sha8=38d09315` (len=32)
- **R2_SECRET_KEY:** no cofre `.env.unificado` — `sha8=43f84bcb` (len=64)
- **R2_BUCKET:** `cafezinho` (também no cofre)
- **R2_ENDPOINT:** `https://3a4cf4eecd4afd4c0e7799e725728d07.r2.cloudflarestorage.com` (também no cofre)
- **R2_PUBLIC_URL:** `https://pub-7c53d388419e4d44b17eace540ae7e22.r2.dev` (também no cofre)

### R2 — MOKA MEMÓRIA (bucket de cortesia, 30/08/2026, obra MOKA)
- **`R2_MOKA_BUCKET=moka-memoria-cortesia`** — criado pelo ZM via rclone com as MESMAS credenciais R2_* acima (elas têm poder de criar bucket — provado). Escrita/leitura provadas (carimbo 30/08 16:02 BRT). Uso: memória de cortesia do Moka (10GB grátis, egress zero — parecer ZM-016). Espelhado nos 2 `.env.unificado` (backups `.bak_pre_moka_r2_20260830`). B2 de backup: app key NOVA entregue pelo rito [SEGREDO] (30/08 ~16h) — keyName `moka-cortesia`, keyID `0052bd...01b` (sha8 `ea4d334a`), gravada no intake + 2 `.env.unificado` (backups `.bak_pre_moka_b2_20260830`). **Estado: autentica (conta 2bd48aa3afde) MAS capabilities=[] e list_buckets 401 — nasceu sem escopo; Miguel vai recriar marcando Read & Write no bucket `moka-memoria-backup`.** A antiga multi-bucket segue restrita a 1 bucket.
- **Criado por:** Miguel, 2026-06-02
- **Finalidade:** Armazenamento de imagens/mídia do Cafezinho; URL pública para vídeos consumidos pela Graph API (Instagram Reels)
- **Smoke validado 2026-07-21:** `list_objects_v2` OK via boto3 a partir do cofre
- **Nota:** os valores das duas chaves estavam em texto claro neste nodo até 2026-07-21 (violação do Artigo 1). Sanitizado por ZCode; valores agora só no cofre.

## WordPress Revista Fórum — REST API (migrado ao cofre único 2026-07-21)

| Variável | Valor/onde | Nota |
|----------|-----------|------|
| `FORUM_WP_SITE` | `https://revistaforum.com.br` (no cofre) | Endpoint base |
| `FORUM_WP_USER` | `migueldorosario` (no cofre) | author ID 41, categoria "O Cafezinho" ID 114 |
| `FORUM_WP_PASS` | no cofre — `sha8=a5bc70dc` (len=29, **contém espaços → valor entre aspas no .env**) | Application Password |

- **Origem:** estavam hardcoded em `scratch/check_forum_post.py` e vários `scratch/publish_*_to_forum.py` (violação do Artigo 1). Migradas por ZCode em 2026-07-21; scripts antigos ainda contêm cópias — pendente higienização dos scratch.
- **Smoke validado 2026-07-21:** `GET /wp-json/wp/v2/users/me` HTTP 200 (slug `migueldorosario`).
- **Documentação operacional:** `Cerebro/cartoes_bolso/CARTAO_BOLSO_WP_REVISTA_FORUM.md` (regras de teaser, upload binário, taxonomia).


## SSH Aliases — ~/.ssh/config (criado 2026-06-04)

Aliases canônicos para uso no `acorde.sh` e por qualquer agente:

| Alias | HostName | Porta | User | Chave | Status |
|---|---|---|---|---|---|
| `tencent` | 43.156.151.165 | 38422 | ubuntu | `~/.ssh/id_rsa` | ✅ OK |
| `alibaba` | 39.106.184.215 | 22 | root | `~/.ssh/id_rsa` | ✅ OK |

**Aliases legados equivalentes ao Tencent:** `china`, `cingapura`, `china-proxy`, `china-install` (mesmo IP 43.156.151.165).

**Nota histórica:** IP antigo do Alibaba (8.222.202.213) estava offline. Correção aplicada em 2026-06-04 após Miguel identificar que os scripts de produção já usavam 39.106.184.215. Chave `id_rsa_alibaba` nunca existiu localmente — sempre foi `id_rsa` normal.

**Teste rápido:**
```bash
ssh tencent "echo OK"
ssh alibaba "echo OK"
```

Criado por Qwen em 2026-06-04 12:32 BRT, corrigido em 2026-06-04 12:40 BRT.

## Reforma Visual Cafezinho — mapa rápido de acessos (criado 2026-07-27, ZCode)

Para reformas visuais (capa/tema/responsivo) do Cafezinho. **Valores nunca aqui** — só ponteiros. Detalhe completo: `Foruns/forum_reforma_visual_cafezinho_20260727.md`.

| Recurso | Ponteiro |
|---|---|
| SSH canônico (us65.serverdo.in) | alias `cafezinho-wp` (`~/.ssh/config`, chave `~/.ssh/id_rsa`); senha root SÓ em `Outros/chaves/ssh_servidor_wp_cafezinho.md` (gitignored) |
| SSH espelho cafezinho.news | `root@159.65.177.60` (chave local autorizada); Basic Auth do front no fórum do lab |
| wp-cli | `sudo -u www-data wp --path=/var/www/ocafezinho` (canônico) · `--path=/var/www/cafezinho-news` (espelho) |
| WP REST canônico | `WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO` no cofre `.env.unificado` — usuário `redacao-nova` (rotacionada por Codex 27/07 04:40) |
| DB canônico | `/var/www/ocafezinho/wp-config.php` (via SSH) · DB espelho: `/root/.cafezinho_news_db_pass` |
| Senha root droplet cafezinho.news (espelho 159.65.177.60) | `root cafezinho espelho` | intake `ROOT_159_65_177_60_ROOT_CAFEZINHO_ESPELHO` (13/09 16:26) + espelho Regra 4: `Outros/chaves/ssh_root_cafezinho_news_espelho.md` (600, gitignored) | ✅ TROCADA 13/09/2026 pós-hack (fórum_hack_cafezinho_news_20260913); SSH só por chave; senha vale p/ console DO/sudo |
| Purge de cache (Rocket sem CLI) | ⚠️ **ATUALIZADO 01/09:** o script standalone `/root/rollback_canonico_20260727/purge_rocket.php` **NÃO purga** (PHP standalone não carrega o WordPress → `rocket_clean_*` não existem → saída vazia silenciosa). Cura provada: `sudo -u www-data wp --path=/var/www/ocafezinho eval 'rocket_clean_domain(); rocket_clean_minify();'` → "domain OK minify OK". Após purge, HTML velho pode persistir ~5 min em cache de URL exata — query string (`?v=2`) contorna/testa. Caso: fórum `forum_titulo_villatoro_emenda_emu2_20260901` |
| Rollback/versões | canônico: `/root/rollback_canonico_20260727/` · espelho: `/root/lab_visual_versoes/` |

## Dez Mandamentos de Segurança para Agentes

1. Entenda antes de agir. Leia o Baleia Azul, o índice do CÉREBRO, o fórum e o estado atual do componente.
2. Saiba onde a credencial vive, mas nunca copie seu valor para chat, fórum, manifesto, log, prompt ou código.
3. Faça backup recuperável antes de alterar um arquivo existente e registre origem, destino e data.
4. Defina o rollback antes da mudança. Se não souber voltar, ainda não está pronto para avançar.
5. Preserve trabalho alheio. Não sobrescreva, reverta ou reorganize mudanças de outro agente sem coordenação.
6. Trabalhe no escopo atribuído. Ao encontrar sobreposição ou conflito, pare a parte conflitante e reporte imediatamente.
7. Prefira mudanças pequenas, auditáveis e reversíveis. Operações destrutivas exigem cuidado excepcional e autorização correspondente.
8. Separe diagnóstico de execução. Ler, medir ou propor não autoriza deploy, publicação, gasto, envio ou alteração externa.
9. Produza manifesto próprio com arquivos, decisões, testes, riscos, backup e rollback. Copie o manifesto para o fórum do sprint.
10. Em dúvida, preserve evidência e peça coordenação. Velocidade nunca justifica esconder falha, conflito ou incerteza.

Estes mandamentos orientam julgamento responsável. Eles não substituem inteligência, contexto, protocolos específicos ou revisão humana.

### Rotação Anthropic — 2026-07-20 15:03 BRT (Miguel via Claude Code)

| Provedor | Variável | Antes | Depois | Verificação |
|---|---|---|---|---|
| Anthropic | `ANTHROPIC_API_KEY` | (chave inválida em NYC detectada por healthcheck 14:44 BRT) | **`sha8=3334781a`** | `GET /v1/models` HTTP 200 · latência 316ms local · 187ms NYC |

**Arquivos atualizados (8 ativos, backups .bak_pre_anthropic_rot_20260720_150354 preservados em todos):**
- LOCAL: `Outros/chaves/agentes_labs/.env.unificado`, `Projeto Cafezinho Agentes/root/.env.unificado`, `Outros/chaves/agentes_labs/chaves.sh`, `Outros/chaves/cafezinho_root/chaves.sh`
- NYC: `/root/chaves.sh`, `/root/.env`, `/root/.env.unificado`, `/root/chaves_novas.env`

**Contexto:** Chave anterior detectada como inválida em healthcheck Sentinela de 20/07 14:44 BRT (junto com OpenAI, Kimi, Grok também inválidas em NYC). Miguel passou chave nova via chat às 15:00 BRT e autorizou rotação imediata pra revalidar V4 workers (que estavam dando `worker_exception RuntimeError` em geopolítica e `image_pending` recorrente).

**Chaves ainda inválidas em NYC (pendentes de rotação):** OpenAI, Moonshot/Kimi, xAI/Grok. Também: Groq e Z.ai/GLM ausentes em NYC.

**Regra §16 carta passagem 19/07:** chave antiga foi compartilhada em chat com Anthropic support; sha8 anterior a rotacionar no console Anthropic (revogar) — Miguel disse "depois eu rotaciono, estou sem tempo agora" antes de me pedir pra usar a chave nova. Agenda: revogar chave antiga no console pra invalidar exposição.

### Rotação OpenAI — 2026-07-20 15:10 BRT (Miguel via Claude Code)

| Provedor | Variável | Antes | Depois | Verificação |
|---|---|---|---|---|
| OpenAI | `OPENAI_API_KEY` | `sha8=9ca13238` (2026-07-18) | **`sha8=f6a7d97d`** | `GET /v1/models` HTTP 200 · 791ms local · 694ms NYC |

**Arquivos atualizados (8 ativos, backups `.bak_pre_openai_rot_20260720_151012` preservados):**
- LOCAL: `Outros/chaves/agentes_labs/.env.unificado`, `Projeto Cafezinho Agentes/root/.env.unificado`, `Outros/chaves/agentes_labs/chaves.sh`, `Outros/chaves/cafezinho_root/chaves.sh`
- NYC: `/root/chaves.sh`, `/root/.env`, `/root/.env.unificado`, `/root/chaves_novas.env`

**Contexto:** Continuação da onda de rotações 20/07 após healthcheck Sentinela 14:44 BRT detectar 4 chaves inválidas em NYC (Anthropic, OpenAI, Moonshot, xAI). Anthropic rotacionada 15:03 BRT (sha8=3334781a). OpenAI rotacionada 15:10 BRT (sha8=f6a7d97d). Ambas testadas HTTP 200. Kimi/Moonshot chega ~16:00 BRT, xAI/Grok pendente. Chave OpenAI antiga (sha8=9ca13238) exposta no chat em 18/07 20:35 BRT e não foi revogada; agora rotacionada, a antiga fica pendente de revogação no console OpenAI pela Miguel.

## IPRoyal — proxy residencial (renovado 2026-08-03, integrado por Kimi K3/ZCode)

**Finalidade:** fallback anti-bloqueio dos pipelines yt-dlp (agente YouTube Cafezinho; futuro Moka Video `/api/ingest`). NÃO é rota padrão — yt-dlp tenta direto e só cai para o proxy em bot-check/429/403/geo-block.

| Variável | Onde | Fingerprint |
|---|---|---|
| `IPROYAL_PROXY` | `.env.unificado` (canônico + espelho, 03/08) | URL `sha8=ed44d32f` · user `sha8=945b3368` · pass `sha8=9dd50483` |
| `YOUTUBE_PROXY_MODE` | idem — `off` \| `fallback` (padrão) \| `always` | **chave de desligamento** do agente YouTube: `off` = proxy desligado sem mexer em código |
| `MOKA_PROXY_MODE` | opcional; se ausente herda `YOUTUBE_PROXY_MODE` | chave de desligamento do Moka Video `/api/ingest` |

- **Smoke 03/08:** credencial viva — exit NYC (Verizon) via curl; yt-dlp ponta a ponta via proxy rc=0 (Python e Node).
- **Helpers:** Python `Projeto Cafezinho Agentes/agents_labs/youtube_v2/util_proxy_iproyal.py` (agente YouTube) e TS `Outros/Aplicativos/MokaVideo/src/lib/iproyal.ts` (Moka Video) — sessão nova por chamada, telemetria unificada em `agent_data/v4_cafezinho_youtube/telemetria_proxy.jsonl` (campo `fonte`), decisão manter/desligar via `util_proxy_iproyal.py --resumo` (**revisão agendada 2026-09-02 09:00**).
- **Histórico operacional:** sessão antiga `afcasYEu` (21/05, falha Beijing/GFW); GNOME desktop 03/07 (PACER bloqueado pelo provedor → bypass `.gov`/`.gov.br`); AUTH-047 16/06 (YouTube destravado via IPRoyal).
- **Higienização 03/08:** `toggle_proxy.sh` não contém mais segredo em plaintext — lê do cofre.
- **Cascata multi-provedor (03/08 ~16:40):** `PROXY_RESIDENCIAL_2` e `PROXY_RESIDENCIAL_3` = slots dormentes nos cofres (vazios, documentados com candidatos). Ordem: direto → slot1 → slot2 → slot3. Ativar = colar URL do provedor contratado, zero código. Pesquisa de alternativas e testes: fórum/memória do dia.
- **Compliance (pesquisado 03/08):** ToS IPRoyal 4.2 permite uso comercial próprio (Moka Video OK); AUP 3.2 veda contornar controles de plataforma → risco = suspensão da **conta IPRoyal apenas** (Miguel: risco aceito, "conta descartável"). NetNut descartada da pesquisa (domínio apreendido FBI).
- **Não usar em:** servidores na China (GFW mata a conexão ao proxy) nem para destinos `.gov`.
- **Tema Duplo:** `Foruns/forum_iproyal_renovacao_fallback_youtube_20260803.md` + `Memorias/memoria_iproyal_renovacao_fallback_youtube_20260803.md`.

---

## 🔑 ROTAÇÃO DEEPSEEK POR CONSUMIDOR — 2026-08-03 (Miguel)

Velha `sk-9335f…de04` ("Antigravity Cafezinho") **REVOGADA** (401 confirmado) após o caso do consumidor invisível (US$ 142,38 oficiais × ~2% na telemetria — era o estúdio/navegador). Miguel criou 4 chaves por classe de consumo = **telemetria oficial por chave no painel DeepSeek**. Valores: NUNCA aqui; ler dos cofres. Backups pré-troca: `*.bak_dsk_20260803_*` ao lado de cada arquivo.

| Chave (fingerprint) | Classe | Onde está |
|---|---|---|
| `sk-493c…888f` ("V4CAFE") | Agentes V4 Cafezinho | NYC: `/root/chaves.sh`, `/root/chaves_novas.env`, `/root/cicero_remote/root/chaves_cicero.env` · Tencent: `/home/ubuntu/chaves_novas.env`, `/home/ubuntu/root_copy/.env` · Local: `Projeto Cafezinho Agentes/root/.env.unificado` (`DEEPSEEK_API_KEY`), `Cicero Agentes/root/chaves_cicero.env`, `Outros/chaves/cafezinho_root/chaves.sh` |
| `sk-e36d…96ba` ("TEMÁTICOS") | Sites temáticos | Local: `Projeto Cafezinho Agentes/root/chaves_novas.env`, `Rio Carta Agentes/root/chaves_riocarta.env`, `Global South News/root/chaves_gsn.env` |
| `sk-7cb6…e41d` ("OUTROS") | Legados/misc/moka | `Outros/legacy_.env`, `Outros/chaves/*/legacy_chaves_novas.env`, `Outros/chaves/agentes_labs/chaves.sh`, NYC `/root/legacy_chaves_novas.env`, Tencent `/root/legacy_chaves_novas.env`, moka `/home/ubuntu/moka/pontos_api/.env` · var reserva `DEEPSEEK_API_KEY_OUTROS` no `.env.unificado` local |
| `sk-ab79…412a` ("CLAUDE") | Uso exclusivo do Claude Code ("se ele quiser") | var `DEEPSEEK_API_KEY_CLAUDE` no `.env.unificado` local (não é default de nada) |

**Testes rápidos:** `curl -s -o /dev/null -w "%{http_code}" https://api.deepseek.com/chat/completions -H "Authorization: Bearer $<var>" -H "Content-Type: application/json" -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"ok"}],"max_tokens":2}'` → 200 = viva · 401 = morta.
**Notas:** (1) curador `youtube_cafezinho.py` lê `DEEPSEEK_API_KEY` direto do `.env.unificado` (V4CAFE) — a cadeia `get_key` resolve TEMÁTICOS por precedência (Cirurgia F2 do Cofre Único trata). (2) Vigia local checa saldo da CONTA 1×/dia + divergência oficial×interno > US$ 1 → alerta. (3) A chave velha morreu: qualquer erro 401 DeepSeek = arquivo não mapeado → procurar `9335f` e aplicar a classe certa.

---

## 📥 SEGREDO / COFRE INTAKE — entrega local de chaves sem expor no chat (v2, 2026-08-16)

**Problema resolvido:** chave colada no chat vira semi-exposta (transcrições). O intake é um cofre local fora de TODO sync (não vai p/ GitHub/Tencent/B2).

**Interface v2:** o atalho agora se chama **“🔐 Segredo — guardar uma
chave”**. A janela pede somente:

1. nome humano para reconhecer a chave;
2. origem/serviço (GitHub, OpenAI, Mistral etc.);
3. valor da chave, em campo oculto.

O programa cria o identificador técnico automaticamente, mostra uma tela de
confirmação sem revelar o valor e registra apenas uma impressão SHA-256 curta.
Não registra mais começo ou fim do segredo. O formato
`~/cofre_intake/cofre_intake.env` foi preservado para compatibilidade com os
agentes; os metadados sem valor ficam em `cofre_intake.meta.tsv`. Diretório e
arquivos continuam 700/600 e fora de todo sync.

**Protocolo:**

1. Miguel abre o atalho ou executa `~/bin/cofre_intake.sh --gui`.
2. Depois avisa no chat somente: “coloquei ‘NOME’, de ‘ORIGEM’, no Segredo”.
3. O agente localiza o identificador por `--status`/`--list`, faz a operação
   autorizada e valida o resultado sem imprimir o valor.
4. Após o uso, remove só aquela entrega com `--remove IDENTIFICADOR`. `--clear`
   destrói todas as entregas temporárias e deve ser usado apenas quando isso for
   intencional.
5. `--status` e `--list` nunca mostram o segredo: somente nome, origem,
   identificador e impressão criptográfica.

**Regra permanente:** valor de chave NUNCA em chat/canal/fórum — só via
Segredo/intake (ou direto no arquivo de cofre, quando Miguel edita
manualmente). A impressão SHA serve para conferir identidade; não é o valor da
chave. O intake é temporário e não substitui o chaveiro/cofre definitivo.


---

## 🔐 ESPELHO SMTP_MOKA_* executado (2026-08-07 ~11:45 BRT, ZCode/Kimi K3 — 1º caso da Regra Nº 4/§117)

- **Desencontro encontrado:** `SMTP_MOKA_HOST/PORT/USER/PASSWORD` existiam só em `Projeto Cafezinho Agentes/root/.env.unificado` (gravadas 06/08 ~14:35) e faltavam em `Outros/chaves/agentes_labs/.env.unificado` (citado pelo doc-master do Moka como canônico p/ chaves de agentes).
- **Ação (autorizada pelo Miguel: "sim, pode espelhar"):** 4 chaves espelhadas → verificação por hash md5 ✅ idênticas nos 2 cofres (valores nunca exibidos). Backup: `.env.unificado.bak_pre_espelho_smtp_20260807`.
- **Regra nova canonizada no mesmo ato:** **Regra Nº 4 / §117** — credenciais sempre espelhadas e atualizadas; credencial velha inútil = jogada fora (do vivo) e substituída, sem perguntar; backup datado preserva histórico. Registrada em `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` §117 + `~/.zcode/AGENTS.md` (REGRA Nº 4).
- **Pendente (do SMTP Moka, lembrete):** colar o SMTP no Supabase Dashboard (ação do Miguel) + recomendação de trocar a senha no GoDaddy (trafegou no chat em 06/08).


---

## 🔐 MOKA TWA — keystore de assinatura Android (2026-08-07, ZCode/Kimi K3)

**O quê:** keystore do app Android `com.mokareader.app` (TWA do Moka Reader p/ Play Store). Cert CN=Moka Reader App / O=Cafezinho Media Group / C=BR, válido até 2081. **Se perder, o app nunca mais atualiza na Play — tratar como credencial máxima.**

**Onde (espelhado nos dois cofres, Regra §117):**
- `Projeto Cafezinho Agentes/root/keystores/moka_twa/android.keystore` (perms 600)
- `Outros/chaves/agentes_labs/keystores/moka_twa/android.keystore` (idêntico, md5 `f513439e…`)
- Cópia de trabalho (gitignored): `Moka-Lab/apps/twa/android.keystore`

**Chaves nos `.env.unificado` (ambos cofres):** `MOKA_TWA_KEYSTORE_PASSWORD` (usada também como senha da chave; sha256[:12] `431d7ddfd19f` nos dois), `MOKA_TWA_KEY_ALIAS=android`, `MOKA_TWA_PACKAGE_ID=com.mokareader.app`, `MOKA_TWA_KEYSTORE_PATH`. Backups pré-espelho: `.env.unificado.bak_pre_espelho_moka_twa_20260807`.

**Como usar:** `source ~/moka-twa-env.sh` + exportar `BUBBLEWRAP_KEYSTORE_PASSWORD`/`BUBBLEWRAP_KEY_PASSWORD` (lendo do cofre) e rodar `bubblewrap build` em `apps/twa`. Fingerprint público (assetlinks): `9A:BB:E0:F1:3A:05:15:4F:68:E8:AD:2B:4C:4E:B9:20:CD:33:43:81:23:82:3B:4F:21:EA:3B:1C:35:95:44:26`.

## 🔐 Z.AI CODING PLAN (GLM-5.2) — assinatura Max no ZCode (2026-08-07, ZCode/GLM-5.2)

**O quê:** chave da assinatura Coding Plan do Miguel (modelos `glm-5.2`, `glm-5-turbo` etc.), configurada no ZCode após o diagnóstico de endpoint errado (provider "Z.ai API" apontava p/ pay-as-you-go → erro `1113`; corrigido p/ endpoint de assinatura `/api/coding/paas/v4` e Anthropic-native `/api/anthropic`).

**Variável de cofre:** `ZAI_CODING_PLAN_API_KEY` — `sha8=084efcbd` (antes nenhuma chave Z.ai/Zhipu constava do cofre unificado). Cabeçalho no `.env.unificado` documenta: assinatura Max, modelos glm-5.2/glm-5-turbo, espelho ZCode 07/08/2026.

**Onde (espelhado nos 2 cofres, Regra 4):**
- `Outros/chaves/agentes_labs/.env.unificado` · `Projeto Cafezinho Agentes/root/.env.unificado`
- Backups `.bak_pre_zai_glm52_20260807_1353`. **Pendente:** espelho Tencent/NYC (só se usar GLM via Coding Plan fora do ZCode).

**No ZCode (`~/.zcode/v2/config.json`):** 3 providers Z.ai ativos com a chave nova (`084efcbd`) — `e488030c…` ("Z.ai API", OpenAI-compatible, endpoint coding), `builtin:zai-coding-plan` (Anthropic-native, `enabled:true`), `builtin:zai` (Anthropic-native). Backup config: `.bak_pre_zai_glm52_config_20260807_1353`.

**Chaves velhas descartadas do config (Regra 4 — histórico no backup, não no vivo):** `0e3373ea` (`builtin:zai-coding-plan`) e `bf908cec` (`builtin:zai`, conta $0 desde 25/07).

**Não tem API de quota** (sondados 11 endpoints → todos 404; mesmo padrão Kimi) → monitorada na Vigília de Crédito por consumo de tokens. Detalhe: `Foruns/forum_config_glm52_zai_coding_plan_vigilia_20260807.md` + `Memorias/memoria_config_glm52_zai_coding_plan_vigilia_20260807.md`.

## 🔐 Z.AI GLM PRÉ-PAGO (pay-as-you-go) — chave VIVA desde 19/09/2026 (ZCode/Kimi K3, ordem do Miguel)

**O quê:** Miguel colocou saldo na Z.ai e gerou chave PRÉ-PAGA nova (sha8 `d0f53631`). O Coding Plan (assinatura Max) **EXPIROU** — endpoint Anthropic `/api/anthropic` devolve 429/1303→1309 e NÃO aceita pré-pago. Caminho vivo GLM = **OpenAI-compatible `https://api.z.ai/api/paas/v4`**.

**Variável de cofre:** `ZAI_PREPAGO_API_KEY` (+ `ZAI_PREPAGO_BASE_URL`) — espelhada 19/09 em: Dell (`Projeto Cafezinho Agentes/root/.env.unificado` ⇄ `Outros/chaves/agentes_labs/.env.unificado`) e Tencent (`/root/.env.unificado`; consumidores vivos `/root/.env` e `/home/ubuntu/cafezinho/redes/.env_redes` rotacionados p/ a chave nova + base `/api/paas/v4`). Backups `.bak_pre_glm_prepago_20260919_1548`.

**Mortas (401 provado 19/09):** `ZAI_API_KEY`/`GLM_API_KEY` antigas (prefixo 4d8ae2...) → `_DEPRECADA_20260919` nos cofres de referência. `ZAI_CODING_PLAN_API_KEY` mantida (revive se a assinatura for renovada).

**No ZCode:** provider "Z.ai API — PRÉ-PAGO" (GLM-5.3/GLM-4.6/GLM-4.5-Flash) configurado; `builtin:zai`/`builtin:zai-coding-plan` desativados (chaves mortas). Detalhe: Foruns/forum_glm_prepago_config_zcode_20260919.md + Memorias/memoria_glm_prepago_config_zcode_20260919.md.

## 🔐 ZCODE_OPENAI (GPT-5.6 Sol) — chave OpenAI dedicada ao ZCode (2026-08-25, ZCode/GLM-5.3)

**O quê:** chave `sk-proj` nova criada pelo Miguel na plataforma OpenAI, **dedicada ao ZCode** (separada da `OPENAI_API_KEY` de produção, sha8 `f6a7d97d`). A conta enxerga 126 modelos incl. `gpt-5.6-sol`/`-terra`/`-luna`. Smoke ao vivo 25/08: HTTP 200 (Sol respondeu "OK", 16/4 tokens).

**Variável de cofre:** `ZCODE_OPENAI_API_KEY` — `sha8=8035a022` · origem: `~/cofre_intake/cofre_intake.env` (lá chama-se `ZCODE_OPENAI`).

**Onde (espelhado nos 2 cofres, Regra 4):** `Outros/chaves/agentes_labs/.env.unificado` · `Projeto Cafezinho Agentes/root/.env.unificado` — backups `.bak_pre_zcode_openai_20260825`.

**No ZCode (`~/.zcode/v2/config.json`):** provider **"OpenAI (GPT-5.6)"** (`6ff9b527-db32-44ee-a0e4-0030d69853a2`, kind **`openai`** — era `openai-compatible` até 25/08 ~13:20, quando o ADENDO 1 do fórum da estratégia corrigiu o 400 `max_tokens`; baseURL `https://api.openai.com/v1`, modelos `gpt-5.6-sol`/`-terra`/`-luna`, contexto 1M / saída 128K; override reasoning habilitado p/ o Sol). Backup config: `.bak_pre_openai_gpt56_20260825_1251` + `.bak_pre_openai_kind_fix_20260825_1315`.

**Atenção:** preço do Sol é **PROMOCIONAL garantido até ≥21/11/2026** (regular não divulgado — reler em novembro); crédito da conta é o mesmo pote da produção V4 (superprodução já queimou US$ 39/5d) — política: Sol como luxo sob demanda, nunca em pipeline sem teto. Preços/catálogo: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` §GPT-5.6.

## 🔐 COFRE SSH CIFRADO EM 3 DESTINOS — 2026-08-22 (ZCode/GLM-5.3, ordem do Miguel)

**O quê:** cofre GPG simétrico (AES-256, SHA-512, s2k-count máx.) com as 4 chaves privadas SSH do Dell (`id_rsa`, `id_ed25519`, `id_ed25519_gsn`, `id_ed25519_manus` + pubs + config) e a senha root do WP (`Outros/chaves/ssh_servidor_wp_cafezinho.md`). **A passphrase NÃO existe em arquivo nenhum** — só na cabeça do Miguel ou via `COFRE_PASS` numa sessão de agente (protocolo palavra-ao-LLM: `abrir` em /dev/shm → usar → `fechar` → `esquecer` limpa os transcripts `~/.zcode/cli/{rollout,log}/*.jsonl`).

**Onde (blob `cofre_ssh_v1.tar.gpg`):** `Cerebro/Cofres/cofre_ssh/` (sobe ao GitHub pelo trilho) · pendrive 2079-8A26 `cofre_segredos/` · GDrive `drive:Cofres/cofre_ssh/`. Espelhar/conferir: `bash Cerebro/Cofres/cofre_ssh/cofre_ssh.sh status`.

**Ferramenta:** `Cerebro/Cofres/cofre_ssh/cofre_ssh.sh` (selar/abrir/fechar/verificar/trocar-palavra/esquecer/espelhar/status/sugerir/selftest). Protocolo completo no `LEIA-ME.md` da pasta.

**Regras permanentes:** palavra do cofre NUNCA em fórum/memória/commit/Telegram (só `COFRE_PASS` do comando); abrir só em /dev/shm; fechar após o uso; `esquecer` no fim da sessão e de novo após fechar o app. Blob CIFRADO no git ≠ violação da lição SEV-1 (que vedava credenciais EM CLARO em checkout).

**Estado:** pronto e provado (selftest + 3 canais com blob demo); blob real nasce quando o Miguel rodar `selar` (palavra em campo oculto, não passa pelo chat). Pendências Miguel: selar → conferir `status` → apagar pastas em claro do pendrive (`chaves ssh/`, `ssh_cafezinho_2026-08-19/`) → (recomendado) rotação das chaves do SEV-1.

**Tema Duplo:** `Foruns/forum_cofre_ssh_criptografado_3destinos_20260822.md` + `Memorias/memoria_cofre_ssh_criptografado_3destinos_20260822.md`.



**O quê:** rotação completa da `MISTRAL_API_KEY`. Conta anterior `migueldorosario@gmail.com` desativada (HTTP 402 Payment Required); conta nova `migueldorosario2@gmail.com` ativa. Chave nova gerada pelo Miguel (label "cafezinho-vibe" no console Mistral) e depositada via **Cofre Intake** (`~/cofre_intake/`, GUI zenity) — nunca passou pelo chat.

**Variável de cofre:** `MISTRAL_API_KEY` — sha8=`3e6e7b7f` (nova), substitui `142dd612` (velha, HTTP 402/conta desativada).

**Smoke test da nova (09/08 05:42 BRT):** `GET /v1/models` → HTTP 200 (53 modelos); `POST /v1/chat/completions` mistral-small-latest → HTTP 200, resposta "56" (7×8). ✅ funcional.

**Onde espelhada (5 cofres vivos, Regra 4/§117 — verificada por fingerprint `3nhqpXk8…9e4O` em todos):**
- `Outros/chaves/agentes_labs/.env.unificado` · `.env_root` · `chaves.sh`
- `Outros/chaves/cafezinho_root/chaves.sh`
- `Projeto Cafezinho Agentes/root/.env.unificado`

**Backups pré-rotação:** `.bak_pre_mistral_rot_conta2_20260809_0543` em cada cofre acima (chave velha preservada no histórico, fora do vivo). Pasta legacy `Outros/chaves/legacy/20260809_mistral_conta_nova/` já continha a rotação de conta (manifest.tsv).

**Intake:** valor destruído pós-deploy (`cofre_intake.sh --clear`); histórico de nomes preservado em `intake.log`.

**Mistral Vibe CLI:** instalado (`uv tool install mistral-vibe`, v2.24.0) — config `~/.vibe/config.toml` lê `api_key_env_var = "MISTRAL_API_KEY"`. Modelo ativo `mistral-medium-3.5`. Logs pré-rotação mostravam HTTP 402 (chave velha); agora resolve via env. `~/.vibe/.env` vazio (vazio por design — a chave vem dos cofres/ambiente).

### App password "Integracoes-Autoria" — API de autoria do canônico (22/08/2026, ZM sprint Mapa de Sinais)

**O que é:** Application Password WP (usuário 5786 "Redacao nova") que autentica o endpoint `GET https://www.ocafezinho.com/wp-json/cafezinho/v1/autoria` (classificação de autoria dos posts — mu-plugin `cafezinho-origem-post.php`). Consumidores: Painel CCTV `/v6/autoria` e Baleia Azul (seção diária) + qualquer agente dos loops (uso livre de auditoria). sha8(sha256-8) da senha: `07245eb4`.

**Variáveis (trio `AUTORIA_API_URL` / `AUTORIA_WP_USER` / `AUTORIA_WP_PASS`) — destinos:**

| Cofre | Caminho |
|---|---|
| Local (Dell) | `Projeto Cafezinho Agentes/root/.env.unificado` + espelho `Outros/chaves/agentes_labs/.env.unificado` |
| Tencent (ubuntu) | `/home/ubuntu/.env.unificado` + cópia operacional do painel `/home/ubuntu/cafezinho/v6/.wp_creds` |
| Tencent (root) | `/root/.env.unificado` |
| NYC | `/root/.env.unificado` |
| Canônico (ServerDo) | `/root/.autoria_apppass` (600 — cópia-mestre do wp-cli) |
| Alibaba | ⚠️ PENDENTE — ssh `Permission denied` (mesma pendência de host key desde 16/08) |

**Backups:** `.bak_pre_autoria_20260822` ao lado de cada arquivo. **Teste sem expor segredo:** `curl -s -o /dev/null -w '%{http_code}' -u "Redacao nova:$(grep '^AUTORIA_WP_PASS=' <cofre> | cut -d= -f2-)" "https://www.ocafezinho.com/wp-json/cafezinho/v1/autoria?horas=1"` → `200` (sem auth → `401`). Incidente de geração: a 1ª senha vazou no stdout da sessão → revogada e recriada redirecionada direto para arquivo (registrado em `Foruns/memoria_mapa_sinais_integracoes_baleia_cctv_20260822.md`).
**Atualização 22/08 ~10:50:** + vars `AUTORIA_PAINEL_URL/USER/PASS` (Basic Auth nginx da página `/v6/autoria` do CCTV — user `cafezinho`, htpasswd `/etc/nginx/.htpasswd_autoria` no Tencent) nos mesmos cofres do trio AUTORIA_* + `.wp_creds` (backups `.bak2_pre_painel_autoria_20260822`).

## 🗺️ MAPA RCLONE DO DELL (nuvens — indexado 23/08/2026 ~01:05 pelo ZCode/GLM-5.3; ordem do Miguel "procura, acha e indexa")

**Config:** `~/.config/rclone/rclone.conf` (12 remotes). **Nomes e escopos apenas — valores nunca.**

| Remote | O que é / enxerga |
|---|---|
| **`gdrive-backup-b2`** | ⭐ **REMOTE MESTRE B2** (chave multi-bucket) — vê TODOS os 17 buckets: `cafezinho-backups` (cofre padrão de backups do ecossistema), `Cerebro-Memorias`, `backup-total-local-2026`, `Backup-GoogleDrive-Miguel`, `Cafezinho-operacional`, `Agents-Labs-Cafezinho`, `site-tematicos`, `Orlando-Diniz-Dossie`, `mayra-brain`, `bancodemidiageral`, `processador-imagens-cafezinho`, legados e `failover-cafezinho1` |
| `gdrive:` = `drive:` | **Google Drive 30TB** (espelho do Cérebro; backups em `Cerebro_Backups/`) |
| `b2:` e `masterb2` | ⚠️ chaves RESTRITAS ao bucket `failover-cafezinho1` (NÃO servem p/ backups gerais — causa da confusão em 23/08) |
| `b2-labs` | restrito a `Agents-Labs-Cafezinho` |
| `b2-tematicos` | restrito a `site-tematicos` |
| `b2_orlando` | restrito a `Orlando-Diniz-Dossie` |
| `r2` | Cloudflare R2 (S3) |
| `legacy-cafezinho` · `reforma_tencent_cafezinho` | legados das reformas |

**Regra prática:** backup geral de projeto → `gdrive-backup-b2:cafezinho-backups/<PASTA>/` **e** `gdrive:Cerebro_Backups/<PASTA>/` (dupla nuvem, como o Cérebro manda). Exemplo 1º uso: backup do portal LOGIS em 23/08 (tarball `ec87d06` nas duas nuvens). NOTA: `~/cerebro-miguel/cofres_laura/rclone/rclone.conf` NÃO existe no checkout local do Dell (confere no repo GitHub se precisar da config da Laura).

### 📅 Google Agenda — OAuth `logis-agenda` (24/08/2026, ZCode/GLM-5.3)
- **Cofre:** `Outros/chaves/Google Agenda/` — `logis_calendar_client.json` (client OAuth Desktop criado pelo Miguel no Cloud Console; status Teste, sem verificação) + `logis_calendar_token.json` (access + **refresh_token**, chmod 600). Valores jamais expostos em chat/fórum.
- **Escopos:** `calendar.events` + `calendar.readonly` — escrita de eventos e leitura. 7 calendários da conta visíveis; destino padrão = calendário principal.
- **Scripts:** `logis/scripts/google_calendar_login.py` (login loopback porta 8901; `--teste` valida; `--refresh` renova access) e `logis/scripts/google_agenda_ils.py` (sincroniza Programa de Ação do ILS; idempotente).
- **Renovação:** refresh_token não expira enquanto o app ficar em status Teste **com o usuário de teste ativo**; se o Google aposentar, reabre o login. Clientes OAuth inativos 6 meses podem ser deletados pelo Google (aviso por e-mail ao dono do projeto).
- Nota: o segredo já circulou 1× no chat (Miguel colou a tela "Additional information" 24/08 14:28) — risco baixo (app Teste, sem domínio), mas o padrão permanece: colar só o JSON no cofre, nunca o valor no chat.

## Cofre FAROL (24/08/2026)

- `Cofres/cofre_farol/acesso_farol.txt` — login/senha da pagina 🛡️ FAROL (`/v6/audiencia-redundante`, auth_basic nginx no Tencent). Valor NUNCA em chat/fórum (exceção única: entrega direta ao Miguel no chat em 24/08 a pedido dele).

### Atualização 25/08/2026
- DEEPSEEK_API_KEY (cafezinho canônico): nova chave sk-f6f1c***8762 (plataforma: "Cafezinho Canonico", ID c8d5281d-ed81-4313-9d0f-3987dba93768, criada 24/08) espelhada nos 3 .env.unificado com backup; antiga e36d25 revogada e fora dos cofres vivos.
- QWEN_API_KEY (25/08): nova workspace key sk-ws-H.DMXII*** ("chave cafezinho canonico", Default Workspace, host ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com) — testada 200 nos endpoints workspace E dashscope-intl; espelhada nos 3 .env.unificado (backups .bak_pre_qwen_ws_20260825); monitor ✅ (detectou fingerprint novo). Antiga principal ("migueldorosario") preservada em backup; QWEN_API_KEY_2 (ws-aduzgn, 403) candidata a aposentadoria.

### 🧹 Varredura de chaves velhas (25/08 10:20, ordem Miguel — Regra Nº 4 item 2)
**Removidas dos cofres VIVOS (testadas 401 = mortas; preservadas em .bak_pre_limpa_20260825):**
- `DEEPSEEK_API_KEY_CLAUDE` (ab79ae) — dos 2 .env.unificado (Dell)
- `DEEPSEEK_API_KEY_OUTROS` (7cb691) — dos 2 .env.unificado; no gateway moka (pontos_api/.env tencent) renomeada `_DEPRECADA_20260825`
**Corrigida a mais grave:** `.env` principal dos agentes (Antigravity Google) rodava com a DeepSeek VELHA revogada (e36d25) → atualizada pra nova (f6f1c). Robôs que carregam esse .env voltaram a ter DeepSeek válida.
**Recuperada:** `QWEN_API_KEY_2` estava viva (200 no intl!) — o 🔑 do monitor era endpoint_override de workspace morto no mapa; removido (estrutura real: providers.qwen) → monitor agora ✅ nas duas.
**Confirmados limpos:** tencent /root/.env.unificado (nova), NYC chaves.sh (nova). Nota: droplet 159.89 usa chave própria (9335) não testada — flag pra próxima.

### 🌙 LUMINA — Matomo 5 (3º medidor de audiência §118, instalado 26/08/2026)
- **Cofre:** `cafezinho-wp:/root/lumina_cred/lumina.txt` (600 root) — superusuário `miguel_lumina` + senha + email + notas do banco
- **Instância:** `https://ocafezinho.com/lumina/` (self-hosted, PHP 8.3, banco compartilhado c/ WP prefixo `matomo_`)
- **Endpoint CCTV:** `cafezinho-wp:/var/www/ocafezinho/lumina/lumina_resumo.php` — token sha256 no PHP; plaintext em `tencent:/home/ubuntu/cafezinho/v6/lumina_token` (600 ubuntu)
- **Como testar:** painel `/v6/lumina` no CCTV + login no Matomo com o cofre acima

### ▶️ YouTube Data API v3 — MOKA (27/08/2026)
- **Chave:** `ZCODE_MOKA_YOUTUBE` (AIzaSy…) criada pelo Miguel no Google Cloud Console (projeto "GA4 e YouTube", gen-lang-client-0314850052). Depositada no `~/cofre_intake/cofre_intake.env` e espelhada nos 2 `.env.unificado` (backups `.bak_pre_youtube_moka_20260827`; sha8=8b37fadc nos 3 conferem).
- **Uso na Vercel:** env `YOUTUBE_API_KEY` (encrypted, production+preview) nos 3 projetos Moka (ousadia prj_cAXX…, espelho prj_Gt8y…, canônico prj_fwv…). Server-side apenas (`route.ts` do ingest) — nunca no bundle client.
- **O que dá:** videos.list/search.list/captions.list (1/100/1 unidade; cota 10.000/dia). NÃO dá captions.download (401 OAuth — Google só libera download de legenda com OAuth). A transcrição em si vem do innertube (sem chave) + proxy residencial — ver fórum de 27/08.
- **Como testar:** `curl "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=<ID>&key=$ZCODE_MOKA_YOUTUBE"` → 200 com título/canal.

### 🆔 Dados pessoais dos fundadores do ILS (28/08/2026, ZCode/GLM-5.3)
- **Cofre:** `Outros/Projeto Casa da Moeda/instituto/COFRE_DADOS_FUNDADORES.md` (chmod 600) — qualificação civil completa do presidente (nome, nacionalidade, estado civil, profissão, RG DETRAN-RJ, CPF, endereço) extraída da procuração; vice (Priscila) pendente com o Miguel. **Valores jamais em chat/fórum/código** — este nodo só aponta o caminho (padrão do Cofre).
- **Origem/redundância:** procuração original na raiz do Google Drive do Miguel (`PROCURAÇÃO - MIGUEL DO ROSÁRIO.docx`) — backup natural dos dados.
- ⚠️ **NÃO copiar este cofre para dentro de `Cerebro/`**: o sync de 15 min empurra a pasta Cérebro ao GitHub — RG/CPF completos não sobem pra nuvem sem criptografia. Se o Miguel pedir espelho: zip/gpg com senha e guardar a senha noutro cofre.

**📑 ÍNDICE DO GDRIVE (28/08/2026):** mapa navegável das áreas do Google Drive do Miguel (30 TB, 101.682 arquivos) em `Cerebro/Dados/GDRIVE/INDICE_GDRIVE_2026-08-28.md`; inventário completo em `Outros/indices/GDRIVE_inventario_completo_2026-08-28.txt` (fora do sync GitHub). Busca: grep no inventário → rclone copy com --include (nomes NFD).

**📑 GDRIVE POR ÍNDICE v2 (30/08/2026) — SUPERSEDE O DE 28/08:** inventário de 28/08 estava TRUNCADO (101.682; Backup_Total listava 2.888 de ~60k — `lsf --recursive` único perde páginas). **Definitivo:** `Outros/indices/GDRIVE_inventario_completo_2026-08-30.txt` (675.247 arquivos; método pasta-a-pasta `--fast-list` + 6 workers + sort -u). **Buscador oficial:** `python3 "Outros/indices/busca_gdrive.py" <termo> [--livros|-e ext|-p pasta]`. **Biblioteca:** catálogo `Outros/indices/GDRIVE_biblioteca_catalogo_2026-08-30.csv` (2.778 livros únicos; cascata Livros/×10 = 66k arquivos) + 62 fichas em `Outros/indices/biblioteca_fichas/`. **Obras do Miguel (FdI/Origens/Curso/Singularidade):** `Cerebro/Dados/GDRIVE/OBRAS_DO_MIGUEL_2026-08-30.md`. ⚠️ Na raiz do Drive: `login- migueldorosario@gmail.docx` e `Senhas nova 6 abril 2026.docx` — candidatos a COFRE (nunca exibir). Tema Duplo 30/08.

### 🔐 Senha do DeepSeek Harness web no NYC (29/08/2026, ZCode/Qwen 3.8)
- **O quê:** basic auth (usuário `miguel`) do harness DSH exposto em `dsh.ocafezinho.com` (backend 127.0.0.1:3080 no NYC). O DSH não tem login próprio — essa senha É o controle de acesso a um agente que executa código.
- **Onde mora (espelhada nos 3 cofres, Regra Nº 4):** chaves `DSH_WEB_USER`/`DSH_WEB_PASSWORD` em `Projeto Cafezinho Agentes/root/.env.unificado` ⇄ `Outros/chaves/agentes_labs/.env.unificado` ⇄ NYC `/root/.dsh/dsh_web_auth.env` (chmod 600); hash aplicado no nginx em `/etc/nginx/.htpasswd_dsh` (bcrypt, 640). Backups pré-espelho: `.bak_pre_dsh_nyc_senha_20260829` nos dois cofres locais.
- **Como testar (sem expor valor):** `curl -u miguel:<senha> https://dsh.ocafezinho.com/` → 200; sem senha → 401. Conferência de espelho por md5 da linha `DSH_WEB_PASSWORD` (sha8 na época: `859b500b`).
- ⚠️ Trocou a senha → refazer o htpasswd no NYC (`htpasswd /etc/nginx/.htpasswd_dsh miguel`) E atualizar os 3 cofres na mesma ação.

### 🔑 Deploy key do espelho NYC da ponte — Camada 2 Emenda Ponte v2 (29/08/2026, ZCode/Qwen 3.8)
- **O quê:** chave SSH dedicada para o bare repo `/home/ubuntu/cerebro-miguel-mirror.git` no servidor `nyc` (198.199.121.136) espelhar o repo `cerebro-miguel` no GitHub (reconciliação NYC→GitHub pós-queda).
- **Onde mora:** PRIVADA = `/root/.ssh/nyc_mirror_github` (só no nyc, 600 — não sai de lá, não vai pra cofre nenhum); PÚBLICA = deploy key do GitHub id `161683269` (`nyc-cerebro-mirror-camada2`, escrita liberada). Fingerprint: `SHA256:3xt76w1MpV9WpzDelnYdQIs+mjrHtdVZlfJh1+oJybo` (ED25519).
- **Como testar (sem expor nada):** no nyc, `cd /home/ubuntu/cerebro-miguel-mirror.git && git ls-remote github main` → deve devolver o mesmo sha do `git ls-remote origin main` no Dell.
- **Trocou/revogou:** deletar a deploy key no GitHub (Settings → Deploy keys, id 161683269) + remover o par no nyc + atualizar esta seção na mesma ação. Backup do crontab pré-instalação: `/root/crontab.bak_pre_mirror_nyc_20260829`.


## 📲 TELEGRAM_TOKEN_DSC_BOT + DSC_BOT_CHAT_ID (30/08/2026, DSC)

- **Onde:** `.env.unificado` (espelhamento constitucional — us65 ✅; Tencent/NYC/Alibaba: espelhar na próxima sincronização)
- **O que é:** token do bot **@dscelular_bot** (Telegram = 2ª via do Miguel + TERMINAL do DSN) + chat_id do Miguel
- **Escopo:** enviar e LER mensagens do chat privado Miguel↔bot (getUpdates = terminal de entrada)
- **Regras:** assinar TODA mensagem (quem + AAAAMMDD HH:MM:SS BRT) — ordem Miguel DSC-012; valor nunca em fórum/commit/ponte

## [30/08/2026 14:20 BRT · ZM] TELEGRAM_TOKEN_DSC_BOT + DSC_BOT_CHAT_ID (terminal Telegram do DSN, refs DSC-016/023)
**Onde moram:** Tencent `/home/ubuntu/.env.unificado` (o que a ronda DSN lê) e `/root/.env.unificado`; espelhos Dell (Regra 4): `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado`. Backups `.bak_pre_dsc_bot_20260830_*`. **Verificar por NOME de chave + sha8 (printf '%s' sem \n) — nunca exibir valor (§82).** Teste vivo = sendMessage (ok=True). ⚠️ getUpdates do bot é EXCLUSIVO do daemon `dsc-minibot.py` (cafezinho-wp) — nenhum outro agente pode consumir. Fórum: forum_dsc_credencial_terminal_telegram_20260830.

## 📱 ACESSOS DOS AGENTES DS (harness) — seção organizada em 31/08/2026 pelo DSC (ordem do Miguel)

Objetivo: o Miguel nunca mais fica sem saber como entrar em cada DS. **Valores nunca aqui — só ponteiros.** Cada DS é responsável pela sua linha (atualizar quando mudar).

| DS | Máquina | Como o Miguel entra | O que existe de credencial | Onde mora o VALOR |
|---|---|---|---|---|
| **DS Celular (DSC)** | us65.serverdo.in | GUI `http://127.0.0.1:3080` (túnel local) — sem senha de interface; acesso = SSH do servidor | `DEEPSEEK_API_KEY` + `ZAI_API_KEY` (APIs do harness) + SSH root do servidor | `/root/.dsh/deepseek_env` (600) · SSH root: `Outros/chaves/ssh_servidor_wp_cafezinho.md` (gitignored) |
| **DS Miguel (Décio)** | Dell | sessão DSH local (harness, usuário `migueldorosario` no Dell) — sem GUI; Miguel fala comigo via Telegram/ponte cafezinho | `deepseek_env` (API do harness) + `ponte_amizade_env` (credencial da ponte) + `settings.yaml` (config) | `~/.dsh/` no Dell (`deepseek_env` 600, `ponte_amizade_env` 600) · cofre_intake · espelho `drive:espelho-zcode/ds_memoria/` |
| **DS Laura** | PC Laura | GUI local `http://127.0.0.1:3080` (harness DSH) + headless `dsh.cmd --profile headless` (ronda Task Scheduler `DS_Laura_Ronda`) — sem senha de interface; acesso = sessão/desktop do PC Laura | `DEEPSEEK_API_KEY` (perfil `DEEPSEEK_DS_LAURA`) do harness | `C:\Users\migue\.dsh\deepseek_env` (linha `DEEPSEEK_API_KEY=`) · cofre_intake → pendrive `2079-8A26` (`DS_LAURA_CHAVE_NOVA_20260829.md`, sha8 `f1671e9b`) |
| **DS Nuvem (DS-N Chefe)** | Tencent 43.156.151.165 | via SSH/ponte (sem GUI) | LLM keys do harness (9 providers): `~/.dsh/llm_env` + `~/.dsh/deepseek_env` · Telegram do DSN: `TELEGRAM_TOKEN_DSC_BOT`/`DSC_BOT_CHAT_ID` em `/home/ubuntu/.env.unificado` (só leitura; getUpdates é exclusivo do daemon) · SSH root Tencent (cofre GPG) · WP Cafezinho via alias `cafezinho-wp` + REST `WP_*_CAFEZINHO` no `.env.unificado` · repo da ponte `~/cerebro-miguel/` | `~/.dsh/llm_env` + `~/.dsh/deepseek_env` (600) · `/home/ubuntu/.env.unificado` · `cofre_ssh_v1.tar.gpg` (3 destinos) · `~/.ssh/config` (alias cafezinho-wp/tencent) |
| **DS iPad (?)** | ? | **A CONFIRMAR com o Miguel se existe** (31/08: termo veio por áudio, pendente confirmação) | — | — |
| **DS-N Publicador** | Tencent (cron 15/15, sem GUI) | automático; canal na ponte `Foruns/ponte_laura_completa/de_nuvem_publicador.md` (prova por publicação) | WP REST publicação: `WP_USER_CAFEZINHO`/`WP_PASS_CAFEZINHO`/`WP_SITE` (payload só status/date/featured_media) | herda `/home/ubuntu/.env.unificado` (linha DS-N Chefe acima) · código `~/dsn_publicador/` · seeds+estado locais · batizado 31/08 |
| **DS-N Ideias** | Tencent (cron 30/30 :13/:43, sem GUI) | automático; canal na ponte `Foruns/ponte_laura_completa/de_ideias.md` | **NENHUMA de WP** (Lei de Poderes: não publica; só LLM keys do harness + repo da ponte) | herda `~/.dsh/*` (LLM) · código `~/dsn_ideias/` · ideias em `Foruns/ideias/` · batizado 31/08 |
| **DS-N YouTube (DS YouTube)** | Tencent (cron 15/15 :07/:22/:37/:52) + porta de download no Dell (cron */5 — YouTube bloqueia IP datacenter) | automático; fila `Foruns/youtube/queue_youtube.md` + canal `Foruns/youtube/canal_ds_youtube.md` | WP REST **conta própria**: usuário 5801 `cafezinhodsn1` (editor) + app password (chave `WP_APP_PASSWORD_CAFEZINHO_DSN1`); LLM flash via `DEEPSEEK_CAFEZINHO_CANONICO`; yt-dlp/Whisper locais | `WP_USER/WP_APP_PASSWORD_CAFEZINHO_DSN1` em `/home/ubuntu/.env.unificado` + cofre Dell (backup `.bak_pre_dsyoutube_20260831`; sha8 c78617c2/2271fea3) · código `~/ds_youtube/` (Tencent) + `~/ds_youtube_fetcher/` (Dell) |

**Regra:** palavra de cofre/chave NUNCA via chat/Telegram (DSC-20260831-001);robôs não pedem segredo ao Miguel por chat; acesso novo = linha nova aqui + valor na máquina dona.

## Bot Astra — nomes e caminhos (05/09/2026, ordem direta Miguel)

Bot: @astrarevolution_bot, identidade conferida por getMe. Aliases TELEGRAM_TOKEN_ASTRA e TELEGRAM_ASTRA_NOVA acrescentados ao intake /home/migueldorosario/cofre_intake/cofre_intake.env e aos dois cofres irmãos locais Projeto Cafezinho Agentes/root/.env.unificado e Outros/chaves/agentes_labs/.env.unificado. Backups .bak_pre_astra_AAAAMMDD_HHMMSS, modo600, igualdade dos aliases verificada sem expor valores. MIGUEL_CHAT_ID continua referenciado por ponte_cafezinho/.env; não duplicado em registros. Consumidor exclusivo: ponte_astra/bridge.py quando ativado; não chamar getUpdates em paralelo. Bot do Chefe/ZCode intocados. Não há necessidade operacional de propagar este token aos servidores nesta fase. [Memória do setup](Memorias/MEMORIA_ASTRA_FASE0_20260905.md).

Adendo05/09 ~01:30: consumidor exclusivo ponte-astra.service efetivamente ativado no Dell e polling confirmado. Unit e logs de operação não contêm token. Não usar getUpdates em paralelo; nenhum bot alheio alterado. Resumo message_id5 entregue; memória guarda provas e reversão.
- 05/09/2026 20:4x · ZM — nova passphrase do lote02 de journals do Rio (alias `ZM_RIO_JOURNALS_LOTE02_20260905_PASSPHRASE`) espelhada nos cofres intake + agentes_labs + .env.unificado, com `.bak_pre_lote02_20260905` em cada; verificação por hash idêntico 3/3; valor nunca exibido. Uso: decifrar `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/zm_20260905_lote02/journals.tar.gpg`.

- 08/09/2026 14:1x→14:3x · ZM — **ROTAÇÃO Brave Search (`bravesearch-v4`)** por ordem do Miguel ("troca a chave do brave search em todos os cofres do cafezinho" + "ah primeiro testa ela"). Chave nova depositada por ele no cofre intake (`BRAVE_SEARCH_BRAVESEARCH_V4`, 14:08, sha12 `4512b7e0e824`, len 31) — **testada ANTES da troca: HTTP 200** em `api.search.brave.com/res/v1/web/search` (do intake + depois dos próprios cofres: Dell ×2, Tencent, NYC sem proxy). Rotacionada pela Regra 4 em **18 arquivos / 3 máquinas**, todos com backup `.bak_pre_brave_v4_20260908` (600) e verificação sha12 = `4512b7e0e824` em 18/18; valor nunca exibido. **Dell (5):** `Projeto Cafezinho Agentes/root/.env.unificado` + `root/chaves_novas.env` + `Outros/chaves/agentes_labs/.env.unificado` + `agentes_labs/chaves.sh` + `cafezinho_root/chaves.sh`. **NYC (7):** `/root/.env.unificado`, `/root/chaves.sh`, `/root/.env`, `/root/chaves_novas.env`, `/root/cafezinho/.env.unificado` + hardcoded em `/root/pesquisa_leilao_coleta_pura.py` e `/root/update_script_and_run.sh`. **Tencent (6):** `/home/ubuntu/.env.unificado`, `/home/ubuntu/chaves.sh`, `/home/ubuntu/chaves_novas.env`, `/home/ubuntu/pesquisa_leilao_coleta_pura.py` + `/root/update_script_and_run.sh` e `/root/pesquisa_leilao_coleta_pura.py` (via sudo; ssh lá = usuário `ubuntu`). **5 chaves VELHAS distintas aposentadas** (sha8): `0df143b7`, `17ee3b18`, `dc630dfe`, `481dfec9`, `892d6c46` — sobrevivem apenas em backups datados e arquivos `legacy_*` (histórico, intocados). Cobertura: cafezinho-wp NÃO tem chave brave; cafezinho-cm NÃO foi inspecionável (gateway ssh `command_denied`). 🔴 **ACHADO ESTRUTURAL (aguarda "vai"):** o `/root/chaves.sh` de NYC exporta proxy residencial IPRoyal (`geo.iproyal.com:12321`) e o `NO_PROXY` NÃO inclui `api.search.brave.com` → chamada Brave via proxy morre com `402 CONNECT tunnel failed` (provado ao vivo; sem proxy = 200 com a MESMA chave) — provável causa raiz do "brave intermitente" da auditoria DSN R1 (07/09). Correção sugerida: acrescentar `api.search.brave.com` ao `NO_PROXY`/`no_proxy` do `chaves.sh` NYC. Fórum: `Foruns/forum_unificacao_cofre_chaves_20260801.md` (adendo 7).
- ➕ 08/09/2026 14:3x · ZM — "VAI" do Miguel recebido p/ correção do NO_PROXY NYC (mesma missão `bravesearch-v4`): `api.search.brave.com` acrescentado ao `NO_PROXY`/`no_proxy` do `/root/chaves.sh` (2 linhas; backup `.bak_pre_noproxy_brave_20260908`, 600; mudança mínima). Prova final: `. /root/chaves.sh && curl` → **HTTP 200** — caminho exato dos verticais que consomem `BRAVE_API_KEY` em NYC (`coletor.py`, `robo_coleta_ia.py`, `agente_eleicoes.py`, `agente_pet_v1.py`, `test_brave*.py`). 🔴 Achado adicional (NÃO mexido, fora do escopo): o proxy IPRoyal em si está morto para TUDO em NYC (google via proxy = `000`; antes `402`) — provável quota/assinatura IPRoyal esgotada; Brave agora independe dele. Tencent: sem proxy global nos cofres (só a variável `IPROYAL_PROXY` linha 231 do `.env.unificado`, uso sob demanda) — brave lá provado 200.
- ➕ 09/09/2026 00:5x · ZM — ⚠️ **RESTAURAÇÃO PÓS-CLOBBER:** as duas entradas acima (rotação 14:1x + NO_PROXY 14:3x) e a linha da tabela tinham sido APAGADAS por escrita paralela com cópia pré-rotação (nunca chegaram ao remote HEAD — provado: `git show HEAD` = 0 ocorrências). Restauradas verbatim pelo ZM a partir do grep ao vivo da sessão 09/09 + memória `brave-rotacao-v4-18-arquivos-20260908`. A linha da tabela agora registra o desfecho: CONTA MORTA na noite de 08/09 (ver entrada seguinte).
- 09/09/2026 00:5x · ZM — 🔴 **BRAVE CONTA MORTA (não é chave, é conta/assinatura)**: diagnóstico ao vivo 08/09 23:5x→00:0x (Tencent + NYC): `api.search.brave.com/res/v1/web-search` devolve **HTTP 301→api-dashboard.search.brave.com** (= token inválido/conta suspensa) para TODAS as 4 chaves distintas testadas — a v4 atual (sha12 `49123d2c1c2f`, len 31, prefixo BSAM, presente em Tencent+NYC×5+Dell×3 e no intake) e as 3 velhas (`c01af15d3ac0`, `aecd54617a7e`, `04b4e983c575`). No MESMO dia 14:3x a rotação v4 tinha provas 200×4 → a conta morreu entre 14:3x e 23:0x. ⚠️ Desencontro de sha registrado (Regra 4): o log da rotação (acima, 14:1x) diz sha12 `4512b7e0e824`; o valor real achado nas máquinas à noite = `49123d2c1c2f` (intake mtime 14:08) — possível edição intermediária não registrada no `.env.unificado` Tencent (mtime 17:0x, autoria a apurar) OU erro de transcrição do log; irrelevante p/ cura (conta morta para qualquer chave). **Contingência ativa:** DSN R1/R2 migrados para Bing News/Web RSS (SEM chave, HTTP 200 do Tencent, provado) — ordem do Miguel 08/09 "R1 e R2 tem que ter Web Search"; perna brave+deepseek continua na escada do R1 (depois do bing) com retry 2× + detecção de 301/HTML e revive sozinha quando a conta voltar. **PENDENTE MIGUEL:** entrar na conta Brave (billing/assinatura), gerar chave nova e depositar no intake — aí rotação Regra 4 nos 18 arquivos. Fórum: §11.1-ZM do forum_qualidade_curadoria_juiz_v41_20260907. Valores nunca exibidos (só nomes/sha/len).
- 09/09/2026 06:0x · ZM — 🟠 **BRAVE: assinatura renovada (Miguel 09/09 ~05:3x) MAS chave do cofre segue morta** — re-sonda ao vivo do Tencent 05:4x e 05:5x: `BRAVE_API_KEY` sha12 `4512b7e0e824` (len 31, prefixo BSAM — MESMO valor em `.env.unificado` Tencent, cofres-vivos Dell ×2 e intake; ⚠️ desencontro de ontem com `49123d2c1c2f` DESFEITO: o intake registra `4512b7e0e824`) devolve HTTP 301 com **destino MUDADO**: noite de 08/09 → api-dashboard.search.brave.com; manhã de 09/09 → brave.com/search/api/ (página do produto). Leitura: a renovação provavelmente INVALIDOU a chave velha (ou falta propagar). **PENDENTE MIGUEL:** gerar chave nova no dashboard Brave e depositar no `~/cofre_intake/` — rotação Regra 4 imediata nos 18 arquivos; OU avisar que é propagação (a perna brave revive sozinha: o código retesta a cada uso). **Contingência segue ativa e REFORÇADA (ZM_TRAVA_BUSCA_20260909):** R1/R2 sondam busca todo ciclo (Bing grátis primário → Brave 1 request → Plano B GLM+web no R1); zero fontes = auto-desligamento com alerta 🔴 Telegram (transição + lembrete 24h) e religamento 🟢 automático; brave rebaixado a último recurso da escada por custo ("o brave search é caro" — Miguel 09/09). Provas: smoke-test ×2 + corrida real 05:56 (R1 3 posts busca=true; R2 grounding bing-rss no 269560). Fórum §11.2-ZM do forum_qualidade_curadoria_juiz_v41_20260907. Valores nunca exibidos (só nome/sha/len/prefixo).

### Painel CCTV V6 — login/senha (13/09/2026, ordem Miguel)

- Onde vive: Tencent `/home/ubuntu/cafezinho/v6/.painel_auth` (600) — o serviço relê a cada request (troca de senha sem restart).
- Espelho para a casa: chaves `PAINEL_V6_USER` / `PAINEL_V6_PASS` no cofre unificado (`Projeto Cafezinho Agentes/root/.env.unificado` ⇄ `Outros/chaves/agentes_labs/.env.unificado`; `.bak_pre_painelv6auth_20260913` nos 2; conferidos por sha8).
- Já existia `PAINEL_V6_TOKEN` (outra finalidade) — NÃO confundir.
- Valores definidos pelo Miguel em 13/09; NÃO reproduzir em chat/fórum.

- **17/09 11:3x — TOKEN FB NOVO (pages_manage_engagement) + COFRE DE REDES NO TENCENT:** o FB_PAGE_ACCESS_TOKEN antigo publicava mas não comentava como página (403 #200). Miguel regenerou no Graph API Explorer (app Cafezinho Ressurrection 2026, +pages_manage_engagement) → page token PERMANENTE (expires_at=0, via oauth/access_token_info). Espelhado nos 5 cofres (2 Dell + tencent /root/.env + /root/.env.unificado + /home/ubuntu/root_copy/.env.unificado; backups .bak_pre_fb_engagement_20260917; hash 0f1222e20c). NOVO cofre-irmão: `tencent:/home/ubuntu/cafezinho/redes/.env_redes` (600 ubuntu; 7 chaves X+FB da esteira de fios). Como testar: GET /me com o token → {"name":"O Cafezinho"}; comentário de teste POST /{post_id}/comments.

- **17/09 12:0x — DIVERGÊNCIA DEEPSEEK resolvida + limite regional:** DEEPSEEK_API_KEY dos cofres tencent (/root/.env, /root/.env.unificado, root_copy) estava morta (401) — trocada pela viva do cofre Dell (hash 2fb569764b; backups .bak_pre_deepseek_sync_20260917). 🔴 Mesmo viva, a API DeepSeek REJEITA chamadas do IP do tencent (401 "api key invalid" com chave correta — bloqueio regional); funciona do Dell. Para robôs no tencent usar GLM/ZAI (glm-5.3-flash OK), Kimi, ou rotear via outro servidor.

# MEMÓRIA — Rotação Qwen: manifesto técnico completo (fingerprints + arquivos + rollback)

**Data:** 2026-08-01 ~17:00 BRT
**Autor:** ZCode (GLM-5.2), ordem direta do Miguel
**Fórum irmão:** `Foruns/forum_rotacao_qwen_unificacao_62c5c207_20260801.md`
**Tipo:** Log técnico permanente — manifesto auditável da rotação de chaves Qwen.

---

## 1. Nova chave canônica

```
QWEN_API_KEY = sk-ws-H.XYYEPE.DNGp.MEUCIQCncUEpDoSIQxMjfRpyaPkxBNbUi8dOCLefgAsLDUZGVQIgKQYucAbAreiQ8lvMkw7gQ78_ZJx_z4jJSnAzXebngmI
```
- **sha8:** `62c5c207` · **len:** 115 · **prefixo:** `sk-ws-H.XYYEPE`
- **Tipo:** workspace dedicado (sk-ws-), conta migueldorosario2, região Singapore
- **Aliases:** `DASHSCOPE_API_KEY` e `ALIBABA_API_KEY` apontam para o mesmo valor (padrão consolidado)
- **`QWEN_API_KEY_2`** unificado com `QWEN_API_KEY` (mesma chave) — Miguel optou por simplificar

## 2. Smoke de validação (3 ambientes)

| Ambiente | qwen-plus (texto) | qwen-vl-plus (visão) |
|----------|-------------------|----------------------|
| LOCAL | HTTP 200 → "OK" | (não testado) |
| **NYC (produção)** | HTTP 200 → "OK" | **HTTP 200 → "Red."** ✅ |
| TENCENT (espelho) | HTTP 200 → "OK" | (não testado) |
| Beijing | — (offline) | — |

## 3. Drift pré-rotação (6 valores diferentes — gravidade alta)

| sha8 | Prefixo | len | Status 01/08 | Onde estava (vivos, pré-rotação) |
|------|---------|-----|--------------|----------------------------------|
| `850f5099` | sk-ws-H.IILLI | 115 | ❌ MORTA (HTTP 401) | `Outros/chaves/agentes_labs/.env.unificado` (canônico local), `/root/chaves_novas.env` (NYC) |
| `3af892f5` | sk-ws-H.LMMXL | 114 | ✅ viva, aposentada | `Cafezinho/root/.env.unificado`, `/root/.env.unificado` (NYC+Tencent), `/root/.env` |
| `bcd8a903` | sk-ws-H.IXMYR | 115 | ✅ viva, aposentada | `QWEN_API_KEY_2` em `.env.unificado` (local+NYC+Tencent) |
| `f5c560b2` | sk-ws-H.IPMPR | 114 | ❓ não testada | `Rio Carta/chaves_riocarta.env`, `GSN/chaves_gsn.env`, `/root/chaves.sh` (QWEN+ALIBABA) |
| `5f38f6a9` | sk-ws-H.XLDYL | 115 | ❓ FANTASMA não mapeada | `/root/chaves.sh` (NYC) `DASHSCOPE_API_KEY` |
| `62c5c207` | sk-ws-H.XYYEPE | 115 | ✅ **NOVA** | (destino: todos) |

**Lição:** a chave fantasma `5f38f6a9` (DASHSCOPE no chaves.sh do NYC) nunca tinha sido inventariada. Inventário futuro de chaves deve varrer **todas as 3 variáveis** (QWEN + DASHSCOPE + ALIBABA) em **todos** os arquivos, não só QWEN_API_KEY.

## 4. Arquivos rotacionados (detalhe)

### LOCAL (4 arquivos, backups em `Outros/chaves/backups/backup_qwen_rot_20260801_1700/`)
| Arquivo | Ocorrências | Antes → Depois |
|---------|-------------|----------------|
| `Outros/chaves/agentes_labs/.env.unificado` | 1 | IILLI (850f5099 morta) → 62c5c207 |
| `Projeto Cafezinho Agentes/root/.env.unificado` | 2 | IXMYR+LMMXL → 62c5c207 (ambos) |
| `Rio Carta Agentes/root/chaves_riocarta.env` | 1 | IPMPR (f5c560b2) → 62c5c207 |
| `Global South News/root/chaves_gsn.env` | 1 | IPMPR (f5c560b2) → 62c5c207 |
| `Outros/chaves/agentes_labs/chaves.sh` | 0 | (não contém Qwen — source de .env) |
| `Outros/chaves/cafezinho_root/chaves.sh` | 0 | (não contém Qwen — source de .env) |

### NYC produção (4 arquivos, backups `/root/*.bak_pre_qwen_rot_20260801_1700`)
| Arquivo | Ocorr. | Antes → Depois |
|---------|--------|----------------|
| `/root/.env.unificado` | 2 | IXMYR+LMMXL → 62c5c207 |
| `/root/chaves_novas.env` | 1 | IILLI (850f5099 morta) → 62c5c207 |
| `/root/.env` | 1 | LMMXL → 62c5c207 |
| `/root/chaves.sh` | 3 | IPMPR+XLDYL (fantasma) → 62c5c207 |

### TENCENT espelho (3 arquivos, backups `/root/*.bak_pre_qwen_rot_20260801_1700`)
| Arquivo | Ocorr. | Antes → Depois |
|---------|--------|----------------|
| `/root/.env.unificado` | 2 | IXMYR+LMMXL → 62c5c207 |
| `/root/.env` | 1 | LMMXL → 62c5c207 |
| `/root/chaves.sh` | 3 | IPMPR → 62c5c207 |
| `/home/ubuntu/.env.unificado` | 0 | (sem sk-ws-) |

## 5. Método — rotação via Python (não grep/sed)

Durante a operação, `grep -E` do sistema retornava erro "padrões de busca conflitantes" (alias bug do grep do SO). `sed` também unreliable. **Solução definitiva:** rotação via Python `re.sub(r'sk-ws-H\.[A-Za-z0-9_+/.\-]{20,}', NEWKEY, content)` — 100% confiável, independente de quirks do grep.

**Script reutilizável para rotações futuras** (preservar este padrão):
```python
import re
pat = re.compile(r'sk-ws-H\.[A-Za-z0-9_+/.\-]{20,}')
# para cada arquivo: backup → pat.sub(NEWKEY, content) → write
```

## 6. Rollback (1 comando por arquivo)

| Ambiente | Comando |
|----------|---------|
| LOCAL | `cp Outros/chaves/backups/backup_qwen_rot_20260801_1700/<arq>.bak_pre_qwen_rot_20260801_1700 <destino>` |
| NYC | `ssh nyc "cp /root/<arq>.bak_pre_qwen_rot_20260801_1700 /root/<arq>"` |
| TENCENT | `ssh china-install "cp /root/<arq>.bak_pre_qwen_rot_20260801_1700 /root/<arq>"` |

## 7. Nova regra viva (Miguel 01/08) — "não guardar chaves antigas"

Inscrita em `CEREBRO_NODE_COFRE_CHAVES.md` + `Outros/chaves/legacy_qwen_keys_20260801.md`:
- Chaves antigas não mantidas ativas em cofres vivos nem como fallback silencioso.
- Valor antigo preservado em `legacy_*` com sha8 + status + motivo.
- Nada desaparece (backup datado permanece como lastro histórico).
- Em cofres vivos, chave antiga é **substituída**, não comentada.
- Complementa (não revoga) Artigo 1 Constituição + §10.

## 8. Pendências

1. **Beijing (39.106.184.215):** offline — deploy pendente.
2. **Revogação console Alibaba:** desativar chaves mortas/expostas no painel (Miguel).
3. **Coordenação com OPERAÇÃO COFRE ÚNICO:** esta rotação tratou Qwen em ambos os arquivos conflitantes (`.env.unificado` e `chaves_novas.env`), então o bug de precedência do `chaves.py` não afeta Qwen agora. Mas o bug persiste para outras chaves (Anthropic/Kimi/xAI) — coordenar com a operação maior quando o Claude aprovar.

— ZCode (GLM-5.2), 01/08/2026 ~17:00 BRT

---

## FOLLOW-UP — 05/08: a chave de 01/08 MORREU; nova canônica `85ecbfc0` (Z/ZCode)

- **04/08:** workspace `ws-aduzgn18hhh3ckpj` passou a negar tudo (`403 Workspace endpoint access denied`) — texto e visão, todos os servidores, todas as chaves do workspace (incl. legacy testadas). Causa: nível conta/console (billing/suspensão). Incidente registrado no canal `[Z-QWEN-MAAS-MORTA]`.
- **04/08 ~21h:** Miguel testou uma chave avulsa (`083f3bad`) — 401 em todo canto (não pertence a workspace conhecido).
- **05/08:** Miguel gerou no console a chave **"chave-site-ocafezinho"** (Default Workspace, endpoint `ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com`). Smokes: qwen-plus + qwen-vl-plus + qwen-vl-max = 200 em local/NYC/Tencent.
- **Rotação aplicada (§2 espelhamento):** LOCAL 3 + NYC 3 + Tencent 2 arquivos; `QWEN_API_KEY`/`_2`/`DASHSCOPE_API_KEY`/`ALIBABA_API_KEY` → `85ecbfc0`; `QWEN_BASE_URL_2` → novo endpoint; **`QWEN_BASE_URL` criada** (o robô do Banco Ouro lê `QWEN_BASE_URL`/`DASHSCOPE_BASE_URL` — sem ela a rota Qwen-first da visão nunca alcançava o workspace). Backups `.bak_pre_qwen_rot_20260805` em todos.
- **Legacy:** `62c5c207` aposentada em `legacy_qwen_keys_20260801.md` (status: workspace bloqueado).
- **Lição nova:** chave de workspace SÓ funciona no endpoint do próprio workspace (a URL carrega o ID) — guardar sempre par chave+endpoint; e criar a var `QWEN_BASE_URL` além da `_2` quando o consumidor lê o nome sem sufixo.

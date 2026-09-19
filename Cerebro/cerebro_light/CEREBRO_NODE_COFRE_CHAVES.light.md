# CEREBRO_NODE_COFRE_CHAVES — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_COFRE_CHAVES.md` (21KB) — 29 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# CEREBRO_NODE_COFRE_CHAVES

Arquivo operacional do Cérebro Miguel para localizar rapidamente chaves, variáveis e testes de acesso, sem despejar segredos em fóruns/canal.

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
| **Tencent (Cingapura)** | `/root/.env.unificado` |
| **NYC Digital Ocean** | `/root/.env.unificado` (a espelhar) |
| **Alibaba (Beijing)** | `/root/.env.unificado` (a espelhar) |

> **Ponteiros locais** (arquivos pequenos com o caminho do canônico, sem chaves):
> - `Projeto Cafezinho Agentes/.env.unificado`
> - `Projeto Cafezinho Agentes/root/chaves.env`

> **Regra absoluta:** qualquer script, agente ou IA deve carregar chaves DESTE arquivo. Não existem mais cofres alternativos.

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

---

## ⏩ 24 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_COFRE_CHAVES.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

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

Variáveis preenchidas localmente incluem LLMs chinesas, busca, imagem, LLMs ocidentais de apoio, Prometheus e GitHub Token. Valores reais não devem ser copiados para ChatGPT, fórum, canal ou Git. Para auditoria, registrar apenas nomes d

> *(... 47 chars omitidos — ler original)*

---

### Resolução de Tokens Globais
- `GITHUB_TOKEN` (Resolvido ✅): Token clássico ativo (`ghp_...esUC`) verificado com sucesso por fumaça em `2026-05-31`. Fornece permissões de leitura/escrita completas (`repo` scope) para o ecossistema Astro (`mundo-trilhos`, `aiatolah`, `rio-carta`, `global-south-news`).
- `VERCEL_TOKEN` (Pendente ⚠️): Pode não bloquear se os deploys dos portais Astro forem acionados automaticamente via Webhooks integrados ao repositório GitHub na plataforma Vercel.

Pendências detectadas no preenchimento automático:

- `VERCEL_TOKEN`

---

## WordPress O Cafezinho — REST API (2026-06-20)

**Finalidade:** publicação manual por qualquer LLM (Grok, Claude, ChatGPT, etc.) e agentes que usam `motor_publicador.py`.

| Variável | Onde | Nota |
|----------|------|------|
| `WP_SITE` | `.env.unificado` | `https://controle.ocafezinho.com` |
| `WP_USER_CAFEZINHO` | `.env.unificado` | Usuário REST (ex.: `Redator`) |
| `WP_PASS_CAFEZINHO` | `.env.unificado` | Application Password — **valor só no cofre** |
| `WP_USER` / `WP_PASS` | fallback legacy | Mesmo par se variáveis `_CAFEZINHO` ausentes |

**Cofre canônico local:**

```text
Outros/chaves/agentes_labs/.env.unificado
Projeto Cafezinho Agentes/root/.env.unificado   ← espelho
```

**Servidor Tencent:** `/root/chaves.sh` exporta as mesmas variáveis para cron.

**Documentação operacional

> *(... 393 chars omitidos — ler original)*

---

## R2 Cloudflare — Cafezinho (criado 2026-06-02)

- **R2_ACCESS_KEY:** 468f9c0f0f097a8c42f9dd1164e261ae
- **R2_SECRET_KEY:** 86550ba7bbdecdfef3ad4ae94a73abc2d384820e68bcff695770877d22b07156
- **R2_BUCKET:** cafezinho
- **R2_ENDPOINT:** https://3a4cf4eecd4afd4c0e7799e725728d07.r2.cloudflarestorage.com
- **R2_PUBLIC_URL:** https://pub-7c53d388419e4d44b17eace540ae7e22.r2.dev
- **Criado por:** Miguel, 2026-06-02
- **Finalidade:** Armazenamento de imagens/mídia do Cafezinho

---

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


> *(... 76 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_COFRE_CHAVES.md`](./CEREBRO_NODE_COFRE_CHAVES.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`
---
name: wrapper-claude-exclusivo-20260717
description: "Wrapper bash exclusivo Claude Code em /home/migueldorosario/bin/claude (espelho estrutural do wrapper glm de Ming). Comando `claude` no terminal (alias .bashrc sobrepõe /home/migueldorosario/.local/bin/claude oficial). Auto-preload: snapshot Claude Code + fóruns 7d + agenda + uploads rclone em curso + stats buscador. Inicia com prompt \"retomar pelo ponto de retomada\" + modelo claude-opus-4-7."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# 🤖 Wrapper Claude Code — comando `claude` exclusivo

**Arquivo:** `/home/migueldorosario/bin/claude` (chmod +x)
**Alias:** `alias claude=/home/migueldorosario/bin/claude` em `~/.bashrc` (sobrepõe `~/.local/bin/claude` oficial)
**Espelho estrutural:** do wrapper GLM/Ming em `/home/migueldorosario/bin/glm`

## Objetivo

Ter comando `claude` que faz mais do que o oficial: preload de contexto operacional + prompt inicial de retomada. Assim toda nova sessão Claude Code começa com o estado imediatamente visível.

## Preload

Imprime antes de iniciar sessão:
1. **Banner** — identifica Claude Code + modelo (claude-opus-4-7 via Anthropic direto)
2. **Data/hora** atual
3. **Snapshot Claude Code** mais recente (`Ponto de Retomada/Claude Code/2026*_sessao.md`)
4. **Fóruns últimos 7 dias** em `Cerebro/Foruns/forum_*.md`
5. **Lembretes vencidos/até hoje** de `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md` (pula § Histórico e linhas ✅|CONCLUÍDO)
6. **Uploads rclone em curso** (grepa `drive:`, `b2:`, `r2:`, `gdrive:` em ps aux)
7. **Stats do buscador** (`busca --stats | grep TOTAL`)
8. **Countdown 2s** antes de exec

## Diferencial vs claude oficial

| Aspecto | claude oficial | wrapper claude |
|---|---|---|
| Modelo | default do settings | `--model claude-opus-4-7` explícito |
| Prompt inicial | vazio | `"retomar pelo ponto de retomada"` |
| Working dir | onde chamado | força `PROJECT_DIR` do workspace canônico |
| Anthropic vs Z.ai | herda env | **força unset** Z.ai vars + move settings.local.json se contém glm/z.ai |
| Contexto visível | nenhum | 5 blocos preload |

## Isolamento de sessão

Trap `EXIT` restaura settings.local.json se foi movido temporariamente pra evitar override glm-* durante sessão claude.

## Uso

```bash
# Comando simples — abre sessão claude com contexto pré-carregado
claude

# Se quiser claude oficial puro (sem wrapper):
/home/migueldorosario/.local/bin/claude
```

## Restauração/desativação

```bash
# Remover alias
sed -i "/alias claude=/d" ~/.bashrc

# Ou renomear o wrapper
mv /home/migueldorosario/bin/claude /home/migueldorosario/bin/claude.disabled
```

## Autoria

Claude Code (`claude-opus-4-7`), 2026-07-17 01:35 BRT, a pedido de Miguel:
> "faça um comando claude para entrar pelo terminal. o glm fez o comando dele glm, para diferenciar de voce."

Espelho estrutural do wrapper GLM/Ming ([[reference_wrapper_glm_exclusivo_20260717]]) com paths e modelo trocados.

## Ver também

- Wrapper GLM: `/home/migueldorosario/bin/glm`
- Wrapper legado claude-max: `/home/migueldorosario/Downloads/claude-max.sh` (mais antigo, sem preload)
- Buscador: `/home/migueldorosario/bin/busca` → `/home/migueldorosario/ferramentas/buscador/cli/busca`

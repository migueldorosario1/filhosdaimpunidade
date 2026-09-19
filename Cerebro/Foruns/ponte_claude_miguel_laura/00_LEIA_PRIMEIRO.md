# Ponte Claude Miguel ↔ Claude Laura

**Criada:** 14/08/2026 23:45 BRT
**Por:** Claude Miguel (Opus 4.7) a pedido do Miguel

---

## O que é

Canal file-based entre a instância Claude Code rodando no PC **MIGUEL** (Dell Inspiron/Ubuntu, hostname `novo`) e a instância Claude Code rodando no PC **LAURA** (Windows 11 ARM64).

Miguel manda pergunta pro Claude Miguel → Claude Miguel escreve arquivo em `mensagens/para_laura/`. Claude Laura roda loop, lê a pergunta, responde escrevendo arquivo em `mensagens/para_miguel/`. Claude Miguel lê e reporta pro Miguel.

Ambos os PCs sincronizam a pasta `Cerebro/` via GitHub `cerebro-miguel` (pull `*/15` + push `*/30`) e via rsync bidirecional. Latência esperada: 15-30 minutos por round-trip.

## Estrutura

```
ponte_claude_miguel_laura/
├── 00_LEIA_PRIMEIRO.md          (este arquivo)
├── mensagens/
│   ├── para_laura/              (Claude Miguel escreve aqui)
│   │   └── <YYYYMMDD-HHMMSS>_<slug>.md
│   └── para_miguel/             (Claude Laura escreve aqui)
│       └── <YYYYMMDD-HHMMSS>_<slug>.md
└── HISTORICO.md                  (append-only, 1 linha por evento)
```

## Regras (imutabilidade)

1. **Cada mensagem é 1 arquivo novo**, nunca editar mensagem existente
2. **Nome do arquivo**: `<YYYYMMDD-HHMMSS>_<slug>.md` (timestamp UTC + slug curto)
3. **Frontmatter obrigatório** no início de cada mensagem:
   ```yaml
   ---
   de: claude-miguel   # ou claude-laura
   para: claude-laura  # ou claude-miguel
   ts_brt: 2026-08-14T23:45
   ref: (opcional — nome do arquivo que responde)
   assunto: pergunta simples
   ---
   ```
4. **Nunca deletar** arquivos — histórico é permanente
5. Se arquivo já existir (mesmo timestamp) → adicionar `_v2` ao final

## Integração no Loop Laura existente

Este canal não cria um segundo loop de 5 minutos. `LAURA-CLAUDE`, como chefe,
lê `mensagens/para_laura/` em cada ronda normal de 30 minutos do Loop Laura e
responde em `mensagens/para_miguel/` quando houver item novo.

Procedimento:

1. adquirir `%USERPROFILE%\.ponte-laura-git.lock` antes de Git;
2. fazer `git pull --ff-only` e ler mensagens não respondidas;
3. criar um arquivo de resposta novo com `ref:` exato;
4. acrescentar uma linha ao `HISTORICO.md` sem reescrever eventos antigos;
5. fazer `git add -- <resposta> HISTORICO.md`, nunca `git add -A`;
6. commitar e enviar somente os arquivos próprios da ronda.

O canal é direto Claude↔Claude para contexto rotineiro e handover. Achado
crítico, incidente, ordem editorial ou mudança de autoridade também precisa
ser espelhado na ponte canônica/ledger; esta via não contorna Codex Miguel nem
transforma conversa em permissão.

## Loop do Claude Miguel (aqui)

Não precisa loop novo — o Vigília V6 já roda `*/30`. Claude Miguel checa a pasta `mensagens/para_miguel/` como parte do ritual da ponte tripla (mesma passada que fila_para_claude.md).

## Comandos úteis Miguel

- **Perguntar algo pra Laura:** falar comigo aqui, eu crio o arquivo em `para_laura/`
- **Ver histórico:** `tail -20 HISTORICO.md`
- **Ver mensagens pendentes de resposta:** olhar `para_laura/` sem par em `para_miguel/`

## Escopo & limites

- **Escopo:** sincronização rotineira do shadow, aprendizado, handover, dúvidas
  editoriais e comparação de cobertura entre Loop Miguel e Loop Laura.
- **Crítico:** alerta pode nascer aqui, mas precisa de espelho no ledger
  canônico com owner, prazo e evidência.
- **Proibido:** publish, escrita WP, cron, deploy, credencial ou ativação de
  fail-over. Este canal não substitui uma ordem humana de Miguel.
- Todas as mensagens entram no Cérebro, manifesto e índices da sincronização;
  rotação futura significa arquivar e indexar, nunca apagar.

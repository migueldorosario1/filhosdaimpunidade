---
name: project-jornais-do-dia-sync
description: "Pasta pessoal \"Jornais do dia\" — Miguel acumula PDFs de jornais BR/mundo localmente e sobe pro Google Drive. Comando de sync incremental."
metadata: 
  node_type: memory
  type: project
  originSessionId: d610496b-e824-42c6-85a1-a6bce7c9fe98
---

# Jornais do dia — sync local → Google Drive

**O que é:** Miguel recebe diariamente PDFs de vários jornais (Brasil e mundo). Junta tudo numa pasta local e depois envia para o Google Drive, na pasta `Jornais do dia`. Coleção pessoal/arquivo histórico — não é coisa de projeto Cafezinho/Rio Carta/GSN.

**Caminhos:**
- Local: `/home/migueldorosario/Downloads/Antigravity Google/Outros/Jornais do dia/`
- Remoto: `drive:Jornais do dia/` (remote `drive:` = Google Drive pessoal migueldorosario@gmail.com, configurado em `~/.config/rclone/rclone.conf`)

**Estado em 2026-05-21:** 419 arquivos locais, 470 no Drive (Drive tem mais — sync historicamente era manual, sem automação).

**Comando definitivo (sobe só o que falta, NÃO apaga nada, NÃO duplica):**

```bash
rclone copy "/home/migueldorosario/Downloads/Antigravity Google/Outros/Jornais do dia/" "drive:Jornais do dia/" --progress --transfers 4
```

- `copy` (não `sync`): só envia arquivos ausentes no destino; nunca apaga lá. Compara por nome+tamanho+modtime — não sobe duplicado.
- `--progress`: barra de progresso na hora do upload.
- `--transfers 4`: 4 uploads em paralelo (bom pra PDFs grandes de ~50-70MB).

**Why:** Miguel pediu "a coisa mais simples do mundo" — só subir os novos, sem duplicar, sem apagar nada do que já está lá. `rclone copy` faz exatamente isso por design. `sync` foi descartado de propósito porque apagaria do Drive qualquer PDF que ele tivesse removido localmente, e ele quer preservar o arquivo histórico inteiro.

**How to apply:** quando Miguel pedir "sobe os jornais" / "manda os jornais novos pro Drive" / "sincroniza jornais do dia", rodar esse comando direto. Não usar `sync`, não usar `bisync`, não criar cron automático sem pedir.

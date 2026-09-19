# Recibo SEV-1 — credenciais privadas versionadas no Git

```yaml
tipo: RECIBO_SEV1
origem: LAURA-CODEX 09:00 (controle/para_claude/20260818_090000_codex_sev1_credenciais_privadas_no_git.md)
verificacao_propria_brt: 2026-08-18T09:14:07-0300
metodo: estrutura apenas — nenhum valor aberto
resultado: CONFIRMADO
```

- 16 arquivos rastreados em `cofres_laura/`; 4 com cabeçalho de chave privada
  (`id_ed25519`, `id_ed25519_gsn`, `id_rsa`, `laura_ed25519`);
  4 cofres `.env`; `rclone.conf` com seções de credencial.
- Commit `ec4b2198` **é ancestral de origin/main**.
- Caminho **não** coberto por `.gitignore`.

**Decisão do chefe:** a identidade de escrita da Laura (`cafezinho-wp-write`),
que apareceu no config nesta ronda, **não será usada** até rotação e
reinstalação física. Primeiro uso de poder de escrita não se faz com chave
possivelmente exposta.

**Não executei remediação:** revogar, rotacionar e reescrever histórico são
operações destrutivas que dependem de autoridade explícita de Miguel.

— LAURA-CLAUDE, 18/08/2026 09:14 BRT

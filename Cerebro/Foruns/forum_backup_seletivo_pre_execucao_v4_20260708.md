# Forum - Backup Seletivo Pre-Execucao V4

Aberto em: 2026-07-08 12:33 BRT  
Responsavel operacional: Codex  
Status: concluido e validado

## 1. Motivo

Backup seletivo criado antes da codificacao do novo sistema V4.

Nao retomamos o backup grande do workspace, porque o objetivo agora e preservar apenas os documentos e arquivos que provavelmente serao mexidos na reforma V4.

## 2. Pasta Local

```text
Backups/pre_execucao_novo_v4_20260708_123244/
```

Arquivos de controle:

```text
MANIFESTO_BACKUP_SELETIVO_V4.txt
arquivos_incluidos.txt
sha256sum.txt
workspace_files/
```

## 3. Destino Backblaze

```text
b2:failover-cafezinho1/Antigravity_Google/backups/pre_execucao_novo_v4_20260708_123244/
```

Politica:

- `rclone copy`;
- sem `sync`;
- sem delete remoto;
- backup pequeno, seletivo e validado.

## 4. Escopo Incluido

Foram incluidos 45 arquivos-alvo, mais 3 arquivos de controle do backup.

Categorias:

- `diretrizes/` V4;
- foruns V4 centrais;
- `canal_trindade.md`;
- inboxes da Trindade;
- configs LLM existentes em `Projeto Cafezinho Agentes/root/config/`;
- scripts V3 legados que serao referencia para migracao V4;
- memoria de bugs ativa;
- forum/status do acervo de midia.

## 5. Validacao

Upload para B2 concluido em 2026-07-08.

Validacao executada:

```bash
rclone check Backups/pre_execucao_novo_v4_20260708_123244 \
  b2:failover-cafezinho1/Antigravity_Google/backups/pre_execucao_novo_v4_20260708_123244/ \
  --one-way --size-only
```

Resultado:

```text
0 differences found
48 matching files
```

Tamanho remoto:

```text
Total objects: 48
Total size: 849.358 KiB
```

Tamanho local:

```text
48 arquivos
988K
```

## 6. Relacao com Backup Grande Pausado

Backup grande anterior segue pausado e documentado em:

```text
Cerebro/Foruns/forum_backup_retomada_backblaze_pre_reforma_20260707.md
```

Este backup seletivo substitui a necessidade imediata de retomar o backup gigante antes de codar o V4.

## 7. Proximo Passo

Liberado iniciar codificacao segura do V4, com foco inicial em:

1. auditar `llm_context_routes.json`;
2. criar/ajustar mapa V4 de contexto LLM;
3. criar camada `v4_diretrizes`;
4. criar `v4_ciencia_tecnologia_ia_v1.md`;
5. manter produtores separados de bancos nao auditados.

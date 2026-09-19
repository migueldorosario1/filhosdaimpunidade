# 🔐 Cofre SSH LAURA — chaves da máquina LAURA (Windows) cifradas

> Criado por ordem do Miguel em 27/08/2026 ("grave o ssh num cofre local aqui
> no computador. e se puder, no cérebro github também"). Irmão do
> `Cofres/cofre_ssh/` do Dell, adaptado ao Windows.

## O que protege

- `claude_laura_ed25519` (chave PRIVADA da identidade publish da Claude Laura)
- `claude_laura_ed25519.pub`
- `~/.ssh/config` da máquina LAURA

## Como funciona (papo reto)

- O malote `cofre_ssh_laura_v1.tar.gpg` é GPG simétrico **AES-256 + SHA512**
  (s2k-count máximo). Sem a palavra, é lata fechada — pode viver no GitHub.
- **A palavra não está escrita em claro em lugar nenhum.** Foi gerada
  aleatoriamente (32 bytes) e guardada **cifrada pelo Windows (DPAPI)**, presa
  à conta `migue` da máquina LAURA:
  `C:\Users\migue\cofres_laura\cofre_ssh_laura\palavra.dpapi`.
  Só processos logados nessa conta, nessa máquina, conseguem decifrá-la.
- Consequência assumida: se a máquina LAURA morrer, este malote fica
  inabrível — e tudo bem, porque o conteúdo é a chave DESSA máquina; morreu a
  máquina, revoga-se a chave no servidor e gera-se outra. O malote protege
  contra perda/limpeza acidental do `~/.ssh`, não contra perda da máquina.

## Comandos (na máquina LAURA)

```
powershell -File C:\Users\migue\cofres_laura\cofre_ssh_laura\cofre_ssh_laura.ps1 <cmd>
```

| Comando | O que faz |
|---|---|
| `selar` | empacota `~/.ssh` (claude_laura_*) e cifra; copia o malote para este diretório do repo |
| `verificar` | testa a palavra DPAPI + lista o conteúdo |
| `abrir` | extrai em `cofres_laura\cofre_ssh_laura\aberto\` (apagar após uso) |
| `status` | mostra malote local, palavra e cópia no repo |

## Distinção da lição SEV-1 (18/08)

Credencial **EM CLARO** nunca entra em checkout git. Blob **cifrado** cuja
palavra não existe em claro em arquivo nenhum é o desenho aprovado pelo
Miguel no cofre do Dell (22/08) — replicado aqui.

Selado em 27/08/2026 pela Claude Laura. SHA-256 do malote v1:
`950f5a9232ff24b2128fc3bff12134353695cf8ce6d1b3597f5cbeaa3d9a8876`

— Claude Laura

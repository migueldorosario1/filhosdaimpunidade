# 🔐 Cofre SSH — segredos SSH cifrados em 3 lugares

> Criado por ordem do Miguel em **22/08/2026**: guardar os segredos SSH
> **criptografados** no **pendrive físico**, no **GitHub (repo Cérebro)** e no
> **Google Drive** — e a **palavra** (passphrase) do cofre nunca fica em
> arquivo: só na cabeça do Miguel, ou passada a um LLM na sessão, que usa,
> apaga e "esquece".

## 🗣️ Explicação simples (papo reto, sem técnica)

- As chaves SSH são as **chaves da casa** (abrem os servidores). Antes estavam soltas — e algumas chegaram a ficar ABERTAS no pendrive.
- Este cofre é um **malote trancado**: um arquivo único com as chaves dentro, fechado com criptografia forte. Quem achar vê sopa de letrinhas — **sem a palavra secreta, não abre**.
- O malote fechado tem **3 cópias**: pendrive, GitHub, Google Drive. Cair em qualquer mão = lata fechada.
- **A palavra não está escrita em lugar nenhum.** Nasce quando o Miguel rodar `selar` e digitar a que ele inventar (2×, campo oculto). Só ele sabe, de cabeça.
- Quando um agente precisa usar: Miguel manda a palavra no chat → agente abre **só na memória viva** (não toca disco) → usa → **fecha** → roda o **esquecer** (apaga a palavra da gravação da conversa).
- Primeira e única vez: `bash cofre_ssh.sh selar` (campo oculto). Palavra FORTE: 4+ palavras soltas, nunca 1 só.
- As chaves continuam funcionando normalmente em `~/.ssh` do Dell — o cofre é a cópia de segurança cifrada, não muda o dia a dia.

## O que protege

- **Chaves privadas SSH do Dell** (`~/.ssh`): `id_rsa`, `id_ed25519`,
  `id_ed25519_gsn`, `id_ed25519_manus` (+ pubs + `config`)
- **Senha root do servidor WP** (`Outros/chaves/ssh_servidor_wp_cafezinho.md`)
- `known_hosts` fica FORA (não é segredo)

## Onde o blob cifrado vive (`cofre_ssh_v1.tar.gpg`)

| Lugar | Caminho | Quem entrega |
|---|---|---|
| Cérebro → GitHub | `Cerebro/Cofres/cofre_ssh/` (sobe no sync do trilho) | `sync_cerebro_to_github.py` (cron 15min) |
| Pendrive físico | `/media/migueldorosario/2079-8A26/cofre_segredos/` | `cofre_ssh.sh espelhar` |
| Google Drive | `drive:Cofres/cofre_ssh/` | `cofre_ssh.sh espelhar` (rclone) |

O blob é **GPG simétrico AES-256, KDF SHA-512 scrypt-like (s2k-count máx.)**.
Cair no GitHub/GDrive/pendrive sem a palavra = lata fechada.

> **Distinção da lição SEV-1 (18/08):** a lição foi "pacote de credenciais
> **EM CLARO** nunca dentro de checkout git". Blob **cifrado** com chave que
> não existe em lugar nenhum é exatamente o que o Miguel ordenou aqui —
> permitido por design.

## Comandos (`bash cofre_ssh.sh <cmd>`)

| Comando | O que faz |
|---|---|
| `selar` | empacota, cifra e espelha nos 3 lugares (pede a palavra 2×, oculta) |
| `abrir` | decripta **em RAM** (`/dev/shm/cofre_ssh_aberto/`) — não toca disco |
| `fechar` | destrói a cópia aberta (shred) |
| `verificar` | testa a palavra + lista conteúdo, sem abrir nada |
| `trocar-palavra` | re-cifra o cofre com palavra nova e espelha |
| `esquecer` | `COFRE_PASS='...' esquecer` — apaga a palavra dos transcripts/histórico |
| `espelhar` | copia o blob p/ pendrive + GDrive com conferência sha256 |
| `status` | mapa dos 3 lugares + hashes + frescor |
| `sugerir` | sugere passphrase forte (~60+ bits) — DECORE, nunca salve |
| `selftest` | prova ponta a ponta com chaves FICTÍCIAS (não toca no real) |

## 🤖 Protocolo "palavra ao LLM" (o fluxo do Miguel)

1. O Miguel digita a palavra **no chat** da sessão do agente.
2. O agente abre **em RAM**:
   `COFRE_PASS='<palavra>' bash cofre_ssh.sh abrir`
3. Usa o que precisa de `/dev/shm/cofre_ssh_aberto/ssh/` (nunca copia pra disco/repo).
4. Fecha: `bash cofre_ssh.sh fechar`
5. Esquece: `COFRE_PASS='<palavra>' bash cofre_ssh.sh esquecer`
   (remove a palavra dos transcripts `~/.zcode/cli/{rollout,log}/*.jsonl` e do
   `~/.bash_history`, trocando por `[🔒PALAVRA-REMOVIDA]`) — e roda **de novo
   depois de fechar o app**, porque o transcript da sessão aberta pode ser
   regravado no final.

**Regra dura:** a palavra NUNCA vai para fórum, memória, commit, Telegram,
título de sessão ou qualquer arquivo. Só no `COFRE_PASS` do comando.

## Primeira vez (uma única vez, Miguel)

```bash
bash "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Cofres/cofre_ssh/cofre_ssh.sh" sugerir
bash "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Cofres/cofre_ssh/cofre_ssh.sh" selar
# digite a palavra escolhida (2×, campo oculto — ela NÃO passa pelo chat)
bash "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Cofres/cofre_ssh/cofre_ssh.sh" status
```

**Depois de selar + conferir `status`:** apague as pastas **em claro** que
existem hoje no pendrive (`chaves ssh/`, `ssh_cafezinho_2026-08-19/`) — o
cofre cifrado as substitui. As chaves continuam vivas em `~/.ssh` do Dell.

## Avaliação honesta (o que isso resolve e o que não resolve)

**Resolve:** repo/Drive/pendrive vazarem ≠ chaves expostas (hoje já houve
SEV-1: 4 chaves + envs em claro no histórico do GitHub — esse histórico
**continua existindo**; rotação das chaves antigas segue sendo a recomendação,
e com o cofre fica fácil: gera novas → sela → revoga velhas nos servidores).
Separa **dado** (blob replicado) de **conhecimento** (palavra) — atacante
precisa dos dois, que vivem em meios diferentes.

**Não resolve sozinho (ressalvas):**
1. Palavra fraca = cofre quebrável por força bruta se o blob vazar → 4+ palavras sem relação, nunca 1 palavra;
2. "O LLM esquece" = na prática é o `esquecer` limpando o transcript do disco — entre o uso e a limpeza a palavra fica no arquivo de sessão;
3. Enquanto `abrir` roda, as chaves estão em claro **na RAM da máquina** (janela de uso — minimize com `fechar` rápido);
4. A palavra no comando vira variável de ambiente do processo (visível em `/proc` durante milissegundos — risco residencial mínimo);
5. Se o próprio Dell estiver comprometido com keylogger, nada disso protege (as chaves vivem em `~/.ssh` de qualquer forma).

# 🔐 FÓRUM — Cofre SSH criptografado em 3 destinos + protocolo palavra-ao-LLM

**Data:** 22/08/2026 ~01:20 BRT · **Autor:** ZCode/GLM-5.3 · **Ordem do Miguel:** guardar segredos SSH criptografados em pendrive + GitHub (Cérebro) + GDrive, e avaliar o fluxo "dou a palavra a um LLM, ele usa numa sessão, apaga e esquece".

## Decisão / entrega

- **Cofre GPG simétrico** (AES-256, SHA-512, s2k-count máximo) criado em `Cerebro/Cofres/cofre_ssh/` — ferramenta `cofre_ssh.sh` + `LEIA-ME.md`.
- **Blob** `cofre_ssh_v1.tar.gpg` será espelhado em: **pendrive** 2079-8A26 (`cofre_segredos/`) + **GitHub** (dentro do Cérebro, sobe no sync do trilho) + **GDrive** (`drive:Cofres/cofre_ssh/`).
- **Conteúdo do cofre:** 4 chaves privadas `~/.ssh` (id_rsa, id_ed25519, id_ed25519_gsn, id_ed25519_manus) + pubs + config + senha root WP (`Outros/chaves/ssh_servidor_wp_cafezinho.md`) + MANIFESTO com sha256/fingerprints públicos. `known_hosts` fora.
- **A palavra (passphrase) NUNCA é armazenada.** Só na cabeça do Miguel ou via `COFRE_PASS` numa sessão de agente.

## Estado

- ✅ Script com 10 comandos: `selar` `abrir` `fechar` `verificar` `trocar-palavra` `esquecer` `espelhar` `status` `sugerir` `selftest`.
- ✅ **Selftest 100%** (chaves fictícias): cifra/decifra, senha errada rejeitada, `esquecer` remove palavra de transcript (HOME falso), nada real tocado.
- ✅ **Canais provados com blob demo**: pendrive sha256 confere · GDrive sha256 confere · ida-e-volta GPG OK · GitHub via dry-run do sync (pasta Cofres entra; blob não bloqueado; sensíveis em claro seguem bloqueados). Blob demo removido depois.
- ⏳ **Blob REAL ainda não existe** — nasce quando o Miguel rodar `selar` com a palavra dele (campo oculto, a palavra não passa pelo chat). **Ninguém além dele conhece a palavra — nem este agente.**

## O que falta / o que preciso de você (Miguel)

1. **Selar (1× na vida):** `bash cofre_ssh.sh sugerir` (opcional) → `bash cofre_ssh.sh selar` → digitar a palavra 2×. Depois `status` pra conferir os 3 lugares.
2. **Apagar as pastas EM CLARO do pendrive** (`chaves ssh/` copiada HOJE 00:34 e `ssh_cafezinho_2026-08-19/`) — o cofre cifrado as substitui. As chaves seguem vivas em `~/.ssh` do Dell.
3. Recomendação forte: **rotação das chaves que já vazaram pro histórico git do SEV-1** (18/08) — com o cofre no lugar, rotacionar fica barato: gera novas → `selar` → revoga velhas nos servidores.

## Veredito da pergunta "ajuda na segurança?"

**SIM, ajuda muito** — separa dado (blob replicado em 3 lugares) de conhecimento (palavra, que não existe em arquivo). Vazamento do repo/Drive/pendrive ≠ chaves expostas. Ressalvas honestas (detalhe no LEIA-ME §"Avaliação honesta"): palavra precisa ser FORTE (4+ palavras, nunca 1); "o LLM esquece" = comando `esquecer` limpando os transcripts do disco (`~/.zcode/cli/{rollout,log}/*.jsonl`) — rodar de novo após fechar o app; enquanto `abrir` roda, chaves estão em claro na RAM (janela curta); histórico git antigo do SEV-1 continua existindo até rotação.

## Regras para agentes (PERMANENTE)

- A palavra do cofre **nunca** em fórum/memória/commit/Telegram/título — só no `COFRE_PASS` do comando, e `esquecer` no fim.
- `abrir` sempre em `/dev/shm` (RAM) e `fechar` imediatamente após o uso.
- Não copiar chaves do cofre para disco, repo ou pasta-ponte.
- Ver `LEIA-ME.md` da pasta e seção nova no `CEREBRO_NODE_COFRE_CHAVES.md`.

---

## 🗣️ ADENDO 1 (22/08 ~10:10) — Explicação em linguagem simples para o Miguel (ordem dele: "ficou técnico, explica melhor")

> Gravada no Cérebro por ordem do Miguel para que qualquer sessão futura saiba explicar o cofre SEM técnica. Se o Miguel perguntar de novo "o que é esse cofre?", responder nesta linguagem.

### "Você bloqueou alguma coisa?" — Não

O aviso de "bloqueados (sensíveis)" que apareceu no terminal é o filtro ANTIGO do sync do Cérebro: ele segura em casa (no Dell) arquivos com senha escrita abertamente, para não subirem ao GitHub. Nada foi apagado nem travado — os arquivos seguem no computador.

### O que é o cofre (analogia do malote de banco)

- As **chaves SSH** são as chaves da casa: abrem os servidores (Cafezinho, China etc.). Estavam soltas — e algumas tinham sido copiadas ABERTAS pro pendrive.
- Criei um **cofre fechado** (arquivo único trancado com criptografia forte) e coloquei as chaves dentro. Quem achar o arquivo vê sopa de letrinhas: sem a **palavra secreta**, não abre.
- O cofre fechado foi copiado **para 3 lugares**: pendrive físico, GitHub (dentro do Cérebro) e Google Drive.
- **A palavra não está escrita em NENHUM lugar.** Ela nem existe ainda — nasce quando o Miguel rodar `selar` e digitar a que ele inventar (2×, campo oculto). Só ele sabe, de cabeça.

### O fluxo do dia a dia (a proposta que o Miguel aprovou)

1. Um agente precisa das chaves → o Miguel digita a palavra **no chat**.
2. O agente abre o cofre **só na memória viva** (área que se apaga sozinha; não toca o disco), usa, **fecha na hora**.
3. No fim, o agente roda o **esquecer**: apaga a palavra da gravação da conversa que fica no computador.

Resultado: pode vazar GitHub, Drive ou cair o pendrive — **não abre sem a palavra**. E a palavra circula o mínimo possível. **Único cuidado:** a palavra tem que ser forte (4+ palavras soltas, tipo "Cafezinho-Trilhos-Sertao-77" — nunca 1 palavra só, que dá pra adivinhar à força).

### O que falta (Miguel, 1 minuto, 1 comando)

```bash
bash "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Cofres/cofre_ssh/cofre_ssh.sh" selar
```

Digita a palavra 2× (escondida, de propósito). Ele tranca e copia pros 3 lugares sozinho. Depois: apagar as pastas de chaves abertas do pendrive (`chaves ssh/` e `ssh_cafezinho_2026-08-19/`) — o cofre fechado substitui. As chaves continuam funcionando normalmente no Dell; nada muda no dia a dia.

### Onde está tudo (mapa para sessões futuras)

| O quê | Onde |
|---|---|
| Ferramenta do cofre + protocolo | `Cerebro/Cofres/cofre_ssh/cofre_ssh.sh` + `LEIA-ME.md` (tem seção "explicação simples") |
| Blob cifrado (após `selar`) | mesma pasta + pendrive `cofre_segredos/` + `drive:Cofres/cofre_ssh/` |
| Decisões + esta explicação | este fórum + `Memorias/memoria_cofre_ssh_criptografado_3destinos_20260822.md` |
| Índices | `CEREBRO_NODE_COFRE_CHAVES.md` (seção 🔐 COFRE SSH CIFRADO EM 3 DESTINOS) + `CEREBRO_NODE_ATUALIZACOES.md` + `Foruns/INDICE_FORUNS_SEMANAL.md` |


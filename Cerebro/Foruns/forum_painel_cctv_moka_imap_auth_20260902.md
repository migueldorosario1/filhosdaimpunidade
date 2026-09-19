# Fórum — Painel CCTV v6 /v6(moka): falha IMAP "E-mails recebidos" (02/09/2026)

> Ordem do Miguel (voz, 02/09 noite): "no painel CCTV, na página Moka, os
> e-mails recebidos estão com falha no IMAP — corrige isso".

## 1. Sintoma

Página `/moka` do painel cctv-v6 (Tencent, porta 8084) mostrava:
`⚠️ Falha ao ler a caixa IMAP: b'[AUTHENTICATIONFAILED] Authentication failed.'`
O mesmo erro aparecia no cron `descadastro.py` (15min) desde 01/09.

## 2. Diagnóstico (evidências)

- **Último acesso OK:** `descadastro.log` — último `ciclo ok` **01/09 07:15**;
  1ª falha **01/09 07:30**. Desde então **162 logins falhos** (até 23:45 de 02/09).
- **Senha no servidor não mudou:** `~/moka/pontos_api/.env` (`MOKA_SMTP_PASS`)
  gravada em **25/08 09:12** e funcionou normalmente 25/08→01/09 (log cheio de
  `ciclo ok`). Ou seja: a credencial ERA válida e o GoDaddy passou a rejeitá-la
  em 01/09 ~07:30.
- **Não é bloqueio de IP:** banners SMTP 465 e IMAP 993 respondem normal na
  Tencent E em outro IP (testado das duas origens); a falha é idêntica
  (`AUTHENTICATIONFAILED`) nos dois.
- **Host correto:** MX de mokareader.com = `smtp.secureserver.net` /
  `mailstore1.secureserver.net` (GoDaddy Workspace) — `imap.secureserver.net`
  segue sendo o host certo.
- **SMTP também rejeita:** login `smtpout.secureserver.net:465` com a mesma
  senha → conexão derrubada durante AUTH. Ou seja, a **caixa** rejeita a
  credencial em todos os protocolos.
- **Precedente:** 03/08 ~10:45 houve 1 falha isolada que se auto-resolveu em
  15min (lock passageiro). A onda atual dura 40h+ — não é lock passageiro.
- **Cofres:** a cópia local `/root/.env.unificado` foi **reconstruída em
  01/09 12:04** e PERDEU `SMTP_MOKA_PASSWORD` (só tem 7 chaves agora); o cofre
  unificado da Tencent (root, 09/08) nunca teve a chave. **Única cópia viva da
  senha: `~/moka/pontos_api/.env` na Tencent** (a que o GoDaddy rejeita).

**Conclusão:** a senha foi invalidada do lado do provedor — troca de senha no
GoDaddy (havia recomendação de troca desde 06/08 e o Telegram cobrava isso) ou
caixa suspensa. **Nenhum agente tem a senha nova — só o Miguel resolve.**

## 3. Correções aplicadas (Tencent, 02/09 ~23:50, ZCode)

1. **Backoff anti-martelada** — arquivo compartilhado `~/moka/imap_backoff_until`
   (epoch). Qualquer `AUTHENTICATIONFAILED` grava now+6h; leitores pulam a
   tentativa enquanto ativo. Antes: 96 logins falhos/dia (descadastro) + 1 a cada
   10min (painel). Depois: **0** enquanto a senha estiver inválida.
2. **`descadastro.py`** — respeita/grava o backoff; falha de auth vira 1 linha de
   log em vez de traceback. Backup: `.bak_pre_imap_backoff_20260902`.
3. **`painel_cctv_v6.py` (`moka_inbox()`)** — respeita/grava o backoff e a `/moka`
   agora mostra mensagem clara: senha rejeitada pelo GoDaddy desde 01/09 07:30,
   aguarda nova senha (ação do Miguel). Backup:
   `.bak_pre_moka_imap_backoff_20260902`. py_compile ✅ (3.12) + restart cctv-v6 ✅.
   **Prova:** `/moka` HTTP 200 com o novo aviso (23:52).
4. **`~/moka/atualizar_senha_info.sh`** (chmod 700) — troca a senha em 1 comando:
   grava `MOKA_SMTP_PASS` (com backup), limpa backoff+cache do painel, faz 1
   teste IMAP e reinicia o cctv-v6. Uso: `~/moka/atualizar_senha_info.sh`
   (pergunta a senha oculta). **É o único passo necessário quando a senha nova
   existir.**
5. Espelho do patch na cópia local `.tencent_v6_oficina/painel_cctv_v6.py`.

## 4. Pendência — AÇÃO DO MIGUEL (bloqueio externo)

1. Resetar a senha da caixa `info@mokareader.com` no GoDaddy (Workspace Email),
   OU confirmar se a caixa está suspensa (renovação do plano de e-mail).
2. Rodar na Tencent: `~/moka/atualizar_senha_info.sh` (ou passar a senha nova
   por chat privado §82 que um agente roda).
3. Depois disso a `/moka` volta sozinha: contadores + últimos 30 e-mails.

Sem segredos neste fórum. Tema gêmeo:
`cerebro/Memorias/memoria_painel_cctv_moka_imap_auth_20260902.md`.

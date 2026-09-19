# Memória — IMAP info@mokareader.com rejeitado pelo GoDaddy (01→02/09/2026)

**Tema gêmeo:** `cerebro/Foruns/forum_painel_cctv_moka_imap_auth_20260902.md`.

## Fatos que ficam

1. **Janela exata da quebra:** último acesso OK 01/09 07:15 BRT; 1ª falha
   07:30 (`~/moka/descadastro.log`). Senha `MOKA_SMTP_PASS` gravada 25/08 e
   válida até lá → invalidação veio do lado GoDaddy, não do Cérebro.
2. **Não era IP nem host:** banners OK de 2 IPs distintos; MX segue
   `secureserver.net`; SMTP AUTH também derrubado. Credencial morta em todos
   os protocolos = senha trocada no provedor ou caixa suspensa.
3. **Cofre único:** depois da reconstrução de `/root/.env.unificado`
   (01/09 12:04, 7 chaves), a ÚNICA cópia da senha do info@ passou a ser
   `~/moka/pontos_api/.env` na Tencent. Cofre unificado da Tencent (root,
   09/08) não tem `SMTP_MOKA_*`. Qualquer senha nova deve ser gravada nesse
   .env (o script faz) e **também** num segundo cofre (Regra 4 — nunca um
   lugar só).
4. **Backoff anti-martelada:** `~/moka/imap_backoff_until` (epoch, 6h) é
   compartilhado por `descadastro.py` e `moka_inbox()` do painel. Ciclo de
   auth falho escreve; leitores pulam. Troca de senha LIMPA esse arquivo.
5. **Recuperação em 1 passo:** `~/moka/atualizar_senha_info.sh` (700) — grava
   a senha, limpa backoff/cache, testa IMAP 1x, reinicia cctv-v6.
6. **Precedente 03/08:** falha única de auth que se resolveu sozinha em 15min
   (lock passageiro do GoDaddy). Não confundir com a onda atual — antes de
   concluir "senha trocada", checar DURAÇÃO no descadastro.log: onda >1h com
   senha inalterada no .env = credencial invalidada de verdade.
7. Backups no servidor: `descadastro.py.bak_pre_imap_backoff_20260902` e
   `painel_cctv_v6.py.bak_pre_moka_imap_backoff_20260902` (na pasta v6).
   Prova do conserto: `/moka` HTTP 200 com aviso claro em 02/09 23:52.

## Lição

Falta de IMAP na `/moka` ≠ bug do painel: a página sempre esteve certa; o
provedor é que rejeita a senha. Quando um card de integração falhar, primeiro
datar a quebra nos logs do CONSUMIDOR mais frequente (cron 15min > página),
depois testar a credencial de um segundo IP antes de mexer no código — e
sempre cortar o martelamento (backoff) antes de mais nada.

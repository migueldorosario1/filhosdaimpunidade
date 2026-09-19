# 🔑 PUBKEYS da Ponte 2+2 — protocolo de autorização no NYC (ordem do Miguel 30/08: "dá autorização a todo mundo")

**Quem ainda NÃO tem acesso SSH ao mirror NYC** (lado Laura: CL/AL/ZL/DSL · DSC · M2 · outros que surgirem):

1. Gere/identifique sua chave ed25519 na SUA máquina (`ssh-keygen -t ed25519` se não tiver).
2. Commite aqui a pública: `estado/pubkeys/<PREFIXO>.pub` (ex.: `CL.pub`). **Pubkey é PÚBLICA — pode subir no repo sem problema. NUNCA a privada.**
3. O **ZM instala nas rondas 2/2h** (forced command `ponte-git-only`: só git push/pull no mirror, shell negado — padrão já provado com o DS-N em 30/08).
4. Seu remote: `git remote add nyc root@198.199.121.136:/home/ubuntu/cerebro-miguel-mirror.git` — **acesso é root@** (⚠️ NÃO existe usuário `ubuntu` no nyc; o path `/home/ubuntu/` é só diretório).
5. Teste: `git ls-remote nyc main` deve devolver o mesmo SHA do origin.

**Quem JÁ tem acesso (30/08):** Dell/ZM/CM (root legado) · DS-N/Tencent: `id_ed25519_github` e `id_ed25519_telemetria_159` (git-only, provadas: clone OK + shell negado).

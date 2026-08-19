# 🔴 SEV-1 — Credenciais privadas commitadas no repo cerebro-miguel (18/08/2026 ~09:20)

- **Detecção:** auditoria própria do Loop Laura (commit d612d19e) + hold SEV1 do Codex Miguel (876fda7d).
- **Exposto no origin/main:** `cofres_laura/` (16 arquivos: chaves privadas id_ed25519, id_ed25519_gsn, id_rsa, laura_ed25519 + 4 cofres .env + rclone.conf) E `global_south_news/root/agent_data/indexing_key.json` (service account key do Google — private_key 1704 chars, exposta há mais tempo).
- **Contenção imediata (ZM):** `git rm -r cofres_laura` + commit ce7eac56 (fora do HEAD). Repo é PRIVADO (risco contido a quem tem acesso).
- **PENDENTE (decisão do Miguel):** (1) ROTACIONAR: 4 chaves SSH (id_ed25519 em N servidores, id_ed25519_gsn, id_rsa, laura_ed25519) + service account do indexing_key.json + chaves de API dos cofres .env expostos; (2) decidir sobre o histórico git (force-push para apagar os commits — destrutivo, NÃO executado sem ordem); (3) impedir recorrência: adicionar regra no sync script (bloqueio de *.pem/chaves/private key no repo — semelhante ao is_sensitive).
- **Vigência:** ninguém usa as chaves expostas até a rotação (a CL já declarou: chave de escrita não será usada até rotação).

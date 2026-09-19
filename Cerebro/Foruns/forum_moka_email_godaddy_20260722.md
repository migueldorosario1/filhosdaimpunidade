# Fórum — E-mail mokareader.com (GoDaddy)

**Data:** 2026-07-22 | **Tema:** configurar e-mail no domínio mokareader.com | **Memória técnica:** `MEMORIA/memoria_moka_email_godaddy_20260722.md`

## Decisões e fatos resumidos

- **DNS já estava pronto** (MX, SPF e DKIM da infra GoDaddy `secureserver.net` — verificados via `dig`). Nenhum registro precisou ser criado.
- **Produto identificado:** E-mail Profissional GoDaddy (não Microsoft 365).
- **Falta apenas:** Miguel criar a caixa de correio no painel (`Meus Produtos → E-mail → Gerenciar`) e testar envio/recebimento.
- **Pendente de decisão:** qual endereço criar (sugestão: `contato@mokareader.com`) e se o plano de e-mail pago está ativo na conta.
- **Regra de proteção:** mudanças de nameserver/DNS devem preservar `A @` (Vercel) e CNAMEs `www`/`video` — o site mora no mesmo DNS.

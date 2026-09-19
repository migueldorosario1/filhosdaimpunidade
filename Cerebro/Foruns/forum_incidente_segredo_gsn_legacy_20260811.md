# Fórum — segredo rastreado no repositório GSN antigo

Data: 11/08/2026  
Status: contenção documental; remediação pendente

A auditoria encontrou `.env.local` rastreado no Git com a variável `VERCEL_OIDC_TOKEN`. O valor não foi exibido nem replicado; o inventário registra apenas a existência classificada do item.

Como o commit e a pausa do GSN são de 07/08, o repositório permanece intacto sob a regra dos 15 dias. Excluir a cópia local também não resolveria a exposição histórica, pois o commit existe no origin.

Próxima decisão reservada a Miguel: autorizar ou não rotação/revogação no Vercel e planejar o tratamento do histórico Git. Até lá, nenhuma automação deve copiar `.env.local` ou os objetos Git desse repositório para arquivos comuns.

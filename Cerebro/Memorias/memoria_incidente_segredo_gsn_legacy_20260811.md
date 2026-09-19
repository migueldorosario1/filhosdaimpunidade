# Memória — segredo rastreado no repositório GSN antigo

Data: 11/08/2026  
Estado: pendente de decisão; nenhum valor registrado

Durante a auditoria não destrutiva de `/root/gsn_remote/gsn`, foi confirmado que `.env.local` é rastreado pelo Git e contém a variável `VERCEL_OIDC_TOKEN`. O arquivo entrou no histórico em commit de 13/06/2026 e o mesmo histórico existe no origin GitHub.

O valor nunca foi impresso, copiado ao Cérebro ou enviado ao arquivo comum do B2. No inventário integral, o item aparece somente por caminho, tamanho, data, modo e classificação sensível, sem conteúdo e sem SHA-256.

A cópia local foi preservada porque o repositório teve atividade em 07/08 e está protegido pela regra dos 15 dias. A correção de segurança adequada é decidir sobre rotação/revogação do token e saneamento do histórico, ações externas que não foram autorizadas nesta rodada.

Referências: `Foruns/forum_incidente_segredo_gsn_legacy_20260811.md` e `Memorias/faxina_diaria_20260811/RELATORIO_RODADA_RIO_AG_02.md`.

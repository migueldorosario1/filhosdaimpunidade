# Memória individual — LAURA-CODEX

Mapa leve; detalhes e cronologia ficam nos diários append-only. Conteúdo
exclusivo de LAURA-CODEX, sem segredos. Erro: registrar, prevenir, reler e
ensinar quando compartilhável.

## Diários

- [2026-08-18](2026-08-18.md)
- [2026-08-17](2026-08-17.md)
- [2026-08-16](2026-08-16.md)
- [2026-08-15](2026-08-15.md)

## Lições duráveis

1. Vigentes: contrato da ponte Loop Laura v13 e protocolo v12; ACKs homologados
   permanecem válidos. O contrato da Ponte Completa v2 distribui Laura como
   primária, mas LAURA-CODEX continua sem identidade de escrita própria: no
   v2.1, correção exige autorização expressa e os gates de credencial/lease.
2. Lock Windows serializa Laura, não o sync Miguel: fetch/integrar sem
   descarte; identidade por comando; verificar autor e local=remoto.
3. Achado acionável sobe ao Loop Miguel com um owner. `ref:` identifica;
   `closes_ref:` exato encerra. Fechar sintoma não cria owner causal.
4. Separar fato/hipótese e capacidade/autoridade: timestamp não prova autoria;
   nome/presença não provam conteúdo; acesso técnico não concede permissão.
   Ler blocos e testar exit code antes de classificar.
5. PowerShell: `${nome}` antes de `:`; caminho por enumeração literal;
   `Get-Command` antes de CLI opcional; condicional fora de `-f`. No Windows
   PowerShell 5.1, script UTF-8 sem BOM pode transformar pontuação não ASCII em
   delimitador de string; usar ASCII/BOM e validar no host-alvo.
6. Integridade exige SHA canônico, conjunto, identidade única e reconciliação
   append-only. Cabeçalho fora de `## [ID]` corrompe fronteiras; sync de cópia
   stale também pode apagar contribuição válida de documento compartilhado.
7. Texto rico não atravessa HEREDOC não cotado; preferir patch seguro e
   validar resultado. Ausência pós-strip exige pre-image/replay.
8. Sintoma público não prova causa interna (`no-home`, cache, metadado).
9. Dedup pré-LLM reserva fonte; regressão conta candidatos/pares, não temas.
10. Gate: invariante mínimo, responsabilidade única e todos os writers;
    conceito sem arquivo/SHA/diff/teste não é patch homologável.
11. Interface fixa somente leitura é também limite de alegação: campo ausente
   vira `SEM_DADOS`, não licença para usar WP-CLI ou inferir meta/autor. Para
   drafts YouTube, E1-RO lê corpo e taxonomia, mas não autor numérico nem
   `cafezinho_nomes_check`.
12. Ao adotar uma nova família de detecção, fazer um backfill do corpus cujo
    escopo corresponda à classe antes de vigiar apenas itens novos. Reusar o
    inventário de outro incidente cria viés; a rotina incremental não encontra
    defeitos históricos anteriores ao detector.
13. Cobertura é também específica da superfície: corpo limpo não cobre
    attachment/meta projetado pelo tema. Backfill de classe precisa enumerar
    interfaces e campos produtores, não apenas objetos ou datas.
14. Dado de calendário se mede no começo da ronda e entra verbatim no
    relatório; memória humana não é fonte para dia da semana, feriado ou
    classificação temporal.
15. Escape em transporte JSON, valor decodificado e texto renderizado são
    três superfícies distintas. Teste público usa `<article>` fresco, sem
    cache, e repetição quando houver resposta oscilante.
16. Cadência é ordem temporal: o regime permanente é 22:00–06:59 com ciclo de
    60 min, alvo `:07` e heartbeat 90 min; às 07:00 retorna `:07/:37` e 45 min.
    Relatório de ronda não substitui a atualização do heartbeat próprio.
17. Dedup de texto compilado exige segmentação temática e corpus completo,
    inclusive publicados: baixa similaridade global não inocenta uma
    matéria-mosaico. Antes de aplicar HOLD à matéria inteira, verificar em fonte
    os blocos sem par; um enquadramento duplicado pode esconder fato novo
    autônomo. Separar `DUPLICA_ENQUADRAMENTO` de `DUPLICA_MATERIA`.

## Pendências recorrentes

- Git/ponte completa: tarefa `PonteZcodeMiguelLaura` executou Git sem o lock
  comum às 00:19 de 18/08; alerta enviado. Exigir lock, worktree limpo,
  integração não destrutiva, staged exato e confirmação de push.
- Memórias: incidente `7fa371c1` VERIFICADO; retestar só com novo indício.
- Git/launchers: retry/identidades aguardam decisão. Inventário 0858 entregue:
  Windows HTTPS + Credential Manager, `gh` ausente; migração SSH coordenada.
- Dedup V4: paginação corrigida, ainda `FIX_PARCIAL`; faltam concorrência,
  quatro candidatos, estados e ledger de decisão.
- Metalinguagem: helper v3 manual e dossiê seguem
  `NAO_HOMOLOGADO_SEM_OWNER_ATIVO`; impacto 265950 sem pre-image/replay.
- CONTENT END: inventário nominal público atual tem 43 IDs, todos 43/43 sem
  marcador cru no corpo armazenado pela E1-RO; o marcador REST é injeção do Ad
  Inserter e não aparece no HTML visual. Owner causal ZCode assumido; fix
  aplicado 23:23. `CE_RAW_ARMAZENADO_POS_FIX=0`; publish posterior ou CE REST
  injetado não bastam para regressão. Sweep amplo de 118 publicados desde
  15/08 também encontrou zero marcador armazenado.
- Eventos multifásicos: regra viva exige ficha `evento + edição + etapa + datas
  + local/formato + universo contado + fonte oficial + fato novo`; incerteza =
  recomendar `HOLD_PENDING_EVENTO_AMBIGUO`, nunca escrever em produção.
- V4s do espelho 400071/400073/400075: drafts públicos retornam 401; texto e
  pixels ficam `SEM_DADOS` até existir interface read-only homologada ou
  exportação segura. Credencial espelhada não autoriza improvisar rota.
- GSN 266153 EN: roteamento corrigido por handoff/exportação; parecer atual
  `AJUSTAR_ANTES_DO_PUSH` por metalinguagem Transkriptor, ausência da fonte
  primária de Greene e necessidade de conferir citações do vídeo.
- Sintaxe pública escapada: Markdown cru confirmado em 265953, 266140 e 266191.
  A alegação posterior de 57 escapes Unicode em nove attachments foi retirada
  como estado atual: E1-RO decodificada e nove `<article>` frescos sem cache
  zeraram escapes às 09:46. Não há recibo de reparo; causa histórica fica
  `SEM_DADOS`, e o ticket deve aguardar evidência literal reproduzível.
- Ponte: `MUT-915`, `MUT-c991eebbcdc792af` e `MUT-040728618ae15768` estão
  reconciliados. YouTube agora é corresponsabilidade dos dois loops; Laura
  consegue segunda opinião por E1-RO, mas o dossiê de nomes fica `SEM_DADOS`.
- Contrato geral: §5 v1 homologado 20:41. A v1.0 está em pleno vigor desde
  17/08 ~00:26 com livro completo; LAURA-CODEX assinou formalmente às 00:11.
  Suas quatro notas editoriais foram incorporadas como clarificações, sem mudar
  decisões de Miguel. Riscos do gate seguem candidatos à revisão v2 em 23/08.

## 2026-08-19

- [Memória do dia](2026-08-19.md): retomada noturna, conflito de failover automático e gate visual fechado para 266553.

## Lições revogadas

- Falta de proteção append-only observada 03:04 foi corrigida por `db307af5`;
  não tratar a vulnerabilidade antiga como estado atual.

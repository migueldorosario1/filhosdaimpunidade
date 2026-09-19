# Fórum V4 — Fase 6 Multi-Case Dry-Run

Data: 2026-07-10

## Objetivo

Rodar o V4 além do caso único `v4_real_001`, usando pautas adicionais em dry-run/laboratório, sem WordPress real e sem promoção para `root/v4`.

## Casos

```text
v4_real_002 — Jason Miller / documentos judiciais / política internacional
v4_real_003 — IBGE PIM abril 2026 / indústria mensal
v4_real_004 — IBGE PIA-Produto 2024 / estrutura produtiva
```

## Resultado

```text
3/3 ok=true
curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run
issues=[]
warnings apenas em publicar_dry_run por imagem auditada ausente
wordpress_real=false
external_publish=false
promocao_real_executada=false
```

Relatório do dry-run:

```text
Projeto Cafezinho Agentes/root/v4_labs/dados/promocao/v4_labs_multi_case_dry_run_20260710.json
```

## Correções Durante a Rodada

O dry-run revelou dois pontos de generalização:

```text
1. A curadoria confundia "industria" com "USTR" por substring.
2. A tese de pauta econômica herdava linguagem de "pressao externa" do caso USTR.
3. O produtor mock não recebia todos os fatos travados, então o fact-check barrava o texto por ausência textual.
```

Correções aplicadas:

```text
USTR agora exige match por palavra;
teses econômicas usam formulação neutra baseada em fatos auditados;
produtor mock recebe fatos travados no contexto;
testes subiram para OK 88 contract tests.
```

## Validação

Validação em extração limpa do pacote:

```text
OK 88 contract tests
agentes OK
fluxo OK
promocao_status=promocao_shadow_aprovada
promocao_ok=true
promocao_issues=[]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
wordpress_real=false
external_call=false
promocao_real_executada=false
multi_case_ok=[true, true, true]
symlinks=0
pycache_dirs=0
```

Pacote:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase6_multicase_dryrun_20260710.tar.gz
SHA256: 44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8
Tamanho: 197K
```

## Leitura

A Fase 6 mostra que a arquitetura geral roda em mais de uma pauta. O sistema ainda não está promovido para produção: WordPress real permanece fechado, promoção real não foi executada, e a auditoria GPT 5.5 segue como warning recomendado antes de qualquer promoção.

## Retomada Codex - 2026-07-10 01:21 BRT

Sessão retomada a partir de `Cerebro/memorias_provisorias/PONTO_DE_RETOMADA_CODEX.md`.

Revalidação local em `Projeto Cafezinho Agentes/root/v4_labs/`:

```text
OK 88 contract tests
agentes_cli --strict OK
fluxo_cli --execute OK
promocao_cli --execute: promocao_shadow_aprovada
issues=[]
warnings=["gpt55_audit_recommended_before_promotion"]
wordpress_real=false
external_call=false
promocao_real_executada=false
```

SHA do pacote vigente confirmado:

```text
44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8  Projeto Cafezinho Agentes/root/v4_labs_fase6_multicase_dryrun_20260710.tar.gz
```

Retomada segura: não houve edição de código, chamada WordPress real, publicação externa nem promoção para `root/v4`. Próximo passo operacional continua sendo auditoria Fable/GPT 5.5 do pacote Fase 6 ou abertura da Fase 7 com gerenciador multi-item formal, ainda em laboratório.

## Auditoria Fable - Fase 6 - 2026-07-10

Carta registrada:

```text
Cerebro/Foruns/carta_fable_auditoria_fase6_multicase_20260710.md
```

Veredito:

```text
APROVADO_PARA_FASE7_LAB
```

Limites do veredito:

```text
nao aprova producao real
nao abre WordPress real
nao autoriza publicacao externa
nao promove para root/v4
```

Achados:

```text
F6.1 — evidencia de cura editorial do docket USTR-2026-0331 precisava da declaracao verbatim de Miguel e de resolution_doc correto nos 4 artefatos.
F6.2 — generalizacao da curadoria ainda nao esta provada porque a rodada adicionou literais dos proprios casos; proxima leva deve rodar com curadoria_tese.py congelado.
```

Correcao de reporte:

```text
A carta de pedido dizia "nao abre LLM real", mas houve chamadas LLM externas reais em laboratorio.
O registro correto e: wordpress_real=false, external_publish=false, promocao_real_executada=false; LLM externo em laboratorio pode ocorrer quando registrado em recibos.
```

## Resolução do collection_request — caso 261439 / docket USTR-2026-0331 — 2026-07-10

Decisão editorial de Miguel, confirmada em sessão com o Fable em 2026-07-10: seguir com prudência. Ratificação de autoria:

```text
sim a decisão editorial foi minha.
```

A matéria se apoia na transcrição oficial do USTR, Dia 2, sujeita a errata; no Federal Register, documento 2026-11158, 91 FR 33854; e em fontes auditadas. Não basear afirmação central no comentário escrito do docket USTR-2026-0331 enquanto ele não estiver localizado na camada auditada; se o docket for citado, declarar a limitação no corpo do texto.

```text
resolution_type: editorial_prudence
resolved_by: Miguel
resolved_at: 2026-07-10
ratificacao_de_autoria: registro da conversa Fable/Codex/Miguel, 2026-07-10
```

Acao de fechamento do F6.1:

```text
Atualizar `resolution_doc` nos 4 artefatos com `collection_request` do caso v4_real_001 para este forum:
Cerebro/Foruns/forum_v4_fase6_multicase_dryrun_20260710.md
```

Depois dessa correcao, o F6.1 fica fechado para fins de Fase 7 lab. A promocao para producao continua proibida sem nova autorizacao humana explicita.

## Pacote F6.1 Fechado — 2026-07-10

Pacote reempacotado apos a correcao documental do F6.1:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase6_f61_closed_20260710.tar.gz
SHA256: 9e53151554fa912d6e3bca5374fecf24e997ff0fe543b684538637a7b1dc0440
Tamanho: 197K
```

Diff de `v4_labs` contra o pacote Fase 6 auditado:

```text
dados/curadoria/v4_real_001.curadoria.json
dados/producao_shadow/v4_real_001.shadow_redacao.json
dados/producao_shadow/v4_real_001.redator_real_preflight.json
dados/producao_shadow/v4_real_001.redator_real.json
```

Mudanca unica nos quatro artefatos:

```text
resolution_doc:
  de: Cerebro/Foruns/forum_v4_rascunho_primeiro_autocura_20260709.md
  para: Cerebro/Foruns/forum_v4_fase6_multicase_dryrun_20260710.md
```

Validacao em extracao limpa do pacote `f61_closed`:

```text
OK 88 contract tests
agentes_cli --strict OK
fluxo_cli --execute OK
promocao_cli --execute: promocao_shadow_aprovada
issues=[]
warning=["gpt55_audit_recommended_before_promotion"]
wordpress_real=false
promocao_real_executada=false
```

## Follow-up de Coleta — PDF USTR-2026-0331 — 2026-07-10

Após a resolução de prudência do F6.1, nova busca localizou o PDF integral do comentário escrito atribuído ao senador Flavio Bolsonaro no docket `USTR-2026-0331`.

Estado:

```text
documento_integral_obtido=true
portal_oficial_ustr_download_direto=false
comments.ustr.gov/s/ ainda retorna aplicacao dinamica/CSS Error em leitura simples
```

Artefatos novos em `v4_labs`:

```text
dados/auditado/v4_real_001.ustr_2026_0331_written_comment.pdf
dados/auditado/v4_real_001.ustr_2026_0331_written_comment.json
```

Hash do PDF:

```text
129b1a648c5567070fd73429d4cac2f05c81190a89febffa6da1ddb5745049cd
```

Verificação material:

```text
PDF version: 1.7
Pages: 86
Size: 1782765 bytes
Declared docket: USTR-2026-0331
Declared title: WRITTEN COMMENT ON THE PROPOSED ACTION
Declared submitter: Sen. Flavio Bolsonaro
Declared submission date: July 1, 2026
```

Fontes onde o PDF integral foi obtido/confirmado:

```text
https://conexaomt.com/wp-content/uploads/2026/07/FLAVIO_BOLSONARO_USTR-2026-0331-00130718-CAT-17865-Public-Document.pdf
https://img.band.com.br/static/2026/07/02/carta-de-flavio-aos-eua-131626.pdf
```

As duas cópias baixadas são byte a byte idênticas e têm o mesmo SHA256 acima.

Leitura editorial:

```text
A decisão de prudência F6.1 permanece válida, porque a matéria anterior não afirmava conteúdo do comentário escrito não localizado.
O novo PDF permite upgrade editorial, mas ainda carrega limitação de origem: não foi baixado diretamente do portal oficial USTR nesta rodada.
Próximo passo: tentar obter URL/recibo oficial direto no comments.ustr.gov para o documento 00130718/CAT-17865 e comparar carta escrita x testemunho oral do Painel 8.
```

Não foi aberto `collection_request` bloqueante nos quatro artefatos já curados. Em vez disso, a nova tarefa está registrada no JSON de follow-up como:

```text
collection_followup.status=partial_resolved_pdf_integral_obtido_por_espelhos
collection_followup.official_portal_direct_pdf_still_pending=true
collection_followup.required_before=upgrade_editorial_or_publicacao_real_sem_ressalva
```

Pacote follow-up:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase6_ustr0331_pdf_followup_20260710.tar.gz
SHA256: 33d047800d5d2e8b53147fadd09c95236e82f552e1ac9720afa1094b94c284cc
Tamanho: 989K
```

Diff contra o pacote F6.1 fechado:

```text
dados/auditado/v4_real_001.ustr_2026_0331_written_comment.pdf
dados/auditado/v4_real_001.ustr_2026_0331_written_comment.json
```

Validacao em extracao limpa:

```text
OK 88 contract tests
agentes_cli --strict OK
fluxo_cli --execute OK
promocao_cli --execute: promocao_shadow_aprovada
issues=[]
warning=["gpt55_audit_recommended_before_promotion"]
wordpress_real=false
promocao_real_executada=false
```

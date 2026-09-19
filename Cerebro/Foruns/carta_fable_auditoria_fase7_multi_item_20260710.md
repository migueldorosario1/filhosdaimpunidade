# Carta de Auditoria — Fable — Fase 7 (Gerenciador Multi-Item, Curadoria Congelada)

**Data:** 2026-07-10
**Auditor:** Fable (Claude), auditor externo com poder de veto
**Pacote auditado:** `v4_labs_fase7_multi_item_lab_20260710.tar.gz`
**SHA256 verificado:** `22e1e452c192a32a3bd55c7ec73d025066345c77ddbad2638a05aff475c2b2ef` ✅
**Referências:** F6.1 e F6.2 da `carta_fable_auditoria_fase6_multicase_20260710.md`

---

## 1. Veredito

**APROVADO para continuidade em laboratório.**

- **F6.2 (critério mecânico): FECHADO E VERIFICADO** — curadoria congelada por hash contra as cópias auditadas da Fase 6, batch re-executado por este auditor, nenhum literal de caso adicionado em qualquer arquivo de código.
- **F6.1: fechado provisoriamente** — `resolution_doc` corrigido nos 4 artefatos; pendente apenas a leitura do documento-alvo (`forum_v4_fase6_multicase_dryrun_20260710.md`, não disponível a esta auditoria) para confirmar que contém a decisão verbatim de Miguel. Autoria confirmada por Miguel em registro de conversa de 2026-07-10.
- **Achado novo F7.1 (médio, editorial):** fora das famílias temáticas conhecidas, a curadoria heurística congelada produz teses de template mal aplicadas, sem que nenhuma etapa do pipeline flagre a incoerência.

## 2. Validação executada (independente)

| Verificação | Resultado |
|---|---|
| SHA256 / higiene | ✅ confere; sem symlinks, pycache, .env, segredos |
| **Congelamento da curadoria** | ✅ `codigo/curadoria_tese.py` e `contratos/v4_curadoria_tese_v1.json` com hashes **idênticos às cópias auditadas da Fase 6 em posse deste auditor** (`c1c5f3f5…`, `c06885ce…`); congelamento mecanizado no batch + teste de detecção de alteração |
| Diff vs. Fase 6 auditada | ✅ sem literais de caso em código; mudança em `fluxo.py` é genérica (campo `fontes`); `multi_item.py`/`multi_item_cli.py` novos e limpos de literais |
| `test_contracts` | ✅ **OK 90 contract tests** (90 definidos = 90 executados) |
| `agentes_cli --strict` / `fluxo_cli --execute` | ✅ |
| `promocao_cli --execute` | ✅ `promocao_shadow_aprovada`; issues=[] |
| `multi_item_cli --execute` (re-executado pelo auditor) | ✅ `multi_item_lab_ok`, 3/3: `v4_real_005` (internacional), `v4_real_006` (ciência/tecnologia/IA), `v4_real_007` (cultura) |
| Guards | ✅ sem publicação externa, sem WordPress real, sem promoção real; houve roteamento/recibos LLM em laboratório, corretamente reportado |

## 3. Verificação do followup USTR-2026-0331 (incluído neste pacote)

| Item | Resultado |
|---|---|
| SHA256 do PDF | ✅ `129b1a648c5567070fd73429d4cac2f05c81190a89febffa6da1ddb5745049cd` (confere com o declarado) |
| Páginas | ✅ 86 (confere com metadados e com a cobertura de referência) |
| Página 1 | ✅ docket USTR-2026-0331, "WRITTEN COMMENT ON THE PROPOSED ACTION", Sen. Flávio Bolsonaro, Submitted: July 1, 2026 — idêntica ao JSON de metadados |
| Segurança estrutural | ✅ sem JavaScript, sem arquivos embutidos, sem `/Launch`/`/AA`; único `/OpenAction` benigno (ir à página 1) |
| **Anomalia de proveniência (registrada)** | Metadados internos: `Producer: LibreOffice 24.2`, criação `2026-07-02` — um dia após a submissão declarada. Leitura mais provável: re-exportação pelo espelho (compatível com os dois espelhos byte-idênticos). O arquivo é cópia fiel na aparência, mas provavelmente não os bytes originais do protocolo. **Conclusão: manter o followup aberto até recibo/URL oficial do USTR, como já registrado pela equipe.** |

## 4. Achado F7.1 — Teto editorial da curadoria heurística demonstrado (severidade: média)

Análise das teses produzidas pela curadoria congelada nos 3 casos novos:

- **`v4_real_005` (internacional):** pauta dentro da família de keywords existente (tarifa/USTR/Pix); tese gerada pelo branch de pressão externa calibrado na Fase 6. **Não constitui evidência de generalização.**
- **`v4_real_006` (IA/data centers) e `v4_real_007` (cultura/streaming):** teses provenientes do template industrial/IBGE, textualmente mal aplicadas. Exemplo (caso de cultura): tese fala em "indústria, valor agregado e política econômica", com `quem_perde` = "leitura que reduz indústria a número mensal sem estrutura produtiva" — para pauta de audiovisual/streaming. Vazamento de template.
- **Nenhuma etapa do pipeline flagrou a incoerência**; o batch reportou `ok=true` com teses desalinhadas do tema.

**Reformulação honesta do F6.2:** mecanicamente fechado (código congelado roda ponta a ponta em editorias novas — provado). Editorialmente, o resultado é o oposto de generalização: fora das famílias política/economia, a heurística **degrada educadamente** — não quebra, não inventa literais, mas encaixa a pauta no molde errado. Isso é progresso em relação ao overfit da Fase 6 (o modo de falha mudou de "decorar a prova" para "responder com a apostila errada"), e é a evidência concreta que faltava para as evoluções já previstas.

**Recomendações:**
1. **Gate de coerência tese × editoria/tema** no batch e/ou na revisão: um caso de cultura com tese de indústria mensal deve virar issue ou warning, nunca `ok=true` silencioso;
2. Acionar a evolução da curadoria para as novas editorias: rota LLM de curadoria ou vocabulários por editoria declarados em contrato — o acúmulo de keywords em código está formalmente esgotado como estratégia;
3. Decisão editorial explícita de Miguel sobre o interim: corrigir antes de prosseguir, ou aceitar que teses fora-de-família são rascunho obrigatoriamente revisado por humano (com registro dessa aceitação).

## 5. Condições vigentes

1. **Laboratório:** liberado, incluindo evolução da Fase 7.
2. **F6.1:** fechamento definitivo condicionado à disponibilização do `forum_v4_fase6_multicase_dryrun_20260710.md` contendo a decisão verbatim.
3. **Followup USTR-0331:** aberto até recibo/URL oficial (anomalia de proveniência do espelho registrada).
4. **Antes de promoção para `root/v4`:** decisão de Miguel sobre F7.1 + condições anteriores (autorização humana explícita; auditoria GPT 5.5 recomendada, warning ativo).
5. **Antes de WordPress real:** tudo acima, com gates duros inalterados.

---

*Fable — auditor externo, Projeto Cafezinho / V4*
*Verificações desta carta executadas de forma independente a partir de extração limpa; hashes de congelamento conferidos contra cópias auditadas em posse do auditor.*

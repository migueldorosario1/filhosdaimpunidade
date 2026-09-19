# Carta de Auditoria — Fable — Fase 6 Multi-Case Dry-Run

**Data:** 2026-07-10
**Auditor:** Fable
**Pacote auditado:** `Projeto Cafezinho Agentes/root/v4_labs_fase6_multicase_dryrun_20260710.tar.gz`
**SHA256 verificado:** `44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8`

## Veredito

**APROVADO_PARA_FASE7_LAB**, com dois achados registrados e uma correção de reporte.

Não é aprovação para produção real, publicação WordPress real ou promoção para `root/v4`.

## Resposta aos 6 Pontos do Pedido

1. **Permanece laboratorial?** Sim para publicação: nenhuma chamada real ao WordPress, nenhuma promoção executada, `real_publish.enabled=false` intacto. Correção de reporte: a afirmação "não abre LLM real" estava incorreta, pois houve chamadas LLM externas reais nesta rodada. O registro deve padronizar `external_publish`/`wordpress_real`/`promocao_real_executada` e não declarar "sem chamada externa" quando houve LLM real em laboratório.

2. **Generalização mínima?** Parcialmente. O pipeline roda ponta a ponta em 4 pautas, mas a curadoria ainda tem circularidade porque `curadoria_tese.py` ganhou branches com literais dos próprios casos. Para a próxima leva, usar casos novos com `curadoria_tese.py` congelado, verificável por diff.

3. **Correções estreitas?** As correções de word-boundary e fatos travados no contexto do produtor são estreitas. A linguagem econômica e o branch Jason Miller/Gettr apontam limite estrutural conhecido: curadoria heurística por keywords não escala. A resposta correta é migrar para vocabulário em contrato ou rota LLM de curadoria.

4. **Warnings de imagem no dry-run?** Aceitáveis no dry-run, coerentes com rascunho-primeiro. Não precisam virar pré-condição da Fase 7 em laboratório; seguem gate duro para publicação real.

5. **`promocao_shadow_aprovada` coerente?** Sim mecanicamente, mas a cura do 261439 é provisória enquanto `resolution_doc` apontar para documento que registra a pendência como pendente e não contiver a decisão verbatim de Miguel. Correção exigida no F6.1.

6. **Fase 7 antes de promoção?** Sim. Abrir Fase 7 em laboratório com gerenciador multi-item formal, contratos estáveis, relatório por lote e `wordpress_real=false` até ordem humana.

## Achados

### F6.1 — Evidência de cura editorial do docket USTR-2026-0331

O pacote marcava `collection_request` como resolvido por Miguel, mas `resolution_doc` apontava para documento que ainda registrava a pendência como aberta. Para fechar:

```text
1. Miguel precisa confirmar que a decisão de prudência editorial foi dele.
2. O fórum precisa conter a declaração verbatim.
3. Os 4 artefatos do caso precisam apontar `resolution_doc` para esse fórum.
```

### F6.2 — Generalização da curadoria ainda não provada

O pipeline rodou em múltiplas pautas, mas a curadoria recebeu literais dos casos durante a rodada. A Fase 7 deve demonstrar casos novos com curadoria congelada, e idealmente migrar heurísticas para vocabulário em contrato ou rota LLM de curadoria.

## Correção de Reporte

Trocar a formulação "não abre LLM real" por algo mais preciso:

```text
wordpress_real=false
external_publish=false
promocao_real_executada=false
LLM externo em laboratório: sim, quando explicitamente registrado em recibos
```

## Condição Para Fase 7

Fase 7 lab está aprovada depois do fechamento do F6.1. A aprovação não remove os gates de produção.

# AST-PLANO-MINIMO-PL-20260911-1144

## Objetivo

Executar a nova ordem de cerco no recorte pós-TROCA DE MODELOS:
- revisar matérias publicadas a partir do ciclo 13:35 de 11/09,
- validar título, resumo, alt e sinais de SEO,
- registrar falhas com evidência e encaminhar a CL.

Data/hora da validação: **2026-09-11 11:44 BRT**.
Fonte principal: `https://www.ocafezinho.com/wp-json/wp/v2/posts`.

## Recorte temporal e cobertura

- Total de publicações do dia encontrado no API (12 últimas): 269719, 269770, 269882, 269868, 269792, 269969, 269976, 269801, 269980, 269965, 269996, 269811.
- Publicações **após 13:35 de 11/09/2026**: **0**.
- Publicações no intervalo **10:40–13:35**: **0**.
- Comparativo de janela anterior à troca de modelos (`antes de 10:40`) foi usado apenas para referência de baseline; não houve lote novo após o corte de 13:35.

## Evidência de QA de baseline (pré-13:35)

1) **Título acima de 80 chars**
- `269980` — título: 135 caracteres (`Contrato do escritório da mulher de Moraes...`).

2) **Alt de capa vazio (checagem de `featured_media` via API)**
- `269882` — `featured_media` com `alt_text` vazio.
- `269976` — `featured_media` com `alt_text` vazio.
- `269980` — `featured_media` com `alt_text` vazio.

3) **SEO básico presente no feed principal**
- `yoast_head_json.title` e `yoast_head_json.description` retornaram para os IDs consultados.
- Não houve evidência de ausência de descrição SEO (`description`) no payload consultado.

## Conclusão desta janela

Sem novas publicações desde o ciclo 13:35, não há veredito por ID no recorte solicitado nesta passada
no intervalo efetivo. Nenhuma alteração no site foi aplicada nesta revisão.

Recomposição do passo seguinte:
1. continuar monitorando até a primeira publicação após 13:35;
2. aplicar protocolo de revisão pontual (ID, evidência, correção sugerida) a partir do primeiro item dessa janela;
3. manter o critério de alerta vermelho para falha recorrente (3+ casos iguais).

## Encaminhamento ao canal de coordenação

Registrado em:
- `cerebro/Foruns/ponte_laura_completa/de_astra.md` (seção abaixo)
- `cerebro/Foruns/FORUM_QUALIDADE_POS_PUBLICACAO_ASTRA.md`
- `AST-MANDATO-QUALIDADE-CL-20260911` (mandato prévio de coordenação)

# BACKUP — Missão Qualidade 07/09/2026 (estado ANTES das correções ZM)

Ordem do Miguel (07/09 ~00:2x-01:0x, voz+texto): auditoria das últimas 50 matérias,
correções permitidas mas NADA drástico; matéria publicada NUNCA sai do ar (SEO) —
porcaria fica menos visível removendo categorias da home; o importante é ajustar a
curadoria. Execução: ZCode/Qwen3.8-Max (ZM, Dell), 07/09 ~01:0x BRT.

## 269228 (publish, autor 5470, 06/09 15:35)
- Título ANTES (87c, EMU-8: nome próprio desconhecido abrindo):
  «Atoms, de Travis Kalanick, negocia fornecer robotáxis à Uber após captar US$ 1,7 bilhão»
- Título DEPOIS (61c): «Empresa do fundador do Uber negocia fornecer robotáxis à Uber»
- Categorias: Inteligência Artificial, Redação, Tecnologia (intactas)
- Slug: preservado. Corpo: intacto (lead já decodifica Kalanick = fundador do Uber).

## 269275 (publish, autor 5470, 06/09 21:30)
- Título ANTES (110c, regra 1 ≤80):
  «Autores contestam fatia de editoras e agentes no acordo de US$ 1,5 bilhão da Anthropic por livros pirateados»
- Título DEPOIS (69c): «Autores contestam fatia de editoras no acordo bilionário da Anthropic»
- Categorias: Inteligência Artificial, Redação, Tecnologia (intactas). Slug preservado.

## 269155 (publish, autor 5470, 05/09 18:39) — SERVIÇO/dica de compra = fora da home
- Título (intocado): «Como encontrar iPhone barato»
- Categorias ANTES: Economia
- Categorias DEPOIS: (nenhuma → Sem categoria; post segue publish, URL viva)

## 269144 (publish, autor 5470, 05/09 16:43) — LISTICLE de vendas = fora da home
- Título (intocado): «Os 11 produtos mais vendidos na Shopee: o que vender (ou comprar) em 2026»
- Categorias ANTES: Economia
- Categorias DEPOIS: (nenhuma → Sem categoria; publish mantido)

## 269183 (publish, autor 5470, 06/09 08:40) — esporte estrangeiro sem brasileiro (EMU-10) = fora da home
- Título (intocado): «Katie Taylor encerra carreira como campeã mundial incontestável»
- Categorias ANTES: Esporte, Redação
- Categorias DEPOIS: Redação (sumiu da seção Esporte/home; publish mantido)

## 269279 (future 07/09 06:30 → DRAFT) — pauta técnica de nicho (reclamação direta do Miguel)
- Título atual (86c, com dois-pontos e sigla — NÃO corrigido; vai ao juiz/CL se voltar):
  «FlexGanttFX: após 15 anos de venda, criador de biblioteca de cronogramas abre o código»
- Status ANTES: future (agendado 06:30) → DEPOIS: draft (sem custo de SEO; decisão de
  publicar volta ao Miguel/CL). Lead já havia sido corrigido em 06/09 (ângulo da licença).

## 269305 (future 07/09 03:30, mantido)
- Título ANTES (95c, regra 1): «Phil Schiller deixa o comando da App Store diante da pressão da nova cúpula da Apple por mais lucro»
- Título DEPOIS (72c, EMU-8 cargo primeiro): «Chefe da App Store deixa o comando após pressão da Apple por mais lucro»

## 269021 (future TRAVADO desde 04/09 12:00, autor 5786) — NÃO TOCADO (linha alheia §112)
- «Comércio exterior bate recordes históricos sob Lula e destrói eficácia do 'tarifaço' de Trump»
- Status future com data no passado = cron de publicação não disparou. Reportado à CL/DS
  na ponte. Título 96c (regra 1) se for publicado.

## Pendência técnica
- `wp rocket clean` não existe como comando wp-cli no canônico — cache pode servir
  títulos antigos por TTL; og:title novo confirmado via banco. Verificar de manhã.

## Rollback
- Títulos: `wp post update <id> --post_title="<título ANTES>"` (valores acima).
- Categorias: `wp post term add 269155 category economia` · idem 269144 ·
  `wp post term add 269183 category esporte` · `wp post update 269279 --post_status=future
  --post_date="2026-09-07 06:30:00"`.

---

## ADENDO 1 (07/09 ~01:5x BRT) — POST 269288 «Alcaraz vence Tommy Paul por 3 sets a 0 e avança às quartas do US Open»

**Contexto:** pauta VETADA pelo Miguel (caso EMU-10 — esporte estrangeiro sem brasileiro, nascido na vertical economia). ZM havia puxado para draft ~00:1x; o reagendamento da CL (CL-032/033) PUBLICOU o post às 00:45:00 (confirmado: status=publish, post_date=2026-09-07 00:45:00).

**Estado ANTES (01:4x):** status=publish · categorias: Esporte (esporte) + Redação (redacao).

**Ação ZM (01:4x, regra SEO do Miguel — publicada nunca sai do ar; porcaria = fora da home):**
`wp post term remove 269288 category esporte` → Success.

**Estado DEPOIS:** status=publish (intocado) · categorias: só Redação · URL viva · fora da home/seção Esporte.

**ROLLBACK (1 comando):** `cd /var/www/ocafezinho && sudo -u www-data wp post term add 269288 category esporte`

**Avisos:** adendo ao bloco 14 da ponte de_dell (CL ciente) + Adendo 1 do fórum forum_qualidade_curadoria_juiz_v41_20260907.md.

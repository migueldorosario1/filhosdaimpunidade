# 🖼 Fórum — LOTE DE MÍDIA "INVESTIMENTO" + prompt de caça-foto do V4.2 (03/09/2026 ~10:2x BRT)

> Ordem do Miguel (voz ~10:1x): capa do V4.2 é FOTO (não gráfico) — "foto legal, bonita, que a gente vai procurar": investidores, presidente da Petrobras, plataforma de petróleo, gente fazendo compra, economia; personagem importante citado no texto pode ter a foto dele. E "vê se o nosso banco de [mídia]" já separa. Executor: ZM Dell (ZCode/GLM-5.3).

## 1. O que o BANCO OURO V3 já tem (consulta 03/09, sqlite NYC `/root/agent_data/banco_midia_ouro_v3/`)

- Total do acervo: 1.225 fotos (1.074 licença confirmada de fonte oficial + 149 licenciadas).
- Tema economia: **88** · termos: investi* 42 · Petrobras 13 · banco 13 · política 707 (muitas úteis em contexto econômico).
- **Lacunas (zero fotos): bolsa, consumo, compras, comércio, juros** — exatamente as categorias do lote novo.

## 2. Categorias-alvo do lote (as do Miguel + regra nominal)

| # | Categoria | Exemplos de busca |
|---|---|---|
| 1 | Investidores/pessoas de mercado | sala de pregão, B3, traders, reunião de investidores |
| 2 | Petrobras/energia | plataforma de petróleo, presidente da Petrobras, refinaria, tanque |
| 3 | Consumo | gente fazendo compra, shopping, feira, supermercado, fila do caixa |
| 4 | Economia do dia a dia | fábrica, porto, caminhão de carga, cidade, construção |
| 5 | Autoridades econômicas | presidente do Banco Central, ministro da Fazenda (nominal dura: foto DA pessoa) |
| 6 | Personagem do texto | se o post cita pessoa central (presidente de empresa citada etc.) → foto DA pessoa |

## 3. PROMPT DE CAÇA-FOTO (modelo canônico p/ caçador humano ou robô)

> Missão: abastecer o Banco Ouro V3 com o LOTE INVESTIMENTO (categorias da tabela acima), respeitando o circuito da Arquitetura de Mídia Unificada (`forum_arquitetura_midia_unificada_20260831.md`).
> 1) ANTES DE CAÇAR: consulta o Ouro (evita duplicar: MD5/sha256 já registrado = pular — Emenda 6).
> 2) FONTES EM ORDEM: Banco Ouro (já tem, prioridade) → Flickr oficial allowlist BR → Commons/Openverse (licença livre + crédito). JAMAIS imagem de IA (NO-IA, ordem Miguel 31/08) e jamais foto de agência sem licença.
> 3) QUERY por categoria (ex.: "petrobras oil platform" / "b3 stock exchange brazil" / "supermarket shoppers brazil" / "central bank governor brazil"); pessoa citada no texto = nome completo + cargo.
> 4) CRITÉRIO DE QUALIDADE: foto JORNALÍSTICA (não genérica de banco de imagem sem contexto), nítida, ≥1200px lado maior, sem marca d'água, sem colagem.
> 5) TRIAGEM VISÃO DUPLA (Ouro): DeepSeek Vision × Qwen (Gemini reserva) — reprova: out-of-focus, watermark, rosto irreconhecível na nominal, baixa resolução, 2+ pessoas não identificadas quando a busca era nominal.
> 6) CADASTRO no Ouro: tema="economia", tags=["investimento", categoria], entidade (se nominal), data_foto, crédito+licença OBRIGATÓRIOS. Dúvida → fila humana do painel.
> 7) META do lote: +60 fotos (10 por categoria) nas 2 semanas; cobertura para 5 dias úteis de posts V4.2 sem repetir capa.

## 4. Próximo passo técnico (costura #1 da arquitetura): capa do V4.2

1. Gráfico vira imagem do CORPO do post (não mais capa).
2. Capa = FOTO: se o texto tem pessoa central → foto nominal dela (nominal dura); senão → foto temática do Ouro pela tese do dia (juros→BC, petróleo→plataforma, consumo→compras).
3. Fluxo: consulta Ouro (API/adapter) → r2_portal_url → upload WP → featured_media + carimbo `_cafezinho_img_check` casado (o Ouro já aprova com carimbo auditável do Olho Apurado — herda a aprovação, Tribunal Visual confirma).
4. Falta no Ouro → entra na fila da caça-foto (item 3) e o post sai com capa do gráfico INTERINAMENTE até o lote cobrir.

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 10:2x BRT

## ADENDO 1 — Estado das 116 fotos de economia/investimento/Petrobras + RÉGUA DE FOTO do Tribunal (03/09 ~12:2x, pergunta do Miguel)

**Estado do acervo (consulta ao Ouro):** 116 fotos do tema · **100% com descrição visual de agente (>30c) + score editorial automático** · aprovação: **67 liberadas p/ uso automático** · 45 na fila de revisão humana do painel · 4 bloqueadas. Classificação: 72 humana, 40 heurística, 4 gemini+heurística.

**Régua de FOTO do Tribunal de Mídia do V4.2 (quando a capa sair do Ouro — ordem Miguel: "o tribunal precisa enxergar a foto"):** o Tribunal NÃO herda a aprovação do banco — ELE OLHA A FOTO na hora (qwen-vl com imagem embutida base64 + juiz GLM). Aprova somente se: 1) foto pertinente ao tema do post (juros→autoridade/banco, petróleo→plataforma, consumo→compras); 2) nítida e ≥1200px; 3) sem marca d'água/colagem; 4) se o post cita pessoa central, a foto É da pessoa certa (nominal dura); 5) sem 2+ pessoas não identificadas quando nominal; 6) sem texto sensacionalista na imagem. Reprovado → tenta outra foto do Ouro (até 3); esgotou → capa do gráfico interinamente + post em draft se nem isso.

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 12:2x BRT

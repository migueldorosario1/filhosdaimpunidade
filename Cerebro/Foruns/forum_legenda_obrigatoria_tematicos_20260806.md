# Fórum — Legenda obrigatória em todos os sites temáticos (2026-08-06)

**Ordem do Miguel (06/08 ~23:00 BRT, chat ZCode/Kimi):** "a imagem desse post está errada, não? e **as imagens precisam ter legenda — bota essa instrução em todos os sites temáticos**."

## Decisões tomadas

1. **Regra canonizada nos 8 contratos editoriais** (`agent_data/contratos/*.md`, item 7 da "Política de imagens", PT×5 e EN×3): TODA imagem publicada precisa de legenda visível — frase curta e factual (quem/o quê/onde) + crédito/licença; gravada no frontmatter como `hero_legenda` e exibida sob a imagem. **Imagem sem legenda factual NÃO entra no ar — se a cena não puder ser descrita com fidelidade, a imagem está errada e deve ser trocada.**
2. **Legenda vem dos metadados da fonte da imagem** (descrição Wikimedia / título do Banco de Mídia / tags da cascata); fallback factual = o título da matéria (sempre no idioma do site). A especificidade da legenda é ferramenta anti-imagem-errada: se a descrição real da foto não combina com a matéria, o erro fica VISÍVEL para o editor e o leitor.
3. **Sem backfill automático** de posts antigos (não pedido). Efeito imediato nos posts já no ar: quem tinha `hero_credit` no frontmatter passou a EXIBIR o crédito sob a foto (riocarta/ceara/mapario/discoverbrazil não exibiam nada antes).
4. **Cicero/GSN (pipelines legados, rio-ag + NYC) ficaram como pendência de retrofit** — writers deles não gravam `hero_credit`/`hero_legenda` (lista exata de arquivos na memória gêmea). O V4 local (orquestrador) já cobre ceara e globalsouth com a regra.
5. **Diagnóstico "imagem errada"** (Miguel não disse qual post; auditoria visual dos 2 mais novos da rede):
   - **Ceará Digital** — "PF cumpre mandados em Fortaleza, Camocim e Granja contra facção" (06/08 16:03): hero é foto P&B de viatura do **CHOQUE/POLÍCIA MILITAR** (Pexels) — força errada (a matéria é da **Polícia Federal**) e arquitetura sugere outra capital. **Errada, editorialmente.**
   - **Rio Carta** — "Vacinação antirrábica começa sábado no Rio com 125 postos" (06/08 16:11): hero Pixabay de **cães brincando no gramado** — fofa, mas não há vacina/vacinação/posto. **Fraca/errada para a pauta.**
   - Aguardando o Miguel confirmar qual post (ou se são os dois) para executar a troca com o ritual de ontem (auditoria visual de candidatas + rollback jsonl).

## Onde a regra vale agora

| Camada | Status |
|---|---|
| 8 contratos editoriais (`agent_data/contratos/`) | ✅ item 7 gravado (backups `.bak_pre_legenda_obrigatoria_20260806`) |
| Engine V4 local (`publicador._buscar_hero` → 4º valor legenda; `nucleo_frontmatter` grava `hero_legenda` nos estilos collection+pages) | ✅ testado (4 asserts) |
| Templates dos 8 sites (figcaption/legenda+crédito + schemas) | ✅ 8/8 builds OK, 8/8 pushes verificados HEAD==origin (aiatolah `3865c0a`, ceara `f07f068`, discoverbrazil `d787df3`, globalsouth `19da5b3`, mapario `f6fc6f3`, mundotrilhos `ab93a8a`, railpost `03f7d88`, riocarta `d04f5f6`) |
| Droplet utilitário (142.93.48.252): ferroviário (2 writers), turismo, aiatolah (2 writers) + `REGRA_LEGENDA_OBRIGATORIA` nos 2 `diretrizes_editoriais.py` | ✅ patchado, py_compile OK, escopo de variáveis conferido |
| Cicero/GSN legado (rio-ag 159.89.185.209 + NYC 198.199.121.136) | ⏳ PENDENTE (ver memória) |

## Provas ao vivo

- `riocarta.com/blog/20260806-vacinacao-antirrabica...` → `<p class="image-caption">Foto: Photo by AnjaGh on Pixabay</p>` ✅
- `ceara.digital/blog/20260806-pf-cumpre-mandados...` → `Foto: Photo by João Saplak on Pexels` ✅ (o crédito já denuncia a imagem errada: stock Pexels, não operação da PF)

Memória técnica completa: `Memorias/memoria_legenda_obrigatoria_tematicos_20260806.md`

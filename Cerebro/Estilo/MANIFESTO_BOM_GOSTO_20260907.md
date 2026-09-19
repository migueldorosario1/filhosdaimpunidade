# MANIFESTO BOM GOSTO — O LEMA DO CAFEZINHO (07/09/2026)

**Instituído por ordem do Miguel (07/09/2026 ~02:0x BRT, voz):**

> "A coleta tem que saber onde buscar coisa boa, tem que ter títulos bons, bom gosto — isso que está faltando. Bom gosto. Como é que a gente vai construir isso? Bom gosto para a coleta, para a produção, para o título, para a revisão, para tudo. Bom gosto — esse vai ser então o lema agora do Cafezinho. Bom gosto, tá? O lema do nosso sistema: bom gosto. As coisas bonitas, elegantes. Isso vale para tecnologia e vale para tudo, geopolítica, é tudo."

## O que é bom gosto (concreto, não vago)

Bom gosto NÃO é "texto bonito". É uma régua de decisão em cada camada:

1. **COLETA (onde buscar coisa boa):** fonte boa é fonte que pauta o Brasil ou o mundo com repercussão no Brasil. Volume não é qualidade — feed que só entrega lixo deve ser podado ou rebaixado. Nicho estrangeiro sem gancho brasileiro não é "coisa boa".
2. **CURADORIA (escolher):** entre pautas aprováveis, escolhe-se a MELHOR nota, não a primeira aceitável. A pergunta única: a Metrópoles ou a revista Fórum estamparia isso? ("o padrão está ali" — Miguel, 06/09.)
3. **PRODUÇÃO (texto):** lead entrega o fato mais importante na primeira frase; cada frase carrega um fato próprio (zero frase-trailer); elegância = especificidade (nome real, número certo, consequência concreta); fecho abre horizonte, não resume.
4. **TÍTULO:** específico e simples; nome próprio desconhecido não abre título; sigla não explicada não entra; clickbait e spoiler vazio são falta de bom gosto, não "estratégia"; máx. 80 caracteres (EMU-9).
5. **REVISÃO:** cortar o supérfluo é ato de bom gosto. Na dúvida entre duas palavras, vence a precisa. Na dúvida entre dois títulos, vence o simples e concreto.
6. **TUDO, inclusive tecnologia e geopolítica:** o lema é o mesmo em todas as verticais — muda o vocabulário, não a régua. Tema estrangeiro só entra com gancho para o Brasil (consequência aqui, comparação, ângulo brasileiro).

## Como o lema está EMBUTIDO no sistema (07/09/2026, madrugada)

| Camada | Mecanismo | Onde vive |
|---|---|---|
| Curadoria (pauta) | Juiz 1 com 7 notas ponderadas + régua Metrópoles/Fórum + **rank-and-best: julga o lote (teto 8) e tenta da melhor nota para baixo** | NYC `v4_labs/codigo/v41_ciclo.py`; critérios em `dados/PADRAO_CURADORIA_QUALIDADE.md` (com o LEMA anexado — entra no prompt do juiz); pesos/corte/teto em `dados/juiz_qualidade.json` (config viva) |
| Produção (texto) | Seção **10. Bom gosto — o lema da casa** no manual do redator (lido pelo briefing a cada ciclo) | `Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md` (canônico) = espelho NYC `dados/MANUAL_DE_ESCRITA_PORTAL.md` (md5 registrados) |
| Texto final | Juiz 2 (mesmas 7 notas no texto pronto; metalinguagem = nota zero = rascunho apagado) | `v41_ciclo.py` |
| Título/revisão final | R2: bolo (7) CONTAGEM EMU-9/EMU-10 + **(8) BOM GOSTO** (título específico e elegante, sem clickbait/frase-trailer/sigla; na dúvida, o simples vence) + gate 4) QUALIDADE DA PAUTA | tencent `/home/ubuntu/dsn_revisor2/dsn_revisor2.py` |
| Revisão de fatos | R1 segue focado em fatos (missão própria) — gosto não se confunde com veracidade | tencent `dsn_revisor1` |

## O que FALTA para o bom gosto na COLETA (aguarda "vai" do Miguel)

- **Guarda de roteamento / aposentadoria dos coletores legados** (BUG-20260907): hoje o juiz barra o lixo na SAÍDA, mas os bancos seguem sujando na ENTRADA (tênis→economia etc.). Cura = keywords de roteamento no intake legado OU desligar `coletor.py eco/amb/...` (os bancos já recebem dos coletores V4.1).
- **Tier de fontes (bom gosto na origem):** classificar feeds A/B/C (A = pauta Brasil com qualidade — prioridade máxima; C = só preenchem volume) e usar o tier na ordem de seleção. Proposta desenhada, não implementada — mexe na coleta, precisa do "vai".

## Governança

Este manifesto é o canônico do lema. Mudanças de critério passam por aqui + `PADRAO_CURADORIA_QUALIDADE.md` (injeção no juiz) + registro em `CEREBRO_NODE_ATUALIZACOES.md`. Fórum-irmão da missão: `Foruns/forum_qualidade_curadoria_juiz_v41_20260907.md`; memória técnica: `Memorias/memoria_qualidade_curadoria_juiz_v41_20260907.md`.

**Assinado: Qwen3.8-Max (ZCode Dell, ZM) — 07/09/2026**

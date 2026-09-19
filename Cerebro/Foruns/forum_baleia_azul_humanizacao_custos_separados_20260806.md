# Fórum — Baleia Azul: humanização + custos em boletim separado (06/08/2026 ~19h)

**Data:** 2026-08-06 ~19:00–19:25 BRT · **Executante:** ZCode (Kimi K3), chat direto · **Ordem:** Miguel (mensagem de voz transcrita)

## Ordens do Miguel (transcritas)

1. "O Baleia Azul não precisa botar o gasto — esse custo entra num boletim separado, um boletim de custos que vai só para mim; não precisa mandar para o Gabriel."
2. "O auditor de títulos também não precisa entrar não."
3. "O sinal de recuperação no Google está meio técnico. Dá mais detalhes, seja mais claro quanto à data que você está se referindo — 'melhorou de 1,83 (02/08) para 1,67' mas não dá a data; 'comparativo 30/07 LCP 1,6%' mas não dá a data. Tem que dar data."
4. "Faz um texto mais humanizado para audiência comparativo; fala também qual é a editoria que está dando mais audiência."
5. "Na recuperação do Google: menos técnico, mais humanizado."
6. "Aqui no Baleia tem pendings de 31/07... ou tem que eliminar isso ou tem que dar uma resposta. 8 pendings de bug. E não sou eu que tenho que ler."
7. "No final tem links canônicos — não tinha esses links canônicos. Humanizar mais o Baleia Azul."
8. "Bota aí o Claude pra pedir pro Kimi ler, pra botar na Ponte Claude e Kimi, pra ler o boletim, ver se tem pendência, se concorda com o boletim, se tem que acrescentar alguma coisa."
9. "Fazer um boletim meio humanizado, linguagem mais humanizada. Bota quais foram as manchetes — mais claro, sem linguagem técnica — quais foram as manchetes escolhidas."
10. "Bota audiência no dia anterior; não só 7 dias — bota média móvel 7 dias e audiência dia a dia até o dia anterior; aí você vê se está aumentando dia a dia — vai ser importante isso também."

## Decisões e aplicação

### E-mail Baleia Azul (alçada Kimi — aplicado e validado 06/08 ~19:15)

- **Saíram do corpo:** 💰 Custos & LLMs e 📝 Auditor de Títulos.
- **Ficaram:** 📊 Audiência (humanizada: dia anterior com data, média móvel 7d com as duas semanas datadas, 14d datado, dia a dia da semana, manchete mais lida de ontem com título completo, **editoria campeã** — "Geopolítica, 52% do interesse" — e manchetes novas completas), 🏥 Saúde (texto corrido, sem tabela), 📈 Google (todas as comparações com as DUAS datas: "de 1,83 em 02/08/2026 para 1,67 em 06/08/2026"; "Comparando 30/07/2026 com 06/08/2026"; siglas traduzidas para frases).
- **Abertura/rodapé de carta:** "Boa tarde! Aqui está o Baleia Azul de hoje…" / "Um abraço, Baleia Azul 🐋".
- **Destinatários:** Miguel + Gabriel Barbosa (2 endereços) — ver `forum_baleia_azul_destinatarios_gabriel_20260806.md`.
- **Backups:** `.bak_pre_humanizacao_20260806` nos 3 arquivos tocados (emissor + 2 coletores) + `.bak_pre_humanizacao_20260806` no coletor de saúde.
- **Brinde:** corpo caiu de ~4.470 para ~3.600 caracteres → **bug do Telegram 400 MORTO** (prova: envio real ao Telegram do Miguel, HTTP 200, 06/08 ~19:15).

### Boletim de custos separado (novo)

- `scratch/enviar_boletim_custos.sh` — conteúdo: Custos & LLMs (mesmo bloco de antes) + Auditor de Títulos. Destinatário **único**: Miguel. Cron: 8h02 e 18h02 (`# BOLETIM_CUSTOS_SO_MIGUEL_20260806`). Dry-run validado.

### Boletim markdown do painel /v6/baleia (alçada do Claude, editor)

- Regras canonizadas em `CEREBRO_NODE_BALEIA_AZUL.md` → seção **"Regras editoriais NOVAS (ordem Miguel, 06/08/2026 ~19h)"**: sem custos, linguagem de carta, datas nas duas pontas, audiência com editoria campeã e manchetes completas, pendência só com resposta/dono+próximo passo (senão sai), sem seção "Links canônicos", ritual Kimi-lê-boletim.
- Mensagem com as diretrizes enviada à Ponte (`inbox_trindade/claude.md`, 06/08 ~19:20) + resumo no canal_trindade.

### Ritual Ponte Claude↔Kimi (novo, ordem 8)

Publicada a edição, o editor (Claude) pinga a Ponte; o Kimi lê o boletim e responde no canal: concorda? tem pendência sem resposta? falta algo? Lacuna apontada entra na edição seguinte.

**1º parecer já dado (boletim 06/08 06:00):**
- "8 pending do bug §86 (31/07)" → **RESOLVIDO em 06/08 ~04:20** pela sessão-vigília Kimi (8/8 publish + 3 decisões fechadas; consta no MONITORAMENTO). A resposta chegou depois do fechamento da edição — por isso parecia "sem atualização". Eliminar amanhã.
- "Backup C05 ~52%" → não é pendência para o Miguel; é status operacional dos agentes (segue rodando). Sugerido virar 1 linha de status fora de "Pendências".
- Seção "Links canônicos" → eliminar.
- Restante do boletim: concordo (39 publish, V5 noturno, regra "gafes Lula = ignorar").

## ADENDO ~19:40 — Estrutura nova: Claude editor, Kimi subeditor + colunista

**Ordem do Miguel (~19:30):** "Você fica sendo subeditor, você tem que ter aprovação. O Claude manda para você, você aprova o boletim, acrescenta alguma coisa. Você pode ser o colunista do boletim — faz uma coluna com 100 palavras todo dia, com alguma observação, bem humanizada."

**Estrutura canônica do Baleia a partir de 06/08 ~19:30:**

| Papel | Quem | Desde |
|---|---|---|
| Editor-chefe | Claude Code | 19/07/2026 |
| **Subeditor (aprovação)** | **Kimi K3** | 06/08/2026 |
| **Colunista diário (~100 palavras)** | **Kimi K3** | 06/08/2026 |

**Fluxo:** Claude fecha ~06:00 → pinga a Ponte → vigília Kimi (*/30) lê, aprova/corrige/acrescenta e devolve parecer + coluna do dia → Claude aplica e publica. **Anti-trava:** sem parecer até ~07:30, publica marcado "sem revisão do subeditor".

**Implementado já:**
- Emissor do Baleia ganha bloco ✍️ COLUNA DO KIMI (lê `dados_baleia_azul/coluna_kimi_YYYYMMDD.md`; sem arquivo, sai sem coluna — nunca trava).
- 1ª coluna escrita (amostra, em `coluna_kimi_20260806.md` — "…time que joga com um atacante só fica previsível. Nacional tem leitor esperando…").
- Telegram ganha trunca segura (3.900 chars + aviso + link) — testado 4.283 → 3.963; bug 400 definitivamente morto, independente do tamanho.
- Automação da vigília */30 atualizada (CronUpdate) com a seção 3b SUBEDITORIA BALEIA AZUL.
- Canonizado no NODE_BALEIA_AZUL (cabeçalho "Subeditor e colunista…") e comunicado ao Claude na Ponte (inbox, ~19:40).

## Fontes

- Emissor Baleia: `scratch/enviar_baleia_azul_v2.sh` · Boletim custos: `scratch/enviar_boletim_custos.sh`
- Coletores: `coletar_audiencia_baleia.py`, `coletar_saude_baleia_azul.py`, `coletar_sinal_google_baleia.py`, `coletar_auditor_titulos_baleia.py` (este agora só no boletim de custos)
- Nodo: `CEREBRO_NODE_BALEIA_AZUL.md` · Memória técnica: `Memorias/memoria_baleia_azul_humanizacao_custos_separados_20260806.md`

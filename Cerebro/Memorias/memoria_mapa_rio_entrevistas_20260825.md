# Memória: Mapa Rio — pesquisa de entrevistas eleições 2026 (log técnico)

**Data:** 2026-08-25 09:15→09:27 BRT · **Autor:** ZCode (GLM-5.3)
**Fórum pareado:** `Foruns/forum_mapa_rio_entrevistas_20260825.md` (conteúdo editorial completo + links lá)

## Método

1. Ritual de abertura: `credito_vigilia.py --status` (Kimi 🔴, Qwen 🔴 — sessão já no fallback GLM-5.3) + leitura do quadro "Em andamento AGORA" do `MONITORAMENTO_DE_TRABALHO.md` (nenhuma sessão no Mapa Rio — livre) + varredura de fóruns/memórias/nodos por "mapa rio" (achados: `forum_banco_eleitoral_cerebro_20260727.md`, `mapa_regional_historico_20260730.md`; sem fórum próprio do Mapa Rio até hoje).
2. WebFetch da home https://mapario.com.br — inventário do que já existe: 43 posts na home, cobertura eleitoral ago/26 com última entrevista 20/08 (Castro), série "pré-candidatos" estaduais (Pedro Duarte 18/08, Alexandre Freitas 16/08, Flávio Valle 15/08), arquivo de entrevistas 1994→2026.
3. 9 WebSearch + 3 WebFetch (G1 agenda, JOTA senado — não carregou, Gazeta do Povo senado, Wikipédia eleição indireta). Dois timeouts de WebSearch (rede lenta) contornados com re-query curta.

## Descobertas carregadas (provadas por 2+ fontes)

- Castro renunciou 23/03/2026 (véspera de julgamento TSE); vice vago desde mai/2025 (Pampolha→TCE); desembargador Ricardo Couto interino desde 24/03; eleição indireta suspensa (Zanin 27/03) e em 19/08 o STF tirou de pauta sem data ⇒ RJ sem governador eleito até 04/10. Mandato-tampão nunca existiu; Ceciliano era o único pré-candidato a ele.
- Castro: 3 buscas PF em 3 meses (última 14/08, Sem Refino/Refit); tentou voltar ao Senado; TSE praticamente fechado (Veja).
- Governo: 9 oficiais (Paes PSD, Garotinho Republicanos, Ruas PL, Marinho, Siri PSOL, Busnello Missão, Pantoja UP, Garcia PSTU, Monteiro PCO). Siri (não Motta!) é o PSOL desde 29/07; Motta disputa reeleição federal 5000.
- Senado: 16 oficiais (lista com números no fórum §3); Datafolha 21/08: Benedita 15%, depois Jordy/Portinho 8%, Crivella/Pedro Paulo/Mônica 6%. Portinho assumiu o espaço de Castro no PL.
- Séries de entrevista VIVAS em ago/26: Record/Balanço Geral RJ 11h30 · Jovem Pan · CNN Eleições · RJ1/InterTV · Diário do Rio (3 federais: Reimont, Salvino, Bandeira de Mello) · Barão nas Eleições (Benedita 12/08) · PodCobrar/Sidney Rezende (Paes) · VEJA+ (Ruas) · Ponto de Vista (Marinho 17 e 20/08).
- Armadilha identificada: série Globo 24–29/08 (Sadi+Natuza) = PRESIDENCIÁVEIS, não governo RJ (o estúdio é no RJ, o que gera confusão em agregadores).

## Estado da missão

- Pronto: cenário + pauta (fórum). 
- Falta: produzir posts; gaveta de pauta viva (Record/JP diários); revisar posts antigos "pré-candidato" e o de Castro 20/08 (sem âncora de interinidade); confirmar partido de André Marinho (Novo no G1 vs Republicanos na VEJA) e a não-candidatura de Ganime; presidência atual da Alerj (eleição de Ruas anulada — Bacellar?).
- Aguarda Miguel: OK para produzir + ritmo.

## Registros

- Fórum novo + este arquivo (Tema Duplo).
- Catalogado em `CEREBRO_NODE_AGENTES.md` (perto das entradas mapario existentes) + linha em `CEREBRO_NODE_ATUALIZACOES.md` + linha no `MONITORAMENTO_DE_TRABALHO.md`.

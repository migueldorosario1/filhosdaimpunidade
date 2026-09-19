# 👔 Diretrizes CEO vira a casa do Manual de Estilo + diagnóstico GA4 da /v6/audiencia — 11/09/2026

> Fórum do sprint ZCode/Kimi K3 de 11/09 ~12:5x→13:1x. Dois pedidos do Miguel na mesma sessão:
> (1) reformar TOTAL a página /v6/diretrizes-ceo do painel CCTV para receber o Manual de Estilo;
> (2) verificar se o gráfico GA4 da /v6/audiencia estava quebrado ("parado no dia 10").
> Memória técnica irmã: `Memorias/memoria_diretrizes_ceo_casa_manual_estilo_20260911.md`.

## 1. /v6/audiencia — o gráfico NÃO está quebrado; é atraso do Google

**Sintoma visto pelo Miguel:** gráfico da /v6/audiencia "parado no dia 10".

**Diagnóstico (provas ao vivo, 11/09 ~15h):**
- A página renderiza fresca ("página gerada 11/09 12:57") e a API do GA4 responde normal — o que falta é dado processado: relatórios padrão mostram 09/09=11.748 views (completo), **10/09=3.668 (parcial, com cauda em decaimento a partir das 11h BRT)** e **11/09=1**.
- **O tráfego real está saudável e o problema NÃO é o site nem a tag:**
  - contador próprio (audiencia_red/FAROL): 10/09 inteiro normal (~96,6 mil navegações) e 11/09 normal (66,5 mil até as 13h; pico 12.817/h às 09h);
  - GA4 tempo real: **68 activeUsers agora** (compatível com a fatia ~12-13% que o GA4 sempre mediu vs. o contador próprio);
  - tag `G-4E5DKNTYET` presente e sadia (script async normal, sem Rocket-delay) na home e em post de hoje — HTTP 200;
  - teste sem o filtro `platform=web` e por plataforma: mesmos números (tudo "web") — filtro inocentado.
- **Conclusão:** stall de processamento dos relatórios padrão do GA4 no lado do Google, iniciado em 10/09 ~11h BRT. Padrão documentado do GA4 (dado intraday pode atrasar 24-48h; o tempo real não é afetado). A cauda em decaimento no dia 10 é a assinatura do processamento paralisado no meio do dia.
- **O que esperar:** backfill automático em 24-72h. Se 10/09 continuar crescendo nas próximas consultas, está curado. **Nada a consertar do nosso lado** — não há deploy, credencial, tag ou tráfego quebrado.
- **Lição operacional:** a /v6/audiencia confia 100% no GA4; quando o Google atrasa, a página parece "morta". Melhoria futura (AGUARDA "vai"): faixa de honestidade cruzando GA4 × contador próprio — se GA4 cai >60% vs. FAROL, exibir "GA4 em atraso de processamento (Google); contador próprio saudável".

## 2. /v6/diretrizes-ceo — reformada TOTAL: agora é a casa do Manual de Estilo

**O que entrou no ar (provas curl no fim da memória):**
1. **⚡ Síntese operacional** do Manual Unificado sempre visível no topo (recorte automático da seção);
2. **📖 "Ler o manual inteiro"** — `/v6/diretrizes-ceo/manual/unificado` renderiza os 34 KB do unificado em HTML (conversor md→HTML próprio, sem dependências);
3. **📚 Manuais específicos** — cards com link de leitura para 7 manuais: unificado, escrita (oficial), escrita-portal, régua de título (EMU-1+2+6), Manifesto Bom Gosto, publicador, comunicação interna. Cada card mostra arquivo, tamanho e data de atualização;
4. **✍️ Interação** — formulário "propor item na diretriz" (➕ incluir / ➖ remover / ✏️ alterar + manual de destino + texto + autor). As propostas caem numa **fila pública** na própria página, com botão 🗑️ (soft delete — nada se apaga, regra da casa). Fila gravada em `tencent:~/cafezinho/v6/ceo/ceo_data/estilo_propostas.jsonl` (fora de qualquer caminho de sync — não morre por clobber);
5. **Matriz antiga de prompts V4 preservada** em `/v6/diretrizes-ceo-v4` (nada se perde).

**Arquitetura (padrão da casa):** módulo novo `tencent:~/cafezinho/v6/painel_cctv_v6_diretrizes_estilo.py` + 4 edições ancoradas no `painel_cctv_v6.py` (rota nova, sub-rota `/manual/<slug>`, 2 POSTs, cartão da home) + backups `.bak_pre_diretrizes_estilo_20260911` e `.bak_fix_api_estilo_20260911`. Os manuais são lidos do checkout do Cérebro no próprio Tencent (`~/cerebro-miguel/cerebro/Estilo/`) — o sync existente mantém a página sempre fresca, sem pipeline novo. Armadilha resolvida: o nginx da porta 80 só faz proxy de `/v6/` → 8084, então o JS chama `/v6/api/...` (o strip entrega `/api/...` ao painel; do_POST aceita os dois).

**Provas:** hub 200 com 5 marcadores; 7 manuais 200; fumaça completa da fila (propor → aparece → remover → some, com `EST-20260911-001` preservado como "removida" no jsonl); validação de tipo inválido rejeitada; matriz antiga 200; /v6/audiencia 200 intacta; home do painel com o cartão novo.

## Estado — o que aconteceu / o que falta / o que preciso de você (Miguel)

- ✅ Feito: diagnóstico GA4 completo (resposta: atraso do Google, não pane); página /v6/diretrizes-ceo reformada e no ar com as 4 funções pedidas; testes de ponta a ponta; backups e rollback documentados na memória.
- ⏳ Falta (nada bloqueante): (a) conferir amanhã se o GA4 backfillou 10/09-11/09 (basta abrir /v6/audiencia — se o dia 10 voltou aos ~11 mil, curado); (b) melhoria opcional da faixa GA4×FAROL (aguarda "vai"); (c) sync das propostas de estilo do Tencent de volta ao Cérebro (hoje a curadoria é manual; aguarda "vai" p/ automatizar).
- 🙏 Miguel: nada urgente. Se quiser, já pode abrir http://43.156.151.165/v6/diretrizes-ceo e testar a fila de propostas.

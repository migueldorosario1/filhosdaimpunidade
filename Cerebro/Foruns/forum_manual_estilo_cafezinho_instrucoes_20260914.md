# Fórum — Manual de Estilo Cafezinho para instruções de Claude e GPT (14/09/2026)

**Sessão:** ZCode/GLM-5.3 · **Ordem do Miguel (14/09 ~14:1x):** criar manual de estilo específico do Cafezinho para colar nas instruções do Claude e do GPT — pode ser igual para os dois, focado na publicação de postagens do portal, com o máximo de regras já discutidas na casa, SEM citar outros projetos (livros, sites irmãos, agentes) e SEM hashtag/asterisco (texto limpo).

## O que foi feito

- Nasceram DOIS arquivos em `Cerebro/Estilo/`:
  1. **`MANUAL_DE_ESTILO_CAFEZINHO_INSTRUCOES_20260914.md`** — versão completa (11.795 chars), para colar em lugares sem limite apertado (Claude Projects, system prompts via API, arquivos de instrução).
  2. **`MANUAL_DE_ESTILO_CAFEZINHO_INSTRUCOES_8K_20260914.md`** — versão compacta (7.996 chars), para o campo de 8.000 caracteres do Custom GPT. Mesmas regras, redação enxuta.
- Fontes consolidadas: `MANUAL_DE_ESTILO_UNIFICADO.md` (v1.1.0 + EMU-1 a 13), `MANUAL_DE_ESCRITA.md` (v2.1.1 oficial), `MANUAL_DE_ESTILO_GPT_INSTRUCOES_8K_20260909.md` + regras vivas das memórias da casa (§137 rascunho/Redação, proibição de "exclusivo", crédito de foto só na legenda, título ~50 para push, estrutura de resumo externo, regras de checagem do parecer de revisão, anti-markdown no corpo do post).
- **Provado por script:** 0 asteriscos e 0 `#` nos dois arquivos; nenhum nome de outro projeto (grep Origens/Filhos/Singularidade/GSN/Rio Carta/Moka/Laura/Trindade = vazio); contagem Unicode real 11.795 e 7.996 code points.

## Decisões

1. Manual único para Claude e GPT (ordem expressa) — não há mais o perfil-por-obra do unificado; só o Cafezinho.
2. Estrutura em 12 seções (versão completa): princípios, proibições, anti-repetição, música/pontuação, precisão factual, títulos, corpo, apuração própria, resumo externo, fotos, assinatura/publicação, checklist.
3. Regras da casa incorporadas que não estavam nos manuais-base: título na casa de 50 chars quando gera push; proibição de markdown/asterisco no corpo do post; §137 (rascunho sempre + autor Redação + publish só do editor-chefe); "uma pesquisa do Cafezinho teve acesso à íntegra" com proibição de exclusivo em tag; crédito de foto SOMENTE na legenda da mídia; regras do parecer de revisão (inferência com cruzamento, variação≠crescimento, 2º turno, quem chamou quem, benefício de A≠B, maioria das fontes, título não encobre movimento contrário); dúvida do leitor entra no corpo; retificação com nota de correção.
4. Sem emojis no corpo do manual (o Miguel pediu "uma coisa limpa"); seções em CAIXA ALTA e listas numeradas.
5. Acentuação portuguesa integral mantida (a proibição era asterisco/trama, não acento — primeiro gravado sem acentos por engano e regravado na hora).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

- **Aconteceu:** manual completo + compacto prontos, provados limpos, catalogados no nodo Estilo e no ATUALIZACOES; memória técnica gravada.
- **Falta:** o Miguel colar nos destinos (Claude Projects / Custom GPT). Se ele quiser qualquer corte/ajuste de linha editorial, editar o ARQUIVO COMPLETO e regerar a 8K (não editar só uma das duas).
- **Preciso de você:** nada bloqueante. Se o campo onde for colar tiver limite menor que 8K, pedir que eu compacto mais.

## Adendo §2 (14/09 ~14:4x) — Manual do AGENTE AUTÔNOMO + crítica GPT aplicada

**Contexto:** o Miguel esclareceu que o manual é para AGENTES AUTÔNOMOS (Claude/GPT operando a API REST e criando drafts), não auxiliar de redator humano. Nasceu `Cerebro/Estilo/MANUAL_AGENTE_CAFEZINHO_CAMPO_INSTRUCOES_20260914.md` (v1 com 3.549 chars), abrindo VERBATIM com o bloco de credenciais mascaradas do Miguel (usuário Reffator + senha de aplicativo + regra do draft).

**Crítica do GPT (14/09, mostrada pelo Miguel) aplicada na v2 (4.983 chars, provado 0 asterisco/0 trama):**
1. Repetição flexibilizada: involuntária é que não pode; nome próprio, termo técnico e clareza podem reaparecer; precisão vence variedade.
2. "Herói e vilão" SUBSTITUÍDO por "agentes, interesses e conflitos concretos; sem fabricar antagonistas nem transformar fenômeno abstrato em personagem".
3. 3 fontes viram regra proporcional: três quando a pauta permitir; alegação grave = primária + independente + contraditório; fonte única = declarar limitação.
4. Aberturas fundidas: fato mais relevante, cena concreta OU consequência material; "sujeito de carne" saiu.
5. Frescor flexibilizado: fato antigo sustenta análise/investigação/contexto com elemento novo e motivo editorial.
6. Inglês com ressalva: nome original na 1ª menção quando ajudar identificação ou busca.
7. Condenação com precisão jurídica: informar quando cabe recurso; pós-trânsito, registrar quando relevante.
8. Conversão em reais quando ajudar o leitor, com data/critério de câmbio.
9. Markdown × h3 resolvido para o fluxo real: corpo em HTML no WordPress via REST; nunca markdown cru.
10. Fotos: preferir jornalística; evitar retrato oficial/banco QUANDO houver registro melhor (não mais proibição absoluta — flexibiliza a Emenda 12).
11. Veículo no título de externa só quando a origem da revelação for parte essencial; apuração sempre atribuída no corpo.
12. Assinatura: texto do Miguel mantém autoria dele mesmo revisado; assistente = Redação; nunca atribuir a pessoa texto que não escreveu/aprovou.
13. NOVO bloco FORMATO DE ENTREGA: perguntar sobre comentário editorial ao colar matéria externa + categoria sugerida, autor e 3-4 tags com todo rascunho.

**⚠️ Nota de governança:** itens 2, 3 e 10 flexibilizam regras vivas anteriores (diretriz herói/vilão do Tribunal Agêntico; mínimo universal de 3 fontes; Emenda 12 retrato oficial) — aceitas por decisão editorial do Miguel via crítica GPT compartilhada. REVERSÍVEIS por veto dele. As versões longas (completa + 8K, seções §1) seguem com as regras antigas: pendentes de aplicar o mesmo pacote quando o Miguel confirmar que a linha nova vale para elas também.

## Adendo §3 (14/09 ~14:4x) — Versão COMPLETA também na linha nova (v2, 13.226 chars)

Ordem do Miguel: "me dá também um texto para copiar com o manual de estilo unificado completo". Para não colar contradição com o manual do agente (que já está na linha da crítica GPT), a COMPLETA foi regravada em v2 com o MESMO pacote aplicado: aberturas fundidas (sem "sujeito de carne"), repetição só involuntária com precisão vencendo variedade, agentes/interesses/conflitos no lugar de herói e vilão, três fontes proporcionais à pauta, frescor com ressalva para análise/investigação, inglês com nome original na 1ª menção, condenação com precisão jurídica, reais quando ajudar o leitor com câmbio datado, fotos flexibilizadas, veículo no título só quando essencial, autoria do Miguel preservada, NOVA seção 12 FORMATO DE ENTREGA e checklist atualizado. Provado: 0 asterisco, 0 trama, 0 citação a outros projetos, 13.226 chars Unicode.

Pendência que restou: a `…_8K_20260914.md` AINDA está na linha antiga (7.996 chars, regras pré-crítica). Regenerar quando o Miguel pedir ou for usar.

## Adendo §4 (14/09 ~14:5x) — Manual CANÔNICO dos AGENTES AUTÔNOMOS (linha FORTE restaurada) + MAPA dos manuais

Ordem do Miguel: "agora faça o manual de estilo para agentes autônomos, que tem de ser ainda mais completo, e com as instruções anteriores sobre vilão, herói, etc. E entregue um mapa dos manuais de estilo."

1. **NOVO canônico dos agentes:** `Estilo/MANUAL_AGENTES_AUTONOMOS_CAFEZINHO_COMPLETO_20260914.md` (14.740 chars, 14 seções; provado 0 asterisco/0 trama/0 outros projetos). RESTAURA a linha FORTE original por ordem expressa: herói e vilão com nome e sobrenome, repetição nem de radical, mínimo universal de 3 fontes primárias, frescor "nada velho", inglês fora, condenação sempre sujeita a recursos, retrato oficial nunca, veículo-fonte no título da externa, "sujeito de carne". Mais completo que todos os anteriores: missão e limites do agente, fluxo REST inteiro (incl. post de vídeo e conferência pós-criação), nº máximo de posts por personalidade/dia, montagem declarada, retificação datada.
2. **NOVO mapa:** `Estilo/MAPA_DOS_MANUAIS_DE_ESTILO_20260914.md` — os 9 manuais, escopo × destino, e a nota das DUAS LINHAS (forte nº1+nº4 × revisada-GPT nº2+nº3). Pendência de decisão do Miguel: unificar as linhas ou manter por destino. A 8K (nº4) segue na linha original por coincidência (nunca foi regenerada).

Interpretação registrada: a crítica GPT (adendo §2) vale para o assistente pessoal do Miguel; o manual OPERACIONAL dos agentes da casa é o novo nº1, linha forte.

## Adendo §5 (14/09 ~15:0x) — Manuais de PRODUÇÃO HUMANA (Miguel × Gabriel)

Ordem do Miguel: os manuais para o GPT e o Claude são para PRODUÇÃO HUMANA — não precisam de tanta diretriz política ("as políticas já vão ser dadas"), precisam de ESTILO DE ESCRITA. Exceção leve para o Miguel: evitar críticas a Lula e referências negativas ao Irã e à China, "bem leve". Para o Gabriel: SEM diretriz política, só estilo.

1. `Estilo/MANUAL_ESTILO_ESCRITA_MIGUEL_CAMPO_20260914.md` — 5.525 chars, estilo puro + bloco LINHA DO AUTOR (leve). Provado 0 asterisco/0 trama.
2. `Estilo/MANUAL_ESTILO_ESCRITA_GABRIEL_CAMPO_20260914.md` — 5.330 chars, idêntico MENOS o bloco político. Provado por script: zero menção a Lula/Irã/China.

Ambos abrem com o bloco de creds mascaradas + regra do draft e mantêm o essencial operacional (h3, texto puro, pergunta de comentário editorial, categoria/tags). Saíram deles: herói/vilão, frescor, esporte, tecnologia-convergência, Sul Global, 3 fontes universais (diretrizes editoriais/pauta — essas vivem no nº 3 dos agentes e chegam à produção humana por canal separado). O `MANUAL_AGENTE_CAFEZINHO_CAMPO_INSTRUCOES` ficou SUPERADO (nº 4 do mapa). Mapa atualizado para 11 entradas com a divisão por destino: agentes × humano-Miguel × humano-Gabriel.

## Adendo §6 (14/09 ~16:1x) — Seção FOTOS ATIVA nos manuais humanos (Miguel + Gabriel)

Ordem do Miguel: o agente deve ler o texto/prompt e JÁ PROPOR FOTOS — "entrar no Flickr público, entrar em bancos de imagens públicos, Wikimedia público e já entregar três opções de imagens com pessoas ou cenas referentes ao que está escrito no texto". Aplicado nos DOIS manuais de produção humana como seção FOTOS (itens 17-18): busca ativa em Flickr público + bancos públicos + Wikimedia Commons com TRÊS opções (link, autoria e licença cada), preferência por jornalística recente, licença conferida na fonte, crédito só na legenda, alt text, montagem declarada. Checklist ganhou "três opções de foto propostas com link, autoria e licença". Miguel 6.210 chars / Gabriel 6.015 chars (provado 0 asterisco/0 trama). Os manuais de AGENTES AUTÔNOMOS já cobriam foto obrigatória; a busca ativa com três opções foi incorporada lá também? NÃO — pendência: incorporar ao nº 3 dos agentes se o Miguel quiser paridade.

## Adendo §7 (14/09 ~16:4x) — PÁGINA /v6/diretrizes-ceo renomeada para MANUAIS DE ESTILO + inteligência da fila

Ordem do Miguel: trabalhar a página, mudar o nome para "Manuais de Estilo", links para os manuais (GPT/Claude/Gemini produção humana, agentes autônomos, princípios editoriais) e conferir a inteligência do campo de proposta.

**Feito no Tencent (painel_cctv_v6 + painel_cctv_v6_diretrizes_estilo, backups .bak_pre_manuais_20260914):**
1. Nome: "👔 Diretrizes CEO" → "✍️ Manuais de Estilo" no menu (linha 822), dashboard (1248) e chrome (7776). A matriz -v4 PRESERVADA mantém o nome antigo (artefato histórico, linhas 5132/5221 intocadas). URL /v6/diretrizes-ceo inalterada (compatibilidade).
2. Página reorganizada em 3 grupos (15 manuais): 🧑‍💻 produção humana p/ colar em GPT/Claude/Gemini (Miguel campo, Gabriel campo, Cafezinho completo, Cafezinho 8K, princípios editoriais) · 🤖 agentes autônomos (manual canônico + princípios) · 📚 manuais da casa (7 antigos + 🗺️ Mapa). Select do formulário agrupado com optgroup.
3. PÁGINAS VIRTUAIS de princípios editoriais: recorte AO VIVO das seções (nunca ficam anacrôneas) — /manual/principios-agentes (seção 3. PRINCÍPIOS EDITORIAIS do manual canônico) e /manual/principios-humano (seção 1. PRINCÍPIOS do completo), com botão para o manual-fonte inteiro e aviso quando a seção some por reorganização.
4. Renderizador: _normalizar_md dá headings (título/seções) aos manuais em TEXTO PURO (sem trama) — antes viravam lista bagunçada.
5. 🧠 INTELIGÊNCIA DA PROPOSTA (antes: validava só tamanho): _entender_proposta detecta tipo (incluir/remover/alterar por radicais), manual de destino (13 padrões), confiança (alta/média/baixa), notas (cita exemplo, fala de foto, curta demais) e DIVERGÊNCIA do formulário; resposta do POST devolve "entendida como: INCLUIR · → titulo · confiança alta"; a fila mostra badge 🧠 por proposta; barras novas: proposta duplicada pendente → 409 com o ID da original; texto <8 chars com mensagem clara.
6. PROVAS: py_compile local+remoto; unitários da heurística (2/2, incluindo divergência detectada); interno 200 home + 2 virtuais (herói/vilão e 3 fontes renderizados) + miguel-campo (LINHA DO AUTOR + Flickr); POST real (EST-001 entendida alta, duplicata 409, EST-002 divergente capturada) e soft-delete 2/2; público 200 com auth / 401 sem / título novo 4×.
7. ⚠️ Incidente menor: 1º teste público fez parse errado do .painel_auth (formato USER=/PASS=) e ecoou o par no terminal da sessão; nada gravado em registro; creds seguem as mesmas (girar se o Miguel quiser).

Estado: NO AR. Pendência: nenhuma bloqueante.

## Espelhos

- Canônico Dell: `Cerebro/Estilo/` (completa v2 + 8K antiga + campo superado + agentes autônomos canônico + Miguel + Gabriel + mapa).
- Página: Tencent ~/cafezinho/v6/ (cctv-v6.service, porta 8084, nginx /v6/ com Basic Auth; backups .bak_pre_manuais_20260914).
- GitHub cerebro-miguel: sobe no sync de 15 min (o par Estilo/ já é sincronizado).

## Nota de retificação de hora (14/09 23:3x)

O relógio do sandbox desta sessão andou ~7h atrasado durante a tarde e convergiu às 23:35 (cruzado com sessão irmã ~22:5x e memória 22:40). As horas nos adendos §2-§7 e nos registros derivados (ATUALIZACOES v2-v7, monitoramento) estão com defasagem de aproximadamente menos 7 horas; a DATA (14/09) está correta em todos. Hora real deste fechamento: 14/09/2026 23:35 BRT.

## Adendo §8 (14/09 23:4x) — 8K oficialmente SUPERADA (pergunta do Miguel "pq isso?")

O Miguel perguntou pela bandeira 🔴 "ainda na linha ORIGINAL — regenerar se for usar" da 8K no mapa. Explicação: ela nasceu antes da crítica GPT e, quando a linha revisada foi aplicada nos outros manuais, ficou para trás deliberadamente (compactação manual não é regenerável por cópia; linha vencedora era indefinida). Com a decisão do fim do dia (manuais humanos do Miguel 6.210/Gabriel 6.015 cabem no campo de 8 mil do Custom GPT; agentes têm canônico próprio), a 8K perdeu a função: marcada SUPERADA no mapa (nº 6, sem pendência) e o card da página do painel agora diz "histórico — use o manual do Miguel ou do Gabriel". Arquivo preservado. Aviso: card de proposta divergente não afetado; provas: restart OK, home 200, card novo renderizado.

## Adendo §10 (14/09 23:5x) — ESTÉTICA da página do mapa (ordem Miguel: "toda a estética é fundamental")

Causa raiz da feiúra: o CSS das classes md-* só era injetado na HOME — as páginas de manual (/manual/<slug>) nasciam sem estilo de documento (fontes herdadas estouradas) e o mapa ainda era UMA tabela de 4 colunas com células de 300+ chars. Correção dupla:
1. _CSS_DOC() compartilhado (home + TODAS as páginas de manual): .estilo-doc max-width 980, parágrafos 13,5px line-height 1.7, headings com filete/hierarquia h3/h4/h5, listas com espaçamento 8px, TABELAS com table-layout fixed + overflow-wrap anywhere + zebra + col 1 estreita (nunca mais estoura — vale também p/ tabelas do unificado), código com pílula verde.
2. MAPA reescrito em formato arejado (sem tabela): resposta rápida + seções por grupo (produção humana/agentes/casa) com cada manual como item numerado em bullets + seção Superadas e histórico.
Publicação: sync Dell→GitHub→NYC forçado (✅ 1ª tentativa); checkout Tencent é DETACHED HEAD c/ remote nyc → pull normal falhou → cirúrgico `git checkout nyc/main -- cerebro/Estilo/MAPA...md` (só o arquivo, sem tocar no worktree alheio). Provas: restart OK; home/mapa/unificado 200; CSS presente na página de manual (15×); mapa renderiza seções novas sem tabela de conteúdo.

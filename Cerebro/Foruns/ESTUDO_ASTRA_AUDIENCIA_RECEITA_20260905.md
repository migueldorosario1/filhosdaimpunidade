# Astra — audiência e receita do Cafezinho, com Moka gratuito

Data: 05/09/2026. Autor: apoio AST de crescimento, para consolidação pelo Astra e decisão do Miguel.

Estado: estudo e plano de experimentos; nenhuma campanha, cobrança, publicação, integração, alteração de produção ou contratação executada. Monitoramento e minuta lidos. Nenhum cofre acessado. A única escrita deste apoio é este documento novo.

## O que eu faria primeiro

Trabalharia em três resultados: fazer o leitor consumir uma segunda matéria útil; tornar o apoio voluntário existente mais compreensível; vender um pequeno patrocínio contextual, com entrega e custo conhecidos. O Moka pode ajudar nessa relação, mas continua gratuito: não deve virar uma cobrança obrigatória escondida no caminho do leitor.

Não começaria por outro contador, robô, loja ou disparador. A casa já tem medidores, Top 10, blocos de recirculação, página de apoio, material Moka e responsáveis. O que falta demonstrar é quanto cada caminho entrega de leitores recorrentes, apoiadores e margem. As propostas abaixo são hipóteses comerciais, não promessa de faturamento.

## 1. O que os dados próprios permitem afirmar

### Retrato recente: estabilidade com leve alta, não explosão

A coordenação AST coletou **somente caches existentes da Tencent em 05/09 às 08:30:18 BRT**, sem consultar API, atualizar cache ou importar o painel. Conferi o JSON da coleta e refiz as somas: na mesma régua GA4 `screenPageViews`, filtro web, **29/08–04/09 = 77.666 views**, contra **22–28/08 = 76.636**, variação **+1,34%**. Média recente: **11.095 views/dia**. São sete dias completos em cada janela, não pessoas únicas ou impressões de anúncios.

O cache de 14 dias foi atualizado às **08:28:53 BRT** e concorda com o cache de 92 dias nos dias comparados. O de 185 dias era mais antigo e ainda trazia 04/09 parcial com 5.866; esse ponto foi excluído do comparativo. A escolha do arquivo pela data de atualização, e não só pelo nome, muda a leitura do negócio.

**A baixa antiga do reporting está superada nesses caches:** 31/08 aparece agora com 11.419 views e 02/09 com 11.783, no lugar dos números muito baixos registrados anteriormente. Isso não demonstra, por si só, aumento de receita ou de recorrência. Para receita e conversão por página ainda faltam os campos descritos adiante.

**FAROL exige esclarecer a definição antes de vender audiência:** na leitura de 04/09 às 23:55:02, o JSON traz `hoje_humanos_distintos=12.613`, maior que `hoje_visitantes_distintos=11.486`; no mesmo registro, `online_30min_humanos=590` e bots=352, contra total=521. Pode haver diferenças de cobertura/definição/frescor entre campos; esta pesquisa não fechou a causa. Não chamar o campo “humanos” de audiência auditada nem somá-lo ao GA4/LUMINA. As 55.437 navegações desse registro são a última leitura às 23:55, não um total de pessoas.

Fonte e método: [evidência canônica da coleta recente](../Memorias/EVIDENCIA_ASTRA_AUDIENCIA_CACHE_20260905.json), produzida em 05/09/2026. Pedido ao dono do FAROL: explicar origem, janela, deduplicação e momento de atualização de cada campo; não corrigir o serviço por conta própria.

### Base histórica com janela definida e arquivos conferidos

A análise de 14/08 define **15/07–13/08/2026 contra 15/06–14/07/2026**, dois períodos de 30 dias, e usa GA4 com `platform=web`, além de Search Console web/Discover separados. Nesta pesquisa conferi os totais nos JSONs originais, sem refazer chamadas às APIs. Isso prova o que foi exportado, não a cobertura completa de humanos nem a audiência atual de setembro.

| Régua | 15/06–14/07 | 15/07–13/08 | Leitura permitida |
|---|---:|---:|---|
| GA4 `totalUsers`, bruto | 91.605 | 150.764 | Usuários identificados pelo GA4; inclui tráfego suspeito documentado |
| GA4 sessões | 129.387 | 187.680 | Sessões da mesma propriedade e filtro |
| GA4 `screenPageViews` | 152.789 | 229.594 | +50,3% no registro; não equivale a humanos ou impressões de anúncio |
| GA4 taxa de engajamento | 30,54% | 36,22% | +5,68 pontos percentuais; mesma definição do export |
| GSC busca web: cliques | 54.518 | 69.549 | +27,6%; cliques de busca, não visitantes únicos |
| GSC busca web: impressões | 1.668.589 | 2.195.009 | +31,6%; oportunidade de busca observada |
| GSC busca web: CTR | 3,267% | 3,169% | Crescer impressões não garantiu melhorar CTR |
| GSC Discover: cliques | 4.055 | 34.677 | Recuperação forte, mas concentrada e volátil |

Fontes: [relatório e definição dos períodos](</home/migueldorosario/Downloads/Antigravity Google/Outros/google search/google search/analise_cafezinho_20260814/RELATORIO_ANALISE_GOOGLE_CAFEZINHO_20260814.md:3>), [GA4 original](</home/migueldorosario/Downloads/Antigravity Google/Outros/google search/google search/analise_cafezinho_20260814/ga4_raw.json>) e [GSC original](</home/migueldorosario/Downloads/Antigravity Google/Outros/google search/google search/analise_cafezinho_20260814/gsc_raw.json>). Consulta local: 05/09/2026.

Na semana **07–13/08 contra 31/07–06/08**, o GA4 teve 59.717 contra 53.294 views, mas os cliques de busca caíram de 17.029 para 15.570 e os de Discover de 8.568 para 5.868. Portanto, um único “crescemos” apaga movimentos diferentes. O relatório também advertia sobre possível incompletude dos dias finais do GSC à época da extração. [Comparativo semanal](</home/migueldorosario/Downloads/Antigravity Google/Outros/google search/google search/analise_cafezinho_20260814/RELATORIO_ANALISE_GOOGLE_CAFEZINHO_20260814.md:56>).

### Quatro cuidados que mudam a decisão

1. **Não chamar estimativa de humanos auditados.** Os “122,5 mil sem bots” do relatório são uma aproximação derivada do tráfego geográfico suspeito, não uma identificação individual de humanos. O adendo forense descreve navegador/resolução/comportamento anômalos e registra a decisão de Miguel de não aplicar filtro. Aqui preservo o bruto e a ressalva; não proponho excluir países. [Diagnóstico e ordem](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_cafezinho_analise_ga4_gsc_20260814.md:39>).
2. **“Título rende 9×” não é resultado causal.** A análise cruzou 42 posts de melhor desempenho, usando score que mistura views GA4, cliques GSC multiplicados por três e Discover. Há seleção dos vencedores e concentração em poucos virais. Economia e geopolítica são boas candidatas a teste, mas não existe garantia de multiplicar audiência trocando verbos. [Método e amostra](</home/migueldorosario/Downloads/Antigravity Google/Outros/google search/google search/analise_cafezinho_20260814/RELATORIO_ANALISE_GOOGLE_CAFEZINHO_20260814.md:94>).
3. **A audiência de 31/08 tem réguas diferentes.** O relatório publicitário registra 50.201 navegações e 14.946 “visitantes distintos (soma/hora)”. A segunda quantidade não deve ser anunciada como 14.946 pessoas únicas no dia. O relatório também errou o dia da semana; o fórum posterior corrigiu para segunda-feira. Os gráficos de mesmo dia da semana já foram entregues. [Régua original](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Relatorios/publicidade/2026-09-01.md:13>) e [correção/entrega dos gráficos](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_queda_producao_audiencia_31aug_20260901.md:114>).
4. **Não confundir atraso do GA4 com queda comercial.** Em 03/09, a casa registrou o report de 02/09 com 335 views/93 usuários enquanto realtime e FAROL continuavam ativos. A evidência de cache recebida e conferida nesta rodada supera esse baixo número: 02/09 agora tem 11.783 views. Não manter “aguardando backfill” como diagnóstico atual com base apenas no fórum antigo. [Registro histórico de 03/09](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_incidente_ga4_backlog_tendencias_20260903.md:17>) e [leitura atual de 05/09](../Memorias/EVIDENCIA_ASTRA_AUDIENCIA_CACHE_20260905.json).

As “500 mil pessoas por mês” citadas publicamente pelo Cafezinho são uma **autodeclaração de 10/06/2023**, não a audiência de 2026 nem número comparável automaticamente ao GA4 atual. [Anúncio histórico do próprio Cafezinho](https://www.ocafezinho.com/2023/06/10/novos-tempos-novo-cafezinho/), consultado em 05/09/2026.

## 2. O que já existe e deve ser reaproveitado

- **Medição:** FAROL, GA4 e LUMINA; gráficos por dia da semana e, desde 03/09, janela de 40 horas/MM8h. Usar cada fonte para a pergunta que ela mede; não somar seus totais nem criar outro painel. [Gráficos existentes](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_farol_grafico_40h_topo_20260903.md:43>).
- **Recirculação/distribuição:** Top 10, histórico e geradores sociais documentados. A versão mais recente do plano consultado estaciona o card Instagram e prioriza o formato Top 10/Top 1 no X, ainda com aprovação do Miguel. Não ressuscitar a primeira versão de três redes como ordem vigente. [Adendos finais do plano social](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_plano_social_top1_conselheiro_audiencia_20260819.md:250>).
- **Apoio:** a página pública do Cafezinho já exibe R$ 12/mês, R$ 120/ano e contribuição de qualquer valor, com PayPal e Pix na leitura atual da página. Não precisamos criar “clube” ou checkout para testar a mensagem; o funcionamento financeiro desses caminhos ainda precisa ser confirmado pelo responsável, sem compra de teste pelo Astra. [Apoie o Cafezinho](https://www.ocafezinho.com/apoie/), consultado em 05/09/2026; oferta exibida, não transação validada. Uma referência a PagSeguro apareceu no resultado de busca, mas não foi confirmada na página atual e não entra no inventário de meios verificados.
- **Moka:** 24 prints, nove banners, 30 pautas, minutas e calendário; uma operação de marketing já foi registrada pelo ZM. O fórum de 03/09 mantém disparos sujeitos ao “vai”. A posição documentada do banner no artigo é depois de “Leia também” e antes da newsletter. [Marketing pronto](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_marketing_moka_20260903.md:9>) e [posição do banner](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md:180>).
- **Publicidade:** DS-N Publicidade e mapa de GAM/redes existentes. Os relatórios examinados ainda não trazem receita, RPM, CTR ou margem conciliados. A alegação de “18 slots vazios” não é receita perdida demonstrada: o próprio histórico mostrou anúncios Denakop injetados por JavaScript nesses espaços. Não ocupar, desativar nem aumentar slots sem inspeção atual e dono. [Lacuna financeira](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Relatorios/publicidade/2026-09-01.md:33>) e [correção do diagnóstico Denakop](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/forum_banners_moka_reader_publicacao_cafezinho_tematicos_20260816.md:152>).

## 3. Quatro comparáveis: o modelo público, não o faturamento

Critério: veículos de jornalismo político/econômico, com site e relação direta com público. Fontes primárias consultadas em **05/09/2026**. Páginas sem data editorial e resultados em cache não garantem checkout ou oferta vigentes neste minuto; nenhuma conta foi criada e nenhum pagamento foi feito.

| Veículo | Formatos e caminhos observados | O que aproveitar como hipótese | Limite da evidência |
|---|---|---|---|
| Brasil 247 | Página de apoio descreve conteúdo aberto, contribuição recorrente/avulsa, membros da TV 247 e encontros; navegação separa TV e cortes; há newsletter | Apoiar a continuidade do jornalismo pode ser proposta de valor sem fechar o conteúdo | É oferta/autodescrição do veículo; não conhecemos membros pagantes, receita, retenção ou alcance deduplicado |
| Jornal GGN | Área de assinante reconhece apoio via YouTube, Catarse, Pix e Google, com benefícios mensais; páginas de newsletter e publicidade | Unificar a experiência do apoiador e ter contato comercial claro, sem multiplicar comunidades desconectadas | Não acessamos conteúdo restrito nem painel financeiro; não deduzimos participação de cada receita |
| DCM | Apoio recorrente e avulso, membros YouTube e contato “Anuncie” com mídia kit | Separar a proposta para leitor da proposta para anunciante | Tabela de apoio não revela taxa de conversão ou receita; mídia kit não foi tratado como auditoria de tráfego |
| Revista Fórum | Loja oficial com livros, canecas, café, camisetas e newsletter comercial; página institucional própria de mobilização com formulário | Produtos e relacionamento podem complementar jornalismo; testar demanda antes de estoque ou operação nova | Página de assinatura retornou 403 e subdomínio de apoio 502; não confirmei benefícios/preços atuais. Loja disponível não prova vendas ou margem |

Fontes Brasil 247: [apoio, acesso aberto, encontros e newsletter](https://www.brasil247.com/apoio/), sem data editorial de atualização visível, consulta 05/09/2026.

Fontes GGN: [área do assinante](https://jornalggn.com.br/assinante-ggn/) e [publicidade](https://jornalggn.com.br/anuncie/), consulta 05/09/2026. Datas variáveis do cabeçalho do site não foram usadas como data de publicação da oferta.

Fontes DCM: [apoio](https://www.diariodocentrodomundo.com.br/apoie/) e [anuncie](https://www.diariodocentrodomundo.com.br/anuncie), sem data editorial visível, consulta 05/09/2026.

Fontes Fórum: [loja oficial](https://www.lojaforum.com.br/), que se identifica como loja da Revista Fórum, e [formulário em domínio institucional](https://mautic.revistaforum.com.br/abaixo-assinado/terrabras), consultados em 05/09/2026. O formulário comprova o formato de mobilização, não autorização para usar seus dados em marketing; não proponho copiar a pauta política ou seus contatos. [Página de assinatura não recuperada](https://revistaforum.com.br/assinatura/).

**Não há ranking de tráfego concorrente neste estudo.** Não obtive analytics auditáveis dos quatro veículos, alcance deduplicado entre site/redes nem demonstrações financeiras. Estimativas de ferramentas de mercado não foram consultadas ou contratadas. Não apresento “visitas mensais”, RPM, conversão ou faturamento inventados. O comparativo é de oferta e organização, não de desempenho.

## 4. A régua mínima antes de testar

Fechar uma tabela de **28 dias completos**, mais os últimos sete dias completos, com BRT e datas de início/fim explícitas. Comparar dias da mesma semana e artigos com a mesma idade de publicação; isolar mudanças de medição e dias incompletos. Não tratar hoje parcial como ontem fechado.

Campos mínimos: URL canônica/ID, editoria, data/hora, dispositivo e AMP/non-AMP quando disponíveis, fonte/mídia, sessões de entrada, views, engajamento, caminho para segunda página e cliques GSC por página/consulta. Usar GA4/GSC existentes; FAROL/LUMINA funcionam como contraste do movimento geral, não substituto automático de conversão por URL.

Dinheiro em tabela separada: receita estimada e finalizada por fornecedor, moeda, período e base; taxas, estornos, receita de apoio, patrocínios e custos incrementais. Só calcular RPM quando numerador e denominador pertencem ao mesmo produto/janela. Não somar repasse consolidado e suas parcelas de GAM/rede como receitas independentes.

Lacunas hoje: série recente completa por conteúdo/origem; explicação estável de cobertura dos medidores; receita conciliada de GAM/AdSense/demais redes; pagamentos ativos do apoio; conversão do apoio por origem; eventos Moka persistidos e versão publicada. Usar exportações/prints que Miguel ou os donos já tenham antes de propor credencial/API nova. Falta de dado deve aparecer como **indisponível**, nunca zero.

## 5. Três experimentos concretos, pequenos e separados

Todos **AGUARDAM VALIDAÇÃO para execução**. Preparação local pode começar com a autorização de estudo; divulgação, teste com escrita, mudanças operacionais e contato comercial dependem de escopo/“vai” próprios. Metas abaixo são critérios propostos de decisão, não previsão nem cálculo de tamanho amostral. O resultado pode ser inconclusivo.

### Experimento 1 — uma boa matéria deve levar à próxima

**Hipótese:** melhorar a seleção de “Leia também” em economia/geopolítica aumenta a segunda leitura sem precisar publicar mais matérias ou comprar tráfego.

**Como:** escolher dez artigos ainda úteis em cinco pares comparáveis por tema, idade e origem de audiência. Sortear um de cada par para receber dois links internos escolhidos por utilidade real, usando o bloco já existente; o outro mantém sua configuração. Janela de 14 dias após autorização. Não mudar títulos, anúncios, frequência social ou layout ao mesmo tempo. Conteúdo desatualizado não entra no teste só porque foi campeão antigo.

**Medir:** sessões que começam no artigo e alcançam outra página editorial ÷ sessões elegíveis de entrada; secundárias: engajamento e retorno em sete dias, se essa coorte puder ser produzida pela medição existente. Guardas: nenhuma queda relevante de tempo engajado, erro de navegação ou interferência em publicidade.

**Decidir:** calcular o efeito por par e o agregado, com volumes e incerteza. Um ganho relativo de pelo menos 15% é o sinal prático proposto para nova rodada, não autorização de expansão automática. Menos de 200 sessões por grupo, poucas segundas leituras, fonte incompleta ou resultado dominado por um viral → inconclusivo. Não chamar diferença exploratória de prova causal generalizável.

**Quem/custo:** Astra seleciona pares e prepara a análise; DSN-Chefe/CM validam relevância editorial; executor autorizado altera somente os dez blocos após aval. Preparação estimada: meio dia; mídia paga e novo serviço: nenhum. Horas e eventual custo de execução devem ser registrados, não escondidos como “grátis”.

### Experimento 2 — testar o convite ao apoio que já existe

**Hipótese:** uma explicação curta do que a contribuição mantém, ligada à página `/apoie/`, converte melhor do que um pedido genérico, sem restringir a leitura.

**Como:** primeiro o dono confirma que os meios de apoio existentes recebem/cancelam corretamente e fornece uma base agregada de 14 dias. Preparar duas versões de chamada, sem criar benefícios ou mudar preços. Em cinco pares de páginas comparáveis, testar a versão atual contra uma chamada contextual durante 14 dias, em posição própria já autorizada e sem deslocar anúncio pago. Mensagem proposta: “Ajude a manter esta cobertura acessível. O apoio é voluntário.” O destino continua sendo o apoio existente.

**Medir:** sessões que chegam ao apoio por origem, novas contribuições efetivamente confirmadas, receita líquida após taxas/estornos e receita de apoio por mil sessões elegíveis. Clique em botão não é pagamento. Para recorrentes, acompanhar cancelamento/continuidade em 30 dias; 14 dias não provam retenção mensal.

**Decidir:** avançar apenas com contribuição líquida positiva, rastreamento suficiente e pelo menos cinco novos apoios confirmados no piloto, sem reclamação relevante de cobrança ou restrição. Esse mínimo é operacional, não prova estatística. Se só houver cliques ou pagamentos não atribuíveis, entregar aprendizado de mensagem e declarar conversão financeira desconhecida. Não abrir checkout novo para contornar a lacuna.

**Quem/custo:** Astra escreve variantes e ficha de medição; Gabriel/Miguel confirmam oferta e meios de apoio; DS-N Publicidade ou responsável financeiro entrega agregados; executor autorizado aplica a chamada. Meio dia de preparo estimado, sem mídia paga. Taxas já praticadas e esforço de suporte entram na margem.

### Experimento 3 — uma cota de patrocínio contextual, sem vender pauta

**Hipótese:** um parceiro compatível aceita financiar uma pequena entrega útil à comunidade, com marca identificada e escopo fechado, sem exigir acesso a dados dos leitores ou controle editorial.

**Como:** preparar uma página comercial usando os relatórios próprios e os prints Moka existentes. Oferecer um piloto de sete dias: apoio identificado em um espaço próprio cuja disponibilidade comercial seja validada, mais uma demonstração já preparada do Moka com material autorizado/domínio público. Não prometer inserção em slots de terceiros, alcance garantido, recomendação editorial comprada ou envio da base de contatos. Não é licença para ocupar o banner Moka automaticamente.

Após “vai” específico, Gabriel/Miguel escolhem até cinco contatos profissionais já conhecidos e autorizam uma abordagem individual, sem lista comprada ou disparo automático. Astra prepara roteiro, proposta e perguntas; não envia mensagens por conta própria. Caso o anunciante prefira serviço, a alternativa é uma oficina B2B de escopo limitado, mantendo o produto gratuito.

**Medir:** respostas qualificadas, reuniões, propostas formais, valor contratado, pagamento recebido, custo de entrega/suporte e margem de contribuição. Regra de preço: custos diretos + horas acordadas + eventual receita publicitária deslocada + margem definida pelo Miguel. Sem esses componentes, preço e retorno permanecem em aberto.

**Decidir:** após cinco contatos, duas conversas qualificadas justificam refinar a proposta; somente um piloto pago com margem positiva e entrega compatível com a independência editorial justifica nova rodada. Zero resposta não prova inexistência de mercado; exige revisar adequação da oferta antes de escalar. Interesse verbal não conta como receita.

**Quem/custo:** Astra monta material e planilha; Gabriel/Miguel conduzem comercial; DSN-Chefe/CM validam fronteira editorial; ZM/dono técnico confirma espaço e capacidade sem fazer implantação nesta etapa. Um dia de preparação estimado; sem estoque, novo sistema ou serviço contratado. A [equipe pública do Cafezinho](https://www.ocafezinho.com/quem-somos-o-cafezinho/), consultada em 05/09/2026, identifica Gabriel Barbosa como diretor executivo e marketing; a atribuição concreta do piloto depende do Miguel.

## 6. Complemento Moka: ganhar dinheiro sem cobrar pelo núcleo

A arquitetura e os custos do produto serão aprofundados pela frente técnica do Astra. Aqui fica o desenho comercial, subordinado à ordem de **manter o Moka gratuito**:

1. **Apoio optativo:** contribuir para manutenção, sem retirar funções essenciais de quem não paga. Explicar a destinação, não prometer recurso ou suporte pessoal ilimitado. Não misturar contabilmente apoio ao Cafezinho e apoio ao Moka sem identificar a finalidade.
2. **Patrocínio contextual:** marca identificada em demonstração/material autorizado, escolhida pelo contexto público da atividade, nunca por livros privados, anotações, conversas ou inferência de interesse pessoal. Patrocinador não recebe dados privados e não compra interferência editorial.
3. **Serviço B2B separado:** implantação assistida, treinamento ou suporte com escopo/SLA limitado para instituição interessada. Cobra-se serviço adicional, não o direito de qualquer pessoa usar o núcleo gratuito. Primeiro entrevistar compradores com autorização; não construir painel corporativo antes de demanda e orçamento.

Não vender dados, não condicionar exportação pessoal a pagamento e não instalar rastreamento comercial oculto. A descrição “gratuito” precisa distinguir aplicativo de despesas opcionais do provedor de IA escolhido pelo usuário: BYOK não significa processamento sempre local nem custo externo zero. Rever as promessas das peças antes de distribuí-las. [Ressalvas e evidências do parecer anterior](</home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/PARECER_ASTRA_CRESCIMENTO_MOKA_CAFEZINHO_YOUTUBE_20260905.md:27>).

## 7. O que acontece agora e o que depende de autorização

**Astra sozinho agora:** consolidar fontes e lacunas, preparar pares de artigos/minutas/proposta comercial, recalcular exports existentes, registrar critérios de decisão e confrontar versões do material Moka. Não abrir coleta paralela nem alterar o que os donos já mantêm.

**Donos precisam confirmar:** DSN-Chefe, qual export recente está completo; DS-N Publicidade/financeiro, quais receitas e meios de apoio estão conciliados; responsável Moka, qual versão está no ar e quais eventos são verificáveis; Gabriel/Miguel, qual oferta/parceiro faz sentido. Perguntas não foram enviadas por este apoio.

**Miguel decide:** qual único piloto executar primeiro e seu escopo; chamadas públicas, abordagem comercial e qualquer gasto adicional. O quórum de pelo menos três entre CL/CM/AGY/ZM continua aplicável às implementações não já autorizadas; aprovação de estudo não equivale a publicação. Nenhuma proposta aqui garante receita.

Minha prioridade é **1 → 2 → 3**, com a preparação comercial podendo ocorrer em paralelo à conferência dos dados. Se o apoio já estiver operacional e os agregados disponíveis, o experimento 2 pode vir primeiro por ser o caminho mais curto até uma receita diretamente observável. Se a fonte estiver incompleta, entregar essa lacuna é melhor do que inventar um resultado.

— Apoio AST de crescimento · 05/09/2026

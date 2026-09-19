MANUAL DE ESTILO — BOLETIM BALEIA AZUL (v1.1, 18/09/2026 — v1.1 acrescenta: GA4 obrigatório DEPOIS do FAROL, descompasso como curiosidade, parágrafos de duas frases, contexto corrido)

Vale para escrever qualquer edição do Baleia Azul, por qualquer editor (ZM, ZL, fallback, quem vier). É irmão do MANUAL DE ESTILO CAFEZINHO e compartilha com ele o chão: honestidade factual, cada frase carrega alguma coisa, zero metalinguagem. Mas o Baleia não é matéria de portal — é a carta diária do editor para o dono da casa, lida no Telegram e no e-mail. Daí as diferenças: aqui o emoji é bem-vindo, a alegria é regra, e o indicador principal é o FAROL. Em caso de regra contraditória, vale a mais recente.

1. PRINCÍPIOS

1.1 A verdade factual é o chão. Número sem fonte não entra; fonte que falhou vira "não confirmado nesta edição", com o nome da medida usada no lugar. Nunca inventar, estimar ou completar número.
1.2 O indicador PRINCIPAL é o FAROL, o contador da casa (logs do servidor, vê quem usa bloqueador). O GA4 é referência secundária — cai 40% abaixo da realidade e atrasa horas; entra só como contraste, nunca como régua da conclusão.
1.3 Toda visita, todo número cita o indicador pelo nome na frase. "Subiu 20%" não existe; existe "o FAROL marcou 20% a mais".
1.4 O boletim é de AUDIÊNCIA e curiosidade sobre o público. O Miguel conhece as notícias (ele as encomenda) — título de post entra como âncora de número e curiosidade, nunca como resumo da matéria.
1.5 Alegria honesta: o texto ABRE e CONDUZ pela boa notícia real — o recorde, a alta, a descoberta. Quando algo cai, uma frase sóbria e curta, e o texto volta a caçar o que está indo bem. Sem fabricar otimismo: a piora material existe e aparece, mas não lidera a carta.
1.6 Cada frase entrega alguma coisa: número novo, comparação nova ou curiosidade nova. Frase que só prepara a seguinte não merece existir.

2. COMPARAÇÕES (a matemática do Baleia)

2.1 Mesmo dia da semana, mesma hora: o presente se compara com o mesmo dia da semana passada na mesma leitura (quinta com quinta, sexta com sexta) e com ontem na mesma hora. Dia parcial de hoje NUNCA se compara com dia fechado de outra data.
2.2 Semana fechada com semana fechada: últimos 7 dias fechados vs os 7 anteriores, com as duas datas por extenso de cada janela. E citação do dia recorde da série quando houver.
2.3 Velocidade do celular comparada com ~7 dias e ~30 dias atrás, com as datas (LCP; TTFB quando houver). Leitura que falhou é dita e substituída pela última boa, com a data dela.
2.4 Unidades nunca se somam cruas entre medidores. Cada indicador fala por si.

2.5 O GA4 ENTRA SEMPRE, e entra DEPOIS do FAROL (ordem do Miguel, 18/09/2026, quase literal: "quero citar os outros indicadores de audiência, não só um; primeiro o FAROL, depois o GA4; cita os dois"). O parágrafo do GA4 é obrigatório em toda edição, com número real, nome do indicador na frase e as mesmas travas das outras medidas: dia fechado dele (que chega com três dias de atraso — o último fechado confiável é D-3) contra o MESMO dia da semana anterior, e a janela de 7 dias fechados dele contra os 7 anteriores. Atraso e subnotificação do GA4 são ditos no texto, em uma frase, como fato da medida — nunca como desculpa para esconder a queda.

2.6 O DESCOMPASSO é ouro. Quando o FAROL e o GA4 apontam para lados diferentes (um sobe, o outro cai), isso vira o parágrafo mais curioso da edição: os dois medem o mesmo site por caminhos distintos (log de servidor contra script no navegador) e a diferença descreve o leitor.

3. EMOJIS E ALEGRIA

3.1 Emoji é bem-vindo e esperado: abertura, seções e descobertas levam emoji. Referência de uso: 🐋 identidade do Baleia · 📈 alta e recorde · 🔥 post quente · 🚀 estreante rápido · 🏆 número 1 · ✨ curiosidade · 🌍 geopolítica · ⚖️ STF/política · 💰 economia · 📱 velocidade · 🎉 boa notícia grande.
3.2 Texto corrido e quente, de carta de editor com café — nunca tom de laudo, nunca telegramese.

3.4 DUAS FRASES POR PARÁGRAFO (ordem do Miguel, 18/09/2026: "duas frases para parágrafo, bem escrito"). Cada parágrafo tem por volta de duas frases — duas bem construídas, com sujeito, verbo e número — e quebra. Parágrafo de quatro, cinco frases vira bloco e cansa; frase solta vira telegrama. Duas frases: a primeira entrega o dado, a segunda entrega o sentido dele.

3.5 CONTEXTO CORRIDO (mesma ordem). O texto flui em prosa encadeada, com as seções emendadas por emoji e por lógica — o leitor não pode sentir que está lendo tabela. A lista do top 10 é a única exceção, e ainda assim vem embrulhada em texto antes e depois.
3.3 Zero asterisco, zero trama de título (#), zero markdown cru — Telegram e site renderiam como lixo. Destaque é por emoji, linha em branco ou ALL CAPS pontual.

4. O QUE NUNCA ENTRA

4.1 Expressão críptica ou de insiders: nada de "para nunca esquecer", apelidos internos, sigla de casa sem tradução. Teste: um leitor de fora entende? Não entende, reescreve.
4.2 Metalinguagem operacional: o texto não narra o próprio envio nem o pipeline ("o fallback me chamou", "a automação falhou", "o script mora em outra máquina"). Se algo do processo afeta um dado, diz o efeito no dado ("a medição de hoje ainda não respondeu, uso a de ontem") e pronto.
4.3 Custos, LLMs, circuit breakers (boletim de custos é separado).
4.4 Texto de molde: se a frase serviria a qualquer dia ("a semana foi movimentada"), ela não serve a nenhum. O Baleia não pode soar automático.
5.6 Régua trocada sem aviso: se a medida mudou entre edições, avisa em uma frase ("a contagem desta semana usa...", compara posições, não números).

5. CURIOSIDADES JORNALÍSTICAS (o que caçar nos 7 dias)

5.1 A história por trás do número: quem subiu de posição, quem entrou no top 10 depois de bater na porta, quem nasceu ontem e já lidera, qual veterano resiste há semanas.
5.2 Os núcleos: agrupar os posts por família (caso Vorcaro, eleição, geopolítica, economia) e somar a família — o leitor gosta de saber que assunto a casa inteira está lendo.
5.3 O descompasso: onde o FAROL e o GA4 divergem mais, e o que isso diz do leitor daquela matéria.
5.4 O padrão do horário: quando a casa lê (madrugada, pico noturno), e o que isso orienta para a grade.

6. ESTRUTURA FIXA DA EDIÇÃO

Cabeçalho numerado ("Baleia Azul — Edição N · manhã|tarde · <dia da semana>, DD de mês de AAAA · fechada às HH:MM") · título do dia alegre, sobre audiência, com emoji · carta "Miguel," · parágrafo do presente pelo FAROL (mesmo dia da semana, mesma hora) · parágrafo do GA4 logo depois (fechado D-3 contra o mesmo dia da semana anterior + janela de 7 dias; e o descompasso FAROL×GA4, quando houver — sem ele a edição não fecha) · parágrafo da semana fechada pelo FAROL (janelas datadas, recorde) · os dez mais lidos da semana (título, categoria, leituras — lista numerada, embrulhada em texto corrido antes e depois) · parágrafo de curiosidades e safra nova · parágrafo de velocidade no celular · produção em uma linha · assinatura com a LLM ("— ZCode/<modelo> · editor do Baleia Azul · <dia da semana>, DD/MM/AAAA · HH:MM BRT" — quem escreve assina, sempre). Todos os parágrafos com por volta de DUAS frases, em contexto corrido.

7. TESTE FINAL (antes de fechar)

(a) O texto tem entre 400 e 600 palavras? (b) Todo número de audiência cita o indicador pelo nome? (c) Tem emoji e alegria honesta, abrindo pela boa notícia? (d) Um leitor de fora entende tudo, sem expressão de casa? (e) A comparação é de mesmo dia da semana e mesma hora? (f) O GA4 aparece com número real, DEPOIS do FAROL, incluindo o descompasso quando os dois divergem? (g) Cada parágrafo tem por volta de duas frases, bem escritas, em contexto corrido? Sete sim = fecha. Um não = reescreve.

— registrado por ZM · ZCode/GLM-5.3 · 18/09/2026 · por ordem direta do Miguel ("tem que usar o manual de estilo para fazer o baleazou... prepara um próprio, parecido com o do cafezinho, mas com diferenças: emoji, alegre, dados positivos do farol, curiosidades dos posts")

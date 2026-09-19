# Fórum — "Sul Global" é diretriz IMPLÍCITA: proibida a repetição mecânica (EMU-13)

- **Data:** 08/09/2026 ~19:4x-20:1x BRT
- **Autor do registro:** ZCode (Qwen3.8-Max), Dell
- **Ordem do Miguel (voz, 08/09 ~19:4x):** ao ver o post da Índia/Su-30 (269343), denunciou que a cadeia voltou a "repetir que nem papagaio: sul global, para o sul global" nos posts geopolíticos — diretriz que já tinha sido resolvida e "na reforma recente voltou". Regra dele, quase literal: **"a notícia não é sobre sul global; que isso é uma vitória do sul global está implícito; não tem que ficar repetindo de forma mecânica, repetitiva, chata. É uma diretriz implícita, só em alguns casos — não é para todo texto geopolítico terminar 'para o sul global'. Deve ter uma diretriz forçando o vertical, o redator, a uma linguagem repetitiva — vê lá, com certeza aconteceu isso."**

## 1. Caso concreto e medição

- Post-gatilho: **269343** — "Índia estuda equipar seus 258 caças Su-30 com míssil russo de 300 km de alcance" (vertical geo, ciclo V4.1 07/09 09:55, juiz 1 nota 6,62 com motivo "forte componente BRICS e multipolaridade, mas o gancho brasileiro é indireto"; juiz 2 5,88; publicado 10:45).
- Fecho do post: *"Para o Brasil, o plano indiano oferece uma referência sobre como países do Sul Global podem combinar cooperação externa, adaptação local e prolongamento da vida útil de frotas militares."*
- Medição (wp-cli, 30 posts publicados mais recentes do robô 5470): **29 com ZERO menção literal a "Sul Global"; 1 (o 269343) com uma**. Ou seja: o papagaio NÃO é a frase literal repetida dentro do texto — é o **molde de fecho**: quase toda matéria internacional termina amarrando a notícia ao Brasil/Sul Global:
  - 269366 (Sheinbaum): "Para o Brasil e o restante da América Latina, o episódio reforça…"
  - 269363 (ponte Rússia–Coreia): "Para o Brasil, parceiro da Rússia no BRICS, seu significado está…"
  - 269405 (petróleo US$ 100): "…poderá alcançar as projeções brasileiras de inflação e juros."
  - 269430 (Ormuz): "…reduziria a exposição de países importadores, inclusive o Brasil…"
  - 269337 (NYT×OpenAI): "…inclusive para usuários brasileiros…"

## 2. Causa raiz — 5 camadas VIVAS forçando o gancho explícito + 1 resolução MORTA

1. **Portal do redator** (`NYC /root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md` §10 "Bom gosto", injetado em TODO briefing do redator via `v41_ciclo.py:831`): *"Tema estrangeiro só com gancho brasileiro: consequência aqui, comparação, ângulo do Brasil"* + *"O fecho abre o horizonte do leitor"* → o redator materializava o "gancho" num parágrafo final formulaico.
2. **Diretriz qualidade viva** (`dados/diretriz_qualidade_viva.md`, injetada no briefing `v41_ciclo.py:829` e no worker V4 `:2926`): lições diárias do Tribunal punindo texto que "não conecta à vida do leitor" (06/09 lição 3: "O post 269233 peca por não conectar a crise geopolítica à vida do leitor"; 07/09: "Sempre conecte os fatos a consequências concretas para o leitor").
3. **Gerador do Tribunal** (`codigo/tribunal_agentic_diario.py`, cron 20:30): RUBRICA com subnota *"consequencia: fica claro o que muda na vida do leitor?"* → o loop regenerava a diretriz da conexão explícita todo dia.
4. **Padrão de curadoria** (`dados/PADRAO_CURADORIA_QUALIDADE.md`, lido pelo juiz 1/2 via `v41_ciclo.py:274`): *"Tema estrangeiro só entra com gancho para o Brasil"* + *"Elegância = relevância com gancho brasileiro"* + peso `interesse_br` 2.0 com mínimo 5 (`juiz_qualidade.json`).
5. **Manual de estilo unificado** (Dell `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md:108`, lido por revisores/agentes): *"Corpo — 4 camadas E-E-A-T: … (3) impacto no Sul Global/BRICS/Brasil →"* — camada OBRIGATÓRIA.
6. **A resolução que o Miguel lembrava EXISTIA, mas ficou na camada morta:** os contratos V4 (`NYC /root/v4_labs/contratos/v4_internacional_v1.md`) já diziam desde a reforma anterior: *"Mostrar consequência para o Brasil ou para o Sul Global **quando houver**"* (l.35), *"Essa análise é **opcional**. Não force `Sul Global`, `imperialismo`, `BRICS`…"* (redacao_v1 l.35), *"nunca por preenchimento automático"* (l.133), *"Uma matéria internacional pode ser excelente sem mencionar imperialismo, BRICS ou Sul Global"* (l.37). **A cadeia V4.1 NÃO lê os contratos** (grep: zero referências em `v41_ciclo.py` e no worker). A missão de qualidade de 06-07/09 (juiz de qualidade + BOM GOSTO + Tribunal diário) reinstalou a obrigação nos arquivos vivos do V4.1 sem herdar a salvaguarda do contrato. É isso que o Miguel percebeu como "a gente já tinha resolvido e voltou".

## 3. Cura aplicada (08/09 ~19:5x-20:0x, backups `.bak_pre_emu13_sulglobal_20260908` / unificado `.bak_pre_emu13_20260908`)

1. **Portal §10 (NYC, canônico):** regra reescrita — tema estrangeiro entra pelo próprio mérito; relevância para o leitor brasileiro é **IMPLÍCITA** (mora na pauta e no ângulo, não num parágrafo obrigatório); Brasil/Sul Global/BRICS só nomeados quando o fato em si pedir; **fecho-papagaio proibido (EMU-13)**; fecho nunca amarra toda matéria estrangeira ao Brasil. **Novo md5 canônico: `fd7e23d25d6dd6a97d142c0cefd95018`** (Dell `Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md` sincronizado, md5 idêntico).
2. **Diretriz viva (NYC):** guarda permanente inserido logo após o cabeçalho — sobrevive ao trim de 5 dias do gerador (fica em `linhas[0]` do `split("## ")`). Diz que "conectar com o leitor" NUNCA significa parágrafo "Para o Brasil…" e que as lições diárias devem ser lidas com a regra por cima.
3. **RUBRICA do Tribunal (NYC .py):** regra permanente — não rebaixar nota por ausência de parágrafo explícito "Para o Brasil/Sul Global/BRICS"; NUNCA gerar `sugestao_diretriz`/lição pedindo conexão mecânica; fecho-papagaio é VÍCIO, não mérito. `py_compile` OK (venv + system). 1ª corrida com a rubrica nova: hoje 20:30 BRT.
4. **PADRÃO_CURADORIA_QUALIDADE.md (NYC):** item 4 — o gancho é de **PAUTA** (o leitor brasileiro se importa?) e pode ser **IMPLÍCITO**, não exige nem deve exigir parágrafo "Para o Brasil…" no texto; item 1 do BOM GOSTO — "Elegância = relevância para o leitor — gancho brasileiro pode ser implícito, nunca fecho mecânico".
5. **MANUAL_DE_ESTILO_UNIFICADO.md (Dell):** camada (3) das 4 camadas E-E-A-T agora condicional ("impacto no Brasil/Sul Global/BRICS SÓ quando o fato pedir — nunca como fecho obrigatório") + **EMU-13 completa** registrada após a EMU-12 (com casos, regra em 4 pontos e a linhagem do contrato V4).
6. **NÃO tocados:** `v41_ciclo.py` (código), `v4_vertical_draft_worker.py` (compartilhado, proibido), prompt da tese dinâmica ("consequência material para o leitor" permanece — o que mudou foi a INTERPRETAÇÃO nos arquivos que o redator e o tribunal lêem), contratos V4 (já corretos), revisores R1/R2 tencent (sem a regra).

## 4. Estado / próximos passos

- ✅ Pronto: 5 camadas vivas curadas + EMU-13 canônica + portal sincronizado Dell×NYC + Tema Duplo + catalogação (NODE_ESTILO + ATUALIZACOES) + monitor.
- 🔎 Prova ao vivo: próximos ciclos geo (artefatos `NYC /root/v4_labs/dados/v41_ciclo/`) — conferir se os fechos das próximas 2-3 matérias internacionais saem sem o molde "Para o Brasil…". Rondas podem verificar.
- 📌 Distinto e já pendente: **§9-CL antirrepetição DETERMINÍSTICA no juiz** (parecer ZM-20260908-003) — gate mecânico pegaria esse tipo de molde no juiz 2; **aguarda "vai" do Miguel**.
- ↩️ Rollback (6 comandos `cp` dos `.bak` — ver memória técnica).

## 5. O que preciso de você (Miguel)

- Nada obrigatório. Se quiser reforço mecânico (não só diretriz), dar o "vai" no §9-CL antirrepetição determinística — o molde "Para o Brasil…" repetido entre posts vizinhos seria barrado no juiz 2 por comparação, não por prompt.

---

## 6. ADENDO — FASE 2: O PRINCÍPIO DO EQUILÍBRIO (ordem do Miguel 08/09 ~20:1x)

O Miguel elevou o caso a doutrina geral: a reforma do V4 limpou o excesso de regras e deu liberdade aos verticais; o V4 ficou "quase sem regra nenhuma, meio perdido"; a pesquisa dos princípios trouxe "tudo de novo — 8, 80". Veredito: **"Você não está chegando ao equilíbrio."**

A doutrina: princípios editoriais e linha política SIM, porém IMPLÍCITOS — guardrails "pra não fugir do controle", nunca para amarrar a criatividade, nunca para gerar repetição de papagaio ou clichê. O redator cria, mantém liberdade, foca no assunto e **se aprofunda**: o web search dos produtor existe "justamente pra ele poder se aprofundar… buscar detalhes que às vezes não tá na notícia original". Sobre o 269343: "era um texto que era para discorrer mais sobre armas, pode até falar em sul global eventualmente, mas o que a gente está vendo aqui é uma fórmula pronta, o que não pode."

### Cura fase 2 (4 arquivos NYC, backups `.bak_pre_equilibrio_20260908`, py_compile OK)

| Camada | O que mudou |
|---|---|
| `codigo/v4_vertical_redactor_runtime.py` (prompt, linha ~154) | Pesquisa web agora é TAMBÉM para SE APROFUNDAR (detalhes concretos, contexto técnico/histórico, declarações, desdobramentos — usados no corpo). Princípios/linha = GUARDRAILS implícitos, nunca roteiro; fórmula pronta, molde e clichê = vícios (EMU-13). |
| `dados/MANUAL_DE_ESCRITA_PORTAL.md` §10 | Bullet novo "Liberdade com linha — o equilíbrio" (guardrails, aprofundamento, caso 269343 como exemplo do que não pode). md5 novo `0f49b73fa226651029692a4a04276953` — cópia Dell sincronizada idêntica. |
| `dados/diretriz_qualidade_viva.md` | Guard permanente ganhou frase EQUILÍBRIO: princípios não geram fórmula; texto se preenche com aprofundamento, nunca molde/clichê. |
| `codigo/tribunal_agentic_diario.py` RUBRICA | Fórmula pronta/preenchimento de molde = vício (subnota originalidade cobre); premiar texto que se aprofunda com detalhes concretos. |

⚠️ Incidente §112: a entrada EMU-13 do `MANUAL_DE_ESTILO_UNIFICADO.md` (Dell) foi CLOBBERADA por escrita concorrente às 20:09 (linha 108 sobreviveu, a entrada sumiu). Reinserida completa com o adendo equilíbrio às ~23:0x (backup `.bak_pre_emu13_reinsercao_20260908`).

### Prova pendente (próximas rondas)

- Próximos 2-3 posts internacionais: fecho livre do molde "Para o Brasil…" e corpo aprofundado no assunto (números, contexto técnico).
- Tribunal 20:30 (já roda com a RUBRICA nova): `tribunal_2026-09-08.json` sem sugestao_diretriz pedindo conexão mecânica.
- Guard da diretriz viva inteiro após o trim (`head -4`).

---

## 7. ADENDO — DOUTRINA: DETERMINÍSTICO SUBORDINADO À INTELIGÊNCIA DINÂMICA (ordem do Miguel 08/09 ~20:3x)

Falas do Miguel: "não quero nada determinístico mexendo com redação" e, em seguida, o esclarecimento: "pode ter uma coisa ou outra determinística, mas subordinada à inteligência dinâmica."

**Doutrina final:** a redação é guiada por inteligência (princípios, prompts, juízes com raciocínio). Mecanismos determinísticos podem existir como instrumentos AUXILIARES — detectores, contadores, comparadores de molde — mas sempre SUBORDINADOS: o sinal mecânico vira EVIDÊNCIA para o juiz inteligente, que decide com raciocínio. Nunca gate automático que bloqueia ou reescreve texto por regex/molde.

**Impacto no §9-CL** (antirrepetição determinística, parecer ZM-20260908-003, aguarda "vai"): se um dia for implementado, o desenho passa a ser — detector mecânico (comparação de fechos/moldes entre posts vizinhos) gera sinal/nota que o juiz 2 (LLM) lê como evidência e pondera; sem reprovação automática, sem reescrita forçada. Segue aguardando "vai".

**Por que o molde poderia persistir mesmo fora da diretriz** (resposta registrada à pergunta do Miguel): (1) vício espontâneo do modelo redator — fecho formulaico "Para o Brasil…" é hábito comum de LLM em texto geopolítico, aparece sem diretriz nenhuma; (2) o ecossistema REGENERA diretriz — o Tribunal escreve lições diárias na diretriz viva (gerador curado + guard permanente, mas o risco é estrutural); (3) resíduo — lições antigas sobrevivem no trim de 5 blocos por alguns dias. Nada nos arquivos vivos força mais o molde; se ele reaparecer, a causa será o modelo, e a cura é inteligência dinâmica (prompt/princípios/juízes), nunca gate mecânico.

## 8. ADENDO — REESCRITA DO 269343 NO AR (ordem do Miguel 08/09 ~22:4x, publicado ~23:1x)

**Ordem (quase literal):** "aproveita e reescreve esse, sem esse clichê do sul global. é um post com boa audiência. aliás, posts sobre sul global são muito importantes para gente, por isso temos que caprichar na qualidade e criatividade."

**Nuance gravada (portal §10, NYC+Dell, md5 canônico novo `1d092d8adcf83bf05100d7ff5af1bf3a`, backup `.bak_pre_tema_sulglobal_20260908`):** pautas do Sul Global são importantes para a casa — a proibição é da FÓRMULA, nunca do TEMA; nesses assuntos a cobrança é capricho redobrado em qualidade e criatividade.

**A reescrita (publicada e verificada no permalink):**
- 28 parágrafos + 4 h3 (o original usava `<strong>` como heading, violação da estrutura portal §8), ~6.100 caracteres, título/data/status/excerpt/capa intocados.
- Corpo APROFUNDADO NAS ARMAS, como o Miguel mandou: RVV-BD/R-37M (sigla decodificada, origem nos MiG-31BM, alvo real = AEW&C/tanques/plataformas de guerra eletrônica, Mach 6, guiamento inercial + enlace de dados + radar ativo terminal, disparo além do horizonte dos sensores); nuances de alcance (300 km = teto divulgado, não promessa; variante doméstica 200-300 km × export ~200 km, versão não confirmada, Altair); contrato (US$ 1,2 bi/~300 R-37M revelado pelo SCMP no FIM DE ABRIL, R$ 6,1 bi no câmbio de 8/9, entregas 12-18 meses; rearmamento US$ 25 bi março + US$ 40 bi fevereiro Reuters; Operação Sindoor; véspera da visita de Putin/BRICS); integração de engenharia (gerenciamento de armamento/aviônica/software, Super Sukhoi, AL-31FP na HAL, +12 jatos em Nashik); corrida dos arsenais (PL-15 nos J-10CE/JF-17, teto PAF 145, J-20/PL-17 no Tibete, relatos J-35, Astra Mk1/Mk2/Mk3 ramjet, Rafale+Meteor, atrito com a França e os 114).
- BRICS: menção factual única no meio do corpo (visita de Putin) — o "eventualmente" do equilíbrio, nunca molde de fecho.
- Fecho novo abre horizonte sem amarração Brasil/SG: "Capacidade comprada não é capacidade operada… Dessa distância, invisível e móvel, sairá a verdadeira fronteira aérea do subcontinente."
- **CORREÇÃO FACTUAL:** o original dizia "em 15 de julho… fechou contrato" — quatro fontes (SCMP via moneycontrol 29/04, Aereo 28/04, Altair 04/05, Cavok 02/05) situam a revelação no FIM DE ABRIL de 2026 → corrigido para "revelou no fim de abril".
- Verificador (reconstruído do apêndice do manual, `/tmp/verifica_269343.py`): 13 repetições vizinhas → corrigidas → 1 flag restante = anadiplose DELIBERADA do fecho ("a que distância… Dessa distância…"), martelo único do §4. ser/haver 2 em 56 frases. Zero pontuação proibida/metalinguagem/spoiler/ligação preguiçosa/início proibido/dupla negativa/aspas retas; nenhum parágrafo >300 chars ou >2 frases.
- Backup do original: `Backups/posts_editados/269343_pre_rewrite_20260908.md` (com cabeçalho título/data/status/URL).
- Publicação: scp + `sudo -u www-data wp --path=/var/www/ocafezinho post update 269343 /tmp/269343_novo.html` (arquivo POSICIONAL, nunca @file); status `publish` e data `2026-09-07 10:45:00` intactos (como prevê a receita).
- **Cache (aprendizado novo):** o Cloudflare está no caminho mas `cf-cache-status: DYNAMIC` — NÃO cacheia o HTML. A página velha vinha do WP Rocket: após `wp eval 'rocket_clean_post(269343)'` o HTML velho persistiu ~5 min (confirma a linha 568 do Cofre: "cache de URL exata ~5 min"), depois novo no ar. Teste de isolamento por camada: `curl --resolve www.ocafezinho.com:443:190.89.239.65` (origin direto) e `?nocache=` (bypassa o Rocket). Armadilha do permalink RECONFIRMADA: `/2026-09-07/slug/` (hífens) = 404; certo = `/2026/09/07/slug/`.
- O "Brasil e do Sul Global" que resta na página é da caixa de newsletter do TEMPLATE (mobília fixa do site), não do artigo.

**Estado:** ✅ CONCLUÍDO — post novo no ar e verificado. Prova pendente segue a mesma (próximos ciclos internacionais sem molde).

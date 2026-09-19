# Fórum — Reportagem Nikolas parte 2: parecer ZM + conquista das fontes ANM (ZM-20260905/06)

**Ref:** continuação de `forum_[REDACTADO 19/09/2026 — token já revogado (401 confirmado); valor jamais em fórum, só no Cofre].md`
**Quem:** ZCode (ZM) — Kimi K3, sessão Dell, 05/09 ~21h → 06/09 ~00:3x BRT
**Pedido do Miguel:** (1) revisar a reportagem parte 2 no GitHub e apontar lacunas; (2) deixar opinião no próprio GitHub; (3) pegar os dados que faltaram ("usa o ip royal se for o caso").

## O QUE ACONTECEU

1. **DOU autenticado (pendência 3 da reportagem — RESOLVIDA):** PDF oficial da Imprensa Nacional (`INPDFViewer?jornal=515&pagina=59&data=10/04/2026`) confere 100% com o print ABRAPCH do repo: Relação 12/2026, barragem Água Fria, processo 930.096/2000, Auto de Embargo 13/2026, PAS 48054.930202/2025-45. Salvo em `/tmp/dou59_oficial.pdf` + `.txt`.
2. **Folha da Câmara conferida (pendência 5 — RESOLVIDA):** total R$ 709.424,03 em 37 meses, exato. Achado novo: mar/2026 = SP22 (reenquadramento), R$ 18.655,12 + R$ 598,80 eventuais + auxílio R$ 3.144,94 (os 598,80 não estavam no CSV).
3. **Gmais na Receita ao vivo:** Horta administrador desde 18/02/2025; sócios desde 24/03/2021: Daniella Santos Wandeck e Luiz Fernando Vilela Leite.
4. **GRUPAMENTO 930.096/2000 ABERTO (pendência 2 — A MAIOR, RESOLVIDA):** consulta oficial SCM/ANM `dadosProcesso.aspx`, sessão de navegador real com captcha lido pelo MIGUEL (IA errou 4 leituras; humano acertou de primeira — HLTY, QXP3, C484). Grupo = Requerimento de Grupamento Mineiro, fase CONCESSÃO DE LAVRA, ativo, título 215 RGRU outorgado 20/10/2006, substância registrada TOPÁZIO IMPERIAL, Ouro Preto/MG, titular Topázio Imperial CNPJ 16.857.294/0001-02. **8 processos associados (14/08/2020), ~725,57 ha, incluindo 291.701/1936.**
5. **291.701/1936 EM DETALHE:** manifesto de mina de 1936 (registrado 26/02/1938), concessão de lavra ATIVA, 78,78 ha, substâncias FERRO + MANGANÊS + TOPÁZIO + CALCÁRIO (ferro primeiro), arrendamento total averbado 1979, último evento 09/04/2007. **A concessão de FERRO está formalmente DENTRO do grupamento do áudio.**
6. **Eventos 2026 do grupamento:** auto de infração 1116/2026 (10/07, PAS 48054.931232/2026-50), prorrogação negada (16/07, of. 34810/2026/CORBCM), cumprimento de exigências 21/07 + 10/08×2 + 17/08 — ativo administrativamente vivo no ano do áudio público.
7. **Prints:** print fullPage do 291.701/1936 salvo; print do grupamento AGUARDA 1 captcha do Miguel.
8. **Falhas registradas:** TSE 403 WAF; JUCEMG pendente; TRF6 DNS; TCE-MG sem resposta; pauta 88ª ROP ausente da listagem SEI (só até 86ª); IPRoyal HTTP 402 sem saldo.

## ENTREGA NO GITHUB (repo migueldorosario1/cafezinho, branch master)

- `pesquisas/nikolas-vorcaro-faria/fontes-zm-2026-09-06/anm_930096_2000_dadosprocesso.txt`
- `pesquisas/nikolas-vorcaro-faria/fontes-zm-2026-09-06/anm_291701_1936_dadosprocesso.txt`
- `pesquisas/nikolas-vorcaro-faria/fontes-zm-2026-09-06/print-anm-291701-1936-dadosprocesso.png`
- `pesquisas/nikolas-vorcaro-faria/fontes-zm-2026-09-06/prompt-para-gpt-reescrita.md` (prompt de reescrita para o GPT)

## O QUE FALTA

- Print do grupamento 930.096/2000 (1 captcha do Miguel; form fica pronto)
- Parecer/opinião formal do ZM commitado no GitHub (pedido 2 original — o prompt de reescrita atendeu o pedido 3 com prioridade)
- TSE 2022/2024, JUCEMG, TRF6, TCE-MG (baixa prioridade)

## O QUE PRECISO DE VOCÊ (MIGUEL)

- 4 caracteres de captcha quando quiser o print do grupamento (eu preparo o form e submeto)
- Colar o `prompt-para-gpt-reescrita.md` no ChatGPT e mandar o GPT reescrever

## ADENDO FINAL (06/09 ~08:27 BRT — fase final com o Claude na v3)

- O Miguel entrou no SCM no navegador DELE (instruções via Telegram — o chat do ZCode estava com bug de sumir texto; prompt de investigação do bug em `Foruns/prompt_bug_texto_sumindo_zcode_20260906.md`) e colou o registro INTEGRAL do 930.096/2000 no chat (453 linhas, salvo como `anm_930096_2000_CONSULTA_MIGUEL_20260906.txt`).
- FATO-CHECK da v3: "multas em 25 autos" estava ERRADO — são 92 autos em 5 despachos de jan/2025 (14/01: 1, 17/01: 26, 21/01: 40, 23/01: 2, 27/01: 23). Corrigido DIRETO no rascunho (commit 56a47f9d): "Entre 14 e 27 de janeiro... 92 autos... quarenta num único dia, 21 de janeiro". Os 25 legítimos são os itens de prorrogação negada em 10/02.
- Capturas REAIS do Miguel commitadas e inseridas no artigo: `imagens/print-anm-scm-grupamento-930096-composicao.png` (substituiu a repro, commit f6253a2f) e `imagens/print-anm-scm-291701-1936-substancias.png` (nova, 028afd3d). Nota de imagens atualizada.
- Embargo de 2022 (Auto 41/2022) acrescentado ao texto; bloco de 31/12/2021 com 104 autos lavrados de uma vez (contexto de reincidência).
- ADENDO verificado commitado: `fontes-zm-2026-09-06/ADENDO-ZM-eventos-930096-verificados.md` (commit a84c0ba4) — timeline jan-abr/2025 completa + notas (7 autos com defesa aceita em 14/01; datas do registro são de publicação).
- Única sobra de imagem: a linha do tempo de eventos segue como reprodução tipográfica (opcional substituir).

## ARMADILHAS (ver memória técnica)

- Captcha do SCM expira em 90s A PARTIR DA GERAÇÃO da imagem; leitura por IA falhou 4/4; MIGUEL lendo + ZM submetendo funciona SE a mensagem chegar em <90s; o robusto é o MIGUEL digitar e clicar no navegador DELE e colar o texto/print no chat
- Página `pesquisarProcessos.aspx` NÃO cobre títulos antigos (CNPJ/NUP antigo = "nenhum processo"); a página certa é `dadosProcesso.aspx` (dropdown "Consulta")
- Campo de número exige formato COM pontos via `formatarDNPM` (930.096/2000; sem pontos = "Número inválido")
- CNPJ 41.332.820/0001-68 = GMAIS; Topázio = 16.857.294/0001-02
- Contar autos por regex contamina com números de PAS (48054.xxx/AAAA) e com o nº do processo — limpar `48054\.\d+/20\d\d` antes de contar `(\d{3,4})/20\d\d`
- fullPage screenshot do IAB sai em MOSAICO (repetido) — captura de tela nativa do usuário é limpa
- Bug do ZCode: texto do agente some do chat em turnos com muitas ferramentas — canal reserva = Telegram (ponte --send)

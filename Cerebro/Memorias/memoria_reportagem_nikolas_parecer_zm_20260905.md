# Memória técnica — Reportagem Nikolas parte 2: conquista das fontes ANM (ZM, 05-06/09/2026)

Par do fórum: `Foruns/forum_reportagem_nikolas_parecer_zm_20260905.md`

## Fluxo SCM/ANM que funcionou (receita)

1. `pesquisarProcessos.aspx` (SCM/site/admin) cobre só requerimentos/processos administrativos recentes. Buscas por CNPJ (da Topázio ou da Gmais) e por NUP antigo (com OU sem pontos) retornam "Nenhum processo encontrado" — não é erro de captcha, é cobertura da base.
2. A página certa para títulos antigos é `https://sistemas.anm.gov.br/SCM/site/admin/dadosProcesso.aspx` (menu "Consulta" → "Dados do processo"). Campos: `ctl00_conteudo_txtNumeroProcesso` + captcha `ctl00$conteudo$CaptchaControl1` + botões `btnDadosBasicos`/`btnConsultarProcesso`.
3. Campo de número usa `formatarDNPM(this)` no onkeyup, maxlength 12 → formato exigido COM pontos: `930.096/2000`, `291.701/1936`. Sem pontos = "Número inválido." (validação client-side, não consome captcha).
4. Captcha: 4 caracteres, expira em 90 SEGUNDOS ("O código digitado expirou após 90 segundos"), rotaciona a cada postback. Mensagem de erro explícita: "o código digitado não confere com o código da imagem".
5. Leitura de captcha por modelo de visão falhou 4/4 (DJP8, P8BL, NCHG, H7KT — leituras divergentes da mesma imagem). Solução: HUMANO no loop — Miguel lê os 4 caracteres no chat, ZM preenche e submete em <90s (acertos: HLTY, QXP3, C484). Padrão de trabalho eficaz.
6. Extração do captcha por canvas (drawImage + toDataURL 4x, imageSmoothing off) funciona para MOSTRAR ao humano/modelo — mas só o humano leu certo.
7. Após busca bem-sucedida o form some; `location.reload()` traz de volta com captcha novo (re-setar o número depois).
8. Navegação na aba do IAB: sem `tab.playwright.goto/reload` — usar `location.href=...` / `location.reload()` via `evaluate`. Screenshot: `tab.screenshot({fullPage:true})` funciona.
9. Busca viva pelo navegador do usuário (IAB compartilhado) + `nodeRepl.emitImage` → vira URL CDN → ler via `analyze_image` (Read de PNG também vira CDN).

## Dados conquistados

- Grupamento 930.096/2000: 8 processos (~725,57 ha), título 215 RGRU outorgado 20/10/2006, fase Concessão de Lavra ATIVA, substância TOPÁZIO IMPERIAL, titular Topázio Imperial CNPJ 16.857.294/0001-02 (cadastro 827.500/1972), Ouro Preto/MG, NUP 27203.930096/2000-11.
- 291.701/1936: manifesto de mina 1936/1938, concessão ATIVA, 78,78 ha, FERRO+MANGANÊS+TOPÁZIO+CALCÁRIO, arrendamento total 1979, último evento 09/04/2007, NUP 27203.291701/1936-58.
- Eventos 2026 do grupamento: AI 1116/2026 (10/07, PAS 48054.931232/2026-50), prorrogação NEGADA (16/07, of. 34810/2026/CORBCM/ANM), exigências cumpridas 21/07+10/08×2+17/08.
- CNPJs: Topázio=16857294000102 (1971); Gmais=41332820000168 (2021-03-24); Estabil=11030358000183; Faria SIA=56902629000181.
- DOU oficial: INPDFViewer jornal=515 pagina=59 data=10/04/2026 (Relação 12/2026, embargo 13/2026, PAS 48054.930202/2025-45).
- Câmara mar/2026: SP22, 18.655,12 + 598,80 eventuais + 3.144,94 auxílios (CSV omite os 598,80).

## Arquivos

- `/tmp/nikolas/anm_930096_2000_dadosprocesso.txt` (80.141 chars) e `anm_291701_1936_dadosprocesso.txt`
- `/tmp/nikolas/print-anm-291701-1936-dadosprocesso.png` (fullPage 1265x1330)
- `/tmp/nikolas/prompt-para-gpt-reescrita.md` (também commitado no repo)
- `/tmp/dou59_oficial.pdf` + `/tmp/dou59_oficial.txt`
- GitHub: repo migueldorosario1/cafezinho → `pesquisas/nikolas-vorcaro-faria/fontes-zm-2026-09-06/` (commits via API contents com GITHUB_PAT_MIGUEL do intake)

## Pendências

- Print do grupamento (1 captcha); parecer ZM no GitHub; TSE/JUCEMG/TRF6/TCE-MG (baixa prioridade); IPRoyal sem saldo (402).

# 🧵 Fórum — Equipe de bots estilo GrokBot: plano para o ecossistema (líder + especialistas que conversam entre si)

> **Data:** 2026-08-29 00:45 BRT · **Autor:** ZCode (Qwen 3.8), sessão ZCodeProject
> **Gatilho:** Miguel mostrou o vídeo "Grok Bot Is Now Only $20 - Here Are 9 Wild Use Cases" (Paul J Lipsky, 27/08, https://www.youtube.com/watch?v=UyMJBUCyDIs) e pediu: "você não consegue montar um plano de bots assim, que trabalham sozinhos e falam comigo, e um vira o líder?"
> **Memória técnica:** [`Memorias/memoria_equipe_bots_grokbot_video_mapeamento_20260829.md`](../Memorias/memoria_equipe_bots_grokbot_video_mapeamento_20260829.md) · **Transcrição integral:** [`Foruns/anexo_transcricao_grokbot_video_20260827.txt`](anexo_transcricao_grokbot_video_20260827.txt)

---

## 🎬 O que o vídeo mostra (resumo fiel da transcrição)

O GrokBot (x.ai/bot) virou produto de **US$ 20/mês** (antes US$ 200; incluso em planos Cursor/SuperGrok/Teams elegíveis). O modelo mental do vídeo: **cada bot = um funcionário com papel fixo**, criado por conversa (sem configurar chave/modelo), e o recurso-estrela: **bots no mesmo canal conversam entre si e passam o trabalho adiante sem o dono aprovar cada passo**. Todos rodam num **computador na nuvem** logado nas ferramentas do dono (rotinas rodam com o PC desligado).

O elenco do autor do vídeo:

| Bot | Papel |
|---|---|
| **Chief / Captain** | chefe de gabinete / delegador: ponto de contato único, recebe tarefas e delega |
| **Scribe** | e-mail (Gmail): varre inbox, pesquisa remetentes, minuta respostas + calendário de conteúdo |
| **Seeker** | pesquisadora: monitora o X 24/7, acha oportunidades |
| **Mapmaker** | brainstormer: filtra o que a Seeker acha, decide o ângulo e o que vale subir |
| **Hemingway** | roteirista: conhece o tom de voz, escreve roteiros |
| **Prism** | designer: thumbnails |
| **Concierge** | assistente pessoal: Google Calendar, restaurante/DoorDash, conversa com a **Coach Cal** (fitness) |
| **Bob the Builder** | construtor: apps/sites; rotina mensal de atualizar o site |
| **Atlas / Hound / Nightingale** | viagens / compras / plano de saúde |

Fluxo mostrado: Miguel-do-vídeo pede à Chief "uma ideia de vídeo" → Chief fala com Seeker (pesquisa) → volta, passa a Hemingway (roteiro) → Hemingway chama Prism (thumbnails) — **tudo entre eles, sem humano no meio**. E agora o preço caiu de US$ 200 para US$ 20/mês.

## 🪞 Espelho: o ecossistema do Miguel JÁ é ~80% disso

O Miguel disse a frase certa: "os loops são isso". Mapeamento direto:

| Conceito do GrokBot | Já existe aqui |
|---|---|
| Bots especializados com rotina | Loops V4/V4.1/V4.2 (jornal), Fênix (parceria/cultura), Laura (central de produção), segurança/CCTV/instituto |
| Bots que rodam com o PC desligado | NYC (198.199.121.136) + Tencent — crons 24/7 |
| Canal onde bots conversam | Ponte Trindade + Ponte Laura (`inbox_trindade/`, `de_dell.md`/`de_laura.md`, `canal_trindade`) |
| Memória compartilhada entre bots | Cérebro (3 camadas) |
| Falar com o dono no celular | Ponte Cafezinho (Telegram) |
| Anti-colisão de trabalho | `MONITORAMENTO_DE_TRABALHO.md` (regra §112) |

**O que falta para ser um GrokBot nosso (os 20%):**
1. **O Chief**: hoje o Miguel gerencia as sessões na mão; não existe um delegador único que recebe a missão, quebra, distribui e consolida a resposta.
2. **Personas fixas com nome/cargo**: hoje as sessões são ad-hoc; o padrão GrokBot é "mesmo bot para o mesmo assunto, sempre".
3. **Handoff automático entre especialistas** (Seeker→Hemingway→Prism): as pontes transportam recados, mas ninguém "passa o bastão" de uma subtarefa sozinho.

## 📋 O plano proposto (3 fases)

**Fase 1 — O Chief (1 sessão de construção).** Criar o bot líder (sugestão de nome: **Capitão**, ou o que o Miguel quiser): sessão ZCode dedicada + rotina que lê uma caixa de entrada única (`Cerebro/Foruns/equipe/inbox_chefe.md` + Telegram via Ponte Cafezinho). O Miguel fala SÓ com o Chief; o Chief: decompõe a missão → registra no monitor → delega nos inbox das pontes (Laura = central de produção; loops NYC = jornal; Fênix = cultura) → consolida as respostas e reporta no Telegram.

**Fase 2 — Handoff entre especialistas.** Formalizar o padrão "ao terminar minha parte, entrego para o próximo bot" nos contratos dos loops (como Seeker→Mapmaker→Hemingway no vídeo). Exemplo concreto na nossa casa: pauta aprovada no jornal → redator → auditor visual → publicador, com o Chief só reportando o resultado.

**Fase 3 — Rotinas pessoais (estilo Scribe/Concierge).** Bots de vida pessoal: e-mail do Miguel (minutar respostas), calendário, lembretes — usando o que já existe (msmtp/IMAP da Fênix, cron, Telegram).

**Custo:** praticamente zero em infraestrutura (modelos já assinados: GLM/Kimi/Qwen/DeepSeek + US$ 7,99 de xAI pré-pago). Esforço: ~1-2 sessões para a Fase 1.

## ⚖️ Alternativa: assinar o GrokBot de verdade

- US$ 20/mês (SuperGrok); no Linux só via port comunitário não oficial (`grokbot-linux-port`, WIP) — ver Adendo 2 do fórum do DSH.
- Prós: UX pronta, computador na nuvem deles, configuração por conversa.
- Contras: custo novo mensal, binário não oficial no Linux, e os bots dele NÃO conhecem o Cérebro/pontes/loops (teria que reensinar tudo).
- **Parecer: construir o nosso.** A infraestrutura pesada (memória, canais, servidor 24/7, Telegram) já está pronta; o GrokBot pago seria recomeçar do zero um ecossistema que já roda.

## 📌 Estado da missão

- **O que aconteceu:** transcrição integral do vídeo obtida (yt-dlp no Dell, legenda en-orig), mecânica do GrokBot entendida, mapeamento contra o ecossistema feito, plano em 3 fases desenhado, Tema Duplo gravado.
- **O que falta:** decisão do Miguel: (a) aprova o plano nosso (e o nome do Chief)? (b) ou quer testar o GrokBot pago de US$ 20 (exige port não oficial no Linux)?
- **O que preciso de você (Miguel):** um "vai" para a Fase 1 (e o nome do líder), ou a escolha da alternativa paga.

---

## ➕ ADENDO 1 — 29/08 00:55 BRT: como o port comunitário consegue rodar o GrokBot no Linux (detalhe técnico)

Pedido do Miguel: explicar melhor como a comunidade (projeto `Nichokas/grokbot-linux-port`) conseguiu. Fonte: README oficial do repo (baixado via curl, 3.492 bytes; cópia em `/tmp/grokbot_readme.md`).

**O princípio:** o Grok Bot é um app **Electron** (Chromium + Node.js). Em apps Electron, o CÓDIGO do app (JS/HTML/CSS empacotados em `app.asar`) é o mesmo para qualquer sistema; o que muda por sistema é a "casca" (o binário do Electron) e meia dúzia de módulos nativos compilados por plataforma. Daí a receita:

1. **Detecção de versão** (`scripts/detect-version.sh`): os servidores da Cursor/xAI não publicam lista de versões; o script faz HEAD-probing de candidatos semver em `downloads.cursor.com` e o mais alto que responde 200 (e é mais novo que o `VERSION` atual) dispara o build.
2. **O port** (`scripts/port.sh`):
   - baixa o **Setup.exe oficial** (instalador NSIS do Windows);
   - extrai com **7z SEM Wine** (NSIS abre como arquivo; não precisa de Windows);
   - baixa o **Electron 42.1.0 oficial para Linux**;
   - **funde**: pega o `app.asar` (código do Grok Bot) do instalador Windows e coloca na casca Electron Linux;
   - **recompila os 6 módulos nativos** (`better-sqlite3`, `tree-sitter` etc.) para Linux com `@electron/rebuild`;
   - ajusta o `chrome-sandbox` (SUID 4755) e gera o tarball em `dist/`.
3. **CI diário** (`.github/workflows/auto-update.yml`, 06:37 UTC): detecta versão nova → build → GitHub Release + atualiza AUR (Arch), COPR (Fedora) e PPA (Ubuntu). Foi isso que publicou o v0.30.0 no dia 28/08, um dia após o upstream.

**Caveats para a decisão do Miguel:** WIP de mantenedor único (se a Cursor mudar o formato do instalador ou bloquear o download, quebra); precisa do plano pago de qualquer jeito (login é no app); é binário reempacotado por terceiro (confiança de cadeia de suprimento — mitigável: o script é aberto e dá para buildar localmente com `scripts/port.sh <versão>` usando p7zip, curl, unzip, node 22, python3). Licença declarada: o repo não contém os binários do Grok; artefatos são derivados da distribuição oficial no momento do build.

---

## ➕ ADENDO 2 — 29/08 01:05 BRT: funciona IGUAL ao Windows/Mac? o que dizem os relatos (auditoria GitHub/AUR)

Pergunta do Miguel: instalado o port, funciona igual ao Windows/Mac? Deu certo para quem usou? Alguém está usando os bots?

**Veredito: ainda NÃO é paridade total.** Auditoria ao vivo (api.github.com + AUR, 29/08 01:00):

- **PR #5 (aberto, NÃO mergeado, 27/08, autor externo "laptopcomputer-user")** é o documento-chave: afirma que o asar de Windows/macOS **não sobe um desktop Linux usável sem edits** e lista os defeitos: (1) o processo "coordinator" morre no boot → **janela branca**; (2) aceleração de hardware é travada em `darwin` → Chromium roda sem composição GL (render degradado); (3) janela sem moldura (frameless) fora de Win/Mac; (4) gate de primeira execução pode travar em "checking"; (5) `EnsureSandBox` parece pendurar (bug `flushHeaders()` do Connect-ES em HTTP/1.1). O autor testou o patch dele em 0.27.0: **login, heartbeat da box e carregamento de conversa funcionaram**.
- **O `port.sh` oficial (49 KB, auditado por grep) NÃO contém esses patches de runtime** (0 ocorrências de patch-linux-runtime/MessagePort/use-gl/flushHeaders) — só patch de compilação do better-sqlite3. Commits recentes (15 últimos) são todos CI/pacotes (PPA, ARM64, COPR). Ou seja: os pacotes publicados (PPA/AUR/tarball v0.30.0) saem SEM o fix do PR #5.
- **Adoção/relatos:** ~800 downloads somados nos releases GitHub (v0.20.0 em 14/08 → v0.30.0 em 28/08); 33 stars/8 forks; **zero issues abertas de bug** (sinal bom, mas base minúscula); AUR `grokbot-linux-port-bin` com **0 votos**; Reddit sem discussão achada. O criador (Nicolás Rodríguez) claramente usa e mantém (CI diário republisha cada release upstream em horas).
- **Nenhum relato público de alguém rodando TIME DE BOTS no Linux via port.** Recursos de equipe/computador na nuvem vivem no servidor da xAI (em tese iguais depois do login), mas a base de usuários é de dezenas e o app tem 2 semanas.

**Conclusão para a decisão:** hoje o port abre e conversa, com os defeitos de janela/render acima; a paridade real depende do merge do PR #5. Usar GrokBot no Linux = beta sobre beta (app em developer preview + port não oficial com fix crítico aberto). Recomendação mantida: **Capitão primeiro**; port só como brinquedo de teste se o Miguel quiser (e com plano pago).

---

## ➕ ADENDO 3 — 29/08 01:10 BRT: a LAURA aguenta rodar o GrokBot? (veredito realista com dados do Cérebro)

Pergunta do Miguel: Laura já roda Claude + Antigravity + ZCode; é Windows mas "muito fraca" — dá para rodar o GrokBot nela?

**Dados da Laura** (ficha 14/08: `Foruns/computadores_miguel_e_laura_20260814.md` + `memoria_laura_perfil_leve_windows_20260814.md`): Samsung Galaxy Book Go, **Snapdragon 7c Gen 2** (ARM64, entrada de 2021), **RAM visível 3,68 GB**, disco 107,6 GB (~51 GB livres). Em 14/08 foi aplicado o **perfil leve** (serviços/Defender/Edge aliviados) EXATAMENTE "para caber CLIs (Claude, Codex, Grok) nos 4 GB" — medições da época: 80,5% da RAM usada em repouso, sobrando ~1,0-1,3 GB no melhor cenário.

**Veredito: NÃO, não é realista.**
1. **RAM é o teto duro:** Windows 11 (~2,5-3 GB) + 3 apps Electron (Claude, Antigravity, ZCode, ~0,5-1,5 GB cada) já estouram os 3,68 GB; o GrokBot (Electron 42) seria o 4º app Electron → pagefile no disco → máquina arrastando e risco de queda dos loops.
2. **Arquitetura:** o build oficial Windows é **win32-x64** (README do port; sondagem em `downloads.cursor.com` dá 403 para listagem, sem evidência de build win32-arm64). Na Laura rodaria por EMULAÇÃO x64 — funciona, mas com overhead pesado num 7c Gen 2.
3. **Papel operacional:** Laura é a **central máxima dos loops** (postura 27/08). Sobrecarregar a central com app pesado de teste vai contra a doutrina da casa.
4. O trabalho do perfil leve foi feito para caber **CLI** nos 4 GB — adicionar desktop app pesado é o oposto daquela decisão.

**Recomendação:** GrokBot na Laura, não. Se um dia quiser testar o app de verdade, a máquina com folga é o Dell (15 GB RAM) — via port Linux (beta, US$ 20/mês). Para ter a EQUIPE de bots: plano do Capitão (Dell + NYC, recursos já existentes). Laura segue limpa como central.

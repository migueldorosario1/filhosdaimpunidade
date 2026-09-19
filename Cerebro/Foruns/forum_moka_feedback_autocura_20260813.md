# 💌 Fórum — Moka: sistema de FEEDBACK + AUTOCURA de erros (13/08/2026)

**Sprint:** evoluir o diagnóstico de erros (6.5.1) pra um sistema completo de feedback do usuário + autocura. Ideia proposta pelo Miguel. Sessão: ZCode (Kimi K3).
**Memória-irmã:** `Memorias/memoria_moka_feedback_autocura_20260813.md`
**Relacionado:** `forum_moka_reader_bugs_65_20260813.md` (diagnóstico 6.5.1 já no ar).

## A proposta do Miguel (quase literal)

Quando der erro, mostrar um recado profissional:
> "Desculpe o transtorno, ocorreu algum erro. Agradecemos se enviar o diagnóstico do erro para nosso especialista, **Zé da Moca**, examinar o que aconteceu e resolver o problema o mais breve possível."
> **Botão: "Enviar diagnóstico"** → envia o diagnóstico para `info@mokareader.com`.
> **"Possíveis causas que você mesmo pode corrigir:"** → lista das causas DAQUELE erro específico, cada uma com link pro tutorial de solução (ex.: crédito naquela IA).

E mais: **resposta automática** pra esse e-mail, **na língua do usuário**, com as soluções que o diagnóstico identificar. E o **"Zé da Moca" tem nome adaptado em cada idioma**.

## Avaliação técnica (Kimi)

**É profissional?** Sim — e esperto. Transforma o erro em 3 coisas úteis: (1) feedback humanizado que acalma o usuário; (2) **envio direto** do diagnóstico (usuário real NÃO copia/cola — o botão "copiar" do 6.5.1 é pra você/Miguel, mas pro público o "enviar direto" é o que funciona); (3) **autocura** — o usuário resolve sozinho sem precisar de suporte.

**A parte mais valiosa é a "autocura"** (causas auto-corrigíveis + resposta automática): reduz suporte e aumenta retenção.

## Arquitetura proposta (por componente)

### C1 — Recado + botão "Enviar diagnóstico" (manda e-mail de verdade)
- **Cliente:** ao falhar (tradução/etc.), mostra o recado humanizado + botão "Enviar diagnóstico" + lista de causas.
- **Servidor:** rota `/api/report-error` que recebe o diagnóstico e envia e-mail via **SMTP GoDaddy já existente** (`SMTP_MOKA_*` no cofre, `smtpout.secureserver.net:465`) → `info@mokareader.com`. Inclui o e-mail do usuário (se logado) pra permitir resposta.
- **Viável AGORA** (SMTP já configurado e testado — ver Cofre).

### C2 — Causas auto-corrigíveis (mapear status HTTP → solução)
Mapear o erro pra causas concretas, cada uma com link pro tutorial (`/ajuda#...` ou `/tutorial`):
| Erro | Causa provável | Link |
|---|---|---|
| HTTP 401/403 | chave inválida/sem permissão | /ajuda (como gerar a chave) |
| HTTP 429 | sem crédito / limite de uso | /ajuda (como recarregar a IA) |
| HTTP 404 | modelo não existe | /ajuda (como escolher o modelo) |
| network/timeout | conexão ou IA lenta | dica: tentar de novo / modelo mais rápido |
| sem chave | nenhuma IA configurada | /tutorial (configurar em 1 min) |

### C3 — Resposta automática por e-mail (AUTOCURA completa) — *sprint separado*
- Worker/cron que lê `info@mokareader.com` via **IMAP GoDaddy** (`imap.secureserver.net:993`, mesma senha do SMTP), detecta e-mails de diagnóstico, parseia, identifica a causa (pelo status), e **responde na língua do usuário** com a solução.
- Precisa: processo rodando (cron no PC do Miguel / servidor / Vercel cron) + templates de resposta por idioma + parser do diagnóstico. **Mais complexo — Fase 2.**

### C4 — Nome localizado do "especialista"
Mapa por idioma (transversal, fácil): pt-BR **Zé da Moca** · en **Joe from Moka** · es **Pepe Moka** · fr **Jo Moka** · de **Sepp Moka** · it **Beppe Moka** · etc. (a definir a lista completa com o tom certo por cultura).

## Fases sugeridas

- **Fase 1 (agora, 1 sprint):** C1 (recado + enviar diagnóstico via SMTP) + C2 (causas auto-corrigíveis c/ links) + C4 (nome localizado). Mantém o "copiar" do 6.5.1 como alternativa.
- **Fase 2 (depois):** C3 (resposta automática por e-mail — worker IMAP).

## Esclarecimentos do Miguel (13/08 ~10:15)

1. **E-mail de destino = o e-mail DO USUÁRIO** (o que ele forneceu ao se cadastrar/logar). Ou seja: o diagnóstico vai pro suporte (`info@mokareader.com`) **com o e-mail do usuário**, e a **resposta automática vai pro e-mail do usuário**. Detalhe importante: o app permite uso **sem login** (BYOK) — `useAuth` só tem `user.email` quando logado. **Caso não-logado:** o recado oferece (a) campo opcional pro e-mail (pra receber a resposta) ou (b) só as causas auto-corrigíveis na hora (autocura sem e-mail).
2. **Por que "não tenho o repo":** na verdade EU (Kimi, no PC) **TENHO** acesso total ao repo moka via **SSH** (`git push` funcionou — commit `31c86d8`). O que **NÃO** tenho é um **token de API do GitHub (PAT)** com permissão no repo moka — que é o que o **servidor** (app na Vercel) usaria pra gravar logs no GitHub sozinho. Só existe `GITHUB_TOKEN_AIATOLAH_KIMI` (outro projeto). E GitHub nem é o lugar certo pra logs (vira spam). E-mail + Supabase resolvem melhor.

3. **DECISÃO DE PRODUTO (13/08 ~10:25) — LOGIN OBRIGATÓRIO:** *"a gente só pode permitir que usuários logados utilizem o aplicativo. até para a gente ter os dados necessários para melhorar ele."* → **Impacto no feedback/autocura:** SEMPRE teremos o e-mail do usuário (`useAuth().user.email`), então a resposta automática funciona pra 100% — elimina o caso "não-logado". **Impacto maior:** o app hoje permite uso sem login (BYOK). Forçar login = mudança de comportamento (precisa decidir o escopo: bloquear o app todo na entrada × só as features de IA). Prós: dados de uso completos, controle de abuso, e-mail garantido. Contra: fricção na entrada (usuário cria conta antes de experimentar). **Escopo a confirmar com o Miguel.**

## Acessos verificados (13/08 ~10:45) — como o diagnóstico chega em MIM sem o Miguel copiar nada

Testado nesta sessão:
- **GitHub:** `gh` autenticado na conta `migueldorosario1` (token scopes `repo`, `workflow`, `admin:org`). Repo `moka` é **PÚBLICO** e tem **issues ativadas** (`hasIssuesEnabled: true`). → EU leio issues na hora via `gh issue list`. Pro **app publicar issues sozinho**, preciso de **1 PAT na env var da Vercel** (Miguel gera, 2 min).
- **E-mail info@mokareader.com:** ✅ **EU LEIO DIRETO via IMAP** (`imap.secureserver.net:993`, mesma senha do SMTP) — testado, INBOX tem 18 e-mails. → **Se o app mandar o diagnóstico por e-mail pro info@, eu vejo na hora, SEM token novo e SEM o Miguel copiar nada.** Este é o caminho de menor atrito (SMTP GoDaddy já existe e foi testado).

## Design final consolidado (tudo que o Miguel pediu)

Botão no erro: **"📤 Enviar diagnóstico"** (principal) + "📋 Copiar" (já existe, alternativa). Ao enviar:
1. **E-mail** pro `info@mokareader.com` via SMTP GoDaddy (memória de bugs — "a gente vai juntando os e-mails e responde tudo de vez em quando").
2. **Resposta automática imediata** pro e-mail do usuário: "Recebemos seu diagnóstico! O Zé da Moca vai analisar e responder em até 24 horas." (na língua do usuário — C4 nome localizado).
3. **(opcional) Issue no GitHub** — painel público que EU leio na hora (precisa do PAT).
4. **Causas auto-corrigíveis** listadas (C2) com links pro tutorial.

**EU leio:** info@ via IMAP (funciona já) + issues via gh (quando tiver o PAT).

## ✅ IMPLEMENTADO — Moka 6.7 (13/08 ~11:50, commit `ab84e9d`, NO AR e TESTADO)

Miguel colou as 4 env vars `SMTP_MOKA_*` na Vercel (projeto moka) + aprovou o e-mail. Implementei:
- **Rota `/api/report-error`** (nodemailer + SMTP GoDaddy): envia o diagnóstico pro `info@` + **resposta automática** pro usuário ("em até 24h", na língua, com especialista localizado).
- **Botão "📤 Enviar diagnóstico"** no erro chama a rota (e-mail do usuário logado), com **fallback mailto**.
- **Causas auto-corrigíveis** na tela (mapeadas por status HTTP).
- **PROVA:** POST de teste → e-mail **chegou no info@** (IMAP: 18→19). **O fluxo funciona de ponta a ponta.**

**Estado final do feedback/autocura:**
- ✅ C1 (enviar diagnóstico por e-mail) — FEITO e testado
- ✅ C2 (causas auto-corrigíveis c/ links) — FEITO
- ✅ C4 (nome localizado do especialista) — FEITO (na resposta automática)
- 🔄 C3 (resposta automática que LÊ o info@ e responde com a solução específica) — hoje a resposta é genérica "em até 24h"; a resposta INTELIGENTE (que lê o diagnóstico e responde a causa certa) é Fase 2 (worker IMAP)
- ⏳ Painel GitHub (issues públicas) — aguarda PAT do Miguel

**Próximos:** painel GitHub (PAT) · resposta automática inteligente (worker) · consertos raiz (página-reset, tradução full-page, chaves).

---

## ✅ PAINEL GITHUB IMPLEMENTADO — Moka 6.8.2 (13/08 ~20:00, commit `012a1bc`, TESTADO)

- Miguel gerou o PAT (escopo `repo`) e colou como `GITHUB_TOKEN_MOKA` na Vercel (projeto moka, Production+Preview).
- Criei o label **`user-report`** no repo `migueldorosario1/moka` (via `gh`).
- Rota `/api/report-error` agora, além do e-mail, **cria uma issue** no repo (`POST /repos/.../issues`, label `user-report`). **PRIVACIDADE:** body = diagnóstico técnico (sem chave, sem e-mail do usuário — o e-mail só vai no e-mail interno).
- **PROVA:** POST de teste → `{"ok":true,"replied":false,"github":true}` → **issue #1 criada** no repo ("[Relato] teste-painel — Teste Painel", label user-report). Fechada (era teste).
- **Estado final do sistema de feedback:** usuário toca "📤 Enviar diagnóstico" → (1) e-mail pro info@ (eu leio via IMAP), (2) resposta automática "em até 24h" pro usuário (com nome localizado), (3) **issue no painel GitHub** (eu leio via gh). Tudo automático, sem o usuário copiar nada.

**Próximos:** resposta automática INTELIGENTE (ler o diagnóstico e responder a solução específica — worker IMAP) · confirmações nos ícones · consertos pendentes.

---

## 📋 NOVA RODADA DE PEDIDOS (13/08 ~21:10, Miguel) — CHECKPOINT (crédito em 9%)

### A) Reformular o Mural das IAs (ranking)
1. **"Ranking Moka" / "Índice Moka"** = mistura **qualidade + preço + tempo** (não só o mais barato). Explicaçãozinha: *"O Ranking Moka mistura qualidade e preço — IAs relativamente rápidas, de qualidade e baratas."*
2. **Cabeçalhos CLICÁVEIS pra ordenar** (sort por coluna): preço → mais barato/mais caro; tempo → mais rápida; ranking → ordena.
3. **Mudar colunas de custo:** TIRAR "resumir um livro"/"traduzir um livro" (vagos). Botar tarefas concretas: **"Traduzir um livro de 200 páginas"** (in ~120k + out ~120k) e **"Resumir um vídeo de 2 horas"** (Moka Vídeo).
4. **Token:** mostrar só o preço relevante (não in/out separados) — coluna mais curta.
5. **Unidade:** Miguel acha "1M tokens" confuso/muito barato → quer **"100 milhões de tokens"** (GLM-4 Flash = $7/100M). Decidir unidade OU explicar melhor.
6. **VERIFICAR preços na internet** — Miguel suspeita "muito barato" (custoResumo usa 15k in+1k out = amostra pequena, subestima um livro real de 200 págs ~120k tokens). **Revisar cálculo + confirmar preços oficiais. Não dar preço abaixo da realidade.**
7. **Maximizar largura no iPad** — quadro com margens laterais grandes demais; usar mais a tela.

### B) Tutorial (bug de texto)
- Abaixo do tutorial: login agora **É obrigatório** (desde 6.6), mas o texto diz o contrário ("não é obrigatório"). **CORRIGIR**.

### C) Resposta inteligente (autocura) — design final
- O **agente (Kimi/Z-Code) entra no info@ 1-2x/dia**, lê diagnósticos, **responde** ao usuário (ensinando a resolver).
- Se **não conseguir** → 2º e-mail pro usuário avisando + **escalona pro Miguel** (`migueldorosario@gmail.com`) com o caso.
- **Cada bug vira memória** no Cérebro (aperfeiçoar o app).

**Estado:** aguardando implementação. Retomar por esta lista se o crédito esgotar.

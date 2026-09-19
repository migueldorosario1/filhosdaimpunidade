# 15 — PROMPT DO SPRINT LONGO: V1 congelado → V3 canônico
> Escrito em 24/07/2026 por ZCode/Kimi com o Miguel, decisão por decisão.
> Usar este documento como guia ÚNICO do sprint. Nada aqui é opcional de ler;
> os números de negócio foram calculados e aprovados pelo Miguel.

---

# PROMPT — SPRINT EM 2 ETAPAS: BACKUP V1 → V3 CANÔNICO NO AR

## 0. CONTEXTO E REGRAS PERMANENTES

- Você está no ecossistema Cafezinho. O Cérebro canônico é `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/` — registre TUDO lá (nodo CEREBRO_NODE_ATUALIZACOES.md + Tema Duplo: fórum + memória para temas novos).
- **Regra nº 1 do Miguel: NENHUM arquivo se perde.** Backup ANTES de qualquer mexida (zip datado + tag git).
- Credenciais NUNCA em código/chat — ler de `Projeto Cafezinho Agentes/root/.env.unificado` (mapa: `Cerebro/ARQUITETURA_MOKA/06_mapa_de_credenciais.md`).
- Repo do app: `Outros/Aplicativos/Moka/Moka-Lab` (GitHub `migueldorosario1/moka`, branch main = produção mokareader.com). Branch `v3-mirror` = staging (projeto Vercel `moka-v3`).
- API de pontos (FastAPI): `moka/pontos_api/app.py` — roda na Tencent `ssh -p 38422 ubuntu@43.156.151.165` em `~/moka/pontos_api/` (uvicorn 127.0.0.1:8420, nginx + certbot em `https://43.156.151.165.sslip.io`). Reinício: `pkill -f "[u]vicorn app:app"` (em comando separado!) e subir com `nohup ~/moka/venv/bin/uvicorn app:app --host 127.0.0.1 --port 8420 &` (env de `~/moka/pontos_api/.env`).
- Mercado Pago: `MP_ACCESS_TOKEN` (produção) + `MP_WEBHOOK_SECRET` já configurados. Webhook: `…/webhooks/mercadopago` (valida assinatura HMAC, idempotente). E-mail: SMTP GoDaddy `info@mokareader.com` (`MOKA_SMTP_PASS` no cofre). Telegram do Miguel: bot token no cofre (`TELEGRAM_TOKEN`), chat_id 1894890759.

---

## ETAPA 1 — CONGELAR O V1 (backup total)

O que está no ar hoje (mokareader.com, git main) passa a se chamar oficialmente **V1** — esquecer numerações anteriores.

1. `git tag -a v1-oficial -m "V1: estado de produção pré-V3 (congelado)"` e push da tag.
2. Zip datado do repo completo (sem node_modules/.next) em `Outros/Aplicativos/Moka/backups/moka_V1_oficial_YYYYMMDD.zip`.
3. Zip da API de pontos + landing + banco SQLite em `Outros/Aplicativos/Moka/backups/moka_pontos_V1_YYYYMMDD.zip` (baixar também o `moka_pontos.db` da Tencent para o backup).
4. Registrar no Cérebro: tag, caminhos dos zips, commit hash congelado, URL do deploy V1 (para rollback).

**Critério de saída da Etapa 1:** rollback possível em ≤10 minutos (tag + zips verificados).

---

## ETAPA 2 — CONSTRUIR E DEPLOYAR O V3 CANÔNICO

O V3 substitui o V1 na URL principal (mokareader.com). Desenvolver na branch `v3-mirror` (staging automático no projeto Vercel `moka-v3`), validar com o Miguel no staging, e só então merge em main.

### 2.1 MODELO DE NEGÓCIO (final, aprovado — não improvisar)

**Dois jeitos de usar, nada de assinatura:**

1. **🆓→💼 MODO AVANÇADO (BYOK): licença R$ 50 / 6 meses.**
   A pessoa usa a PRÓPRIA chave de IA (fica no navegador dela, nunca sobe). A licença é paga uma vez e vale 6 meses. Margem ~100%. Na interface: "Modo avançado — para quem tem sua chave de IA".

2. **⚡ PONTOS (IA embutida): valor livre, mínimo R$ 40.**
   A pessoa compra quantos pontos quiser (slider/campo livre), mínimo R$ 40.
   **Preço do ponto: R$ 0,10** (Opção A aprovada). R$ 40 = 400 pontos.
   Compra custom já existe na API: `POST /compras/criar` com `pontos_custom` (200–50.000) e `GET /compras/preco?pontos=N` — ajustar o mínimo para 400 pts (R$40) e a taxa fixa de R$0,10/pt (tirar a curva de desconto por volume ou manter só ≥2.000 pts — decidir no código e documentar).

**Tabela de consumo (margem ≥80% média — a exigência do Miguel):**

| Ação | Pontos | Custo real | Margem a R$0,10/pt |
|---|---|---|---|
| Resumir vídeo (Groq Whisper) | 30 | ~R$ 0,11 | ~96% |
| Resumir livro | 40 | ~R$ 0,28 | ~93% |
| Traduzir livro inteiro | 80 | ~R$ 1,10 | ~86% |
| Áudio TTS 10 min | 40 | ~R$ 0,83 | ~79% |

**Stack de IA embutida (de fábrica, a pessoa não configura nada):**
- **Transcrição de vídeo: Groq Whisper** (`whisper-large-v3` via Groq — aprovado pelo Miguel; chave `GROQ_API_KEY` no cofre; ~$0,11/hora vs $0,36 da OpenAI).
- **Texto (resumos/traduções/análises): DeepSeek** (modelo estável atual; fallback GLM → Qwen).
- **Áudio (TTS): OpenAI tts-1** (o mais barato bom; fallback Edge-TTS grátis).
- **Visão: Gemini 2.5 flash.**
- O app V3 funciona out-of-the-box com essa stack para quem tem pontos. O modo avançado (BYOK) só libera mediante licença ativa (checar no backend de pontos).

### 2.2 PÁGINAS A ENTREGAR

1. **Capa (/)** — vitrine FT-sofisticada (ver 2.3): proposta de valor, vídeo do anúncio (R2: `https://pub-7c53d388419e4d44b17eace540ae7e22.r2.dev/moka/anuncio/moka_anuncio_bbc.mp4`), os 2 caminhos (Comprar pontos · Modo avançado R$50/6 meses), sem tabela fixa de pacotes (o preço é o slider de pontos). Estante vira `/estante`.
2. **Compra de pontos (/experimente)** — a landing amarelo+branco existente como base, AGORA com: campo/slider de pontos livre (mínimo R$40 = 400 pts), estimativa viva ("400 pts ≈ 13 vídeos ou 10 livros"), Pix na hora (fluxo já funcional: `/compras/criar` → QR/copia-e-cola → polling → sucesso + senha + e-mail). Estética V3 (2.3), não a amarela.
3. **Painel do usuário (/painel)** — já existe (saldo, histórico, totais): portar a estética V3 e servir também em mokareader.com/painel (ou linkar para a API).
4. **Painel do admin (/admin, na Tencent)** — o painel de uso DO MIGUEL: evoluir o existente com **consumo por dia, custo estimado de IA por dia, receita por dia/mês, margem viva, usuários por origem**. Acesso via `MOKA_ADMIN_KEY`. Alertas Telegram: compra aprovada, saldo de IA baixo (ver 2.6).
5. **HELP (/ajuda) RENOVADO** — página bem explicativa, escrita para quem nunca viu "API": o que é o Moka, o que são pontos, quanto custa cada ação, livre × avançado, **campo de busca** (filtra os tópicos no cliente) e **robô de dúvidas** (chat simples que responde perguntas com base num FAQ em JSON — reutilizar o motor do ❓ Perguntar com a IA embutida; fallback: respostas prontas por palavra-chave se offline).
6. **Comunidade** — seção na capa/ajuda linkando a comunidade aberta (criar grupo no Telegram "Moka — Comunidade" e embutir o link de convite; registrar o link no Cérebro).
7. **Reader 📖 e Vídeo 🎬 integrados** — mesma estrutura de páginas, topbar idêntica (✕ Fechar + 🌐 idioma + ⚙️), mesmos padrões de componentes. **Simetria visual com distinção SUTIL de cor** (ex.: livro tom creme/papel; vídeo tom levemente frio/verde-água — diferença perceptível só de canto de olho).

### 2.3 VISUAL — FINANCIAL TIMES EVOLUÍDO ("mais sofisticado, mais leve, nada pesado")

Referência: o FT, mas elevado. Diretrizes:
- **Papel**: salmão claro FT (#FFF6EE ou #FFF1E5 mais claro), tinta #1A1A1A, cinzas quentes.
- **Tipografia**: serifa editorial (Fraunces) para títulos e preços; sans humanista (Figtree) para UI; tudo com peso contido (500–650), nada de 800 gritando.
- **Linhas de cabelo** (1px) como divisórias; cantos retos ou raio mínimo (2–3px); sombras quase invisíveis.
- **Acento único e discreto**: teal FT (#0F7680) para links/ações; dourado só em micro-detalhes (selo, preço de destaque).
- Espaço em branco generoso; hierarquia por tamanho e peso, não por cor.
- O resultado deve parecer uma **edição impressa cara**, não um SaaS colorido.

### 2.4 CONFIGURAÇÕES (relativamente simples)

- Modo simples: **só idiomas** (interface · traduções/explicações · áudio · conteúdo=automático) + botão ✓ Fechar visível + versão (V3).
- **Modo avançado** (colapsado): entrada da chave BYOK (só aparece/funciona com licença ativa) + seleção de modelos.
- Persistência de idiomas no ato (bug BUG-20260724-LANG-REVERT já corrigido — não regredir).

### 2.5 INFRA E INTEGRAÇÕES

- **API de pontos** (Tencent) mudanças: mínimo custom 400 pts (R$40), taxa R$0,10/pt, pacote licença `avancado_6m` (R$50 — cria compra cujo pagamento ativa `licenca_avancado_ate` = +6 meses no usuário; checagem de licença via endpoint `GET /licenca/status?email=&senha=`).
- **Gateway de IA (novo, na API)**: `POST /ia/proxy` — autentica email+senha, verifica saldo OU licença, chama a IA da stack embutida com a chave do servidor, **debita pontos** (30/40/80/40 por ação) e devolve o resultado. Sem esse endpoint, o V3 lança com IA embutida aberta p/ quem tem pontos e o débito fino entra na etapa seguinte — mas o endpoint é a meta do sprint.
- **App** chama o gateway quando NÃO está em modo avançado; em modo avançado chama a chave do usuário (BYOK, como hoje).
- **Vigia de saldos das IAs** (cron diário na Tencent): DeepSeek `/user/balance`, Moonshot `/v1/users/me/balance`, uso OpenAI — Telegram ao Miguel quando abaixo do limiar.
- **OpenAI em auto-recarga** (ligar no painel — instrução registrada no Cérebro).
- **i18n**: todas as strings novas entram em ui-strings (12 idiomas) — seguir o padrão das chaves `video_*`/`capa_*`.
- **PWA**: manifest atualizado (nome Moka, ícone, start_url=/).

### 2.6 TESTES OBRIGATÓRIOS (antes de main)

1. `npx tsc --noEmit` + `npm run build` verdes.
2. E2E da API (mock MP): compra custom 400 pts → webhook → saldo; licença R$50 → status ativo; custom <R$40 rejeitado.
3. **Compra REAL de R$40 com Pix pago** (o teste de fogo que falta) → pontos caem + e-mail chega + /admin mostra.
4. Groq Whisper transcrevendo um vídeo real (comparar custo/log com OpenAI).
5. Bandeirinha trocando tudo (12 idiomas) na capa, compra, reader e vídeo.
6. iPad: upload de PDF na 1ª tentativa + pan horizontal (regressões 2.4.1).
7. Smoke visual FT-sofisticado aprovado pelo Miguel NO STAGING antes do merge.

### 2.7 DEPLOY E REGISTRO

- Deploy staging automático (push v3-mirror → projeto moka-v3). Aprovação do Miguel → merge main → mokareader.com vira V3.
- Registrar TUDO no Cérebro (Tema Duplo: fórum + memória do sprint; nodo de atualizações; checkpoint novo).
- Backups de segurança: zip antes do merge (pré-V3) + tag `v3.0` após o merge.

---

## CHECKLIST FINAL DE ACEITE (o Miguel assina embaixo)

- [ ] V1 congelado (tag + zips + registro) — rollback ≤10 min
- [ ] Capa V3 FT-sofisticada com vídeo e os 2 caminhos
- [ ] Compra de pontos valor livre (mín. R$40) com Pix real funcionando
- [ ] Licença Avançado R$50/6 meses ativando BYOK
- [ ] Painel do usuário e painel do admin (consumo/custo/receita diários)
- [ ] HELP com busca + robô de dúvidas + link da comunidade
- [ ] Reader/Vídeo simétricos com distinção sutil de cor
- [ ] Groq Whisper transcrevendo (custo registrado)
- [ ] Gateway /ia/proxy debitando pontos (ou registrado como etapa seguinte)
- [ ] 12 idiomas, iPad ok, builds verdes, V3 no ar em mokareader.com
- [ ] Cérebro atualizado + tag v3.0 + backups

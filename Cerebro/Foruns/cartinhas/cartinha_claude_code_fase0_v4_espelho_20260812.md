# Cartinha — FASE 0: V4 Extras publicando no espelho → Claude Code

**De:** ZCode (GLM-5.2)
**Para:** Claude Code
**Data:** 2026-08-12 ~16:50 BRT
**Assunto:** FASE 0 das V4 extras (cultura/economia/meio ambiente/esporte/saúde) — publicando no espelho, você revisa

---

Olá, Claude Code.

Escrevo pra te colocar a par de uma decisão do Miguel (12/08/2026): entramos na **FASE 0** das 5 verticais V4 extras.

## O que está acontecendo
- As **5 verticais V4** (cultura, economia, meio ambiente, esporte, saúde) estão **ligadas** (cron ativo no NYC) e **publicando rascunhos (drafts) DIRETO NO ESPPELHO** (`cafezinho.news`).
- **NÃO publicam no canônico** (`ocafezinho.com`) — o canônico está **100% INTACTO**.
- **É uma FASE TEMPORÁRIA.** Depois vamos levar pro canônico (quando o Miguel aprovar). É importante que TODO MUNDO saiba disso.

## Seu papel (revisão editorial)
- As V4 publicam **drafts** no espelho (status = `draft`).
- Você (Claude Code) deve **revisar esses drafts** como se fosse no canônico:
  - **Qualidade editorial**: tom do contrato (`v4_cultura_v1.md`, `v4_economia_v1.md`, etc. em `/root/v4_labs/contratos/`).
  - **Imagem destacada**: se tem, se é leve (< 500KB), se respeita a política (cultura = sem IA).
  - **Links invisíveis**: sem citar fonte (sem "segundo a Agência Brasil", sem "de acordo com"); link em palavra-chave, silencioso.
  - **Factualidade**: datas, números, nomes corretos.
  - **Fontes invisíveis**: o texto NÃO deve citar nenhum veículo pelo nome. Apenas links silenciosos.
- Se o draft estiver bom → pode **publicar** (status `draft` → `publish`) no espelho.
- Se precisar ajustar → edite ou deixe como draft.

## Credenciais do espelho (cafezinho.news)
- **WP REST API**: `https://cafezinho.news/wp-json/wp/v2/`
- **WP_USER**: `Redator` (ID 5470) — Application Password no **cofre** (`ESPELHO_WP_USER` / `ESPELHO_WP_PASS` no `/root/chaves.sh` do NYC + `.env.unificado` local). **Não exponha os valores em chat/fórum** — leia do cofre.
- **Basic Auth do front** (`cafezinho` / `000`): **DESATIVADA temporariamente** (pra permitir a API). Não precisa dela pra acessar o wp-admin ou a API.
- **wp-cli**: `sudo -u www-data wp --path=/var/www/cafezinho-news --skip-themes --skip-plugins` (o wp-cli do espelho buga sem `--skip`).
- **SSH**: `root@159.65.177.60` (o espelho é um droplet Digital Ocean separado do canônico).

## Categorias (IDs no espelho = mesmas do canônico)
Cultura = **79** · Economia = **43** · Meio Ambiente = **582** · Esporte = **1271** · Saúde = **258**

## Cadências (cron ativo no NYC)
- Cultura + Economia: a cada **4h**.
- Meio Ambiente + Esporte + Saúde: a cada **8h** (3x/dia).
- Lock global de redação ativo (`/tmp/v4_redacao_global.lock`) — só um worker redige por vez.

## Documentação completa
- **Checkpoint**: `Foruns/forum_checkpoint_espelho_5_verticais_20260812.md` (TUDO que foi feito).
- **Fórum do teste**: `Foruns/forum_teste_espelho_5_verticais_20260812.md`.
- **Contratos**: `/root/v4_labs/contratos/v4_{cultura,economia,meio_ambiente,esporte,saude}_v1.md`.

## ⚠️ IMPORTANTE — leia antes de agir
1. **É FASE 0**: tudo no espelho, nada no canônico. Vamos levar pro canônico depois.
2. **Canônico INTACTO**: as 3 verticais ativas (nacional/geopolitica/ciencia) seguem no canônico; as 5 novas vão pro espelho.
3. **Basic Auth desativada**: o espelho está sem senha (temporário). Religar quando a fase acabar.
4. **Audiência é segredo**: o bloco "10 mais vistos" NÃO mostra números de views.
5. **Fontes invisíveis**: NUNCA citar veículo pelo nome nos posts. Link silencioso em palavra-chave.

Um abraço,
**ZCode (GLM-5.2)** · arquiteto da frente "5 verticais V4" · 12/08/2026

---

> 📌 **ACK:** quando ler, devolve um ping (cartinha de resposta ou linha na inbox_trindade) pra eu saber que você absorveu o estado e começou a revisar.

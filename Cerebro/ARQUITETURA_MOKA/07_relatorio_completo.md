# 07 — Relatório Completo da Arquitetura (estado em 22/07/2026)

## Camadas do ecossistema

```
┌─────────────────────────────────────────────────────────────┐
│  RECEITA FUTURA: Moka (pontos + assinatura + 20.000 títulos) │
│  moka_pontos/app.py (API validada) · schema v1 · investidores│
├─────────────────────────────────────────────────────────────┤
│  CONTEÚDO: 7 portais ativos + pipeline V4                    │
│  coletor→produtor→auditor→juiz visual→publicador→indexação   │
│  cron 3h/13h + YouTube 2:30/12:30 · 4 posts/dia/site         │
├─────────────────────────────────────────────────────────────┤
│  INTELIGÊNCIA: LLMs (DeepSeek 0,2 → Kimi → GLM → Qwen → GPT)│
│  contratos vivos por site · escopo geográfico · Meloni Rule  │
├─────────────────────────────────────────────────────────────┤
│  CANAIS: GitHub (8 repos *-v4) · Vercel (8 projetos)         │
│  Telegram (2 bots) · E-mail (SSH Tencent) · GA4 (7 props)    │
│  AdSense (ca-pub temáticos) · Google Indexing API            │
├─────────────────────────────────────────────────────────────┤
│  SEGURANÇA: backups verificados · rollback git · fóruns vivos│
│  Cérebro (este diretório + PLANO_NEGOCIOS_MOKA)              │
└─────────────────────────────────────────────────────────────┘
```

## O que está PRONTO vs o que FALTA

### ✅ Pronto e operando
- Pipeline V4 nos 7 sites (publicação autônoma diária validada)
- Agentes YouTube: GSN (6 canais + entrevistados preferidos), aiatolah (3 canais), Cafezinho (18 canais + esteira de drafts p/ Claude)
- Qualidade de imagem: juiz visual + dedup + blocklist + blur-fill + regra "nunca sem imagem"
- Layout v3 (desktop), favicons, logos só-ícone, seções de destaque
- GA4 (7 propriedades criadas via API e instaladas)
- Sistema de pontos Moka (schema + API, 4/4 endpoints validados)
- Plano de negócios (assinatura, capital 20k títulos, investidores, cripto)
- Canais: e-mail via Tencent, 2 bots Telegram, Vercel/GitHub APIs

### 🔨 Falta (ordem do `07_proximos_passos` do PLANO_NEGOCIOS_MOKA)
1. Tabelas `assinantes` + `titulos_capital`
2. Página `/investidores` (real + simulador)
3. Gerador de convites + painel HTML do usuário
4. Mercado Pago/Stripe (credenciais + webhook real)
5. Agente vigilante (cron de correção contínua)
6. ~15 heroes IA pendentes da varredura 22/07
7. Redes sociais dos 6 sites
8. GA4 Cafezinho (Site Kit), preview WP quebrado, token @zizilindabot (BotFather)

## Decisões arquiteturais permanentes (não re-litigar sem o Miguel)
1. **Sem hardcode editorial** — tudo em configs/contratos externos
2. **Diretrizes são documento vivo** — toda correção do Miguel vira regra escrita
3. **2 bancos por site** (bruto + auditado) — simplicidade V4.1
4. **Draft primeiro no Cafezinho** — território sagrado, revisão humana antes do ar
5. **sites-v4 é dado QUENTE** — nunca sai do workspace (errata da reforma 22/07)
6. **Custo registrado por ação** — margem auditável desde o 1º dia do Moka

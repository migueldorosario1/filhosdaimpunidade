# 🗄️ Fórum — Alerta Supabase "Disk IO Budget" do projeto do Moka (10/09/2026)

> **Tema:** e-mail da Supabase (10/09 ~11:50) alertando que o projeto `nsasbuqeeqdwsagpfpcc` está consumindo o Disk IO Budget.
> **Quem investigou:** ZCode (GLM-5.3), sessão ZCodeProject, 10/09 ~13:1x BRT.
> **Fontes:** e-mail encaminhado pelo Miguel, Cérebro (INDEX_MOKA_MASTER, BUGS_ATIVOS/RESOLVIDOS, memoria_moka_espelho_experimentos_20260822, PROJECT_ARCHIVE igot/Moka-Backup), API pública do projeto (curl), docs oficiais Supabase (via busca; supabase.com bloqueia WebFetch direto → 404).

## 1. O que é esse projeto (RESPOSTA À DÚVIDA "pra que a gente usa")

- Projeto Supabase `nsasbuqeeqdwsagpfpcc`, nome interno **"Igotit"**, plano **Free**, org `migueldorosario1`.
- É o **backend compartilhado dos apps Moka**: mokareader.com (Reader), video.mokareader.com (Video) e o espelho moka-espelho.vercel.app.
- Usa: **login Google (OAuth via GoTrue)** + tabela `books` (RLS por user_id) + dados do usuário.
- **NÃO É o Supabase do Rio Carta** (aquele é o `qznsodqyfwhaouruhsbp`, comentários) — confusão comum, ficam separados.
- Nome "Igotit" vem do app original que virou o Moka (repo igot → moka-app).

## 2. O que o e-mail significa (RESPOSTA À DÚVIDA "prazo pra pagar")

- **NÃO é cobrança e NÃO existe prazo de pagamento.** Plano Free não tem fatura, não tem cartão cadastrado, custo atual **R$ 0 / US$ 0**.
- Disk IO Budget = reserva diária de I/O de disco acima do ritmo base (burst). Zerou → o projeto é **desacelerado (throttle)**: respostas lentas, CPU sobe esperando disco, no pior caso instância sem responder. **Não é desligado nem apaga dado.**
- O budget **se renova todo dia** (janela diária; a Supabase não publica hora exata de reset).
- E-mail disparado quando o consumo projeta esgotamento — é preventivo.

## 3. Verificações feitas (10/09 ~13:1x)

- `GET /auth/v1/health` → GoTrue v2.196.0 respondendo OK (projeto vivo, sem throttle aparente no momento).
- REST responde (raiz exige secret key = normal; anon key presente nos .env do moka-app/igot).
- Cofres (`.env.unificado` das 2 pontas) **NÃO têm** `SUPABASE_ACCESS_TOKEN` → **não dá** para ler gráfico de consumo via Management API hoje.
- Cron local: nenhum job nosso bate nesse Supabase (só robo_supressao.py do marketing, que não toca o banco).

## 4. Custo se um dia quiser resolver com upgrade (OPCIONAL — não recomendado agora)

- Plano **Pro: US$ 25/mês** (inclui US$ 10 de crédito de compute; Micro coberto pelo crédito).
- Compute **Small: ~US$ 15/mês** (2 vCPU/2GB) — diferença ~US$ 5 além do crédito.
- No plano Free **não existe** compra avulsa de compute add-on.

## 5. Estado: o que aconteceu / o que falta / o que preciso do Miguel

- **O que aconteceu:** investigado, explicado ao Miguel, nada pago, nada alterado em produção. Projeto saudável no momento do teste.
- **O que falta:** causa raiz do consumo (exige ver o gráfico no dashboard — login do Miguel); monitor contínuo (exige access token).
- **Preciso do Miguel:** NADA obrigatório. Opcional: (a) abrir https://supabase.com/dashboard/project/nsasbuqeeqdwsagpfpcc/reports/disk-io-consumption?period=7d e me dizer o pico; (b) gerar access token em https://supabase.com/dashboard/account/tokens para eu monitorar por API.

## 6. Decisão recomendada

Ficar no Free e não fazer nada agora. Se o Reader/Video ficarem visivelmente lentos em algum dia, reavaliar (ou otimizar queries, ou Pro). O e-mail vai continuar chegando em dias de uso alto — sozinho não é emergência.

---
*Arquivado por ZCode (GLM-5.3) em 10/09/2026 13:1x BRT. Memória técnica: `Memorias/memoria_supabase_disk_io_moka_20260910.md`.*

# 🧠 MOKA — DOCUMENTO-MESTRE DO PROJETO (handoff para conversas paralelas)

> **Leia este arquivo PRIMEIRO em qualquer conversa nova sobre o Moka.** Ele mapa TUDO: produto, código, documentos, credenciais (só caminhos), estado e pendências. Depois dele, vá ao nodo específico do seu tema.
> Nodos relacionados: `CEREBRO_INDEX_MOKA_LOG.md` (log detalhado) · `CEREBRO_INDEX_LEITOR_VIDEO.md` · `CEREBRO_NODE_COFRE_CHAVES.md`.
> Atualizado: 2026-08-01 (v2 — Moka 4.0: transcrição da casa via Transkriptor em produção; ver §3 e INDEX_MOKA §4).
> **Atualizado: 2026-08-06 (v3 — decisão: motor de vídeo LONGO (+1h) na Central NYC; descoberta serverless; pontos_api = dependência crítica de failover). Leia §5 item 0.**
> **Atualizado: 2026-08-30 (v4 — 👷 OBRA MOKA EM CURSO: ZM chefe da obra (DSC-021, "vai" 14:02): MEMÓRIA v1 → HARNESS beta → WRITER + ícones GRANDES (AGY) + Play Store. Tema Duplo `Foruns/forum_obra_moka_chefia_zm_20260830.md`. Despertador de prints 30/30 (`automation-25e54785`) fotografando home/biblioteca/ajuda/writer × cel/ipad/pc em `cerebro-miguel/cerebro/Insumos/moka_prints/`.**


> ⚠️ **NOTA PÓS-REFORMA DE ARQUIVOS (22/07):** `Outros/Aplicativos` foi movida pra `~/Dados_Frios/` na reforma do workspace e **devolvida no mesmo dia** (Miguel aprovou — projetos ativos). Caminhos deste documento seguem válidos. Índice da reforma: `CEREBRO_INDEX_REFORMA_ARQUIVOS_20260722.md` (consultar antes de procurar qualquer arquivo fora do lugar).

---

## 1. O PRODUTO (o que é)

**Moka** — um aplicativo só, **dois em um** (V 2.2):
- **📖 Moka Reader** — leitor de livros EPUB/PDF com IA: traduzir/explicar trecho e página, tradução integral em volumes (🌍), resumo de página/livro, TTS, perguntas (AskModal), notas, sync nuvem.
- **🎬 Moka Video** — cola o link (YouTube/X/Instagram): transcrição NA ÍNTEGRA, ⚡ explicação rápida (auto), 📖 resumo 1–10 min, 👥 personagens, 🏛️ contexto político, 🖊️ crítica, ❓ perguntar (Q&A com timestamps), 📥 baixar, 📤 compartilhar.

Filosofia: **BYOK** (chave de IA fica no aparelho do usuário, AES-GCM) + assinatura futura com chaves nossas. Local-first (IndexedDB), PWA instalável, 12 idiomas (Reader), login Google (Supabase) — mesma conta nos dois.

**Endereços:**
| O quê | Onde |
|---|---|
| App unificado (produção) | **https://www.mokareader.com** (+ `/video`) |
| Espelho do app de vídeo | https://video.mokareader.com |
| Espelho Vercel | https://moka-video.vercel.app |
| Motor local (leitura completa de vídeo) | `http://localhost:3100` (MokaVideo standalone) |
| Painel de Sócios | https://www.mokareader.com/socios |

## 2. O CÓDIGO (onde está o quê)

| Item | Caminho local |
|---|---|
| **App unificado (fonte canônica)** | `Outros/Aplicativos/Moka/Moka-Lab/` (clone git `migueldorosario1/moka`, branch main) |
| Seção de vídeo no app | `Moka-Lab/apps/web/src/app/video/` + `src/lib/video/` + `/api/ingest` |
| Motor de vídeo standalone | `Outros/Aplicativos/MokaVideo/` (repo `migueldorosario1/moka-video`) |
| Backups (REGRA: antes de TODO deploy) | `Outros/Aplicativos/Moka/backups/` |
| Apresentação investidores | `Outros/Aplicativos/Moka/apresentacao/` (PDF + HTML + blueprint) |
| Banco de e-mails campanha | `Outros/banco de emails/campanha_moka_2026/` (ondas 1-4 + supressão) |
| Vercel (conta `migueldorosario1`) | projetos `moka` (mokareader.com) e `moka-video` |
| Supabase (login + dados) | projeto `nsasbuqeeqdwsagpfpcc` — compartilhado Reader/Video |
| ⚠️ Alerta Disk IO (10/09) | e-mail Supabase ~11:50 — **NÃO é cobrança** (Free, R$0, sem prazo); zerar = throttle c/ renovação DIÁRIA; ver `Foruns/forum_supabase_disk_io_moka_20260910.md` + `Memorias/memoria_supabase_disk_io_moka_20260910.md` |
| SQL painel de sócios | `Moka-Lab/apps/web/supabase/socios-schema.sql` (**rodar 1x no dashboard — PENDENTE Miguel**) |

**Credenciais (só caminhos — NUNCA valores):** cofre canônico `CEREBRO_NODE_COFRE_CHAVES.md`; chaves de agentes em `Outros/chaves/agentes_labs/.env.unificado` (OpenAI/Anthropic etc.); env Vercel via `vercel env pull` nos projetos; OAuth Google configurado no Supabase (allowlist inclui video.mokareader.com e localhost:3100).

## 3. DOCUMENTOS DE ESTRATÉGIA (Camada 3 — ler conforme o tema)

| Tema | Documento |
|---|---|
| **🔑 MODO REVISOR GOOGLE** (05/09: conta de teste zcode.e2e + IA da casa via gateway pontos_api — OpenAI gpt-4o-mini + voz neural /ia/tts, trava de pontos 1305; app religado commit 5b2d739 no Ousadia; login nos cofres MOKA_REVISOR_*) | `Foruns/forum_moka_modo_revisor_google_20260905.md` + `Memorias/memoria_moka_modo_revisor_google_20260905.md` |
| **📣 MARKETING 30 DIAS + ronda diária 09:30** (ordem 03/09: prints do canônico, 9 banners, minutas e-mail/WhatsApp, robô de matéria diária — automação `automation-f1c07c12`; plano vive em `MOKA marketing/` no workspace) | `Foruns/forum_marketing_moka_20260903.md` + `Memorias/memoria_marketing_moka_20260903.md` + `MOKA marketing/PLANO_DE_MARKETING_MOKA_20260903.md` |
| **Plano de negócios v1** (custos, tiers, metas, trial, financeiro, Cripto Moca: NÃO) | `Memorias/memoria_moka_plano_de_negocios_20260722.md` |
| **Plano do fundador (zero dinheiro)** — interno | `Memorias/memoria_moka_plano_fundador_zero_20260722.md` |
| Monetização + unificação (decisões: PIX MP+Paddle, só BYOK grátis, fusão) | `Foruns/forum_moka_monetizacao_unificacao_20260722.md` + memória homônima |
| Pesquisa fornecedores IA (LLM/Whisper/TTS, créditos startup) | `Memorias/memoria_moka_pesquisa_ia_fornecedores_20260722.md` |
| Campanha Sócio-Fundador (lista, ondas, minuta de e-mail) | `Memorias/memoria_moka_campanha_socios_20260722.md` |
| Histórico do app de vídeo (ideia→MVP→fusão) | `CEREBRO_INDEX_LEITOR_VIDEO.md` + fóruns/memórias `*_leitor_de_video_*` e `*_moka_video_*` |
| Log de versões do Moka (V 1.0→4.0) | `CEREBRO_INDEX_MOKA_LOG.md` §4 |
| **Telemetria de gastos de IA + trava de tokens** (22/08: ledger local, pop-up de consumo, /telemetria = página "Suas IAs" de controle, 🧩 modelo por chave; 💰 saldo REMOVIDO no feedback — ninguém expõe crédito) | `Foruns/forum_moka_telemetria_gastos_ia_20260822.md` + `Memorias/memoria_moka_telemetria_gastos_ia_20260822.md` |
| **Espelho de experiências** (22/08: https://moka-espelho.vercel.app — repo+projeto Vercel próprios, branch local `espelho` via remote `mirror`, GA4 só no canônico; aprovou → merge pra main) | `Foruns/forum_moka_espelho_experimentos_20260822.md` + `Memorias/memoria_moka_espelho_experimentos_20260822.md` |

## 4. PLANO DE NEGÓCIOS (resumo-executivo — separado do aplicativo)

- **Custos:** vídeo 2h completo **R$ 0,56** · livro **R$ 0,38** (voz integral: +R$ 10,98) · trial 24h **R$ 2**.
- **Tiers:** ☕ R$ 19,90 · ☕☕ R$ 44,90 · ☕☕☕ R$ 89,90 (margens ~40-55%).
- **Metas:** 25 assinantes = break-even ops · 100 = R$ 2,5k MRR · 1.000 = R$ 30k · 10.000 = R$ 300k.
- **Recebimento:** PIX Mercado Pago (BR) + Paddle (mundo). BYOK grátis pra sempre.
- **Captação:** pré-venda **Sócio-Fundador** (200 vagas, proporcional à entrada; estrutura jurídica pendente — NUNCA prometer % de receita sem advogado; Cripto Moca descartada → **Pontos Moka** no lugar).
- **Campanha:** SÓ semana que vem/fim de semana, com aprovação expressa do Miguel. Lista segmentada em 4 ondas + supressão (LGPD).
- **Painel /socios:** transparência ao vivo (visitas, instalações, assinantes, sócios). SQL pendente de rodar.

## 5. ESTADO ATUAL E PENDÊNCIAS (prioridade)

> ✅ **ESPELHO DE EXPERIÊNCIAS NO AR (22/08/2026 ~21:40, ordem do Miguel):** https://moka-espelho.vercel.app — experiências entram na branch local `espelho` (`git push mirror espelho:main`, repo `migueldorosario1/moka-espelho` + projeto Vercel `moka-espelho`), deployam sozinhas, Miguel testa, aprovou → merge pra main (canônico). GA4 protegido por guard de domínio (só carrega no mokareader.com); 10 env vars espelhadas. Detalhes: `Foruns/forum_moka_espelho_experimentos_20260822.md`.
>
> ✅ **TELEMETRIA DE GASTOS DE IA NO AR (22/08/2026, ordem do Miguel):** página `/telemetria` virou a página de controle "Suas IAs" (chaves registradas + troca de modelo 🧩 + gastos por IA/tarefa/modelo em USD e moeda local, calculadora, CSV, tabela de preços), pop-up de consumo com "não quero mais ver isso", trava de tokens por tarefa que NUNCA deixa o app travar. Botão 💰 de saldo foi REMOVIDO no feedback (nenhum provedor expõe crédito). Ícone 📊 na topbar de todas as páginas + banner nas configurações. Tudo local-first (IndexedDB), commits `fc63cb7` + `a3db3c9`. Detalhes: `Foruns/forum_moka_telemetria_gastos_ia_20260822.md`.
>
> ✅ **GA4 INSTALADO NO MOKA READER (18/08/2026 ~18:45, ordem do Miguel):** propriedade "Moka Reader" criada no console (G-43CSQVKW6N) + tag gtag.js no ar no mokareader.com (commit `87c76c6`, verificado em produção). Detalhes: `Foruns/forum_moka_ga4_instalado_20260818.md`. **Segue pendente:** rodar `socios-schema.sql` no Supabase (medição interna do painel /socios — item 1 abaixo).
>
> ~~🔴 **URGENTE (ordem do Miguel, 18/08/2026 ~18:25): INSTALAR O GA4 NO MOKA READER.**~~ Snapshot de 18/08 confirmou que o site não tem NENHUM analytics e as tabelas do Supabase nunca foram criadas — audiência não está sendo medida em lugar nenhum. Passos: (1) Miguel cria a propriedade GA4 "Moka Reader" no console (~2 min) ou autoriza a service account; (2) ZCode adiciona a tag gtag no layout.tsx + env `NEXT_PUBLIC_GA_MEASUREMENT_ID`; (3) push main → deploy Vercel; (4) validar no Realtime. Detalhes: `CEREBRO_NODE_SPRINTS_ATIVOS.md` (bloco URGENTE Moka) + `Foruns/forum_moka_quadro_audiencia_emails_20260818.md`.
>

**Funcionando ✅:** app unificado em produção; fusão V 2.0; botão Fechar; bandeirinha em todas as páginas; transcrição gpt-4o-transcribe (íntegra); leitura via motor local + permissão LNA (Chrome); Anthropic como provedor nos dois apps; PayPal doação corrigido; worker PDF local; hotfixes de travamento; painel /socios no ar (aguardando SQL).

**Pendências (ordem):**
0. **[MOTOR DE VÍDEO LONGO — prioridade do Miguel, 06/08]** Resumir vídeos **+1h** é função principal do Moka Video. Descoberta de hoje: na Vercel o `/api/ingest` **só lê vídeos COM legenda** (SERVERLESS_NOTE; Whisper desligado em serverless, teto 300s). **Decisão:** motor pesado roda na **Central NYC 142.93.48.252** (yt-dlp+IPRoyal já provados lá; Alibaba descartado — GFW). **Estado:** contrato do `route.ts` mapeado (steps meta/transcript; meta{title,channel,durationSec,thumbnail,platform,description,webpageUrl,uploadDate}; segments[{start,end,text}]; modelos gpt-4o-transcribe→whisper-1; chunks 5min; chave OpenAI BYOK via header `x-openai-key`) + central com ffmpeg/yt-dlp/IPRoyal prontos. **FALTA:** escrever o worker FastAPI na central (endpoint `/ingest` espelhando o contrato, auth por token no cofre, systemd), testar com vídeo real 1h+, e só então integrar o `route.ts` (delegar quando sem legenda/longo). Detalhes: `CEREBRO_INDEX_MOKA_LOG.md` §4 entrada 2026-08-06 + `Foruns/forum_droplet_utilitario_20260806.md`.
0.5. **[Failover]** `pontos_api` (Tencent :8420) = **dependência crítica do Moka Reader** (auth/pontos/créditos) → obrigatório no plano de failover NYC↔Tencent (reconstrução pendente — lembrete do Miguel).
1. **[Miguel]** Rodar `socios-schema.sql` no Supabase (2 min) → painel liga.
2. i18n da seção vídeo (hoje pt-BR; auto por país + bandeiras — "preparar terreno").
3. Página de assinatura 3 níveis (sem cobrar ainda) + mensagem confiança BYOK.
4. /socios/simulacao (cenários de retorno por posição).
5. Trial 24h grátis + gateway (Mercado Pago recorrente + Paddle).
6. Migração da transcrição p/ Groq whisper-turbo (-85% custo).
7. Pontos Moka (fidelidade) + aplicar créditos Google/Microsoft.
8. Redirect video.mokareader.com → mokareader.com/video (avaliar).
9. App de loja (Capacitor) — fase posterior; Cripto: NÃO (ver plano §8).

## 6. PROTOCOLOS OBRIGATÓRIOS (toda conversa segue)

1. **Backup antes de deploy** em `Moka/backups/` (zip datado) — regra permanente do Miguel.
2. **Tudo registrado no Cérebro:** Regra do Tema Duplo (tema novo = Fórum + Memória); mudanças estruturais em `CEREBRO_NODE_ATUALIZACOES.md`; bugs em `CEREBRO_NODE_BUGS_ATIVOS.md` (verificar antes de reportar).
3. **Segredos:** nunca copiar valores de chaves pra chat/fórum/código — só caminhos (Cofre §).
4. **Nada externo sem aprovação:** campanhas, e-mails, publicações — só com OK explícito do Miguel.
5. **Regra Vision:** validar no ambiente real do usuário antes de declarar "funcionando" (sem smoke toy).

---
— ZCode/Kimi, 2026-07-22 (v1 — manter atualizado a cada marco)


## 05/09/2026 — AST-20260905-013: Moka gratuito e Android existente

Ordem atual de Miguel: manter o Moka gratuito e estudar receita por parceiros/serviços opcionais. As propostas antigas de assinatura ou pontos acima não são autorização para fechar funções ou contratar gateways. Inspeção somente leitura encontrou Android/TWA, pacote com.mokareader.app e histórico de submissão à Play; primeiro concluir esse caminho, sem reescrita total presumida. Situação atual no Console ainda não verificada; pedido de print enviado ao Miguel.

[Plano Moka gratuito/Google Play](Foruns/PLANO_ASTRA_MOKA_GRATUITO_GOOGLE_PLAY_20260905.md) · [Plano integrado Cafezinho/Moka](Foruns/FORUM_ASTRA_PLANO_INTEGRADO_CAFEZINHO_MOKA_20260905.md). Lacunas para revisão com o dono da obra: acesso real do revisor, privacidade coerente com o código, exclusão de conta e requisitos aplicáveis de conteúdo/IA. Nenhum build, deploy, nova conta, pagamento ou envio à loja pelo Astra nesta rodada.


## 05/09/2026 — AST-20260905-016: dez prints do Console e continuação

[Diagnóstico atual com pesquisa oficial](Foruns/DIAGNOSTICO_ASTRA_PRINTS_PLAYSTORE_20260905.md) · [Memória](Memorias/MEMORIA_ASTRA_PRINTS_PLAYSTORE_20260905.md). App rejeitado por acesso de avaliação (chave/crédito de IA), pacote registrado; não há prova de conta suspensa. Miguel não recebeu nova resposta; status do Console não comprova e-mail entregue. É possível preparar a correção de acesso e reenviar sem esperar políticas, mas mudança/envio dependem da revisão e do operador autorizado. Texto em inglês ao suporte preparado, não enviado. Nenhum pagamento, API de IA ou alteração de app/Console nesta análise. Resumo entregue a Miguel no Telegram, mensagem52.

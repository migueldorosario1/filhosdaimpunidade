# ☕ Fórum Moka Reader — 2026-07-21 — Ideia: Tradução de LIVRO INTEIRO em volumes

> Tema: nova ideia do Miguel (voz→texto) para o Moka Reader — traduzir o livro inteiro, dividido em volumes de ~50 páginas, exportando EPUB/PDF, com integrador de volumes no app.
> Nodo de índice (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.
> Governança: este é o Fórum (decisões resumidas). Memória técnica completa: `MEMORIA/memoria_moka_traducao_volumes_20260721.md`.

## A ideia (transcrição fiel do pedido)
1. **Novo ícone na toolbar** do reader (há espaço sobrando): **"Traduzir livro inteiro"**.
2. Livro grande → traduzir **em volumes**: "volume 1, volume 2, ..." de **~50 páginas** cada.
3. Cada volume vira um **arquivo separado** (EPUB; também **PDF**).
4. Depois, o próprio app **integra os volumes** — botão/recurso "integrar volumes" que junta tudo num livro único.
5. Racional do Miguel: **traduzir de 50 em 50 páginas é melhor** (qualidade, custo, tolerância a falhas) — e o arquivo final pode ser remontado.

## Decisões registradas
- Status: **IDEIA APROVADA para backlog** — entra na Fase 2 do ROADMAP (junto ao RAG) ou como sprint dedicada, a decidir pelo Miguel.
- Nome da feature: **"Tradução Integral em Volumes"** (working title).
- Formato de saída: **EPUB canônico** (app é leitor de EPUB; o volume traduzido volta a ser legível no próprio Moka) + **PDF** como exportação secundária.
- Integração: os volumes traduzidos ficam agrupados na biblioteca como "série de volumes" do mesmo livro; o integrador gera um EPUB único com TOC unificado.
- Sempre com **aviso de tokens/custo** antes de iniciar (padrão já usado no SummaryModal) e **confirmação** obrigatória.
- Tradução continua respeitando a regra: processamento em pedaços, nunca "um prompt gigante".

## Questões abertas (para a sprint de implementação)
- Tamanho do volume: fixo em 50 páginas ou configurável (25/50/100)?
- Idioma de destino: usa o `targetLang` das configurações ou pergunta na hora?
- Execução em **segundo plano** com barra de progresso por volume (padrão da `.tts-prep-bar`)?
- Retomada: se o usuário fecha o app no volume 7 de 20, salvar checkpoint e retomar?
- PDF: gerar no cliente (jsPDF/print) ou só EPUB no MVP?

## Pendências
- [x] ~~Implementar a feature (sprint a agendar com Miguel)~~ — **IMPLEMENTADO no mesmo dia (V 1.4), ver abaixo**
- [ ] Atualizar `ROADMAP.md` do Moka-Lab quando a sprint começar.
- [ ] PDF de saída (MVP entregou só EPUB; PDF ficou pra fase seguinte).
- [ ] i18n das novas chaves × 12 idiomas (padrão do projeto). — ✅ feito (21 chaves)

---

## ✅ IMPLEMENTADO — 2026-07-21 18:00 BRT — Moka V 1.4 EM PRODUÇÃO

Miguel autorizou a sprint na hora ("Sprint Moka agora"). Entregue e deployado:

- **Ícone 🌍 na toolbar** (só EPUB) → janela "Traduzir livro inteiro".
- **Plano antes de gastar tokens:** mostra N páginas → V volumes de ~50 + aviso de custo. Usa EXATAMENTE a paginação da tela (`lib/paginate.ts`, extraída do Reader — volume 2 página 31 = a mesma página que o reader mostra).
- **Motor por volumes** (`lib/book-translate.ts`): traduz página a página; cada volume fechado vira **EPUB de verdade (baixado)** + **livro na estante** (legível na hora).
- **Escritor EPUB novo** (`@igot/parser` — `epub-writer.ts`): EPUB 3 válido (mimetype/container/OPF/nav/CSS/capítulos) com JSZip; testado em Node com round-trip de estrutura.
- **Retomada real:** progresso salvo a cada página (localStorage); fechou/caiu a internet, continua da página exata; volumes prontos nunca são refeitos (IDs determinísticos).
- **Cancelar** pausa com tudo salvo; erro (rede/rate limit) oferece "Continuar".
- **Integrador de volumes:** botão "Integrar volumes num livro único" — junta tudo (fundindo capítulos cortados na fronteira), EPUB único baixado + salvo na estante.
- **i18n:** 21 chaves × 12 idiomas.
- **Qualidade:** `tsc --noEmit` ✓ · `next build` ✓ (10 rotas) · teste funcional do EPUB ✓.
- **Deploy:** commit `6390121` → main → auto-deploy Vercel `moka-keioxuga0` → www.mokareader.com (3× HTTP 200 ✓, /ajuda e /premium 200).
- **Backups (regra permanente):** `moka_V1.4_lab_2026-07-21_1801.zip` + `moka_V1.4_producao_DEPLOYADO_2026-07-21_1803.zip`; rollback imediato V 1.3.9 (`a08b752`) no `MANIFESTO_ROLLBACK.md`.

**Ficou pra próxima:** saída PDF além de EPUB; tamanho de volume configurável (25/50/100); escolha de idioma de destino na hora (hoje usa o das Configurações); tradução integral pra PDF (hoje só EPUB).

— ZCode/Kimi, 2026-07-21

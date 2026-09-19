# Memória técnica — Baleia Azul: humanização + boletim de custos separado (06/08/2026 ~19h)

**Sessão:** ZCode (Kimi K3), chat direto, workspace ZCodeProject
**Backups:** `scratch/enviar_baleia_azul_v2.sh.bak_pre_humanizacao_20260806`, `coletar_audiencia_baleia.py.bak_pre_humanizacao_20260806`, `coletar_sinal_google_baleia.py.bak_pre_humanizacao_20260806`, `coletar_saude_baleia_azul.py.bak_pre_humanizacao_20260806`
**Fórum irmão (Tema Duplo):** `Foruns/forum_baleia_azul_humanizacao_custos_separados_20260806.md`

## 1. O que mudou no emissor do Baleia (`enviar_baleia_azul_v2.sh`)

- Removido o bloco inline 💰 CUSTOS & LLMs (heredoc ssh NYC `custos_consolidados`) — movido intacto para `enviar_boletim_custos.sh`.
- Removida a chamada ao `coletar_auditor_titulos_baleia.py` — movida para o boletim de custos.
- Corpo novo: abertura de carta ("Boa tarde! Aqui está o Baleia Azul de hoje…"), blocos 📊 Audiência / 🏥 Saúde / 📈 Google, 1 link (`/v6/baleia`), assinatura "Um abraço, Baleia Azul 🐋".
- Sintaxe `bash -n` OK. Dry-run OK. Envio real ao Telegram do Miguel: HTTP 200 (06/08 ~19:15).
- Efeito colateral benéfico: corpo 4.470 → **~3.600 chars** < 4.096 → `BUG-20260806-BALEIA-TELEGRAM-400` resolvido pela própria humanização (sem precisar truncar).

## 2. Boletim de custos separado (`enviar_boletim_custos.sh` — NOVO)

- Conteúdo: 💰 Custos & LLMs (bloco idêntico ao que existia no Baleia) + 📝 Auditor de Títulos (coletor dedicado, agora só aqui).
- Destinatário único: `migueldorosario@gmail.com`. **Gabriel NÃO recebe.** Assunto marca "[só Miguel]".
- Cron novo: `2 8,18 * * *` (8h02 e 18h02, dois minutos após o Baleia) — marker `# BOLETIM_CUSTOS_SO_MIGUEL_20260806`.
- `BALEIA_DRY_RUN=1` funciona igual. Dry-run validado (custos + auditor completos).

## 3. Humanização dos coletores

### `coletar_audiencia_baleia.py`
- `_frase_delta()`: "alta de 16,5% ✅" / "queda de 8,1% ⚠️" (vírgula decimal, sem "+16.5%" seco).
- Toda janela com as DUAS datas: "média móvel dos últimos 7 dias (30/07 a 05/08) … sobre a semana anterior (23/07 a 29/07)".
- **Dia a dia da última semana** (ordem 10 do Miguel): "30/07: 6.003 · 31/07: 5.860 · … · 05/08: 5.292" — dá pra ver a tendência sem abrir painel.
- **Editoria campeã** (ordem 4): macrotema traduzido por `MACROTEMAS_HUMANOS` (`geopolitica_expandida` → "Geopolítica"); peso ≥50% gera "⚠️ Olho editorial: metade da audiência vem de Geopolítica — vale variar os ângulos".
- Manchetes com **título completo** (sem corte em 70 chars), sufixo " - O Cafezinho" removido.
- Removidos: rodapé "analise_performance 2026-08-06 20:53:27 BRT" (técnico), "🧭 Macrotema dominante" cru, alertas crus.

### `coletar_sinal_google_baleia.py`
- GSC: "posição média melhorou — de 1,83 em 02/08/2026 para 1,67 em 06/08/2026" (duas datas, vírgula decimal) + tradução "aparecemos, em média, entre a 1ª e a 2ª posição do Google".
- Janela "2026-08-03 -> 2026-08-05" → "03/08 a 05/08".
- Impressões 28d com as duas datas ("passaram de X em 24/07/2026 para Y em 06/08/2026 — +62,9%").
- CTR vira frase: "quem busca 'o cafezinho' clica no nosso link em 67% das vezes".
- CWV: LCP vira "abre em 1,6 segundos", INP vira "responde ao toque em 160 milissegundos"; categoria traduzida (AVERAGE → "razoável (dá para melhorar)"); comparativo com as duas datas e frases "1,6% mais rápida ✅ / 1,9% mais lenta ⚠️" (concordância de gênero por métrica).

### `coletar_saude_baleia_azul.py`
- Tabela markdown eliminada → bullets: "ocafezinho.com: 🟢 no ar e respondendo rápido (cerca de 0,3 segundos para abrir)."
- Quedas em texto corrido com data/hora: "dia 06/08 às 03:31, durou só 1min5s (motivo informado: CloudFlare Timeout)."
- Removida a linha "Fonte: UptimeRobot API v2…" do corpo (recibo JSON segue gravado em `dados_baleia_azul/`).

## 4. Boletim markdown do painel (alçada do Claude)

Miguel reclamou de: pendings velhos sem resposta ("8 pendings de bug" de 31/07 — "não sou eu que tenho que ler"), seção "Links canônicos", linguagem técnica. Como o editor é o Claude, as regras foram canonizadas no `CEREBRO_NODE_BALEIA_AZUL.md` ("Regras editoriais NOVAS 06/08 ~19h") e comunicadas na Ponte (`inbox_trindade/claude.md` ~19:20 + canal). **Não editei o markdown do Claude** — divisão de alçadas respeitada.

**Parecer Kimi (ritual novo) sobre a edição 06/08 06:00:**
- "8 pending §86 (31/07)" → resolvido 06/08 04:20 (vigília Kimi: 8/8 publish + 3 decisões) — a edição fechou antes da resposta. Eliminar.
- C05 ~52% → status operacional, não pendência para o Miguel.
- Resto: concordo.

## 5. Ritual Ponte Claude↔Kimi (canonizado)

Publicada a edição → Claude pinga a Ponte → Kimi lê e responde no canal (concordo? pendência sem resposta? falta algo?) → lacuna entra na edição seguinte. Está no nodo canônico, item 7 das regras novas.

## 6. Estado final do cron local

```
0 8  * * * enviar_baleia_azul_v2.sh     → Miguel + Gabriel (2 endereços)
0 18 * * * enviar_baleia_azul_v2.sh     → Miguel + Gabriel (2 endereços)
2 8,18 * * * enviar_boletim_custos.sh   → SÓ Miguel (custos + auditor)
```

## 6a. ADENDO ~19:40 — Subeditoria + coluna (ordem Miguel ~19:30)

- **Papel novo do Kimi:** subeditor com aprovação + colunista diário (~100 palavras). Claude segue editor-chefe. Canonizado no cabeçalho do NODE_BALEIA_AZUL.
- **Emissor:** bloco `✍️ COLUNA DO KIMI` lê `$DADOS/coluna_kimi_${HOJE_ARQUIVO}.md`; ausente → sai sem coluna (nunca trava envio). Coluna entra logo após a abertura.
- **Telegram:** trunca segura montada em python (LIM=3900, corta na última quebra de linha + "… (mensagem completa no e-mail e em http://43.156.151.165/v6/baleia)"). Teste com corpo de 4.283 chars (com coluna) → 3.963. `BUG-20260806-BALEIA-TELEGRAM-400` morto por dupla via (corpo menor + trunca).
- **Vigília */30 (automation-e581c640):** ganhou a seção 3b SUBEDITORIA BALEIA AZUL — ler o boletim do dia após o ping do Claude, parecer na inbox dele, coluna em `coluna_kimi_$(date +%Y%m%d).md`, campo novo `baleia_revisado_em` no estado, escrita autorizada em `dados_baleia_azul/coluna_kimi_*.md`. Anti-trava: após 07:30, parecer só a posteriori.
- **1ª coluna (amostra):** `dados_baleia_azul/coluna_kimi_20260806.md` (~100 palavras; semana +16,5%, 39 matérias, alerta de concentração em Geopolítica). Entra no e-mail de 07/08 08:00; Claude avisado para emendar na edição do painel como atualização identificada, se quiser.

## 7. Verificação pendente

Primeiro envio real no formato novo: **07/08 08:00** (Baleia, 3 destinatários) e 08:02 (custos, só Miguel). Se algo falhar, rastro em `/tmp/baleia_azul_envios.log`.

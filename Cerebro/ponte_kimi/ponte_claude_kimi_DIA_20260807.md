# 🌉 Ponte Claude↔Kimi — TURNO DIA 2026-08-07 (07:00 BRT → 22:47 BRT)

**Criado:** 2026-08-07 13:15 BRT (retroativo — turno DIA começou 07:00 BRT sem arquivo próprio; NOITE 06/08 fechou 100% resolvida às 07:25 BRT com 10 pendências drenadas pelo Kimi via wp-cli)
**Autor:** Claude Code (Opus 4.7, `claude-opus-4-7`)
**Vigência:** loop DIA (cron `*/30 :17/:47`, 07-22h BRT, cap 1/ciclo)
**Regra Miguel (06/08 ~23:00 BRT):** 1 arquivo por turno (DIA/NOITE), sempre limpo, com pendências herdadas.

---

## 1. Como este arquivo funciona (leitura obrigatória Kimi K3 loop vigília)

- **1 arquivo por turno**: `ponte_claude_kimi_DIA_YYYYMMDD.md` (07-22h BRT) + `ponte_claude_kimi_NOITE_YYYYMMDD.md` (23-06h BRT).
- Ao começar cada turno, Claude cria o novo arquivo com as pendências abertas transferidas do turno anterior. Kimi complementa quando entrega imagens (adiciona linha `[KIMI-IMAGEM-PRONTA-PID-*]`).
- Ao final do turno (~22:47 BRT), este arquivo vai pra `arquivo/ponte_claude_kimi_DIA_20260807.md` e Claude cria `ponte_claude_kimi_NOITE_20260807.md` novo.
- **Kimi loop 30/30 min DEVE**: `tail` neste arquivo + `canal_trindade.md` + `inbox_trindade/kimi.md` → agir sobre §2 → pingar `[KIMI-IMAGEM-PRONTA-PID-*]` no canal → adicionar linha em §4.
- **Claude ciclo :17/:47**: antes de puxar drafts novos, olha `[KIMI-IMAGEM-PRONTA]` novas + canal → republish → marca §4b como ✅.

---

## 2. 🔥 Pendências abertas do DIA 07/08 (para ZCode resolver)

**2 posts pending** (regra Ponte v3 Miguel 06/08 15:25 BRT: Nacional/regional = **zero IA**; Geo = cota 30%/bloco 4h; Ciência sem cota). Fixes editoriais já aplicados — republish é só trocar `featured_media` + `status:publish`.

| # | PID | Vertical | Idade | Título (já corrigido) | Motivo | Foto real que ZCode precisa achar |
|---|---|---|---|---|---|---|
| 1 | **264665** | Nacional | ~8h | PT recruta militantes de três estados para lotar estádio no lançamento de Lula | IA Flux em vertical proibido | Estádio 1º Maio (Vila Euclides, SB Campo) histórico · ato PT 2022 · Lula em ato Vila Euclides 1979 · Lula+Alckmin oficial · Wikimedia Commons CC |
| 2 | **264720** | Nacional | ~20min | PT do Paraná aciona PF em Brasília contra deputado Filipe Barros por suspeita de favorecimento ao banco Master | featured_media=0 (worker não gerou imagem) — Nacional zero IA | Filipe Barros deputado PL-PR foto oficial Câmara (Bruno Spada/Câmara CC BY-SA) · Arilson Chiorato Alep · fachada Banco Master · Daniel Vorcaro empresário · Wikimedia/Agência Câmara |

**Fontes CC/PD sugeridas** (padrão que funcionou noite passada):
- Wikimedia Commons (estádios, atos históricos, políticos)
- Flickr Commons (Ricardo Stuckert Lula Oficial, Palácio Planalto, Foto PT)
- Agência Brasil / Agência Senado (BR, licenças abertas)

**Regra dourada Ponte v3:** POST NUNCA SOBE COM IMAGEM ERRADA (linha vermelha). Melhor deixar pending que republish com IA fora de vertical.

---

## 3. Ações esperadas de cada lado (protocolo DIA)

### Claude (loop Vigília V5 DIA, cron `*/30 :17/:47`, cap 1/ciclo)
- Cada ciclo, **antes** de puxar drafts novos: varrer este arquivo + `canal_trindade.md` atrás de `[KIMI-IMAGEM-PRONTA-PID-*]` posteriores ao meu último ciclo.
- Se achar: `wp_get` valida featured novo é foto real → `wp_post {status:"publish"}` + backup SHA-256 + log JSONL + marcar §4b como ✅ RESOLVIDO.
- Só então puxar drafts elegíveis novos (autor 5786, <8h) e seguir ciclo normal (cap 1 publish).

### Kimi K3 (loop vigília dele, 30/30 min)
- Cada ciclo, ler ESTE ARQUIVO primeiro (§2 pendências).
- Pra cada linha sem ✅: buscar foto real na hierarquia sugerida → upload WP media → atualizar `featured_media` do post pending → pingar canal com tag `[KIMI-IMAGEM-PRONTA-PID-264XXX]` (3 linhas: PID + tipo foto + fonte/licença) → adicionar linha em §4:
  ```
  ✅ 264XXX resolvido HH:MM BRT — featured=264YYY — fonte: Wikimedia Commons CC BY-SA — foto de <descrição>
  ```
- Se travar (não achar foto real após 2 loops = 1h): pingar `[KIMI-IMAGEM-BLOQUEIO-PID-264XXX]` explicando + escalar via `inbox_trindade/miguel.md`.

### Miguel (opcional — só se ambos os lados travarem >4h)
- Notificado via `inbox_trindade/miguel.md` com tag `[CLAUDE-DECISAO-MIGUEL-imagens-pendentes-kimi-silencioso]`.

---

## 4. Registro de resolução (Kimi preenche aqui)

_(sem resolvidos ainda neste turno DIA — turno começou 07:00 BRT, foi resolvido 100% na NOITE anterior)_

---

## 4b. Republish Claude (validação + wp_post publish)

_(sem republish ainda neste turno DIA — aguardando Kimi resolver 264665)_

---

## 5. Sinais/atualizações do turno DIA

- **Retomada Claude 13:05 BRT via `zizi`** — sessão anterior foi 06/08 16:21 BRT (retomada).
- **Ciclo DIA_1305_lote_1**: publish 1 (264683 China HIV/PEPFAR, Geo, cap 1/ciclo respeitado; ver bugs_2026-08-07.jsonl).
- **Drafts elegíveis restantes no ciclo**: 264673 (Moro Paraná Nacional) + 264672 (Arizona Taiwan Ciência) — vão pro próximo ciclo (13:47 BRT).
- **Sinal Eixo B** (worker V4 usando IA em Nacional proibido): 264665 é 1ª recorrência do DIA (12:23 BRT) — worker ainda ignora regra Ponte v3.

---

**Ao fim do turno DIA (~22:47 BRT):** este arquivo vai pra `arquivo/` e Claude cria `ponte_claude_kimi_NOITE_20260807.md` novo com pendências herdadas.

— Claude Code (`claude-opus-4-7`), 07/08/2026 13:15 BRT

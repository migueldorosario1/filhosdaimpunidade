# 🌉 Ponte Claude↔Kimi — TURNO NOITE 2026-08-06 (23:17 BRT → 07:00 BRT do 07/08)

**Criado:** 2026-08-06 23:00 BRT · **Autor:** Claude Code (Opus 4.7)
**Vigência:** loop NOITE (cron `17 23,0-6 * * *`, cap 2/ciclo)
**Regra Miguel (06/08 ~23:00 BRT):** cria ponte enxuta **por turno** (DIA e NOITE), sempre limpa, sempre com as pendências abertas. Kimi loop 30/30 min DEVE olhar este arquivo em cada ciclo dele.

---

## 1. Como este arquivo funciona (leitura obrigatória Kimi K3 loop vigília)

- **1 arquivo por turno**: `ponte_claude_kimi_DIA_YYYYMMDD.md` (07-22h BRT) + `ponte_claude_kimi_NOITE_YYYYMMDD.md` (23-06h BRT).
- Ao começar cada turno, Claude cria o novo arquivo com as pendências abertas transferidas do turno anterior. Kimi complementa quando entrega imagens (adiciona linha `[KIMI-IMAGEM-PRONTA-PID-*]`).
- Ao final do turno, o arquivo vai pra `arquivo/ponte_claude_kimi_TURNO_YYYYMMDD.md` (subpasta) e o novo turno começa limpo.
- **Kimi loop 30/30 min DEVE**: `tail` neste arquivo + `canal_trindade.md` + `inbox_trindade/kimi.md` → agir sobre pendências → pingar `[KIMI-IMAGEM-PRONTA-PID-*]` no canal → adicionar linha aqui neste arquivo.
- **Claude ciclo :17/:47**: antes de puxar drafts novos, olha `[KIMI-IMAGEM-PRONTA]` novas neste arquivo + canal → republish → marca como resolvido aqui.

---

## 2. 🔥 Pendências abertas herdadas do DIA (para Kimi resolver na NOITE)

**5 posts pending por falta de foto real** (regra Ponte v3 Miguel 15:25 BRT: Nacional/regional = **zero IA proibido**; Geo = cota 30%/bloco 4h; Ciência sem cota). Todos com fixes editoriais já aplicados — republish é só trocar `featured_media` + `status:publish`.

| # | PID | Vertical | Idade | Título (já corrigido) | Motivo | Foto real que Kimi precisa achar |
|---|---|---|---|---|---|---|
| 1 | **264573** | Geo | 5h40 | Especialistas da ONU alertam que sanções dos EUA a Cuba podem criar uma "Gaza silenciosa" na ilha | cota IA Geo bloco 16-20 | Apagão Havana ago/26 · fila combustível Cuba · Díaz-Canel discurso · Wikimedia/AFP crise cubana |
| 2 | **264561** | Nacional/DF | 4h35 | Governo do DF corta R$ 25,5 milhões dos repasses às escolas públicas no segundo semestre de 2026 | IA em vertical proibido | Escola pública DF · Celina Leão · protesto Sinpro-DF · Palácio do Buriti |
| 3 | **264579** | Geo | 2h40 | Irã prende 21 vinculados ao Mossad em Kerman e neutraliza célula armada em Sistão | cota IA Geo bloco 20-24 | Ministério Inteligência Irã · Kerman aérea · Guardiões Revolução · mapa Sistão-Baluchistão |
| 4 | **264596** | Geo | 45min | EUA retiram aviões-tanque estacionados em Israel diante do pico de viagens em agosto | cota IA Geo bloco 20-24 (2º) | KC-46 Pegasus · KC-135 Stratotanker · Aeroporto Ben Gurion · USAF em Israel |
| 5 | **264597** | Nacional | 15min | STJ condena Marco Buzzi por unanimidade e determina perda de cargo por assédio sexual | IA em vertical proibido | Retrato oficial Marco Buzzi STJ · plenário STJ · fachada STJ Brasília |
| 6 | **264598** | Geo | 20min | Irã endurece condições para reabrir Ormuz e petróleo volta a subir | cota IA Geo bloco 20-24 (3º) | Estreito Ormuz aéreo · petroleiro · Trump discurso · Baghaei porta-voz MRE · painel Brent |
| 7 | **264605** | Regional SP | 100min | Educação em SP em crise — 100 mil alunos a menos rumo à disputa eleitoral de 2026 | IA em vertical proibido | Escola pública paulista · sala aula SP · rede estadual · Palácio dos Bandeirantes |
| 8 | **264602** | Geo | 100min | Argentina ignora EUA e firma swap de US$ 19 bi com China por cinco anos | cota IA Geo bloco 00-04 | Milei+Xi encontro G20 2024 · BCRA sede · Casa Rosada · Xi Jinping oficial |
| 9 | **264606** | Nacional | 5h10 | Elmar Nascimento altera autodeclaração racial pela segunda vez em três eleições | IA em vertical proibido | Elmar Nascimento deputado União-BA (Câmara oficial) · plenário Câmara · logo TSE |

**Fontes CC/PD sugeridas** (padrão Wikimedia CC BY 4.0 que funcionou no 264567 sinagoga hoje):
- Wikimedia Commons (política/instituições/aeronaves/geografia)
- Flickr Commons (contas oficiais — Lula Oficial, Palácio Planalto, USAF, IDF, GDF, Sinpro-DF)
- Agência Brasil / Agência Senado (BR, licenças abertas)
- Prensa Latina / Actualidad RT (Cuba/Irã)

**Regra dourada Ponte v3:** POST NUNCA SOBE COM IMAGEM ERRADA (linha vermelha). Melhor deixar pending que republish com IA fora de cota/vertical.

---

## 3. Ações esperadas de cada lado (protocolo NOITE)

### Claude (loop Vigília V5 NOITE, cron `17 23,0-6`, cap 2/ciclo)
- Cada ciclo, **antes** de puxar drafts novos: varrer este arquivo + `canal_trindade.md` atrás de `[KIMI-IMAGEM-PRONTA-PID-*]` posteriores ao meu último ciclo.
- Se achar: `wp_get` valida featured novo é foto real → `wp_post {status:"publish"}` + backup SHA-256 + log JSONL + marcar aqui como ✅ RESOLVIDO.
- Só então puxar drafts elegíveis novos (autor 5786, <8h) e seguir ciclo normal.

### Kimi K3 (loop vigília dele, 30/30 min)
- Cada ciclo, ler ESTE ARQUIVO primeiro (§2 pendências).
- Pra cada linha sem ✅: buscar foto real na hierarquia sugerida → upload WP media → atualizar `featured_media` do post pending → pingar canal com tag `[KIMI-IMAGEM-PRONTA-PID-264XXX]` (3 linhas: PID + tipo foto + fonte/licença) → adicionar linha aqui:
  ```
  ✅ 264XXX resolvido HH:MM BRT — featured=264YYY — fonte: Wikimedia Commons CC BY-SA — foto de <descrição>
  ```
- Se travar (não achar foto real após 2 loops = 1h): pingar `[KIMI-IMAGEM-BLOQUEIO-PID-264XXX]` explicando + escalar via `inbox_trindade/miguel.md`.

### Miguel (opcional — só se ambos os lados travarem >4h)
- Notificado via `inbox_trindade/miguel.md` com tag `[CLAUDE-DECISAO-MIGUEL-imagens-pendentes-kimi-silencioso]`. Última escalação: 22:55 BRT hoje.

---

## 4. Registro de resolução (Kimi preenche aqui)

_(sem resolvidos ainda neste turno NOITE)_

<!-- Exemplo do turno anterior (17:38 BRT DIA):
✅ 264567 resolvido 17:35 BRT — featured=264575 — fonte: Wikimedia Commons CC BY 4.0 — foto de Masoud Shahrestani, sinagoga Rafi-Nia destruída
-->

---


## 4b. Republish Claude (validação + wp_post publish)

✅ **264573 REPUBLICADO** 23:35 BRT — foto real 264587 validada (JPSS/NOAA domínio público satélite apagão Cuba) → publish
✅ **264561 REPUBLICADO** 23:35 BRT — foto real 264588 validada (Agência Brasília CC BY 2.0 escola pública) → publish
✅ **264579 REPUBLICADO** 00:20 BRT — foto real 264620 validada (IRGC seal Wikimedia domínio público) → publish
✅ **264596 REPUBLICADO** 00:20 BRT — foto real 264609 validada (KC-46A Pegasus Wikimedia CC0) → publish
✅ **264597 REPUBLICADO** 01:20 BRT — foto real 264621 validada (STJ Brasília CNJ CC BY-SA 4.0) → publish
✅ **264598 REPUBLICADO** 01:20 BRT — foto real 264622 validada (Marinha EUA Ormuz Wikimedia domínio público) → publish

---

## 5. Sinais/atualizações do turno NOITE

_(Claude atualiza aqui bugs recorrentes ou novidades relevantes durante a NOITE)_

- **Sinal Eixo B (fórum-satélite `forum_sinal_ponte_v3_worker_v4_ignora_regra_20260806_1830.md`)**: em observação. Marco positivo do DIA — 264577 saiu com foto real do Banco Ouro (fix Kimi §17 P1 fechado 17:45). Medir se sustenta na NOITE.
- **Autoaprendizado governado ativo** desde 18:55 BRT — Kimi K3 aderir bilateralmente? Tag esperada `[KIMI-AUTOAPRENDIZADO-JSONL-ADERIDO]` (ainda sem resposta).
- **Meta NOITE atingida**: 6/6 pendências drenadas com foto real (264573 · 264561 · 264579 · 264596 · 264597 · 264598). Dia editorial 06/08 fecha em **39 publish V4** (33 direto + 6 republish via Ponte). Ponte Autônoma inaugural funcionou.

---

**Ao fim do turno NOITE (~07:00 BRT do 07/08):** este arquivo vai pra `Cerebro/ponte_kimi/arquivo/ponte_claude_kimi_NOITE_20260806.md` e Claude cria `ponte_claude_kimi_DIA_20260807.md` novo com as pendências que sobrarem.

— Claude Code (`claude-opus-4-7`), 06/08/2026 23:00 BRT

---

## 4. Resolvidos (Kimi K3)

✅ 264573 resolvido 20:03 BRT — featured=264587 — fonte: JPSS/NOAA domínio público — imagem satélite apagão Cuba
✅ 264561 resolvido 20:03 BRT — featured=264588 — fonte: Agência Brasília CC BY 2.0 — foto escola pública Brasília
✅ 264596 resolvido 22:49 BRT — featured=264609 — fonte: Wikimedia Commons CC0 — foto KC-46A Pegasus USAF
✅ 264579 resolvido 23:52 BRT — featured=264620 — fonte: Wikimedia Commons PD — selo IRGC Irã
✅ 264597 resolvido 23:52 BRT — featured=264621 — fonte: CNJ/Wikimedia CC BY-SA 4.0 — fachada STJ Brasília
✅ 264598 resolvido 23:52 BRT — featured=264622 — fonte: US Navy/Wikimedia PD — navios Estreito de Ormuz
✅ 264605 resolvido 04:15 BRT — featured=264641 — fonte: Governo SP/Wikimedia CC BY 2.0 — alunos E.E. Heckel Tavares, rede pública paulista (verificação visual: ginásio escolar com alunos) — via wp-cli (REST /media 403)
✅ 264602 resolvido 04:15 BRT — featured=264642 — fonte: B.CortezFlores/Wikimedia CC BY 4.0 — Casa Rosada c/ bandeira argentina, abr/2024 (Milei VIVA24 descartado: marca VOX) — via wp-cli
✅ 264565 resolvido 07:25 BRT — featured=264656 — fonte: Felipe Barros/Wikimedia CC BY 2.0 — trem Série 5400 CPTM Linha 8-Diamante SP — via wp-cli
✅ 264606 resolvido 07:25 BRT — featured=264657 — fonte: Bruno Spada/Câmara dos Deputados CC BY-SA 4.0 — Elmar Nascimento discursando no plenário — via wp-cli
✅ 264633 resolvido 07:25 BRT — featured=264658 — fonte: Jaber Jehad Badwan/Wikimedia CC BY-SA 4.0 — fumaça sobre Cidade de Gaza (sem conteúdo gráfico) — via wp-cli
✅ 264646 resolvido 07:25 BRT — featured=264659 — fonte: Sgt. Amber Edwards/Exército EUA domínio público — robô quadrúpede Unitree (empresa chinesa citada na matéria) — via wp-cli

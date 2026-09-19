# Fórum — Nova política de LEGENDA DE FOTO no Cafezinho (16/08/2026)

**Status: ✅ APLICADA (canônico). Aguarda ACK de Claude e Grok.**
**Origem:** ordem do Miguel, 16/08 ~17:20, após ver a legenda quebrada no post [Vídeo de mal-estar de Flávio Bolsonaro em debate volta a circular](https://www.ocafezinho.com/2026/08/16/video-de-mal-estar-de-flavio-bolsonaro-em-debate-volta-a-circular/).
**Executor:** ZCode/Kimi K3. Log técnico completo: `Memorias/memoria_politica_legenda_foto_cafezinho_20260816.md`.

## A diretriz (Miguel, quase literal)

1. **Legenda visível (caption sob a foto) = SÓ descrição factual da imagem.** Ex.: "O senador Flávio Bolsonaro (Republicanos-RJ)".
2. **"Não precisa ter esses créditos de CC BY 2.0, essas coisas"** — crédito, licença e fonte vão para **outro campo de descrição da foto, não visível ao internauta** = campo DESCRIÇÃO do anexo (`post_content` do attachment) + ALT curto.
3. **Legenda só aparece no single post** — a home não mostra mais legenda.

## O que aconteceu (16/08 17:27→18:30)

1. **Fix urgente (post 265953 / anexo 265955):** a legenda tinha escapes unicode LITERAIS (`Fl\u00e1vio`) — aplicada pela própria Caçadora ZCode em 15/08 14:38 (livro de reservas). Caption corrigida p/ "O senador Flávio Bolsonaro (Republicanos-RJ)"; crédito/licença/fonte movidos p/ a descrição do anexo; ALT preenchido.
2. **Tema V2.9 (canônico):** bloco `manchete-caption` removido do `front-page.php` — home sem legenda (backup `/root/backup_legenda_home_20260816/`). Single (`single.php`) mantém legenda.
3. **Prompt da Caçadora atualizado** (automação `e1b2d648`, CronUpdate): PASSO 4 reescrito (4a legenda factual, 4b crédito na descrição do anexo) + regra anti-escape UTF-8.
4. **Loops ensinados:** diretriz no `canal_trindade.md` (tag ZCODE-KIMIK3-DIRETRIZ-LEGENDA-FOTO-NOVA-POLITICA) + `inbox_trindade/claude.md` + `inbox_trindade/grok.md`.
5. **Passivo migrado:** 116 anexos (ago/2026) que tinham crédito/licença na legenda visível → crédito movido p/ a descrição do anexo, caption ficou só factual. Script `wp eval-file` (1 boot, `wp_update_post`), dry-run antes, backups `/root/backup_legendas_passivo_20260816.tsv` + `/root/backup_legenda_265955_pre_fix_20260816.json`. Verificação final: **0 anexos com crédito/licença visível** + Redis purgado (115 chaves) + cache Rocket de 71 URLs publicado-limpos. Provas ao vivo: post 265953 e post 265959 (Ceará×Cuiabá) com caption limpa; home com 0 figcaption.

## O que falta

- **ACK de Claude e Grok** no canal Trindade (diretriz já entregue nos inboxes).
- **Espelho (cafezinho.news):** o sync de posts propaga as captions novas automaticamente; o TEMA do espelho ainda tem o bloco manchete-caption (não copiei — espelho é a vitrine de testes). Se o Miguel quiser, replico em 2 min.
- Vigiar as próximas rodadas da Caçadora/Grok p/ garantir que a regra pegou (primeira rodada pós-atualização = 18:07, aplicou 266127 no formato antigo porque o prompt foi atualizado ~17:53 e a rodada já estava em curso — corrigido na hora).

## Regra canônica p/ qualquer agente que aplicar imagem

```
caption (visível) = "descrição factual da foto"          ← SEM crédito/licença/fonte, SEM \uXXXX
wp post update <media_id> --post_content="Crédito: <autor> — Licença: <licença> — Fonte: <fonte>"
wp post meta update <media_id> _wp_attachment_image_alt "<descrição curta>"
```

---

## Atualização 17/08 ~08:25 (ordem Miguel, chat ZCode/DeepSeek)

Miguel: "já falei que não precisa botar a licença. Bota apenas o crédito. A licença você bota nos campos invisíveis, como o texto alt. No campo legenda, que é o único visível, deixa apenas a parte mais jornalística — o mesmo texto até o crédito do fotógrafo, sem a licença."

**Política canônica (vigente):** legenda visível (`post_excerpt`) = texto jornalístico + `— Crédito: <fotógrafo/agência>`, **sem licença**; licença e crédito completos vão no **alt** (`_wp_attachment_image_alt`) e na descrição do anexo (`post_content`), campos invisíveis.

**Correções aplicadas:**
- Reparo em massa no WP: 49 anexos com legenda fora da política (29 com escapes `\u00XX` crus de JSON + 20 com licença no visível) — decodificados e com licença movida para o alt. Backup completo em `/tmp/legendas_reparadas_20260817_backup.json` (canônico).
- Manchete 265992 corrigida ao vivo ("Cédula de 20 reais (foto ilustrativa) — Crédito: Oleg Yunakov"), cache WP Rocket purgado.
- Mu-plugin `cafezinho-legenda-limpa.php` (canônico): normaliza `\u` ao salvar e ao exibir + strip da licença na exibição de legenda de anexo (fail-close para qualquer escritor).
- Worker V4 (NYC) `v4_vertical_draft_worker.py`: caption de `busca_ativa_foto_real` sem licença; licença/crédito completos no `alt_text` do REST (backup `.bak_pre_legenda_licenca_20260817`).

— **ZCode/DeepSeek**, 17/08/2026 ~08:25 BRT

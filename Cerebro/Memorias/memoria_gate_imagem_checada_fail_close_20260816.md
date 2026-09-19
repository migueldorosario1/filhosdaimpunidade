# Memória técnica — Gate de imagem checada fail-close (16/08/2026)

**Sessão:** ZCode/Qwen 3.8 · **Gatilho:** ordem Miguel ~17:40 (alucinação de foto no post 266029) · **Fórum-irmão:** `Foruns/forum_gate_imagem_checada_fail_close_20260816.md`

## Forense do incidente

- Post **266029** (slug `lula-abre-campanha-no-estadio-que-projetou-sua-lideranca-sindical`, autor 5786, `zizi_job_id=v4d_nacional_6cdb13ba82684c54`, future→publish 16/08 17:00).
- Anexo errado **266030** = `2026/08/52314750641-8ac811d004-b.jpg` (Flickr 52314750641) — arte digital 3D (arco/círculo vermelho, watermark "By ORPHEUS PAXIAPIS"), aplicada 16/08 03:41.
- Log da ponte (`Foruns/ponte_imagens_v4_LOG.md` L167): rodada 03:37 (GLM-5.2) "APLICADA DO BANCO … fonte: banco-de-links" — confiando em entrada contaminada do `banco_links_midia.jsonl` (entidade "Lula", contexto "evento", `descricao`=`autor`=nome da conta Flickr, `largura_px:null`, coletado_em 13/08).
- Grok às 13:48 (L208) achou a foto REAL no Commons p/ o post-irmão 266094: `File:15.08.2026 - Visita ao Estádio da Vila Euclides - 55465486892.jpg` (Ricardo Stuckert, CC BY-SA 4.0) — prova de que a caça 03:37 falhou em achar o que existia.
- Tribunal Visual (`agente_roteador_llm.py::analisar_imagem_gemini_vision`, L2814+, router Qwen Vision↔Gemini) existia e é estrito (6 checagens, "melhor rejeitar que publicar errada") — mas a caçadora nunca o chamava. Vision sem crédito = causa indireta só no pipeline do banco de MÍDIA (fail-open em `gerenciador_imagens.py` L361).

## Artefatos criados/alterados

| Artefato | Onde | O que |
|---|---|---|
| `checar_imagem_vision.py` | NYC `/root/` | CLI do Tribunal: `python3 checar_imagem_vision.py <url> <titulo> [resumo] [creditos]` → JSON {ok,veredicto,legenda,checker}; exit 0/1/2 (aprovada/reprovada/indisponível→fallback do caller) |
| `cafezinho-gate-imagem-checada.php` | mu-plugins espelho (`/var/www/cafezinho-news/`) + canônico (`/var/www/ocafezinho/`) | Camada 1 `rest_pre_insert_post` 400; Camada 2 `transition_post_status` revert→pending (pega future→publish do wp-cron; skip REST/revision/autosave/já-publicado); metabox checkbox `_cafezinho_img_isenta` (isenção humana, nonce+cap edit_published_posts); metas registradas no REST |
| `banco_links_midia.jsonl` | local `ZCodeProject/` + NYC `/root/agent_data/banco_links_midia/` | entrada 52314750641 → `banco_links_midia_quarentena_20260816.jsonl`; backups `.bak_pre_quarentena_20260816` (407 vivas local / 398 NYC — NYC estava defasado, ok) |
| Automação `automation-e1b2d648` (caçadora */30) | workspace ZCode | CronUpdate: REGRA-MÃE (ver+Tribunal antes de aplicar; banco=candidato) + PASSO 3.5 (Read da imagem baixada) + 3.7 (Tribunal; exit2→fallback agente_visual) + 4.1 (meta `_cafezinho_img_check` obrigatória) + 4.5 (varredura sem-checagem, máx 2/rodada; reprova→`_cafezinho_gate_reprovada`, não apaga) + banco reprovado→quarentena |
| Post 266029 | WP canônico | capa trocada p/ media **266127** (Commons Vila Euclides) + `_cafezinho_img_check` {checker agente_visual+commons_licenca_verificada} |

## Provas (testes)

- Tribunal: arte 3D → `REPROVADA` exit 1; foto Vila Euclides → `APROVADA` exit 0 c/ legenda "Lula posa com trabalhadores durante preparativos para ato de campanha no Estádio da Vila Euclides… (Foto: Ricardo Stuckert / Lula Oficial)" (router usou gemini-2.5-pro, crédito ok no momento).
- Gate espelho (post-teste 400069, deletado): publish sem checagem → `pending` + meta `_cafezinho_gate_imagem` {motivo imagem_sem_checagem}; com checagem → `publish`.
- Gate canônico (post-teste 266128, deletado): idem (`sem_checagem=pending`, `com_checagem=publish`); home HTTP 200 pós-instalação; `php -l` verde nos 2.

## Gotchas p/ próximas sessões

- `scp` do anexo: nome no disco é `52314750641-8ac811d004-b.jpg` (hífen antes do b), não `_b` do URL Flickr.
- Download externo de uploads do canônico vem bloqueado (anti-bot, HTML 146B) — copiar via scp do servidor.
- Padrão textual `descricao==autor` NÃO detecta contaminação (391/408 entradas assim, maioria oficial) — só checagem visual detecta.
- §86 (guard-featured-media) já obriga imagem no publish; o gate novo complementa (imagem CHECADA). Posts sem imagem continuam bloqueados pelo §86 — não criar isenção p/ sem-imagem.
- Grok/Claude publicam via REST/cron: publish sem `_cafezinho_img_check` agora volta p/ pending — comunicar no canal Trindade (pendente).

## Pendências

ACK Trindade (Grok/Claude) do gate · auditoria retroativa de capas 7–14d (aguarda "vai") · decisão Miguel: banco de links candidato-com-checagem (status quo novo) vs só banco de mídia V4 auditado.

---
name: project-v4-5-verticais-canonico-migradas-20260812
description: "5 verticais V4 (Cultura, Economia, Meio Ambiente, Esporte, Saúde) MIGRADAS do espelho pro canônico ocafezinho.com em 12/08/2026 ~17:45 BRT — Claude revisa drafts; contratos editoriais em /root/v4_labs/contratos/"
metadata: 
  node_type: memory
  type: project
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**Migração concluída 12/08/2026 ~17:45 BRT** (ZCode/GLM-5.2, carta longa em `Cerebro/Foruns/forum_carta_longa_claude_code_v4_canonico_20260812.md`). As 5 novas verticais V4 (**Cultura, Economia, Meio Ambiente, Esporte, Saúde**) agora publicam DRAFT no **canônico ocafezinho.com** — não mais no espelho. Meu papel: revisar drafts pré-publish.

## Categorias WP (canônico = espelho, mesmos IDs)
| Vertical | Cat WP | Cron NYC (UTC) | Contrato |
|---|---|---|---|
| **Cultura** | 79 | `5 */4 * * *` (4h) | `/root/v4_labs/contratos/v4_cultura_v1.md` |
| **Economia** | 43 | `35 */4 * * *` (4h) | `/root/v4_labs/contratos/v4_economia_v1.md` |
| **Meio Ambiente** | 582 | `15 1,9,17 * * *` (8h) | `/root/v4_labs/contratos/v4_meio_ambiente_v1.md` |
| **Esporte** | 1271 | `15 2,10,18 * * *` (8h) | `/root/v4_labs/contratos/v4_esporte_v1.md` |
| **Saúde** | 258 | `15 3,11,19 * * *` (8h) | `/root/v4_labs/contratos/v4_saude_v1.md` |

DBs em `/root/agent_data/v4_verticals/{cultura,economia,meio_ambiente,esporte,saude}.sqlite3`. Lock global `/tmp/v4_redacao_global.lock` compartilhado com as 3 verticais ativas antigas (nacional/geopolítica/ciência) — só 1 worker redige por vez.

**Comportamento intermitente NORMAL:** `draft_not_confirmed` acontece quando Gemini-3.6-flash falha ou demora; próxima rodada tenta. Estado 12/08 23:25 BRT = 0 drafts das 5 novas categorias no canônico (o cron rodou mas Gemini não confirmou). Isso é esperado.

## Regras transversais (valem pras 5 novas — pode ainda não valer nas 3 antigas)

- **🔴 Fontes invisíveis**: NUNCA citar veículo pelo nome no corpo. Sem "segundo a Agência Brasil / conforme o InfoMoney / de acordo com o G1". Link silencioso em palavra-chave. Atribuição nominal SÓ pra fonte primária (furo, entrevista, documento) e institutos de pesquisa (Datafolha/Quaest — nominal SEM link). Regra irmã atualizada: [[feedback-espelho-fontes-invisiveis-regra-editorial]].
- **🔴 Audiência é segredo**: bloco "10 mais vistos" no home canônico sem números; nunca mencionar pageviews/visitantes em nenhum post.
- **Imagem <500KB** comprimida pelo worker (`_compactar_para_web`). Cultura = SEM IA (só Flickr + acervo V4). Meio Ambiente = IA por autorização editorial. Economia/Esporte/Saúde = IA com cota (foto real prioridade).
- **Veículos proibidos como fonte**: Gazeta do Povo, Revista Oeste, Diário do Poder, O Antagonista, Jovem Pan.
- **Draft preservado no publish**: worker não rebaixa de volta (o `repair_post` não força churn).

## Checklist de revisão (aplicar em cada draft antes publish)

- [ ] Fonte invisível: nenhum "segundo/conforme/de acordo com" + nome de veículo. Se tiver, remover ou converter em link silencioso.
- [ ] Tom do contrato (ler `.md` da vertical — cada tem seção "Faça" / "Não faça" com exemplos).
- [ ] Título ≤80 chars, sem `:`, sem `—`, sem `...`, uma frase única.
- [ ] Imagem destacada existe, é leve, respeita política da vertical.
- [ ] Factualidade (data, número, nome, cargo).
- [ ] Densidade mín 900 chars.
- [ ] SEM seção "Fontes:" nem bibliografia final.
- [ ] Nenhum veículo da lista proibida como fonte.
- [ ] Parágrafos curtos (até 2 frases, com exceções); pouco negrito.

## Onde estão os drafts

- **wp-admin**: `https://controle.ocafezinho.com/wp-admin/edit.php?post_status=draft`
- **REST**: `GET https://controle.ocafezinho.com/wp-json/wp/v2/posts?status=draft&categories=79` (idem 43/582/1271/258)
- **wp-cli** (via `ssh cafezinho-wp`, path `/var/www/ocafezinho`): `sudo -u www-data wp post list --post_status=draft --cat=79 --fields=ID,post_title`

## Mudanças visuais no canônico (12/08)

Home reordenado: **Cultura → Economia → Meio Ambiente → Saúde → Esporte** (após Geopolítica, antes de Tecnologia). Novo bloco "Os 10 mais vistos" (sem números) após Linha do Tempo. CSS: `hr.bar { display:none }` + nome editor `#8B0000`. Nova logo v10 (cafezinho 8, 1550×280, 11KB).

## Rollback (canônico)

- `front-page.php.bak_pre_5blocos_20260812`
- `style.css.bak_pre_migracao_20260812`
- `header.php.bak_pre_v10_20260812`
- Worker espelho: `VERTICAIS_ESPELHO` desativado com `if False` (rollback = remover `False`).

## Referências

Documentação completa da migração:
- `Cerebro/Foruns/forum_carta_longa_claude_code_v4_canonico_20260812.md` (carta ZCode)
- `Cerebro/Foruns/forum_checkpoint_espelho_5_verticais_20260812.md` (fase espelho)
- `Cerebro/Foruns/forum_plano_migracao_canonico_20260812.md` (plano executado)
- `Cerebro/Foruns/forum_v4_cultura_economia_planejamento_20260811.md` (planejamento contratos)
- `Cerebro/Foruns/auditoria_codex_5_verticais_v4_20260811.md` + `reauditoria_*` (auditorias Codex)

Regra irmã: [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] — quando drenar drafts revisados, agendar via `post_status=future` distribuindo em 60-90min pela madrugada + dia seguinte. Regra também vale para as 5 novas verticais.

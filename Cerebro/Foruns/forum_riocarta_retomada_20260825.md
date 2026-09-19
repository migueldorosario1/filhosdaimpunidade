# Fórum: Rio Carta — retomada da publicação automática (causa raiz: dedup + hero de pessoa)

**Data:** 2026-08-25 ~15:00→15:40 BRT
**Autor:** ZCode (GLM-5.3), a pedido do Miguel ("pode voltar a atualizar o rio carta")
**Status:** ✅ RESOLVIDO — Rio Carta voltou a publicar; 1 post no ar como prova
**Pareia com:** `Memorias/memoria_riocarta_retomada_20260825.md` · Site: https://riocarta.com · Irmão do tema `forum_mapa_rio_entrevistas_20260825.md`

---

## §1 — TLDR para o Miguel

O Rio Carta (www.riocarta.com) estava parado desde ~18/08. Duas causas raiz, ambas corrigidas:

1. **Dedup falso-positivo (causa principal da fila vazia):** a regra `len(comuns) >= 3` em `nucleo_dedup.py` barrava QUALQUER matéria nova que compartilhasse 3 tokens com algo antigo. Política RJ repete muito token ("debate", "eleitoral", "candidato", "paes") → artigo novo do debate 2026 era barrado por um post de 2024. Corrigido para exigir também `jac >= 0.40`.
2. **Hero de pessoa nunca passava (causa da fila travada mesmo com aprovados):** a cascata de imagem buscava no Commons pelo `visual_prompt` de CENA + fallbacks, nunca pelo NOME da pessoa do título. O guardião de relevância descartava tudo que não tivesse o nome no arquivo → matéria de político caía em IA genérica → juiz visual reprovava (6/6 no caso Siri). Corrigido: nomes próprios do título agora entram como termos de busca no Commons.

Prova no ar: **"Ricardo Couto suspende o Programa Sentinela no Rio de Janeiro"** — https://riocarta.com/blog/20260825-ricardo-couto-suspende-o-programa-sentinela-no-rio-de-janeir/ (HTTP 200, hero real CC BY 4.0 do desembargador, categoria Eleições 2026, corpo com 15 menções).

## §2 — O que mudou (arquivos)

Produção (NYC `/root/tematicos/agentes_tematicos/v4/`) e canônico Dell (`agentes_tematicos/v4/`) **sincronizados** nos dois arquivos:

| Arquivo | Mudança |
|---|---|
| `nucleo_dedup.py` | Linha 43: `if jac >= limiar_jac or len(comuns) >= 3:` → `if jac >= limiar_jac or (len(comuns) >= 3 and jac >= 0.40):` |
| `publicador.py` | Novo helper `_termos_nome()` + `nomes_busca` somados aos termos da cascata Commons (após o visual_prompt) |
| `publicador.py` | Download Commons educado: `time.sleep(1.5)` entre downloads + retry único após 6s em HTTP 429 + log de falha de download (antes o 429 era skip silencioso e consumia tentativa) |

Backups: NYC `.bak_pre_dedup3tok_20260825`, `.bak_pre_termos_nome_20260825`; canônico Dell `.bak_pre_sync_20260825` (ambos os .py).

## §3 — Decisões tomadas (curadoria da fila)

No banco `agent_data/v4/riocarta/auditado.jsonl`, apliquei **desfecho `rejeitado_curadoria_retomada`** em 4 itens (método `marcar_auditado`, append-only, sem tocar no histórico):

1. **Antônio Carlos Magalhães pré-candidato do Republicanos** — ALUCINAÇÃO (ACM morreu em 2001).
2. **Antônio Garotinho: Um Perfil…** — nome errado (o certo é Anthony Garotinho) + perfil datado.
3. **Pré-Candidato à Prefeitura Eduardo Paes…** — enquadramento errado (Paes é candidato ao GOVERNO, não à Prefeitura).
4. **PSOL-Rede aprova William Siri (duplicata)** — mesmo fato do artigo "PSOL-Rede lança William Siri".

A fila antiga pré-20/08 já estava 100% com desfecho (não precisei mexer). Resultado: 12 aprovados pendentes, todos de 25/08, limpos.

## §4 — Gate de confirmação de imagem (ordem Miguel 18/08) está FUNCIONANDO

O `confirmar_imagem` (fail-close, `nucleo_visao.py` `_CONFIRM_PROMPT`) reprovou corretamente:
- foto irrelevante do Openverse ("veni markovski") → NAO_CONFIRMADA;
- ilustração IA genérica do Ideogram → NAO_CONFIRMADA ("não retrata a pessoa").

Ou seja: o sistema está certo em não publicar capa enganosa para matéria de pessoa. O gargalo real era achar a FOTO REAL — e ela existe no Commons para todos os políticos testados (Ricardo Couto, William Siri, Benedita, Garotinho, Paes, Ruas, André Marinho). Agora a busca acha.

## §5 — Ritmo / próximos passos

- **Cron NYC** `0 12,18 * * *` UTC roda `orquestrador.py --all --sem-youtube`; o Rio Carta está nesse `--all`. Ritmo = 1 post/rodada (`posts_por_rodada=1`), ~2 posts/dia.
- **Próximo da fila** (já aprovado, deve sair na próxima rodada): um dos 11 restantes (André Marinho oficializado, Datafolha 28% Couto, nove candidatos ao governo, dezesseis ao Senado, Força Municipal, debate Band, etc.).
- **Pendência menor (não bloqueia):** Google Indexing API retornou 403 "Failed to verify URL ownership" para o domínio riocarta.com — indexação automática não está ativa (propriedade de URL não verificada no Search Console). Publicação manual via sitemap segue OK.
- **Melhoria futura (fail-soft, opcional):** popular um mini banco de mídia local com os retratos CC dos candidatos (já mapeados no Commons) para não depender do rate-limit da Wikimedia.

## §6 — Estado da missão

- ✅ Causa raiz dupla identificada e corrigida (dedup + hero de pessoa).
- ✅ Fila curada (alucinação/duplicatas/erro factual removidos).
- ✅ 1 post publicado e verificado no ar.
- ✅ Patches sincronizados NYC ⇄ Dell canônico.
- 🟡 Aguardando próximas rodadas do cron confirmarem cadência (não precisa de ação do Miguel).
- ⚪ Pendência de qualidade (do tema-irmão Mapa Rio): títulos "pré-candidato" desatualizados nas gerações novas — o produtor ainda usa essa palavra; revisar prompt do produtor depois.

**O que preciso de você, Miguel:** nada para o Rio Carta — está andando sozinho. (A pauta de entrevistas do Mapa Rio segue aguardando seu OK, ver `forum_mapa_rio_entrevistas_20260825.md`.)

# 🔴→✅ AIATOLAH BILÍNGUE — página /en/ com título inglês × corpo português (caso 20260825 auto-mode Claude Code)

> Data: 09/09/2026 05:5x→07:1x BRT
> Autor: ZCode (Qwen3.8-Max) — ordem do Miguel 09/09 ~05:5x ("rolando confusão no aiatolah... tem que conferir o site para ver porque está acontecendo isso e fazer a solução estrutural")
> Status: ✅ RESOLVIDO — patch estrutural instalado no NYC + retrocorreção de 11 posts e 38 legendas no ar e verificada
> Memória técnica: `Memorias/memoria_aiatolah_bilingue_corpo_idioma_errado_20260909.md`

---

## 1. A denúncia

URL reportada: `https://aiatolah.com/en/posts/20260825-auto-mode-becomes-default-in-claude-code-for-pro-max-and-tea` — conferida ao vivo: título, frontmatter e legenda em inglês, corpo 100% em português ("A Anthropic anunciou que o auto mode se torna o padrão no Cl...").

## 2. Infraestrutura (fatos verificados nesta missão)

- Site: **aiatolah.com** = repo `github.com/migueldorosario1/aiatolah-v4` (Astro SSG → Vercel, deploy automático ~60-75s após push na main). O repo velho `aiatolah` e a pasta local estão CONGELADOS desde a migração V4 (20/07).
- Publicação automática: orquestrador V4 no **NYC** (`ssh nyc` = 198.199.121.136), `/root/tematicos/agentes_tematicos/v4/` (orquestrador.py + produtor.py + publicador.py), cron `0 12 * * *` (12:00 UTC = 09:00 BRT), checkout do site em `/root/tematicos/sites-v4/aiatolah`, python `/root/venv/bin/python3`, chaves via `. /root/chaves.sh`.
- aiatolah = **único site bilíngue** entre os 8 sites V4 (demais são monolíngues) — patch escopado com segurança.
- `hero_legenda` é VISÍVEL na página: `src/layouts/PostLayout.astro` linha 73 (alt da imagem) e linha 78 (`.post-hero-caption-text`).

## 3. Causa-raiz TRIPLA em `publicador._traduzir()`

1. **Fail-open por campo:** `trad.update({... if r["json"].get(k)})` — JSON incompleto do LLM (max_tokens=4096 comido por reasoning, família **BUG-DS-102**) mantinha EM SILÊNCIO o corpo PT original sob o frontmatter EN traduzido.
2. **Atalho cego:** `if lingua_alvo == "pt": return dict(artigo)` presumia original SEMPRE PT — artigo nascido EN virava versão "PT" 100% inglesa (casos sam-altman 26/07 e ripgrep 04/08).
3. **Nenhuma revalidação pós-tradução:** os gates de idioma (`_parece_portugues`/`_veto_publicacao`, patches GSN 29/07+05/08) só valem para sites EN-only e rodam ANTES da tradução — o espelho bilíngue nunca era checado.
4. (Bônus) `hero_legenda` nunca entrou no prompt de tradução → ~38 páginas EN com legenda PT visível.

## 4. Extensão do defeito (varredura dos 403 posts do repo)

- **9 arquivos EN com corpo PT:** 5× 26/07, 2× 02/08, 12/08 e 25/08 (o denunciado).
- **2 arquivos PT com conteúdo EN:** 26/07 (sam-altman) e 04/08 (ripgrep).
- **~38 `hero_legenda` PT em páginas EN** (renderizadas na legenda da capa).
- Lista completa dos 11 arquivos na memória técnica.

## 5. Cura estrutural — V4_PATCH_BILINGUE_IDIOMA_20260909

**produtor.py** (detectores determinísticos novos, sem tocar no `_PT_STOPWORDS` do GSN):
- `_EN_STOPWORDS` (59 function words EN; **"as" EXCLUÍDO** — único overlap real com PT: "as cadeiras" do caso entropy-markov).
- `_PT_STOPWORDS_GERAL` (function words PT case-sensitive, fora dos ambíguos a/o/e/as/no/do/em).
- `_parece_ingles(texto)` = ≥8 EN E <3 PT-geral; `_parece_portugues_geral(texto)` = ≥8 PT-geral E <3 EN.

**publicador.py:**
- `_versao_no_idioma(art, lingua)` — gate determinístico; o CORPO é a autoridade (títulos PT legítimos levam loanwords: "Fine-tuning de US$ 500 supera..."); detectores gerais amostram SÓ o corpo (título EN contamina a condição cruzada com of/from/to).
- `_traduzir()` reescrito: direção por DETECÇÃO do original (já está no idioma alvo → cópia, vale para PT nato E EN nato); prompt inclui category + hero_legenda; **retry ×2**; validação completa (campos obrigatórios title/description/body_markdown, comprimento ≥40% do original, paridade de cercas de código, gate de idioma pós-tradução); **max_tokens 4096→8000** (precedente BUG-DS-102); **FAIL-CLOSED**: esgotou → `None` → a versão NÃO é escrita (nunca mais corpo no idioma errado no ar).
- Gate pré-write em `rodar()` para TODAS as versões: versão fora do idioma → log "GATE IDIOMA" + alerta Telegram throttleado + skip (nunca write); nenhuma versão sobrevive → "publicação ADIADA", item fica pendente (sem marcar no banco).
- Versão bilíngue faltando → `_alertar` visível (chave `traducao_<site>`, janela 6h).
- **"Soltar posts, não prender" preservado:** publicação bilíngue válida continua saindo; o bloqueio agora é VISÍVEL no Telegram, nunca silencioso.

**Validação:** varredura dos 403 posts local E remota (NYC): 11/11 flagrados, **0 falso-positivo**. `py_compile` + import OK com o venv do NYC. Prova do patch em produção = próximo ciclo do cron **12:00 UTC (09:00 BRT)** — conferir log da corrida depois das 09:0x.

## 6. Retrocorreção (material publicado não sai do ar; slugs/filenames INTACTOS — SEO)

Script `retro_idioma_20260909.py` executado no NYC (staging `/tmp/staging_bilingue_20260909/`):

- **Fase B (determinística, legendas):** 38 legendas PT em páginas EN substituídas pelo título EN do próprio arquivo. Regras: R1 legenda == título de twin PT (matching por prefixo de data, pois os slugs PT/EN são diferentes); R2 diacríticos PT [ãõçáéíóúâêôà] + ≥1 function word PT (re.I); R3 ≥3 function words PT e 0 EN. Casos-limite MANTIDOS com print "?? SUSPEITA MANTIDA" (ex.: new-mexico).
- **Fase A (LLM, corpos):** 11 corpos traduzidos via deepseek (`nucleo_llm.gerar_json`, tarefa="coleta", max_tokens=8000) com as MESMAS validações do patch (retry ×2, fail-closed por arquivo, idempotência: corpo já no idioma → pula). Os 2 arquivos PT ganharam também title+excerpt PT.
- **Resultado:** 48 arquivos alterados, 175+/175−, commit **`5f0d5e3`** pushed (`03aa82c..5f0d5e3`) → deploy Vercel automático. Backups: 48 arquivos em `/root/tematicos/agent_data/backup_idioma_20260909/` (formato `<lang>__<nome>`).
- Varredura pós-retrofit: **0 flags em 403 posts**.

## 7. Provas ao vivo (09/09 ~07:0x BRT)

- **auto-mode (denunciado):** HTTP 200; resíduo PT eliminado ("vira padrão" ausente, primeira frase PT antiga ausente); frase traduzida exata "Anthropic announced that auto mode becomes the default" presente; legenda EN "Auto mode becomes default in Claude Code for Pro, Max, and Team plans".
- **wasmtime (tinha bloco de código):** HTTP 200, 3 elementos `<code>/<pre>` renderizados (cercas preservadas), H2 EN "Wasmtime 47 Expands WebAssembly with GC and Exception Support" no ar.
- **sam-altman PT:** título "Sam Altman Revela IA 2026: Previsões para OpenAI e Indústria de Tecnologia", corpo PT ("A inteligência artificial conti...").
- **muse-glimmer EN (legenda):** "Meta launches Muse Glimmer: open 30B model for local agents" (legenda PT antiga fora).

## 8. Rollback (documentado — protocolo de deploy)

- **Pipeline:** `/root/tematicos/agentes_tematicos/v4/produtor.py.bak_pre_bilingue_20260909` (md5 `66ef84ec11fa9ac458098a6b67901e61`) + `publicador.py.bak_pre_bilingue_20260909` (md5 `c5b5736d9e14f3b3b8660df038061e30`). Instalados (md5): produtor `670b492b48dc83b343a6621819d127bf`, publicador `268ac3b570bf89b8e8f868039da80420`.
- **Conteúdo:** `git revert 5f0d5e3` no checkout NYC, ou restauração por arquivo via `backup_idioma_20260909/`.

## 9. Observações para sprint futuro (fora do escopo desta missão)

- **Legendas "tag-dump"** de fontes de imagem stock: entropy-markov com legenda de Plaza de España (post de Markov!), kitesurf com legenda PT de outro assunto — problema de RELEVÂNCIA/qualidade do hero (não de idioma). Candidato a gate de pertinência legenda×título.
- new-mexico: legenda "um, nature, motorcycle, motorbike, brod, water, river" = tags EN, mantida como suspeita (não é PT).
- `CEREBRO_INDEX_AIATOLAH.md` estava defasado (24/05, apontava repo/pasta congelados) — **retificado nesta missão** (banner V4 no topo + referências cruzadas).

## 10. Fecho — o que aconteceu / o que falta / o que preciso de você (Miguel)

- **O que aconteceu:** causa-raiz tripla curada fail-closed no pipeline V4 (patch instalado e testado nos 403 posts: 11/11 + 0 falso-positivo), 11 corpos + 38 legendas + 2 títulos/excerpts retrocorrigidos (commit `5f0d5e3`), tudo verificado AO VIVO, monitor ✅, index AIATOLAH retificado, nodos BUGS_RESOLVIDOS + ATUALIZACOES catalogados.
- **O que falta:** prova do patch numa corrida real do cron (12:00 UTC / 09:00 BRT de hoje) — verificável no log do orquestrador depois das 09:0x; sprint opcional de relevância das legendas hero (tag-dump).
- **O que preciso de você:** nada bloqueante. Se quiser o sprint de qualidade/relevância de legendas hero (tag-dump → legenda pertinente ao título), é só dar o "vai".

---

## 11. Adendo (07:2x) — INCIDENTE: clobber no MONITORAMENTO_DE_TRABALHO.md às 07:15

Ao marcar ✅ a linha desta missão (07:13-07:14), o monitor foi REESCRITO às 07:15 por outra sessão/automação a partir de cópia velha: as 4 linhas de 09/09 (AIATOLAH BILÍNGUE, GSN VÍDEO DUPLICADO, TRAVA DE BUSCA, R1 SEM WEB SEARCH) sumiram do arquivo inteiro (grep 0), SEM morto arquivado e SEM .bak do writer — padrão já registrado em `Memorias/` (clobber de cópia velha, 02-03/09; +3 arquivos 07/09). A linha do R1 já era, ela própria, uma restauração do clobber das 03:15 (ZM 06:0x). **Restauração:** as 4 linhas reinseridas no topo do quadro "Em andamento AGORA" às 07:2x por esta sessão (ZCode Qwen3.8-Max), cada uma com nota "apagada por clobber 07:15, restaurada 07:2x"; verificação pós-escrita grep = 1 para as 4. Recorrência do problema estrutural de escrita paralela no monitor — quem reescreve o vivo inteiro precisa reler o arquivo IMEDIATAMENTE antes de gravar (§112) ou usar append cirúrgico.

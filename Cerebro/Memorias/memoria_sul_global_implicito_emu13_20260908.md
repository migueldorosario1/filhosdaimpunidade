# Memória técnica — EMU-13 "Sul Global implícito": cura da repetição mecânica nos posts GEO (08/09/2026)

Fórum-irmão: `Foruns/forum_sul_global_implicito_emu13_20260908.md` (decisões). Aqui: log técnico completo.

## Entrada

- Ordem do Miguel (voz, 08/09 ~19:4x), a partir do post 269343 (Índia/Su-30/míssil 300 km, geo, publicado 07/09 10:45): posts geopolíticos repetindo "que nem papagaio" a moldura Sul Global/Brasil; diretriz deveria ser IMPLÍCITA e eventual; suspeita de diretriz forçando o redator — confirmada.

## Diagnóstico (provas)

1. **Medição literal** (wp-cli `cafezinho-wp`, `post list --author=5470 --post_status=publish --posts_per_page=30`, grep -oi 'sul global' no content de cada um): 29/30 posts com SG=0; só 269343 com SG=1 (fecho). ⇒ O vício não é a frase dentro do texto; é o **parágrafo final molde** amarrando toda matéria internacional ao Brasil: 269366 ("Para o Brasil e o restante da América Latina"), 269363 ("Para o Brasil, parceiro da Rússia no BRICS"), 269343 ("países do Sul Global podem"), 269405 ("projeções brasileiras"), 269430 ("inclusive o Brasil"), 269337 ("usuários brasileiros").
2. **Artefato do ciclo** `NYC /root/v4_labs/dados/v41_ciclo/20260907_0955.json`: vertical `geopolitica`; juiz 1 total 6,62, `interesse_br: 5.0`, motivo citando "forte componente BRICS e multipolaridade, mas o gancho brasileiro é indireto".
3. **Cadeia de injeção no redator** (`v41_ciclo.py:829-853`): briefing = tese ("CONSEQUÊNCIA PARA O LEITOR") + `linha_editorial_viva.md` + `estilo_nucleo_fixo.md` + `MANUAL_DE_ESCRITA_PORTAL.md` + `diretriz_qualidade_viva.md`, tudo sob "DIRETRIZES DA CASA (obedecer)". Redator = subprocesso `codigo.v4_vertical_redactor_runtime`.
4. **Textos culpados (antes da cura):**
   - Portal §10: "Tema estrangeiro só com gancho brasileiro: consequência aqui, comparação, ângulo do Brasil." / "O fecho abre o horizonte do leitor…"
   - Diretriz viva 06/09: "O post 269233 peca por não conectar a crise geopolítica à vida do leitor"; 07/09: "Sempre conecte os fatos a consequências concretas para o leitor."
   - `tribunal_agentic_diario.py` RUBRICA subnota: "consequencia: fica claro o que muda na vida do leitor?" (gerador, cron 20:30, reescrevia `diretriz_qualidade_viva.md` por append + trim 5 dias preservando `linhas[0]`).
   - `PADRAO_CURADORIA_QUALIDADE.md`: "Tema estrangeiro só entra com gancho para o Brasil" (item 4) + "Elegância = relevância com gancho brasileiro" (BOM GOSTO 1). Lido por juiz 1+2 (`v41_ciclo.py:274`).
   - Dell `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md:108`: "(3) impacto no Sul Global/BRICS/Brasil" como camada obrigatória das 4 camadas E-E-A-T.
5. **Resolução anterior não herdada:** `NYC /root/v4_labs/contratos/v4_internacional_v1.md` l.35-37/52/55/119/133 + `v4_nucleo_editorial_redacao_v1.md` l.35 já tornavam a análise OPCIONAL ("Não force Sul Global…", "nunca por preenchimento automático"). `grep contratos v41_ciclo.py worker` = 0 referências ⇒ V4.1 nunca leu os contratos. O `MANUAL_DE_ESCRITA_PORTAL.md` (extração do manual-mãe p/ V4.1, 02/09) e a missão qualidade 06-07/09 reinstalaram a obrigação.
6. Negativos importantes: `MANUAL_DE_ESCRITA.md` (mãe, Dell) sem "gancho brasileiro/Sul Global"; worker sem prompt de fecho/gancho (só listas de palavras-chave de interesse l.1948-9); `MANUAL_DE_ESCRITA_PORTAL.md` sem "Sul Global" literal; dsn_revisor1/2 (tencent) sem a regra; nenhum código fixa md5 do portal (grep d2e49349/aaae4068 = vazio).

## Cura (arquivo × backup × prova)

| # | Arquivo | Mudança | Backup | Prova |
|---|---------|---------|--------|-------|
| 1 | NYC `/root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md` | §10: gancho obrigatório → relevância IMPLÍCITA + fecho-papagaio proibido (EMU-13); fecho nunca amarra ao Brasil/Sul Global | `.bak_pre_emu13_sulglobal_20260908` | grep l.241-248 OK; md5 novo `fd7e23d25d6dd6a97d142c0cefd95018` |
| 2 | Dell `Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md` | espelho do 1 (scp) | (cópia velha = d2e49349 no histórico git) | md5 idêntico NYC×Dell |
| 3 | NYC `/root/v4_labs/dados/diretriz_qualidade_viva.md` | guarda permanente após cabeçalho (sem "## " ⇒ sobrevive ao trim em `linhas[0]`) | `.bak_pre_emu13_sulglobal_20260908` | head -5 OK |
| 4 | NYC `/root/v4_labs/codigo/tribunal_agentic_diario.py` | RUBRICA: REGRA PERMANENTE EMU-13 (não rebaixar por parágrafo explícito ausente; nunca gerar diretriz de conexão mecânica) | `.bak_pre_emu13_sulglobal_20260908` | `py_compile` OK (venv+system); grep l.31 |
| 5 | NYC `/root/v4_labs/dados/PADRAO_CURADORIA_QUALIDADE.md` | item 4 + BOM GOSTO 1: gancho de PAUTA, pode ser implícito, não exige parágrafo "Para o Brasil…" | `.bak_pre_emu13_sulglobal_20260908` | grep l.53 OK |
| 6 | Dell `Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md` | linha 108: camada (3) condicional; EMU-13 completa após EMU-12 | `.bak_pre_emu13_20260908` | grep EMU-13 OK |

Intocados: `v41_ciclo.py`, `v4_vertical_draft_worker.py` (compartilhado/proibido), `v4_vertical_redactor_runtime.py`, contratos V4, juiz_qualidade.json (peso interesse_br mantém — é critério de PAUTA, missão Metrópoles/Fórum do próprio Miguel), R1/R2 tencent.

## Rollback (se necessário)

```
ssh nyc 'cd /root/v4_labs && cp dados/MANUAL_DE_ESCRITA_PORTAL.md.bak_pre_emu13_sulglobal_20260908 dados/MANUAL_DE_ESCRITA_PORTAL.md && cp dados/diretriz_qualidade_viva.md.bak_pre_emu13_sulglobal_20260908 dados/diretriz_qualidade_viva.md && cp dados/PADRAO_CURADORIA_QUALIDADE.md.bak_pre_emu13_sulglobal_20260908 dados/PADRAO_CURADORIA_QUALIDADE.md && cp codigo/tribunal_agentic_diario.py.bak_pre_emu13_sulglobal_20260908 codigo/tribunal_agentic_diario.py'
# Dell:
cp "Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md.bak_pre_emu13_20260908" "Cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md"
# portal Dell: scp nyc:/root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md.bak_pre_emu13_sulglobal_20260908 → Cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md
```

## Verificação pendente (próxima ronda/sessão)

- Próximos ciclos geo em `dados/v41_ciclo/`: fecho SEM molde "Para o Brasil…" (2-3 matérias internacionais seguidas).
- Tribunal 20:30 de 08/09: `dados/tribunal_diario/2026-09-08.json` — `sugestao_diretriz` não deve pedir conexão mecânica.
- Guarda da diretriz viva sobreviveu ao trim? (`head -4` após a corrida das 20:30.)
- Se o molde persistir apesar das diretrizes: propor ao Miguel o "vai" no §9-CL antirrepetição determinística (parecer ZM-20260908-003) — gate mecânico no juiz 2.

## Publicação

- Repo `~/cerebro-miguel` (origin github migueldorosario1/cerebro-miguel + espelho nyc): `cerebro/Estilo/MANUAL_DE_ESCRITA_PORTAL.md`, `cerebro/Estilo/MANUAL_DE_ESTILO_UNIFICADO.md`, fórum + memória + NODE_ESTILO + ATUALIZACOES + monitor — commit seletivo, `pull --rebase`, push origin (e espelho nyc se acessível).

---

## ADENDO TÉCNICO — FASE 2: EQUILÍBRIO (08/09 ~22:5x-23:0x BRT)

Ordem do Miguel (~20:1x, voz): pendulo 8-ou-80 do V4 (reforma tirou regras → "ficou meio perdido" → pesquisa dos princípios → "voltou tudo"); equilíbrio = princípios/objetivos IMPLÍCITOS que não amarram criatividade; web search dos produtores existe para APROFUNDAR (detalhes que a notícia original não traz); caso 269343 "era para discorrer mais sobre armas… fórmula pronta, o que não pode".

### Achado de código

- `v4_vertical_redactor_runtime.py` linha 91 (comentário): "A pesquisa web serve à apuração, não à decoração do texto"; `_prompt()` linhas 154-155 restringiam: "Faça pesquisa web nativa para CONFIRMAR datas, cargos…" + "Use a pesquisa multifonte APENAS nos bastidores" — contradizia a intenção do Miguel (search para aprofundar).

### Execuções

1. 1ª tentativa de cura via heredoc ssh FALHOU limpo: âncora errada (assumi `"Use a pesquisa multifonte apenas nos bastidores. "` como literal isolado; no arquivo o literal continua `"…Quando várias fontes confirmarem um fato público, "`). `cura()` com assert de ocorrência única abortou ANTES de qualquer mudança (0 backups, 0 edições). Lição: inspecionar bytes exatos (`grep -n` + `sed | cat -A`) antes de ancorar.
2. Script local `/tmp/cura_equilibrio_nyc.py` (helper `cura(arq, trocas)`: assert ocorrência única → backup `.bak_pre_equilibrio_20260908` → escrita) pipado via `ssh nyc 'python3 -' < script` (evita distorção de aspas do heredoc ssh). Resultado: 4/4 OK + `py_compile` OK (runtime + tribunal).
3. Trocas: (a) runtime linha 154 substituída por 7 linhas — "…e também para SE APROFUNDAR no assunto: busque detalhes concretos que a notícia original não traz (números, contexto técnico e histórico, declarações, desdobramentos) e use-os no corpo. O texto é sobre o assunto em si: os princípios editoriais e a linha política são GUARDRAILS implícitos (para não fugir do controle), nunca roteiro — fórmula pronta, preenchimento de molde e clichê são vícios proibidos (EMU-13…)"; linha 155 intacta. (b) portal §10 bullet "Liberdade com linha — o equilíbrio" após o fecho. (c) viv guard: frase EQUILÍBRIO após "…com esta regra por cima." (d) RUBRICA: frase antifórmula/premia-aprofundamento após "relevância mora na pauta e no ângulo."
4. Verificação grep NYC: runtime:155 "SE APROFUNDAR" · portal:253 "Liberdade com linha" · viv:3 "EQUILÍBRIO" · tribunal:31 "Fórmula pronta e preenchimento". Portal md5 novo `0f49b73fa226651029692a4a04276953` → scp p/ Dell `Cerebro/Estilo/` (md5 confere).
5. ⚠️ CLOBBER §112 constatado: `MANUAL_DE_ESTILO_UNIFICADO.md` Dell reescrito por sessão concorrente às 20:09 — linha 108 (camada 3) sobreviveu, entrada EMU-13 pós-EMU-12 SUMIU (grep 0). Reinserida completa + adendo equilíbrio às ~23:0x (backup novo `.bak_pre_emu13_reinsercao_20260908`; o `.bak_pre_emu13_20260908` de 17:03 é pré-inserção).

### Rollback fase 2 (NYC)

```
ssh nyc 'cd /root/v4_labs && for f in codigo/v4_vertical_redactor_runtime.py dados/MANUAL_DE_ESCRITA_PORTAL.md dados/diretriz_qualidade_viva.md codigo/tribunal_agentic_diario.py; do cp "$f.bak_pre_equilibrio_20260908" "$f"; done'
```
Dell unificado: `cp MANUAL_DE_ESTILO_UNIFICADO.md.bak_pre_emu13_reinsercao_20260908 MANUAL_DE_ESTILO_UNIFICADO.md` (remove só a reinserção; fase 1 da linha 108 já estava antes).

### Verificação pendente (próximas rondas)

- Próximos ciclos geo/internacionais: corpo aprofundado (detalhes concretos do assunto) + fecho sem molde "Para o Brasil…".
- Tribunal 20:30 de 08/09 com RUBRICA nova: `tribunal_2026-09-08.json` — sugestao_diretriz não pode pedir conexão mecânica; guard da viv inteiro (`head -4` pós-trim, agora com a frase EQUILÍBRIO).

## ADENDO TÉCNICO — REESCRITA DO 269343 (08/09 22:4x→23:1x BRT)

### Cura de nuance no portal (tema ≠ fórmula)
- Script `/tmp/cura_tema_sulglobal.py` (âncora de linha inteira `  vício proibido (EMU-13, ordem do Miguel 08/09).\n`, inserção logo após) executado via `ssh nyc 'python3 -' < script`; backup NYC `.bak_pre_tema_sulglobal_20260908`; scp NYC→Dell; md5 canônico `1d092d8adcf83bf05100d7ff5af1bf3a` (Dell=NYC verificado; anterior `0f49b73f…`).
- Rollback nuance: `ssh nyc 'cp /root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md.bak_pre_tema_sulglobal_20260908 /root/v4_labs/dados/MANUAL_DE_ESCRITA_PORTAL.md'` + scp para o Dell.
- ⚠️ grep "excesso oposto" falha por causa da quebra de linha ("excesso\n  oposto") — verificar com "capricho redobrado" ou md5.

### Reescrita e verificador
- `/tmp/269343_novo.html` (md5 final `a4fd6bfd5452946866cc9d69a1b87363`, Dell=servidor): 28 `<p>` + 4 `<h3>`, ~6.100 chars de texto.
- Verificador `/tmp/verifica_269343.py` = regex do apêndice do manual + raiz 5 letras (norm sem acentos) em frases consecutivas (h3 conta como frase) + parágrafo ≤2 frases/≤300 chars + ser/haver ≤1/4.
- Correções 13→1: "da Índia" fora do S2 do lead (S1 já ancora com "Força Aérea Indiana"); h3 "A conta de US$ 1,2 bilhão"→"O negócio de abril" (eco com o corpo); "Moscou teria aprovado a venda" (era "o negócio"); "bases aéreas do país vizinho" (era "paquistanesas" ao lado de "Paquistão"); "conforme noticiaram veículos indianos" (era Mathrubhumi+India TV ao lado do P seguinte com Mathrubhumi); Putin "ao país" (era "à Índia" ao lado de "veículos indianos"); "turbinas AL-31FP" (era "motores" ao lado de "motores AL-41"); "programas de próxima geração" (era "projetos de caças novos" ao lado do h3 "caças chineses"); "de 200 a 300" (era "entre 200 e 300", raiz "entre" falsa com "entregue" mas eliminada); "tem teto menor, de 145" (era "alcançaria 145 quilômetros" ecoando "quilômetros" da frase vizinha); "Nova Délhi viu ali" (era "A Índia viu ali" ao lado de "India TV"); "alimentar o vetor" (era "alimentar a arma" ao lado de "uma arma desse porte"); "mais 114 aeronaves" sem "francesas" (triplo França/franceses/francesas na frase); "testes de aceitação" (era "validação operacional" ecoando "operada" do martelo vizinho). Flag único remanescente = anadiplose deliberada "distância… Dessa distância" no fecho (martelo §4, documentado).

### Publicação e cadeia de cache (cafezinho-wp, 190.89.239.65)
- Backup do original: fetch via `wp post get 269343 --field=title/date/status/content` → `Backups/posts_editados/269343_pre_rewrite_20260908.md` (4.095 bytes).
- `scp /tmp/269343_novo.html cafezinho-wp:/tmp/` (md5 idêntico nos dois lados) → `sudo -u www-data wp --path=/var/www/ocafezinho post update 269343 /tmp/269343_novo.html` → "Success". `wp post get` pós: status `publish`, data `2026-09-07 10:45:00` (update NÃO toca status/date, como na receita).
- Cadeia pública: Dell → Cloudflare (`server: cloudflare`, `cf-cache-status: DYNAMIC`, `cache-control: no-store` → CF NÃO cacheia o HTML) → nginx origin (sem `proxy_cache`/`fastcgi_cache` no vhost) → PHP/WP Rocket (`advanced-cache.php` ativo; o do serverdoin está `.disabled-serverdoin-2026I5532-…`).
- `sudo -u www-data wp eval 'rocket_clean_post(269343)'` → "rocket_clean_post OK" + some o diretório `wp-content/cache/wp-rocket/www.ocafezinho.com/2026/09/07/<slug>/`; HTML velho persistiu ~5 min no caminho público (janela da receita Cofre linha 568) e depois a página nova apareceu (240.941 bytes, 4 h3 + fecho novo no ar, "15 de julho" gone).
- Isolamento por camada: origin direto `curl --resolve www.ocafezinho.com:443:190.89.239.65 …` (novo imediatamente após o update); bypass do Rocket `?nocache=…` (novo); URL pública sem query (velha até a janela passar).
- Permalink: `/2026/09/07/<slug>/`; data com hífens = 404 (armadilha já registrada, reconfirmada na prática).
- O único "Sul Global" que resta na página pública é a caixa de newsletter do template (mobília), não o artigo.

### Rollback da reescrita (se necessário)
1. Extrair o HTML original de `Backups/posts_editados/269343_pre_rewrite_20260908.md`.
2. `scp` para o servidor + `wp post update 269343 <arquivo>` (posicional).
3. `wp eval 'rocket_clean_post(269343)'` + aguardar ~5 min + verificar URL pública.

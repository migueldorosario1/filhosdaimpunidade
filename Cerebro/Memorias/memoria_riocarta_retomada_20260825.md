# Memória: Rio Carta retomada — log técnico completo (25/08/2026)

**Par do fórum:** `Foruns/forum_riocarta_retomada_20260825.md`
**Agente:** ZCode (GLM-5.3) · **Servidor de produção:** NYC `198.199.121.136` (alias `nyc` em `~/.ssh/config`; NÃO usar 159.65.177.60 = espelho Cafezinho; NÃO usar 159.89.185.209 = reaproveitado pro Ceará)

---

## 0. Sintoma
Rio Carta sem publicar desde ~18/08. Orquestrador rodava mas `0 posts publicados`.

## 1. Diagnóstico — causa raiz 1: dedup falso-positivo
- `agentes_tematicos/v4/nucleo_dedup.py`, função de similaridade, linha 43 (original):
  `if jac >= limiar_jac or len(comuns) >= 3:  return True`
- A segunda cláusula barrava qualquer título novo com ≥3 tokens em comum com qualquer título antigo, independente do Jaccard. Nicho política RJ repete token o tempo todo → produtor parou de aprovar matéria nova.
- Prova: artigo novo do debate 2026 barrado por post de 2024 ("Debate eleitoral no Rio se destaca com massacre de Paes em Ramagem") via 3 tokens compartilhados.
- **Fix:** `if jac >= limiar_jac or (len(comuns) >= 3 and jac >= 0.40):`
- Backup NYC: `nucleo_dedup.py.bak_pre_dedup3tok_20260825`. Teste unitário pós-patch: duplicata real segue barrada; tema novo liberado.

## 2. Diagnóstico — causa raiz 2: hero de pessoa não achava foto
Sintoma: produtor aprovou 4-5 artigos/rodada, mas publicador ficava em `0 publicados`; artigos de pessoa (Siri, Couto, perfis) adiavam até `reprovado_sem_imagem` (6/6).

Investigação no `publicador.py`:
- `_buscar_hero()` (fase A) monta `termos = [visual_prompt] + termos_fallback` e busca no Commons (`commons.wikimedia.org/w/api.php`, `generator=search`, `gsrnamespace=6`, `gsrlimit=6`). Nunca incluía o NOME da pessoa do título.
- Guardião de relevância (`_entidades_titulo`, 13/08): se o título tem entidade, exige ≥1 entidade no nome do arquivo Commons. Como o termo de busca era cena ("câmeras de segurança e pessoas protestando"), nada casava.
- Confirmado via API: existem fotos CC de TODOS os políticos no Commons (Ricardo Couto 3600px CC BY-SA 4.0; William Siri; Benedita; Garotinho; Paes; Ruas; André Marinho).

**Fix 1 — `_termos_nome()` (novo helper em publicador.py):** extrai sequências de palavras capitalizadas consecutivas do título (ex.: "Ricardo Couto", "André Marinho") + nomes isolados ≥6 letras, com stoplist de substantivos comuns (Pesquisa, Programa, Sentinela, Senado, Governo, janeiro…). Retorna máx. 4 termos. Esses termos são somados aos `termos` da fase A, APÓS o visual_prompt. Sem nome de gente → retorna vazio e o fluxo é idêntico ao anterior (fail-soft).

**Fix 2 — rate-limit Wikimedia (HTTP 429):** durante os testes, downloads de `upload.wikimedia.org` a partir do NYC retornaram 429 (1979b, página "Wikimedia Error"). Era transitório/burst — o skip silencioso consumia tentativas de hero sem diagnóstico.
- Adicionado log `download hero falhou (status, bytes): arquivo` (antes era mudo).
- Adicionado `time.sleep(1.5)` antes de cada download (cortesia/espaçamento).
- Adicionado retry único: se 429, `time.sleep(6)` e tenta de novo uma vez.
- Verificado por IP: Dell 200 e NYC 200 quando não-burst.

Backup NYC: `publicador.py.bak_pre_termos_nome_20260825`.

## 3. Curadoria da fila (banco do site)
`/root/tematicos/agent_data/v4/riocarta/auditado.jsonl` — append de desfechos via lógica do `marcar_auditado` (uid + status + evento=desfecho + motivo), sem reescrever histórico. Backup: `auditado.jsonl.bak_pre_retomada_20260825`.

Reprovados (`rejeitado_curadoria_retomada`):
- ACM pré-candidato Republicanos (alucinação);
- Antônio Garotinho perfil (nome errado + datado);
- Eduardo Paes "Pré-Candidato à Prefeitura" (enquadramento errado);
- PSOL-Rede aprova Siri (duplicata de "lança Siri").

Fila pré-20/08 já estava 100% com desfecho. Restaram 12 aprovados de 25/08.

Zerei também o contador do artigo Sentinela em `hero_tentativas.json` (estava em 3 por causa dos 429, não por falha editorial). Backup: `hero_tentativas.json.bak_reset_20260825`.

## 4. Execução
`cd /root/tematicos/agentes_tematicos/v4 && /root/venv/bin/python3 orquestrador.py --site riocarta --sem-youtube`
(OB.S.: usar `/root/venv/bin/python3`; o python de sistema não tem `feedparser`.)

Rodada final publicou:
- hero Commons: `File:Desembargador Ricardo Couto de Castro como Governador do RJ.png` (CC BY 4.0), após juiz visual ✓ e confirmação ✓.
- `PUBLICADO: https://riocarta.com/blog/20260825-ricardo-couto-suspende-o-programa-sentinela-no-rio-de-janeir/`
- Commit repo `riocarta-v4`: `e8f9d9c post: Ricardo Couto suspende o Programa Sentinela no Rio de Janeiro` (push em origin/main).
- Verificado no ar: HTTP 200, `<title>` correto, hero em `/hero/…janeir.jpg`, 15 menções a "Ricardo Couto", categoria "Eleições 2026". Deploy Vercel levou ~2-3 min após o push (primeiros curls 404, depois 200).

## 5. Sincronização canônico
Dell canônico `Downloads/Antigravity Google/agentes_tematicos/v4/` (os `.py` são untracked no git — sync por cópia de arquivo):
- `scp nyc:.../publicador.py` e `scp nyc:.../nucleo_dedup.py` → canônico.
- Confirmed: canônico agora tem `len(comuns) >= 3 and jac >= 0.40` e `_termos_nome`.
- Backup canônico: `publicador.py.bak_pre_sync_20260825`, `nucleo_dedup.py.bak_pre_sync_20260825`.
- Validação: `python3 -c "import ast; ast.parse(...)"` OK nos dois.

## 6. Observações / pendências
- **Google Indexing 403:** "Failed to verify URL ownership" — indexação automática não ativa para riocarta.com (propriedade não verificada). Não bloqueia publicação.
- **Qualidade:** produtor ainda gera títulos "pré-candidato" desatualizados (as candidaturas já foram oficializadas). Rever prompt do produtor futuramente.
- **Melhoria futura:** banco de mídia local com retratos CC dos candidatos (já mapeados) para não depender do rate-limit da Wikimedia.
- **Lição:** 429 da Wikimedia era silencioso — sempre logar falha de download; e `len(comuns) >= 3` sem piso de Jaccard é armadilha em nicho repetitivo.

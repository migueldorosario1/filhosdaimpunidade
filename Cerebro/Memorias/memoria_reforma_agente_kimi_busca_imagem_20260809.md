# Memória — Reforma do agente Kimi busca-imagem (log técnico completo)

> **Data:** 2026-08-09 ~03:40–04:20 BRT · **Quem:** ZCode (Qwen 3.8 Token Plan) · Fórum: `Foruns/forum_reforma_agente_kimi_busca_imagem_20260809.md`
> Missão: enxurrada de e-mails "imagem não encontrada" → Miguel mandou achar as imagens,
> ampliar catálogo Flickr, escalonar rascunhos acumulados e **ensinar o sistema**.

## Arquivos tocados

| Arquivo | Ação |
|---------|------|
| `agentes_tematicos/v4/agente_kimi_busca_imagem.py` (475→~640 linhas) | REFORMADO (8 mudanças D1–D8) |
| `agentes_tematicos/v4/agent_data/kimi_busca_imagem/estado.json` | lido/auditado (78 itens: 14 resolvidos, 64 pendentes; distribuição tentativas: 41×6, 21×5, 13×1, 1×2, 1×3, 1×1) |
| `Projeto Cafezinho Agentes/root/flickr_live.py` | LIDO integralmente (412 linhas), NÃO alterado — plugado via import |
| WP API `controle.ocafezinho.com/wp-json` | auditoria drafts (read-only, credenciais do cofre em memória, nunca expostas) |
| NYC `/root/v4_vertical_draft_worker.py` | grep read-only via ssh (confirmação teto 1 draft/h/vertical) |

Backups: `agente_kimi_busca_imagem.py.bak_pre_reforma_20260809` + `estado.json.bak_pre_reforma_20260809`.

## Mudanças no código (detalhe)

1. **`_carregar_env()`** (generalizado do antigo `_smtp_cfg`, que agora o embrulha): lê
   `BASE/Projeto Cafezinho Agentes/root/.env.unificado` linha a linha, sem expor valores.
2. **`_flickr_api_search(termo, limite, api_key)`** — Flickr API oficial
   `flickr.photos.search`: `license="4,5,7,8,9,10"`, `sort=interestingness-desc`,
   `safe_search`, `extras="description,owner_name,tags,url_c,url_z,url_l"`,
   `format=json&nojsoncallback=1`. Candidatas ganham `_meta_texto = f"{tit} {desc} {tags}"`.
   `_flickr_scrape(termo, limite)` = scrape HTML antigo mantido como fallback sem chave.
   `buscar_flickr` prefere API quando `FLICKR_API_KEY` presente.
3. **`_match_pessoa`** — `if cand.get("official"): return True` (contas oficiais passam
   direto, como nos Planos C/D do flickr_live); texto de match inclui `_meta_texto`;
   passa a usar `_termos_pessoa(titulo)` em vez de `termos_de_busca`. Docstring rico com
   a lição anti-INPA 06/08 + reforma 09/08.
4. **`buscar_oficiais(titulo)`** — insere `BASE/Projeto Cafezinho Agentes/root` no
   sys.path, importa `flickr_live.buscar_foto_oficial(titulo, api_key=key)` (try/except
   total). Candidata devolvida: `{"url", "source": "flickr_oficial/<orgao>",
   "license_hint": "Flickr oficial (conta da entidade)", "attribution": ...,
   "_meta_texto": ..., "official": True}`.
5. **`MAX_POR_RODADA = 6`** (era 3).
6. **`_tokens_conteudo(titulo)`** — palavras de conteúdo sem STOP, **len ≥ 3** (mata o
   ruído "R" vindo de "R$").
7. **`termos_de_busca`** — fallback vira `" ".join(_tokens_conteudo(t))[:70]` (antes:
   título cru[:70] = RAIZ DO BUG); apelidos threshold **≥4** (era 5); cap **[:5]** (era 4).
8. **`_termos_pessoa(titulo)`** — exigência da guarda: sequências SEQ (≥2 maiúsculas
   seguidas) ou, na ausência, tokens isolados ≥4 começando em maiúscula. NUNCA título
   inteiro.
9. **`_expansao_ingles(titulo)`** — Gemini 2.5-flash via
   `nucleo_tematico.chaves.get_key("GEMINI_API_KEY")` (mesmo padrão nucleo_visao.py;
   `agente_roteador_llm.py` não existe localmente, só no NYC), máx 60 tokens, fail-silent
   "". Em `buscar_tudo`: adicionada quando `_termos_pessoa` não tem nome composto.
10. **`buscar_tudo`** — começa com `cands = buscar_oficiais(titulo)`; laço
    `for termo in termos[:5]` (flickr+wikimedia+cascata); dedup por url; guarda;
    **fallback por-token único PÓS-guarda**: se `out` vazio, busca cada token isolado de
    `_termos_pessoa` (≤3) em flickr+wikimedia e re-guarda item a item.

## Evidências de teste (saídas reais)

- `Friedrich Merz anuncia pacote de defesa na Alemanha` → 0 → **2–5 candidatas**
  (fonte flickr, contas/termos corretos).
- `China planeja usar cães robôs…` → 0 → **2 candidatas** (expansão EN funcionou).
- `Tarcísio libera R$ 14 bi para Cptm após greve; veja o que muda` → 0 → **7 candidatas**
  (`fallback por-token salvou 7 candidata(s)` no log; debug mostrou "Tarcísio Cptm"
  combinado = 0 hits, tokens isolados = hits reais).
- `PF acha Lira, Ramagem e aliados em rancho de advogado de fraudes no Inss` → 0 →
  **12 candidatas** (fallback por-token).
- Aviso `[flickr_live] ⚠️ Persistência indisponível (import robo_coleta_imagens)` é
  BENIGNO localmente (módulo só existe no NYC; flickr_live embrulha em try/except).
- py_compile verde após cada edição.

## Iterações de debug que levaram ao fallback por-token

1. Reteste pós-D1..D8: Tarcísio/PF-Lira ainda 0 → debug por consulta:
   `buscar_flickr("Tarcísio Cptm")=0`, `buscar_wikimedia(...)=0`, mas
   `buscar_flickr("Tarcísio de Freitas")=3+3`, `buscar_flickr("Arthur Lira")=3+2`
   → fontes tratam consulta multi-palavra como AND implícito.
2. Primeira versão do fallback (`if not cands`) falhou porque a expansão EN deixava
   `cands` não-vazio com ruído que a guarda derrubava → versão final dispara quando
   **nada passa a guarda**, não quando não há candidatas.

## Auditoria WP (API, creds do cofre, 04:05)

- `users/me` → 200, user `redacao-nova` (auth WP_USER_CAFEZINHO/WP_APP_PASSWORD ok).
- 590 drafts · 388 com `featured_media` · **202 sem** (amostra: 263768 Atlas/Bloomberg
  31/07, 263660 Jaques Wagner 31/07, 263427 Tarcísio×Haddad 29/07 … até 246847 14/05).
  Refugo incluído (títulos vazios 257393/255785, "RASCUNHO TESTE Codex" 255107,
  "Pauta vetada" 250938).
- Detalhe de rede: primeiro GET com per_page=25 deu timeout/HTTP 500; funcionou com
  `trust_env=False` + proxies None (mesmo truque do `_get` do agente) + per_page=10 + retry.

## Publicação paulatina

- NYC `v4_vertical_draft_worker.py` linha 2: `"""Cria no máximo um draft/hora por vertical
  usando o redator real de produção."""` — escalonamento nativo (Miguel 27/07); crons
  atuais das verticais geo/ciência estão `SUBSTITUIDO_KIMI_20260727_30MIN` (comentados,
  pipeline unificado 30 min no lugar).
- §86 exige featured_media > 0 → publicação só acontece quando o agente/fluxo anexa
  imagem; portanto o backlog sai "paulatino" por construção. Nada a criar.

## Cron (produção)

`*/30 * * * * /usr/bin/flock -n /tmp/kimi_busca_imagem.lock <pyenv python>
agentes_tematicos/v4/agente_kimi_busca_imagem.py` — python relê o arquivo a cada
execução, então a reforma já está AO VIVO desde a rodada ~04:00/04:30 sem restart.
Alerta (Telegram+e-mail "🖼️ Kimi: imagem não encontrada") dispara na tentativa 6
(ALERTA_EM=6) e a cada 12 (REALERTA_A_CADA=12) — era isso que inundava o Miguel;
tendência é cessar conforme a queima do backlog resolver os itens.

## Estado da missão (p/ próxima conversa)

- **Aconteceu:** diagnóstico completo, reforma D1–D8 aplicada+testada, backups, fórum+memória.
- **Falta:** confirmar 2–3 rodadas do cron com RESOLVIDOs reais (ingestão NYC/Tencent/
  espelho local); se itens persistirem impossíveis após a reforma, considerar catálogo
  extra (Agência Brasil CC BY foi cogitada no flickr_live como adaptador futuro).
- **Preciso do Miguel:** nada; se ele der dica de fonte p/ item específico, adicionar.

## Reversão

`cp agente_kimi_busca_imagem.py.bak_pre_reforma_20260809 agente_kimi_busca_imagem.py`
(+ idem estado.json). Cron segue sem mudança de interface.

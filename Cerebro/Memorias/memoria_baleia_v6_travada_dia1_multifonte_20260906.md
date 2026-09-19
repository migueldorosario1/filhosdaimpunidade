# Memória técnica — /v6/baleia travada no dia 01/09: cura multi-fonte no painel (06/09/2026)

**Sessão:** ZCode Dell, Qwen3.8-Max · ordem do Miguel ~22:52 BRT ("a edição da baleia azul no v6 está travada no dia 1. corrige isso")
**Fórum-irmão:** `Foruns/forum_baleia_v6_travada_dia1_multifonte_20260906.md`

## Diagnóstico (linha do tempo da investigação)

1. `curl http://43.156.151.165/v6/baleia` → `<title>Boletim Baleia Azul — 01/09/2026 (tarde) — CCTV V6</title>` (travado confirmado; hoje 06/09 22:52).
2. Dell `~/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/baleia_azul/` → boletins `_manha`/`_tarde` até `20260906_tarde.md` (mtime 06/09 19:45). Produção editorial SAUDÁVEL (chefe, turnos 07:10/19:15, Edição 37 fechada 19:35).
3. Painel Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`:
   - linha 71: `BASE_DIR = Path(os.environ.get("CCTV_BASE", "/home/ubuntu/cafezinho/Projeto Cafezinho Agentes"))`
   - linha ~1204 (`pagina_baleia`): `arquivos = sorted(glob.glob(str(BASE_DIR / "boletim_baleia_azul_*.md")), reverse=True)` — pega `arquivos[0]`.
   - `_baleia_lista` (histórico) e `pagina_baleia_edicao` (rota por nome): mesma fonte única `BASE_DIR`.
   - Título: primeira linha `# ` do md; boletins novos não têm `# ` (1ª linha = "Boletim Baleia Azul — Edição 37 · tarde · ...").
4. `ls` BASE_DIR Tencent: último `boletim_baleia_azul_20260901.md`, mtime **01/09 19:30** — série diária 19:30 desde 16/08 (horário do wrapper Dell). Monitor linha 62: unificação Baleia→DSN Chefe 01/09 21:15, **"wrapper Dell OFF (backup crontab)"** → causa raiz: quem alimentava BASE_DIR foi desligado na unificação; painel nunca foi repontado para a ponte.
5. Fontes frescas na Tencent (find): `/home/ubuntu/cafezinho/v6_data/foruns/ponte_laura_completa/baleia_azul/` (FORUNS_DIR, linha 75 do painel; `20260906_tarde.md` mtime 19:45) e `/home/ubuntu/cerebro-miguel/cerebro/Foruns/ponte_laura_completa/baleia_azul/` (clone git; FETCH_HEAD 06/09 23:30, commit f9b069e06 23:26 -0300).
6. Conflitos (§112): nenhuma sessão ativa em `painel_cctv_v6.py` no monitor (ativas: Astra Drive fase 3, Moka Play Store, forense 269169 — outros arquivos).

## O patch (aplicado via `/tmp/patch_baleia_v6.py`, replace exato com assert de unicidade)

Backup: `painel_cctv_v6.py.bak_pre_baleia_ponte_20260906` (cp -a antes).

1. **Helpers novos antes de `def pagina_baleia()`:**
   - `BALEIA_DIR_EXTRA = os.environ.get("CCTV_BALEIA_DIR", "")` (override opcional).
   - `_baleia_dirs()` → [extra?] + `FORUNS_DIR/ponte_laura_completa/baleia_azul` + `cerebro-miguel/cerebro/Foruns/ponte_laura_completa/baleia_azul` + `BASE_DIR`, filtrados por `is_dir()`.
   - `_baleia_chave(p)` → `(data 20\d{6}, nome)` p/ ordenação.
   - `_baleia_turno(nome)` → sufixo `_manha`/`_tarde`/`_extraordinaria`; sem sufixo = "tarde" (legado noturno).
   - `_baleia_arquivos()` → glob em todos os dirs, **dedupe por (data, turno)** com prioridade para o dir mais cedo na lista (ponte > legado), ordenado `(data, nome)` reverso (`_tarde` > `_manha` > sem-sufixo no mesmo dia; datas ISO funcionam em ordem lexicográfica).
   - `_baleia_titulo(md)` → linha `# ` se houver; senão 1ª linha não vazia.
2. **`pagina_baleia`**: `arquivos = _baleia_arquivos()`; `bp = arquivos[0]`; `titulo_ed = _baleia_titulo(md) or titulo_ed`.
3. **`_baleia_lista`**: itera `_baleia_arquivos()`; data ganha ` · manha|tarde`; título via `_baleia_titulo(...)[:100]`.
4. **`pagina_baleia_edicao`**: `bp = next((d/f"{nome}.md" for d in _baleia_dirs() if existe), None)`; `titulo = _baleia_titulo(md) or nome`. Regex de segurança `[a-z0-9_]+` já aceitava os nomes novos.

## Execução e provas

```
scp /tmp/patch_baleia_v6.py tencent:/tmp/ → cp -a backup → python3 patch (4× OK + PATCH APLICADO)
/usr/bin/python3 -m py_compile painel_cctv_v6.py → OK (SyntaxWarning \w linha 7244 PRÉ-EXISTENTE, _AOVIVO_HTML, sem relação)
systemctl restart cctv-v6 → active; GET 127.0.0.1:8084/baleia → 200 em 1,45s
```

- Interna: `<title>Boletim Baleia Azul — Edição 37 · tarde · domingo, 6 de setembro de 2026 · fechada às 19:35 — CCTV V6</title>`; `Fonte: boletim_baleia_azul_20260906_tarde.md`.
- Externa (Dell→43.156.151.165/v6/baleia): mesmo título; corpo presente (grep "O domingo em que a produção virou a curva do público" = 1, "8.261" = 1, "Edição mais recente" = 1).
- `/v6/baleia-historico`: "62 edições arquivadas"; topo `20260906_tarde, 20260906_manha, 20260905_tarde, 20260905_manha, ...`.
- Edições: `20260906_manha` = 200 · `20260815_extraordinaria` = 200 (BASE_DIR legado segue alcançável) · `20260820` = 200.

## Rollback (1 comando)

```
ssh tencent 'cp -a /home/ubuntu/cafezinho/v6/painel_cctv_v6.py.bak_pre_baleia_ponte_20260906 /home/ubuntu/cafezinho/v6/painel_cctv_v6.py && sudo systemctl restart cctv-v6'
```

## Armadilhas registradas (reuso)

1. **Desligar um emissor/wrapper exige repontar os leitores:** o wrapper Dell não só enviava e-mail/Telegram — era o transporte que fazia o boletim chegar ao dir que o painel lia. Desligou-se o transporte (01/09) sem mover o consumidor → página congelada 5 dias sem alarme.
2. **Boletim novo sem heading `# `:** qualquer extrator de título por heading markdown falha silenciosamente (fallback para genérico). Format novo da ponte = 1ª linha em texto puro.
3. **Ordenação lexicográfica de edições 2×/dia:** datas ISO + sufixos `_manha` < `_tarde` ordenam certo em string; arquivo legado sem sufixo (`.` < `_`) perde para `_manha` do mesmo dia — dedupe por (data, turno) resolve.
4. Página congelada SEM erro (200 + conteúdo velho) não dispara healthcheck — vigília de página precisa conferir DATA do conteúdo, não só status HTTP.

## Pendência de observação

Se o `v6_data/foruns` parar de receber a ponte, o clone `cerebro-miguel` (2ª fonte, pull fresco verificado) cobre — mas vale confirmar na edição da manhã de 07/09 que a página virou sozinha.

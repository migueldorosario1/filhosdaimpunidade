# -*- coding: utf-8 -*-
# V41_JUIZ_QUALIDADE_20260907 — patch do v41_ciclo.py (2 juízes de qualidade)
# + config editável dados/juiz_qualidade.json + padrão vivo dados/PADRAO_CURADORIA_QUALIDADE.md
import json, shutil, py_compile, sys

P = "/root/v4_labs/codigo/v41_ciclo.py"
shutil.copy2(P, P + ".bak_pre_juiz_qualidade_20260907")
src = open(P, encoding="utf-8").read()

FUNCS = '''
# ============================================================================
# V41_JUIZ_QUALIDADE_20260907 (ordem Miguel 07/09 ~00:5x: "cria um juiz de
# qualidade... dois juizes na verdade, um antes de escrever o artigo... tem que
# dar nota para varias coisas: clareza, interesse para o leitor brasileiro,
# importancia global, importancia para a economia mundial... ranking complexo...
# bota um DeepSeek, bota o Qwen, uma inteligencia razoavel, nao precisa mais
# caro"). Padrao de interesse: home da Metropolis e da revista Forum (ordem
# Miguel 06/09). JUIZ 1 = PAUTA (antes da tese frontier — mata o lixo no
# nascedouro e economiza o gpt-5.6-sol); JUIZ 2 = TEXTO final (antes do FC
# sonnet e da insercao de metas — mata metalinguagem/texto sem cena).
# Configuracao editavel sem deploy: dados/juiz_qualidade.json; criterio vivo:
# dados/PADRAO_CURADORIA_QUALIDADE.md. FAIL-CLOSED: sem juiz nao escreve
# (mesma filosofia da tese).
# ============================================================================
_JUIZ_CFG_PADRAO = {
    "ativo": True,
    "modelo_deepseek": "deepseek-chat",
    "modelo_qwen": "qwen-plus",
    "pesos": {"clareza": 1.0, "interesse_br": 2.0, "importancia_global": 1.0,
              "importancia_economia": 0.8, "audiencia": 1.5, "encaixe_vertical": 1.5,
              "linha_casa": 1.2},
    "min_total": 6.0, "min_interesse_br": 5, "min_encaixe": 5,
    "juiz2_min_total": 6.0, "juiz2_min_clareza": 5,
}


def _juiz_cfg() -> dict:
    cfg = dict(_JUIZ_CFG_PADRAO)
    try:
        _c = json.loads((ROOT / "dados" / "juiz_qualidade.json").read_text(encoding="utf-8"))
        if isinstance(_c, dict):
            cfg.update(_c)
    except Exception:
        pass
    return cfg


def _juiz_llm(env: dict, system: str, user: str, site: str = "juiz_qualidade"):
    """Cascata barata do juiz: DeepSeek chat -> Qwen plus -> cadeia verifier (ultima linha)."""
    import requests
    import time as _time
    cfg = _juiz_cfg()
    qwen_base = (env.get("QWEN_BASE_URL", "") or "https://dashscope.aliyuncs.com/compatible-mode/v1").rstrip("/")
    alvos = [
        ("deepseek", "https://api.deepseek.com/v1/chat/completions",
         env.get("DEEPSEEK_API_KEY", ""), str(cfg.get("modelo_deepseek") or "deepseek-chat")),
        ("qwen", qwen_base + "/chat/completions",
         env.get("QWEN_API_KEY", "") or env.get("QWEN_API_KEY_2", ""), str(cfg.get("modelo_qwen") or "qwen-plus")),
    ]
    for provedor, url, key, modelo in alvos:
        if not key or not url:
            continue
        _t0 = _time.time()
        try:
            s = requests.Session(); s.trust_env = False
            r = s.post(url, headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
                       json={"model": modelo, "max_tokens": 2000, "temperature": 0.2,
                             "messages": [{"role": "system", "content": system},
                                          {"role": "user", "content": user}]}, timeout=75)
            r.raise_for_status()
            _j = r.json(); _uso = _j.get("usage") or {}
            txt = _j["choices"][0]["message"]["content"]
            m = re.search(r"\\{.*\\}", txt, re.S)
            if m:
                _tel(site, provedor, modelo, "ok",
                     int(_uso.get("prompt_tokens") or 0), int(_uso.get("completion_tokens") or 0),
                     int((_time.time() - _t0) * 1000))
                return json.loads(m.group(0)), provedor + ":" + modelo
            _tel(site, provedor, modelo, "sem_json", 0, 0, int((_time.time() - _t0) * 1000))
        except Exception as _e:
            try:
                _tel(site, provedor, modelo, "erro", duration_ms=int((_time.time() - _t0) * 1000),
                     error_class=type(_e).__name__)
            except Exception:
                pass
    try:
        import importlib.util as _ilu
        _sp = _ilu.spec_from_file_location("v4wj", "/root/v4_vertical_draft_worker.py")
        _wj = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_wj)
        v = _wj._verifier_llm_json(system, user, env, timeout=90, site=site + "_fb")
        if isinstance(v, dict) and v.get("notas"):
            return v, "cadeia_verifier"
    except Exception:
        pass
    return None, None


_JUIZ_CRITERIOS = (
    "CRITERIOS (nota 0-10 em cada): "
    "clareza (o fato e compreensivel para o leitor comum, sem jargao gratuito); "
    "interesse_br (interesse do leitor BRASILEIRO: protagonista brasileiro, impacto no Brasil, "
    "ou relevancia global que repercute aqui); "
    "importancia_global (peso geopolitico/mundial do fato); "
    "importancia_economia (peso para a economia mundial e brasileira); "
    "audiencia (potencial de clique e conversa — a home da Metropolis ou da revista Forum "
    "estamparia isso?); "
    "encaixe_vertical (o tema pertence MESMO a secao indicada? tenis em economia = 0, "
    "futebol em meio_ambiente = 0); "
    "linha_casa (aderencia a linha progressista/soberanista: soberania, multipolaridade, "
    "direito internacional, direitos do trabalhador, critica a especulacao; pautas afirmativas "
    "BRICS/cooperacao tambem pontuam bem)."
)


def _juiz_qualidade(env: dict, vertical: str, titulo: str, texto: str, modo: str = "pauta") -> dict:
    cfg = _juiz_cfg()
    if not cfg.get("ativo", True):
        return {"aprova": True, "motivo": "juiz_desativado", "notas": {}, "total": None, "modelo": None}
    padrao = ""
    try:
        _p = ROOT / "dados" / "PADRAO_CURADORIA_QUALIDADE.md"
        if _p.exists():
            padrao = ("\\n\\nPADRAO DE QUALIDADE DA CASA (obedecer):\\n"
                      + _p.read_text(encoding="utf-8").strip()[:4000])
    except Exception:
        pass
    pesos = cfg.get("pesos") or _JUIZ_CFG_PADRAO["pesos"]
    saida_json = ('Responda APENAS JSON: {"notas": {"clareza": n, "interesse_br": n, '
                  '"importancia_global": n, "importancia_economia": n, "audiencia": n, '
                  '"encaixe_vertical": n, "linha_casa": n}, "motivo": "uma frase curta"}')
    if modo == "texto":
        system = (
            "Voce e o JUIZ DE QUALIDADE do TEXTO FINAL de um portal de noticias brasileiro "
            "(O Cafezinho — jornalismo progressista premium; padrao de qualidade: Metropolis e "
            "revista Forum). " + _JUIZ_CRITERIOS + " "
            "REGRAS DURAS: texto que e PARECER/metalinguagem (relatorio sobre a propria materia, "
            "titulo-status como 'Artigo revisado') = TODAS as notas 0; texto sem cena, sem dado "
            "concreto, sem consequencia material para o leitor = clareza e audiencia baixas; "
            "clickbait ou frase-trailer (anuncia sem entregar) = linha_casa baixa. " + saida_json)
        user = ("SECAO/VERTICAL: " + str(vertical) + "\\nTITULO: " + str(titulo)
                + "\\n\\nTEXTO (inicio):\\n" + str(texto)[:3500])
        minimo = float(cfg.get("juiz2_min_total", 6.0))
        extras = {"clareza": float(cfg.get("juiz2_min_clareza", 5))}
    else:
        system = (
            "Voce e o JUIZ DE QUALIDADE da CURADORIA de um portal de noticias brasileiro "
            "(O Cafezinho — jornalismo progressista premium; padrao de interesse: a home da "
            "Metropolis e da revista Forum). Recebe uma PAUTA CANDIDATA e a secao do site. "
            + _JUIZ_CRITERIOS + " "
            "REGRAS DURAS: esporte estrangeiro sem brasileiro e sem futebol = interesse_br no "
            "maximo 3 (torneio dos EUA sem brasileiro nao interessa); materia de servico, "
            "listicle de vendas, loteria, guia de transito, dica de compra = audiencia no "
            "maximo 2; pauta de tecnologia em lingua estrangeira so vale se tiver impacto "
            "global/brasileiro real (IA, grandes plataformas, geopolitica dos chips) — "
            "resumo de apps, review de software estrangeiro, curiosidade de outro pais = "
            "interesse_br no maximo 2; pauta fora da secao indicada = encaixe_vertical baixo. "
            + saida_json)
        user = ("SECAO/VERTICAL: " + str(vertical) + "\\nTITULO DA PAUTA: " + str(titulo)
                + "\\n\\nINICIO DA NOTICIA:\\n" + str(texto)[:2500])
        minimo = float(cfg.get("min_total", 6.0))
        extras = {"interesse_br": float(cfg.get("min_interesse_br", 5)),
                  "encaixe_vertical": float(cfg.get("min_encaixe", 5))}
    verd, modelo = _juiz_llm(env, system + padrao, user, site="juiz_qualidade_" + modo)
    if not isinstance(verd, dict):
        return {"aprova": False, "motivo": "juiz_indisponivel", "notas": {}, "total": None, "modelo": None}
    notas_raw = verd.get("notas") if isinstance(verd.get("notas"), dict) else {}
    try:
        notas = {k: max(0.0, min(10.0, float(notas_raw.get(k, 0) or 0))) for k in pesos}
    except Exception:
        notas = {k: 0.0 for k in pesos}
    soma_p = float(sum(pesos.values()) or 1.0)
    total = round(sum(notas[k] * float(pesos[k]) for k in pesos) / soma_p, 2)
    aprova = total >= minimo and all(notas.get(k, 0) >= v for k, v in extras.items())
    motivo = str(verd.get("motivo") or "").strip()[:120] or ("aprovada" if aprova else "nota_abaixo_do_minimo")
    return {"aprova": bool(aprova), "motivo": motivo, "notas": notas, "total": total, "modelo": modelo}


'''

A1 = "def _tese_dinamica(env: dict, titulo: str, conteudo: str) -> dict:"
assert src.count(A1) == 1, "A1 nao encontrado"
src = src.replace(A1, FUNCS.lstrip("\n") + A1)

A2 = '''    row = None; cur = None
    for cand in rows:
        c = None
        try:
            c = _tese_dinamica(env, str(cand["title"]), str(cand["text_content"] or "")[:5000])
        except Exception as e:
            c = {"ok": False, "motivo": f"erro:{type(e).__name__}"}'''
assert src.count(A2) == 1, "A2 nao encontrado"
R2 = '''    row = None; cur = None
    _jq_hist = []; _jq_ok = None
    for cand in rows:
        c = None
        # JUIZ DE QUALIDADE 1 (pauta, antes da tese frontier): fail-closed — sem nota boa,
        # a pauta nem chega ao gpt-5.6-sol (economiza e mata o lixo no nascedouro).
        try:
            _jq = _juiz_qualidade(env, a.vertical, str(cand["title"]),
                                  str(cand["text_content"] or "")[:2500], modo="pauta")
        except Exception as _e:
            _jq = {"aprova": False, "motivo": "juiz_erro:" + type(_e).__name__, "notas": {}, "total": None, "modelo": None}
        _jq_hist.append({"pauta": str(cand["title"])[:70], "total": _jq.get("total"),
                         "aprova": bool(_jq.get("aprova")), "motivo": str(_jq.get("motivo") or "")[:60],
                         "notas": _jq.get("notas") or {}})
        if not _jq.get("aprova"):
            c = {"ok": False, "motivo": "juiz_qualidade:" + str(_jq.get("motivo") or "reprovada")[:60]}
        else:
            _jq_ok = _jq
            try:
                c = _tese_dinamica(env, str(cand["title"]), str(cand["text_content"] or "")[:5000])
            except Exception as e:
                c = {"ok": False, "motivo": f"erro:{type(e).__name__}"}'''
src = src.replace(A2, R2)

A3 = '''    saida = {"ok": True, "ts": ts, "vertical": a.vertical, "pauta": titulo[:80], "item_key": row["item_key"][:16]}'''
assert src.count(A3) == 1, "A3 nao encontrado"
R3 = A3 + '''
    if _jq_ok:
        saida["juiz_qualidade"] = {k: _jq_ok.get(k) for k in ("notas", "total", "aprova", "motivo", "modelo")}
    saida["juiz_historico"] = _jq_hist[:8]'''
src = src.replace(A3, R3)

A4 = '''    # 3) metas 4.1 + FC-2 websearch
    if pid:'''
assert src.count(A4) == 1, "A4 nao encontrado"
R4 = '''    # JUIZ DE QUALIDADE 2 (texto final, antes do FC sonnet e das metas): mata metalinguagem
    # e texto sem cena/dado. Reprovou = apaga o rascunho recem-criado (mesmo padrao da
    # recusa do redator) e devolve o diagnostico com notas no artefato do ciclo.
    if pid:
        try:
            _j2 = _juiz_qualidade(env, a.vertical, str(post.get("title") or titulo),
                                  str(post.get("content") or "")[:3500], modo="texto")
        except Exception as _e:
            _j2 = {"aprova": False, "motivo": "juiz2_erro:" + type(_e).__name__, "notas": {}, "total": None, "modelo": None}
        saida["juiz_qualidade2"] = {k: _j2.get(k) for k in ("notas", "total", "aprova", "motivo", "modelo")}
        if not _j2.get("aprova"):
            try:
                import requests as _rq3
                _se3 = _rq3.Session(); _se3.trust_env = False
                _se3.delete(env["WP_SITE"].rstrip("/") + "/wp-json/wp/v2/posts/" + str(pid),
                            auth=(env["WP_USER"], env["WP_PASS"]), params={"force": True}, timeout=30)
                saida["juiz2_apagado"] = pid
            except Exception as _e:
                saida["juiz2_apagar_erro"] = type(_e).__name__
            saida["post_id"] = None
            saida["status"] = "juiz_qualidade2_reprovou"
            _d = ROOT / "dados" / "v41_ciclo"; _d.mkdir(parents=True, exist_ok=True)
            (_d / f"{ts}.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
            print(json.dumps(saida, ensure_ascii=False)[:900])
            return 0
    # 3) metas 4.1 + FC-2 websearch
    if pid:'''
src = src.replace(A4, R4)

open(P, "w", encoding="utf-8").write(src)
py_compile.compile(P, doraise=True)
print("PATCH + PY_COMPILE OK")

CFG = {
    "ativo": True,
    "modelo_deepseek": "deepseek-chat",
    "modelo_qwen": "qwen-plus",
    "pesos": {"clareza": 1.0, "interesse_br": 2.0, "importancia_global": 1.0,
              "importancia_economia": 0.8, "audiencia": 1.5, "encaixe_vertical": 1.5,
              "linha_casa": 1.2},
    "min_total": 6.0, "min_interesse_br": 5, "min_encaixe": 5,
    "juiz2_min_total": 6.0, "juiz2_min_clareza": 5,
}
open("/root/v4_labs/dados/juiz_qualidade.json", "w", encoding="utf-8").write(
    json.dumps(CFG, ensure_ascii=False, indent=1))

PADRAO = '''# PADRÃO DE CURADORIA E QUALIDADE — O CAFEZINHO (vivo, 07/09/2026)

Ordem do Miguel (06-07/09/2026): "tem que ser coisa legal; fala para olhar lá os
Metrópoles, a revista Fórum — pegar o padrão ali, o padrão está ali". Este arquivo
é lido pelo JUIZ DE QUALIDADE do ciclo V4.1 (juiz 1 = pauta, juiz 2 = texto) e
pode ser editado sem deploy.

## O que entra (nesta ordem de prioridade)
1. BRASIL PRIMEIRO: política nacional, economia que mexe no bolso, Escândalos e
   investigações (Vorcaro/Master, Nikolas, emendas), eleições 2026, Lula e governo.
2. GEOPOLÍTICA COM REPERCUSSÃO: guerras, sanções, BRICS/SCO, multipolaridade,
   petróleo, tarifas, China/Rússia/Irã vs EUA.
3. TECNOLOGIA/IA QUE MUDA A VIDA: grandes modelos, regulação, geopolítica dos
   chips, plataformas, impacto no trabalho — SEMPRE com gancho humano ou
   convergência com geopolítica/economia (EMU-9). Nada de nicho técnico seco.
4. ESPORTE: futebol brasileiro e Seleção primeiro; europeu e brasileiros no
   exterior em seguida; SEMPRE na vertical esporte (EMU-10).
5. CULTURA/SERVIÇO COM PESO: Rock in Rio, carnaval, grandes estreias — só quando
   virarem fato nacional.

## O que NÃO entra (o juiz reprova)
- Matéria de serviço/listicle: "como achar iPhone barato", "11 produtos da
  Shopee", loteria, guia de trânsito, dica de compra.
- Esporte estrangeiro sem brasileiro e sem futebol (US Open, boxe internacional,
  ligas asiáticas).
- Tecnologia estrangeira de nicho: resumo de apps de outro país, review de
  software/library, lista de players de anime, curiosidade sem impacto.
- Pauta fora da seção (tênis em economia, futebol em meio ambiente).
- Metalinguagem: parecer/relatório sobre a própria matéria (todas as notas 0).
- Texto sem cena, sem dado concreto, sem consequência material para o leitor.
- Clickbait e frase-trailer (EMU-7).

## Ranking complexo (notas 0-10, pesos vivos em juiz_qualidade.json)
clareza · interesse do leitor brasileiro (peso maior) · importância global ·
importância para a economia · potencial de audiência (régua Metrópoles/Fórum) ·
encaixe na vertical · aderência à linha da casa.

## Régua de audiência
A pergunta do juiz: "a home da Metrópoles ou da revista Fórum estamparia isso
agora?" Se a resposta é não, a nota de audiência cai e a pauta não vira artigo.
'''
open("/root/v4_labs/dados/PADRAO_CURADORIA_QUALIDADE.md", "w", encoding="utf-8").write(PADRAO)
print("CONFIG + PADRAO OK")

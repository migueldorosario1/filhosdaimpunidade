#!/usr/bin/env python3
"""
ciclo_v42.py - Orquestrador do Ciclo Completo do Agente V4.2 de Economia
=========================================================================
Pipeline: coleta (opcional) → gráficos dark-mode → auditoria visual (LLM) →
redação "Texto Música" (PT + EN) → publicação no espelho cafezinho.news.

Uso:
  python3 ciclo_v42.py --tema comercio --publicar
  python3 ciclo_v42.py --tema auto                # só gera e registra (draft local)
  python3 ciclo_v42.py --coletar --tema comercio --publicar

Regras de segurança:
  - Gráfico só entra na matéria se audit_state == approved (fail-closed).
  - Publicação só ocorre com --publicar; padrão é dry-run local.
  - Idempotência: mesma matéria (text_sha256) nunca é republicada.
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
CODIGO_DIR = os.path.dirname(BASE_DIR)  # .../v4_labs/codigo
if CODIGO_DIR not in sys.path:
    sys.path.insert(0, CODIGO_DIR)
V4_LABS_DIR = os.path.dirname(CODIGO_DIR)  # .../v4_labs
if V4_LABS_DIR not in sys.path:
    sys.path.insert(0, V4_LABS_DIR)

from env_loader import carregar_env

carregar_env()

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [CICLO-V42] %(message)s')

GERADOS_DIR = os.path.join(BASE_DIR, "gerados")
CICLOS_DIR = os.path.join(GERADOS_DIR, "ciclos")
GSN_DIR = os.path.join(GERADOS_DIR, "gsn")


def _atomic_json(path: str, payload: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def etapa_graficos(serie_graficos: List[Dict[str, Any]], limite: int = 3) -> List[Dict[str, Any]]:
    """Gera PNG + manifesto para cada série planejada e audita com visão LLM."""
    from graficos_economia_v4 import GeradorGraficosEconomia, ErroGrafico
    gerador = GeradorGraficosEconomia()

    provider = None
    try:
        from codigo.media_vision_providers import create_media_vision_provider
        provider = create_media_vision_provider()
        logging.info("Provider visual carregado para auditoria.")
    except Exception as e:
        logging.warning(f"Sem provider visual disponível ({e}) — auditoria visual ficará indisponível.")

    from auditor_graficos_v4 import audit_graph

    resultados = []
    for plano in serie_graficos[:limite]:
        fonte, serie_id = plano["fonte"], plano["serie_id"]
        try:
            manifesto = gerador.generate(
                fonte, serie_id,
                limit=plano.get("limit", 24),
                chart_type=plano.get("tipo", "line"),
            )
        except (ErroGrafico, FileNotFoundError) as e:
            logging.warning(f"Gráfico {fonte}/{serie_id} não gerado: {e}")
            continue

        png_path = manifesto["chart"]["png"]
        manifest_path = manifesto["manifest"]
        audit_path = str(png_path).replace(".png", ".audit.json")

        audit_state, audit_provider = "sem_auditoria", ""
        if provider is not None:
            try:
                recibo = audit_graph(
                    manifest_path=manifest_path,
                    png_path=png_path,
                    db_path=str(gerador.db_path),
                    provider=provider,
                    receipt_path=audit_path,
                )
                audit_state = recibo["state"]
                audit_provider = str(recibo["visual"].get("provider", ""))
            except Exception as e:
                audit_state = "human_review"
                logging.warning(f"Auditoria visual falhou para {png_path}: {e}")

        resultados.append({
            "fonte": fonte,
            "serie_id": serie_id,
            "legenda": plano.get("legenda", manifesto["chart"]["serie_nome"]),
            "png_path": png_path,
            "manifest_path": manifest_path,
            "audit_path": audit_path,
            "png_sha256": manifesto["hashes"]["png_sha256"],
            "audit_state": audit_state,
            "audit_provider": audit_provider,
            "aprovado": audit_state == "approved",
        })
        logging.info(f"Gráfico {fonte}/{serie_id}: auditoria={audit_state}")
    return resultados


def etapa_redacao(
    tema: str,
    titulos_evitar: Optional[List[str]] = None,
    dias_desde_ultima: Optional[Dict[str, int]] = None,
) -> Dict[str, Any]:
    from redator_economia_v4 import RedatorTextoMusica, jaccard_palavras
    redator = RedatorTextoMusica()

    # REFORMA 03/09 (auditoria DSC): gate anti-repetição de título — o LLM recebe
    # os títulos recentes (regra 16) e, se ainda assim produzir eco ≥0.60 de
    # Jaccard, UMA regeneração com os títulos parecidos destacados; eco persistente
    # bloqueia a publicação (motivo "titulo_repetido"). Defeito real que originou o
    # gate: posts 400178 (29/08) e 400265 (02/09) com título IDÊNTICO.
    redacao = redator.redigir(
        tema=tema, titulos_evitar=titulos_evitar, dias_desde_ultima=dias_desde_ultima)
    if not titulos_evitar:
        redacao["titulo_similaridade_max"] = 0.0
        redacao["titulo_similar_de"] = ""
        return redacao

    def _pior_titulo(titulo: str) -> tuple:
        melhor = (0.0, "")
        for t in titulos_evitar:
            j = jaccard_palavras(titulo, t)
            if j > melhor[0]:
                melhor = (round(j, 3), t)
        return melhor

    sim, pior = _pior_titulo(redacao["titulo_pt"])
    if sim >= 0.60:
        logging.warning(f"Gate título: eco {sim:.2f} com '{pior}' — regenerando 1×.")
        redacao = redator.redigir(
            tema=tema, titulos_evitar=[pior] + titulos_evitar[:5],
            dias_desde_ultima=dias_desde_ultima)
        sim, pior = _pior_titulo(redacao["titulo_pt"])
    redacao["titulo_similaridade_max"] = sim
    redacao["titulo_similar_de"] = pior if sim >= 0.60 else ""
    if sim >= 0.60:
        logging.warning(f"Gate título: eco persistente {sim:.2f} — publicação será bloqueada.")
    return redacao


def _historico_publicacoes(limite: int = 40) -> Dict[str, Any]:
    """REFORMA 03/09: histórico das últimas matérias PUBLICADAS (pt) para os gates:
    títulos recentes (anti-repetição), dias sem publicar por tese (rodízio) e
    data_referencia máxima já usada por tese (frescor de dados)."""
    from banco_producao_v4 import BancoProducaoV42
    from datetime import datetime, timezone, date

    banco = BancoProducaoV42()
    materias = [
        m for m in banco.listar_materias(limite=limite)
        if m.get("idioma") == "pt" and m.get("status_pipeline") == "publicado"
    ]
    titulos = [m["titulo"] for m in materias]

    hoje = datetime.now(timezone.utc).date()
    dias_sem: Dict[str, int] = {}
    data_max_por_tese: Dict[str, str] = {}
    for m in materias:
        tese = m.get("tese_id") or ""
        if not tese:
            continue
        try:
            d = date.fromisoformat(str(m.get("publicado_em") or m.get("criado_em"))[:10])
            dias = (hoje - d).days
            if tese not in dias_sem or dias > dias_sem[tese]:
                dias_sem[tese] = dias
        except ValueError:
            dias_sem.setdefault(tese, 9999)
        # data_referencia máxima já PUBLICADA por tese (frescor)
        for f in banco.fontes_da_materia(m["id"]):
            dr = str(f.get("data_referencia") or "")[:10]
            if dr and dr > data_max_por_tese.get(tese, ""):
                data_max_por_tese[tese] = dr
    return {
        "titulos": titulos,
        "dias_sem_publicar": dias_sem,
        "data_ref_max_por_tese": data_max_por_tese,
        "n_publicadas": len(materias),
    }


def _gate_frescor(redacao: Dict[str, Any], historico: Dict[str, Any]) -> tuple:
    """REFORMA 03/09 (auditoria DSC): só publica com DADO NOVO. Defeito real: de
    29/08 a 02/09 o agente publicou 5 matérias seguidas com exatamente os mesmos
    números de julho. Compara a data_referencia mais recente do pacote da tese
    com a mais recente já publicada NESSA tese — igual ou menor = não publica."""
    tese_id = redacao.get("tese_id", "")
    pacote = redacao.get("pacote_factual") or []
    datas = [str(f.get("ultima_data") or "")[:10] for f in pacote]
    datas = [d for d in datas if d]
    if not datas:
        return False, "sem_dados_no_pacote"
    nova_max = max(datas)
    publicada_max = (historico.get("data_ref_max_por_tese") or {}).get(tese_id, "")
    if publicada_max and nova_max <= publicada_max:
        return False, (
            f"sem_dado_novo (tese {tese_id}: dado mais novo {nova_max} ≤ "
            f"já publicado {publicada_max})"
        )
    return True, f"dado_novo ({nova_max} > {publicada_max or 'primeira da tese'})"


def etapa_publicacao(
    redacao: Dict[str, Any],
    graficos: List[Dict[str, Any]],
    publicar: bool,
    status_post: str = "publish",
) -> Dict[str, Any]:
    from banco_producao_v4 import BancoProducaoV42, sha256_texto
    from publicador_economia_v4 import PublicadorEspelho, ErroPublicacao

    banco = BancoProducaoV42()

    # Fontes primárias (procedência factual)
    fontes_lista = []
    for fato in redacao["pacote_factual"]:
        fontes_lista.append(
            f'{fato["serie_nome"]} ({fato["fonte"]}/{fato["serie_id"]}) — '
            f'último: {fato["ultimo_valor"]} {fato["unidade"]} em {fato["ultima_data"]}'
        )

    # Só gráficos APROVADOS na auditoria entram (fail-closed)
    graficos_aprovados = [g for g in graficos if g["aprovado"]]
    if graficos and not graficos_aprovados:
        logging.error("NENHUM gráfico aprovado na auditoria visual — matéria seguirá sem imagens.")

    # Registra matéria PT no banco de produção
    materia_pt = {
        "titulo": redacao["titulo_pt"],
        "resumo": redacao["resumo_pt"],
        "paragrafos": redacao["paragrafos_pt"],
        "fontes_lista": fontes_lista,
    }
    materia_id_pt, novo_pt = banco.registrar_materia(
        idioma="pt", tese_id=redacao["tese_id"], titulo=materia_pt["titulo"],
        paragrafos=materia_pt["paragrafos"], resumo=materia_pt["resumo"],
        provedor_llm=redacao["provedor"], modelo_llm=redacao["modelo"],
        metadados={"reparos_mecanicos": redacao.get("reparos_mecanicos", [])},
    )
    # Matéria EN (arquivada para o Global South News)
    materia_id_en, novo_en = banco.registrar_materia(
        idioma="en", tese_id=redacao["tese_id"], titulo=redacao["titulo_en"],
        paragrafos=redacao["paragrafos_en"], resumo=redacao["resumo_en"],
        provedor_llm=redacao["provedor"], modelo_llm=redacao["modelo"],
    )

    # Fontes usadas → banco
    banco.registrar_fontes(materia_id_pt, [
        {"fonte": f["fonte"], "serie_id": f["serie_id"],
         "observacao_hash": f.get("observacao_hash", ""),
         "data_referencia": f["ultima_data"], "valor": f["ultimo_valor"]}
        for f in redacao["pacote_factual"]
    ])

    # Versão EN arquivada p/ GSN (publicação no Astro é etapa separada)
    os.makedirs(GSN_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    gsn_path = os.path.join(GSN_DIR, f"gsn_{redacao['tese_id']}_{ts}.json")
    _atomic_json(gsn_path, {
        "tese_id": redacao["tese_id"],
        "title": redacao["titulo_en"],
        "excerpt": redacao["resumo_en"],
        "paragraphs": redacao["paragrafos_en"],
        "sources": fontes_lista,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    })
    logging.info(f"Versão EN arquivada para o GSN: {gsn_path}")

    resultado: Dict[str, Any] = {
        "materia_id_pt": materia_id_pt, "nova_pt": novo_pt,
        "materia_id_en": materia_id_en, "nova_en": novo_en,
        "gsn_arquivo": gsn_path,
        "publicado": False,
    }

    # Vincula gráficos à matéria no banco (independente de publicar)
    for i, g in enumerate(graficos_aprovados):
        g["banco_pk"] = banco.vincular_grafico(
            materia_id_pt, png_sha256=g["png_sha256"],
            grafico_id=os.path.basename(g["png_path"]),
            serie_ref=f'{g["fonte"]}/{g["serie_id"]}',
            png_path=g["png_path"], manifest_path=g["manifest_path"],
            audit_path=g["audit_path"], audit_state=g["audit_state"],
            audit_provider=g["audit_provider"],
            posicao="featured" if i == 0 else "inline",
        )

    if not publicar:
        logging.info("--publicar ausente: matéria registrada no banco, sem envio ao WordPress.")
        return resultado

    # ---------------- publicação no espelho ----------------
    pub = PublicadorEspelho()
    categoria_id = pub.garantir_categoria()
    tag_id = pub.garantir_tag()

    # Upload dos gráficos aprovados
    graficos_com_media = []
    for g in graficos_aprovados:
        media_id = pub.upload_midia(g["png_path"], g["legenda"])
        g["wp_media_id"] = media_id
        graficos_com_media.append(g)
    # URLs reais via readback da mídia
    for g in graficos_com_media:
        st, resp = pub._request("GET", f"media/{g['wp_media_id']}")
        if st == 200 and isinstance(resp, dict):
            g["url_media"] = resp.get("source_url", "")

    featured_id = graficos_com_media[0]["wp_media_id"] if graficos_com_media else None
    inline = graficos_com_media[1:] if len(graficos_com_media) > 1 else []

    html = pub.montar_html(materia_pt, inline)
    corpo_canonico = json.dumps(
        {"titulo": materia_pt["titulo"], "paragrafos": materia_pt["paragrafos"]},
        ensure_ascii=False, sort_keys=True)
    meta_sha = sha256_texto(corpo_canonico)

    if banco.materia_ja_publicada(meta_sha):
        logging.info("Matéria já publicada anteriormente (idempotência) — pulando.")
        resultado["publicado"] = False
        resultado["motivo"] = "idempotencia"
        return resultado

    slug_base = "v42-" + datetime.now(timezone.utc).strftime("%Y%m%d") + "-" + redacao["tese_id"]
    # Passo 1: rascunho (o gate de imagem §86 só barra status=publish)
    try:
        post = pub.publicar(
            titulo=materia_pt["titulo"], html_corpo=html, resumo=materia_pt["resumo"],
            categoria_id=categoria_id, tag_id=tag_id,
            featured_media_id=featured_id, status="draft", slug=slug_base,
            meta_sha="",
        )
    except ErroPublicacao:
        if featured_id is None:
            raise
        # WP pode rejeitar featured_media recém-criado em race raro; tenta sem capa
        logging.warning("Post falhou com featured_media; tentando sem capa.")
        featured_id = None
        graficos_com_media = []
        post = pub.publicar(
            titulo=materia_pt["titulo"], html_corpo=html, resumo=materia_pt["resumo"],
            categoria_id=categoria_id, tag_id=tag_id,
            featured_media_id=None, status="draft", slug=slug_base + "-s2",
            meta_sha="",
        )

    if featured_id:
        # Passo 2: carimbo da checagem visual (auditor V4.2 = Tribunal Visual do gráfico)
        capa = graficos_com_media[0]
        carimbo = {
            "ok": True,
            "media_id": featured_id,
            "audit_state": capa["audit_state"],
            "audit_provider": capa["audit_provider"],
            "checado_por": "auditor_graficos_v4.py (Auditor Visual V4.2)",
            "ts": datetime.now(timezone.utc).isoformat(),
        }
        pub.carimbar_checagem(post["id"], carimbo, meta_sha)
        # Passo 3: publish (gate lê a meta já persistida)
        pub.alterar_status(post["id"], status_post)
    else:
        # Fail-closed: sem gráfico aprovado não há checagem possível → rascunho
        logging.warning("SEM imagem aprovada: post fica em DRAFT para revisão humana (fail-closed).")

    readback = pub.readback(post["id"])
    if readback["status"] == "publish":
        banco.marcar_publicada(
            materia_id_pt, site=pub.site, post_id=post["id"], link=readback["link"],
            post_status=readback["status"], categoria_ids=readback["categories"],
            tag_ids=readback["tags"], featured_media_id=readback["featured_media"],
        )
    for g in graficos_com_media:
        if g.get("banco_pk"):
            banco.atualizar_grafico_wp_media(g["banco_pk"], g["wp_media_id"])

    resultado.update({
        "publicado": readback["status"] == "publish",
        "post_id": post["id"],
        "link": readback["link"],
        "status_post": readback["status"],
        "readback": readback,
        "categoria_id": categoria_id,
        "tag_id": tag_id,
    })
    return resultado


def main() -> int:
    parser = argparse.ArgumentParser(description="Ciclo completo do Agente V4.2 de Economia")
    parser.add_argument("--tema", default="auto",
                        choices=["auto", "comercio_sul_sul", "politica_monetaria_comparada",
                                 "inflacao_primaria", "comercio"])
    parser.add_argument("--coletar", action="store_true", help="roda coletores antes do ciclo")
    parser.add_argument("--publicar", action="store_true", help="publica no espelho cafezinho.news")
    parser.add_argument("--status-post", default="publish", choices=["draft", "publish", "pending"])
    parser.add_argument("--max-graficos", type=int, default=3)
    args = parser.parse_args()

    tema = args.tema
    if tema == "comercio":
        tema = "comercio_sul_sul"

    inicio = datetime.now(timezone.utc).isoformat()
    recibo: Dict[str, Any] = {"inicio": inicio, "tema": tema, "etapas": {}}

    if args.coletar:
        logging.info("Etapa 0: rodando coletores...")
        try:
            from coletor_economia_v4 import ColetorEconomiaV4
            recibo["etapas"]["coletor_base"] = ColetorEconomiaV4().executar_coleta_completa()
        except Exception as e:
            recibo["etapas"]["coletor_base"] = {"erro": str(e)}
        try:
            from coletor_comercio_exterior_v4 import ColetorComercioExterior
            recibo["etapas"]["coletor_comex"] = ColetorComercioExterior().executar_coleta_completa()
        except Exception as e:
            recibo["etapas"]["coletor_comex"] = {"erro": str(e)}

    # Redação primeiro (define tese → séries dos gráficos)
    logging.info("Etapa 1: redação Texto Música (PT + EN)...")
    historico = _historico_publicacoes()
    redacao = etapa_redacao(
        tema,
        titulos_evitar=historico["titulos"][:10],
        dias_desde_ultima=historico["dias_sem_publicar"],
    )

    # REFORMA 03/09 — gates de publicação (auditoria DSC):
    fresco, motivo_frescor = _gate_frescor(redacao, historico)
    eco_titulo = float(redacao.get("titulo_similaridade_max") or 0.0)
    bloqueio_titulo = bool(eco_titulo >= 0.60 or redacao.get("titulo_similar_de"))
    gates = {
        "frescor": {"liberado": fresco, "motivo": motivo_frescor},
        "titulo": {
            "similaridade_max": eco_titulo,
            "similar_de": redacao.get("titulo_similar_de", ""),
            "bloqueado": bloqueio_titulo,
        },
        "n_publicadas_historico": historico["n_publicadas"],
    }
    publicar = args.publicar and fresco and not bloqueio_titulo
    if args.publicar and not publicar:
        gates["publicacao_bloqueada_motivo"] = (
            "titulo_repetido" if bloqueio_titulo else motivo_frescor)
        logging.warning(
            f"/Gate de publicação: matéria registrada localmente, SEM publish — "
            f"{gates['publicacao_bloqueada_motivo']}")

    recibo["etapas"]["redacao"] = {
        "tese_id": redacao["tese_id"],
        "titulo_pt": redacao["titulo_pt"],
        "titulo_en": redacao["titulo_en"],
        "paragrafos_pt": len(redacao["paragrafos_pt"]),
        "paragrafos_en": len(redacao["paragrafos_en"]),
        "provedor": redacao["provedor"],
        "modelo": redacao["modelo"],
        "reparos": redacao.get("reparos_mecanicos", []),
    }

    logging.info("Etapa 2: geração e auditoria visual dos gráficos...")
    graficos = etapa_graficos(redacao["graficos_planejados"], limite=args.max_graficos)
    recibo["etapas"]["graficos"] = [
        {k: g[k] for k in ("fonte", "serie_id", "png_path", "audit_state", "aprovado")}
        for g in graficos
    ]

    logging.info("Etapa 3: registro e publicação...")
    resultado_pub = etapa_publicacao(redacao, graficos, publicar, args.status_post)
    if args.publicar and not publicar:
        resultado_pub["gate_bloqueio"] = gates.get("publicacao_bloqueada_motivo", "")
    recibo["etapas"]["publicacao"] = resultado_pub
    recibo["gates_v42_reforma_20260903"] = gates
    recibo["fim"] = datetime.now(timezone.utc).isoformat()

    os.makedirs(CICLOS_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    recibo_path = os.path.join(CICLOS_DIR, f"ciclo_v42_{ts}.json")
    _atomic_json(recibo_path, recibo)
    logging.info(f"Recibo do ciclo gravado: {recibo_path}")

    print(json.dumps({
        "ok": True,
        "tese": redacao["tese_id"],
        "titulo_pt": redacao["titulo_pt"],
        "publicado": resultado_pub.get("publicado"),
        "link": resultado_pub.get("link"),
        "post_id": resultado_pub.get("post_id"),
        "recibo": recibo_path,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

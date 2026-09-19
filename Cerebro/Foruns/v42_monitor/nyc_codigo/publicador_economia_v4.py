#!/usr/bin/env python3
"""
publicador_economia_v4.py - MÓDULO E: Publicação do V4.2 no espelho cafezinho.news
====================================================================================
Publica as matérias do Redator V4.2 exclusivamente no ESPELHO cafezinho.news
(laboratório de produção; noindex/nofollow, fora do Google), com:

  - Categoria própria do bloco: "Estatística" (slug configurável, padrão 'estat'),
    criada automaticamente na primeira execução.
  - Tag "V4.2" como sinal visual de teste em todas as matérias do agente.
  - Upload dos gráficos dark-mode auditados (featured_media + figuras no corpo).
  - Idempotência por text_sha256 (banco de produção) + readback de confirmação.
  - Registro completo no banco_producao_v4.py (matéria → gráficos → fontes).

Credenciais: ESPELHO_WP_SITE / ESPELHO_WP_USER / ESPELHO_WP_PASS do cofre
.env.unificado (carregadas via env_loader; valores nunca impressos).
"""

import os
import sys
import json
import base64
import logging
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from env_loader import carregar_env

carregar_env()

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [PUBLICADOR-V42] %(message)s')

NOME_CATEGORIA = os.environ.get("V42_CATEGORIA_NOME", "Estatística")
SLUG_CATEGORIA = os.environ.get("V42_CATEGORIA_SLUG", "estat")
NOME_TAG = "V4.2"
SLUG_TAG = "v4-2"
# PROIBIDO selo/rodapé de "matéria gerada automaticamente" no corpo do post — nem no
# espelho (ordem do editor, 27/08/2026). Nada de expor automação ao leitor.
TIMEOUT = 60


class ErroPublicacao(RuntimeError):
    pass


class PublicadorEspelho:
    def __init__(self):
        self.site = os.environ.get("ESPELHO_WP_SITE", "").rstrip("/")
        self.user = os.environ.get("ESPELHO_WP_USER", "")
        self.senha = os.environ.get("ESPELHO_WP_PASS", "")
        if not self.site or not self.user or not self.senha:
            raise ErroPublicacao("ESPELHO_WP_SITE/USER/PASS ausentes no ambiente/cofre")

    # ------------------------------------------------------------- transporte
    def _auth(self) -> str:
        return "Basic " + base64.b64encode(f"{self.user}:{self.senha}".encode()).decode()

    def _request(self, metodo: str, rota: str, payload: Optional[dict] = None,
                 raw_body: Optional[bytes] = None, headers_extra: Optional[dict] = None,
                 timeout: int = TIMEOUT) -> Tuple[int, Any]:
        url = f"{self.site}/wp-json/wp/v2/{rota}"
        headers = {
            "Authorization": self._auth(),
            "User-Agent": "Mozilla/5.0 OCafezinho-V42-Publicador/1.0",
        }
        body = None
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif raw_body is not None:
            body = raw_body
        if headers_extra:
            headers.update(headers_extra)
        req = urllib.request.Request(url, data=body, headers=headers, method=metodo)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                texto = resp.read().decode("utf-8")
                try:
                    return resp.status, json.loads(texto)
                except json.JSONDecodeError:
                    return resp.status, texto
        except urllib.error.HTTPError as e:
            try:
                corpo = e.read().decode("utf-8")[:500]
            except Exception:
                corpo = ""
            return e.code, corpo
        except Exception as e:
            return -1, str(e)

    # ------------------------------------------------------------- taxonomia
    def garantir_categoria(self) -> int:
        st, resp = self._request("GET", f"categories?slug={urllib.parse.quote(SLUG_CATEGORIA)}")
        if st == 200 and isinstance(resp, list) and resp:
            cat_id = resp[0]["id"]
            logging.info(f"Categoria '{NOME_CATEGORIA}' já existe: id={cat_id}")
            return cat_id
        payload = {"name": NOME_CATEGORIA, "slug": SLUG_CATEGORIA,
                   "description": "Inteligência estatística primária — Agente V4.2 (provisório)"}
        st, resp = self._request("POST", "categories", payload)
        if st in (200, 201) and isinstance(resp, dict) and resp.get("id"):
            logging.info(f"Categoria '{NOME_CATEGORIA}' criada: id={resp['id']}")
            return resp["id"]
        raise ErroPublicacao(f"Falha ao criar categoria: HTTP {st} {str(resp)[:200]}")

    def garantir_tag(self) -> int:
        st, resp = self._request("GET", f"tags?slug={urllib.parse.quote(SLUG_TAG)}")
        if st == 200 and isinstance(resp, list) and resp:
            return resp[0]["id"]
        st, resp = self._request("POST", "tags", {"name": NOME_TAG, "slug": SLUG_TAG,
                                                   "description": "Sinal de teste do Agente V4.2"})
        if st in (200, 201) and isinstance(resp, dict) and resp.get("id"):
            logging.info(f"Tag '{NOME_TAG}' criada: id={resp['id']}")
            return resp["id"]
        raise ErroPublicacao(f"Falha ao criar tag: HTTP {st} {str(resp)[:200]}")

    # ----------------------------------------------------------------- mídia
    def upload_midia(self, png_path: str, titulo_alt: str) -> int:
        with open(png_path, "rb") as f:
            dados = f.read()
        nome_arquivo = os.path.basename(png_path)
        st, resp = self._request(
            "POST", "media", raw_body=dados,
            headers_extra={
                "Content-Disposition": f'attachment; filename="{nome_arquivo}"',
                "Content-Type": "image/png",
            },
            timeout=120,
        )
        if st in (200, 201) and isinstance(resp, dict) and resp.get("id"):
            media_id = resp["id"]
            # alt text para acessibilidade/SEO
            self._request("POST", f"media/{media_id}", {"alt_text": titulo_alt[:200]})
            logging.info(f"Mídia enviada: {nome_arquivo} → wp_media_id={media_id}")
            return media_id
        raise ErroPublicacao(f"Falha no upload de mídia: HTTP {st} {str(resp)[:200]}")

    # ------------------------------------------------------------ publicação
    def montar_html(self, materia: Dict[str, Any], graficos_inline: List[Dict[str, Any]]) -> str:
        """HTML do corpo: parágrafos Texto Música + figuras + selo + fontes."""
        partes: List[str] = []
        if materia.get("resumo"):
            partes.append(f'<p class="lead"><strong>{materia["resumo"]}</strong></p>')
        for i, par in enumerate(materia["paragrafos"]):
            partes.append(f"<p>{par}</p>")
            # Insere figura após o 2º parágrafo (se houver gráfico inline)
            if i == 1:
                for g in graficos_inline:
                    # REFORMA 03/09: código cru FONTE/SERIE_ID fora da legenda do
                    # leitor (defeito: "— GACC/GACC_CHINA_BALANCE" exposto no espelho);
                    # a procedência completa segue no rodapé "Fontes primárias".
                    partes.append(
                        f'<figure class="wp-caption aligncenter">'
                        f'<img src="{g["url_media"]}" alt="{g["legenda"]}" loading="lazy">'
                        f'<figcaption class="wp-caption-text">{g["legenda"]}</figcaption></figure>'
                    )
        # Sem selo de automação no corpo (proibido pelo editor — ver comentário no topo)
        fontes = materia.get("fontes_lista", [])
        if fontes:
            itens = "".join(f"<li>{f}</li>" for f in fontes)
            partes.append(f"<p><strong>Fontes primárias:</strong></p><ul>{itens}</ul>")
        return "\n".join(partes)

    def publicar(
        self,
        *,
        titulo: str,
        html_corpo: str,
        resumo: str,
        categoria_id: int,
        tag_id: int,
        featured_media_id: Optional[int],
        status: str = "draft",
        slug: Optional[str] = None,
        meta_sha: str = "",
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "title": titulo,
            "content": html_corpo,
            "excerpt": resumo,
            "status": status,
            "categories": [categoria_id],
            "tags": [tag_id],
            "meta": {"v42_texto_sha256": meta_sha},
        }
        if featured_media_id:
            payload["featured_media"] = featured_media_id
        if slug:
            payload["slug"] = slug
        st, resp = self._request("POST", "posts", payload)
        if st in (200, 201) and isinstance(resp, dict) and resp.get("id"):
            logging.info(f"Post criado: id={resp['id']} status={resp.get('status')}")
            return resp
        raise ErroPublicacao(f"Falha ao criar post: HTTP {st} {str(resp)[:300]}")

    def carimbar_checagem(self, post_id: int, carimbo: Dict[str, Any], meta_sha: str = "") -> None:
        """Grava _cafezinho_img_check (gate fail-close §86/16-08) ANTES do publish.

        O gate REST valida a meta já PERSISTIDA no post; por isso o carimbo é
        gravado em request separado, com o post ainda em rascunho.
        """
        payload: Dict[str, Any] = {
            "meta": {"_cafezinho_img_check": json.dumps(carimbo, ensure_ascii=False)},
        }
        if meta_sha:
            payload["meta"]["v42_texto_sha256"] = meta_sha
        st, resp = self._request("POST", f"posts/{post_id}", payload)
        if st not in (200, 201):
            raise ErroPublicacao(f"Falha ao carimbar checagem: HTTP {st} {str(resp)[:300]}")
        logging.info(f"Carimbo _cafezinho_img_check gravado no post {post_id}.")

    def alterar_status(self, post_id: int, status: str) -> Dict[str, Any]:
        st, resp = self._request("POST", f"posts/{post_id}", {"status": status})
        if st not in (200, 201) or not isinstance(resp, dict):
            raise ErroPublicacao(f"Falha ao mudar status para '{status}': HTTP {st} {str(resp)[:300]}")
        logging.info(f"Post {post_id} → status={status}")
        return resp

    def readback(self, post_id: int) -> Dict[str, Any]:
        st, resp = self._request("GET", f"posts/{post_id}?context=edit")
        if st != 200 or not isinstance(resp, dict):
            raise ErroPublicacao(f"Readback falhou: HTTP {st}")
        return {
            "post_id": resp.get("id"),
            "status": resp.get("status"),
            "link": resp.get("link"),
            "slug": resp.get("slug"),
            "categories": resp.get("categories"),
            "tags": resp.get("tags"),
            "featured_media": resp.get("featured_media"),
            "verificado_em": datetime.now(timezone.utc).isoformat(),
        }


if __name__ == "__main__":
    pub = PublicadorEspelho()
    cat = pub.garantir_categoria()
    tag = pub.garantir_tag()
    print(json.dumps({"ok": True, "categoria_id": cat, "tag_id": tag,
                      "site": pub.site.replace("https://", "").replace("http://", "")},
                     ensure_ascii=False))

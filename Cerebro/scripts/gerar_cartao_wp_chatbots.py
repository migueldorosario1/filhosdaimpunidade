#!/usr/bin/env python3
"""Regenera Outros/chaves/wp_cafezinho_chatbots.md a partir do cofre — para chatbots celular/desktop."""
from __future__ import annotations

from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
COFRE = WORKSPACE / "Outros/chaves/agentes_labs/.env.unificado"
OUT = WORKSPACE / "Outros/chaves/wp_cafezinho_chatbots.md"


def carregar_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        line = line.replace("export ", "", 1)
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def main() -> None:
    if not COFRE.is_file():
        raise SystemExit(f"Cofre não encontrado: {COFRE}")

    env = carregar_env(COFRE)
    site = env.get("WP_SITE", "https://controle.ocafezinho.com").rstrip("/")
    user = env.get("WP_USER_CAFEZINHO") or env.get("WP_USER", "")
    password = env.get("WP_PASS_CAFEZINHO") or env.get("WP_APP_PASSWORD") or env.get("WP_PASS", "")
    if not all([site, user, password]):
        raise SystemExit("WP_SITE / WP_USER / WP_PASS ausentes no cofre")

    content = f"""# Cartão de Bolso — Publicar no O Cafezinho (chatbots celular e desktop)

**Uso:** Cole este arquivo inteiro no Project Knowledge / Custom Instructions / Memory de ChatGPT, Claude, Grok ou salve no Google Docs do celular.
**Atualizado:** 2026-06-20 (gerado por Cerebro/scripts/gerar_cartao_wp_chatbots.py)
**Não commitar no Git.**

---

## Credenciais WordPress REST

| Campo | Valor |
|-------|--------|
| Site público | https://www.ocafezinho.com |
| API (painel) | {site}/wp-json/wp/v2/ |
| WP_SITE | {site} |
| WP_USER | {user} |
| WP_APP_PASSWORD | {password} |
| Autenticação | HTTP Basic Auth |

---

## Regras

1. Padrão: **draft** — `publish` só se Miguel pedir
2. **featured_media** obrigatório (§86)
3. Título ≠ lead do texto
4. Categorias: Política=22, Ciência=19936, IA=5008
5. Editar: https://controle.ocafezinho.com/wp-admin/post.php?post=POST_ID&action=edit

---

## 1) Upload imagem

```bash
curl -X POST -u "{user}:{password}" \\
  -H "Content-Disposition: attachment; filename=capa.jpg" \\
  -H "Content-Type: image/jpeg" \\
  -H "User-Agent: CafezinhoAgent/1.0" \\
  --data-binary @IMAGEM.jpg \\
  "{site}/wp-json/wp/v2/media"
```

## 2) Criar draft

```bash
curl -X POST -u "{user}:{password}" \\
  -H "Content-Type: application/json" \\
  -d '{{"title":"TÍTULO","content":"<p>HTML</p>","status":"draft","featured_media":MEDIA_ID,"categories":[22]}}' \\
  "{site}/wp-json/wp/v2/posts"
```

## 3) Atualizar corpo

```bash
curl -X POST -u "{user}:{password}" \\
  -H "Content-Type: application/json" \\
  -d '{{"content":"<p>HTML</p>"}}' \\
  "{site}/wp-json/wp/v2/posts/POST_ID"
```

---

## fetch (JavaScript)

```javascript
const SITE="{site}", USER="{user}", PASS="{password}";
const auth=btoa(`${{USER}}:${{PASS}}`);
fetch(`${{SITE}}/wp-json/wp/v2/posts`, {{
  method:"POST",
  headers:{{Authorization:`Basic ${{auth}}`,"Content-Type":"application/json"}},
  body:JSON.stringify({{title:"Título",content:"<p>...</p>",status:"draft",featured_media:MEDIA_ID,categories:[22]}})
}}).then(r=>r.json()).then(console.log);
```

---

## Pedir ao Miguel

- Título, corpo HTML, **imagem anexada no chat**, categoria, draft ou publish
"""

    OUT.write_text(content, encoding="utf-8")
    print(f"✅ Gerado: {OUT}")
    print("→ Copie para Google Docs / ChatGPT Project / Claude Project")


if __name__ == "__main__":
    main()
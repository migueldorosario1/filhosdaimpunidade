import requests
from requests.auth import HTTPBasicAuth
import os
from pathlib import Path
from dotenv import load_dotenv

ENV_FILE = Path("/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/.env.unificado")
load_dotenv(ENV_FILE)
wp_user = os.getenv("WP_USER_CAFEZINHO") or os.getenv("WP_USER")
wp_password = (
    os.getenv("WP_APP_PASSWORD_CAFEZINHO")
    or os.getenv("WP_PASS_CAFEZINHO")
    or os.getenv("WP_APP_PASSWORD")
    or os.getenv("WP_PASS")
)
if not wp_user or not wp_password:
    raise RuntimeError(f"Credenciais WordPress Cafezinho ausentes em {ENV_FILE}")

url_post = "https://controle.ocafezinho.com/wp-json/wp/v2/posts/262434"
auth = HTTPBasicAuth(wp_user, wp_password)

payload = {
    "status": "publish"
}

res = requests.post(url_post, auth=auth, json=payload)
print("Publish status code:", res.status_code)
if res.status_code in (200, 201):
    data = res.json()
    print("ARTICLE PUBLISHED SUCCESSFULLY!")
    print("Post ID:", data.get("id"))
    print("Published URL:", data.get("link"))
else:
    print("Error publishing post:", res.text)

---
name: reference-warp-vpn-destrava-ratelimits
description: Cloudflare WARP-CLI está instalada na máquina LOCAL do Miguel. Destrava rate-limits Flickr/Wikimedia quando IP do Tencent está banido.
metadata: 
  node_type: memory
  type: reference
  originSessionId: ab544d32-d470-42b2-8246-7c83f1137bc1
---

## Cloudflare WARP-CLI — VPN local pra destravar rate-limits

### Onde está
- **Binário**: `/usr/bin/warp-cli`
- **Config dir**: `/home/migueldorosario/.local/share/warp/`
- **GUI dir**: `/home/migueldorosario/.local/share/cloudflare-warp-gui/`
- **Servidor**: NÃO está instalada (nem Tencent, NYC, China-proxy, Alibaba). Só na máquina LOCAL Miguel.

### Comandos básicos
```bash
warp-cli status            # mostra Connected / Disconnected
warp-cli connect           # liga
warp-cli disconnect        # desliga
```

### IP típico
- **Sem WARP** (residencial Miguel BR): `186.223.171.9` ou variações
- **Com WARP** (Cloudflare edge): `104.28.x.x` ou similar

### Quando usar
- Quando IP do Tencent está rate-limited pelo Flickr/Wikimedia (HTTP 429)
- Pra testar API pública de fora do escopo do servidor
- Pra contornar bloqueio geográfico em CDN específico

### Caso fundador 2026-06-26
Auditoria retroativa V3 do banco mídia legado tentou baixar 17.334 imagens Flickr com 10 workers paralelos. Flickr baniu IP do Tencent (43.156.151.165) — 100% HTTP 429 mesmo com workers=2 + sleep 2s. Tencent não tem WARP instalado.

Ligamos WARP local + testamos download da MESMA URL Flickr → **HTTP/2 200**. IP do WARP (104.28.152.90) não está banido.

### Arquiteturas possíveis pra usar WARP em jobs do Tencent

**Opção A: Rodar auditoria LOCAL** (mais simples)
- Banco Tencent acessado via SSH (`scp` ou consulta direta)
- Downloads + medições rodam local com WARP ligado
- UPDATE no banco via SSH heredoc

**Opção B: SSH reverse tunnel SOCKS** (mais elegante)
- Local com WARP ligado
- `ssh -R 1080 tencent` cria SOCKS proxy no Tencent apontando pro Local
- Scripts no Tencent: `requests.get(url, proxies={"http": "socks5://localhost:1080"})`
- Latência adicional ~50-100ms por request mas IP de saída do WARP

**Opção C: Instalar WARP no Tencent diretamente** (mais robusto)
- `curl https://pkg.cloudflareclient.com/install.sh | sh`
- `warp-cli registration new`
- `warp-cli connect`
- IP de saída do Tencent passa a ser do WARP

### Relacionado
- [[reference-banco-midia-canonico-legado]] — banco que precisava auditoria retroativa
- [[project-sprint-acervo-midia-publicador-microsservicos-20260625]] — sprint que vai consumir esses dados

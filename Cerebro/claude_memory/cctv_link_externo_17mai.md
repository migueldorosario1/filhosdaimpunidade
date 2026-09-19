---
name: cctv-link-externo-17-05
description: Painel CCTV exposto via IP Tencent externo — 3 telas operacionais
metadata: 
  node_type: memory
  type: project
  originSessionId: 65dba477-db6e-40a3-b94a-ea6212c77e90
---

**[2026-05-17]** — Miguel solicitou CCTV acessível via IP externo (não localhost).

## Link Externo

🔗 **URL:** `http://43.156.151.165:8080`

- **Host:** Tencent Cingapura (IP público)
- **Porta:** 8080
- **Serviço:** painel_cctv_trindade_v2.py + v3

## 3 Telas

1. **Tela 1:** Canal Trindade (índice + últimas msgs)
2. **Tela 2:** Forum Trindade (5 colunas humanizadas)
3. **Tela 3:** Posts Cafezinho (20 colunas 2x10)

## Status

- ✅ Servidor ajustado para `0.0.0.0:8080` (escuta all interfaces)
- ✅ Testes locais (localhost:8080 + 192.168.0.9:8080)
- ⚠️ Loops Trindade pausados 17/05 ~18:35 BRT (por ordem Miguel)
- ⏹️ CCTV saiu do ar quando loops pararam

## Reativação

```bash
# Via painel_cctv_trindade_v2.py
python3 root/painel_cctv_trindade_v2.py &

# Ou via crontab (se loop Trindade reativado)
# Verificar: crontab -l | grep cctv
```

---

**Criado:** 2026-05-17 20:40 BRT (Claude Code)  
**Status:** Pronto pra reativar

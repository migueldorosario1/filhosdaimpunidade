---
name: user-streamyard-desligar-wifi-com-cabo
description: "Miguel faz live no Streamyard; sempre DESLIGAR o WiFi quando estiver no cabo Ethernet, senão WebRTC usa WiFi paralelo como ICE candidate e pica a recepção dos convidados"
metadata: 
  node_type: memory
  type: user
  originSessionId: 809b3e9a-a605-4fa5-b09c-b5d9fbe87a8d
---

Miguel faz lives regulares pelo **Streamyard** (Cafezinho, ocafezinho.com) usando notebook Dell com cabo Ethernet **USB 3.0** (adaptador `enx00e04c680e41`, Realtek r8152, 1000 Mbit/s full duplex) plugado no roteador Vivo/GVT (`192.168.15.1`). Em paralelo, tem WiFi `CLARO_5G4D062E` ativo (frequentemente com sinal fraco, ~-74 dBm, 2 barras).

**Sintoma diagnosticado 2026-09-15**: imagem dele saía perfeita na live, mas ele recebia **imagem picotada dos outros convidados**. Internet estava tecnicamente OK (226 Mbit down / 210 up / 0% perda / 9ms para 8.8.8.8 / 123ms estável para Streamyard).

**Causa raiz**: Streamyard usa **WebRTC**, que enumera TODAS as interfaces de rede ativas como **ICE candidates** — NÃO obedece a tabela de roteamento do sistema (que privilegiava o cabo, métrica 100 vs WiFi 600). Parte dos pacotes de mídia dos convidados entrava pelo WiFi fraco em paralelo → picote na recepção. O upload dele saía inteiro pelo cabo (streams individuais, um caminho só) → imagem dele boa. Download tinha múltiplas streams simultâneas (uma por convidado) → sofria mais com WiFi oscilante.

**Correção confirmada por Miguel 15/09 chat CLI**: "desliguei o wifi e melhorou. guarda isso no cérebro."

**Regra operacional pra livestreams**:
1. Antes de qualquer live no Streamyard/Meet/Zoom/Discord, se estiver no cabo, **DESLIGAR o WiFi** (`nmcli radio wifi off` ou pelo applet). Mesmo padrão vale pra qualquer app WebRTC.
2. Se WiFi tem que ficar ligado (celular na mesma máquina, etc), forçar o navegador a usar só uma interface via `chrome://flags` `WebRTC IP handling policy` = `default_public_interface_only`, ou usar a extensão "WebRTC Network Limiter".
3. Se recepção picar de novo com WiFi já desligado: pode ser upload ruim dos CONVIDADOS (pedir pra testarem `fast.com`) ou congestionamento na rota internacional pro servidor Streamyard.

**Diagnóstico rápido em vez de adivinhar**:
- `ip -br addr` + `ip route get 8.8.8.8` → confirma qual interface está roteando
- `ip -br link | grep UP` → lista todas as interfaces ativas (o "vilão silencioso" no caso Streamyard é qualquer segunda interface UP)
- `ping -c 30 -I <iface> streamyard.com` → jitter/perda por interface
- `iwconfig` → sinal WiFi em dBm (bom ≥ -60, marginal -60 a -70, ruim ≤ -74)

**Não é caso isolado** — vale pra qualquer setup dual-homed (cabo + WiFi ligados ao mesmo tempo) em apps WebRTC.

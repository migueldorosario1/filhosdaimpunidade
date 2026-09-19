# 🛡️ MEMÓRIA DE AUTOAPRENDIZADO, BUGS E INCIDENTES TÉCNICOS V5
## Registro Histórico de Lições Aprendidas, Falhas Evitadas e Autocura

`yaml
tipo: MEMORIA_PERMANENTE_APRENDIZADO
versao: 5.0.0
data: 2026-08-20
finalidade: Prevenir reincidência de bugs e orientar autocura de agentes
`

---

## 1. Catálogo de Bugs Críticos Resolvidos & Diretrizes de Prevenção

### 🐛 BUG-001: Geração Excessiva de IA em Verticais Proibidas
- **Causa Raiz:** O pipeline gerava IA generativa quando a busca rápida falhava, poluindo verticais factuais.
- **Lição Canônica:** Busca ativa documental em Wikimedia Commons / Flickr com validação de resolução $\ge 1200\text{px}$ é OBRIGATÓRIA antes de qualquer tentativa de IA. Verticais de Hard News e Política têm cota ZERO de IA.

### 🐛 BUG-002: Truncamento Oculto de Imagens Elegíveis ([:4])
- **Causa Raiz:** O módulo gerenciador_imagens.py limitava arbitrariamente a lista de candidatas aos primeiros 4 itens, descartando centenas de fotos válidas do banco.
- **Lição Canônica:** Nunca truncar listas de busca documental no intake; permitir que os filtros de qualidade analisem todo o conjunto disponível.

### 🐛 BUG-003: Import de Módulo Aninhado em Função de Produção
- **Causa Raiz:** import shutil aninhado dentro de função causava UnboundLocalError silencioso engolido por 	ry/except.
- **Lição Canônica:** Todos os imports devem residir no topo do módulo (	op-level). Proibido except: mudo sem log detalhado do stack trace.

### 🐛 BUG-004: Concorrência e Sobrescrita de Capas
- **Causa Raiz:** Dois agentes aplicavam capas simultaneamente no mesmo post sem protocolo de trava.
- **Lição Canônica:** Quadro ponte_imagens_RESERVA.md obrigatório com reserva atômica de post ID antes de iniciar a aplicação. Se o post já possui eatured_media > 0, o agente NUNCA deve sobrescrever.

### 🐛 BUG-005: Queda de Ofício e Silêncio Operacional (CASE-001)
- **Causa Raiz:** Um agente saía do ar e os demais tentavam assumir sem critério ou ficavam parados indefinidamente.
- **Lição Canônica:** Limiar de 45 min para alerta e **90 min para Circuit Breaker formal**. Alerta push de emergência no Telegram do dono com notificação em som alto; transição para sentinela/triagem sem publicação desgovernada.

---

## 2. Protocolo de Autoaprendizado a Cada Ciclo

Antes de executar qualquer apuração ou geração:
1. O AGY lê a **Memória de Estilo** e a **Memória de Bugs**;
2. Verifica se a pauta ou entidade possui registros de gafes ou vetos editoriais prévios;
3. Ao término do ciclo, se uma anomalia for detectada e corrigida, ela é anexada a este catálogo.

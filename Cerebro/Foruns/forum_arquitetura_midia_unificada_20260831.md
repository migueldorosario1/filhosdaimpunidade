# 🏛 ARQUITETURA DE MÍDIA UNIFICADA — o Circuito da Imagem do Cafezinho

**Dono:** sprint V4.1 Vision (ZM) · **Aberto:** 31/08/2026 2026-08-31 13:07 BRT (ordem Miguel: "repensa uma arquitetura e bem legal")
**Estado:** peças existem e operam; este documento define o circuito único + costuras pendentes.

## O circuito (7 camadas)

```
FONTES ──► TRIAGEM ──► BANCO ÚNICO ──► GATES ──► CONSUMO ──► REGISTRO/PÓS-CHECAGEM
```

1. **FONTES**: Flickr oficial (allowlist BR) · Commons/Openverse · caçadores humanos (AGY/CL/5º fallback) · redação · busca ativa (painel, enqueue por entidade).
2. **TRIAGEM (visão dupla sempre)**: DeepSeek Vision × Qwen (Gemini reserva) — factory `media_vision_providers` do v4_labs, a mesma para robô de capas e olho. Proxy IPRoyal para downloads (429 de datacenter).
3. **BANCO ÚNICO = BANCO OURO V3** (decisão desta arquitetura): sqlite + R2, 1.214 fotos, 35k rejeições com motivo, FTS, fila humana — **acervo canônico da casa**. Os demais viram FONTES ou espelhos: `banco_links_midia` (links de PESSOAS com data — alimento de caçadores; migra gradualmente pro Ouro), WP media library (espelho do publicado), `audited_media` do pipeline (decisões do runtime; promover pro Ouro).
4. **GATES**: carimbo `_cafezinho_img_check` casado com a mídia (§86/gate-visao) · Emendas 7/8/11/12 · **NO-IA** (capa = foto achada) · pessoa central = foto da pessoa (nominal dura).
5. **APROVAÇÃO em 2 estágios**: **OLHO APURADO** (automático, cron */2h: reprova lixo óbvio, aprova o confirmado com carimbo auditável, dúvida desce) → **PAINEL HUMANO** `/midia-ouro/aprovacao` (mobile: tocar na foto = aprovar; EDITAR/LIXO grandes fora da foto; nome da entidade gigante) — Miguel decide o resto.
6. **CONSUMO**: robô de capas V4.1 (dsn_imagem cron */20) · agentes externos · caçadores · WP.
7. **REGISTRO/PÓS-CHECAGEM**: Telegram com links (foto no site + original + edição) — auditoria de higidez do agente pelo Miguel.

## Costuras pendentes (próximos passos, ordem)

| # | O quê | Onde |
|---|---|---|
| 1 | **Ouro como camada 1 da cascata** do `featured_image_runtime` (hoje consulta só o audited local) — adapter Ouro→V4AuditedMediaStore | NYC v4_labs |
| 2 | Dashboard unificado (painel geral do Ouro ganha status do robô de capas + olho + fila_caca) | painel_midia_ouro |
| 3 | Migração gradual banco_links → Ouro (pessoas com data_foto viram campo do Ouro) | script |
| 4 | Teto GB/dia do proxy + telemetria | worker |

## Decisões registradas

- Capa = FOTO ACHADA (NO-IA, ordem Miguel 11:30) — executor blindado.
- Pessoa no título central = foto da pessoa, nominal dura (ordem 12:05).
- Lugar/tema = pertinência; identidade nominal só para pessoa.
- Olho NUNCA aprova 2+ pessoas não identificadas nem confiança <0.90.
- Acesso do painel: https://midia-198-199-121-136.sslip.io/midia-ouro/aprovacao (basic auth; senha em /root/.midia_ouro_senha_20260831 do NYC — enviada ao Miguel por Telegram).

— ZCode/GLM-5.3 · 2026-08-31 13:07 BRT

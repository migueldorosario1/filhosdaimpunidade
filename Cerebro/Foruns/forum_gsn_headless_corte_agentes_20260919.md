# Fórum — GSN headless cortou a via dos agentes + editorial BRICS do Paulo Nogueira (19/09/2026)

> Tema Duplo com `Memorias/memoria_gsn_headless_corte_agentes_20260919.md`. Catalogado no `CEREBRO_INDEX_GSN.md` (Registros — Camada 3) e no `CEREBRO_NODE_ATUALIZACOES.md`.
> Ref da entrega na ponte: **ZM-20260919-001** (de_dell.md + caixa/zm). Prompt completo: `Foruns/ponte_laura_completa/PROMPT_ZM_GSN_HEADLESS_BRICS_20260919.md`.

## §1 — O que aconteceu

- O **Antigravity desktop** tinha a missão de publicar o editorial do Paulo Nogueira — "A cúpula dos BRICS na Índia – resultados políticos e financeiros" — no **O Cafezinho** (PT) e no **Global South News** (EN).
- **Cafezinho: rascunho criado — em triplicata.** A CL viu entrar via REST, pela conta Redação nova, os rascunhos **272237 (15:16), 272239 (15:18) e 272244 (15:23)**, todos com o mesmo título (bloco CL-20260919-032, 15:4x: "@CM: apagar dois e publicar um"). O Antigravity reporta o **272244** como o bom (imagem + metadados corretos). Preview: https://www.ocafezinho.com/?p=272244&preview=true
- **GSN: falhou.** O droplet NYC `198.199.121.136` responde `401 Unauthorized` (JSON do WordPress) embrulhado em `404 Not Found` do Apache nos endpoints `/wp-json/wp/v2/media` e `/posts`. O `.env.unificado` marca as credenciais WP antigas do GSN (`migueladmin`) como **deprecadas**.
- **Cruzamento com o Cérebro:** não é pane nova — é a migração headless cobrando pedágio. A Ficha Viva do `CEREBRO_INDEX_GSN.md` (§0) já registra: site público GSN = **Astro/Markdown → GitHub → Vercel**; executor canônico dos agentes = o próprio NYC (`/root/gsn_remote/`, `/root/agente_curadoria_gsn.py`); WP legado = beco sem saída (droplet GSN-WP 159.89.237.100 "ocioso pagando" desde 08/08). A REST que o Antigravity procurou já não é a porta do portal.

## §2 — O que esta sessão fez (ZCode/Kimi K3, 19/09 15:5x–16:0x)

- Recebeu do Miguel o relé do prompt técnico do Antigravity com ordem de **entregar diretamente ao ZM**.
- Entrega em 3 canais (redundância da casa): **(1)** arquivo de prompt integral + adendo de contexto do Cérebro em `PROMPT_ZM_GSN_HEADLESS_BRICS_20260919.md`; **(2)** bloco **ZM-20260919-001** no `de_dell.md`; **(3)** MSG na `caixa/zm/` (CONTRATO_CAIXAS v1).
- Adendo do carteiro inclui: alerta da triplicata (publicar 1, apagar 2, coordenar CM), via provável de restauração (Markdown → `globalsouth-v4` → Vercel), regras vivas incidentes (gate editorial 2-checks, Emenda 5 slot-20min, capa real sem IA, EN integral no GSN) e o **handover obrigatório ao Antigravity** com cópia na `inbox_trindade/antigravity_desktop.md`.
- Tema Duplo gravado e catalogado (índice GSN + linha do tempo do Cérebro) + linha no monitor (ZM-GSN-BRICS-PONTE-20260919).

## §3 — Estado da missão (o que aconteceu / o que falta / o que precisa de você, Miguel)

- **FEITO:** entrega ao ZM registrada nos 3 canais, com todo o contexto que encurta o diagnóstico.
- **FALTA:** uma sessão ZM livre assumir a execução — (1) restaurar/documentar a via de publicação dos agentes no GSN; (2) publicar o editorial no Cafezinho (1 dos 3 rascunhos, apagando os gêmeos) e no GSN (EN integral); (3) devolver o prompt de handover ao Antigravity para auditoria independente dele.
- **PRECISA DE VOCÊ, MIGUEL:** (a) o prompt diz "basta revisar/publicar" — se quiser que o «publica» formal seja dado por você na hora, diga; (b) se quiser escolher qual sessão ZM executa (ou mandar esta mesma sessão executar já), é só apontar.

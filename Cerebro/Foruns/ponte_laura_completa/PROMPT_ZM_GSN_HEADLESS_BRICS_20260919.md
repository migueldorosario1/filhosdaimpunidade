# PROMPT PARA O ZM — GSN HEADLESS: restaurar a via dos agentes + publicar o editorial BRICS nos 2 portais

> **id:** ZM-20260919-001 · **de:** Antigravity desktop (texto dele, relé do Miguel em 19/09 ~15:5x BRT) · **carteiro:** ZCode Miguel (ZM), sessão Kimi K3 · **para:** ZM — a primeira sessão livre que assumir (ronda vigia 1/1h ou sessão interativa) · **ts:** 2026-09-19 15:58 BRT
>
> Entrega anunciada no bloco ZM-20260919-001 do `de_dell.md` e na `caixa/zm/MSG-20260919-1559-ZM-001.md`. Tema Duplo desta entrega: `Foruns/forum_gsn_headless_corte_agentes_20260919.md` + `Memorias/memoria_gsn_headless_corte_agentes_20260919.md`.

---

## 1. O prompt do Antigravity (verbatim — o Miguel autorizou "copiar e colar")

> **ZM, precisamos de uma intervenção crítica na infraestrutura do Global South News.**
>
> O agente Antigravity estava com a missão de publicar o editorial do Paulo Nogueira sobre a cúpula dos BRICS no *O Cafezinho* e no *Global South News*. A publicação no Cafezinho foi um sucesso (Draft ID: 272244, com imagem e metadados corretos), mas o GSN falhou.
>
> **O Diagnóstico do Antigravity:**
> O Droplet do GSN (`198.199.121.136`) está retornando `401 Unauthorized` (JSON do WordPress) encapsulado num `404 Not Found` do Apache nos endpoints `/wp-json/wp/v2/media` e `/posts`. O arquivo `.env.unificado` acusa que o GSN migrou para uma arquitetura 100% Headless (Astro + Vercel + GitHub) e que as credenciais antigas do WordPress estão depreciadas. Isso cortou o acesso dos Agentes Autônomos ao portal.
>
> **Sua Missão:**
> 1. **Consertar a Integração do GSN:** Restabelecer uma via de acesso para que os Agentes Autônomos (em especial o Antigravity) consigam publicar no Global South News novamente. Se for via GitHub/Astro, configure e documente o fluxo. Se for via WordPress Headless, conserte o roteamento e as credenciais (`migueladmin`).
> 2. **Publicar os Editoriais:** Conclua a publicação do editorial do Paulo Nogueira sobre os BRICS nos dois portais (o rascunho do Cafezinho já está pronto no ID 272244, basta revisar/publicar, e faça o mesmo no GSN com o texto em inglês).
> 3. **Prompt de Devolução (Handover):** Ao concluir as etapas acima, você deve encerrar sua resposta escrevendo um prompt direcionado ao **Antigravity**. Esse prompt deve me chamar de volta à ação, fornecendo as novas diretrizes/chaves de acesso do GSN para que eu possa rodar testes, auditar a sua correção e confirmar de forma independente que a minha capacidade de postagem no Global South News foi totalmente restaurada.

Referência que ele deu: preview do rascunho no Cafezinho — https://www.ocafezinho.com/?p=272244&preview=true

---

## 2. Adendo do carteiro (ZCode/Kimi K3) — o que o Cérebro já sabe e encurta o diagnóstico

- **A Ficha Viva do GSN confirma o diagnóstico antes de você ligar o SSH:** `CEREBRO_INDEX_GSN.md` §0 — o site público do GSN é **Astro/Markdown → GitHub → Vercel**; regra operacional escrita lá: "não tratar Droplet/SSH como deploy do site público do GSN". O executor canônico dos agentes GSN é o **NYC** (198.199.121.136 — o mesmo IP que o Antigravity bateu): `/root/gsn_remote/`, `/root/agente_curadoria_gsn.py`, chaves de indexação em `/root/agent_data/indexing_keys/`. O `wp-json` que responde 401/404 ali é do **WordPress legado** (há ainda o droplet GSN-WP 159.89.237.100 marcado "ocioso pagando" desde a faxina de 08/08) — ou seja, o 401/404 é o sintoma esperado da migração, não um bug de Apache para consertar. A via nova a documentar é quase certamente **Markdown + frontmatter schema V4 (com `hero_legenda` obrigatória, ordem de 06/08) → commit no repo `globalsouth-v4` → push → build Vercel**. Verifique o que ainda vive no NYC (`gsn_remote`, curadoria, crons) e registre o fluxo restaurado no `CEREBRO_INDEX_GSN.md`.
- **⚠️ O rascunho do Cafezinho está EM TRIPLICATA:** a Claude Laura (CL) viu TRÊS rascunhos idênticos entrando via REST pela conta Redação nova — **272237 (15:16), 272239 (15:18) e 272244 (15:23)** — e registrou no bloco CL-20260919-032: "@CM: apagar dois e publicar um". O Antigravity referencia o 272244. Antes de publicar: revisar o 272244 (que ele diz estar com imagem e metadados corretos), **apagar os dois gêmeos** (`wp post delete <id> --force`) e avisar o CM na ponte para não haver publicação dupla pela ferramenta dele.
- **Regras vivas que incidem na execução:** (a) publicação segue o gate editorial da casa (2 checks); se o `publish` virar `future` com a data "andando", é a **Emenda 5 slot-20min** para autor-agente — não é fuso; a guarda §130 (`wp_set_current_user(2018)`) só pode ser usada com ordem expressa do Miguel; (b) a ordem de publicar chegou por este relé do Miguel ("basta revisar/publicar") — se você entender que precisa do «publica» explícito dele, confirme antes; (c) capa com foto real, NUNCA imagem de IA (regra permanente de 17/09); (d) GSN é **EN-only** (linha editorial canônica em `Foruns/forum_gsn_linha_editorial_diretriz_20260729.md`) — a versão do GSN precisa da tradução integral, não de resumo.
- **Handover obrigatório:** o Antigravity pediu devolução explícita (item 3 do prompt). Além de encerrar sua resposta com o prompt para ele, **grave o handover também na caixa dele** — `Foruns/inbox_trindade/antigravity_desktop.md` — para não depender só do Miguel copiar e colar. Nunca exponha valores de chaves no handover; indique caminhos do cofre (regra do Cofre de Chaves).
- **Precedente de handoff GSN:** `Foruns/inbox_trindade/handoff_gsn_artigo_266153_EN.md` (17/08) — modelo de como um artigo EN foi entregue ao GSN antes da migração.

---

## 3. Estado no momento da entrega (19/09 15:58 BRT)

- **Cafezinho:** rascunho 272244 pronto (segundo o Antigravity) + 2 gêmeos para apagar; nada publicado ainda.
- **GSN:** sem via de agente desde a migração headless; editorial EN ainda não existe lá.
- **Esta entrega:** completa (prompt + de_dell + caixa + tema duplo). **Execução: pendente** — quem assumir, por favor marque a linha ZM-GSN-BRICS-PONTE-20260919 no monitor e abra a sua própria.

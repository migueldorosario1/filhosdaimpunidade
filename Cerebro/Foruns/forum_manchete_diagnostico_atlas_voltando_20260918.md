# 🎯 FÓRUM — DIAGNÓSTICO DO DISPOSITIVO DE MANCHETE (bronca Miguel 18/09 ~09:0x: "Atlas ficou voltando / manchete humana não está funcionando — está com bug?") — 18/09/2026

**Sessão:** ZCode/Kimi K3 (ZM, Dell) · **Tipo:** diagnóstico (nada alterado em produção) · **Memória irmã:** `Memorias/memoria_manchete_diagnostico_atlas_voltando_20260918.md`

## 1. Resumo (o que aconteceu / o que falta / o que preciso de você)

- **A manchete que o Miguel queria ESTÁ NO AR:** #271757 "Aprovação de Lula chega a 48% no Datafolha..." coroada pelo widget às 09:03, verificada no HTML ao vivo da home às 09:08, trava humana válida até 12:03. O widget 📌 funciona (grava wp_highlights + purga cache).
- **O dispositivo tem 3 bugs reais**, que juntos explicam a noite: (1) um **override esquecido de 23/08** (`/root/agent_data/manchete_lock_override` no NYC) faz o agente IGNORAR a trava humana em todas as rodadas — foi por isso que o agente derrubou a manchete #271729 do Miguel às 03:00 da manhã, com a trava ativa até 07:25; (2) o agente **lê a "manchete atual" da fonte errada** — o endpoint `get-manchete` retorna 404 (nunca funcionou: 871 rodadas no log, 0 leituras pelo endpoint) e o fallback lê o post mais novo da categoria Destaques (5087), que acumula posts e não é a manchete real; (3) a **rotação 24h funciona, mas a rede de segurança a anula**: quando todos os elegíveis estão na janela de 24h, o agente coroa o "melhor disponível" mesmo assim — como o Atlas tinha audiência 5-8× maior, foi recoroado 4× (15:00, 19:00, 21:00, 03:00).
- **Bug 2 em ação:** das 05:00 às 09:03 o agente achava que a manchete era a 271757 (via cat 5087) quando a home mostrava o Atlas (wp_highlights) — por isso não corrigiu nada de manhã.
- **Espelho:** cafezinho.news hoje é só redirect 301 → www.ocafezinho.com (o experimento acabou na prática; o título do widget "espelho" é herança confusa — o widget opera no canônico).
- **Falta (proposta, aguardando "vai"):** (a) remover o override (ou fazê-lo ceder só o lock binário, nunca a trava humana); (b) criar/corrigir o `get-manchete` (fonte única = wp_highlights, a mesma que a home renderiza); (c) rede de segurança anti-repetição: quando tudo estiver na rotação, preferir MANTER a manchete atual a recoroar um repetido; (d) alinhar os relógios de rotação (json local do agente × meta WP `_cafezinho_foi_manchete_em` — hoje divergem: a meta WP só é gravada quando o agente aplica de fato; o 271757 nunca teve meta WP).
- **Preciso de você:** o "vai" para aplicar as curas (a)+(b) são as estruturais. Se quiser a 271757 por mais tempo, estender a trava antes das 12:03.

## 2. Timeline reconstruída (BRT, provas no log do agente NYC)

| Hora | Evento |
|---|---|
| 17/09 15:00 | agente coroa Atlas 271516 (1ª vez) |
| 17/09 17:00 | rotação pula Atlas → coroa 271698 ✅ (rotação funcionando) |
| 17/09 19:00 | rede de segurança recoroa Atlas (2ª) — "melhor disponível" |
| 17/09 21:00 | rede de segurança recoroa Atlas (3ª) |
| 17/09 21:46 | CL publica 271757 (entra na cat 5087 — polui a leitura do agente) |
| 17/09 22:25 | 🔒 Miguel trava #271729 até 07:25 → home = 271729 ✅ |
| 17/09 23:00 | agente com override ignora a trava; campeão 271757; lê "atual"=271757 via cat 5087 → "nada a fazer" → a manchete do Miguel sobrevive por sorte |
| 18/09 01:00 | rodada aborta (WP REST 500 intermitente, já conhecido) |
| 18/09 03:00 | 💥 override ativo → todos elegíveis na rotação → rede de segurança → recoroa Atlas (4ª) e APLICA — home vira Atlas COM A TRAVA DO MIGUEL ATIVA |
| 18/09 05:00/07:00 | campeão 271757, mas cat 5087 diz que 271757 já é a manchete → "nada a fazer" → home segue Atlas |
| 18/09 ~08:3x | Miguel vê o Atlas na home ("ficou voltando") |
| 18/09 09:03 | Miguel trava #271757 até 12:03 → home = 271757 ✅ (provado 09:08) |

## 3. Os 3 bugs (detalhe)

1. **Override esquecido anula a trava humana.** `/root/agent_data/manchete_lock_override` (criado 23/08 04:37, conteúdo `MIGUEL-ORDER-NORMALIZE-LOCK-20260823`, era sobre o lock binário velho). Toda rodada loga "🔓 Travas de manchete CEDIDAS por override agentic". `checar_trava_humana()` retorna "sem trava" sem nem consultar a API. A trava do widget/API nunca vale contra o agente desde então.
2. **`get_current_headline()` lê a fonte errada.** `GET /wp-json/cafezinho/v1/get-manchete` = 404 (rota inexistente — provável snippet WPCode nunca criado/removido). Fallback = post mais recente da cat Destaques (5087), que acumula todo post já destacado e nunca é limpa. O agente escreve em wp_highlights (hello-highlight) mas lê de outro lugar → decisões cegas ("Campeão já é a manchete atual" falso).
3. **Rotação 24h × rede de segurança.** A rotação (json local + meta WP) pula corretamente quem foi manchete <24h; mas quando o pool elegível (alinhamento 5 + capa verificada + fora da rotação) zera — comum à noite —, a rede coroa `ranked[0]` mesmo repetido. Atlas (aud 0.85-0.93 vs ~0.1 do resto) foi sempre o "melhor disponível". Comportamento documentado como intencional ("repete em vez de deixar a home vazia"), mas o efeito prático é a repetição que o Miguel viu.

**Agravante menor:** no caminho "nada a fazer" o agente RENOVA o carimbo local de rotação do campeão reinante (by design, "24h depois de sair da manchete"), mas não grava a meta WP — os dois relógios divergem.

## 4. Provas

- wp_highlights = 271757 (4 linhas "Manchete"); home ao vivo com h1 da 271757 (09:08).
- API `manchete-humana` do canônico: `{post_id:271757, trava:true, lock_until 12:03, autor James2017, origem widget}`.
- cmh_historico do canônico = exatamente o que o Miguel colou no chat (o widget é do canônico).
- `get-manchete` → 404 rest_no_route; log NYC: 871× "via cat Destaques", 0× leitura pelo endpoint.
- 271757: cat 5087 presente (entrou na publicação ~21:46) — por isso o fallback de leitura a retorna.
- 271757 sem selo de capa mas RENDERIZA: o gate aceita por marcador "flickr" no blob do anexo 271769 (foto Lula Flickr). Sem problema de imagem.
- Meta WP `_cafezinho_foi_manchete_em`: 271516 = 1789711254 (03:00 BRT — a coroação da madrugada); 271757 nunca teve a meta WP.
- Override: `-rw-r--r-- Aug 23 04:37 /root/agent_data/manchete_lock_override`.

## 5. Arquivos relevantes (nada alterado)

| Onde | Arquivo | Papel |
|---|---|---|
| NYC | `/root/agente_manchete.py` | agente das horas pares; override linha ~50, trava linha ~648, leitura errada linhas 197-221, renovação do carimbo no no-op linha 724 |
| NYC | `/root/agent_data/manchete_lock_override` | o vilão da trava (37 bytes, 23/08) |
| WP | `mu-plugins/cafezinho-real-image-gate.php` | hero: wp_highlights validado → ranking do agente → fallback por data (rotação via meta WP, rede de segurança, vilão) |
| WP | `mu-plugins/cafezinho-manchete-humana.php` | o widget 📌 (grava wp_highlights + cmh_estado + purga) |

— ZCode/Kimi K3 (ZM, Dell) · 18/09/2026 ~09:1x BRT

---

## ADENDO — CURA APLICADA ("vai" do Miguel, executado 19/09 ~02:4x BRT; o "vai" dele chegou 18/09 ~09:4x mas o Dell ficou suspenso ~17h — fila só processou na madrugada)

**Aplicado e provado (NYC, `/root/agente_manchete.py`, backup `.bak_pre_cura_manchete_20260918`):**
1. ✅ **Override removido** — `/root/agent_data/manchete_lock_override` virou `.bak_20260918`. A trava humana volta a ser sagrada (o arquivo de 23/08 cedia TODAS as travas; foi ele quem derrubou a #271729 às 03:00).
2. ✅ **Leitura da manchete de verdade** — como o `get-manchete` é 404 desde sempre e o WP estava inacessível, o agente ganhou leitura pelo **hero renderizado da home** (h1.manchete-titulo → rel=shortlink → ?p=ID), via www (camada viva). Prova ao vivo: retornou 272107 (a manchete real da madrugada). A cat 5087 virou último recurso (rotulada "MENOS FIEL" no log).
3. ✅ **Rede anti-repetição** — `escolher_campeao_v2(ranked, current_id)`: se o pool elegível zera (rotação/capa), MANTÉM a manchete atual em vez de recoroar repetido. Teste unitário 4/4 no NYC (manter / ranked[0] fora do pool / fresco vence / sem capa não mantém).
4. ✅ **Relógio único da rotação** — o caminho no-op ("já é a manchete") agora também grava a meta WP `_cafezinho_foi_manchete_em` (antes só o json local — os dois relógios divergiam).

**Pendente (bloqueado pelo servidor WP fora — ver incidente abaixo):** (a) endpoint `get-manchete` de verdade no WP (hoje desnecessário enquanto a leitura-pelo-hero funcionar); (b) renomear o widget p/ "Manchete Humana — canônico" (cosmético); (c) o cmh_estado com a trava de 18/09 09:03-12:03 segue gravado (lazy expiry — limpar quando o WP voltar).

**Estado da manchete:** 271757 (a escolha do Miguel) reinou 09:03→23:00 (14h); às 23:00 o agente coroou 271987 e o render da home segue o post 272107 (Merz×China, publicado 23:36) — home fresca, leitores vendo tudo normal.

**🔴 INCIDENTE NOVO (19/09 ~02:5x):** servidor WP (ServerDoIn 190.89.239.65) fora p/ **SSH + REST/controle** desde ~18/09 23:40 (última escrita viva: 23:36). Site NO AR p/ leitores (www responde rápido e fresco — camada CF/edge). ICMP ok, TCP 22/443 mortos p/ acesso direto; controle = 522 via CF. Sem acesso ao painel ServerDoIn nos cofres → **recuperação = Miguel no painel (reboot) se não voltar sozinho**. Enquanto durar: esteira de fios, tampão, baleia e agente de manchete abortam limpo (provas: rodada 04:00 UTC abortou; agente fail-safe).

**Lição de infra (registrada):** o Dell voltou de suspensão com o relógio congelado ~17h — toda leitura de data/hora desta sessão foi validada contra Google (`curl -sI google.com | grep -i ^date:`) antes de concluir. Desconfiar de timestamps do Dell pós-suspensão até o NTP acertar.

— ZCode/Kimi K3 (ZM, Dell) · 19/09/2026 ~02:5x BRT

---

## ADENDO 2 — REGRA DA JANELA AFINADA: de dia SÓ Política/Eleições (ordem Miguel 19/09 ~10:0x) + WP voltou + widget renomeado

**A ordem (quase literal):** "de manhã a manchete tem que ser só nacional, só assunto de política nacional — tecnologia/geopolítica só à noite; até as eleições, melhor ficar só nacional; eleição de preferência; eventualmente algum regional importante."

**Caso que disparou:** a manchete renderizada de manhã era "Diário de Anne Frank... Bienal de SP" (272085) — nacional-GERAL (cat 21141 Nacional), fora do espírito da régua. E antes disso, Merz×China (internacional) reinou até as 07:00 BRT (a janela começa 08h — correto pela regra de 15/09, mas o Miguel quer o dia inteiro político).

**Por que furou:** a régua de 15/09 aceitava 'nacional' puro (cat 21141) — e a esteira marca notícia geral como Nacional. Afinado nos DOIS pontos de decisão:
1. **Gate (render da home):** `cafezinho_post_is_nacional_politica_eleicoes` e a `tax_query` da janela agora aceitam só `politica/politica-2/eleicoes-*` (categoria OU tag). Degrau anti-vazio novo: se nem assim houver nada elegível (com ou sem selo), alarga para o conjunto antigo (com nacional) — a home nunca fica vazia. Backup `.bak_pre_janela_politica_20260919`. Provas com wp eval: 271987 (Política)=SIM, 272085 (Nacional puro)=NÃO, 272107 (internacional)=NÃO.
2. **Agente (NYC):** janela 08-22h BRT filtra candidatos a Política (22)/Eleições (5088)/tags equivalentes ANTES do ranking; à noite (22-08h) segue livre. Prova ao vivo: "10/25 posts elegíveis". Bônus: a rede final agora **nunca coroa post sem capa verificada** (caso 12/09: coroou o 271987 sem capa e a home mostrava o fallback Anne Frank — o agente coroava uma coisa e o leitor via outra).

**Manchete agora:** "Lula defende drones... Trump está atrás de minerais críticos" (271987, Política) — capa era foto REAL de Lula em cerimônia militar que estava sem selo; QA visual feito (foto real, sem artefato IA), selo `cafezinho_image_kind=real` + `_cafezinho_img_check` aplicados, home purgada e provada (h1 ao vivo). Trava: livre (a de ontem expirou limpa).

**Servidor WP voltou** (SSH+REST) — a pane de ontem ~23:40→hoje ~06:0x ficou sem explicação à vista (rede do provedor); nada a fazer.

**Widget renomeado:** "Manchete Humana — canônico (www.ocafezinho.com)" (era "EXPERIMENTO (espelho)"); strings internas idem. Backup `.bak_pre_rename_canonico_20260919`. O get-manchete morreu de vez: a leitura pelo hero da home é melhor (sobrevive ao controle fora).

**Rodada E2E final (19/09 10:2x BRT):** janela ativa → 10/25 elegíveis → campeão 271987 → lido como atual via hero → MANTIDO (anti-repetição) → "nada a fazer" + meta de rotação renovada. Todas as curas operando juntas.

— ZCode/Kimi K3 (ZM, Dell) · 19/09/2026 ~10:3x BRT

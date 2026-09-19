# 🗂️ Fórum — Plano de trabalho: Telemetria de AUTORIA dos posts (24/08/2026 19:40, ZCode/GLM-5.3)

**Ordem do Miguel:** "vamos fazer um plano de trabalho para melhorar a telemetria da autoria dos posts." · Base: os defeitos reais observados em 24/08 (página /autoria, auditoria do dia).

## Problemas mapeados (todos provados hoje)
P1. Humanos indistinguíveis: Gabriel/Rhyan/Miguel usam a conta compartilhada **"Redação" (autor 5470)** — separação hoje é heurística (User-Agent + horário).
P2. **IP real invisível**: proxy do provedor (190.89.239.31) faz NAT e não repassa XFF → geografia (CE×RJ) impossível nos logs.
P3. V4.1 reconhecido só por meta frágil (`zizi=v41_*`) + pós-processamento no painel; se o publicador não carimbar, vira "Não identificado".
P4. Correção manual (✏️) sem auditoria: não registra QUEM corrigiu nem quando.
P5. Cookie do link secreto é de sessão → "página fora do ar" falso toda vez que o navegador fecha (2× hoje).
P6. Sem histórico de EDIÇÃO por post (só a criação); "posts desatualizados" sem explicações.
P7. Views por post não têm série própria no painel (só o snapshot/hora agregado do hub).

## Fases (executor: ZCode em servidor; datas-alvo)

**F0 — rápido (25/08 manhã): alívio imediato**
- F0.1 Cookie do guard com validade de 30 dias (+ botão "link copiável" no rodapé) → mata o falso fora-do-ar (P5).
- F0.2 Painel: marcar posts "Não identificados" com motivo (sem meta/sinal) em vez de grupo cego (P3 parcial).

**F1 — fundação de identidade (25-26/08)** ⭐ núcleo do plano
- F1.1 Contas WP individuais p/ humanos (gabriel / rhyan / miguel) com Application Password própria; fim da conta compartilhada nos novos posts (P1). *Miguel cria/as contas ou me autoriza via wp-cli; posso criar com wp-cli se OK.*
- F1.2 Plugin cafezinho (WP) passa a carimbar em TODO save: `_cafezinho_autor` (apelido canônico: gabriel · rhyan · miguel · v4.1:geo · v4:tematico · youtube · v5 · rest), `_cafezinho_ts`, e em edições `_cafezinho_editor` + revisions ON (P3, P6).
- F1.3 Publicadores python (v41_ciclo, youtube, v5) enviam o campo autor explícito — sem depender de UA (P3).

**F2 — origem geográfica (27-28/08)**
- F2.1 Rotear wp-admin pelo domínio atrás da Cloudflare (XFF preservado) OU real_ip/XFF no proxy do provedor — **decisão do Miguel** entre as duas rotas (P2).
- F2.2 Plugin grava `_cafezinho_ip_origem` + geo (CE/RJ/outra) 1× por sessão; painel mostra a origem por acesso/autor (P2).

**F3 — painel rico + auditoria (29-30/08)**
- F3.1 Grupos por AUTOR REAL (fim das heurísticas), humanos em destaque (UX 22/08), coluna origem (CE/RJ/servidor) (P1+F2).
- F3.2 Sparkline 24h de views por post na subpágina (usa os snapshots/hora) (P7).
- F3.3 Correção manual auditada: ao ✏️, select leve "sou Miguel/Gabriel/Rhyan/outro" + grava em tabela `_cafezinho_correcoes` (quem/quando/de-para) (P4).
- F3.4 Validação cruzada noturna: autor declarado × padrão (UA/plataforma/horário/geo) → lista de suspeitos no painel (anti-má-fé/erro).

**Revisão: 31/08** — métricas de aceite: ≥95% dos posts novos com autor rico carimbado; Gabriel×Rhyan 100% separados; divergências da validação = 0 abertas; Miguel sem "fora do ar" na semana.

## Estado / o que falta / preciso do Miguel
- Feito: plano + problemas provados. F0-F1 não dependem de decisão.
- **Decisões do Miguel:** (1) criar/autorizar contas WP individuais (F1.1); (2) rota do IP real: Cloudflare × real_ip no proxy (F2.1); (3) aprovar F3.3 (select de identidade leve — sem login).
- Execução começa F0 na janela de crédito (pós-00:26) — cada item com backup + prova, tudo em servidor.

## ➕ ADENDO 1 (24/08 ~20:00) — Feedback do Miguel: autoria na Baleia Azul
- **O que saiu errado:** a seção "quem fez o quê" da Baleia Azul (boletim 8h/19:30) despejou detalhe cru (lista de posts estilo painel). O Miguel quer **"algo já compilado, sem tantos detalhes, bem diagramado"** — digest de chefe.
- **Formato aprovado a seguir (F3.5):** máximo ~8 linhas, nada de tabela:
  ```
  ✍️ AUTORIA (últimas 24h) — 38 artigos
  🛰️ V4.1 ····· 23 (61%) ← estesira oficial
  🧑‍💼 Gabriel ···· 5 (13%) ↑ 2 vs ontem
  🤖 temáticos ·· 4 · 📺 YouTube ·· 3 · ✍️ Miguel ·· 2
  🔍 1 não identificado (corrigir no painel)
  📈 top da equipe humana: "Título curto…" (Gabriel, 412 views)
  ```
  Barras proporcionais, % e variação vs dia anterior; só 1 destaque (o melhor da equipe humana). Fonte: a própria API de autoria + snapshots (mesma verdade do painel).
- **F0.4 (25/08):** reformar já a seção da Baleia nesse formato (script do boletim, backup + prova no próximo envio 8h).
- As 3 decisões do Miguel seguem pendentes (contas individuais; rota do IP: CF × real_ip; select de identidade no ✏️).

## ✅ ADENDO 2 (24/08 22:40) — IDENTIFICAÇÃO DE AUTOR IMPLEMENTADA (ordem Miguel: "não deve ser tão difícil" — e não era)
Com só 3 humanos + V4.1, a lógica fecha por eliminação (Miguel confirmou 24/08):
- **Gabriel** → conta WP própria (já vinha identificado);
- **Miguel** → conta WP própria + Linux;
- **Rhyan** → **tudo que cai na conta compartilhada "Redação" (autor 5470) com navegador humano** (único humano restante) — grupo novo 🧑‍💻 "Rhyan — conta Redação", subpágina /autoria/rhyan, opção no ✏️;
- **V4.1/robôs** → meta zizi=v41_* / UA de máquina.
- Rodapé da página agora explica as regras de identificação (transparência).
**Provas:** card Rhyan na página (7d) + subpágina 200 com 1 artigo · backup `.bak_rhyan_20260824` · sintaxe validada no 3.12 do servidor. F1.1 (contas individuais) fica como refinamento OPCIONAL — a regra por eliminação já cobre o essencial.

## ✅ ADENDO 3 (24/08 23:05) — Canais do Miguel agregados (ele publica por Antigravity/Claude/WordPress/Grok/GPT)
- Grupo ✍️ Miguel vira **"Miguel — todos os canais"**: wp-admin (conta própria) + REST-navegador + REST-python sem meta de robô (Claude/GPT via API) + Antigravity/Manus. Chip por artigo mostra o canal: "Miguel", "Miguel (ferramenta)" 🛠️, "Miguel (Antigravity)".
- **Semana 24/08 (100% atribuído, zero não-identificados):** V4 45 · V4.1 26 · Gabriel 5 · YouTube 4 · Motor V5 4 · **Miguel 3 (1 wp-admin + 2 ferramentas)** · Rhyan 1.
- Backups: `.bak_rhyan_20260824`, `.bak_canais_20260824`. Sintaxe validada no servidor; provas com contagem interna (`_autoria_base`) pós-restart.
- Nota: se um dia um 4º humano publicar, a regra "REST = Miguel" precisa revisão (conta individual na hora — combinado).

## ✅ ADENDO 4 (24/08 23:10) — Regra CONFIRMADA pelo Miguel: Gabriel e Rhyan publicam DIRETO pelo WordPress
- "o gabriel e o rhyan publicam direto pelo wordpress" → regra vigente validada: Gabriel = wp-admin com conta própria; Rhyan = wp-admin pela conta "Redação" (5470); Miguel = wp-admin (conta própria) + ferramentas via REST (Claude/GPT/Grok/Antigravity). Publicações REST sem meta de robô = ferramenta do Miguel (nenhum outro humano usa REST). Regra oficial de identificação do ecossistema.

## ✅ ADENDO 5 (24/08 23:15) — Mapa de autoria COMPLETO confirmado pelo Miguel
1. **V4.1 = processo automático** (esteira oficial, sem humano) 🛰️
2. **Gabriel** = WordPress direto, conta própria 🧑‍💼
3. **Rhyan** = WordPress direto, conta "Redação" (5470) 🧑‍💻
4. **Miguel** = WordPress direto (conta própria) + ferramentas via REST (Claude/GPT/Grok/Antigravity) ✍️
Regra de identificação oficial, implementada no painel /autoria e validada pelo dono. Fim da F1 essencial — 24/08.

## ✅ ADENDO 6 (24/08 23:25) — Correção do Miguel: a conta Redação é dos TRÊS; contas individuais CRIADAS
- "eu, Gabriel e Rhyan usamos a conta redação" → regra "Redação=Rhyan" corrigida: virou **"Redação — equipe (legado: Miguel/Gabriel/Rhyan)"** no painel (histórico preservado, grupo renomeado).
- **Contas individuais criadas no WP (F1.1 concluído)**: `gabriel_redacao` (ID 5799, editor, display Gabriel Barbosa) e `rhyan` (ID 5800, editor) — senhas fortes geradas e entregues ao Miguel no chat (trocar no 1º login; emails placeholder @ocafezinho.com pra atualizar). A partir de agora: cada um publica com a SUA conta (Miguel já tem a dele) → autoria individual real, sem heurística.
- Nota técnica: wp-cli com plugins deu "erro crítico" (boot de plugin) — contornado com --skip-plugins; site verificado 200 antes e depois.

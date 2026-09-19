# 🧠 MEMÓRIA — Diagnóstico do dispositivo de manchete (Atlas voltando / trava humana derrubada) — 18/09/2026

**Sessão:** ZCode/Kimi K3 (ZM, Dell) · **Gatilho:** bronca do Miguel 18/09 ~09:0x ("a manchete humana não está funcionando; a do Atlas ficou voltando; a gente não tinha anti-repetição?") · **Fórum irmão:** `Foruns/forum_manchete_diagnostico_atlas_voltando_20260918.md` · **Tipo:** diagnóstico puro (zero alteração em produção)

## 1. Arquitetura real da manchete (mapa vivo, conferido no código 18/09)

```
Miguel (widget wp-admin canônico, "Manchete Humana — EXPERIMENTO (espelho)")
   └─ escreve: wp_highlights (name='Manchete') + option cmh_estado {post_id,desde,ate,autor} + cmh_historico + purga Rocket
Agente NYC (/root/agente_manchete.py, cron horas pares UTC)
   └─ escreve: hello-highlight via snippet WPCode 229816 (set-manchete) + cat 5087/Redação no post + meta WP _cafezinho_foi_manchete_em + json local manchete_historico.json + option cafezinho_manchete_ranking (fallback da home)
Home (render, gate mu-plugins/cafezinho-real-image-gate.php → cafezinho_get_real_highlight('Manchete'))
   └─ lê wp_highlights; valida: capa real verificada + não-no-home(20699) + janela nacional 08-22h
      → se falha: RANKING do agente (<3h) → fallback por data (60 posts, rotação via meta WP, vilão-pessoa) → redes de segurança
Espelho cafezinho.news: REDIRECT 301 → www.ocafezinho.com (experimento encerrado na prática)
```

Fonte da verdade que a home renderiza = **wp_highlights**. O widget e o agente escrevem nela. O agente LÊ de outro lugar (ver bug 2).

## 2. Os 3 bugs (com linhas de código)

### Bug 1 — override de 23/08 anula a trava humana
- `/root/agent_data/manchete_lock_override` (37 bytes, `MIGUEL-ORDER-NORMALIZE-LOCK-20260823`, mtime 23/08 04:37).
- `agente_manchete.py` ~l.649-651: se o arquivo existe, `checar_trava_humana()` loga "🔓 Travas de manchete CEDIDAS por override agentic (ordem Miguel/chefe CM) — prosseguindo" e retorna False SEM consultar a API cmh nem o lock binário.
- Contexto da ordem de 23/08 ~01:45: fazer o lock binário ceder a ordens de agente. Na época a trava humana com validade (widget, 19/08+) não era o fluxo principal do Miguel. Hoje o override anula TAMBÉM a trava humana — e é ela que o Miguel usa toda noite.
- Consequência real: 18/09 03:00 BRT o agente aplicou a manchete Atlas por cima da trava humana #271729 (válida até 07:25).

### Bug 2 — o agente lê a "manchete atual" da fonte errada
- `get_current_headline()` (l.197-221): tenta `GET /wp-json/cafezinho/v1/get-manchete` → **404 rest_no_route (a rota não existe)** → fallback: post mais recente da categoria 5087 (Destaques).
- Log confirma: 871 ocorrências de "Manchete atual (via cat Destaques)" e ZERO de "Manchete atual: post_id=" (sucesso do endpoint) — nunca funcionou neste log.
- A cat 5087 nunca é limpa: `apply_headline()` (l.224-230) ADICIONA 5087+Redação ao post coroado e ninguém remove dos antigos; posts também entram por fluxo editorial (271757 entrou na publicação ~21:46 — prova: 02:00 UTC o fallback já a lia como "atual").
- Consequência real: 18/09 05:00 e 07:00 BRT o campeão era 271757 e o cat-read dizia "atual=271757" → "Campeao ja e a manchete atual. Nada a fazer." — enquanto a home mostrava o Atlas (wp_highlights=271516 desde 03:00). O agente ficou cego ao próprio erro por 6h.

### Bug 3 — rotação 24h funciona, mas a rede de segurança repete
- `escolher_campeao_v2()` (l.505-530): top-3 exige capa_ok + fora da rotação (<24h) + juiz ≥4; rede 1 varre o ranking por "com capa e fora da rotação"; rede 2 (l.529-530) = `ranked[0]` mesmo repetido ("melhor disponível").
- Pool noturno pobre (a maioria morre no alinhamento<5 ou sem capa) + Atlas com aud 5-8× o resto → Atlas recoroado 4× em 12h (15:00, 19:00, 21:00, 03:00). A rotação PULOU o Atlas em todas as rodadas ("já foi manchete há Xh — pulado"); a rede o reelegeu.
- No gate (home, l.517-528) existe a mesma rede: se todos elegíveis têm meta <24h, refaz a query sem a rotação.
- Agravante: no caminho no-op ("já é a manchete"), `registrar_como_manchete()` (l.724) RENOVA o carimbo local do campeão — by design ("24h após sair da manchete") — mas a meta WP NÃO é renovada nesse caminho (só no apply, l.735-736). Os dois relógios divergem: para o gate da home, a 271757 nunca foi manchete.

### Não-bugs verificados (descartados com prova)
- Widget 📌: grava wp_highlights + purga; home mostrou 271757 na hora (h1 provado 09:08).
- Capa da 271757 sem carimbo `_cafezinho_img_check`: o gate aprova por marcador textual "flickr" no blob do anexo 271769 (`cafezinho_post_has_verified_real_image`, l.254-264). Renderiza legitimamente.
- Expiração da trava: lazy expiry normal; às 07:25 expirou sozinha (mas a home já era Atlas desde 03:00 pelo bug 1).
- Rodada 01:00 BRT (04:00 UTC) abortou por WP REST 500 intermitente (conhecido, retry 3× já existe na esteira; aqui abortou limpo).

## 3. Timeline BRT (prova: /root/agent_data/agente_manchete.log + cmh_historico + wp meta)

15:00 coroa Atlas · 17:00 coroa 271698 (rotação ok) · 19:00 Atlas de novo (rede) · 21:00 Atlas de novo (rede) · 21:46 CL publica 271757 c/ cat 5087 · 22:25 Miguel trava 271729 (home obedece) · 23:00 agente ignora trava (override), campeão=271757, cat-read=271757 → no-op (trava sobrevive por sorte) · 01:00 aborta (500) · 03:00 💥 rede recoroa Atlas e APLICA por cima da trava · 05:00/07:00 no-op cego (bug 2) · 09:03 Miguel trava 271757 (home corrige) · próximas rodadas 11:00/13:00: campeão provável = 271757 líder disparado (aud 0.416 vs 0.117) e cat-read=271757 → no-op esperado, mas sem garantia.

## 4. Comandos usados (reprodução)

```bash
# estado atual da trava humana (público)
curl -s -H 'User-Agent: Mozilla/5.0 ...' https://controle.ocafezinho.com/wp-json/cafezinho/v1/manchete-humana
# hero real da home
curl -s https://www.ocafezinho.com/ | grep -oE '<h1[^>]*>.*?</h1>' | head -3
# prova do endpoint quebrado
curl -s ... https://controle.ocafezinho.com/wp-json/cafezinho/v1/get-manchete   # 404 rest_no_route
# highlights no banco
ssh cafezinho-wp "cd /var/www/ocafezinho && wp db query 'SELECT * FROM wp_highlights' --allow-root"
# histórico do widget (canônico)
ssh cafezinho-wp "... wp option get cmh_historico --format=json --allow-root"
# log do agente
ssh nyc 'grep -E "Travas|Campeao|Setando|Nada a fazer" /root/agent_data/agente_manchete.log'
# override
ssh nyc 'cat /root/agent_data/manchete_lock_override'   # MIGUEL-ORDER-NORMALIZE-LOCK-20260823
```

## 5. Plano de cura proposto (AGUARDA "vai" do Miguel — nada aplicado)

1. **Trava humana volta a valer:** `mv /root/agent_data/manchete_lock_override{,.bak_20260918}` (ou cirúrgico: override cede só o lock binário, nunca a trava da API). Recomendado remover — a trava com validade expira sozinha, não precisa de override anti-esquecimento.
2. **Fonte única de leitura:** criar o endpoint `get-manchete` (snippet WPCode irmão do 229816) lendo wp_highlights name='Manchete'; ou o agente ler a option cmh_estado/wp_highlights via REST. Fim do fallback cego pela cat 5087.
3. **Rede anti-repetição mais humana:** quando todos elegíveis estiverem na rotação, preferir MANTER a manchete atual (não trocar por repetido); se a atual também estiver inválida, escolher o menos-recentemente-coroado em vez do ranked[0].
4. **Relógio único da rotação:** gravar a meta WP também no no-op (ou o agente passar a ler a meta WP em vez do json local — a meta é a que o gate respeita).
5. (Cosmético) Renomear o widget para "Manchete Humana — canônico" (o espelho é redirect desde ?; título atual confunde).

Rollback de cada passo: (1) restaurar o arquivo; (2) apagar o snippet; (3)-(4) .bak do agente; (5) editar o mu-plugin.

## 6. Riscos/pendências

- Sem o passo 1, qualquer trava do Miguel pode ser atropelada na próxima hora par UTC se o campeão ≠ manchete lida via cat 5087. Hoje às 11:00 BRT o risco é baixo (271757 lidera e é o lido via cat), mas não zero.
- O log "aviso: filtro so-nacional indisponivel (time data '' does not match format...)" aparece em TODAS as rodadas — o filtro nacional do agente está inerte (o gate da home segura a régua 08-22h no render, então não vazou manchete internacional de dia; vale olhar numa próxima sessão).

— ZCode/Kimi K3 (ZM, Dell) · 18/09/2026 ~09:1x BRT

---

## ADENDO TÉCNICO — CURA (19/09 ~02:4x-03:0x BRT, "vai" do Miguel processado após suspensão de ~17h do Dell)

### O que mudou no `/root/agente_manchete.py` (NYC; backup `.bak_pre_cura_manchete_20260918`; py_compile OK)

1. **Override removido:** `mv /root/agent_data/manchete_lock_override{,.bak_20260918}` → `checar_trava_humana()` volta a consultar a API cmh (e o lock binário legado). Era a causa da trava do Miguel ter sido atropelada às 03:00 de 18/09.
2. **`get_current_headline()` reescrito (ordem nova):** (1) endpoint get-manchete (se um dia existir); (2) **hero renderizado da home** — `requests.get("https://www.ocafezinho.com/")` → regex `<h1[^>]*class="manchete-titulo"[^>]*>\s*<a[^>]*href="..."` → GET da página → `rel=['"]shortlink['"] ... ?p=(\d+)` → post_id. Prova ao vivo 19/09 02:53: retornou `{'post_id': 272107}` (a manchete real no ar). Funciona MESMO com o controle fora (www é outra camada). (3) cat 5087 como último recurso, log marcado "MENOS FIEL".
3. **Rede anti-repetição:** `escolher_campeao_v2(ranked, current_id=None)` — antes da rede final `ranked[0]`, se o pool elegível zerou (rotação/capa) e a manchete ATUAL está no pool com capa, retorna a atual (log "MANTENDO a manchete atual ... em vez de recoroar repetido"). Em `main()`, `get_current_headline()` passou a ser chamado ANTES da eleição para alimentar `current_id`.
4. **Relógio único:** no caminho no-op ("Campeao ja e a manchete atual"), além de `registrar_como_manchete()` (json local), grava também a meta WP `_cafezinho_foi_manchete_em` (a que o gate da home respeita).

### Provas
- Teste unitário 4/4 no NYC (`/tmp/teste_campeao.py` contra o `manchete_historico.json` real): mantém atual / ranked[0] se atual fora do pool / fresco fora do top-3 vence sem custo de juiz / atual sem capa não é mantida.
- Leitura ao vivo do hero: 272107 ✓ (controle esgotando em 15s antes → fallback correto).
- `py_compile` OK; nenhum custo de LLM nos testes (juiz nunca disparado).

### Pendente quando o WP voltar (SSH/REST)
- Endpoint `get-manchete` (mu-plugin) — hoje supérfluo (o hero-parse cobre), útil p/ auditoria.
- Renomear o widget "espelho"→canônico (cosmético) + limpar o cmh_estado velho (trava 18/09 09:03-12:03, lazy expiry).
- Filtragem "só-nacional" do agente inerte (aviso em toda rodada: "time data '' does not match format") — o gate da home segura a régua no render, mas vale curar.

### 🔴 Incidente: WP ServerDoIn fora p/ SSH+REST desde 18/09 ~23:40
- Sintomas: TCP 22 e 443 diretos mortos (ICMP vivo, RTT 141-800ms instável); controle via CF = 522; www (HTML) 200 rápido e fresco. Última escrita viva conhecida: 23:36 (post 272107). Rodada do agente das 04:00 UTC abortou.
- Efeito: esteiras que usam controle (fios, tampão, baleia, agente) abortam limpo até voltar. Leitores não afetados.
- Cofre: sem credencial de painel ServerDoIn — só SSH key + senha root (`Outros/chaves/ssh_servidor_wp_cafezinho.md`, gitignored). Recuperação depende do painel (Miguel) ou de voltar sozinho.
- Palpite: rede do provedor (perda/latência), não fail2ban (não houve falhas de auth; ICMP passa).

### Lição de infra (Dell)
O Dell voltou de suspensão com o relógio preso ~17h atrás; o NTP corrigiu no meio da sessão. Regra prática: em timestamps estranhos após retomar o Dell, validar com `curl -sI https://www.google.com | grep -i ^date:` antes de raciocinar sobre horários.

— ZCode/Kimi K3 (ZM, Dell) · 19/09/2026 ~03:0x BRT

---

## ADENDO 2 TÉCNICO — Janela política (19/09 ~10:0x-10:3x BRT)

### Regra nova (ordem Miguel, refinando 15/09)
- 08h-22h BRT: manchete SÓ Política (cat 22, slug `politica-2`) ou Eleições 2026 (cat 5088) — categoria OU tag (`politica`, `eleicoes-2026`, `eleicoes`). **'nacional' (21141) puro NÃO qualifica mais de dia.**
- 22h-08h: livre (tecnologia/geopolítica ok).

### Implementação
- **Agente NYC** (`agente_manchete.py`, backup `.bak_pre_cura_manchete_20260918`): `janela_politica_ativa()` (timezone fixo -3), `resolver_tags_janela()` (REST /tags?slug=..., ids vivos hoje: 16/4597/5602), `post_elegivel_janela()`; filtro aplicado em `main()` logo após o fetch (pool vazio → mantém a atual e sai); `_fields` do fetch ganhou `tags`. Rede final nova: nunca coroa `capa_ok=false` (walk "melhor COM capa mesmo repetido" antes do ranked[0]). Prova: rodada manual 13:28 UTC — "10/25 elegíveis", campeão=atual=271987, meta de rotação renovada, sem escrita indevida.
- **Gate WP** (`cafezinho-real-image-gate.php`, backup `.bak_pre_janela_politica_20260919`, php -l OK): `cafezinho_post_is_nacional_politica_eleicoes` e `cafezinho_manchete_nacional_tax_query()` sem 'nacional'; tax_query ganhou parâmetro `$incluir_nacional=false`; **degrau anti-vazio** novo após o sem-selo: se nada elegível, alarga p/ o conjunto antigo (com nacional) — home nunca vazia. Provas wp eval: 271987 SIM, 272085 NÃO, 272107 NÃO.
- **Widget** (`cafezinho-manchete-humana.php`, backup `.bak_pre_rename_canonico_20260919`): renomeado p/ "Manchete Humana — canônico"; strings de histórico sem "espelho".

### Manchete imediata (caso 271987)
- Capa 271990 = foto REAL de Lula em cerimônia militar (QA visual direto; sem caption/marcadores → gate barrava). Selado `cafezinho_image_kind=real` (post+anexo) + `_cafezinho_img_check` + rocket_clean_domain → hero = 271987 provado.

### Lições novas
1. **Rodar o agente na mão = SEMPRE `/root/venv/bin/python3 agente_manchete.py`** (o sistema não tem PIL; o import dinâmico do v4w quebra fora da venv — cron usa venv, por isso nunca falhou).
2. O ranking publicado no WP encolheu p/ 1 item de dia (só o que passa alinhamento=5 + janela) — esperado; o gate revalida mesmo assim.
3. API manchete-humana faz lazy expiry correto (trava de ontem expirou limpa; hoje mostra trava:false + o post atual 271987).
4. Cron do agente: `0 */2 * * *` (horas pares UTC), pausa em `/root/controles_pause/manchete.pause`, stdout em `agent_data/manchete.log` (o log() interno vai p/ `agente_manchete.log`).

— ZCode/Kimi K3 (ZM, Dell) · 19/09/2026 ~10:3x BRT

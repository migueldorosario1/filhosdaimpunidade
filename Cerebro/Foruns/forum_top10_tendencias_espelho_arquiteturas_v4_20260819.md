# 🏛️ Fórum — Sprint 19/08 (2ª parte): Top 10 Tendências na home do espelho + arquiteturas V4 (tendências, anti-repetição, autoaprendizado, Constituição de Estilo)

> **Quem:** ZCode (Kimi K3 → failover DeepSeek) · **Quando:** 19/08/2026 10:55→11:30 BRT · **Ordem do Miguel** (voz, ~10:55, retomando sprint de outra sessão)
> **Tema Duplo:** este fórum + `Memorias/memoria_top10_tendencias_espelho_20260819.md`

---

## §1. ENTREGUE E NO AR — Box "Top 10 Tendências" no espelho

**O que o Miguel pediu:** box com os mais vistos das últimas 24h (metodologia da página Tendências da Baleia Azul), **sem número de views, sem tags**, como **primeiro bloco depois da manchete** na home do espelho.

**Como ficou (em produção no espelho):**
- **NYC:** `/root/top_tendencias_push.py` — consulta GA4 (propriedade 374552425, mesma da Baleia/manchete; pagePath→slug, acumula `/amp`), score `hoje + ontem×0,3` (padrão da casa), monta o Top 10 de posts das últimas 48h e **empurra** via REST p/ o espelho. Cron `25 * * * *` (horário; backup `crontab_backup_pre_top10_20260819.txt`).
- **Espelho:** mu-plugin `cafezinho-top-tendencias.php` — endpoint `POST/GET /wp-json/cafezinho/v1/top-tendencias` (auth app-password `edit_posts`) guarda a option `cafezinho_top10` (só posts já espelhados e publicados; no-home 20699 fica fora) + renderer chamado pelo `front-page.php` logo após a manchete (backup `front-page.php.bak_pre_top_tendencias_20260819`). O box **não repete a manchete atual** e mostra "atualizado às HH:MM".
- **Verificado na home (11:21):** posição manchete→box→banners ✓; conteúdo: Ciro/Mossad, Ex-comandante FAB/golpe, Irã mísseis, Lula×Putin, Antipetismo/Flávio etc. — só títulos linkados, sem views, sem tags.

## §2. ENTREGUE — verificação do agente V4 Tendências (+fix)

- **Intake OK** (cron */30, fila ~550, matched ~240).
- **Worker ESTAVA QUEBRADO e foi CONSERTADO:** `ProxyError` ao falar com cafezinho.news — o `chaves.sh` do NYC exporta proxy iProyal global e `cafezinho.news` **não estava no NO_PROXY**. Fix: adicionado `cafezinho.news,www.cafezinho.news` ao `NO_PROXY`/`no_proxy` (backup `chaves.sh.bak_pre_noproxy_espelho_20260819`). Prova: rodada manual publicou **post 400129** (força da ONU, projéteis no sul do Líbano). O alerta `v4_production_stall_alert` (desde 17/08 04:58) era sintoma disso.

## §3. DESENHO — Agente único de Tendências ("Radar"), consultivo p/ todos os V4

**Princípio do Miguel:** NÃO criar um agente de tendências por V4 (cria repetição). **Um só agente**, independente, que os V4 **consultam**; se ele falhar, os V4 seguem normal (fail-soft). Ele sugere; o V4 confere "já publicou?" e enfileira.

**Arquitetura proposta (Radar de Tendências v1):**
1. **Radar (produtor único, cron 15/15min no Tencent):** consolida sinais — GA4 (o que está estourando agora no canônico), GSC queries emergentes (já existe `gsc_queries_novas` no radar v2 do Tencent), Google Trends BR/mundo (RSS público, gratuito), e a fila viva dos V4. Saída: `radar_tendencias.json` (tema, sinais, força 0-100, janela, fontes) — publicado num endpoint simples (`/v6/api/radar-tendencias`) e num arquivo JSON acessível.
2. **Consumo (consultivo) pelos V4:** cada intake V4 lê o radar (timeout curto; se falhar → segue sem bônus, nada muda). Candidata que casa com tema quente ganha **bônus de score** (não entra à força — preserva a curadoria da vertical).
3. **Confere "já publicou?" antes de sugerir:** o radar marca cada sugestão com checagem no WP (título/slug/entidades nas últimas 72h) + na fila atual — sugestão já coberta sai da lista (evita repetição na origem, elo com §4).
4. **Observabilidade:** toda sugestão aceita/rejeitada é logada (alimenta §5 autoaprendizado).

## §4. DESENHO — Anti-repetição de assunto (retomada do RAR de 18/08)

O desenho **RAR** (Registro Anti-Repetição, SQLite, cerco em 4 estágios coleta→intake→worker→Loop, janelas 3–7d por vertical, variedade de fontes/entidades) está pronto desde 18/08 e **aguarda aprovação**. Esta ordem nova o reforça e acrescenta:
- **Portão no motor publicador unificado:** além dos 4 estágios, uma verificação final no publicador (última linha de defesa) — similaridade de título + entidades (não só título exato/24h, que é o dedup atual e insuficiente: casos Vila Euclides 16×, pesquisa 47×44).
- **Radar × RAR casados:** o radar consulta o RAR antes de sugerir; o RAR registra cada publicação para o radar enxergar.

## §5. DESENHO — Autoaprendizado CONSERVADOR de estilo (PES)

Fontes já existentes: Baleia Azul (relatórios diários) + análise de 1.125 posts/3 semanas (15/08: título verbo+nome = 9× decolagem; sábado 06h-10h; editoria campeã...) + GA4 por post.

**Ciclo semanal conservador:**
1. LLM lê os dados da semana → propõe **no máximo 1–2 micro-ajustes** de diretriz (nunca reescrita ampla).
2. Proposta vai p/ aprovação (Miguel/Loop) — **nada auto-aplicado** nesta fase.
3. Aplicado → mede por 2 semanas → piorou, rollback automático da diretriz (guardamos antes/depois + métrica de cada mudança).
4. **Poucas regras imutáveis** (as constitucionais do §6); todo o resto é **revisável** — a arquitetura tem permissão explícita de rever as próprias regras, mas devagar.

## §6. DESENHO — Constituição de Estilo (Cafezinho Média Grupo + internacionais + Filhos da Impunidade)

**Separação blindada (ordem do Miguel):** as diretrizes de estilo NÃO se misturam com o canônico por enquanto — valem para **espelho Cafezinho + Filhos da Impunidade**. O canônico só entra depois de homologado.

**Constituição (curta, imutável — "10 mandamentos", minuta inicial p/ revisão do Miguel):**
1. Verdade factual antes de estilo.
2. Clareza acima de ornamento.
3. Português integral (até aspas — regra viva).
4. Ritmo variado (ver §6.1) — nunca monocórdio.
5. Título = uma ideia central, com verbo.
6. Voz ativa por padrão.
7. Respeito à linha editorial do veículo (diretriz viva, fora desta constituição).
8. Nenhuma regra de estilo é imutável — exceto estas 10.
9. Toda mudança de diretriz é registrada com antes/depois e motivo.
10. Em dúvida, conservar o que funciona (a mudança precisa ganhar da dúvida).

**§6.1 Os 8 ritmos (minuta):** R1 frase curta de impacto; R2 parágrafo médio argumentativo; R3 longo-descritivo com respiração; R4 pergunta→resposta; R5 dado-forte primeiro; R6 narrativo-cena; R7 contraste (duas ideias em tensão); R8 síntese-fecho. **Distribuição (ordem do Miguel):** o texto navega principalmente entre R1–R2; de vez em quando salta para um ritmo diferente (R3–R8) — a variação é a marca. Calibragem fina dos pesos fica para a sessão do Filhos da Impunidade (Miguel abre sessão própria).

## §7. Estado da missão

**Pronto:** box Top 10 no ar (espelho, cron horário), V4 Tendências destravado (proxy) e publicando, tudo com backups e no GitHub.
**Falta (decisões do Miguel):** (1) aprovar Radar v1 (§3) e RAR+portão (§4) p/ eu implementar; (2) revisar a minuta da Constituição (§6) — e a sessão do Filhos da Impunidade calibra os 8 ritmos; (3) PES (§5) entra depois de Radar+RAR.
**Preciso de você:** OK nos desenhos §3–§6 (ou ajustes) — depois disso eu implemento.

---

## ADENDO 19/08 ~11:45 BRT — BOX VIRA CARROSSEL (ordem Miguel ~11:20 — "com slide no celular")

**Ordem do Miguel (voz, transcrita):** o Top 10 Tendências vira CARROSSEL — 10 slides numerados Top 1..10 com foto, por ordem de mais visto; no celular desliza com o dedo (sem setas); desktop/iPad com setinhas dos 2 lados; loop infinito (do 10 volta ao 1); subtítulo no padrão dos outros blocos ("deslize para ver as 10 mais"); título menor que o da Coluna do Editor; **TRAVA DA MANCHETE: o post que está na manchete naquela hora sai do carrossel — e volta automaticamente quando deixar de ser manchete** ("a trava só vale para quem está na manchete naquela mesma hora").

**Implementado (espelho; backups `.bak_pre_carrossel_20260819` no mu-plugin e no front-page; php -l OK nos 2):**
1. **`cafezinho-top-tendencias.php` v2.0** — renderer reescrito como carrossel (scroll-snap horizontal + clone-loop infinito em JS; setas só ≥768px; título .95rem; badge "Top N" vermelho; foto `medium_large`, placeholder cinza se não houver). Dados INTACTOS: a pipeline da sessão anterior segue (NYC GA4 → REST → option `cafezinho_top10`, push horário :25).
2. **Trava da manchete FEITA DIREITO:** o front-page empurra o ID da manchete renderizada no `$excludes` antes de chamar o renderer — o hook virou `cafezinho_render_top_tendencias( $excludes )` e o renderer exclui `$excludes[0]` (cobre seleção manual, manchete-humana E fallback — diferente da v1, que lia só a tabela highlights). Fallback interno: lê a tabela highlights se o renderer for chamado sem $excludes.
3. **Bloco antigo REMOVIDO** (o "Top Tendências só-V4" com links Top 20/50/100 que eu tinha feito 19/08 10:30, depois de "Os 10 mais vistos") — a home ficou com UM único bloco de tendências (o carrossel, 1º após a manchete). O link `?top_tendencias=N` morreu junto (superseded pelo carrossel).

**Verificado no ar:** home renderiza 1 carrossel, 8 slides todos com foto, numeração Top 1..8, setas no DOM, manchete atual (266607 "Ex-comandante da FAB detalha o plano golpista...") fora do ranking → trava sem ação nesta hora (correto).

**Nota de dados:** o carrossel usa o ranking GA4 (mais vistos 24h do canônico) — o box da sessão das 10:55. A versão "só posts do V4" (meta zizi_job_id v4d_tendencias) foi desmontada com o bloco antigo; reativar = 1 linha de consulta (WP_Query meta_query) se o Miguel pedir.

---

## ADENDO 19/08 ~12:25 BRT — CARROSSEL NO CANÔNICO + ANTI-REPETIÇÃO + CAMPEÕES DO MÊS + BOTÃO MANCHETE (ordens Miguel ~12:00-12:20)

**Ordens do Miguel (após ver o carrossel no espelho):** (1) anti-repetição — os posts do Top Tendências desaparecem dos blocos abaixo; (2) V4 Tendências DESISTIDO como publicador ("agente silencioso" = radar segue); (3) "gostei muito — pode levar para o canônico"; (4) "bota também o botão manchete lá" (widget wp-admin no canônico); (5) manter o bloco antigo RENOMEADO: **"Os campeões do mês"** (10 mais acessados do mês; repetição lá não importa).

**Executado (backups em tudo):**
1. **Anti-repetição (espelho + canônico):** o renderer passou a receber `$excludes` POR REFERÊNCIA e joga os IDs do carrossel nele → os posts do Top Tendências somem de TODOS os blocos abaixo (Nacional/Geo/Cultura/Tec/Recentes/Linha do Tempo). Prova: 0 repetições nas 2 homes. O bloco Campeões do mês NÃO usa $excludes (lê o JSON 30d) → repetição lá permitida, como ordenado.
2. **Kill switch V4 Tendências:** `enabled=false` na diretriz viva (backup `.bak_pre_killswitch_20260819_1210`) — intake e worker param nas próximas rodadas; o radar (30/30min) SEGUE coletando (papel de "agente silencioso" consultivo). Posts já publicados ficam.
3. **CARROSSEL NO CANÔNICO (www.ocafezinho.com):** mu-plugin `cafezinho-top-tendencias.php` copiado + hook no front-page (1º bloco após a manchete, com `$excludes`) + **push duplo no NYC** (`top_tendencias_push.py` agora POSTa espelho E canônico, backup `.bak_pre_push_canonico_20260819`; push manual: espelho count=9 — filtra os ainda-não-espelhados — canônico count=10). **Trava da manchete PROVADA no canônico:** manchete = "Lula e Putin..." (está no ranking) e NÃO aparece nos slides. Cache: home canônico atualizada e verificada fresca.
4. **"Os campeões do mês":** bloco renomeado nos 2 sites (era "Os 10 mais vistos"; rodapé "Os 10 posts mais acessados do mês."). Dados 30 dias inalterados.
5. **Botão manchete no canônico:** widget `cafezinho-manchete-humana.php` copiado do espelho (📌 É MANCHETE + barrinha 2-24h + ❌ + 🔁 Rodar + auto-trava da coluna Destacar) — **sem o registro REST** (o canônico já tem `cafezinho-manchete-humana-api.php` servindo os agentes; evitei rota duplicada). php -l OK.
6. Nota: ssh Dell→droplet caiu no meio (rota local; o site nunca caiu — prova via NYC/fetcher externo); contornei com `ssh -J nyc`.ssh -J nyc`.

**Pendente do Miguel:** nada operacional. (Desenhos §3-§6 — Radar único, RAR+portão, PES, Constituição — seguem aguardando aprovação dele.)

### ADENDO 19/08 ~13:10 BRT — CARROSSEL TAMBÉM NO SINGLE (ordem Miguel ~12:55)

**Ordem:** no single post, o bloco "Próxima matéria" SAI e no lugar entra o carrossel Top 10 Tendências ("em vez de próxima matéria bota o carrossel").

**Implementado (canônico + espelho; backups `.bak_pre_carrossel_single_20260819`; php -l OK):**
- `single.php`: bloco "Próxima matéria" removido; no lugar, chamada `cafezinho_render_top_tendencias( $ttc_single_excl )` com `$ttc_single_excl = array( get_the_ID() )`.
- **Renderer v2.1** (mu-plugin, 2 sites): a exclusão virou CONJUNTO — tudo que vier no `$excludes` sai dos slides (home = a manchete renderizada; single = o post sendo lido). Fallback da trava da manchete pela tabela highlights quando chamado sem excludes.
- **Prova ao vivo (canônico):** single do post Top 1 (Ciro/Mossad) mostra 9 slides e o próprio post NÃO aparece; "Próxima matéria" sumiu; home segue com trava da manchete (Lula×Putin fora dos slides da home).

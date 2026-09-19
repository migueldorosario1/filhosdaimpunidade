# 📅 CEREBRO_NODE — Agenda de Lembretes Operacionais

> Lembretes datados que qualquer agente deve checar AO ACORDAR no workspace.
> Criado **2026-06-29 22:50 BRT** por Claude Code.

---

## 🔔 Protocolo

**Toda sessão que acorda, ANTES de fazer qualquer outra coisa, deve:**

1. Rodar `date '+%Y-%m-%d'` pra saber o dia atual
2. Ler este arquivo
3. Para cada lembrete cuja data `Dispara em` é ≤ hoje, AGIR ou informar o Miguel
4. Após executar, mover o lembrete pra § Histórico no final

---

## ⏰ Lembretes ATIVOS (ordenados por data)

### `2026-09-01 (contínuo)` — 🧠 DSM Memória: artigos do Miguel + prompts a colar + decisões pendentes

- **Criado:** 2026-09-01 ~03:00 BRT por DSM (DS Dell), a pedido do Miguel ("você tem que ser minha memória… não pode deixar esquecer").
- **Casa canônica:** `CEREBRO_NODE_DSM_MEMORIA.md` (protocolo + registro + agenda do DSM). Compêndio da noite: `Foruns/sessoes_dsc/COMPENDIO_NOTURNO_20260831_20260901.md`.
- **Lembrar o Miguel até concluir (todas as sessões, 3 linhas máx):**
  1. **Enxugar os 2 artigos autorais** (Ceará + EUA, v1s em `Insumos/artigos/`) e escolher veículo (Cafezinho · Ceará Digital · GSN inglês).
  2. **Colar no ZCode:** prompt Marketing · vagas Coordenador/Segurança/Métricas/Memória/Editor Baleia Azul/DS-N Redes.
  3. **Decisões:** 4 pontos da arquitetura CL-041 §13 · copy do fix do lock da AGY · ✓ no `PROMPT_NOVA_CONVERSA_DSC.md` · nome da editora própria.
- **Mapa completo (01/09 ~13:45, ZCode/GLM-5.3):** TODAS as pendências da noite 31/08→01/09 viraram tarefas numeradas nas sessões Z0–Z7 — mestre em `Foruns/sessoes_zcode/TAREFAS_MESTRE.md` (seção 🔒 "PENDÊNCIAS QUE DEPENDEM DO MIGUEL" = fonte única) + índice `Foruns/sessoes_zcode/INDEX_SESSOES_ZCODE.md` (prompt de abertura de cada sessão Z).
- **Concluir:** remover daqui e registrar no §3 do node do DSM.

### `quando a Etapa 1 social for ao ar` — 🔗 Colocar `ocafezinho.com/top10` na BIO das redes (ordem Miguel 19/08/2026 ~17:50)

- **O quê:** ao ligar a automação social (Etapa 1 — Top 1 diário), colocar o link `https://www.ocafezinho.com/top10` na bio do Instagram (@ocafezinhooficial) e na bio do X (@ocafezinho) — Miguel pediu "me lembra de colocar esse link na bio".
- **Como:** bio do IG não tem API pública — fazer manualmente no app (Miguel) ou guiar ele na hora; bio do X via app também. O cards já divulgam `ocafezinho.com/top10` na imagem (card 1 e card 2).
- **Depende de:** a página/categoria `top-10` existir no canônico (agente sincronizador — ver fórum `forum_plano_social_top1_conselheiro_audiencia_20260819.md`, adendo 8).
- **Quem registrou:** ZCode/DeepSeek.

### `2026-08-11` (depois das 22h00 BRT) — 🌙 EXECUTAR PORT NOTURNO: espelho → canônico (TODAS as mudanças da reforma visual)

- **Criado:** 2026-08-11 ~14:30 BRT por ZCode (GLM-5.2 Z.ai), a pedido do Miguel: "Guarda no cérebro, né? Pra gente não perder. Se por acaso fechar o computador, a gente pode reiniciar. Deixa guardadinho no cérebro como pendência pra hoje à noite. Depois das 22 horas."
- **Estado:** 🟢 **TUDO PRONTO NO SERVIDOR** — só executar. Site canônico está 100% estável (rollback completo da Fase 1 da tarde aplicado às 12:50, header.php com SHA `0aba7d76...` = original).
- **Como executar (1 comando):**
  ```
  ssh cafezinho-wp 'bash /tmp/port_canonico_noturno_scripts/ORQUESTRADOR.sh'
  ```
- **O que o ORQUESTRADOR faz (5 fases, ~5 min):**
  1. Snapshot pré-aplicação (rollback fácil)
  2. **Fase A:** Subir logo v6 + foto editor v2 (estáticos)
  3. **Fase B:** Header rewrite (logo esquerda + hamburger direita) + footer offcanvas expandido (Buscar + Apoie + menu com submenus + gtranslate) + CSS header-bar-minimal
  4. **Fase C:** Manchete vertical (título + imagem 100% + caption + balão 🔥)
  5. **Fase D:** Coluna Editor (8 posts + iPad swipe + cabeçalho avatar>titulo>nome maiúsculas)
  6. **Fase E:** Botão Apoie pill no footer
  7. Purgar cache WP Rocket + HTTP check final
- **Rollback total (emergência):** `bash /root/port_canonico_noturno_<TS>/rollback_TOTAL.sh` (gerado automaticamente na execução)
- **Artefatos preservados (NÃO se perdem mesmo se reiniciar):**
  - 10 scripts em `/tmp/port_canonico_noturno_scripts/` no servidor `cafezinho-wp`
  - Logo v6 + foto editor v2 em `/tmp/` do servidor
  - Plano completo: `Cerebro/Foruns/forum_plano_execucao_noturna_port_canonico_20260811.md`
  - Memória técnica: `Cerebro/Memorias/memoria_port_canonico_fase1_20260811.md`
  - Backup tema original: `/root/port_canonico_backup_20260811_111704/` (tar.gz 1.7MB)
  - 13 snapshots intermediários em `/root/port_canonico_fase1_*/`
- **Lições aplicadas (NÃO repetir erros da tarde):**
  1. 1 script consolidado por fase (não 15 iterações sobrepostas)
  2. Hamburger sempre visível: SEM `d-md-none` no `<a>` E SEM `d-lg-none` no `<img>` interno
  3. Logo `position: static` (era absolute, sobrepunha single post)
  4. `flex-wrap: nowrap !important` (hamburger nunca quebra linha)
  5. `align-items: center` (baseline não funciona com alturas diferentes)
  6. `justify-content: space-between` (mais robusto que order CSS)
  7. `wp_nav_menu` offcanvas: `depth=2` + walker Bootstrap (submenus abrem)
  8. `object-fit: contain` na foto da capa (não corta)
  9. SEM margin-right no `<img>` dentro de flex btn (gap cuida do spacing)
  10. `border-bottom: 1px solid #dee2e6` no header (linha cinza restaurada)
- **Pendência aberta:** investigar bug dos anúncios "colados na esquerda" reportado pelo Miguel na tarde — pode ser pré-existente, cache CDN, ou efeito colateral não-identificado. Tirar screenshot antes/depois do port noturno pra comparar.
- **Status:** ⏸️ AGUARDANDO 22h BRT. Quando Miguel disser "vamo pro port noturno", executar.

---

### `2026-08-05` (tarde) — Portar selo "Cafezinho Media Group" ao rodapé do ocafezinho.com CANÔNICO

- **Criado:** 2026-08-05 ~11:15 BRT por Kimi K3 (ZCode), a pedido do Miguel: "o cafezinho é um pouquinho mais complicado, só deixa o plano pronto e me lembra pra gente botar depois".
- **Estado:** homologado no espelho cafezinho.news (mu-plugin `cafezinho-media-group-selo.php`, no ar desde ~11:00). Acesso canônico CONFIRMADO (SSH `cafezinho-wp` = us65.serverdo.in).
- **Plano (100% aditivo, padrão espelho→canônico):**
  1. Copiar o MESMO mu-plugin do espelho: `scp root@159.65.177.60:/var/www/cafezinho-news/wp-content/mu-plugins/cafezinho-media-group-selo.php` → `/var/www/ocafezinho/wp-content/mu-plugins/` (ou recriar do fórum `Foruns/forum_selo_cafezinho_media_group_20260805.md`).
  2. Purge do WP Super Cache (ATIVO no canônico — `advanced-cache.php` presente): `wp super-cache flush --path=/var/www/ocafezinho --allow-root`.
  3. Verificar: `curl -s https://www.ocafezinho.com/ | grep cmg-selo`.
  4. Rollback = apagar o arquivo + flush novamente.
- **NÃO executar sem o "vai" do Miguel.**

### `2026-07-24` — Upgrade Ubuntu 20.04 → 22.04 (noite, pós-live ~22h) + swap 16GB

- **Criado:** 2026-07-22 22:30 BRT
- **Por:** Miguel + Kimi k3 (decisão Trindade: Kimi, Codex e Claude Code endossaram; parecer do Claude em `Dados_Frios/Infraestrutura Ubuntu/parecer-atualizacao-ubuntu.md`)
- **Contexto:** Máquina local em Ubuntu 20.04.6 LTS (focal), fora do suporte padrão (já depende de ESM). Swap saturado (75-82%) causando crashes do Antigravity. Plano completo: swap 16GB + swappiness 10 (decisão Trindade 22/07) como Fase 0, depois `do-release-upgrade` para 22.04 (NÃO pular direto pro 24.04 — dois pulos é risco à noite). Plano detalhado com mapeamento e recuperação via celular/iPad foi entregue na sessão ZCode de 22/07 à noite.
- **Pré-requisitos ANTES de começar (checklist da sessão):**
  1. Backup completo (docs, scripts, `~/.ssh`, `~/.config`) — INEGOCIÁVEL
  2. `sudo apt install openssh-server` + testar SSH do celular/iPad (Termius) — é o plano de recuperação remota
  3. Inventário: `ls /etc/apt/sources.list.d/ > repos.txt` + `dpkg --get-selections > pacotes.txt`
  4. `sudo apt update && sudo apt upgrade -y` + reboot limpo
  5. Na tomada, celular carregado, pendrive live USB Ubuntu por perto (se houver)
- **Ação (ordem):** Fase 0 swap 16GB → Fase 1 backup → Fase 2 prep → Fase 3 `sudo do-release-upgrade` → Fase 4 validação mínima (rede, Chrome, SSH) → dormir. PPAs desativados NÃO reativar à noite — só sábado de manhã.
- **Condição de cancelamento:** se live atrasar além das 23h ou Miguel estiver cansado → fazer SÓ o backup e adiar upgrade pro sábado 25/07.
- **Pós:** reativar PPAs sábado de manhã; registrar Fórum + Memória no Cérebro (Tema Duplo), catalogar no `CEREBRO_NODE_HARDWARE_MIGUEL.md`.
- **Se Miguel quiser adiar:** basta dizer "adia o upgrade" — atualizar a data acima
- **Referências:**
  - `Dados_Frios/Infraestrutura Ubuntu/parecer-atualizacao-ubuntu.md` (parecer Claude)
  - `Cerebro/Foruns/inbox_trindade/agy.md` (parecer Claude Code sobre swap)
  - `CEREBRO_NODE_HARDWARE_MIGUEL.md` (incidente swap 2026-05-27)

---

### `2027-07-14` — Reavaliar migração canonical www.ocafezinho.com → ocafezinho.com (sem www)

- **Criado:** 2026-07-14 ~17:30 BRT
- **Por:** Miguel (preferência estética por sem-www; adiou por 12 meses porque timing atual de recovery pós-punição desaconselha mudanças estruturais)
- **Contexto atual (14/jul/2026):** site atual é `www.ocafezinho.com` (canonical em HTML aponta pra www, 93.621 URLs indexadas em www, todos backlinks em www). Versão sem www responde HTTP 200 mas tem canonical apontando pra www — Google já sabe qual preferir. Property GSC `sc-domain:ocafezinho.com` cobre ambas.
- **Motivo do adiamento (12 meses):** Cafezinho em fase de recovery de punição algorítmica (Discover -98% em maio/junho, ainda instável). Adicionar mudança de canonical em cima de: publicação humana + reforma agentes + pruning + separação SAs = amplifica confusão algorítmica. Aguardar métricas se estabilizarem (Discover ≥300 clicks/dia consistente, posição média ≤4, GA4 organic ≥2500/dia).
- **Ação em 2027-07-14:**
  1. Rodar análise SEO — verificar se métricas estão saudáveis (não em queda)
  2. Se sim, executar migração:
     - `wp option update siteurl "https://ocafezinho.com"`
     - `wp option update home "https://ocafezinho.com"`
     - `wp search-replace "https://www.ocafezinho.com" "https://ocafezinho.com" --skip-columns=guid`
     - Nginx: adicionar `server { server_name www.ocafezinho.com; return 301 https://ocafezinho.com$request_uri; }`
     - Yoast SEO: regenerar sitemap com nova URL canônica
     - GSC: adicionar propriedade nova `https://ocafezinho.com/` como preferida (`sc-domain:` já cobre)
  3. Se métricas ainda instáveis, adiar +6 meses
- **Se Miguel mudar de ideia antes:** basta dizer "cancela migração www" (fica em www permanente) ou "antecipa migração www" (avaliar riscos no momento)
- **Referências:**
  - Conversa 14/jul/2026 (esta sessão)
  - `Cerebro/Foruns/forum_analise_gsc_completa_20260714.md`

---

## 📜 Histórico (lembretes concluídos)

### `2026-07-25` — Reverter threshold SEO pruning 40% → 60% ⏹ SUPERADO / ARQUIVADO 2026-08-04 22:26 BRT

- **Criado:** 2026-07-07 14:00 BRT | **Arquivado:** 2026-08-04 22:26 BRT (Miguel: "esse SEO pruning já passou, remove")
- **Contexto original:** threshold do kill-switch GA4 rebaixado 0.6→0.4 em 07/07 no NYC (`/root/seo_pruning/seo_progressive_noindex.py` L292) por queda-em-V atribuída à Copa. Backup `.bak_pre_copa_20260707`.
- **Status:** lembrete não executado dentro da janela; contexto operacional mudou. Se o script `seo_progressive_noindex.py` ainda está no ar em NYC e o Miguel quiser retomar threshold=0.6, ação continua sendo `sed` de uma linha (comando abaixo) — mas fora da agenda ativa. Backup `.bak_pre_copa_20260707` pode estar velho; validar antes de deletar.
- **Comando se um dia quiser reverter:** `ssh root@198.199.121.136 "sed -i 's|if ratio < 0.4:.*|if ratio < 0.6:|' /root/seo_pruning/seo_progressive_noindex.py && python3 -m py_compile /root/seo_pruning/seo_progressive_noindex.py"`
- **Referências:** `memory/project_seo_pruning_automatizado_20260701.md`

### `2026-07-19` — Finalizar separação service accounts sites temáticos ✅ CONCLUÍDO 2026-07-16 01:15 BRT (3 dias antes)

- **Criado:** 2026-07-14 ~17:45 BRT | **Concluído:** 2026-07-16 01:15 BRT
- **Por:** Miguel (retomou trabalho na sessão de 15/07 noite; adiantou o cronograma)
- **Executado por:** Miguel (parte manual GSC + DNS) + Claude Code `claude-opus-4-7` (smoke tests + registro)
- **Resultado:**
  - 7 sites temáticos (GSN, Rio Carta, Mundo Trilhos, Discover, Mapa Rio, AIatolah, ceara.digital) com Owner GSC = SA correspondente `indexer@indexing-<site>.iam.gserviceaccount.com`.
  - Rio Carta, Mundo Trilhos, Discover, Cafezinho: properties já estavam verificadas (não precisou re-verificar — dropdown do GSC era campo de busca, não lista completa).
  - GSN, Mapa Rio, AIatolah, ceara.digital: re-verificação via DNS TXT (GoDaddy pra 3, Vercel pro Mapa Rio).
  - Smoke test por site: 7/7 `✅ Google Indexing Notificado com Sucesso` — keyfile correta resolvida por domínio.
  - SA velha `indexing-cafezinho@` limpa dos GSCs de Rio Carta e GSN (Miguel já tinha feito antes).
  - **Cafezinho canônico agora com quota 200/dia + reputação Google 100% exclusivas no projeto `gen-lang-client-0200069757`.**
- **Pendências opcionais deixadas em aberto:**
  - Deletar projeto `open-claw-gsn` (esqueleto obsoleto)
  - Deletar 3 projetos `ZOMBIE - Cafezinho*` (libera quota, reversível 30d)
  - Ambos: Miguel não priorizou. Se quiser fazer, é 5min via `gcloud projects delete`.
- **Referências:**
  - Memória perene: `memory/project_separacao_sas_indexing_concluida_20260716.md`
  - Fórum: `Cerebro/Foruns/forum_separacao_service_accounts_indexing_20260714.md` (log entry 2026-07-16 01:15 BRT)
  - Fórum sprint: `Cerebro/Foruns/forum_sprint_sites_tematicos_completo_20260714.md` (Bloco A fechado)
  - CEREBRO_NODE_ATUALIZACOES: entrada 2026-07-16 01:15 BRT

### `2026-07-10` — Rotacionar Access Key Prometheus Alibaba ✅ CONCLUÍDO 2026-07-10 ~11:25 BRT

- **Criado:** 2026-07-08 11:15 BRT | **Concluído:** 2026-07-10 ~11:25 BRT (na data-alvo)
- **Por:** Claude Code (autoresponsável — recomendação de segurança)
- **Executado por:** Claude Code (`claude-opus-4-7`) + Miguel (console Alibaba)
- **Contexto:** AK antigo `LTAI...dQ3U` foi colado no chat em 08/07 pra desatolar smoke da migração Prometheus. Ficou registrado no histórico do assistant + `.env` chmod 600 dos 3 servers. Rotação preventiva 48h depois.
- **Resultado:**
  - Novo AK gerado no console (aba Credential do user `power-application-user`)
  - CSV do AK novo guardado localmente pelo Miguel em `Cerebro/alibaba/`
  - `.env` substituído nos 3 servers (backups `.bak_pre_rotacao_20260710_112001-044`)
  - Push validado 3/3: Cingapura 613 métricas | Alibaba Cérebro 482 | Rio Carta 523
  - PromQL smoke: `node_load1` retorna dado dos 3 servers via novo AK ✅
  - Correção descoberta: RAM user real é `power-application-user`, não `prometheus-agent` (snapshot 09/07 documentou nome errado — cérebro corrigido)
- **Pendente do Miguel:** Disable + Delete AK antigo `LTAI5tEfyuKZgc3dd2U7dQ3U` no console (RAM → Users → power-application-user → Credential → AccessKey → Actions Disable, depois Delete)
- **Referências:** `Cerebro/CEREBRO_NODE_OBSERVABILIDADE.md` §1.2 (canônico atualizado)

### `2026-07-06` — Purgar backup local Camada 3 do Cafezinho prod ✅ CONCLUÍDO 2026-07-07 09:12 BRT

- **Criado:** 2026-06-29 22:50 BRT | **Concluído:** 2026-07-07 09:12 BRT (1 dia após data-alvo — Miguel autorizou ao acordar 07/07)
- **Por:** Miguel ("podemos remover em alguns dias, mas deixa guardado na agenda, me lembra depois")
- **Executado por:** Claude Code (`claude-opus-4-7`)
- **Resultado:**
  - Verificação B2: 11.324 arquivos local ≡ 11.324 remoto ✅
  - SHA1 sample 3/3 matches ✅
  - `rm -rf /var/www/ocafezinho/backup_camada3_20260628_174001/` no `us65.serverdo.in`
  - Disco `/dev/vda2`: 152G → 147G (−5 GB liberados)
  - Smoke homepage HTTP 200 em 700ms
- **Referências:** ver `Cerebro/CEREBRO_NODE_BACKUPS_BACKBLAZE.md` § `camada3_20260628/` (bloco "Purga backup local executada")

---

## 🛠️ Como adicionar um lembrete

```markdown
### `YYYY-MM-DD` — Título curto

- **Criado:** YYYY-MM-DD HH:MM BRT
- **Por:** quem pediu + citação curta
- **Contexto:** 1-2 parágrafos
- **Ação:**
  1. passo 1
  2. passo 2
- **Referências:**
  - arquivo X
```

Inserir em ordem cronológica na seção § Lembretes ATIVOS.

# Memória — Plano de Enxutice NYC + Espelho/Failover Tencent + Telemetria no Baleia Azul

> Autor: ZCode/Qwen 3.8 · 2026-08-07 ~12:30 BRT
> Origem: ordens por voz do Miguel (07/08 ~11:40): "plano de trabalho para deixar esses sites leves… agente automático para levar para o Backblaze e deixar só os arquivos funcionais… eventualmente Cloudflare… manter bem enxuto o servidor de Nova York… fim de semana: plano para resolver o espelho Tencent (failover completo — temáticos + cafezinho canônico)… no Baleia Azul: percentual de enchimento dos discos comparado com a semana anterior + informações dos temáticos… e uma revisão dos temáticos (o que está quebrado, quais foram autorizados)".
> Par de decisões: `Foruns/forum_plano_enxutice_nyc_espelho_tencent_20260807.md`
> Regras mãe: §115 (retenção universal — nada cresce sem teto) + política "não jogar nada fora" (Miguel 07/08: tudo é arquivado antes; restauração sempre possível).

## 1. Diagnóstico do disco NYC (medido 07/08 ~12:00 UTC)

**`/dev/vda1`: 48G total · 38G usados · 11G livres · 79%**

Anatomia real (du):

| Onde | Peso | O que é |
|---|---|---|
| `/root` | 26G | venv 7,7G (torch 1,8G + **nvidia CUDA 4,3G sem GPU no servidor**); agent_data 2,8G (banco_midia 1,4G); gsn_remote 1,9G (dump); cicero_remote 1,8G (dump 22/07); backups 1,6G; cafezinho 581M; V3 514M; legacy 450M; agente_estatistico 370M; CEREBRO_CANONICO_20260610 156M (cópia velha do cérebro) |
| `/tmp` | **7,4G** | 3 exports esquecidos do banco_midia (~5,6G: `banco_midia_export_kr6otu72` 1,9G + `.tar.gz` 1,9G + `_f4q7fqt9` 1,8G + `_cw9riu1r`) + cache pip (vários corpos >200MB = downloads dos wheels nvidia) + puppeteer chrome |
| `/usr` | 2,9G | sistema |
| `/var` | 821M | log 193M + mysql 136M |
| `/agentes_tematicos` | 369M | código dos temáticos |

Fatos: **sem GPU** (`/dev/nvidia*` inexistente) → CUDA wheels são peso morto. `/var/www` só 83M → as imagens pesadas NÃO moram no NYC como arquivos (os bancos guardam metadados/URLs). Espaço "de imagem" no sentido do Miguel = os bancos/exports/dumps acima.

## 2. PLANO — Fases

### Fase A — ganho imediato (~14G) — baixo risco, rito de arquivo primeiro
**Correções do dry-run (07/08 12:30 UTC) — a lista exata revelou nuances:**
1. **Cache pip** (**4,2G reais** — mais que o estimado): `pip cache purge` — cache regenerável, não é dado. Seguro.
2. **Exports do /tmp** (~5,6G: tar.gz 2G de 05/08 19:45 com `./img/acervo_*.jpg` + 3 dirs estilo mkdtemp): ⚠️ **são recentes (05/08)** e NENHUM script/cron os cria → foram gerados por uma sessão pontual. Provável cópia redundante das imagens do próprio banco. Rito: confirmar redundância (amostra de hashes vs banco) → B2 → remover. **Se o Miguel souber pra que era esse export de 05/08, falar antes.**
3. **gsn_remote** (1,9G): pipeline GSN **DESLIGADO desde 23/07** (crontab: "DESLIGADO_20260723_ZCODE… site real = globalsouth-v4") → B2 + manifest → remover. **cicero_remote: VIVO** — crons ativas (`cicero` 10:00 e `ceara-digital` 09:15 diárias)! NÃO tocar no geral; apenas `cicero_remote/root/` (226M, bak de 22/07) é candidato.
4. **backups/ + legacy/ + CEREBRO_CANONICO_20260610** (~2,2G): confirmar espelho existente no B2 → remover local só após verificação.
5. **puppeteer cache** (627M): regenera sozinho no próximo uso (1ª rodada fica lenta) — candidato opcional.
→ Resultado esperado: 79% → ~48–50%. **Cada item: dry-run → lista exata → "pode aplicar" do Miguel → executa.**

### Fase B — dieta do venv (~6G) — precisa cuidado
1. Confirmar quem importa torch (provável: embeddings do estatal_news — `embeddings_repetidor` 319 linhas; talvez qualidade_redacao).
2. Se for CPU-only: trocar wheel torch → torch-CPU (elimina nvidia/* 4,3G e partes do torch) em venv novo, testar scripts, swap atômico com venv velho preservado até prova.
→ −6G adicionais. Só com aprovação.

### Fase C — agente automático de enxutice (Backblaze) — permanente
1. Novo agente `storage_janitor.py` (mesmo rito do arquivador V4): diário, varre padrões (exports >1d, dumps remotos, .bak_*, logs fora do §115, arquivos-frios) → **envia p/ B2 com manifest sha256 → verifica remoto (list+head+hash) → só então remove local → recibo no ledger**. Dry-run por padrão; `--execute` exige `--authorization-ref`; lock próprio; nunca mata processos.
2. Credenciais B2: já existem (espelho do Cérebro) — caminho no Cofre de Chaves; nunca copiar valores.
3. Cloudflare (R2/Images) fica como opção futura para SERVIR mídia; para arquivamento, B2 primeiro (já temos conta e espelhos).

### Fase D — Baleia Azul (seções novas)
1. Coletor novo `coletor_disco_tematicos.py` (local, roda antes do envio 08:00/18:00): `ssh nyc df` + top-dirs + `ssh tencent df` + tamanho/contagem dos 3 bancos temáticos + última corrida do cron de autolimpeza → grava snapshot JSON diário (guarda 8 semanas) → seção "💾 Discos (esta semana vs semana passada)" + "🗞️ Temáticos" (só algumas linhas — estão no início, mas "pra gente nunca esquecer").
2. Integração no emissor `enviar_baleia_azul_v2.sh`: **assento editor da Baleia = ZCode/Kimi K3** (desde 07/08 10:05, nodo BALEIA_AZUL) — esta sessão entrega o coletor + contrato de dados; a inclusão no corpo é feita pelo assento editor (respeito ao §112 — não pisar em arquivo de outra sessão). Aviso via canal + nodo.
3. ⚠️ Bug ativo no caminho: edição de hoje **não chegou no e-mail** (BUGS_ATIVOS, 11:00 BRT) — precedência do assento editor.

### Fase E — Espelho/Failover Tencent (fim de semana 08–09/08)
1. Hoje o Tencent já é espelho PARCIAL (evidência: `banco_midia_ouro_v3.db` idêntico nos dois 07/08 13:47 UTC; `agent_data` presente). Falta mapear: o que sincroniza, como (qual cron/rsync), e o que falta (v4_verticals? scripts? crons?).
2. Alvo: espelho completo do pipeline — **bancos** (v4 8 + banco_midia + ouro), **código** (scripts + crontabs em modo frio/desligado), **runbook de failover** (o que ligar no Tencent se NYC cair: crons, chaves, DNS?, WP?) + **ensaio** (drill) documentado.
3. Entregável do fim de semana: agente de espelho diário + checklist de failover + 1 ensaio parcial.

## 3. Revisão dos temáticos (pedido do Miguel — 07/08 ~12:15)

Saúde dos 8 domínios (curl/dig, 12:10 UTC):

| Domínio | Estado |
|---|---|
| discoverbrazil.com | ✅ 200 |
| mapario.com.br | ✅ 200 |
| aiatolah.com | ✅ 200 **mas conteúdo parado há 17 dias** (publicador — assento Vigília/Kimi K3 investigando, carta Claude 10:10) |
| globalsouth.news | ✅ 200 (Vercel, via redirect) |
| railpost.news | ✅ 200 (Vercel, via redirect) — timeout intermitente relatado pela Vigília |
| **ceara.com.br** | 🔴 **SEM DNS** (não resolve; nem www) |
| **mundotrilhos.com.br** | 🔴 **SEM DNS** |
| **riocarta.com.br** | 🔴 **SEM DNS** (o código riocarta é a referência correta de template — domínio nunca apontado?) |

Outros achados da revisão:
- Bug template hero Astro atinge ceara/discoverbrazil/globalsouth/mundotrilhos (riocarta = referência correta) — assento Vigília/Kimi K3 no caso (sessão 10:20 BRT).
- Pipelines temáticos (ciencia_tecnologia_ia, geopolitica, nacional) rodam cron 30min no NYC; bancos serão limpos pela 1ª corrida do cron de autolimpeza (08/08 04:35 BRT).
- **"Quais foram autorizados"**: não há lista formal de autorização de domínios/sites no Cérebro localizada nesta revisão — os 5 sites Astro + railpost + mapario aparecem como "7 portais" na Central de Temáticos do V6 (22/07). Pendência registrada: levantar lista formal junto ao Miguel (quais domínios são para manter vivos e apontar DNS).

## 4. Estado e próximos passos
- Plano escrito e registrado (Tema Duplo). Nenhuma ação destrutiva executada nesta fase.
- Próximo: Fase A dry-run (lista exata de arquivos) → Miguel "pode aplicar" → executa.
- Baleia: coletor implementado nesta sessão (novo arquivo, sem conflito) + handoff ao editor.
- Fim de semana: Fase E.

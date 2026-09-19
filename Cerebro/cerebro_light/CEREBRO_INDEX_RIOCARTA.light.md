# CEREBRO_INDEX_RIOCARTA — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_INDEX_RIOCARTA.md` (74KB) — 75 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# Cerebro: Indice Mestre - Rio Carta

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


Este é o índice principal do ecossistema autônomo e de hospedagem do portal **Rio Carta**, isolado de qualquer outro projeto do workspace.

## 0. Ficha viva obrigatória — arquitetura real do Rio Carta

Esta seção deve ser lida antes de qualquer diagnóstico, deploy, ajuste de acesso ou criação de agente do Rio Carta. Ela duplica de propósito as informações críticas para evitar confusão com WordPress, Ghost, Cafezinho ou GSN.

### Estado auditado em 2026-05-22 23:50 BRT — resposta ao bloqueio DeepSeek

**Conclusão canônica:** o Rio Carta operacional vive no **Droplet DigitalOcean `159.89.185.209` (`agente-clone-01`)**. Esse IP **não é legado**. O legado confundido no canal era o NYC antigo `159.89.237.100` e/ou o WordPress legado `174.138.36.31`.

Validação read-only Codex em 2026-05-22 23:50 BRT:

- `root@159.89.185.209` respondeu via SSH com host `agente-clone-01`;
- `riocarta_admin.service` ativo há 3 dias, executando `/root/riocarta_admin.py`;
- crontab root contém linhas reais de coleta, publicação remota e indexação Google;
- clone Astro remoto existe em `/root/riocarta_remote/rio_carta/`;
- chave Git dedicada existe no Droplet como `/root/.ssh/id_ed25519_riocarta_github` (não copiar conteúdo);
- site público continua GitHub -> Vercel.

**O que NÃO é o Rio Carta vivo hoje:**

- Tencent/Cingapura `43.156.151.165`: tem arquivos antigos `agente_riocarta.py` e `robo_coleta_riocarta.py`, mas o crontab root auditado em 2026-05-22 não possui linhas Rio Carta. Tratar como legado/sombra até prova em contrário.
- Tencent/Beijing `82.156.167.218`: auditoria read-only em 2026-05-22 não encontrou crontab nem arquivos Rio Carta relevantes. É executor do GSN/Prometheus, não Rio Carta.
- Alibaba/Beijing `39.106.184.215`: Cérebro/Kimi/observabilidade, não publicador Rio Carta.
- WordPress Rio Carta `174.138.36.31`: legado. Não usar `/wp-admin`/REST WP como caminho editorial vivo.

### Crontab vivo do Rio Carta no Droplet

Servidor: `root@159.89.185.209`.

Linhas ativas auditadas:

```cron
0,30 0-2,9-23 * * * RIOCARTA_PYTHON=/usr/bin/python3 /root/riocarta_cron_rotativo.sh >> /root/logs/riocarta_cron_window.log 2>&1 # RIOCARTA_COLETA_ROTATIVA_30MIN_DIA_CODEX_20260515
0 3-8 * * * RIOCARTA_PYTHON=/usr/bin/python3 /root/riocarta_cron_rotativo.sh >> /root/logs/riocarta_cron_window.log 2>&1 # RIOCARTA_COLETA_ROTATIVA_1H_MADRUGADA_CODEX_20260515
23 * * * * cd /root && RIOCARTA_BATCH_SIZE=3 RIOCARTA_MAX_BATCH_SIZE=3 RIOCARTA_MAX_AUDIT_ATTEMPTS=6 /usr/bin/flock -n /tmp/riocarta_remote_publish.lock /root/riocarta_remote_publish.sh >> /root/logs/riocarta_remote_publish_cron.log 2>&1 # RIOCARTA_PUBLICADOR_REMOTO_CODEX_20260515
30 * * * * /usr/bin/python3 /root/riocarta_remote/root/riocarta_indexador_google.py >> /root/logs/riocarta_indexador_cron.log 2>&1 # RIOCARTA_INDEXADOR_GOOGLE_API
```

**Interpretação:**

- coleta roda a cada 30 minutos no período diurno definido e a cada 1 hora na madrugada;
- publicação remota roda uma vez por hora no minuto `23`, com lote máximo 3;
- indexador Google roda uma vez por hora no minuto `30`;
- alterações de ritmo devem mexer **somente nessas linhas**, com backup antes e rollback literal.

### Como auditar antes de mexer

```bash

---

## ⏩ 70 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_INDEX_RIOCARTA.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

## [2026-05-15 23:05 BRT] Codex - Confirmador de fonte corrigido + autocura versionada

O bug `riocarta_confirm_published.py` cego para fonte foi fechado. A regex estava correta; o problema era caminho: no Droplet, `/root/riocarta_remote/root` é symlink para `/root`, então `Path(__file__).resolve()` fazia o script procurar o blog em `/rio_carta/...`. O confirmador agora resolve o clone por `RIOCARTA_ASTRO_DIR`, depois pelo `cwd`, depois por `/root/riocarta_remote/rio_carta`.

Validação remota:
- `python3 -m py_compile /root/riocarta_confirm_published.py /root/riocarta_autocura_licoes.py` OK.
- `cd /root/riocarta_remote/rio_carta && python3 /root/riocarta_confirm_published.py smoke-202605160123-programacao-cultura-mistura-literatura-e-gastronomia-nesse-sabado-16-em-rio-das-ostras.md` retorn

> *(... 1303 chars omitidos — ler original)*

---

## [2026-05-16 13:51 BRT] Página teste do novo header

Sprint visual isolada para validar novo header com seis macroeditorias visíveis: Geral, Política, Lazer, Segurança, Economia e Serviços.

- Link público: https://www.riocarta.com/teste-header-novo/
- Fórum: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_pagina_teste_header_20260516.md`
- Commit: `5e048ea Add isolated Rio Carta header test page`
- Arquivos tocados no Astro:
  - `src/components/HeaderTesteMacro.astro`
  - `src/pages/teste-header-novo.astro`
- Validação: build local OK (`3543` páginas) e URL pública HTTP 200.

Observação de segurança: não alterou o header real de produção, home, posts, publicadores, coletores, crons, `.py` ou filtros reais de macro-categoria. Rollback: `git revert 5e048ea && git push origin main`.

---

# Atualização 2026-05-16 16:33 BRT - Imagem destacada indevida / Tribuna de Petrópolis

Caso corrigido: post `Datafolha: Lula e Flávio lideram rejeição com 47% e 43%; Zema tem 15% e Caiado 13%` saiu com a logomarca da Tribuna de Petrópolis como imagem destacada.

Correção aplicada:
- post público passou a usar `/hero/smoke-smoke-202605160823-lula-ironiza-caso-de-flavio-bolsonaro-com-vorcaro.webp`;
- imagem ruim original preservada em backup local do repo Astro;
- build limpo validado após remover concorrência de build local;
- commit Astro relacionado: `a40a51b Fix Datafolha post hero image`;
- URL validada: `https://www.riocarta.com/blog/smoke-202605161823-datafolha-lula-e-flavio-lideram-rejeicao-com-47-e-43-zema-tem-15-e-caiado-13/`.

Lição operacional:
- imagem destacada que seja logo/c

> *(... 456 chars omitidos — ler original)*

---

## [2026-05-19 16:52 BRT] Rio Carta — publicação destravada; gargalo real é Git/logs + autonomia incompleta

Diagnóstico Codex: o 403 em `/wp-json/wp/v2/posts` é endpoint legado e não é o caminho vivo de publicação. O Rio Carta atual publica por Astro/Markdown/GitHub/Vercel.

Causa real do bloqueio: `scripts/riocarta_publish_hourly_batch.mjs` tentava `git add` em logs ignorados (`logs/rio_carta_publication_audit.jsonl` e `logs/rio_carta_relatorio_bloqueios.md`), abortando o commit remoto.

Correção:
- `1ff1b1db Fix Rio Carta publish ignored logs`
- lote publicado via ponte local como `2ecd8740 Publish Rio Carta manual batch`
- URL validada HTTP 200: `https://www.riocarta.com/blog/smoke-202605191916-o-quinto-escalao-da-mafia-assumiu-o-governo-do-rio-diz-paes-sobre-crise-politica-no-estado/`

> *(... 289 chars omitidos — ler original)*

---

## [2026-05-22 18:37 BRT] Fórum Planejamento e Redução de Ritmo de Publicação do Rio Carta

- **Fórum**: [forum_planejamento_publicacao_riocarta_20260522.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/Foruns/forum_planejamento_publicacao_riocarta_20260522.md)
- **Objetivo**: Solicitação formal de Miguel à Trindade (Claude / Codex) para reduzir o ritmo de publicação em ~50% no crontab remoto (Tencent VPS) para preservar tokens/custos, com foco no planejamento estratégico de qualidade e finalização da programação dos agentes sociais.

---

## PONTEIROS
- Original completo: [`CEREBRO_INDEX_RIOCARTA.md`](./CEREBRO_INDEX_RIOCARTA.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`
# 🧠 MEMÓRIA PESSOAL — DS (CEO em treinamento)

**Agente:** DS (DeepSeek/DSH, Dell) · **Papel:** CEO em treinamento / chefe de equipe do ecossistema Cafezinho
**Nomeado por:** Miguel, 29/08/2026 · **Loop:** organizado 15/15 (aprendizado) · **Foco:** aprender, anotar, liderar

> **Memória em 3 lugares (ordem do Miguel):**
> 1. **Local:** este arquivo (`Cerebro/memorias_provisorias/memoria_ds_ceo_viva.md`)
> 2. **GitHub:** via repo `cerebro-miguel` (sync do Cérebro)
> 3. **GDrive:** via rclone (`drive:espelho-zcode/ds_memoria/`)

## 🎯 Missão (ordem do Miguel, 29/08/2026)

- Loop **organizado** a cada 15 min (nunca frenético): acordar → ler ponte Laura → examinar posts
  publicados/rascunhos/agendados do Cafezinho → examinar memória de bugs → **anotar bugs +
  solução proposta/encontrada** → atualizar esta memória.
- **Foco: aprendizado.** Cada ronda deve ensinar algo novo sobre o ecossistema.
- Ser treinado pelo **Claude Miguel** (chefe editorial) — instruções detalhadas do papel virão dele.
- Regra-mãe mantida: **nunca publicar/editar produção sem ordem explícita do Miguel.**

## 🗺️ Mapa do que aprendi (seed — 29/08/2026)

### Infraestrutura
- **WordPress do Cafezinho:** servidor `cafezinho-wp` (190.89.239.65, alias SSH) → `/var/www/ocafezinho/`
  (WP-CLI com `--allow-root`; o site público passa por Cloudflare).
- **Tencent SG** (43.156.151.165, alias `cingapura`/`china`): agentes, painel CCTV, sem WP.
- **NYC** (45.55.50.249, alias `nyc`): failover.
- **GDrive:** rclone `drive:` — ponte usa `drive:espelho-zcode/`.
- **AGY** (motor de publicação) roda na **Laura (Windows)**, não no servidor.

### Operação (estado em 29/08 ~13h)
- Seca do site desde 02:19 (posts agendados não disparam → suspeita de **wp-cron quebrado** + AGY pendurado).
- Esteira tem posts parados (ex.: 267724 agendado 29/08 10:05 sem disparar).
- 267727 (debate Band) **5º dia sem capa** (`featured_media: 0`).
- 268201: AGY disse "foi pra lixeira", mas **não está na lixeira** (pode ter sido excluído).
- Push do GitHub destravado (sync 10:37/10:52 + .gitignore reforçado contra segredos).

### Pontes
- Ponte Laura: `de_dell.md` (Dell escreve) / `de_laura.md` (Laura escreve) — formato `[data] REF — DE → PARA`.
- Ref do DS: `DS-YYYYMMDD-NNN`. Sinais: Miguel→DS = `charuto`; Laura→DS = `baleia` (em `~/.dsh/ponte_amizade_env`).

## 📝 Lições e bugs (append-only — a ronda anota aqui a cada achado)

<!-- A ronda faz append aqui: [data] BUG: ... / SOLUÇÃO: ... / LIÇÃO: ... -->

## 🔄 Ritual de despertar da ronda (15/15)

1. Ler ponte Laura (`Cerebro/Foruns/ponte_laura_completa/de_dell.md` + `de_laura.md`, tail)
2. Examinar posts do Cafezinho (publicados/rascunhos/agendados) — WP-CLI no `cafezinho-wp` + REST
3. Examinar memória de bugs (`Cerebro/CEREBRO_NODE_BUGS_ATIVOS.md`, `BUGS_RESOLVIDOS.md`, `BUGS_SOLUCOES.md`)
4. Anotar bugs + soluções (append aqui + nos nodos de bugs, com ref)
5. Atualizar memória viva → espelhar GitHub (push) + GDrive (rclone)
6. Relatório curto no Telegram (script)

*Última atualização: 29/08/2026 ~13h (criação — seed)*

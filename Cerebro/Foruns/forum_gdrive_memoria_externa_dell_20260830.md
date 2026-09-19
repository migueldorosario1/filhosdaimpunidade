# 🛰️ Fórum — GDRIVE COMO MEMÓRIA EXTERNA (Dell leve p/ vídeo) — 30/08/2026

**Ordem:** Miguel, 29/08 ~20h (via prompt do DS-Dell/Décio colado no ZCode Miguel). **Agente:** ZCode/GLM-5.3 (sessão 30/08 manhã). **Refs:** ponte ZM-20260830-006 (plano) e ZM-20260830-007 (fechamento). Memória irmã: `Memorias/memoria_gdrive_memoria_externa_dell_20260830.md`.

**Meta:** Dell leve para gravar/editar vídeo; Google Drive como memória externa (mount como pasta); backup do Cérebro 12h/12h; memória do DSC espelhada no Drive; todos informados na ponte.

## 1. Opinião do ZCode (registrada na ponte ZM-006)

Plano do DS-Dell está **certo no essencial** (Cérebro 272M fica; mídia fria sobe; mount vira pasta), com 4 correções de execução que evitaram pisar em engrenagens vivas:

1. **"Downloads/ antigos 78G" ≈ `Antigravity Google/` inteiro** (Cérebro + projetos vivos + `.git` 28G que NUNCA se apaga). Downloads fora do AG tem só poucos MB. Escopo corrigido para itens frios específicos.
2. **`Outros/novo livro` intocado** — tem sincronização bidirecional própria (cron 04:30 `backup_livro_gdrive.sh` com `--update` + app web escrevendo direto no Drive via `/api/drive`). Mexer = quebrar o fluxo do livro.
3. **`Outros/Aplicativos` intocado** — foi DEVOLVIDO ao workspace em 22/07 por causa dos projetos Moka/MokaVideo ativos (registro no próprio `backup_semana_gdrive.sh`).
4. **`Outros/Jornais do dia` já se arquiva no Drive sozinho** (30,5 GiB no Drive; local só guarda recentes; zero PDFs >21d em disco). Nada a fazer.

**Destravamento DSC-010:** os remotes `drive:`/`gdrive:` já estavam autorizados no Dell (shared drive 30 TiB, 29,2 livres) — o `rclone authorize` esperando login do Miguel era desnecessário para esta missão. DS-Dell avisado na ponte.

## 2. O que foi FEITO (prova viva: `~/gdrive_offload/CARIMBOS.jsonl`)

| Item | Ação | Resultado |
|---|---|---|
| Caches regeneráveis (chrome cache 2,5G, OptGuide 4G, npm, updater/uv/node-gyp/Tectonic, .deb claude-desktop) | apagados | **−7G** (63%→61%) |
| tar.gz Casa da Moeda 136M | conferido no Drive (136266629=136266629) → apagado local | ok:true |
| **Mount `~/GDrive`** | systemd user `gdrive-mount.service` (`~/.config/systemd/user/`), vfs-cache writes limitado a 2G | **NO AR** — prova escrita+leitura+remoção OK |
| **Backup Cérebro 12h/12h** | novo cron `40 15` (o 03:40 existia) — mesmo script → B2+Drive+Alibaba | instalado |
| **Memória DSH/DSC no Drive** | `drive:Backup_Total/DSH_Dell_memoria` (sessions+profiles+pacote .gpg; `deepseek_env`/`ponte_amizade_env`/`settings.yaml` EXCLUÍDOS por §82) + cron diário 06:50 | 99 arquivos no Drive |
| Purge Service Worker do Chrome (4,3G) | script `~/gdrive_offload/sw_purge_quando_fechar.sh` roda */30 e só apaga **com o Chrome fechado**; se autodesliga ao concluir | armado |
| Fila copy→check→delete | `~/gdrive_offload/rodar_fila.sh` (nohup, sobrevive à sessão): `mapa videos` 2,2G (sobe p/ `Dados_Frios/Dell_leve_20260830/mapa_videos`) · `pautas editoriais` 15G (top-up das 2.462 faltantes → apagar) · `~/legacy` 11G (53.984/53.984 JÁ conferidos → apagar) · `legenda trailer ressurrection` 7,9G (27/27 conferidos → apagar; docs e filme palestina FICAM locais) | em execução |

**Nunca tocados:** Cérebro inteiro, `AG/.git` (28G), `chaves/`, `Projeto Casa da Moeda` (cofre fundadores ILS), todos os `.env`, `Outros/indices/` (sessão do índice GDrive trabalhando lá AGORA), `novo livro`, `Aplicativos`, `Negocios Priscila/docs+filme palestina`, `.zcode/cli/memories`.

## 3. Coordenação com a sessão ÍNDICE GDrive (30/08 manhã)

Só **adicionei** pastas novas no Drive (`Dados_Frios/Dell_leve_20260830/mapa_videos`, `Backup_Total/DSH_Dell_memoria`). Nada existente foi movido/renomeado. Inventário de 30/08 pode não conter essas pastas — revarrer quando conveniente.

## 4. ⚠️ Flag de segurança (S2) — NÃO corrigido sem ordem

O `backup_acervo_100_b2_drive.sh` (diário 04:30) sobe `Outros/` inteiro para Drive+B2 **incluindo `chaves/` em texto plano** (desde 17/08). Sugestão: acrescentar `--exclude 'chaves/**'` (e cia.) ou migrar p/ pacote .gpg como o DSC-013. Pendência registrada; nenhum valor exposto em chat/fórum.

## 5. Como usar / retomar / restaurar

- **Acessar o Drive no Dell:** pasta `~/GDrive` (qualquer app do Miguel abre como pasta normal). Escrita ok (cache 2G máx). Serviço: `systemctl --user status gdrive-mount`.
- **Retomar/auditar a fila:** `tail ~/gdrive_offload/offload.log` + `cat ~/gdrive_offload/CARIMBOS.jsonl` (cada item só apaga com `rclone check` limpo: missing=0, diff=0, matched>0).
- **Restaurar algo:** `rclone copy "drive:<dest>" "<caminho local>"` (ex.: pautas → `rclone copy "drive:pautas editoriais o cafezinho" ".../Outros/"`).

## 6. Estado da missão (formato Regra nº 3)

- **O que aconteceu:** caches −7G; mount no ar; crons 12h/DSC/purge instalados; memória DSC no Drive; fila de ~36G (2,2+15+11+7,9) rodando com gate de prova; ponte avisada (ZM-006) e empurrada.
- **O que falta:** fila terminar (ver CARIMBOS.jsonl — cada item tem carimbo ok:true/false); purge do Service Worker (dispara sozinho quando o Chrome fechar); recarregar Drive na cabeça das rotinas que usavam as pastas movidas (ponteiros .txt deixados nos lugares).
- **O que preciso do Miguel:** nada obrigatório. Opcional: (1) fechar o Chrome uma vez p/ liberar os 4,3G de Service Worker; (2) decidir sobre a flag §4 (excluir chaves do acervo-100); (3) se quiser AINDA mais leve, os próximos candidatos são `AG/Cicero Agentes` 902M e `AG/scratch` 885M (menor prioridade).

## 7. ADENDO ~11:30 — NOVA ORDEM: MIGRAÇÃO TOTAL EM 3 DIAS (Miguel, voz 30/08 ~11:15)

**"Tudo vai para o G-Drive. Fica só o Cérebro e os arquivos de trabalho. Nada pode se perder — backup duplo GDrive + Backblaze. Pra ganhar tempo: primeiro GDrive, depois GDrive→Backblaze. Hoje já deixa leve com os pesadões. Vistoria ampla primeiro (programas, arquivos sujos, sujeira de instalação) — sem limpar nada de programa ainda. 3 dias."**

### Retificação importante (caso-escola)
O item "pautas: 2.462 faltando no Drive" do meu primeiro relatório estava **INVERTIDO**: a convenção do `rclone check --combined` provada empiricamente — `- ` = existe SÓ NO DESTINO (Drive). O Drive `pautas editoriais o cafezinho` tem **3.552 objetos/28,5 GiB** vs 1.090/15G locais: **o Drive é SUPERCONJUNTO** (guarda 2.462 arquivos que o Miguel já apagara do disco no passado). Gate do `offload_item.sh` corrigido: bloqueia em `+ ` (só-local=faltando no Drive) e `* ` (hash difere); `- ` não bloqueia. O carimbo ok:false das pautas foi falso-negativo SEGURO (nada apagado); re-run na fila 2.

### Cadeia do Dia 1 (encadeada pela mesma trava, provas em CARIMBOS.jsonl / CARIMBOS_B2.jsonl)
1. `rodar_fila.sh` (fila 1): mapa videos ✅ ok:true 2,33G · pautas falso-bloqueio (retificado) · legacy (cópia em curso) · legenda trailer
2. `fila2_dia1.sh`: **pautas 15G (gate corrigido → libera)** · legacy retry `--skip-links` (symlinks davam falso-positivo) · **lixeira 4G com BACKUP no Drive antes de esvaziar** · legenda retry
3. `relay_b2_dia1.sh`: espelha Drive→B2 (`backup-total-local-2026`) de tudo que subiu hoje = **backup duplo**

### Vistoria ampla (sem limpar nada — relatório p/ decisão do Miguel)
| Achado | Tamanho | Classificação | Proposta |
|---|---|---|---|
| Lixeira (~/.local/share/Trash) | 4,0G | lixo | Dia 1 (com backup antes de esvaziar) |
| snapd (revisões desativadas) | 5,8G | sucata de instalação | Dia 2: `snap remove --revision` das desativadas + `refresh.retain=2` |
| Docker (2 imagens, 0 containers) | 610M | sucata | Dia 2: `docker image prune -a` |
| Android SDK + .android | 7,4G | ferramenta (TWA Moka) | Dia 2/3: decidir com Miguel (arquivar se não fizer mais builds) |
| .pyenv | 7,0G | TRABALHO ATIVO (crons usam 3.10.13) | FICA |
| .nvm | 4,1G | TRABALHO ATIVO (dsh/node) | FICA (limpar versões node velhas no Dia 2) |
| .rustup + .cargo | 1,7G | provável órfã | Dia 2: conferir uso → arquivar |
| /tmp, apt cache, journals | ~600M | sucata | Dia 2 |
| 4kvideodownloader ×2 (plus e normal) | 654M | programas duplicados | Dia 2: desinstalar um (ou os dois) c/ aval |
| Kernels antigos (5.4 headers + 5.14 oem) | ~1G | sucata de instalação | Dia 2: remover com aval |
| RAM/boot | — | saudável | RAM 8,5G livres (bom p/ vídeo); boot 55s (plymouth 21s+NM-wait 9s otimizáveis) |
| AG/.git | 28G | histórico vivo | Dia 3: decidir backup-only p/ Drive |

**Estado:** o que aconteceu = Dia 1 em execução (cadeia acima). O que falta = filas terminarem (provas nos carimbos), relay B2, e as decisões do Miguel sobre a tabela do Dia 2. O que preciso do Miguel = "vai" para os itens da vistoria (snap/docker/kernels/4k/Android/rust).

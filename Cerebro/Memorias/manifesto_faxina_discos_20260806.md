# 🧹 MANIFESTO — Faxina de discos NYC + Rio-Carta-Agentes (06/08/2026)

> **Autorização do Miguel (06/08 ~12:55 BRT):** "pode limpar o que não vai fazer falta... leva pro Backblaze e a gente apaga. Lembrando que tudo tem que ser mapeado e indexado. Antes de apagar, tem que indexar e mapear... pode limpar à vontade. E esse emergencial do Rio Carta Agentes, pode fazer, é emergência."
> **Executor:** ZCode (Kimi K3), chat direto. **Regra aplicada:** indexar (nome/tamanho/md5/data) → subir B2 → verificar no B2 → só então apagar local.
> **Contexto:** `Foruns/forum_mapa_servidores_ecossistema_20260806.md` + `Memorias/memoria_mapa_servidores_ecossistema_20260806.md`.

---

## ✅ RESULTADO GERAL

| Máquina | Antes | Depois | Livre |
|---|---|---|---|
| Rio-Carta-Agentes (24G) | **100%** (0 livre) 🚨 | **87%** | 3,2 GB |
| NYC failover-vigia (48G) | **94%** (3,1G) | **79%** | 11 GB |

---

## 1. Rio-Carta-Agentes (159.89.185.209)

### 1a. Apagado direto (lixo puro, indexado antes — sem valor p/ B2)

| Item | Tamanho | md5 / nota |
|---|---|---|
| `cicero/.git/objects/pack/tmp_pack_UyvzqK` | 86 MB | `a353490a12ff48cb870e0ae41b293885` — resto de git fetch interrompido (01/08) |
| `cicero/.git/objects/pack/tmp_pack_mL4BQs` | 1,16 GB | `ee9c8b107e1d55b68d765d840f865a99` — idem (24/07) |
| `/var/log/btmp.1`, `auth.log.1`, `syslog.1`, `auth.log.{2,3,4}.gz` | ~120 MB | logs rotacionados |
| `/var/cache/apt` (`apt clean`) | 114 MB | cache de pacotes |
| journal systemd (rotate+vacuum p/ 100M) | ~16 MB | journal ativo não arquiva mais que isso |

### 1b. B2 → verificado → apagado local

| Item | Tamanho | Destino B2 (verificado via `rclone lsl`) |
|---|---|---|
| `votacao_candidato_munzona_2022.zip` | 578.876.095 B | `b2:failover-cafezinho1/faxina/rio_carta_agentes_20260806/` ✅ |
| `votacao_candidato_munzona_2024.zip` | 48.427.594 B | idem ✅ |

### 1c. Instalado
- **do-agent 3.18.14** (métricas p/ painel DO) — `active` ✅. Antes não existia no droplet.

### Não mexido (proposital)
- `swapfile` 6,1G (RAM é só 1G — vital) · clones git (packs são o histórico real; `git gc` não comprimiu — já otimizados) · `cicero_inbox.db`/`gsn_inbox.db` (vivos) · `ceara_publication_audit.jsonl` 197M (auditoria viva — candidato a rotação futura).

## 2. NYC failover-vigia (198.199.121.136)

### 2a. Vacuum
- journal systemd: rotate+vacuum → **827,5 MB liberados**.

### 2b. B2 → verificado → removido local (`rclone move`)

| Item | Tamanho | Destino B2 |
|---|---|---|
| 6× `banco_imagens_reais.db.pre_janitor_2026062{1,2}_*` | 2,33 GiB | `b2:failover-cafezinho1/faxina/nyc_20260806/backups_midia_pre_janitor/` ✅ |
| 2× `banco_indice_midia_v3_pre_view_v3_foto_destacada{,_2}_20260626_*.db` (**gêmeos — md5 idêntico `e1a6eb3b8516dc5f274a933a8ef62ce1`**) | 2 × 1,29 GB | `.../nyc_20260806/backups_pre_view/` ✅ |
| 4× dirs `banco_midia_andre_mendonca_*_2026062{6,9}_*` (db+shm+wal) | ~1,3 GB | `.../nyc_20260806/andre_mendonca/` ✅ |
| staging zips rio-ag | 598 MiB | `.../rio_carta_agentes_20260806/` ✅ |

**Manifesto remoto:** `/root/faxina_20260806_b2_manifest.txt` (no NYC) = listagem `rclone lsl` pós-upload.

### Não mexido (vivo ou sensível)
- `/root/agent_data/banco_midia/banco_indice_midia_v3.db` 1,3G (**VIVO** — cópia do master Tencent) · `/root/venv` 7,7G · `/root/backups/` restante · `log_rotas_llm.jsonl` 160M (telemetria viva — candidato a rotação).

## 3. Notas operacionais

- **Bucket usado:** `failover-cafezinho1` — o remote `b2:` do NYC tem app key restrita a ele. Tentativa anterior com a key `cafezinho-backups-rw` (do cofre local) **falhou** no NYC com erro B2 "not currently supported on API version number 1" — chave possivelmente incompatível com a versão do rclone do servidor. **Re-home futuro:** server-side copy `faxina/` → bucket `cafezinho-backups` usando a master key local (`Outros/chaves/backblaze_b2.env`), se o Miguel quiser o bucket semanticamente certo.
- **Nova app key B2 `sites-tematicos-2`** (criada pelo Miguel no console, 06/08 ~13:10 BRT): guardada no cofre canônico `Outros/chaves/backblaze_sites_tematicos_2.env` (chmod 600, **valores nunca em chat/fórum**). Testada: acesso restrito ao bucket **`site-tematicos`** ✅. Uso: backups dos sites temáticos.
- **do-agent:** instalado+ativo também em `gsn-youtube-nyc-01` (antes: 2/5 droplets sem métricas). Agora 4/4 droplets acessíveis reportam ao painel DO (GSN WP zumbi sem acesso SSH).
- **Pendências:** (a) Miguel criar alert policies 80/90% no painel DO (caminho: menu esquerdo **Insights → Monitoring → Create Resource Alert**); (b) decidir destino do droplet gsn-youtube-nyc-01 (ocioso) e do GSN WP zumbi; (c) re-home B2 opcional; (d) Alibaba — confirmar fim da cobrança; (e) ServerDo — reboot diário 03:31 (investigar).

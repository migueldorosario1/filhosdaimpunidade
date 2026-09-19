# Fórum — Faxina Rio-Carta lote01: ZM assume a bandeira do Astra (05/09/2026)

> **Data:** 2026-09-05 20:24 BRT · **Autor:** ZM (ZCode/GLM-5.3) · **Status:** ✅ MISSÃO CUMPRIDA COM GATES
> **Memória (log técnico completo):** `Memorias/memoria_faxina_rio_lote01_zm_20260905.md`
> **Ordem do Miguel (~20h, voz):** assumir a bandeira do Astra (GPT-6), limpar o servidor do Rio Carta com muita segurança — "analisa primeiro" — e usar a experiência para planejar a faxina dos demais servidores (Cafezinho, Moka).
> **Base:** parecer do tutor DS-N Chefe 05/09 09:06 (RESPOSTAS.md) + `forum_plano_faxina_continua_droplets_20260807.md` (override 11/08: nada sem indexação+backup+autorização) + `PLANO_ASTRA_RETIRADA_REVISAO_DSN_ZM_20260905.md` do Astra.

## 1. O que aconteceu (resumo executivo)

1. **Gates do tutor fechados um a um** (era a pendência do recibo TG-112 do Astra):
   - Acesso durável ao inventário + complemento CONFIRMADO (hashes idênticos; documentos no GitHub origin/main nos commits abbe37011 e ecd19767 + cópias locais).
   - Backup B2 reconferido de ambiente independente: os 3 objetos do lote01 baixados na Tencent com SHA256 idêntico ao recibo AST-011 (custo de egress ~US$0,01).
   - **Ensaio de restauração em cópia isolada (Tencent /root/zm_ensaio_rio_20260905/): 17/17 verde** — conteúdo, uid/gid 0:999, modo final 0640, ACL `system.posix_acl_access` efetiva (hash do valor idêntico), `user.crtime_usec`, mtime/atime em nanossegundos, e journalctl leu/parsou os journals recuperados (exit 0, JSON válido, 3 amostras). Relatório: `Memorias/zm_relatorio_ensaio_rio.json`.
2. **Achado crítico na revalidação ao vivo:** o systemd-journald do Rio já tinha removido sozinho **12 dos 17** candidatos (A01–A12, os mais antigos) entre 08:26 e ~20:10 — vacuum por disco cheio (96%, sem overrides no journald.conf; KeepFree violado faz o journald devorar os arquivados mais antigos). **Sem perda:** o backup lote01 do Astra (07:54) cobre os 17 byte a byte, feito ~12h antes da remoção pelo sistema.
3. **Retirada executada dos 5 remanescentes** (A13–A17), com revalidação imediata no ato (5/5 SHA256 idênticos ao inventário, metadados 0:999/0640/nlink1, nenhum processo com arquivo aberto — aborto automático se divergisse): caminhos literais, sem glob. **220.000 KB (~215 MiB) liberados; ocupação 96% → 95%.**
4. Preservados e verificados antes E depois: `system.journal` ativo + os **26 excluídos** (contagem da base 43→38 = exatamente −5). Serviços saudáveis antes e depois: caddy=200, cicero_admin=302, journald active.

## 2. Números antes/depois (Rio-Carta-Agentes 159.89.185.209)

| Métrica | Antes (20:10) | Depois (20:20) |
|---|---|---|
| Ocupação / | 96% | **95%** |
| Livre | 1.202.492 KB | **1.427.984 KB** |
| Arquivos na base journal | 43 | 38 (−5 exatos) |
| caddy :80 / cicero :5000 | 200 / 302 | 200 / 302 |
| journald | active | active (uso 1.4G) |

## 3. Causa estrutural (o que realmente cresce no Rio — mapeado hoje)

- **/root = 10,7 GB (46% do disco!):** git packs com imagens versionadas — `riocarta_remote` 3,9G + `cicero_remote` 3,6G + `gsn_remote` 1,7G (≈9,2G) + `agentes` 0,7G + `.npm` 0,2G.
- **/var/log/journal = 1,4–1,8 G** e **voraz**: sem overrides no journald.conf; com o disco em 96% o journald apaga os arquivados mais antigos sozinho (comprovado hoje) — e **vai comer os 26 preservados em dias, sem backup**.
- O lote01 (~398 MB nominais; 220 MB reais agora) era, como o tutor disse, ajuda pequena.

## 4. Recomendações Rio — AGUARDAM "VAI" DO MIGUEL (nada executado)

1. **URGENTE — lote02 de BACKUP dos 26 excluídos** (+ novos que nasceram): mesmo rito do Astra (inventário → B2 cifrado → verificação). Motivo: o journald está em modo voraz e os 26 não têm cópia. Custo ~US$0,01.
2. **journald.conf**: `SystemMaxUse=400M` + `MaxFileSec=30d` — estanca o voraz e recupera ~1,0–1,4G. É mudança de retenção global: decisão do Miguel (plano Astra §7 manda consultar).
3. **git gc nos 3 repos** (compacta, não perde conteúdo; −2 a −3G estimados) + purge `.npm` (206MB) — decisão pendente desde o fórum de 07/08.
4. Com 1+2+3: Rio estimado em ~65–70%.

## 5. Plano dos demais servidores (medição de hoje 20h, vigia + SSH)

| Servidor | Hoje | Causas do crescimento | Prioridade / ação | Backup |
|---|---|---|---|---|
| **Rio-Carta-Agentes** | **95%** 🔴 | git packs 9,2G + journald voraz (ver §3) | itens §4 acima | B2 `faxina/rio-ag/` (padrão lote01 provado) |
| **NYC-failover (V4)** | 70% 🟡 | logs ciclos LLM + bancos custos (era 79% em 07/08 com pip 4,2G — hoje pip 18M) | confirmar pontos quentes atuais; archiver V4 segue | archiver V4 + B2 faxina/ |
| **Tencent (painéis+Moka)** | 68% 🟡 | `backups/` 9,2G fora do B2 (censo 07/08) + v6_data/jsonl | levar backups/ ao B2 com verificação, depois limpar | B2 espelho existente |
| **ServerDo WP Cafezinho** | 42% 🟢 | WP cresce devagar (posts+imagens em /var/www) | rotina: dump WP + uploads → B2; sem limpeza agora | (a definir — ver cofre/site-tematicos) |
| **Espelho cafezinho.news** | 29% 🟢 | /var/www 13G | monitorar | — |
| **gsn-youtube-nyc (central alertas)** | 41% 🟢 | journald 487MB | limitar SystemMaxUse quando mexer | — |
| **Moka** | 🟢 | sem servidor dedicado: 64M na Tencent + app no Ousadia; peso real = repo git (imagens) | nada em disco; usar tags/git como backup (já existente) | tags + GDrive |

**Regra para todos (override 11/08 mantido):** indexar item por item → backup B2 verificado → prova de restauração em cópia isolada → autorização explícita do Miguel → só então retirar; vigia :42 já alerta 🟠85/🔴95.

## 6. Estado / o que falta / o que preciso do Miguel

- **O que aconteceu:** gates fechados com provas; 12 já tinham sido removidos pelo próprio journald (backup cobre); 5 retirados com revalidação no ato; 220 MB reais liberados; Rio 96→95%; serviços íntegros; causa estrutural mapeada (git packs + journald voraz).
- **O que falta:** decisões do §4 (lote02 urgente, journald.conf, git gc/.npm); plano fino NYC/Tencent (backups ao B2) aguarda "vai" também.
- **O que preciso do Miguel:** o "vai" para o §4.1 (lote02) é o mais urgente — os 26 journals preservados correm risco real de sumirem sem cópia. §4.2 e §4.3 podem ir juntos no mesmo pacote de decisão.

## Recibo

- Ensaio: `Memorias/zm_relatorio_ensaio_rio.json` (Tencent, 17/17, journalctl verde; área de ensaio apagada, só relatório+scripts permanecem).
- Espaço liberado hoje pela ação ZM: 225.492 KB (df antes/depois). Zero perda: 17/17 com cópia B2 validada + restauração provada; 12 remoções foram do próprio journald, documentadas aqui.
- Sem despesas além de egress B2 ~US$0,01 (download de verificação 94MB, igual ao readback que o Astra já faz).

## ADENDO 1 — 20:4x — ordem do Miguel: HOJE SÓ RIO; lote02 autorizado

Ordem direta do Miguel (05/09 à noite): "não mexe no cafezinho canonico não. no tencente, faz antes uma análise mais profunda de segurança. hoje vamos mexer apenas no rio carta". Registrado:

- **Cafezinho canônico (ServerDo): VETADO hoje** — nenhuma ação, nem rotina de backup; sai do escopo imediato.
- **Tencent: CONDICIONADA** — qualquer faxina lá (backups/ 9,2G → B2 etc.) exige ANTES análise de segurança mais profunda (a definir em sessão própria; não é hoje).
- **Rio: pacote §4 autorizado para hoje** — lote02 de backup (em execução agora), teto do journald (SystemMaxUse=400M + MaxFileSec=30d, via drop-in com .bak) e depois git gc nos 3 repos + purge .npm. Ordem de segurança mantida: NENHUM vacuum antes do lote02 validado no B2.
- Passphrase do lote02 espelhada nos 3 cofres (alias ZM_RIO_JOURNALS_LOTE02_20260905_PASSPHRASE) com backup prévio datado — Regra 4 cumprida (verificação por hash 3/3).

## ADENDO 2 — 21:1x — pacote Rio executado: 96% → 88%

Com o "vai" da noite (só Rio), executado na ordem de segurança:
1. **Lote02 validado**: inventário 36 journals/1,5 GB (hash duplo+xattrs, ativo preservado, 1 aberto pulado) → manifesto prévio no GitHub ANTES do upload → tar USTAR (36+inventário+manifesto) → GPG AES256 (passphrase própria nos 3 cofres, Regra 4) → B2 `zm_20260905_lote02/` → readback na Tencent: hashes idênticos, 36/36 conferidos, journalctl lendo. Recibo no manifesto.
2. **Teto do journald**: drop-in SystemMaxUse=400M + MaxFileSec=30d + restart + vacuum → **1,1 GB liberados**; o voraz está contido (antes: apagava histórico sozinho; agora: teto duro de 400M e 30 dias).
3. **git gc ×3 + npm**: gc quase neutro (−26 MB cicero; packs já compactados — imagens no histórico são a causa); `.npm/_npx` −201 MB.
4. **Resultado: 96% → 88%, 2,9 GB livres.** Serviços saudáveis em todas as medições (caddy 200, cicero 302, journald/caddy/cicero_admin active).
5. Pendências/decisões futuras (não executadas): imagens versionadas nos git packs (≈6,1 GB — LFS ou repo de mídia é decisão arquitetural); 1 journal aberto fora do lote02 (coberto pelo teto); faxina Tencent SÓ APÓS análise de segurança profunda (ordem do Miguel); Cafezinho canônico vetado hoje.

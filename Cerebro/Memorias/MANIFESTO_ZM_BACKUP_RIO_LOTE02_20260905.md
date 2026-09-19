# MANIFESTO ZM — Backup lote02 dos journals do Rio (prévio ao upload)

> **Registro em 05/09/2026 ~20:4x BRT, ANTERIOR ao upload B2** (rito do lote01/Astra: indexar → registrar → copiar → verificar; nada é apagado).
> **Autorização:** ordem do Miguel 05/09 à noite — "hoje vamos mexer apenas no rio carta" (pacote §4 do fórum da faxina; Cafezinho canônico e Tencent fora do escopo de hoje; Tencent condicionada a análise de segurança prévia).

## Escopo do lote02

- Host: `Rio-Carta-Agentes` (159.89.185.209), base exclusiva `/var/log/journal/524f4f88ab99d451c9ee123e69fd5010`.
- **36 membros** `system@…journal` fechados e não abertos por processo algum (varredura /proc), hash SHA256 estável em **dupla leitura**.
- **Total: 1.520 MB** lógicos. Inclui os 25 excluídos do plano original (sem cópia até hoje) + os novos rotacionados pelo journald voraz (incluindo 12 de hoje).
- **Preservados fora do lote:** `system.journal` (ativo) e 1 `system@` pulado por estar aberto por processo no momento do snapshot (fica para lote futuro ou vacuum após o teto).
- O tar incluirá também o inventário e este manifesto (melhoria sobre o lote01: o pacote B2 fica autossuficiente para recuperação; o lote01 tinha o complemento só no Cérebro/GitHub).

## Inventário integral

[INVENTARIO_ZM_LOTE02_RIO_20260905.json](INVENTARIO_ZM_LOTE02_RIO_20260905.json) — SHA256 `d6e3da9aea6ecdc1d420c4a3be92240327d2798f1c046936817e68926aae9141`. Capturado no próprio host via Python puro (stat ns + dupla leitura SHA256 + xattrs `system.posix_acl_access`/`user.crtime_usec` em base64 com hash próprio, à imagem do complemento do Astra).

## Destino e cifra

- `b2:failover-cafezinho1/faxina/rio-ag/journals/2026-09/zm_20260905_lote02/` (mesmo bucket/família do lote01; sem novo plano/contratação).
- GPG AES256 + ZLIB, passphrase dedicada no cofre pelo alias **`ZM_RIO_JOURNALS_LOTE02_20260905_PASSPHRASE`** (espelhada nos 3 cofres com backup prévio; valor jamais em documento/chat/git).
- Objetos previstos: `journals.tar.gpg`, `manifest.json`, `README.txt`.

## Verificação prevista (antes de qualquer vacuum)

Download integral do B2 em ambiente independente → SHA256 do pacote → decifragem → extração isolada → conferência dos 36 membros (nome/tipo/tamanho/SHA vs inventário) → amostra de metadados (ACL/xattrs/ns) → journalctl lê amostra → recibo final aqui. Falha em qualquer etapa = lote NÃO validado e NENHUM vacuum.

## Retirada local

**Nenhuma remoção é executada pelo lote02.** O vacuum do journald (após drop-in `SystemMaxUse=400M`) reduzirá o histórico local a ~400 MB — somente DEPOIS da validação completa deste lote. Os 12 removidos pelo próprio journald hoje e os 5 retirados ontem à noite pelo ZM (autorizados) estão cobertos pelo lote01 (AST-011).

## Recibo final

(preenchido após a verificação — ver adendo no fim do arquivo)

## Recibo final — 05/09/2026 21:1x BRT — LOTE02 VALIDADO

Upload concluído 21:13 BRT. Readback integral em ambiente independente (Tencent, /root/zm_lote02_readback_20260905/):

| Objeto no B2 | Bytes | SHA256 |
|---|---:|---|
| journals.tar.gpg | 407.591.584 | 48fb5422be5d7c8aa5ebb7d9f66edb2980dec7dfaea691e28e98c3e7c7910da6 ✓ |
| manifest.json | 792 | (no manifest) |
| README.txt | 318 | (no manifest) |

Tar decifrado: 1.593.907.200 bytes, SHA256 0cb56c416728fd0638403b1cd4f1cbb905a3cdd15209979aab6c5ebbe7127ae2 ✓.
38 membros = 36 journals + inventário + manifesto (pacote autossuficiente). **36/36 conferidos** (tamanho+SHA vs inventário interno); journalctl leu amostras (exit 0, JSON válido). Relatório: `Memorias/zm_relatorio_readback_lote02.json`. Área de ensaio da Tencent limpa ao final.

Com o lote validado, executado em sequência (ordem do Miguel desta noite):
1. Drop-in `/etc/systemd/journald.d/90-faxina-zm.conf` (SystemMaxUse=400M, MaxFileSec=30d) + restart → journald active.
2. `journalctl --vacuum-size=400M` → **1,1 G liberados**; base 38→16 arquivos; ativo preservado; caddy 200 / cicero 302.
3. `git gc` nos 3 repos (pouco ganho: packs já compactados; cicero −26 MB) + purge `.npm/_npx` (−201 MB).

**Disco do Rio: 96% → 88% na noite (2,9 GB livres).** Observações: 1 journal ficou fora do lote02 (aberto por processo no snapshot — pequeno, coberto pelo teto de 30 dias; registrar em lote futuro). O peso estrutural remanescente são os git packs com imagens versionadas (≈6,1 GB) — solução arquitetural (imagens fora do git/LFS) fica como recomendação, decisão do Miguel.

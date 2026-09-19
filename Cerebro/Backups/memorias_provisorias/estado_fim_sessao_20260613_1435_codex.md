# Estado de Fim de Sessão — Codex

**Data:** 2026-06-13 14:35 BRT  
**Contexto:** computador do Miguel vai desligar; retomada deve partir deste ponto.

## Estado Atual da Grande Reforma

O sistema está em pausa de segurança na migração lado a lado Tencent.

**Não há autorização Codex para deploy, smoke tests 5–8, cron novo, WordPress ou `--apply --yes`.**

## Fatos Confirmados

1. A árvore local patcheada da Grande Reforma está em:
   `Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/`

2. Patches locais aplicados:
   - `Sistema/publicador/publicador_cafezinho.py` carrega `.env.unificado`, lê `WP_STATUS_GLOBAL`/`WP_STATUS`, aceita `draft`, `pending`, `private`, `publish`, mas escrita real só com `--apply --yes`.
   - `Sistema/midia/agente_midia.py` carrega `.env.unificado`, lê `BANCO_MIDIA_DB`, fallback para `/root/agent_data/banco_midia/banco_imagens_reais.db`, e rede/upload/escrita só com `--apply --yes`.
   - `Config/.env.unificado.example` criado com:
     - `WP_STATUS_GLOBAL="draft"`
     - `BANCO_MIDIA_DB="/root/cafezinho/dados_agentes/banco_midia/banco_imagens_reais.db"`

3. Validações locais passaram:
   - `python3 -m py_compile` nos scripts tocados.
   - `--help` dos scripts principais.
   - `agente_midia.py` sem flags roda dry-run sem WP, sem IA externa, sem upload e sem escrita.

4. Kimi iniciou smoke tests Tencent e pausou corretamente:
   - Testes 0–4 parcialmente/majoritariamente OK.
   - Testes 5–8 não executados.
   - Ela reconheceu que copiou código do legado para staging remoto.

5. Auditoria remota somente leitura Codex confirmou:
   - `/root/cafezinho` na Tencent contém código legado amplo.
   - Há muitos scripts com `wp/v2/posts` e `wp/v2/media`.
   - `motor_publicador.py` remoto em staging ainda decide `status_post = "draft" if como_rascunho else "publish"` e não usa `WP_STATUS_GLOBAL` no ponto decisivo.
   - `/root/cafezinho` tem 157 arquivos `*.py`, `*.sh` ou `.env*`.
   - Banco staging está em permissões `644`; pasta `755`, ainda não `640/750`.
   - Snapshot `/root/snapshot_root_pre_reforma_20260613.tar.gz` existia com 4.2G e PID `274072` ainda aparecia em execução no momento da checagem.

6. Canal Trindade foi rotacionado constitucionalmente:
   - backup: `Projeto Cafezinho Agentes/Foruns/historico_canal_trindade/rotacao_constitucional_20260613_1420/canal_trindade_20260613_1420.md`
   - manifesto: `Projeto Cafezinho Agentes/Foruns/historico_canal_trindade/rotacao_constitucional_20260613_1420/MANIFESTO_ROTACAO_CANAL.json`
   - canal atual: 28 linhas.

7. Atualização posterior (~16:05 BRT): Kimi corrigiu o erro e limpou o staging remoto.
   - Verificação Codex somente leitura confirmou:
     - `/root/cafezinho/portal_cafezinho`: `COUNT=0`
     - `/root/cafezinho/sites_tematicos`: `SITES_COUNT=0`
     - banco `/root/cafezinho/dados_agentes/banco_midia/banco_imagens_reais.db`: preservado com 17M
     - permissões atuais do banco/pasta: `root:ubuntu`, `770/660`
     - snapshot PID `274072` não está mais vivo
     - snapshot `/root/snapshot_root_pre_reforma_20260613.tar.gz` existe com 6.4G
   - Consequência: risco imediato de executar publicadores legados dentro do staging foi removido.
   - Bloqueio permanece porque ainda não há código pós-reforma patcheado em `/root/cafezinho/portal_cafezinho`.

## Fóruns Relevantes

- Plano migração lado a lado:
  `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_plano_migracao_duplicada_lado_a_lado_tencent_20260613.md`

- Smoke tests Tencent/Kimi:
  `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-13/forum_smoke_tests_tencent_executados_20260613.md`

- Canal Trindade atual:
  `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`

## Bloqueio Atual

**Testes 5–8 estão bloqueados.**

Não executar:

1. `maestro_editorial.py --apply --yes`
2. publicadores em `/root/cafezinho/portal_cafezinho`
3. corretores/curadores/agentes temáticos com `wp/v2/posts` ou `wp/v2/media`
4. cron novo
5. `git push` dos temáticos
6. qualquer smoke com escrita real em WordPress
7. copiar legado novamente para staging

## Próxima Decisão Necessária de Miguel

Escolher uma destas opções:

1. **Recriar staging remoto a partir de artefato mínimo local patcheado**  
   Recomendação Codex. Mais limpo e menos risco que remendar 157 arquivos legados.

2. **Autorizar patch remoto supervisionado**  
   Mais arriscado; só deve ocorrer com manifesto de arquivos, backup, `py_compile`, `rg` de segurança e sem cron.

Sem essa decisão, o estado correto é permanecer pausado.

## Primeiro Passo na Retomada

Ler:

1. Constituição:
   `Projeto Cafezinho Agentes/A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/CONSTITUICAO_DA_GRANDE_REFORMA.md`
2. Este arquivo.
3. Os dois fóruns acima.
4. Canal Trindade atual.

Snapshot remoto já foi confirmado como terminado às ~16:05 BRT. Se quiser reconfirmar na retomada:

```bash
ssh tencent 'ps -fp 274072 || true; ls -lh /root/snapshot_root_pre_reforma_20260613.tar.gz 2>/dev/null || true; find /root/cafezinho/portal_cafezinho -mindepth 1 -maxdepth 1 | wc -l'
```

Somente leitura, sem alterar nada.

— Codex, 2026-06-13 14:35 BRT

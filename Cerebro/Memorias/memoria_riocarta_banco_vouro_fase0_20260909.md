# Memória técnica — Rio Carta × Banco de Mídia V-Ouro (FASE 0 viva) + curadoria RJ

Data: 09/09/2026 · Sessão: ZCode Qwen3.8-Max (Dell) · Fórum irmão: `Foruns/forum_riocarta_banco_vouro_fase0_20260909.md`

## 1. Diagnóstico (por que o Rio Carta "não tinha" banco)

- FASE 0 existe desde 05/08 em `/root/tematicos/agentes_tematicos/v4/publicador.py` (~linhas 446-501): `from nucleo_banco_midia import buscar_no_banco`; candidatas[:8] ANTES da cascata externa; exceção → log "banco de mídia indisponível — seguindo cascata externa".
- `nucleo_banco_midia.py` lê `BANCO_DIR = ../../agent_data/v4/banco_midia` (index.json + img/). Esse espelho só existia no Dell (sync 05/08 via banco_midia_sync.py). Pipeline V4 roda no NYC → FASE 0 morta ([] sempre).
- Achado: `/tmp/banco_midia_export.tar.gz` de 17/08 09:24 (2,75GB) no NYC = dump feito e NUNCA extraído lá. Apagado e regenerado.
- Forense execucoes_ouro: escritor "fantasma" de 30min = ronda DeepSeek do Dell (`ronda_30min.sh` → dsh headless → SSH NYC → python heredoc); exec 2389 sem fim (~03:00 BRT 09/09); últimos ciclos 0 aprovações. NÃO ressuscitar (economia).
- Aprovações RJ de 05/08 foram para --db de teste (sem linha "once" no execucoes_ouro vivo) → banco vivo nunca as recebeu.

## 2. Coleta RJ no banco vivo (NYC)

- Patch em `/root/V3/robo_banco_ouro_midia_v3.py`: bloco `PACOTE_RJ_RIOCARTA_20260909` no ENTIDADES_PADRAO (backup `.bak_pre_pacote_rj_20260909`): Ricardo Couto 97, William Siri 84, Carlos Jordy 80, Carlos Portinho 78, Andre Marinho 74, Anthony Garotinho 74.
- Manifesto `/root/V3/manifest_rj_20260909.json`: 10 entidades (Couto 97, Paes 92, Benedita 88, R.Neves 84, Siri 80, Jordy 76, Portinho 74, Marinho 70, Garotinho 70, Castro 66).
- Comando: `cd /root/V3 && nohup /root/venv/bin/python3 robo_banco_ouro_midia_v3.py --manifest /root/V3/manifest_rj_20260909.json --confirmar --max-aprovadas 40 --limite-por-entidade 14 --max-aprovadas-por-entidade 6 >> /root/agent_data/logs/robo_rj_20260909.log 2>&1 &` (2 corridas; total +40 aprovadas).
- Resultado no banco vivo (`/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db`, total 1294): Couto 12, Neves 6, Benedita 6, Portinho 6, Garotinho 6, Siri 2, Jordy 1, Castro 1, Paes 0 (purgado), Marinho 0 (sem foto encontrada).
- QA visual (Dell /tmp): couto1/couto2 (EBC Fiocruz 23/05/26, Couto no pódio + Lula de chapéu) = genuínas; imgl5902/5871/5991 (álbum GovRJ evento França 01/06/26) = mesmo homem calvo-barba-grisalha = Couto (5991 = foto de assinatura com representante francês). VEREDITO: manter.

## 3. Purga Paes + GUARDA_CURADORIA

- Motivo: álbum Flickr GovRJ "Reunião com prefeito Eduardo Paes" (15/01/2024) — cena real = evento de saúde com camisas "SAÚDE"/bandeira; homem central (~40a, camisa branca) NÃO é Paes; descrição copy-paste do álbum; e foto com Castro inapropriada p/ linha editorial.
- Purga 1 (10:31 UTC): 5 linhas de midia_ouro + rejeicoes `curadoria_riocarta_20260909`. Robô relançado RE-APROVOU as 5 (+1 nova) em 10:35 — causa: robô nunca lê rejeicoes_ouro (grep `FROM rejeicoes_ouro` = 0 hits); dedup = só hash em midia_ouro (linha ~1213).
- Purga 2: 6 linhas apagadas de midia_ouro + midia_ouro_fts + midia_ouro_indice; 11 rejeicoes curadoria_* no total.
- Patch GUARDA_CURADORIA_20260909 no robô (antes do hash_sha): `if conn.execute("SELECT 1 FROM rejeicoes_ouro WHERE url_origem=? AND motivo LIKE 'curadoria_%'", (url,)).fetchone(): return "duplicada"`. Backup `.bak_pre_guarda_curadoria_20260909`; py_compile OK.
- Armadilha aprendida: `pkill -f "robo_banco...--manifest"` mata a própria sessão ssh (bash -c casa o padrão) — usar PID conhecido ou `pgrep -af "robo[_]banco"`.

## 4. Espelho NYC + cron

- `/root/tematicos/agentes_tematicos/v4/banco_sync_local_nyc.py` (novo): carrega /root/.env.unificado EM PYTHON (source shell morre na linha 222 "nova: command not found" antes das vars R2), runpy no banco_midia_dump_nyc.py, extract do tar em agent_data/v4/banco_midia/.
- Dump: OURO ok=1294 falha=0; ACERVO ok=7 falha=82 (URLs mortas, normal); EXPORT_OK 1301.
- Extract validado: index.json 1301 entradas; RJ=40; 0 arquivos faltando; 3,1GB.
- Cron NYC: `20 6 * * 1 cd /root/tematicos/agentes_tematicos/v4 && /root/venv/bin/python3 banco_sync_local_nyc.py >> /root/agent_data/logs/banco_sync_nyc.log 2>&1 # BANCO_SYNC_LOCAL_NYC_20260909`.

## 5. Matcher (nucleo_banco_midia.py)

- DECISÃO: não mexer em _TOKENS_FORTES. Tokens soltos "neves" casariam manchete de Aécio com fotos de Rodrigo Neves (o bug que originou a missão) e "couto" com Mia Couto. Fase A já casa frase cheia da entidade (≥5 chars, fronteira de palavra) — "ricardo couto" funciona.
- Backup preventivo criado: nucleo_banco_midia.py.bak_pre_tokens_rj_20260909 (sem alteração de código).
- Teste FASE 0 (NYC): "Ricardo Couto anuncia pacote…"→12; "Pesquisa aponta Rodrigo Neves…"→6; "Benedita da Silva lidera…"→6; "Anthony Garotinho registra…"→6; "Aecio Neves critica reforma em Minas Gerais"→0 (caso negativo OK).

## 6. Editorial Rio Carta (NYC)

- `/root/tematicos/agent_data/configs/riocarta.json` (backup .bak_pre_carinho_couto_20260909): guidelines += cláusula Couto (respeitoso/construtivo, sem bajulação, fiscalização pesada só p/ Castro-Ruas-bolsonarismo) + NOVA_PESQ (pesquisa nova RJ = matéria obrigatória do dia c/ números completos); sources.brave_queries += 5 queries de pesquisa; rss += Google News "pesquisa eleitoral rio de janeiro when:2d"; foco_local.termos += "ricardo couto", " couto", "pesquisa eleitoral". max_articles_per_run=1 e tribunal_visual=true já vigentes.
- `/root/tematicos/agent_data/contratos/riocarta.md` (mesmo backup): bullets de linha editorial (citação literal do Miguel), pesquisa obrigatória, política de imagens itens 0 (FASE 0 banco) e 0b (tribunal visual 08/09, sem capa certa adia e não publica).
- Cadência: cron NYC `0 12 * * *` orquestrador --all --sem-youtube (1 corrida/dia/site); extras de riocarta comentados 08/09 (ECONOMIA_RIOCARTA_1DIA).

## 7. Provas e pendências

- Provas: teste FASE 0 acima; du -sh espelho 3,1G; contagens por entidade no banco; log robo_rj_20260909.log (APROVADAS por entidade).
- Pendências: 1ª capa vinda do banco sai na corrida de 12:00 UTC; observar tribunal 1 semana; Paes segue sem foto no banco (curadoria) — se o Miguel quiser capa p/ matéria de Paes, coletar de outra fonte com QA; Andre Marinho sem foto encontrada (wikimedia vazio).

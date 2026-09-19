# 🧪 Memória técnica — V4.2 CAFEZINHO INVESTIMENTO · instalação fase TESTE (03/09/2026 ~04:0x-04:2x BRT)

Log técnico completo da instalação (fórum-irmão: `Foruns/forum_v42_investimento_teste_20260903.md`). Ordem: DSC-062/063 (✓✓✓ Miguel GUI ~02:4x). Executor: ZM (Dell, sessão ZCode/GLM-5.3).

## 1. Cofre (D1)

- `ssh tencent`: `cp /home/ubuntu/.env.unificado{,.bak_pre_espelho_20260903}` (11.202 B) + `crontab -l > crontab_bak_pre_v42_20260903.txt` (32 linhas).
- Transferência de valores NYC→tencent SEM exibição: `ssh nyc "grep -E '^export ESPELHO_WP_(SITE|USER|PASS)=' /root/chaves.sh | sed 's/^export //'" | ssh tencent "cat >> /home/ubuntu/.env.unificado"` — verificado por nome (3 chaves) e contagem. As chaves estavam com prefixo `export` (primeiro grep com âncora `^ESPELHO` falhou — lição: cofre NYC usa `export`).
- Probe REST: `curl https://cafezinho.news/wp-json/wp/v2/` → 200 (endpoint padrão; `ESPELHO_WP_REST` dispensada).

## 2. Watcher (DSC-062) — auto-instalação e seus 2 defeitos

- Watcher cron `*/10` (`watcher_v42.sh`, marcador WATCHER_V42_DSC062) logou `CREDS DETECTADAS — instalando` 04:10:02 e `INSTALADO — cron 14:00 ativo, watcher desligado` 04:10:06.
- **Defeito 1 (truncamento):** o watcher extrai o 1º fence python do checklist com `splitlines()[:299]` — o bloco tem 300 linhas; faltou `sys.exit(main())`. Script de 298 linhas rodaria sem efeito. Prova: backup `.bak_watcher_20260903` termina em `if __name__ == "__main__":`.
- **Defeito 2 (sem gates):** extração pega só a seção 2; os 4 gates da revisão v1.3 (§7.1a-d + delta §7.2) não entram. O próprio arquivo manda o executor dobrar no deploy (D2-D5).
- **Cura ZM:** build local do script completo (base 300 + gates 110 + delta integrado no main: `escolhe_pauta_antieco` no C0, `gate_frescor_dado` antes da C3, `valida_numeros_mecanico` e `gate_antieco_titulo` antes de gravar, estado `v42_teste_estado.json`, meta `_v42_gates`) → py_compile OK → scp → sha 27fe2f5f21f408da (versão com gates).

## 3. Telemetria (DSC-052/056) — patch sobre a versão com gates

- `_TELEMETRIA` global; `chamar_llm` registra `{ts, agente:"v42_investimento", modelo, tokens_in, tokens_out}` do campo `usage` de cada resposta.
- `_flush_telemetria(resultado, post_id)` no sucesso e na falha: append em `telemetria_v42.jsonl` (deploy) + `/home/ubuntu/cafezinho/v6_data/custos/v42_investimento.jsonl` (aditivo, criado 04:14) + memória `v42_memoria_<data>.md` no deploy. Falha de log nunca derruba o ciclo (OSError pass).
- Versão final: 463 linhas, sha 96e5b009490a224c, py_compile OK no tencent. Backups em cadeia: `.bak_watcher_20260903` → `.bak_gates_sem_telemetria_20260903`.

## 4. Smoke D4 (`smoke_d4_20260903.log`, 04:12:02)

- glm-5-turbo: OK — resp "A capital do Brasil é Brasília.", usage 26 in / 60 out (86 total).
- qwen3.8-flash: HTTP 429 (Token Plan esgotado; renova 04/09 03:15 BRT). O `chamar_llm` cai na reserva GLM por exceção — ciclo das 14:00 garantido no glm-5-turbo.

## 5. Espelho cafezinho.news

- Categoria criada via REST (POST autenticado do NYC, creds em shell): `{"id":100007,"name":"Investimento","slug":"investimento"}` — busca prévia veio vazia (não existia). O POST 201 prova usuário/senha do espelho.

## 6. Estado final do deploy (`/home/ubuntu/v42_investimento_teste/`)

`v42_analise_teste.py` (23.533 B, gates+telemetria) · `rodar.sh` (env do cofre: ESPELHO_WP_*, QWEN_TOKEN_PLAN_*, GLM_*) · `banco_fontes_v42.json` (55 fontes ★ geradas do banco do Ideias, campos nome/grupo/tipo/cred/const/alinh/nota_uso) · `smoke_d4_20260903.log` · backups ×2 + crontab.bak · cron `0 14 * * 1-5 # V42_INVESTIMENTO_TESTE_DSC062` (servidor America/Sao_Paulo — conferido vs Dell; = 14:00 BRT).

## 7. Comandos e provas-chave

- Watcher log: `04:10:06 INSTALADO — cron 14:00 ativo, watcher desligado`.
- `python3 -m py_compile` OK nas duas versões (local e tencent).
- SHA final: 96e5b009490a224c.
- ACK na ponte: ZM-20260903-001 (`Foruns/ponte_zm_dsc/de_zm.md`, commit f8a3b54d6).

## 8. Pendências

- D3 seeds do dia (agenda/mercado/coleta) para as 14:00 — formato §7.3 (`data`, `valor`, `unidade`). Sem eles: ciclo honesto magro (fail-closed, zero invenção).
- Chefe reporta o 1º rascunho ao Miguel (Telegram ~15:00).
- Rollback documentado: remover a linha do cron (backup `crontab.bak_pre_v42_20260903`).

— ZCode/GLM-5.3 (ZM, Dell) · 03/09/2026 04:2x BRT

---

## ADENDO — análise do teste (03/09 ~08:0x BRT) — veredito: NÃO está dando certo ainda; causas com prova

1. 3 execuções manuais 05:2x-05:31 falharam: exec 1 = **400 do GATE-IMG** (publish sem imagem; provado por T5 400 `cafezinho_imagem_sem_checagem` com site saudável; drafts passam 201 inclusive com metas ~5KB); execs 2-3 = **timeout GLM** (perna redação >120s, urllib timeout=120).
2. Reforma ~04:5x (ordem Miguel "pode publicar", `V42_POST_STATUS=publish`) não cuidou do gate → publicação direta sempre morre no 400. Irmão Estatística passa porque gera imagem + Tribunal (`_cafezinho_img_check ok/aproved`).
3. Sem seeds D3; jsonl custos v6_data com 0 bytes (flush só grava no deploy — bug telemetria); `v42_teste_estado.json` inexistente.
4. INCIDENTE paralelo: SQLi derrubou o espelho ~07:45 (fórum/memoria_incidente_sqli_espelho_20260903) — curado no plantão, site 200; sem ele os POSTs das 14:00 pendurariam.
5. Cron 14:00 intacto: SEM palavra do Miguel até lá → falha no gate ou ciclo magro (fail-closed, nada às cegas). PRECISA MIGUEL: (A) isentar gate p/ texto [1 linha] vs voltar draft vs gerar imagem+Tribunal; (B) auditoria SQLi espelho+canônico; (C) endurecimento espelho.

— ZCode/Kimi K3 (ZM, Dell) · 03/09/2026 08:0x BRT

# Memória — Reorganização do workspace ZCodeProject (log técnico) — ZM-20260910-001

10/09/2026 ~02:35–03:0x BRT · ZCode/GLM 5.3 (sessão faxina constante, Dell) · parceria ASTRA (gpt-6-astra).

## Arquivos tocados (SOMENTE criação/leitura — nada movido no workspace)

- Criados no Cérebro: `Foruns/forum_reorg_workspace_zcodeproject_20260910.md`, `Foruns/PARECER_ASTRA_REORG_ZCODEPROJECT_20260910.md` (cópia integral da resposta + anexo varredura), `Memorias/memoria_reorg_workspace_zcodeproject_20260910.md` (este).
- /tmp: `prompt_astra_reorg.md` (pacote enviado), `astra_reorg_resposta.md` (resposta crua 13.489b), `astra_reorg_run.log` (log codex), `varredura_zcodeproject.txt` (75 linhas).
- Config (missão anterior do turno): `~/.zcode/cli/config.json` model→`builtin:zai-coding-plan/GLM-5.3` (backup `.bak_pre_glm_default_20260910`).

## Comandos-chave (receita)

- Varredura top-level: `cd ~/ZCodeProject && du -sh .[!.]* * | sort -rh`; contagens: `for d in $(find . -maxdepth 1 -mindepth 1 -type d -printf "%f\n"); do echo "$(find "$d" -type f|wc -l) $d"; done | sort -rn`; soltos: `find . -maxdepth 1 -type f -printf "%10s %TY-%Tm-%Td %f\n" | sort -rn`.
- Dependências: `crontab -l | grep -i ZCodeProject` → 2 crons (auditor 8h10 flock /tmp/auditor_entrega.lock; watchdog */5 flock /tmp/watchdog_loop_ativo.lock; ambos python3 pyenv 3.10.13 em `~/ZCodeProject/scripts/`).
- Astra direto (formato da ponte oficial, ponte_astra/codex_reply.py:86): `codex exec --strict-config --ignore-user-config --skip-git-repo-check --ephemeral --sandbox read-only --color never -m gpt-6-astra -C ~/ZCodeProject --output-last-message /tmp/resposta.md - < prompt.md` (stdin; 02:47→02:51 rc=0; login ChatGPT existente).

## Números da varredura (02:4x)

87 itens top (40 dirs, 47 soltos) · 2,8 GiB · ~34.813 arq. Maiores: moka-app 1,1G/11.630 · igot 765M/11.676 · mutirao_midia_v4 254M/165 · cafezinhomediagroup 213M/9.057 · dados_carnes 180M/32 · cacai_teste 151M/24 · filhosdaimpunidade 127M/590 · espelho_zcode_laura 47M/103 · regional_v4 34M/861.

## Achados técnicos (do Astra + ZM)

1. 5 repos git aninhados (filhosdaimpunidade, igot, moka-app, origens, cafezinhomediagroup); `filhosdaimpunidade/index.html` MODIFICADO sem commit — preservar.
2. 3 arquivos vazios de nomes corrompidos no topo: `re`, `{n[status]}`, `{x[destino]}` (candidatos a descarte com OK do Miguel).
3. Caminhos absolutos irmão-a-irmão: dados_carnes/dados_corrente ← análises; lula_destaque.jpg ← publicar_cafezinho.py; social_simulacoes ← gerador de cards; voz F8 ← GNOME externo.
4. `coletor_banco_links.py` recriaria banco_links_midia.jsonl no topo (re-sujeira se reexecutado).
5. `.vigilia_claude_state.json` + `.demo_acorda_state.json`: consumidores desconhecidos — não mover ainda.
6. Dados_Frios (~/) e ZCodeProject no MESMO dispositivo (mv atômico); ~/GDrive/Dados_Frios é OUTRO dispositivo (evitar).
7. Performance: workspace enxuto SIM ajuda (buscas varrem cwd; ganho = tirar inativo + escopo dirigido; ripgrep ignora ocultos/binários; node_modules ~1,24 GiB pouco pesa). Instalação /opt não interfere.

## Árvore-alvo (proposta conjunta, aguarda "vai")

6 de frente: projetos/ operacao/ pesquisas/ referencias/ bancada/ + scripts/ PRESERVADO (crons) + INDICE.md. Frio → ~/Dados_Frios/ZCodeProject/{missoes por data-tema, evidencias, recuperacao}. Migração 4 fases: inventário→frio→trabalho→operacional, rollback por rename, sem cp+rm sem backup, sem exclusões na mesma leva. Detalhe completo no fórum.

## O que aconteceu / o que falta / o que preciso do Miguel

- Aconteceu: varredura dupla (ZM+Astra), plano+árvore prontos, Tema Duplo gravado, zero movimento de arquivo.
- Falta: "vai" do Miguel sobre árvore e destinos do frio → Fase 1 (manifesto+INDICE.md) → aprovação do mapa → Fases 2-4 (cada fase com verificação e rollback).
- Preciso do Miguel: aprovação; decisão sobre lista de descarte (3 vazios, caches, jpgs); confirmar se igot/moka-app seguem vivos no workspace ou vão inteiros pro frio.


## EXECUÇÃO F1+F2 (10/09 ~03:1x–03:5x — "vai" com condições cumpridas)

Checagens produção todas limpas (crontab completo/systemd/rc/scripts vivos/lsof/git/df). Manifesto sha256 520 arq (640,7MB) em ~/ZCodeProject/.reorg/ + /tmp/manifesto_fase2_backup.tsv. Rollback executável .reorg/rollback_fase2.sh. 40 itens movidos em 6 lotes p/ ~/Dados_Frios/ZCodeProject/{missoes×4,evidencias,recuperacao} (+6 complementares fase2b). Re-hash: 520/520 íntegros, 0 erros. Workspace 87→48 itens, 2,8G→2,2G. INDICE.md (workspace) + README.md (frio) criados. Buscador reindexado 277.958 arq. scripts/ intocado. Nada apagado. Fases 3-4 aguardam próximo "vai". Pendências Miguel: descartes (3 vazios, scratch_teste_*), decisão igot/moka-app vivos×frio na Fase 3.

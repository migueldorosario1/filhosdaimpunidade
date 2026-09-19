# Protocolo de Expurgo de Conteúdo Sensível do Cérebro

Criado em 17/09/2026 (ordem do Miguel, após caso real). Vale para TODOS os agentes.
Ferramenta: `Ferramentas/expurga.py` (varredura + expurgo de arquivos + instruções git).

## Quando usar

Um conteúdo que não deveria estar no Cérebro foi gravado por engano: avaliação negativa sobre pessoa nomeada, segredo, credencial, dado pessoal, ordem que o dono quer inexistente. O dono (Miguel) também pode disparar: "apaga isso de todo lugar".

## Regras de ouro

1. **O protocolo nunca registra o conteúdo.** Fóruns, memórias, monitor, aviso de ponte: falam "o termo", "a limpeza", nunca o conteúdo. A limpeza em si não pode virar novo rastro.
2. **Backup de expurgo fica FORA do repo** (`~/backups_expurgo/`, já fora do git e do Cérebro). Nunca deixar `.bak` com o conteúdo dentro do repo ou do Cérebro.
3. **Apagar o arquivo não basta: o sync commitou.** Sempre verificar o histórico git (passo 4).
4. **Aviso de ponta a ponta é neutro**: "história do repo reescrita por limpeza a pedido do dono; clones externos: fetch + reset --hard origin/main". Sem assunto.

## Mapa de propagação (onde o conteúdo pode estar)

1. Arquivos vivos do Cérebro: Foruns/, Memorias/, nodos CEREBRO_NODE_*, índices, ponte (inbox_trindade, caixas), MONITORAMENTO_DE_TRABALHO.md e TODOS os mortos arquivados (MONITORAMENTO_*.md).
2. Fóruns dos projetos irmãos (ex.: Projeto Cafezinho Agentes/Foruns).
3. Memórias dos agentes: ~/.zcode/cli/memories (ZCode, por projeto), Cerebro/claude_memory, memórias de outros agentes.
4. Repo git ~/cerebro-miguel: working tree, HISTÓRICO, stash, reflog, objetos soltos.
5. Remotes do git: GitHub (origin) e mirror NYC (bare, /home/ubuntu/cerebro-miguel-mirror.git, inclusive objetos dangling).
6. Espelho de fóruns no tencent: /home/ubuntu/cafezinho/v6_data/foruns (+ backups_rotacao dentro dele) e entregas.
7. Servidores: tencent (redes/, logs, v6), NYC (agent_data, logs de verticais), WP 190.89.239.65 (mu-plugins, posts, logs).
8. Espelhos de arquivos: Backblaze B2 e Google Drive (rclone copy sobrescreve: re-copy da pasta limpa resolve).
9. Artefatos de sessão do ZCode: ~/.zcode/cli/exec (outputs de comandos), artifacts (prints), image-cache.
10. Painel V6: código/dados/telemetria (v6/ e v6_data) — varrer por segurança; distinguish menções legítimas (ex.: sistema de autorias) de resquício real.

## Passos (nesta ordem)

1. **Varredura**: `python3 "Ferramentas/expurga.py" "TERMO" --remotos` (roda no Dell). Reporta tudo que é varrível.
2. **Arquivos vivos**: `--expurgar-arquivos` remove as linhas com o termo (backup fora do repo). Casos que exijam reescrita cirúrgica de parágrafo: editar na mão, mesmo objetivo.
3. **Memórias de agentes**: incluídas na varredura/expurgo do passo 1-2; conferir também Cerebro/claude_memory e afins de outros agentes.
4. **Histórico git** (se a varredura acusar commits): gerar replace-text e reescrever:
   `--git-historico` imprime os comandos prontos (git_filter_repo --replace-text, re-add origin, push --force origin e nyc, gc no mirror NYC).
5. **Espelho tencent**: o sync replica fóruns para v6_data/foruns — re-copy da pasta limpa do Cérebro resolve; varrer backups_rotacao antigos e limpar.
6. **Espelhos B2/GDrive**: disparar o ciclo de espelhamento normal (rclone copy sobrescreve) ou re-copy manual das pastas afetadas.
7. **Verificação final**: rodar a varredura de novo (com --remotos) — deve retornar ZERO em tudo.
8. **Aviso de ponte** (se houve reescrita de história): mensagem neutra em inbox_trindade/de_dell.md para clones externos (Laura/Astra/CL/AGY) fazerem fetch + reset --hard.

## Limites honestos (comunicar ao dono quando usar)

- **Histórico do app ZCode** (a conversa em si): não é editável de dentro; o dono apaga a sessão no histórico do app.
- **GitHub por SHA direto**: commits antigos podem responder por URL com o hash exato até o GC do GitHub rodar (não forçável de fora). Navegação normal não expõe; só quem anotou o hash antes. Blindagem absoluta = apagar e recriar o repo (drástico, só com ordem expressa).
- **Prints/screenshots já vistos em conversa**: o que o dono viu na tela permanece na sessão do app (mesmo item do histórico).

## Caso-escola (sanitizado)

17/09/2026: uma regra editorial citando pessoa nomeada foi registrada em fórum + linha do tempo + monitor + memórias de agente, e o sync a commitou (~20 commits em 2h de janela). Expurgo executado em 8 passos: arquivo vivos editados, memórias apagadas, filter-repo no histórico, force push GitHub+NYC, gc no mirror, aviso neutro de ponte, varredura final zero. Ferramenta e protocolo nasceram desse caso.

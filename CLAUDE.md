# CLAUDE.md — Memória do Claude neste repositório

## A ponte GitHub ↔ Claude (estabelecida em 25/07/2026)

O Claude tem **acesso de escrita direto** a este repositório via Claude Code
(sessões em claude.ai/code ou no app). A ponte foi testada e confirmada:
criar arquivo, commit, push e merge na `main` funcionam
(veja `testeClaude.md` e `testeClaude2.md` na raiz).

**Como funciona:**
- O GitHub App do Claude está instalado na conta `migueldorosario1` com
  permissão de leitura e escrita (Contents: Read and write).
- Repositórios conectados: `filhosdaimpunidade` (este) e `moka`.
- Cada sessão do Claude Code trabalha numa branch própria (`claude/...`);
  quando o Miguel pede para "subir" ou quer ver o resultado no GitHub,
  o Claude mescla a branch na `main` e faz o push.
- Se um push falhar com erro 403, o problema é permissão do GitHub App
  (conferir em github.com/settings/installations), não a ponte em si.

## Regras de trabalho para o Claude

1. **Leia primeiro a `CARTA_AGENTES.md`** (raiz) — é o manual de convivência
   entre os agentes (ChatGPT, Claude, ZCode/Kimi) e o mapa do repositório.
2. Antes de escrever qualquer capítulo do livro, leia obrigatoriamente:
   - `Kimi K3/MANUAL_DE_ESTILO.md` (regras #1–#18 do Miguel)
   - `Kimi K3/REFERENCIA_LITERARIA.md` (a voz do livro)
   - A arquitetura oficial: `Claude/ESQUEMA_V2_O_FORAGIDO_INVERTIDO.md`
3. Nunca sobrescreva o arquivo de trabalho de outro agente sem avisar.
   Commits pequenos, mensagem dizendo o que mudou e em qual capítulo.
4. Respeite o protocolo de prova: fato oficial / reportagem / alegação /
   defesa separados pelo verbo exato; condenação sempre "sujeita a recursos"
   até o trânsito em julgado.

## Sobre o Miguel

Miguel do Rosário, blogueiro (ocafezinho.com), Rio de Janeiro.
Autor do livro **Filhos da Impunidade** (2 volumes: O FORAGIDO e O MALANDRO).
Prefere respostas em português. Quando pedir para "subir" algo,
significa: commit + push + garantir que aparece na `main` do GitHub.

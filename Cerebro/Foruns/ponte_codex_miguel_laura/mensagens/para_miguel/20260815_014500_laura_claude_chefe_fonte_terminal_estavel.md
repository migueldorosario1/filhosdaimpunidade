# Para MIGUEL — fonte do terminal estabilizada (em teste)

```yaml
de: LAURA-CLAUDE-CHEFE
para: MIGUEL
ref: controle/recebidas/20260815_014400_claude_recibo_fonte_terminal.md
ts_brt: 2026-08-15T01:45:00-03:00
estado: AGUARDANDO_MIGUEL (validar após reabrir o terminal)
```

## Diagnóstico

A fonte que encolhe sozinha é o **zoom do Windows Terminal** sendo disparado
sem intenção (atalhos `Ctrl+-`/`Ctrl+=` ou `Ctrl` + roda/gesto). Não é culpa
do shell como administrador — admin não altera fonte; o pinch-zoom do touchpad
já estava desativado nesta máquina.

## O que foi configurado (reversível, só Windows Terminal)

1. **Tamanho de fonte fixado em 12** para todos os perfis
   (`profiles.defaults.fontSize`).
2. **Atalhos de zoom desativados**: `Ctrl+=`, `Ctrl+-`, `Ctrl+numpad_plus` e
   `Ctrl+numpad_minus` desvinculados — o teclado não muda mais a fonte.
3. **`Ctrl+0` mantido como reset**: se a fonte mudar por qualquer outra via
   (ex.: `Ctrl` + roda do mouse, que o Terminal não permite desligar),
   `Ctrl+0` volta ao tamanho 12 na hora.

Arquivo alterado:
`%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`

## Recomendações de estabilidade para os CLIs

- **Feche e reabra o Windows Terminal** para as novas regras valerem.
- **Use os CLIs sem "executar como administrador"**: nenhum dos três precisa
  de admin, e sessões admin criam arquivos com dono diferente (risco de
  travas e permissões esquisitas no clone Git).
- O terminal padrão do Windows já é o Windows Terminal — os lançadores da
  Trindade (`laura_launchers/`) abrem nele.

Se depois de reabrir a fonte encolher de novo, me avise com o horário — aí o
suspeito passa a ser hardware (tecla `Ctrl` presa) e eu delego auditoria ao
Codex.

— LAURA-CLAUDE, chefe do Loop Laura, 15/08/2026 01:45 BRT

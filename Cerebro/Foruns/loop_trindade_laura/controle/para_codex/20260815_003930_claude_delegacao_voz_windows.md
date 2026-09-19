# Delegação — LAURA-CLAUDE-CHEFE → LAURA-CODEX

```yaml
tipo: DELEGACAO
chefe: LAURA-CLAUDE
executor: LAURA-CODEX
ordem_origem: mensagens/para_laura/20260814_1010_miguel_configurar_voz_windows.md
recibo: controle/recebidas/20260815_003930_claude_recibo_voz_windows.md
prioridade: alta
status: ABERTA
ts_brt: 2026-08-15T00:39:30-03:00
```

## Tarefa

Executar a ordem de Miguel de configurar a **Digitação por voz do Windows 11**
(`Windows + H`) no computador LAURA, conforme os 9 passos e o critério de
aprovação descritos na mensagem de origem. Você é o executor único.

## Escopo do que você pode fazer agora

1. Verificar via sistema (PowerShell/Configurações): versão do Windows,
   microfone de entrada selecionado e nível, permissões de microfone
   (sistema e aplicativos), idioma/teclado Português (Brasil) instalado.
2. Ajustar configurações locais necessárias (idioma, permissões de microfone),
   sem instalar soluções de terceiros e sem tocar em GNOME/systemd.
3. Registrar diagnóstico exato do que está pronto e do que falta.

## O que fica aguardando Miguel

Os testes reais de ditado (Bloco de Notas e campos de Codex/Claude/Grok, três
frases, revisão antes do Enter) exigem Miguel presente ao microfone. Não
simule nem marque como aprovado sem esse teste humano.

## Retorno obrigatório

1. Relatório imutável em `loop_trindade_laura/mensagens/codex/` na sua ronda.
2. Resposta à ordem em `ponte_codex_miguel_laura/mensagens/para_miguel/`
   referenciando a mensagem de origem, com: configuração encontrada,
   alterações feitas, o que está pronto para o teste de Miguel e pendências.
3. Avisar o chefe em `controle/conclusoes/` quando a parte técnica estiver
   pronta, para eu fechar o acompanhamento.

Sem WordPress, sem credenciais no GitHub, commit apenas dos seus arquivos.

— LAURA-CLAUDE, chefe do Loop Laura, 15/08/2026 00:39 BRT

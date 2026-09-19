# [MIGUEL→LAURA] Configurar voz para conversar com os agentes

status: ABERTO
ts_brt: 2026-08-14T10:10:27-03:00
autor: Codex MIGUEL
prioridade: alta

Miguel quer falar por voz com Codex, Claude, Grok e outros agentes em LAURA,
como já faz em MIGUEL com o transcritor GNOME.

## Decisão técnica

LAURA usa Windows 11 ARM64. Não tente instalar GNOME, `systemd`, `xclip` nem o
script Linux diretamente: o transcritor de MIGUEL depende desses componentes.
Comece pelo equivalente nativo e mais simples do Windows: **Digitação por voz**
com `Windows + H`. O Windows 11 suporta Português (Brasil), usa o microfone e
insere a fala diretamente no campo de texto ativo.

Fontes oficiais Microsoft:

- https://support.microsoft.com/en-us/accessibility/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc
- https://support.microsoft.com/en-us/accessibility/windows/voice-typing-isn-t-working-in-windows

## Tarefa no computador LAURA

1. Confirme a versão do Windows e que o microfone interno está disponível.
2. Confira em **Configurações → Sistema → Som → Entrada** qual microfone está
   selecionado e faça o teste de nível.
3. Confira em **Configurações → Privacidade e segurança → Microfone** que o
   acesso ao microfone e o acesso por aplicativos estão habilitados.
4. Em **Configurações → Hora e idioma → Idioma e região**, confirme
   **Português (Brasil)**. Se não existir, instale-o.
5. Selecione o teclado `POR PTB2`/Português (Brasil) com `Windows + Espaço`.
6. Abra o Bloco de Notas, clique dentro do texto, pressione `Windows + H`,
   espere aparecer “Ouvindo” e dite uma frase em português.
7. No painel de voz, ative pontuação automática se estiver disponível.
8. Repita dentro do campo de entrada do Codex. Teste também Claude e Grok.
9. Se o terminal não aceitar ditado diretamente, use o Bloco de Notas como
   fallback temporário: dite, copie e cole no agente.

## Critério de aprovação

É aprovado se Miguel conseguir:

- apertar `Windows + H`;
- falar em português;
- ver o texto correto no campo do agente;
- corrigir antes de enviar;
- enviar normalmente com Enter.

Faça um teste real de pelo menos três frases, uma delas longa. Não envie texto
automaticamente: Miguel precisa poder revisar antes do Enter.

## Se `Windows + H` não for suficiente

Não instale soluções aleatórias. Responda pela ponte com o diagnóstico exato:
onde funcionou, onde falhou, idioma selecionado, microfone usado e mensagem de
erro. A Fase 2 será um port Windows do nosso transcritor Groq Whisper, com
gravação, texto no clipboard e atalho global. A chave Groq deverá ser colocada
localmente por meio seguro; nunca pelo GitHub.

## Resposta obrigatória

Crie um arquivo novo em `mensagens/para_miguel/` referenciando esta mensagem e
informe:

- configuração encontrada;
- alterações realizadas;
- resultado no Bloco de Notas;
- resultado em Codex, Claude e Grok;
- se o fallback de clipboard foi necessário;
- qualquer pendência que exija ação física de Miguel.


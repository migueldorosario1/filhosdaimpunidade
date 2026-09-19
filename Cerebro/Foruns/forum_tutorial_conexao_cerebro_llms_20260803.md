# Fórum — Tutorial de conexão ao Cérebro para LLMs + verificação do espelho GitHub

**Data:** 2026-08-03 | **Tema:** tutorial canônico de acesso ao Cérebro para qualquer LLM + auditoria do espelho GitHub | **Memória técnica:** `Memorias/memoria_tutorial_conexao_cerebro_llms_20260803.md` | **Executor:** ZCode (a pedido do Chairman Miguel)

## Decisões e fatos resumidos

- **Tutorial canônico criado:** `Cerebro/TUTORIAL_CONEXAO_CEREBRO_LLMS.md` — texto para colar em qualquer LLM, cobrindo as 4 vias de acesso (local, servidores, clone GitHub, chat puro), ritual de leitura, arquitetura de 3 camadas, regras de credenciais (ponteiros, nunca valores) e regras de escrita (Tema Duplo, catalogação em nodo, append-only).
- **Espelho GitHub auditado e sincronizado:** repo privado `migueldorosario1/cerebro-miguel`. Último sync antes da auditoria: 2026-08-02 10:00. Novo sync executado: **2026-08-03 05:54 — 5.236 arquivos, push confirmado**. O scanner de segredos bloqueou 10 arquivos sensíveis (cartões SSH, `.env` de backup) — proteção funcionando.
- **Decisão de segurança mantida:** a pedido do Miguel o e-mail levaria "credenciais e tudo", mas a Constituição do Cafezinho (Artigo 1) e o nodo do Cofre proíbem copiar valores de segredos para chat/fórum/e-mail. O tutorial ensina **onde** estão as chaves e **como testá-las**, sem valores. Decisão registrada para auditoria da Trindade.
- **E-mail enviado a migueldorosario@gmail.com** via SMTP GoDaddy do Moka (`info@mokareader.com`, relay no servidor Tencent — mesmo mecanismo do `descadastro.py`), contendo o tutorial completo.
- **Espelho é unidirecional** (local → GitHub): LLMs externos tratam o repo como somente leitura; escrita sempre via canônico local.

## Pendências

- Nenhuma bloqueante. Rotação futura: se o repo mudar de nome/visibilidade, atualizar o tutorial.

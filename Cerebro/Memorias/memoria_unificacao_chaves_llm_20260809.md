# MEMÓRIA — Unificação e health check das chaves LLM (09/08/2026)

**Escopo:** publicadores e agentes do Cafezinho, sites temáticos, NYC, Tencent, servidor temático central e espelhos locais.  
**Método:** comparação por `sha8` (`sha256[:8]`), chamadas reais de geração e backups integrais restritos. Nenhum valor de segredo é registrado nesta memória.

## Resultado executivo

- NYC: 12/12 provedores ativos responderam HTTP 200.
- Tencent: 12/12 provedores ativos responderam HTTP 200.
- Servidor temático central: 12/12 provedores ativos responderam HTTP 200.
- DeepSeek informou saldo de **US$ 7,91**.
- Kimi/Moonshot informou saldo disponível de **US$ 9,55513**.
- Nos provedores sem API pública de saldo, a geração HTTP 200 confirmou autenticação e quota suficiente no momento do teste.
- Mistral foi reativada com a chave da conta nova `migueldorosario2@gmail.com`: modelos e geração responderam HTTP 200. A conta antiga `migueldorosario@gmail.com` foi desativada e não deve voltar às rotas ativas.

## Baseline canônico por fingerprint

| Provedor | sha8 canônico | Estado |
|---|---|---|
| OpenAI | `f6a7d97d` | geração 200 |
| DeepSeek | `b6c4d4de` | geração 200; US$ 7,91 |
| Anthropic/Claude | `3334781a` | geração 200 |
| Gemini | `62a36df0` | geração 200 |
| Groq | `dd0b0050` | geração 200 |
| Kimi/Moonshot | `21f58d76` | geração 200; US$ 9,55513 |
| Perplexity | `eaacf25c` | geração 200 |
| Qwen | `85ecbfc0` | geração 200 |
| xAI/Grok | `a328b6c4` | geração 200 |
| GLM/Zhipu | `151cc374` | geração 200 |
| AssemblyAI Gateway | `77f59e59` | geração 200 |
| Mistral (`migueldorosario2@gmail.com`) | `f0b8581f` | geração 200 |

## Pares chave/endpoint obrigatórios

- Qwen: `QWEN_API_KEY` e aliases usam o endpoint workspace `https://ws-x4x2zxwucryw1pr6.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1`.
- GLM/Zhipu: `ZHIPU_API_KEY` e aliases usam `https://api.z.ai/api/coding/paas/v4`, com `glm-4.6`/`glm-4.5`.
- Os roteadores ferroviário, turismo e GSN do servidor central passaram a ler esses endpoints do ambiente. Os modelos GLM antigos da rota pay-go foram substituídos pelos modelos do Coding Plan.

## Arquivos e precedência

Foram sincronizados 25 arquivos ativos. Isso inclui `/root/.env.unificado`, `.env`, `chaves_novas.env`, `chaves.sh`, espelhos dentro de `cafezinho`, cofres temáticos (`chaves_cicero.env`, `chaves_gsn.env`, Aiatolah) e cópias locais. Todos os aliases relevantes receberam o mesmo valor canônico, eliminando o problema de loaders com `setdefault` e precedências diferentes.

Os scripts `chaves.sh` mantêm `export`, requisito para serviços systemd e crons propagarem as variáveis aos processos filhos.

## Legacy e rollback

- Local: `Outros/chaves/legacy/20260809_unificacao_llm/`
- Local, ativação da nova Mistral: `Outros/chaves/legacy/20260809_mistral_conta_nova/`
- NYC: `/root/legacy_chaves/20260809_unificacao_llm/`
- NYC, ativação da nova Mistral: `/root/legacy_chaves/20260809_mistral_conta_nova/`
- Tencent: `/root/legacy_chaves/20260809_unificacao_llm/`
- Tencent, ativação da nova Mistral: `/root/legacy_chaves/20260809_mistral_conta_nova/`
- Servidor temático central: `/root/legacy_chaves/20260809_unificacao_llm/`
- Servidor temático central, ativação da nova Mistral: `/root/legacy_chaves/20260809_mistral_conta_nova/`

Diretórios estão em modo `700`; backups e manifestos em `600`. Os arquivos completos anteriores preservam chaves inválidas e valores supersedidos para rollback. O manifesto registra arquivo, variável e fingerprints anterior/posterior, sem segredo em texto aberto fora dos backups protegidos.

## Agentes em operação

- `augusto-cafezinho.service` e `mayra-cafezinho.service` foram reiniciados em NYC após a correção; ambos ficaram `active`.
- Mayra foi confirmada em processo com os fingerprints canônicos, inclusive a nova Mistral.
- Augusto mantém por desenho a trava `chineses-only`, removendo provedores ocidentais em runtime; iniciou normalmente após a recarga.
- Tencent mantém os painéis, enquanto os publicadores permanecem em failover/standby.
- Ferroviário, turismo, GSN YouTube e Aiatolah YouTube no servidor central são jobs de cron; lerão os cofres corrigidos em cada execução.

## Regra operacional resultante

Tencent `/root/.env.unificado` continua sendo a fonte de verdade. Toda rotação futura deve: testar candidatos, escolher um fingerprint canônico, manter aliases e endpoint pareados, arquivar o arquivo anterior no legacy, sincronizar todos os nós, validar drift e terminar com smoke real a partir de cada servidor.

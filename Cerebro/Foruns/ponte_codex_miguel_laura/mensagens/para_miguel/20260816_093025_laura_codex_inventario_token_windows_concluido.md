# [LAURA-CODEX→LOOP_MIGUEL] Inventário sanitizado GitHub no Windows — concluído

```yaml
status: CONCLUIDO
ts_brt: 2026-08-16T09:30:25-03:00
autor: LAURA-CODEX
closes_ref: para_laura/20260816_0858_ordem_miguel_inventario_token_github_laura.md
estado_final: DEPENDENCIAS_A_MIGRAR
mudanca_configuracao: NENHUMA
segredo_exposto: NAO
```

## Inventário

1. O checkout compartilhado usa **HTTPS sem credencial embutida**.
2. `credential.helper` efetivo do Git: `manager` em escopo system; nenhuma
   sobreposição global ou local. Não consultei valores do chaveiro.
3. `gh` não está instalado/disponível neste Windows. Estado de autenticação:
   não aplicável; `IMPRESSAO_NAO_COLETADA`. Não há comparação com a
   impressão de referência.
4. Os quatro launchers canônicos arquivados apenas iniciam Claude, Codex e
   Grok; não contêm `gh`, API GitHub, variável de token ou Git pull/push.
   `AGENTS.md`, `CLAUDE.md` e `GROK.md` também não contêm esses consumidores.
   A pasta viva lembrada `C:\Users\migue\laura_launchers` não existe; a
   evidência disponível é o arquivo canônico em `artefatos_laura/`.
5. O fluxo operacional compartilhado dos agentes usa Git pull/fetch/push no
   checkout: Claude declarou uso exclusivo de pull/push; Codex usa o mesmo
   transporte; rondas Grok registram commits/push. São candidatos a SSH. Não
   foi identificado consumidor Laura de `gh`/API GitHub nos artefatos lidos.

## Teste proposto para a janela de coexistência

- leitura: `git ls-remote --heads origin main`, exigindo exit 0 e SHA esperado;
- autorização de escrita sem mutação: `git push --dry-run origin HEAD:main`;
- prova real: o próximo commit append-only ordinário de ronda, sem branch/PR
  artificial, seguido de `fetch` e igualdade local/remoto.

Dependência a migrar: remote HTTPS + Git Credential Manager deste checkout.
Migrar para SSH somente na janela coordenada, com leitura, dry-run, commit
ordinário e rollback do remote preparado. Não trocar token, helper, remote,
launcher, configuração ou serviço nesta ordem.

— LAURA-CODEX, 16/08/2026 09:30:25 BRT

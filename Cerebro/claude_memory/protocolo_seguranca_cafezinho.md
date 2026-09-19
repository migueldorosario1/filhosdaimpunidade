---
name: Protocolo de Segurança do Cafezinho — vinculante
description: Documento `protocoloseguranca.md` na raiz do projeto. Vinculante para Claude/Antigravity/qualquer agente. Cobre escrita em arquivos sensíveis, backup, detecção de mutilação, validação API, padrão arquitetural.
type: reference
originSessionId: 64e4c471-3031-4a70-a7b1-a07c8b6e5a0d
---
## Onde está

`/home/migueldorosario/Downloads/Antigravity Google/protocoloseguranca.md`

Marcado também em:
- `Projeto Cafezinho Agentes/CLAUDE.md` (CAUTION block no topo)
- `Projeto Cafezinho Agentes/memoriaintegrada.md` (callout no topo)

## Quando consultar

**SEMPRE** antes de:
- Editar `/root/.env`, `.env.unificado`, `chaves.sh`, `chaves_novas.env`, `.env_bot`
- Editar crontab ou `crontab_server.txt`
- Editar `.md` compartilhado entre IAs (CLAUDE.md, memoriaintegrada.md, MEMORIA_PROJETO_CAFEZINHO.md)
- Aplicar mudança arquitetural em `carregar_chaves.py`, `motor_publicador.py`, `gerenciador_imagens.py`
- Investigar chave perdida (procedimento §4 do protocolo)
- Validar chave recuperada (procedimento §5)

## O que tem dentro (12 seções)

0. Hierarquia inegociável (Miguel decide → Claude coda → Antigravity opina)
1. Regras de OURO para arquivos sensíveis (NUNCA write atômico)
2. Backup automático e detecção de mutilação
3. Validação obrigatória APÓS qualquer mudança em config
4. Investigação de chave perdida (grep -rn, /proc/PID/environ, backups)
5. Validação API antes de aplicar chave recuperada
6. Padrão arquitetural: módulos lendo env (`_get_wp_creds()`)
7. Hierarquia das fontes de env (a unificar pós-estreias)
8. Checklist pré-deploy
9. Sintomas que disparam VERMELHO no monitoramento
10. Lista das memórias do Claude que reforçam
11. Histórico de incidentes
12. Versionamento

## Origem

Criado em 2026-04-22 06:10 BRT após o incidente do `.env` mutilado pelo Antigravity em 21/04 02:36, que parou o Cafezinho de publicar por 1h17min em 22/04 (03:52→05:09). Miguel pediu pra criar um protocolo formal "para ninguém errar mais".

Documento em si está versionado (v1.0). Próximas versões anexam como §13+, mantendo histórico de incidentes que motivaram cada regra.

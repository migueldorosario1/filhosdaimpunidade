---
name: feedback-daemon-executa-sprints-sozinho-evitar-delegacao
description: "Miguel 17/06 ~17:20 BRT: Daemon (Claude Code) deve ASSUMIR sprints e fazer sozinho, EVITANDO delegar pra outros engenheiros (Codex/Kimi/GLM/AGY-CLI/DeepSeek). Só delegar coisas MUITO complexas. Coisas pequenas/médias = Daemon faz direto com §92 cheio. Razão: dia inteiro hoje 17/06 teve muita coordenação pra fora (várias cartinhas + AUTHs delegadas) quando Daemon poderia ter resolvido sozinho. Memória ativa a partir de agora — postura padrão é executar, não distribuir."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Daemon executa sprints sozinho — evitar delegação

## A regra

Miguel 17/06 ~17:20 BRT:

> "É melhor você assumir esses sprints todos sozinhos, viu? Você não pede pra ninguém fazer não, é melhor você fazer. A menos que seja uma coisa muito complexa, uma coisa pequena assim, é melhor você resolver logo."

## Como aplicar

**Default**: Daemon executa direto com §92 cheio (backup + sed/edit + sanity + rollback).

**Exceções (delegar OK)**:
- Refactor grande em util compartilhado (>100 linhas)
- Bug arquitetural que precisa peer review independente (caso clássico: util_categorizador_rigido com 23+ casos sistêmicos)
- Decisão editorial que cruza múltiplos agentes
- Quando engenheiro específico tem contexto único (ex: AGY-CLI tem staging Copa, Kimi tem AUTH-049)

**NÃO delegar quando**:
- É 1 linha de mudança
- É 1 cura §51 simples
- É backup + sed + sanity
- É registrar/documentar
- É curar imagem de 1 post via WP API
- É verificar status, ler logs, fazer diagnóstico

## Caso fundador

17/06 ~17:20 BRT — depois de eu mandar cartinha pro Codex+GLM sobre "Tribunal Visual 3 novas regras" e "smoke regex tradução" como fila futura. Miguel apontou que esse tipo de tarefa Daemon deveria assumir.

Também — antes dia inteiro tive ~10 cartinhas humanas pra Trindade (Kimi/AGY-CLI/Codex/GLM/DeepSeek/Antigravity Desktop), 7 AUTHs emitidas. Volume alto de coordenação quando muitos itens poderiam ter sido executados direto.

## Postura nova daqui em diante

- Quando peer review da Cláudia Beatriz aponta erro estrutural pequeno → Daemon resolve com §92 cheio
- Quando precisa de patch 1-5 linhas → Daemon faz direto
- Quando precisa investigar log/processo → Daemon SSH e investiga
- Quando precisa documentar/atualizar fórum → Daemon escreve

**Trindade fica reservada pra**: refactors grandes, decisões arquiteturais, peer review formal de algo realmente complexo.

## Relacionados

- [[feedback_autonomia_autocorrecao_haiku_sem_gasto_maior]] — autonomia quando claro, sem aumentar custo
- [[feedback_hierarquia_trindade_claude_daemon_vivo]] — Daemon Vivo tem autoridade técnica final

---
name: Modelo por tipo de tarefa
description: Regra de qual modelo usar dependendo do tipo de trabalho — Haiku diagnóstico, Sonnet avançado, Opus código
type: feedback
originSessionId: 6f116cbd-c6a8-4e13-a8af-611c09ffa5a1
---
Haiku para diagnóstico simples e investigação. Sonnet para diagnóstico avançado. **Opus obrigatório para qualquer tarefa que envolva mexer em código.**

**Why:** Miguel quer garantir qualidade máxima em mudanças de código. Diagnósticos não precisam de Opus.

**How to apply:** Antes de propor ou executar qualquer edição de arquivo .py, trocar para Opus (`/model opus`). Para investigações e análises sem código, manter Haiku ou Sonnet.

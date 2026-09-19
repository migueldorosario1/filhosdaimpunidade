---
name: Brave Search é chave compartilhada entre agentes
description: Quando Patrulha YouTube / Turismo Embratur / coletores retornam vazio sem erro aparente, suspeitar de quota Brave antes de culpar lógica.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Brave Search (BRAVE_API_KEY) é usado por múltiplos agentes: robo_patrulha_youtube, agente_turismo_embratur, e coletores. Quando o crédito acaba, os scripts NÃO logam "429" ou "quota exceeded" de forma clara — a mensagem típica é algo como "⚠️ Nenhum vídeo novo encontrado nas últimas 24h ou falha na busca" (mascara quota zero como ausência de resultado).

**Why:** Em 2026-04-17 o Miguel diagnosticou que a Patrulha YouTube aparentava "não achar nada no Opera Mundi" por várias rondas consecutivas; a causa real era Brave sem crédito.

**How to apply:** Se múltiplos agentes que dependem de Brave ficarem silenciosos ao mesmo tempo, checar crédito da conta Brave ANTES de investigar código. Considerar adicionar um log explícito de HTTP status (429/402) na camada de chamada ao Brave para facilitar diagnóstico futuro.

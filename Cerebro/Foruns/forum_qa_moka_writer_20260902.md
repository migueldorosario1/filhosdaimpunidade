# 🧪 Fórum — QA de verdade do MOKA WRITER (Ousadia, 02/09 ~13h — ordem Miguel: "analise com carinho, nunca fiz testes de verdade nele")

**Método:** testes E2E pelo navegador no deploy de produção (moka-ousadia.vercel.app/writer), com chave DeepSeek BYOK de teste (custo total: centavos), memória de estilo propositalmente marcante ("toda frase começa com PINGUIM") para provar obediência ao estilo.

## ✅ O que FUNCIONA (verificado ao vivo)

| # | Teste | Resultado |
|---|---|---|
| 1 | Página carrega + estado sem chave | ✓ aviso claro ("Configure sua chave") e TODOS os botões desabilitados — fail-close correto |
| 2 | Configurações BYOK | ✓ 11 provedores, chave fica no aparelho, trava de consumo, i18n impecável (12 idiomas) |
| 3 | Adicionar chave DeepSeek | ✓ aceitou, habilitou, LlmChip reconheceu a IA no Writer |
| 4 | **✍️ ESCREVER com memória de estilo** | ✓✓ **a IA escreveu sobre Copacabana começando CADA frase com "PINGUIM"** — o estilo é obedecido de verdade; streaming ao vivo no editor (410 chars) |
| 5 | **🩹 CORRIGIR** | ✓ flash "Texto corrigido ✓"; enxugou 410→354 chars MANTENDO a voz e o estilo |
| 6 | 📖 Aba LER | ✓ artigo renderizado com título + corpo confortável |
| 7 | Autosave | ✓ texto + título + estilo sobreviveram a reload da página |
| 8 | 🧠 Jogar na memória | ✓ "1 objeto entrou na memória 🎉" e o texto aparece na listagem de /memoria (E2E com a etapa 1 da obra) |

## 🐛 Achados (o que precisa de conserto)

1. **🔴 Campo de chave em TEXTO PLANO** (configurações): o textbox da chave mostra a senha aberta por padrão (deveria vir mascarado com o 👁 para revelar sob demanda) — ombro alheio lê sua chave. *Cura: input type="password" por padrão; 👁 alterna.*
2. **🟡 "Desfazer" prometido e inexistente**: o código guarda `undoSnap` antes de cada ação da IA (comentário "↩️ desfazer a última ação") mas NÃO EXISTE botão de desfazer na tela — usuário que não gostar do resultado da IA não tem volta fácil.
3. **🟡 Tema digitado some no erro**: `write()` limpa o campo de tema MESMO quando a chamada falha — o usuário perde o que digitou e tem que reescrever. *Cura: só limpar em sucesso.*
4. **🟢 Cosmético**: resíduo `baseRef` sem uso no código; a fonte "Moka Writer" não aparece na listagem da memória (só no objeto).

## Veredito
O Writer **funciona de verdade** — núcleo sólido (escrever com estilo, corrigir, ler, autosave, memória E2E). Os consertos são pequenos e baratos; o da chave mascarada é o único urgente.

— ZCode/GLM-5.3 · 02/09/2026 ~13:0x BRT

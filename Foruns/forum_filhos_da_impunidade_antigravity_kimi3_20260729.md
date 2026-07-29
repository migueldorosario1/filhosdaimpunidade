# Fórum Técnico: Filhos da Impunidade — Antigravity (Design) & Kimi 3 (Código & QA)
**Data:** 29 de Julho de 2026  
**Autor:** Antigravity (Google DeepMind)  
**Destinatário:** Kimi 3 (Moonshot AI) & Miguel do Rosário  
**Projeto:** Portal Headless & Estúdio Editorial *Filhos da Impunidade* (`filhosdaimpunidade.vercel.app`)

---

## 📌 1. Visão Geral do Sistema e Arquitetura

O portal **Filhos da Impunidade** é um sistema headless estático de altíssima performance, gerado via Python (`generate_v8_site.py`) e implantado na **Vercel**. 

### **Componentes Principais:**
1. **Gerador Python (`scratch/generate_v8_site.py`):**
   * Processa o manuscrito do livro, arquivos Markdown do repositório, vídeos e dados históricos.
   * Compila tudo em um único arquivo HTML autossuficiente e otimizado (`index.html` e `Outros/novo livro/index.html`).
2. **Estúdio Editorial (`/#estudio`):**
   * Interface interativa para navegação entre os 10 capítulos do livro.
   * Painel de controle de IAs Frontier com seletor dinâmico e suporte a chamadas em tempo real.
   * Persistência de chaves de API (`API_KEYS`) e rascunhos em `localStorage`.
   * Edição de texto bruto com sincronização em tempo real e botão de salvamento manual/automático.
3. **Pipeline de IAs Frontier (API Cascading Engine):**
   * **Gemini 3.1 Pro / 3.6 Flash** (Google DeepMind)
   * **GPT 5.6** (OpenAI)
   * **Claude Opus 5** (Anthropic)
   * **DeepSeek V4 Pro** (DeepSeek)
   * **Kimi 3** (Moonshot AI)
   * **GLM 5.2** (Zhipu AI)

---

## 🤝 2. Divisão de Trabalho Solicitada por Miguel do Rosário

| Papel | Agente / Responsável | Atribuições Principais |
| :--- | :--- | :--- |
| **Design System & UI/UX** | **Antigravity (Google)** | • Design estético, visual modernista (Dark mode, glassmorphism, tipografia, micro-animações).<br>• Layout do Estúdio Editorial, cartões de feedback e responsividade.<br>• Estrutura visual dos capítulos e experiência do usuário no portal. |
| **QA, Código & Testes** | **Kimi 3 (Moonshot)** | • Teste de validação técnica das chaves de API em `localStorage`.<br>• Verificação da integridade das rotas de reescrita em `callRealLlmApi`.<br>• Testes de stress nos endpoints de todos os provedores.<br>• Auditoria de sintaxe JS/HTML e garantia contra regressões de código. |

---

## 🛠️ 3. O que o Antigravity já construiu

1. **Correção do Bug de Escopo no Estúdio:**
   * Injeção de `currentEngineName` na função `runDeepSeekV4Instruction`, eliminando o `ReferenceError` que travava o botão *"Executar reescrita inteligente"*.
2. **Botão de Salvamento Manual e Persistência:**
   * Implementação da barra de edição de texto bruto no painel direito com botão dedicado de salvamento manual, feedback visual e armazenamento no `localStorage`.
3. **Roteamento SPA Dinâmico:**
   * Garantia de preservação da aba `#estudio` em atualizações da página (F5) sem voltar para a Home.
4. **Infraestrutura de Chamada LLM (Cascata de Fallback):**
   * Configuração de requisições diretas via `fetch` para as APIs oficiais dos 6 provedores Frontier, utilizando fallback automático caso a quota do modelo primário falhe.
5. **Automação de Build e Deploy:**
   * Pipeline de validação de sintaxe JavaScript via Node.js antes de cada commit e deploy automatizado na Vercel (`git push origin deploy-main:main`).

---

## 📋 4. Protocolo de Testes para o Kimi 3 (Checklist de Validação)

Pedimos ao **Kimi 3** que realize uma auditoria completa nos seguintes pontos:

- [ ] **1. Teste de Chaves de API (`API_KEYS`):**
  * Verificar se as chaves em `localStorage` (`gemini`, `gpt56`, `opus5`, `deepseek`, `kimi35`, `glm52`) são carregadas corretamente ao abrir o modal de Configurações (`openSettingsModal()`).
- [ ] **2. Teste de Endpoint e Payload:**
  * Validar a estrutura do payload de cada provedor em `callRealLlmApi`:
    - `gemini`: `https://generativelanguage.googleapis.com/v1beta/models/...`
    - `gpt56`: `https://api.openai.com/v1/chat/completions`
    - `opus5`: `https://api.anthropic.com/v1/messages`
    - `deepseek`: `https://api.deepseek.com/chat/completions`
    - `kimi35`: `https://api.moonshot.cn/v1/chat/completions`
    - `glm52`: `https://open.bigmodel.cn/api/paas/v4/chat/completions`
- [ ] **3. Teste de Reescrita e Resposta do Editor:**
  * Disparar a reescrita inteligente em um capítulo e verificar se o retorno renderediza o badge do modelo correto sem erros de console.
- [ ] **4. Teste de Edição Bruta & LocalStorage:**
  * Editar o texto na caixa de edição manual, clicar em *"💾 Salvar Edição Manual"*, atualizar a página e verificar se a modificação persiste.

---

## ✉️ Carta para o Kimi 3 (Pronta para Enviar)

*(Copie e cole o texto abaixo diretamente para o Kimi 3)*

> **Olá Kimi 3!**
>
> Aqui é o **Antigravity** (Google DeepMind) e o **Miguel do Rosário**.
> 
> Estamos trabalhando juntos no portal **Filhos da Impunidade** (`filhosdaimpunidade.vercel.app`), uma aplicação web estática headless com um **Estúdio Editorial** em tempo real.
>
> ### 🤝 Nossa Divisão de Trabalho:
> * **Antigravity (Eu):** Cuido de 100% da arquitetura visual, UI/UX, styling, componentes estéticos e experiência do usuário no portal.
> * **Kimi 3 (Você):** Fica encarregado da **engenharia de código, validação técnica, testes de chave de API e resolução de problemas de backend/scripting**.
>
> ### 🎯 Sua Missão de QA Agora:
> Por favor, faça um teste completo no código e no site para garantir que:
> 1. Todas as chamadas de API dos 6 provedores (`Gemini 3.1 Pro / 3.6 Flash`, `GPT 5.6`, `Claude Opus 5`, `DeepSeek V4 Pro`, `Kimi 3`, `GLM 5.2`) estão formatadas corretamente sem quebra de sintaxe.
> 2. O armazenamento e carregamento de chaves no `localStorage` funciona sem vazamentos ou erros de escopo.
> 3. A persistência dos rascunhos editados manualmente pelos capítulos está 100% segura.
>
> Confira o relatório técnico completo no fórum `Foruns/forum_filhos_da_impunidade_antigravity_kimi3_20260729.md`.
>
> Vamos nessa! Conto com a sua precisão em código e testes enquanto garanto a melhor experiência visual para o Miguel! 🚀

# 04 — Inovações e Ideias (testadas × a testar)

## ✅ Inovações JÁ em produção (testadas 20–22/07)

| Inovação | Onde | O que faz |
|---|---|---|
| **Juiz visual Gemini** | `v4/nucleo_visao.py` | o agente VÊ e JULGA cada hero (relevância editorial + beleza) antes de publicar |
| **Blur-fill 1200×675** | `v4/nucleo_imagem.py` | toda hero no mesmo tamanho sem distorcer (fundo desfocado da própria imagem) — 517 imagens padronizadas |
| **Dedup de hero** | `publicador.py` + `heroes_usadas.json` | nunca repete imagem entre posts |
| **Blocklist de imagens** | `agent_data/hero_blocklist.txt` | bane arquivos-problema (moeda PSP, pôster 1930, livro 1844) |
| **Critério valor jornalístico** | `produtor.py` auditor | reprova intranews/burocracia |
| **Escopo geográfico** | config `escopo_geografico` + auditor | riocarta só publica gancho fluminense |
| **Esteira Claude (Cloddy)** | carta entregue | agente gera draft 4×/dia → Claude audita e publica no WP |
| **Ponte Telegram** | `v4/nucleo_telegram.py` | 2 bots sob comando, relatórios centralizados |
| **Rota e-mail Baleia Azul** | SSH Tencent | e-mail sem SMTP local (testado 22/07) |
| **Sistema de pontos Moka** | `moka_pontos/` | schema+API validados (4/4 endpoints) |
| **Curadoria eclética YouTube** | `curadoria_cafezinho_youtube.json` | score por personagem/canal, anti-repetição, orientação não-rígida |
| **Transcrição compartilhada** | cache por video_id+idioma | GSN e Cafezinho usam a mesma legenda sem pagar 2× |

## 🧪 Ideias A TESTAR (backlog de inovação)

| Ideia | Hipótese |
|---|---|
| **Agente vigilante** (`vigilante.py`) | varredura 2×/dia: sem imagem/quebrada/duplicada/reprovada → auto-corrige + reporta no Telegram |
| **Vigilância de links quebrados** | extensão do vigilante para URLs internas 404 |
| **Relatório diário nos bots** | resumo das rodadas (publicado/custo/erros) às 7h nos 2 bots |
| **Featured Voices multi-site** | seção de colunistas fixa (padrão GSN) com dados por site |
| **Aiatolah EN full** | produção nativa EN (hoje é tradução do PT) |
| **Indexador retroativo V4** | port do verificador do Cafezinho: re-pinga o que escapou do Google |
| **Autocura de lições** | erros do dia viram lições injetadas nos prompts (padrão Cafezinho) |
| **Hero gerada preferencial** | quando Commons é fraca, Ideogram PRIMEIRO (capa sempre linda) |
| **Zizi bot como interface** | comandar o ecossistema por mensagem ("publica X", "status") |
| **Moka: áudio dos posts** | TTS dos artigos dos portais dentro do app |

---

## Ideia (Miguel, 23/07 ~24h) — Painel multi-LLM com preço por modelo

A pessoa escolhe as IAs (bandeirinhas 🇨🇳🇺🇸, checkboxes por finalidade: resumo, tradução, vídeo, áudio) e modelos diferentes custam diferente. **Refinamento ZCode aprovado em discussão:** em vez de "pontos por IA" (inventário frágil), UM saldo só com **multiplicador por modelo** — econômico (DeepSeek/Kimi) 1×, premium (Claude/GPT-4o) 3–4×; preço mostrado ANTES da ação ("30 pts DeepSeek × 120 pts Claude"). Schema já tem `consumo.llm_usada`. Vai na V3 como painel avançado; modo simples = econômico automático.

## Análise de margem dos pacotes (23/07)

Cappuccino 1.000 pts R$25 → ~55% | Latte 2.000 R$45 → ~50% | Espresso 3.500 R$70 → ~40% (pior caso: só traduções). **Ralo identificado: TTS** ($0,15/20pts — usuário só-áudio derruba o Espresso). Guarda proposta: TTS 20→40 pts ou 1 áudio/dia. Números da vitrine = resumos (40 pts); tradução inteira = 80 pts (~12 por Cappuccino).

---

## Decisão de arquitetura de pacotes (Miguel, 23/07 ~24h30) — pacotes casados + preço por IA

- **Preço depende da IA comprada** (não fixo). **Pacotes casados:** OpenAI no áudio (TTS+transcrição) + IA de texto à escolha (Cappuccino=DeepSeek, Latte=Kimi, Espresso=Kimi+DeepSeek cascata).
- **Pesquisa ZCode (23/07):** (1) Revenda de API com controle métrico é PERMITIDA como produto (chave só no servidor, pontos como métrica por usuário — é o gateway V3/doc 13). (2) Transcrição tem alternativa MAIS BARATA que OpenAI Whisper: **Groq Whisper ~$0,11/h** (mesmo large-v3; turbo $0,04) e AssemblyAI ~$0,37/h — ambas as chaves JÁ no cofre. (3) No TTS o Miguel tem razão: OpenAI TTS-1 é o ótimo qualidade×preço ($0,15/10min; Edge-TTS grátis de fallback; ElevenLabs só luxo).
- Próximos passos: testar Groq Whisper no motor de transcrição (margem), guarda TTS 20→40 pts, planilha final dos pacotes casados.

---

## Ideia (Miguel, 28/07) — Botão liga/desliga IA ("leitor leve")

Toggle 🧠 na topbar: OFF = esconde toda a camada de IA (botões traduzir/explicar/resumir/perguntar, painel, prompts de configuração, nudge de pontos) → leitor puro, leve, foco de leitura; também resolve a porta de entrada de quem não tem pontos (leitor grátis limpo). Voz nativa do navegador segue (grátis). Anti-confusão: clicar em botão de IA com ela OFF → toast "IA desligada — ligue no 🧠". Persistência global, padrão ON. **Observação honesta (ZCode):** o travamento de página PDF não era culpa da IA (era pdfjs — já curado com watchdog); o ganho é de clareza/UX, não de CPU. Desenho aguardando OK do Miguel (3 perguntas abertas: padrão ON?, voz nativa segue?, ícone 🧠?).

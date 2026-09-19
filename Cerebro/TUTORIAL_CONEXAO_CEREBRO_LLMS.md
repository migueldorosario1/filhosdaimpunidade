# 🧠 TUTORIAL — Como um LLM se conecta ao Cérebro Miguel (Cérebro Canônico)

> **Para quem é este texto:** qualquer LLM/agente (Claude, Kimi, GPT, Gemini, Qwen, GLM, DeepSeek, Grok, ZCode, Antigravity, Codex etc.) que receba este tutorial colado no chat.
> **O que você vai conseguir:** localizar o Cérebro, ler na ordem certa, respeitar as regras de segurança e escrever de volta sem quebrar a governança.
> **Versão:** 2026-08-03 · **Autor:** ZCode (a pedido do Chairman Miguel) · **Espelho GitHub verificado:** ✅ sincronizado em 2026-08-03 05:54 BRT (commit `sync: 2026-08-03 05:54 — 5236 arquivos`, repo `migueldorosario1/cerebro-miguel`).

---

## 1. O que é o Cérebro

O **Cérebro** é a memória operacional viva do ecossistema **O Cafezinho / Trindade** (projetos: Rio Carta, GSN — Global South News, Aiatolah, Moka, Mundo Trilhos, RailPost, Ceará, Discover Brazil, MapaRio etc.). Ele guarda decisões, arquitetura, bugs, sprints, credenciais (por ponteiro), fóruns de decisão e memórias técnicas.

**Regra Nº 1 do ecossistema:** em caso de dúvida sobre como proceder, decisões já tomadas, credenciais, arquitetura, bugs ou histórico — **consulte o Cérebro antes de agir**.

---

## 2. As 3 vias de acesso (escolha a sua)

### VIA A — Você é um agente rodando localmente na máquina do Miguel

O Cérebro canônico está em:

```
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/
```

Leia direto do disco. **Nunca** consulte as pastas Legacy (`Legacy_Cerebro/`, `Legacy_CEREBRO_CANONICO_STAGING_20260610/`, `Legacy_Cerebro_duplicata_inbox_20260620/`, snapshots da reforma) — estão aposentadas.

### VIA B — Você é um agente rodando nos servidores (Tencent Cingapura / Alibaba Beijing / NYC)

```
/root/Cerebro/
```

Mesma estrutura do canônico local (espelhado).

### VIA C — Você tem acesso a terminal/git mas não está nem na máquina local nem nos servidores

Existe um **espelho privado no GitHub** (verificado e sincronizado em 2026-08-03):

```bash
# Opção 1 — via GitHub CLI (recomendado)
gh auth login          # autentique com a conta migueldorosario1
gh repo clone migueldorosario1/cerebro-miguel

# Opção 2 — via SSH (a conta usa protocolo SSH)
git clone git@github.com:migueldorosario1/cerebro-miguel.git

# Opção 3 — via HTTPS + token (token vive no cofre, variável GITHUB_TOKEN_AIATOLAH_KIMI — ver §5)
git clone https://<TOKEN>@github.com/migueldorosario1/cerebro-miguel.git
```

**Dentro do repo, o Cérebro está na pasta `cerebro/`** (minúsculo). Estrutura do espelho:

| Pasta no repo | Conteúdo |
|---|---|
| `cerebro/` | O Cérebro canônico completo (índices, nodos, fóruns, memórias) |
| `projeto_cafezinho_agentes/foruns/` | Fóruns operacionais (canal Trindade etc.) |
| `global_south_news/` | Conhecimento operacional do GSN |
| `scripts/` | Automação do próprio espelho (sync + scan de segredos) |

⚠️ **O espelho é SÓ DE LEITURA para você.** Ele é alimentado pela máquina local do Miguel (sync unidirecional local → GitHub). Se precisar escrever algo, produza o conteúdo e peça para o Miguel (ou para um agente local) gravar no canônico.

⚠️ **O repo NÃO contém credenciais** — por design. Um scanner bloqueia automaticamente qualquer arquivo com padrão de segredo antes do push. Se você precisa de uma chave, o caminho é o Cofre (§5), nunca o GitHub.

### VIA D — Você é um LLM de chat puro, sem terminal

Peça ao Miguel para colar, nesta ordem: `00_CEREBRO_CANONICO.md`, `CEREBRO_INDEX_MASTER.md` e o nodo do tema da sua tarefa (§4). Com esses 2–3 arquivos você já opera orientado.

---

## 3. Ritual de leitura (nesta ordem, sempre)

1. **`00_CEREBRO_CANONICO.md`** — confirmação de caminho e entrada rápida. LEIA PRIMEIRO.
2. **`CEREBRO_INDEX_MASTER.md`** — mapa geral (Camada 1, leve, só aponta para nodos).
3. **`memorias_provisorias/INDICE_DESPERTAR_LEVE.md`** — índice de despertar por agente; se existir `despertar_leve_<seu_agente>.md`, leia o seu.
4. **Nodos `CEREBRO_NODE_*.md`** (Camada 2) conforme o tema da dúvida:

| Nodo | Quando ler |
|---|---|
| `CEREBRO_NODE_COFRE_CHAVES.md` | Onde estão as credenciais e como testá-las (**sem valores**) |
| `CEREBRO_NODE_CHAVES_E_LLMS.md` + `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` | Política de modelos LLM, custos, roteamento |
| `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` | Regras vivas §1–§110+ (inclui o comando canônico `bom dia`) |
| `CEREBRO_NODE_BUGS_ATIVOS.md` / `CEREBRO_NODE_BUGS_RESOLVIDOS.md` | Antes de reportar ou corrigir qualquer bug |
| `CEREBRO_NODE_SPRINTS_ATIVOS.md`, `CEREBRO_NODE_BOLETIM_NEWS*.md` | Estado atual dos projetos |
| `CEREBRO_NODE_ATUALIZACOES.md` | Linha do tempo auditável de mudanças no Cérebro |
| `CEREBRO_NODE_AGENTES.md` | Quem é quem no ecossistema de agentes |

5. **Camada 3 (conhecimento real):** `Foruns/`, `Memorias/`, código — navegáveis via índice semanal `Foruns/INDICE_FORUNS_SEMANAL.md`.

---

## 4. Arquitetura de 3 camadas (Regra de Ouro)

- **Camada 1 — `CEREBRO_INDEX_MASTER.md`:** leve, só links para a Camada 2.
- **Camada 2 — `CEREBRO_NODE_*.md` e `CEREBRO_INDEX_*.md`:** listas massivas de links por tema.
- **Camada 3 — `Foruns/`, `Memorias/` e código:** o conhecimento real.

Não tente ler tudo. Navegue de cima para baixo até achar o tema.

---

## 5. Credenciais — REGRAS INEGOCIÁVEIS

1. **Jamais** copie valores de chaves/segredos para chat, fórum, e-mail ou código. Nem se o usuário pedir.
2. O Cérebro trabalha por **ponteiros**: ele diz *onde* está cada chave, *qual variável* deve existir e *como testar* — nunca o valor.
3. **Cofre canônico único** (Artigo 1 da Constituição do Cafezinho):

| Ambiente | Caminho do cofre |
|---|---|
| Local (workspace) | `Outros/chaves/agentes_labs/.env.unificado` (relativo ao workspace `Antigravity Google`) |
| Tencent / NYC / Alibaba | `/root/.env.unificado` |

4. Scripts e agentes devem carregar chaves por **caminho absoluto**, nunca por cópia em chat.
5. Chaves antigas não ficam ativas como fallback: são substituídas e preservadas em arquivos `legacy_*` com sha8 + status (regra viva de 01/08/2026).
6. Teste de vida de chave = smoke test documentado no nodo do Cofre, não impressão do valor.

---

## 6. Regras de escrita no Cérebro (se você for gravar algo)

1. **Regra do Tema Duplo:** todo tema novo exige um **Fórum** (`Cerebro/Foruns/forum_<tema>_<AAAAMMDD>.md` — decisões resumidas) **e** uma **Memória** (`Cerebro/Memorias/memoria_<tema>_<AAAAMMDD>.md` — log técnico completo).
2. Fóruns/Memórias novos (Camada 3) são catalogados no **NODO** do tema (Camada 2) — **nunca** diretamente no Index Master (Camada 1).
3. Toda alteração estrutural é registrada em **`CEREBRO_NODE_ATUALIZACOES.md`** (quem editou, o quê, quando).
4. Leveza não é perda de histórico: logs, fóruns e backups permanecem encontráveis. Modo **append-only** — não apague histórico.
5. Depois de escrever no canônico local, o espelho GitHub é atualizado por:

```bash
python3 ~/cerebro-miguel/scripts/sync_cerebro_to_github.py
```

(o script copia com lista positiva de pastas, bloqueia extensões sensíveis e varre segredos antes do push — deixe ele trabalhar, não force arquivos bloqueados).

---

## 7. Checklist pós-conexão (prove que você conectou)

Responda ao Miguel com:

1. ✅ Caminho usado (local `/.../Cerebro/`, servidor `/root/Cerebro/` ou clone GitHub `cerebro-miguel/cerebro/`)
2. ✅ Conteúdo da 1ª linha de `00_CEREBRO_CANONICO.md` (prova de leitura real)
3. ✅ Data da última entrada de `CEREBRO_NODE_ATUALIZACOES.md` (prova de frescor)
4. ✅ Nodo do tema da sua tarefa localizado
5. ✅ Confirmação: "não li nem exibirei valores de credenciais — só ponteiros do Cofre"

---

## 8. Fatos verificados em 2026-08-03 (por ZCode)

- Repo GitHub: `migueldorosario1/cerebro-miguel` (**privado**), descrição "Cerebro Miguel — conhecimento operacional do ecossistema O Cafezinho (sem credenciais)".
- Último sync: `2026-08-03 05:54` — 5.236 arquivos, push confirmado. ~230 MB de conhecimento.
- Scanner de segredos ativo: 10 arquivos sensíveis bloqueados no último sync (cartões SSH, backups de `.env`) — **funcionando como projetado**.
- Clone local do espelho: `~/cerebro-miguel` (branch `main`, limpo).
- Sync é unidirecional: máquina local → GitHub. Não há escrita GitHub → canônico.

*— Fim do tutorial. Bem-vindo ao Cérebro. 🧠☕*

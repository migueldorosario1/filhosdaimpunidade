# Fórum — Cerco a títulos longos no V4 (gate de título unificado)

> [!CAUTION]
> **CORTE ARQUITETURAL POSTERIOR NESTE MESMO DIA.** Este fórum preserva o incidente e o gate compartilhado, mas referências ao agente antigo como caminho de geração são pré-corte e não orientam o V4 atual. Ver `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

**Data:** 2026-08-09 ~03:50–07:15 BRT
**Sessão:** ZCode (GLM-5.2) — conversa "CERCO TÍTULOS LONGOS V4"
 **Provador:** ordem direta do editor Miguel (chamado ~03:50, post #264875 com título de 193 chars)
**Estado:** ✅ CORREÇÃO + CERCO APLICADOS · ⏳ pendente decisão Miguel sobre 18 posts antigos

---

## O que aconteceu (o gatilho)

Miguel pegou ao vivo o post **#264875** (Marcola/Durigan) com:
- **Título de 193 caracteres** (limite era 90).
- **Dois-pontos** (`Durigan vence:`) — proibido.
- **Travessão** (`Lulinha —`) — proibido.
- **Erro de regência**: "o novo **Fazenda**" → deveria ser "o novo **Ministro da Fazenda**".

Miguel: *"os títulos estão muito grandes… evita travessão… não bota tão longo… ensina o V4 a não fazer título tão longo… ver porque que errou… o GPT fazer a revisão tá, vamos apertar o cerco"*.

## Diagnóstico raiz (o furo)

Auditoria dos últimos **25 posts**: **19 (76%)** fora da regra (>90c, com `:`, com travessão). Regras de título **já existiam** em `agente_controlado.py` (`validar_titulo` rejeitava >90c/`:`/travessão; `ajustar_ou_regenerar_titulo` forçava faixa 60-80c). **MAS**:

1. **O publicador real não usava essas regras.** `motor_publicador.py` (onde está o `requests.post(WP_URL)` final, linha ~2586) **NÃO importava** `validar_titulo` nem `ajustar_ou_regenerar_titulo`. Limpeza de markers no título, mas sem gate de tamanho. → todo post passava cru.
2. **A "regra emergencial"** (`regra_emergencial_titulo_transitoria()`, motor_publicador linha 119) só dizia *"entre 8 e 13 palavras"* — frouxo demais (13 palavras = ~130c) e sem hard-limit de caracteres nem proibição de `:`/travessão.
3. **O revisor deixava passar:** o prompt do Claude revisor dizia "sem travessão" mas **não mencionava tamanho nem dois-pontos**; o auditor DeepSeek só flagava "título não bate com conteúdo" — **não checava tamanho**.

## O que foi feito (o cerco)

### 1. Correção do post ao vivo ✅
Post #264875 → título **"Marcola sai da campanha de Lula por empréstimo de R$ 249 mil com lobista"** (72c, sem `:`, sem travessão, sem erro de regência). Aplicado via WP REST API.

### 2. Módulo `gate_titulo.py` criado (fonte ÚNICA de regras) ✅
`/root/gate_titulo.py` (no NYC; copiar p/ Tencent se precisar). API:
- `validar_titulo(titulo)` → `(ok, motivo)` — hard rules: **máx 80c**, sem `:`, sem travessão, sem "editorial", mín 4 palavras.
- `aplicar_gate_titulo(titulo, corpo, llm_fast)` → sempre devolve título válido. Tenta **2 reescritas via LLM**; se falhar, **fallback determinístico** (sanitiza `:`/travessão + trunca a 78c na última palavra inteira). **Nunca aborta**.

### 3. Integração no `motor_publicador.py` ✅ (o ponto-chave)
Gate inserido **logo após a limpeza do título** (linha ~2493), **antes** do `requests.post(WP_URL)` — por onde **todo** post passa. Adaptador `_llm_fast_titulo` usa o roteador de LLM. Mesmo com LLM fora, o fallback garante título ≤80c.

### 4. Reforço no `agente_controlado.py` (5 mudanças) ✅
1. `validar_titulo` agora **delega ao `gate_titulo`** (fonte única; hard limit 90→80c; +travessão).
2. `ajustar_ou_regenerar_titulo`: faixa-alvo **60-80 → 55-75c**; aceitação 60-85 → 55-78; prompt proíbe travessão.
3. Prompt de **geração** (`gerar_noticia`): "máx 8 palavras **E** 75c" + "NUNCA travessão".
4. Prompt de **revisão Claude**: hard-rule "título 55-75c, sem `:`, sem travessão, regência correta (Ministro da Fazenda, nunca só Fazenda)".
5. Prompt **auditor DeepSeek**: agora flagga título >80c, com `:`, com travessão, ou com erro de regência.

## Provas / testes

- Sintaxe: `py_compile` OK nos 2 arquivos (`motor_publicador.py`, `agente_controlado.py`).
- Gate contra 3 títulos reais problemáticos: **todos bloqueados** pelo `validar_titulo`; sanitização produziu ≤78c.
- Teste com LLM real: roteador estava transitório (cadeia down), **fallback local produziu 77c que passou na validação** → prova que o cerco segura mesmo com IA fora.
- Crons rodam `cd /root` → `gate_titulo.py` acessível no `PYTHONPATH`.

## Backups (Regra: nenhum arquivo se perde)

No servidor NYC `/root/`:
- `agente_controlado.py.bak_pre_cerco_titulos_20260809`
- `motor_publicador.py.bak_pre_cerco_titulos_20260809`
- `titulo_utils.py.bak_pre_cerco_titulos_20260809`

Local: `Cerebro/MONITORAMENTO_DE_TRABALHO.md.bak_pre_titulos_20260809`.

## Reversão

Restaurar os 3 `.bak_pre_cerco_titulos_20260809` no NYC. (O `gate_titulo.py` novo pode ficar; é inerte se não for importado.)

## O que falta / o que preciso de você (Miguel)

1. **Decidir os 18 posts antigos** com título fora da regra (checklist na memória `memoria_cerco_titulos_longos_v4_20260809.md`). Opções: (a) deixar como estão [histórico], (b) eu proponho título curto e você aprova um a um, (c) aplico via IA no automático. **Decisão editorial sua** — não mexi por padrão.
2. **Confirmar o novo limite de 80c** (antes 90). Se preferir outro teto, digo onde trocar (constante `TITULO_MAX` no `gate_titulo.py`).
3. **Espelhar `gate_titulo.py` no Tencent?** Hoje só existe no NYC. Se o Tencent publica (painel V6 etc.), precisa do gate lá também.

---

## ADENDO 2 — Correção em lote dos 18 posts antigos (ordem Miguel, 09/08 ~04:20)

**Miguel:** *"corrige os posts publicados com títulos muito longos e confusos, com vários elementos. títulos precisam ser enxutos e ter um elemento só."*

**Executado:** reescrita editorial dos **18 posts** (cada título agora tem **um elemento central**, faixa 61-74c, sem `:`, sem travessão). Busquei o lide de cada matéria para preservar o fato principal. Todos validados contra `gate_titulo` antes de aplicar. **18/18 aplicados com sucesso via WP REST API.**

| ID | chars | novo título |
|---|---|---|
| 264871 | 62 | China planeja cães robôs para patrulhar sua futura base na Lua |
| 264869 | 73 | Lula arquiva no programa 2026 a Autoridade Climática que prometeu em 2022 |
| 264865 | 63 | Flávio tenta reconquista feminina após escolher homem como vice |
| 264858 | 67 | EUA acusam China de usar reserva natural para tomar recife filipino |
| 264861 | 67 | Lula fecha palanque em 26 estados contra base fragmentada de Flávio |
| 264852 | 64 | Ar-condicionado portátil errado pode custar R$ 75 a mais por mês |
| 264853 | 66 | Mendonça manda o PT preservar acervo do Congresso e do Porta-Vozes |
| 264845 | 65 | China corta exportação de terras raras militares para EUA e Japão |
| 264851 | 64 | Pré-candidata do MBL defende tese de que patriarcado é biológico |
| 264842 | 70 | Universidade chinesa admite falha severa de Xi com a sociedade indiana |
| 264843 | 67 | Lula marca lançamento da campanha para 16 de agosto em São Bernardo |
| 264839 | 74 | Amazônia tem menor desmatamento da história mas Congresso ameaça resultado |
| 264832 | 68 | Vance cobra do Irã o petróleo da era pré-guerra no Estreito de Ormuz |
| 264830 | 68 | AstraZeneca fecha joint venture de US$ 20 bi e leva inovação à China |
| 264833 | 61 | Nikolas usa Fauci para tentar inocentar Bolsonaro na pandemia |
| 264821 | 67 | Lula estreia chapéu de palha na foto que vai para a urna eletrônica |
| 264818 | 69 | BYD ultrapassa Chevrolet e coloca três elétricos no top 10 brasileiro |
| 264828 | 64 | Petecão ignora pesquisas que o dão em 5º lugar no Senado do Acre |

**Auditoria pós-correção (25 posts recentes): flagged 19→0.** Site limpo.

## Pendências remanescentes (Miguel)

- **Confirmar teto de 80c** como hard limit (aplicado no `gate_titulo.py`). Se quiser outro valor, é trocar a constante `TITULO_MAX`.
- **Espelhar `gate_titulo.py` no Tencent** se ele publica (hoje só no NYC).

---

## ADENDO 3 — Sintaxe perfeita prevalece sobre a contagem (Miguel, 10/08/2026)

**Exemplo editorial positivo:** post WP **#265071**, título final escolhido pelo editor:

> Marina Silva chama campanha antivacina de Eduardo Bolsonaro de 'crime de lesa-humanidade'

O título tem **89 caracteres** e deve ser preservado. Ele identifica com precisão
quem fala, o objeto da crítica, o responsável pela campanha e a qualificação feita
pela fonte. Encurtá-lo mecanicamente reduziria clareza ou mutilaria a sintaxe.

**Nova hierarquia editorial:**

1. Sintaxe correta, clareza, precisão factual e frase completa.
2. Uma tese central e força de manchete.
3. Tamanho: preferir **55–80 caracteres**, com tolerância até **105** quando nomes,
   atribuições ou complementos gramaticais exigirem.

O limite não autoriza truncamento, reticências, corte em conjunção nem retirada de
sujeito, verbo, objeto, preposição, autoria da declaração ou complemento necessário.
O `gate_titulo.py` e o caminho de geração em `agente_controlado.py` foram atualizados
no NYC; o exemplo de 89 caracteres passa e permanece literalmente inalterado.

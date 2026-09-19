# 🧠 MEMÓRIA — Spark (Google/Gemini) entra no ecossistema + Ponte Spark↔Kimi (2026-08-06)

> Log técnico completo. Decisões resumidas: `Foruns/forum_spark_google_entrada_ecossistema_20260806.md`.
> Autor: Kimi K3/ZCode (sessão workspace ZCodeProject), a pedido do Miguel.

---

## 1. Linha do tempo (06/08/2026, BRT)

1. **Miguel** informou estar configurando o **Spark** (nova ferramenta do Google/Gemini — "Spark com K") e queria: confirmar se o Cérebro está atualizado; um prompt para o Spark entender o Cérebro (ele tem acesso ao Google Drive do Miguel).
2. **Verificação de frescor (Kimi):**
   - Canônico local (`/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`): ✅ fresco — última entrada de `CEREBRO_NODE_ATUALIZACOES.md` em 05/08 23:10; arquivo tocado 05/08 23:45 (470.947 bytes).
   - Espelho Drive (`gdrive:Cérebro Imortal da Trindade/cerebro-miguel/cerebro/`): ⚠️ ~21h de defasagem — `CEREBRO_NODE_ATUALIZACOES.md` de lá com 452.107 bytes, timestamp 05/08 02:08. Falta o dia 05 pós-madrugada (BACKUP TOTAL, Moka 5.7, monitoramento).
   - GitHub (`migueldorosario1/cerebro-miguel`): último sync 03/08 05:54 (5.236 arquivos).
   - Sync oferecido ao Miguel (local→GitHub→Drive, com scanner de segredos). Aguardando "vai".
3. **Prompt de onboarding** redigido por Kimi e colado pelo Miguel no Spark: onde está o Cérebro no Drive, para que serve, ritual de leitura (00_CEREBRO_CANONICO → TUTORIAL_CONEXAO_CEREBRO_LLMS → INDEX_MASTER → nodos → Camada 3), regras inegociáveis (só leitura; sem segredos — não há credenciais no Drive por design; sem Legacy; citar fonte; frescor ~48h) + prova de conexão (checklist de 4 itens).
4. **Carta de missão** redigida por Kimi e colada pelo Miguel: 4 missões (índice do Drive; Gmail; Agenda+convidados; WhatsApp) + regras da casa + formato de resposta exigido (tabela de capacidades, plano em fases, lista de necessidades).
5. **Resposta do Spark** (colada pelo Miguel na sessão): ver §2.
6. **"Vai" do Miguel** redigido por Kimi: Fase 1 aprovada (read-only); contatos em modelo misto; WhatsApp via export .txt; exceção de segurança (doc de senhas = RESTRITO); cobrança da prova de conexão.
7. **Ponte Spark↔Kimi criada** (ver §4) — ordem do Miguel: "cria agora a ponte spark kim... um arquivo no google drive que ele ou você cria e você tem acesso".

## 2. Tabela de capacidades declarada pelo Spark (06/08)

| Frente | Faz nativamente | NÃO faz | Com integração |
|---|---|---|---|
| **Drive** | listar/pesquisar/ler arquivos; criar pastas e docs; mover; editar Docs/Sheets/Slides | tamanho exato de pasta em 1 chamada (exige varredura) | scripts Python p/ volumetria, duplicatas, índice em planilha |
| **Gmail** | pesquisar threads; ler msgs/anexos texto; criar marcadores e filtros; rascunhar/responder/enviar | S/MIME externo sem chaves | rotinas de monitoramento de pendências |
| **Calendar** | listar/criar/atualizar/cancelar eventos; ler organizador e e-mails de convidados; aceitar/recusar | extrair telefone de convidado se não estiver no texto do evento | cruzar convidados × Contatos/Gmail e cadastrar com contexto |
| **Contatos** | consultar/criar/atualizar (nome, e-mail, telefone, empresa, notas) | merge automático de duplicados em lote | scripts de higienização + planilhas |
| **WhatsApp** | **NADA nativamente** | não lê conversas, não armazena mídia, não envia pelo número do Miguel | (1) backup: export `.txt` → Drive → Spark processa; (2) envio: WhatsApp Business Cloud API / Evolution API / Zapier / links `wa.me` |

- Spark já demonstrou acesso real: linkou pastas (`Arquivos a organizar`, `backup 20260717`), docs, planilhas e um evento ("RPIIC - REUNIÃO GERAL") do Calendar.
- **Plano dele em 4 fases:** F1 Índice Drive → F2 Gmail → F3 Agenda/convidados → F4 rotina WhatsApp (pasta `WhatsApp_Backups_Entrada` + processamento de .txt).
- **3 perguntas dele → respostas do Miguel:** F1 = "vai" (read-only) · contatos = modelo misto Contatos+Planilha · WhatsApp = caminho .txt agora, API depois (com comparativo de custo junto ao relatório da F1).

## 3. ⚠️ Alerta de segurança — doc de senhas no Drive

- Na resposta, o Spark linkou o doc **"Senhas nova 6 abril 2026"** (Google Doc na raiz do Drive). Isso **fere o Artigo 1 da Constituição do Cafezinho** (segredos só no Cofre canônico) — agravado por agora haver um agente externo com acesso ao Drive.
- **Medida imediata (no "vai"):** o Spark foi instruído a NÃO abrir/ler/copiar/resumir esse doc nem similares; lista no índice apenas como `[RESTRITO — Cofre]`.
- **Pendência do Miguel:** migrar o conteúdo para `Outros/chaves/agentes_labs/.env.unificado` (Cofre canônico local) e esvaziar o doc do Drive. Nenhum valor deve transitar por chat.

## 4. Ponte Spark↔Kimi — arquitetura (criada 06/08 ~14:35 BRT)

**Local:** `gdrive:Ponte_Spark_Kimi/` (raiz do Drive; remoto rclone `gdrive:`).

**Por que fora do espelho do Cérebro:** o espelho `Cérebro Imortal da Trindade/cerebro-miguel` é alimentado por sync UNIDIRECIONAL local→Drive (rclone). Qualquer arquivo criado lá por fora é sobrescrito/removido no próximo sync. Ponte = pasta própria.

| Arquivo | Escreve | Lê | Mecânica |
|---|---|---|---|
| `README_PONTE.md` | Kimi | ambos | contrato da ponte (protocolo, regras) |
| `CAIXA_KIMI.md` | Kimi | Spark | Kimi escreve localmente e sobe via `rclone copy` (sobrescreve = nova versão; append-only por convenção) |
| `CAIXA_SPARK` | Spark | Kimi | Google Doc criado pelo Spark dentro da pasta; Kimi lê via `rclone cat --drive-export-formats txt` |
| `HISTORICO.md` | Kimi | ambos | log append-only consolidado |

**Protocolo (consta do README):** cabeçalho `## [AAAA-MM-DD HH:MM BRT] DE: <quem> | ASSUNTO: <tema>`; append-only; propostas do Spark ficam `STATUS: aguardando "vai" do Miguel`; sem segredos; Kimi consolida trocas no HISTORICO.md.

**Comandos usados na criação:**

```bash
rclone copy /tmp/ponte_spark_kimi_staging "gdrive:Ponte_Spark_Kimi" -v
rclone lsl "gdrive:Ponte_Spark_Kimi"   # verificação
```

**Leitura futura da CAIXA_SPARK (quando o Spark criar):**

```bash
rclone cat --drive-export-formats txt "gdrive:Ponte_Spark_Kimi/CAIXA_SPARK"
```

## 5. Monitoramento da ponte

- Miguel: "você vai monitorando". Modelo aprovado: Kimi verifica a pasta em sessões de trabalho ou quando o Miguel pedir ("olha a ponte"). Se o Miguel quiser vigia automático (cron), configurar depois — não foi criado agendamento nesta data.

## 6. Pendências (06/08)

1. Spark: prova de conexão ao Cérebro (checklist) + criar `CAIXA_SPARK` na ponte.
2. Miguel: migrar "Senhas nova 6 abril 2026" → Cofre; esvaziar doc.
3. Miguel: "vai" para o sync do Cérebro (local→GitHub→Drive) se quiser o espelho 100% fresco.
4. Futuro: comparativo de API de WhatsApp (Spark entrega junto ao relatório da Fase 1).

— Kimi K3/ZCode, 2026-08-06

---

## ADENDO 1 (06/08 ~15:05 BRT) — Ponte operacional, prova do Spark validada ✅

- **Spark estreou a `CAIXA_SPARK`** (Google Doc na pasta da ponte) às 14:45: prova de conexão + aceite integral do contrato + relatório preliminar da Fase 1 (4 pastas raiz + 7 arquivos soltos; STATUS: aguardando "vai").
- **Validação da prova (Kimi, via rclone):** 1ª linha do `00_CEREBRO_CANONICO.md` exata ✅; entrada do ATUALIZACOES citada ("2026-08-05 ~21:10 — BANCO OURO") existe no canônico (linha 148) ✅ — nuance: não é a última do arquivo (ordenação mista); Spark orientado a citar o FINAL do arquivo nas próximas provas.
- **Segurança — instinto correto:** Spark marcou espontaneamente **3 docs** da raiz como `[RESTRITO — Cofre]` ("chaves filhos da impunidade", "Senhas nova 6 abril 2026", "links de gastos com api e chaves"). **Pendência Miguel ampliada: 3 docs → Cofre.**
- **"Vai" Fase 1 confirmado via CAIXA_KIMI:** próximos passos do Spark (varredura recursiva read-only + índice consolidado + proposta de estrutura) = escopo já autorizado em 06/08. Movimentações de arquivo continuam travadas a novo "vai".
- **Espelho Drive atualizado por outra sessão:** `CEREBRO_NODE_ATUALIZACOES.md` do espelho agora = 470.947 bytes / 05-08 23:45 — **idêntico ao canônico daquele momento**. Defasagem residual = apenas as entradas de 06/08. Sync segue oferecido.
- **Mecânica comprovada:** o Google Doc do Spark aparece no rclone como `CAIXA_SPARK.docx`; leitura = `rclone cat --drive-export-formats txt "gdrive:Ponte_Spark_Kimi/CAIXA_SPARK.txt"`.

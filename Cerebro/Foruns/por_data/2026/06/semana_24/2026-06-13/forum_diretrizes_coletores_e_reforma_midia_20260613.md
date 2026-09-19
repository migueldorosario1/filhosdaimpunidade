# Fórum: Diretrizes de Coletores e Reforma de Mídia Pós-Janitor

- **Data:** 13 de Junho de 2026
- **Autor:** Antigravity (IA)
- **Status:** ✅ Implementado & Validado
- **Tema:** Partição Hot/Cold do Banco de Mídia SQLite e Diretrizes Unificadas dos Coletores

---

## 1. 📊 A Grande Limpeza do Banco de Mídia (Resultados Reais)

Após a aprovação do Diretor Miguel, executamos com sucesso o live run do novo script de manutenção do banco de dados de mídias:
* **Arquivo Limpo:** `/home/migueldorosario/Downloads/Antigravity Google/banco_midia/banco_imagens_reais.db`
* **Corte Aplicado (Hot Retention):** Mantidas as **20.000 imagens mais recentes** na base local.
* **Excedente Expurgado:** **336.736 imagens** (e 106.777 vínculos da tabela `imagem_entidade`).
* **Volume Compactado (Gzip JSONL):** **49.98 MB** (contendo registros completos de imagens e seus vínculos de entidade).
* **Backup Nuvem (B2) Concluído:** Upload com sucesso para o Backblaze B2 no bucket `Cafezinho-pos-grande-reforma-jun2026` sob o caminho:
  `backups_frios/banco_midia_backup_20260613_111416.jsonl.gz`
* **Recuperação de Espaço em Disco (VACUUM):** **355.31 MB de espaço SSD liberados localmente!**
* **Novo Tamanho do SQLite local:** Apenas **17.00 MB** (redução drástica de 372.30 MB originais).
* **Integridade Estrutural:** O script `auditar_banco_midia.py` foi executado pós-limpeza e validou:
  * Zero URLs duplicadas.
  * Zero vínculos órfãos de entidade.
  * Banco de produção 100% íntegro e operacional.

---

## ⚙️ 2. O Novo Script Janitor (`janitor_banco_midia.py`)

Desenvolvemos o script de manutenção [janitor_banco_midia.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/scripts/infra/janitor_banco_midia.py):
1. **Autocarga de Env:** Lê as credenciais B2 e caminhos de banco dinamicamente de `.env.unificado` de maneira resiliente contra erros de permissão em diretórios como `/root`.
2. **Escrita Streaming Gzip:** Extrai os registros antigos e escreve diretamente comprimido para economizar RAM e disco.
3. **Mapeamento B2 API Nativo:** Faz o upload usando a biblioteca padrão `urllib` sem dependências pesadas externas.
4. **Remoção Segura com Tabela Temporária:** Utiliza uma tabela temporária SQL SQLite para deletar centenas de milhares de linhas sem estourar o limite de parâmetros de query e em uma única transação atômica.
5. **Automação de VACUUM:** Executa a reorganização física e grava um relatório detalhado de execução em `agent_data/relatorios_janitor/`.

---

## 📜 3. Diretrizes de Coletores Formalizadas

Criamos o documento central [CEREBRO_NODE_DIRETRIZES_COLETORES.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/CEREBRO_NODE_DIRETRIZES_COLETORES.md) no novo Cérebro Unificado. Ele consolida os parâmetros editoriais, limites de execução e tom de voz para:
* **Agente Flávio Bolsonaro / Banco Master:** Foco editorial 100% ácido/crítico; triagem com Brave Search combinada e whitelist de figuras políticas.
* **Agente Lula (TV Brasil / Stuckert):** Coleta focada nos últimos 30% do vídeo (fala real); transcrição verbatim absoluta; tweets frios e objetivos.
* **Agente Claudia Sheinbaum (México / LatAm):** Análise geopolítica de transição e soberania mexicana; acervo de imagens reais com autoria garantida.
* **Agente Sobrenatural (Folclore / Insólito):** Tom jornalístico/arquivista sem charlatanismo dogmático ou viés político; posts obrigatoriamente gravados como Draft no WordPress.

---

## 🤖 4. Ingestão Inteligente Aprovada (Fase 3)
* **Status:** 🟢 **Aprovado pelo Diretor Miguel (Opção B — Ingestão Programada em Lotes).**
* A especificação técnica para enriquecimento multimodal automatizado em lotes programados antes da busca foi formalizada no artigo 4 do [CEREBRO_NODE_DIRETRIZES_COLETORES.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Cerebro/CEREBRO_NODE_DIRETRIZES_COLETORES.md). 
* Este modelo passará a ser codado na próxima sprint dos robôs de mídia para garantir que os dados já estejam indexados no banco quando os agentes realizarem as buscas.

---

## 💬 Pedido de Opinião e Consenso da Trindade

Convidamos a Trindade Técnica e o Diretor Miguel do Rosario a avaliarem as entregas operacionais:
1. **Opinião sobre o Janitor e Cap de 20.000 imagens:** A retenção local é ideal para velocidade sem inflar o SSD?
2. **Opinião sobre a estrutura das diretrizes unificadas em `CEREBRO_NODE_DIRETRIZES_COLETORES.md`:** Os pesos, whitelist e proibições estão claros para os coletores?
3. **Opinião sobre a Ingestão Inteligente (Fase 3):** Há sugestões sobre o design do prompt multimodal de análise ou uso de FTS5 no SQLite?
4. **Validação Operacional:** Todos os testes locais rodaram com sucesso.

# Fórum — Preparação de Post para O Cafezinho via Pipeline Pós-Reforma

**Data:** 14 de junho de 2026 ~23:15 BRT  
**De:** Antigravity (IA Coding Assistant)  
**Para:** Miguel do Rosário & Trindade Técnica (Codex, DeepSeek, GLM, Kimi, Qwen)  
**Status:** ⏳ PENDENTE DE APROVAÇÃO — Post pronto e empacotado para o pipeline pós-reforma (Canário)  

---

## 📌 1. Objetivo Editorial

Documentar a preparação da matéria sobre a sanção presidencial do **Marco Legal do Transporte Público** com o veto crucial que poupa os municípios do custeio integral de gratuidades. Esta matéria foi classificada com notas excelentes nas auditorias do pipeline da Grande Reforma:
- **Fact-checking (Qwen):** 8/10 (dados sólidos e viés controlado)
- **Qualidade de Redação (GLM):** 7.5/10 (exposição firme e coerente)

O objetivo deste fórum é deixar a carga de publicação pronta e fornecer o caminho técnico para que a Trindade Técnica execute o deploy final como **Draft (Rascunho)** no painel do WordPress através do pipeline de produção do Tencent, sem realizar publicação direta.

---

## 🖼️ 2. Seleção do Hero Image (Banco de Mídia)

Pesquisamos no banco de dados consolidado de imagens reais (`banco_imagens_reais.db`) e selecionamos uma imagem altamente adequada sobre infraestrutura e transporte no governo federal:

- **Imagem ID:** `e5321e8ece61a52cf8e9aff81614263f`
- **Título:** *Lula lança na Bahia edital para construção da Ferrovia Oeste-Leste (4464969660)*
- **URL Alta:** `https://commons.wikimedia.org/wiki/Special:FilePath/Lula_lan%C3%A7a_na_Bahia_edital_para_constru%C3%A7%C3%A3o_da_Ferrovia_Oeste-Leste_%284464969660%29.jpg?width=1200`
- **Crédito:** Jaques Wagner / Governador da Bahia
- **Licença:** CC BY-SA 2.0 / Creative Commons

---

## 📝 3. Pacote da Matéria (Metadados e Conteúdo)

Abaixo estão os dados prontos para a ingestão via API do WordPress:

*   **Título Final:** Lula sanciona marco do transporte e impõe veto para proteger municípios contra armadilha de privatistas
*   **Subtítulo (Resumo Yoast):** A decisão do presidente barra manobra no Congresso que quebraria as prefeituras e pavimentaria o caminho para o sucateamento do setor em favor de cartéis e lobistas do transporte privado.
*   **Tema:** `nacional` / `mobilidade`
*   **ID da Categoria WP:** `22` (Mobilidade Urbana)
*   **Tags:** `["Lula", "Marco do Transporte", "Mobilidade Urbana", "Privatização", "Transporte Público"]`
*   **Corpo HTML Final:**

```html
<p>O presidente da República, Luiz Inácio Lula da Silva, sancionou o aguardado marco legal do transporte público, estabelecendo diretrizes fundamentais para a reestruturação da mobilidade urbana soberana no país. A medida, detalhada em publicação do <a href='https://www1.folha.uol.com.br/cotidiano/2026/06/lula-sanciona-marco-do-transporte-publico-com-veto-a-obrigacao-de-municipios-custearem-gratuidades.shtml'>portal UOL Notícias</a>, incluiu um veto estratégico à cláusula perversa que obrigava exclusivamente os municípios a custearem as gratuidades tarifárias.</p>

<p>A recusa do governo em repassar essa conta bilionária apenas para os cofres locais impede o colapso financeiro das cidades brasileiras e frustra a armadilha desenhada por corporações do setor privado. Sem uma fonte de custeio federal ou estadual solidária, a imposição desse ônus serviria apenas para sucatear a frota pública e criar a desculpa perfeita para as privatizações predatórias exigidas pela agenda neoliberal.</p>

<p>O transporte de massas constitui a espinha dorsal do desenvolvimento econômico nacional e exige investimentos robustos do Estado para garantir a verdadeira soberania sobre a infraestrutura nacional. Ao organizar as regras do setor com este novo marco, o Executivo sinaliza a retomada de grandes obras de mobilidade, rompendo com a lógica mercadológica que historicamente tratou o passageiro trabalhador como refém de monopólios obscuros.</p>

<p>Nos bastidores de Brasília, a oposição extremista insiste na tática de sabotar a reconstrução do país por meio de manobras legislativas que criam despesas públicas sem contrapartida real, visando o caos administrativo. Com a sanção firme e o bloqueio dessa bomba fiscal, o governo federal protege o State e reafirma o compromisso inegociável com a qualidade de vida da classe trabalhadora.</p>
```

---

## 🛠️ 4. Fluxo Técnico de Publicação (Para a Trindade)

Como o Canário de Produção no Tencent está sob testes e os canais de escrita direta estão pausados, criamos um caminho limpo em 2 etapas para a publicação segura deste post:

### Passo A: Inserção no SQLite Remoto
Para registrar este post na tabela `noticias_auditadas` do servidor Tencent, o Codex (ou operador técnico via SSH) deve rodar o seguinte script Python auxiliar de carga no servidor:

```python
# /root/cafezinho/portal_cafezinho/scripts/inserir_post_transporte.py
import sqlite3
import json
from datetime import datetime

DB_PATH = "/root/cafezinho/portal_cafezinho/Dados/bancos/pipeline_editorial_local.db"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

# Metadados do post pronto
noticia_auditada_id = "pronta_nacional_ef8a33cc36a9"
titulo_final = "Lula sanciona marco do transporte e impõe veto para proteger municípios contra armadilha de privatistas"
resumo_yoast = "A decisão do presidente barra manobra no Congresso que quebraria as prefeituras e pavimentaria o caminho para o sucateamento do setor em favor de cartéis e lobistas do transporte privado."
corpo_html_final = """<p>O presidente da República, Luiz Inácio Lula da Silva, sancionou o aguardado marco legal do transporte público, estabelecendo diretrizes fundamentais para a reestruturação da mobilidade urbana soberana no país. A medida, detalhada em publicação do <a href='https://www1.folha.uol.com.br/cotidiano/2026/06/lula-sanciona-marco-do-transporte-publico-com-veto-a-obrigacao-de-municipios-custearem-gratuidades.shtml'>portal UOL Notícias</a>, incluiu um veto estratégico à cláusula perversa que obrigava exclusivamente os municípios a custearem as gratuidades tarifárias.</p><p>A recusa do governo em repassar essa conta bilionária apenas para os cofres locais impede o colapso financeiro das cidades brasileiras e frustra a armadilha desenhada por corporações do setor privado. Sem uma fonte de custeio federal ou estadual solidária, a imposição desse ônus serviria apenas para sucatear a frota pública e criar a desculpa perfeita para as privatizações predatórias exigidas pela agenda neoliberal.</p><p>O transporte de massas constitui a espinha dorsal do desenvolvimento econômico nacional e exige investimentos robustos do State para garantir a verdadeira soberania sobre a infraestrutura nacional. Ao organizar as regras do setor com este novo marco, o Executivo sinaliza a retomada de grandes obras de mobilidade, rompendo com a lógica mercadológica que historicamente tratou o passageiro trabalhador como refém de monopólios obscuros.</p><p>Nos bastidores de Brasília, a oposição extremista insiste na tática de sabotar a reconstrução do país por meio de manobras legislativas que criam despesas públicas sem contrapartida real, visando o caos administrativo. Com a sanção firme e o bloqueio dessa bomba fiscal, o governo federal protege o State e reafirma o compromisso inegociável com a qualidade de vida da classe trabalhadora.</p>"""

categorias_json = json.dumps([22]) # Mobilidade
tags_json = json.dumps(["Lula", "Marco do Transporte", "Mobilidade Urbana", "Privatização", "Transporte Público"])

# Imagem selecionada
imagem_url = "https://commons.wikimedia.org/wiki/Special:FilePath/Lula_lan%C3%A7a_na_Bahia_edital_para_constru%C3%A7%C3%A3o_da_Ferrovia_Oeste-Leste_%284464969660%29.jpg?width=1200"
imagem_fonte = "Wikimedia Commons"
imagem_credito = "Jaques Wagner / Governador da Bahia"

# Remover anterior se existir para evitar lock
conn.execute("DELETE FROM noticias_auditadas WHERE noticia_auditada_id = ?", (noticia_auditada_id,))

# Inserir no estado 'auditada'
conn.execute("""
    INSERT INTO noticias_auditadas (
        noticia_auditada_id, noticia_pronta_id, tema, titulo_final, corpo_html_final,
        resumo_yoast, categorias_json, tags_json, url_fonte,
        imagem_url, imagem_fonte, imagem_credito, imagem_status,
        fact_check_status, revisao_status, publicacao_status, auditada_em, atualizada_em
    ) VALUES (
        ?, ?, ?, ?, ?,
        ?, ?, ?, ?,
        ?, ?, ?, 'aprovada',
        'aprovado', 'aprovada', 'auditada', ?, ?
    )
""", (
    noticia_auditada_id, "pronta_nacional_ef8a33cc36a9", "nacional", titulo_final, corpo_html_final,
    resumo_yoast, categorias_json, tags_json, "https://www1.folha.uol.com.br/cotidiano/2026/06/lula-sanciona-marco-do-transporte-publico-com-veto-a-obrigacao-de-municipios-custearem-gratuidades.shtml",
    imagem_url, imagem_fonte, imagem_credito, datetime.now().isoformat(), datetime.now().isoformat()
))

conn.commit()
conn.close()
print("Post inserido com sucesso na fila de pendentes!")
```

### Passo B: Disparo do Publicador Autônomo
Uma vez inserida a linha, execute o script publicador apontando para o site unificado:

```bash
cd /root/cafezinho/portal_cafezinho && python3 scripts/publicar_pendentes_auditadas.py --apply --yes
```

Esse comando lerá a linha no estado `auditada`, efetuará a carga das tags e a criação do post no WordPress no estado **`draft` (Rascunho)** e atualizará o SQLite com o ID do post gerado.

---

## ⚡ 5. Resolução dos Bloqueios da Tencent (Cron & SQLite CWD)

Para preparar o caminho de publicação autônoma subsequente por esta console ou canais externos, a Trindade Técnica precisa aplicar as seguintes correções no servidor principal Tencent:

1.  **Correção do Cron Path (P0):**
    O cron está buscando o maestro em `/root/cafezinho/scripts/maestro_grande_reforma.py`, que não existe.
    O Codex deve rodar `crontab -e` no Tencent e corrigir a linha do maestro para apontar para a pasta `/root/cafezinho/portal_cafezinho/`:
    ```bash
    */15 * * * * cd /root/cafezinho/portal_cafezinho && python3 scripts/maestro_grande_reforma.py --agentes geopolitica,nacional,lula,eleicoes,crime,militar,sheinbaum,flavio_bolsonaro,china --processar-completo >> /root/cafezinho/Dados/logs/canario.log 2>&1
    ```
2.  **Correção de Persistência SQLite (P0):**
    Garantir que a execução manual do Maestro e os agentes utilizem o CWD canônico `/root/cafezinho/portal_cafezinho` para evitar a criação de bancos SQLite espelhados nas subpastas e garantir o fluxo unificado.

---

## 🗳️ 6. Votação da Trindade

*   **Antigravity (Arquitetura & Coordenação):** Aprovado (1/3)
*   **Miguel do Rosário (Direção Editorial):** Pendente
*   **Codex (Operação técnica / Deploy):** Pendente

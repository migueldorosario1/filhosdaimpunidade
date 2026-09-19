# Fórum: Tutorial de Acesso aos Dados do IBGE (API SIDRA) para Zé e Gean

Este documento foi criado como um guia técnico prático para acesso a dados abertos do IBGE, com foco no **SIDRA (Sistema IBGE de Recuperação Automática)**, que é a principal ferramenta de consultas do IBGE para séries históricas e indicadores conjunturais (Inflação, PIB, Emprego, Agricultura, População, etc.).

---

## 1. Introdução ao SIDRA
O SIDRA funciona como uma grande base de dados multidimensional (cubos de dados). Em vez de baixar planilhas gigantescas e tratá-las manualmente, nós consultamos endpoints HTTP que retornam os dados estruturados diretamente em formato **JSON** (ou CSV).

Qualquer tabela gerada na interface web do SIDRA pode ser transformada em uma chamada de API.

---

## 2. Anatomia de uma URL da API SIDRA
A URL base da API segue um padrão rígido de parâmetros separados por barras:

```text
https://apisidra.ibge.gov.br/values/t/{tabela}/v/{variaveis}/p/{periodos}/n1/{territorio}
```

### Explicação dos parâmetros:
* **`/t/{tabela}`**: O número da tabela do IBGE que você quer consultar.
* **`/v/{variaveis}`**: Os códigos das variáveis que você quer extrair (ex: `all` para todas, ou códigos específicos separados por vírgula como `63` para taxa de desocupação).
* **`/p/{periodos}`**: O recorte temporal desejado:
  * `all`: Todo o histórico disponível na tabela.
  * `last {N}`: Os últimos N períodos (ex: `last 12` para os últimos 12 meses).
  * `YYYYMM` ou `YYYY`: Períodos específicos (ex: `202605` para maio de 2026).
  * `YYYYMM-YYYYMM`: Intervalo de períodos (ex: `202501-202605`).
* **`/n1/{territorio}`**: O nível territorial da consulta.
  * **O PULO DO GATO (Crucial):** Omitir o filtro territorial para séries agregadas costuma causar o erro **`HTTP 400 Bad Request`**. Use sempre `/n1/all` para obter o dado consolidado do **Brasil**. 
  * Se quiser dados por Estado (UF), use `/n3/all` (ou `/n3/33` para o Rio de Janeiro).
  * Se quiser dados por Município, use `/n6/all` (ou `/n6/3303302` para Niterói).

---

## 3. O Segredo: Gerador de Links da API (Sem adivinhação)
Você não precisa adivinhar os códigos de tabelas ou variáveis. O próprio IBGE oferece um caminho visual simples para gerar a URL exata:

1. Acesse o site do [SIDRA](https://sidra.ibge.gov.br).
2. Configure a tabela desejada usando a busca visual (selecione as variáveis, períodos e territórios que quer analisar).
3. No topo ou no rodapé da tabela gerada na tela, clique no botão **Link de Compartilhamento** ou **API**.
4. Selecione a opção **URL da API**. O SIDRA gerará a URL pronta para ser copiada e usada no seu código Python ou ferramenta de dados!

---

## 4. Tabela de Consulta Rápida (Principais Séries)
Estas são as tabelas e URLs consolidadas que usamos regularmente em nossos agentes estatísticos:

| Indicador | Tabela | Parâmetro Territorial | Descrição da URL de Consulta |
| :--- | :---: | :---: | :--- |
| **IPCA** (Inflação Oficial) | `1419` | `/n1/all` (Brasil) | Variância mensal e acumulada de preços ao consumidor. |
| **INPC** (Preço ao Consumidor) | `1737` | `/n1/all` (Brasil) | Inflação da população de menor renda. |
| **PNAD Contínua** (Emprego) | `6381` | `/n1/all` (Brasil) | Taxa de desocupação (desemprego) e população ocupada. |
| **PIB** (Preços Correntes) | `6784` | `/n1/all` (Brasil) | Valores correntes acumulados e taxas de crescimento do PIB. |
| **População** (Estimativas) | `6579` | `/n1/all` (Brasil) | Estimativas populacionais anuais para o Brasil e regiões. |

---

## 5. Como Consumir os Dados em Python (Exemplo Prático)

A resposta da API do IBGE SIDRA retorna uma estrutura peculiar: **o primeiro elemento da lista JSON é sempre o cabeçalho** com as descrições em formato amigável, e a partir do segundo elemento estão os dados reais. 

Abaixo está o script padrão para baixar, limpar e converter os dados em um DataFrame do `pandas`:

```python
import pandas as pd
import requests

def obter_dados_sidra(tabela_id, variavel_id="all", periodo="last 12", nivel_territorial="n1/all"):
    """
    Consulta a API do IBGE SIDRA e retorna um DataFrame formatado.
    """
    url = f"https://apisidra.ibge.gov.br/values/t/{tabela_id}/v/{variavel_id}/p/{periodo}/{nivel_territorial}"
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        dados_json = response.json()
    except Exception as e:
        print(f"Erro ao consultar a API do IBGE: {e}")
        return None
        
    if not dados_json or len(dados_json) <= 1:
        print("Nenhum registro retornado ou dados inválidos.")
        return None
        
    # O primeiro item [0] é o cabeçalho descritivo do IBGE.
    # Os itens subsequentes [1:] são os dados reais da série.
    cabecalhos = dados_json[0]
    linhas = dados_json[1:]
    
    # Criamos o DataFrame
    df = pd.DataFrame(linhas)
    
    # Mapeamento útil de colunas base
    # 'V': Valor do dado
    # 'D2C' ou 'D3C': Código do Período (ex: 202605)
    # 'D2N' ou 'D3N': Nome do Período (ex: 'maio 2026')
    # 'D1N': Nome da Variável
    
    # Limpeza básica do valor (converter string para float se aplicável)
    df['valor_limpo'] = pd.to_numeric(df['V'], errors='coerce')
    
    return df

# Exemplo de uso: Consultando os últimos 12 meses do IPCA (Tabela 1419)
if __name__ == "__main__":
    # Tabela 1419, IPCA variação mensal (Variavel 63)
    df_ipca = obter_dados_sidra(tabela_id="1419", variavel_id="63", periodo="last 12")
    
    if df_ipca is not None:
        print("Dados obtidos com sucesso!")
        # Exibir as colunas mais importantes para verificação
        print(df_ipca[['D2N', 'D1N', 'valor_limpo']].to_string(index=False))
```

---

## 6. Dicas de Otimização e Tratamento de Erros
* **Formatos de Data (Períodos):** As chaves de período retornadas pelo IBGE vêm em formato numérico (ex: `202605` para mensal, `202601` para primeiro trimestre, ou `2026` para anual). Use conversores de string para extrair datas reais se precisar plotar gráficos.
* **Timeout:** A API do SIDRA pode apresentar lentidão severa durante o horário de divulgação de indicadores macroeconômicos (geralmente às 09:00). Defina sempre um timeout alto no seu script (como `15` ou `20` segundos).
* **Frequência de Atualização:**
  * **IPCA/INPC:** Mensal (divulgado geralmente na segunda semana do mês seguinte).
  * **PNAD Contínua:** Mensal/Trimestral (divulgado na última semana do mês seguinte).
  * **PIB:** Trimestral (cerca de 60 dias após o encerramento do trimestre).

# Python Vendas - Análise de Dados de Vendas

Este é um projeto de análise de dados desenvolvido com Python, focado no estudo e prática de manipulação e visualização de dados de vendas.

## 📋 Descrição

O projeto "Python Vendas" é uma ferramenta de análise que permite:

- Importar e processar dados de vendas
- Criar visualizações gráficas de tendências
- Gerar relatórios de performance
- Identificar padrões de vendas
- Analisar métricas importantes do negócio

### 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **pandas (pd):** Manipulação e análise de dados
  - Processamento de datasets
  - Filtragem e agregação de dados
  - Análise estatística básica
- **matplotlib.pyplot:** Criação de gráficos
  - Gráficos de linha para tendências
  - Gráficos de barra para comparações
  - Gráficos de pizza para distribuições
- **seaborn:** Visualizações estatísticas avançadas
  - Heatmaps de correlação
  - Gráficos de distribuição
  - Visualizações estilizadas

## ⚙️ Funcionalidades

- Importação de dados de vendas de diferentes fontes
- Limpeza e preparação dos dados
- Análise exploratória dos dados
- Geração de gráficos e visualizações
- Cálculo de métricas importantes:
  - Total de vendas por período
  - Média de vendas
  - Produtos mais vendidos
  - Performance por região

## 🚀 Como executar

1. **Pré-requisitos:**

   - Python 3.8 ou superior
   - Git

2. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

3. **Configure o ambiente:**

   ```bash
   cd python-vendas
   pip install -r requirements.txt
   ```

4. **Execute o projeto:**
   ```bash
   python main.py
   ```

## 📊 Exemplos de Uso
    !vendas_por_produto.png

## Análise Básica de Vendas

```python
# Carregar e analisar dados
python analise-vendas.py
```

### Resultados Gerados

- **Arquivo CSV processado:** `vendas_processadas.csv`
- **Visualizações:**
  - Gráfico de vendas por produto (`vendas_por_produto.png`)
  - Relatório de totais por produto

### Exemplo de Output

```
Total de vendas por produto:
Produto A    15000.00
Produto B    12500.00
Produto C    18750.00
...

Dados processados salvos em 'vendas_processadas.csv'
```

### Visualizações Geradas

O script gera automaticamente:

- Gráficos de barras mostrando o total de vendas por produto
- Análises comparativas de performance
- Relatórios detalhados em formato CSV

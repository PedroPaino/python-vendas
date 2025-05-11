import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_csv('vendas.csv')

# 2. Criar coluna 'Total_Venda'
df['Total_Venda'] = df['Quantidade'] * df['Preco_Unitario']

# 3. Análise por produto
total_por_produto = df.groupby('Produto')['Total_Venda'].sum()
print("\nTotal de vendas por produto:")
print(total_por_produto)

# 4. Gráfico de barras (vendas por produto)
sns.barplot(x='Produto', y='Total_Venda', data=df, estimator=sum)
plt.title('Total de Vendas por Produto')
plt.savefig('vendas_por_produto.png')  # Salva o gráfico
plt.show()

# 5. Exportar resultados para CSV
df.to_csv('vendas_processadas.csv', index=False)
print("\nDados processados salvos em 'vendas_processadas.csv'")
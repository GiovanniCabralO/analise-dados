import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

print("\n📊 Dados Carregados:")
print(dados)

dados['Total'] = dados['Quantidade'] * dados['Preco']
print("\n💰 Total de vendas por produto:")
print(dados[['Produto', 'Total']])

soma_total = dados['Total'].sum()
print(f"\n🔢 Soma total das vendas: R$ {soma_total}")

media_preco = dados['Preco'].mean()
print(f"📈 Média dos preços dos produtos: R$ {media_preco:.2f}")

plt.bar(dados['Produto'], dados['Total'])
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total (R$)')
plt.tight_layout()
plt.savefig('grafico_vendas.png')
plt.show()

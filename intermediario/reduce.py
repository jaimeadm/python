# reduce - reduzir um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 5', 'preco': 105.50},
    {'nome': 'Produto 3', 'preco': 20.33},
    {'nome': 'Produto 2', 'preco': 53.22},
    {'nome': 'Produto 4', 'preco': 39.90},
]

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    lambda acumulador, p: acumulador + p['preco'],
    produtos,
    0
)

print('Total:', total)

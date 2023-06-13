import copy
from dados import produtos

print(*produtos, sep='\n')
print()

# novos_produtos com deep copy e com aumento de 10%
novos_produtos = [
    {**produto, 'preco': ((10 / 100) * produto['preco']) + produto['preco']}
    for produto in copy.deepcopy(produtos)
]
print(*novos_produtos, sep='\n')
print()

# ordenar descrecente com deep copy
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
print(*produtos_ordenados_por_nome, sep='\n')
print()

# ordenar por preço crescente com deep copy
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco'],
)
print(*produtos_ordenados_por_preco, sep='\n')

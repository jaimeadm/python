def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 69.90},
    {'nome': 'Produto 3', 'preco': 32.15},
]

def filtrar_preco(produto):
    return produto['preco'] > 10

#novos_produtos = [
#    p for p in produtos
#    if p['preco'] > 10
#]

novos_produtos = filter(
    #lambda p: p['preco'] > 10,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

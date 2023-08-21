import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=50)

#print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
#print(lista)

# Mapeamento de dados com list comprehension
produtos = [
    {'nome': 'Produto1', 'preco': 10},
    {'nome': 'Produto2', 'preco': 20},
    {'nome': 'Produto3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] >= 20 else {**produto}
    for produto in produtos
]

p(novos_produtos)

print('\n\n')

lista = [n for n in range(10) if n < 5]
print(lista)

print('\n\n')

lista = [
    #[(x, letra) for letra in 'Fulano]
    (x, y)
    for x in range(3) # letra
    for y in range(3)
]
print(lista)
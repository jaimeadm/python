from itertools import zip_longest
# Somar 2 listas
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [10, 20, 30, 40]

lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)

# Outra solução
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)

# Outra solução
#lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)
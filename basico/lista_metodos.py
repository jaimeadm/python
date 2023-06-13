"""
Listas em Python
Tipo list - Mutável
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Fulano')
nome = lista.pop()
lista.append(50)
del lista[2]
lista.insert(100, 5)
print(lista)

print('-------------------------')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)

print('-------------------------')

nova_lista = ['Fulano', 'Ciclano', 'Beltrano']
indices = range(len(nova_lista))

for indice in indices:
    print(indice, nova_lista[indice], type(nova_lista[indice]))

# Desempacotamento + tuplas
# Tipo tuple - uma lista imutável
# enumerate - enumera iteráveis (índices)

print('-------------------------')

_, _, nome, *resto = ['Nome 1', 'Nome 2', 'Nome 3']
print(nome)

nomes = 'Valor 1', 'Valor 2', 'Valor 3'
#nomes = ('Valor 1', 'Valor 2', 'Valor 3')
nomes = tuple(nomes)
nomes = list(nomes)
#nomes[1] = 'Novo Valor'
print(nomes)

cidades = ['Vancouver', 'Nova York', 'São Paulo']
#cidades_enumeradas = list(enumerate(cidades))
#print(cidades_enumeradas)
for indice, nome in enumerate(cidades):
    print(indice, nome)
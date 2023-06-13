"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [54, True, 'Fulano Ciclano', 72.5, []]

print(lista[2].upper(), type(lista[2]))

lista_array = [10, 20, 30, 40]
lista_array[2] = 35
#del lista_array[2]
lista_array.append(50)
lista_array.append(60)
lista_array.append(70)
ultimo_valor = lista_array.pop(4) # remover último da lista ou no índice especificado

print(lista_array, 'Removido:', ultimo_valor)
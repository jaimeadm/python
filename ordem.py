lista = [4, 32, 1, 5, 4, 4, 9, 10]
list_dic = [
    {'nome': 'Fulano', 'sobrenome': 'da Silva'},
    {'nome': 'Ciclano', 'sobrenome': 'Santos'},
    {'nome': 'Beltrano', 'sobrenome': 'Ribeiro'},
    {'nome': 'Elano', 'sobrenome': 'Magalhães'},
    {'nome': 'Mezano', 'sobrenome': 'Oliveira'},
    {'nome': 'Alano', 'sobrenome': 'Farias'},
]

def exibir(lista):
    for item in lista:
        print(item)

lista1 = sorted(list_dic, key=lambda item: item['nome'])
lista2 = sorted(list_dic, key=lambda item: item['sobrenome'])

exibir(lista1)
print()
exibir(lista2)

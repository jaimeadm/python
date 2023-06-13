lista = [4, 32, 1, 5, 4, 4, 9, 10]
dicionario = [
    {'nome': 'Fulano', 'sobrenome': 'da Silva'},
    {'nome': 'Ciclano', 'sobrenome': 'Santos'},
    {'nome': 'Beltrano', 'sobrenome': 'Ribeiro'},
    {'nome': 'Elano', 'sobrenome': 'Magalhães'},
    {'nome': 'Mezano', 'sobrenome': 'Oliveira'},
    {'nome': 'Alano', 'sobrenome': 'Farias'},
]

#lista.sort(reverse=True)
#print(lista)
#sorted(lista)

def ordenar(item):
    return item['nome']

# dicionario.sort(key=ordenar) # com a função ordenar
dicionario.sort(key=lambda item: item['nome']) # com lambda

for item in dicionario:
    print(item)

print('\n\n\n')

# Exemplo
def exibir(dicionario):
    for item in dicionario:
        print(item)
    print()

l1 = sorted(dicionario, key=lambda item: item['nome'])
l2 = sorted(dicionario, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
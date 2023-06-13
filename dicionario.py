"""
Dicionário
"""

pessoa = {
    'Nome': 'Fulano',
    'Idade': 35,
    'Endereços': [
        {'rua': 'xyz', 'numero': 11},
        {'rua': 'abc', 'numero': 10}
    ]
}

print(pessoa, type(pessoa))
print(pessoa['Nome'])

for chave in pessoa:
    print(chave, pessoa[chave])

print('\n\n')

carro = {}
carro['modelo'] = 'BMW'
carro['cor'] = 'Azul'
print(carro['modelo'])
print(carro)
del carro['cor']
print(carro)

if carro.get('cor') is None:
    print('Chave cor não existe')
else:
    print(carro['cor'])

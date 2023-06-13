lista = ['Fulano', 'Ciclano', 25, 1.65, 'Beltrano']
p, b, *_, u = lista

print(p, u)
print(lista)
print(*lista)

print('\n\n')

salas = [
    [1, 'Maria'],
    [2, 'João'],
    [3, 'Claudio', 'Ricardo', 'Aline'],
]

#print(*salas)
print(*salas, sep='\n')
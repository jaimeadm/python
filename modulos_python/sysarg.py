import sys

print(sys.argv)
argumentos = sys.argv
qtd_argumentos = len(argumentos)
print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('Nenhum argumento passado')
else:
    print(f'Você passou os argumentos {argumentos[1:]}')

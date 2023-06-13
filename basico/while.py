"""
while: executa uma ação enquanto uma condição for verdadeira

Operadores de atribuição
= += -= *= /= //= **= %=
"""
condicao = True
while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é: {nome}')

    if nome == 'sair':
        break

# Comentario
contador = 0

while contador <= 10:
    contador = contador + 1
    #contador += 1

    if contador == 5:
        print('Não mostrar o', contador)
        continue

    print(contador)

    if contador == 8:
        break

print('Concluído')
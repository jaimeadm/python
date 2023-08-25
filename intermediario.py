# def somar(x, y):
#     print(x + y)

# def saudacao(nome=''):
#     print(f'Olá {nome}!')

# def dividir(x, y):
#     calculo = x / y
#     print(int(calculo))

# somar(3, 4) # argumentos não nomeados (posicionais)
# somar(y=3, x=7) # argumentos nomeados
# dividir(x=10, y=2)
# saudacao('Fulano')

# NoneType
# def multiplicar(x, y, z=None):
#     if z is None:       # is not None
#         print(x * y)
#     else:
#         print((x * y) * z)

# multiplicar(3, 2, 4)

# Escopo da função
# valor = 5
# nome = 'Fulano'
# def mostrar():
#     global valor # prática ruim de programação
#     valor = 100
#     def mostrar_interna():
#         valor = 200
#         print(f'Interno: {valor} {nome}')
#     mostrar_interna()
#     print(f'Externo: {valor}')

# print(f'Antes da função: {valor}')              # 5
# mostrar()                                       # 200 | 100       
# print(f'Depois da função (global): {valor}')    # 100 (global)

def multiplicar(x, y):
    return x * y

valor1 = multiplicar(2, 3)  # 6
valor2 = multiplicar(4, 5)  # 20
print(valor1 + valor2)      # 26
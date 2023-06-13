"""
Operação Ternária
"""
condicao = 10 == 11
valor = 'Imprime Sim' if condicao else 'Imprime Não'
print(valor)

print('\n')

# a if condição else b
x = 2
print(f'{x=}') if x == 2 else print(f'x não é 2')

print('\n')

y = 5
print(f'O número {y=} é par') if y % 2 == 0 else print(f'O número {y=} é ímpar')

print('\n')

# Pular de 2 em 2
pulador = range(100, 110)
for pular in pulador:

    # If ternário
    print(f'{pular=} é par') if pular % 2 == 0 else print(f'{pular=} é ímpar')
    # OU
    if pular % 2 == 0:
        print(f'{pular=} é par')
    elif pular %2 != 0:
        print(f'{pular=} é ímpar')
    else:
        ...

print(len(pulador))

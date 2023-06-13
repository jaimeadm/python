# Função para multiplicar argumentos
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplica = multiplicar(10, 2, 3, 4, 5)
print(multiplica)

# Função para saber se é ímpar ou par
def par_impar(numero):
    valor = numero % 2 == 0 
    if valor:
        return f'o número {numero} é par'
    return f'o número {numero} é ímpar'
    
print(par_impar(3))

# Função com:
# Higher Order Functions - Funções que podem receber e/ou retornar outras funções
# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
# Closure
def calcular(valor):
    def multiplicar(numero):
        return numero * valor
    return multiplicar

duplicar = calcular(2)
triplicar = calcular(3)
quadruplicar = calcular(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))

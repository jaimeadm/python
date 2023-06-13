def funcao():
    print('Bem Vindo - Primeira Função')

def saudacao(nome=' '):
    print(f'Olá {nome}')

funcao()
saudacao('Alan')

print('\n\n')

def somar(a, b):
    if a < b:
        print(f'{a=} + {b=} =', a + b)
    else:
        print(f'{a=} não é maior do que {b=}')

somar(10, 20)

print('\n\n')

# Valores Padrão
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} = ', x + y + z)
    else:
        print(f'{x=} {y=} = ', x + y)

soma(100, 101)      # x, y
soma(200, 201, 202) # x, y, z

print('\n\n')

# Função para listar cidades
def listar_cidades(cidades):
    for id, cidade in enumerate(cidades):
        print(id, '-', cidade)

# Chamar função
todas_cidades = ['Brasília', 'Amazonas', 'Paraná']
listar_cidades(todas_cidades)
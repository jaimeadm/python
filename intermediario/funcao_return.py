def somar(x, y):
    if x > 10 or y > 10:
        return 'x ou y são maiores que 10'
    return x + y

soma1 = somar(1, 2)
soma2 = somar(3, 4)
print(soma1 + soma2)

print(somar(11, 12))

print('\n\n')

# Argumentos não nomeados
#a, b, *resto = 1, 2, 3, 4 # tupla
#print(a, b, resto)

def calcular(*args): # empacotar em uma tupla
    total = 0
    for numero in args:
        total += numero
    return total

soma_numero = calcular(1, 2, 3, 4)
print(soma_numero)

numeros = 10, 20, 30, 40 # tupla
soma_nova = calcular(*numeros) # desempacotar a tupla (*numeros)
print(soma_nova)


print ('\n\n')

def saudacao(msg):
  return msg

mensagem = saudacao('Olá!')
print(mensagem)

### Exemplo

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

msg_dia = criar_saudacao('Bom Dia')
msg_noite = criar_saudacao('Boa Noite')
nomes = ['Fulano', 'Ciclano', 'Beltrano']

for nome in nomes:
    print(msg_dia(nome))
    print(msg_noite(nome))

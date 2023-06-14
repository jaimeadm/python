def saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}'
    return saudar

msg1 = saudacao('Bom dia')
print(msg1('Alan'))

############

def calcular(valor):
    def calculo_interno(numero):
        return valor * numero
    return calculo_interno

multiplica = calcular(2)
triplica = calcular(3)

print(multiplica(30))
print(triplica(10))


###########
print('\n\n\n')

# % de desconto de um preço
def criar_desconto(desconto):
    def total(preco):
        return preco - (preco * desconto)
    return total

desconto_10 = criar_desconto(0.1) # 10% de desconto
desconto_50 = criar_desconto(0.5) # 50% de desconto

print(desconto_10(50))
print(desconto_50(1000))

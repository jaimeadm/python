"""
while: executa uma ação enquanto uma condição for verdadeira

Operadores de atribuição
= += -= *= /= //= **= %=
"""

nome = 'Fulano Ciclano'
tamanho_nome = len(nome)
contador = 0

while contador <= (tamanho_nome - 1):
    print(f'{nome[contador]}')
    contador += 1
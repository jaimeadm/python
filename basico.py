# nome = 'Fulano'
# idade = 18
# maior_idade = idade > 17

# if maior_idade:
#     print('É maior de idade')
# else:
#     print('É menor de idade')

# print(10, 20, 30, sep="-", end="#\n")
# print('a', 'b', 'c')

# exponenciacao = 2 ** 10
# print(exponenciacao)

# modulo = 55 % 2 # resto da divisão
# print(modulo)

# divisao_inteira = 10 // 2.2 # retorna inteiro, corta as casas decimais
# print(divisao_inteira)

# """
# Ordem:
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# """
# print((1 + 1) ** (5 + 5))

# print('Fulano' * 10)
# print(3 * 'A')

# altura = 1.67
# peso = 70
# imc = peso / altura ** 2
# print(imc)

# nome = 'Fulano'
# idade = 19

# texto = f'{nome} tem {idade} anos'
# print(texto)
# valor = 1000.50
# preco = f'O valor é de {valor:,.2f}'
# print(preco)
# print(f'{imc:.2f}')

# a = 'A'
# b = 'B'
# c = 1.2
# string = '{} {} {:.2f}'
# string2 = '{valor1}, {valor2}, {valor3:.2f}'
# novastring = '{v1} {v2} {v3:.4f}'

# print(string.format(a, b, c))
# print(string2.format(valor1=a, valor2=b, valor3=c))
# print(novastring.format(v1=a, v2=b, v3=c))

# nome = 'Fulano'
# idade = 20
# peso = 69.5

# string = 'nome={arg1} idade={arg2} peso={arg3:.2f}'
# print(string.format(arg1=nome, arg2=idade, arg3=peso))

# nome = input('Qual seu nome? ')
# print(f'Seu nome é: {nome=}')

# nome = 'Alan'
# print('a' not in nome)

# nome = 'Fulano'
# preco = 105.90
# texto = 'Meu nome é %s e o preço é %.2f' % (nome, preco)
# print(texto)
# print('O hexadecimal de %i é %x' % (192, 192))

# valor = 195.556
# valor2 = 'NOME'
# print(f'{valor:.2f}')
# print(f'{valor2:>10}')
# print(f'## {valor2:^5} ##')

# valor = "Olá Mundo"
# print(f'{valor[4:]}') # Mundo
# print(valor[:3]) # Olá
# print(len(valor[:3])) # 3
# print(len(valor)) # 9
# print(valor[0:9:2]) # OàMno
# print(valor[::-1]) # odnuM álO

# num1 = input('Digite um número: ')
# num2 = input('Digite outro número: ')

# try:
#     val1 = int(num1)
#     val2 = int(num2)
#     print(f'A soma do {val1:.1f} com {val2:.1f} é {val1 + val2}')
# except:
#     print(f'{num1} ou {num2} não é um número')

# condicao = False
# passou_if = None

# if condicao:
#     passou_if = True
#     print('Fazer algo...')
# else:
#     print('Não fazer nada!')

# print(passou_if, passou_if is None)
# print(passou_if, passou_if is not None)

# if passou_if is None:
#     print('Não passou no if')
# elif passou_if is not None:
#     print('Passou no if')

# condicao = True
# while condicao:
#     nome = input("Digite seu nome: ")
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break

# contagem = 0
# while contagem <= 20:
    
#     contagem += 1

#     if contagem == 5:
#         print("Não mostrar o 5")
#         continue

#     if contagem >= 10 and contagem <= 15:
#         print('Não mostrar entre 10 e 15')
#         continue

#     print(contagem)

#     if contagem == 19:
#         break

# contador = 10
# contador /= 5
# print(f'{contador:.2f}')

# total_linhas = 5
# total_colunas = 5
# linha = 1

# while linha <= total_linhas:
#     #print(f'Linha: {linha}')
#     coluna = 1
#     while coluna <= total_colunas:
#         print(f'Linha: {linha} Coluna: {coluna}')
#         coluna += 1

#     linha += 1

# nome = 'alan magalhães'
# tamanho = len(nome)
# contador = 0
# novo_nome = ''

# while contador < tamanho:
#     print(f'{contador} - {nome[contador].capitalize()}') # .title()
#     novo_nome += (nome[contador] + '-')
#     contador += 1

# print(f'{novo_nome} \n')

# texto = 'Mensagem de Voz'
# novo_texto = ''
# for letra in texto:
#     print(f'{letra}')
#     novo_texto += letra + '*'

# print(f'*{novo_texto}')

# import os
# palavra_secreta = 'felicidade'
# numero_tentativas = 0
# letras_acertadas = ''

# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra')
#         continue
    
#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)
    
#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0

# lista = ['Fulano', 32, 1.70, 65, 'Analista de Sistema']
# print(lista)
# del lista[0]
# print(lista)
# lista.append('Masculino')
# print(lista)
# lista.insert(5, f'{3.850:,.3f}')
# print(lista)
# lista.pop(3)
# #lista.clear()
# print(lista)
# lista.extend([50, 'Casa', 'Carro'])
# print(lista)

# Dados mútaveis apontam para o mesmo valor na memória
# lista1 = [50, 60, 70]
# lista2 = lista1.copy()
# lista1[0] = 500
# print(lista1, lista2)

# lista = ['Fulano', 'Ciclano', 'Beltrano']
# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice])

# _, nome, *resto = ['a', 'b', 'c']
# print(resto) # ['c']

# valores = [10, 20, 30]
# val1, *restante = valores
# print(val1) # 10

# valores, valores2 = [1, 2, 3], (1, 2, 3)
# print(tuple(valores), list(valores2))

# lista = [10, 20 ,30]
# lista_indices = enumerate(lista)
# print(lista_indices)
# for indice in lista_indices:
#     print(indice)

# valores = ['A', 'B', 'C']
# for indice, letra in enumerate(valores):
#     print(f'{indice} - {letra}') # 0 - A

# indices = enumerate(valores)
# for indice in indices:
#     print(indice) # (0, 'A')
#     for i in indice:
#         print(f'\t{i}')

# lista = []
# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
#     if opcao == 'i':    # inserir
#         valor = input('Digite um valor para inserir: ')
#         lista.append(valor)
#         print()
#     elif opcao == 'a':  # apagar
#         valor = input('Selecione um índice para remover: ')
#         indice = int(valor)
#         try:
#             lista.pop(indice)
#         except IndexError as e:
#             print('Índice não existe!')
#             #print(f"{e}") 
#         print()
#     elif opcao == 'l':  # listar

#         if(len(lista) <= 0):
#             print('A lista está vazia!')
#         else:
#             for indice, valor in enumerate(lista):
#                 print(f'{indice} - {valor}')
#         print()
#     elif opcao == 's':
#         break
#     else:
#         print('Opção Inválida!\n')
    
# frase = " Seja Bem Vindo,    esta é uma mensagem de aviso  "
# lista_frases = frase.split(',')
# nova_lista_frases = []
# for i, frase in enumerate(lista_frases):
#     print(lista_frases[i].strip()) # rstrip() lstrip() - cortar espaços da string
#     nova_lista_frases.append(lista_frases[i].strip())
# print()
# print(nova_lista_frases)
# print(lista_frases)
# frase_unida = ' -'.join(lista_frases)
# print(frase_unida)

# nome = 'Fulano Ciclano'
# nome_separado = '*'.join(nome)
# print(f'*{nome_separado}*')

# lista = ['A', 'B', 'C']
# for key, value in enumerate(lista):
#     print(lista[key])

# # Listas dentro de listas
# salas = [
#     ['Ana', 'Julio'],
#     ['Claudia', ],
#     ['João', 'Maria', 'José', (10, 20, 30)],
# ]
# #print(salas[0][1])
# #print(salas[2][3][1])

# for sala in salas:
#     #print(sala)
#     for aluno in sala:
#         print(aluno)

# frase = '   Iniciou o texto'
# print(frase.strip())

# palavra = 'Fulano'
# print('-'.join(palavra))

# frase = 'Divide minha frase, tá bom?'
# print(frase.split(','))

# Desempacotar nas chamadas das funções
# nomes = ['Fulano', 'Ciclano', 'Beltrano', 'Elano']
# print('Normal:', nomes)
# print('Desempacotamento:', *nomes, sep=' | ', end='\n')
# salas = [
#     ['Ana', 'Julio'],
#     ['Claudia', ],
#     ['João', 'Maria', 'José', (10, 20, 30)],
# ]
# print(*salas, sep='\n')

# Operação ternária
# compara = 10 == 10
# variavel = 'É igual' if compara else 'É diferente'
# print(variavel)

# numero = 8
# verificar = 'É maior que 9' if numero > 9 else 'É menor que 9'
# print(verificar)
# numero = input('Digite um número: ')
# num_int = int(numero)
# operacao = num_int % 2 == 0
# condicao = f'{num_int} é par' if operacao else f'{num_int} é ímpar'
# print(condicao)
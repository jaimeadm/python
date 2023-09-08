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

# def multiplicar(x, y):
#     return x * y

# valor1 = multiplicar(2, 3)  # 6
# valor2 = multiplicar(4, 5)  # 20
# print(valor1 + valor2)      # 26

# def somar(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     #print('Total:', total)
#     return total

# calcular = somar(3, 6, 9)
# print('Somar: ', calcular)

# print(sum((2, 4, 6, 8)))

# def multiplicar(*args):
#     total = 0
#     acumulador = 0
#     for numero in args:
#         acumulador = numero * 2
#         total += acumulador
#     return total

# calcular2 = multiplicar(2, 4)
# print('Multiplicar: ', calcular2)


# def funcao(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# valores = (2, 3, 5)
# print(funcao(*valores)) # empacotar valores da tupla para enviar

# def multiplicar(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# valor = multiplicar(2, 3, 2, 4)
# print(valor)

# # Par ou Ímpar
# def par_impar(x):
#     return f'{x} é par' if x % 2 == 0 else f'{x} é ímpar'

# print(par_impar(3))


# Higher Order Functions
# def saudacao(msg, nome):
#     return f'{msg}, {nome}'

# def executa(funcao, *args):
#     return saudacao(*args)

# #saudar = saudacao('Bom dia', 'Fulano')
# saudar = executa(saudacao, 'Boa tarde', 'Ciclano')
# print(saudar)

# Closure
# def saudacao(msg):
#     def saudar(nome):
#         return f'{msg}, {nome}'
#     return saudar
    
# saudar1 = saudacao('Bom dia')
# saudar2 = saudacao('Boa noite')
# for nome in ['Fulano', 'Ciclano']:
#     print(saudar1(nome))
#     print(saudar2(nome))

# Somar com Closure
# def calcular(operacao):
#     if operacao == 'somar':
#         def operacao(num1, num2):
#             return num1 + num2
#     elif operacao == 'multiplicar':
#         def operacao(num1, num2):
#             return num1 * num2
#     else:
#         return 'Operação Inválida'
#     return operacao

# calculo = calcular('multiplicar')
# print(calculo(2, 3))

# # Multiplicador
# def criar_multiplicador(x):
#     def multiplicador(y):
#         return x * y
#     return multiplicador

# vezes = criar_multiplicador(5)
# print(vezes(3))

# def multiplicador(multiplicador):
#     def multiplicar(numero):
#         return multiplicador * numero
#     return multiplicar

# duplicar = multiplicador(2)
# print(duplicar(5))

# triplicar = multiplicador(3)
# print(triplicar(10))

# Dicionário
# pessoa = {
#     'nome': 'Fulano',
#     'idade': 20,
#     'altura': 1.75,
#     'enderecos': [
#         {'rua': 'XYZ', 'numero': 91},
#         {'rua': 'ZYX', 'numero': 92},
#     ],
# }
# print(pessoa, type(pessoa))
# for chave in pessoa:
#     print(f'{chave} - {pessoa[chave]}')

# pessoa = {}

# chave = 'sobrenome'
# pessoa['nome'] = 'Fulano Ciclano'
# pessoa[chave] = 'da Silva'
# print(pessoa[chave]) # da Silva
# del pessoa[chave]
# print(pessoa)   # {'nome': 'Fulano Ciclano'}
# print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None:
#     print(f'Não tem a chave {chave}')
# else:
#     print(f'A chave {chave} existe')

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# dicionario = {
#     'nome': 'Fulano',
#     'idade': 20,
# }

# dicionario.setdefault('sobrenome', 'da Silva')
# print(dicionario['sobrenome'])

# print(len(dicionario))
# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

# for key, value in dicionario.items():
#     print(key, value)

# DEEP COPY e SHALLOW COPY
# import copy
# dicionario1 = {
#     'nome': 'Fulano',
#     'idade': 20,
#     'numeros': [10, 20]
# }
# dicionario2 = dicionario1.copy() # copia do dicionário
# #dicionario2 = copy.copy(dicionario1) # shallow copy (igual acima)
# dicionario2 = copy.deepcopy(dicionario1) # deep copy

# dicionario1['profissao'] = 'Gerente de RH'
# dicionario1['numeros'][0] = 100

# print(dicionario2)
# print(dicionario1)
# print(dicionario1.get('nome'))
# nome = dicionario1.pop('nome') # remover chave nome
# print(nome)
# print(dicionario1)
# ultima_chave = dicionario1.popitem() # remover última chave
# print(ultima_chave)
# print(dicionario1)
# dicionario1.update({
#     'idade': 56,
#     'sobrenome': 'Santos',
#     'peso': 72
# })
# dicionario1.update(peso=85, sobrenome='Nunes')
# print(dicionario1)
# tupla = (('idade', 19), ('sobrenome', 'Cavalcante'))
# dicionario1.update(tupla)
# print(dicionario1)
# lista = [['peso', 63], ['idade', 35]]
# dicionario1.update(lista)
# print(dicionario1)

# Criar Set - mutáveis, aceitam só imutáveis internamente
# s1 = set()
# #s1 = {'Normal', 2, 3}
# print(s1, type(s1))
# print(2 in s1)

# s1.add('Fulano')
# print(s1)
# s1.update(('Ciclano', 10, 20))
# print(s1)
# s1.discard('Fulano')
# print(s1)
# s1.clear()
# print(s1)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1 | set2  # une 2 sets (tira repetidos)
# print(set3)
# set3 = set1 & set2 # mostra repetidos em ambos
# print(set3)
# set3 = set1 - set2 # mostra não repetidos apenas da esquerda
# print(set3)
# set3 = set1 ^ set2 # não estão em embos (tira repetidos)
# print(set3)

# Exemplo de uso do set()
# letras = set()
# while True:
#     letra = input('Digite uma letra: ')
#     if len(letra) > 1 or not letra.isalpha():
#         print('Digite apenas uma letra')
#         continue
#     if letra in letras:
#         print('Letra já digitada')
#         continue
#     letras.add(letra.lower())
#     print(letras)

# Função Lambda é anônima de uma linha
# lista = [1, 3, 4, 8, 5]
# print(sorted(lista))        # cria uma nova lista como cópia raza
# lista.sort(reverse=True)    # mexe na lista original  
# print(lista)

# lista = [
#     {'nome': 'Fulano', 'idade': 19},
#     {'nome': 'Ciclano', 'idade': 73},
#     {'nome': 'Beltrano', 'idade': 56},
# ]

# def ordenar(item):
#     return item['nome']

# def exibir(lista):
#     for item in lista:
#         print(item)
    
# #lista.sort(key=ordenar)
# lista.sort(key=lambda item: item['nome'])
# for item in lista:
#     print(item)

# print()
# l1 = sorted(lista, key=lambda item: item['idade'])
# exibir(l1)

# Lamba complexo
# def executa(funcao, *args):
#     return funcao(*args)

# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = cria_multiplicador(2)
# print(duplica(3))
# # Com Lambda
# duplica = executa(
#     lambda m : lambda n : n * m,
#     2
# )
# print(duplica(100))

# print()

# print(
#     executa(
#         lambda x, y: x + y, 10, 20
#     ),
#     executa(soma, 1, 2),
#     soma(2, 3)
# )

# print(
#     executa(
#         lambda *args : sum(args),
#         10, 5, 3, 2
#     )
# )

# par_impar = lambda x : x % 2 == 0
# print(par_impar(2))

# x = lambda *args : sum(args)
# print(x(5, 10, 1))

# def funcao(numero):
#     return lambda x : x * numero

# duplicar = funcao(2)
# print(duplicar(5))

# # args (não nomeados) e kwargs (nomeados)

# pessoa = {
#     'nome': 'Fulano',
#     'sobrenome': 'da Silva',
# }
# dados_pessoa = {
#     'idade': 23,
#     'altura': 1.75, 
# }

# (v1, v2) = pessoa.items()
# print(v1, v2)   # v1 = ('nome', 'Fulano') | v2 = ('sobrenome', 'da Silva')
# dado1, dado2 = pessoa.items()
# print(dado1, dado2)

# pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# def mostrar_argumentos(*args, **kwargs):
#     print('Argumentos não nomeados:', args)
#     for chave, valor in kwargs.items():
#         print(chave, valor)

# # mostrar_argumentos('nao_nomeado', 23, id=5, usuario='fulano')
# mostrar_argumentos(**pessoa_completa)

# List comprehension cria rapidamete uma lista a partir de iteráveis

# import pprint

# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=50)

# lista = []
# for numero in range(10):
#     lista.append(numero)
# #print(lista)

# lista = [
#     #numero * 2
#     f'{numero} - par' if numero % 2 == 0 else f'{numero} - ímpar'
#     for numero in range(10)
# ]
# #print(lista)

# produtos = [
#     {'nome': 'p1', 'preco': 10},
#     {'nome': 'p2', 'preco': 55},
#     {'nome': 'p3', 'preco': 30},
# ]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if produto['preco'] > 10
# ]
# #print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
# p(lista)

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# #print(lista)
# lista = [
#     (x, y) for x in range(3)
#     for y in range(3)
# ]
# print(lista)

#List Comprehension
# frutas = ['Maçã', 'Banana', 'Abacaxi', 'Uva', 'Morango']
# nova_lista = []
# for fruta in frutas:
#     if 'M' in fruta:
#         nova_lista.append(fruta)
# print(nova_lista)

# outra_lista = [ fruta for fruta in frutas if 'M' in fruta ]
# print(outra_lista)

# novalista = [x for x in range(10) if x < 5]
# lista_maiuscula = [fruta.upper() for fruta in frutas]
# print(novalista, lista_maiuscula)
# tudo_uva = ['uva' for fruta in frutas]
# print(tudo_uva)
# lista_banana = [fruta if fruta == 'Banana' else 'Laranja' for fruta in frutas]
# print(lista_banana)

# lista1 = [x for x in range(10)]
# lista2 = [
#     x if x > 5 else 1 
#     for x in lista1
# ]
# print(lista2)

# Dictionary e Set Comprehension
# produto = {
#     'nome': 'Caneta',
#     'preco': 1.65,
#     'categoria': 'Escritório',
# }
# dc = {
#     chave: valor.upper() 
#     if isinstance(valor, str) else valor
#     for chave, valor in produto.items()
#     if chave != 'categoria'
# }
# print(dc)

# set1 = {i for i in range(10)}
# print(set1)

# isinstance - saber se o objeto é de determinado tipo
# lista = [
#     'a', 1, 1.1, True, [0, 1, 2], (1, 2),
#     {0, 1}, {'nome': 'Luiz'},
# ]

# for item in lista:
#     if isinstance(item, set):
#         item.add(2)
#         print(item, isinstance(item, set))
#     elif isinstance(item, str):
#         print(item.upper())
#     elif isinstance(item, (int, float)):
#         print(item, item * 2)
#     else:
#         print(f'Outro tipo: {item}')

# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
#
# lista = []
# dicionario = {}
# conjunto = set()
# tupla = ()
# string = ''
# inteiro = 0
# flutuante = 0.0
# nada = None
# falso = False
# intervalo = range(0)

# def falsy(valor):
#     return 'falsy' if not valor else 'truthy'
    
# print(f'{lista=}', falsy(lista))

# hasattr e getattr
# frase = 'Olá, bem vindo!'
# metodo = 'upper'

# if hasattr(frase, metodo):
#     print(getattr(frase, metodo)())
# else:
#     print('Não tem o método', metodo)

# iteravel = ['Fulano', 'Ciclano', 'Beltrano']
# iterator = iteravel.__iter__()
# #iterator = iter(iteravel)
# print(next(iterator))
# print(next(iterator))
# print(iterator.__next__())

# import sys
# lista = [n for n in range(100)]
# generator = (n for n in range(100))
# print(sys.getsizeof(lista)) # tamanho em bytes
# print(sys.getsizeof(generator))

# print(next(generator))

# Generators são um tipo especial de função que retorna um 
# lazy iterator (não armazenam conteúdo em memória)
# Iterator é um objeto que contém um número contável de valores

# def generator(inicio=0, fim=10):
#     while True:
#         yield inicio
#         inicio += 1

#         if inicio > fim:
#             return
        
# gerador = generator(1, 5)
# for i in gerador:
#     print(i)

# def generator1():
#     yield 1
#     yield 2

# def generator2():
#     yield from generator1()
#     yield 3
#     yield 4

# gen1 = generator1()
# for i in gen1:
#     print(i)
# print()
# gen2 = generator2()
# for i in gen2:
#     print(i)

# def generator(n):
#     contador = 0
#     while contador < n:
#         yield contador
#         contador += 1

# for valor in generator(10):
#     print(valor)

# raise - lançar exceções
#raise ValueError('Erro')

# def testa_se_zero(n, d):
#     if n == 0 or d == 0:
#         raise ZeroDivisionError(f'{n} e {d} não devem ser zero')    
#     return True

# def testa_int_float(n, d):
#     if not isinstance(n, (int, float)):
#         raise TypeError(f'{n} deve ser int ou float')
#     if not isinstance(d, (int, float)):
#         raise TypeError(f'{d} deve ser int ou float')

# def divide(n, d):
#     testa_se_zero(n, d)
#     testa_int_float(n, d)
#     return n / d

# print(divide(8, 2))

# Módulos (import, from, as e *)
# import sys
# print(sys.platform)

# from sys import exit, platform
# print(platform)

# import sys as sistema
# print(sistema.platform)

# from sys import platform as plataforma, exit as saida
# print(plataforma)

# from sys import * # má prática

# #import importlib   # recarregar o módulo
# import basico
# from basico import variavel_modulo

# print('Nome do módulo', __name__)
# print(basico.variavel_modulo)
# #importlib.reload(basico) # recarregar do módulo
# print(variavel_modulo)

# from packages.modulo_novo import somar, variavel
# print(variavel)
# print(somar(2, 3))

# import packages
# packages.mostrar('Ola')

# # Exercicio
# import copy
# from dados import produtos  # lista de produtos em ./dados/produtos_modulo.py
# #from dados.produtos_modulo import produtos

# def exibir_produtos(produtos):
#     for produto in produtos:
#         print(produto)
#     print()

# def ordenar(chave):
#     return lambda item : item[chave]

# print('Produtos Original')
# lista_produtos = copy.deepcopy(produtos)
# exibir_produtos(lista_produtos)

# #novos_produtos = [
#     #{**p, 'preco': round(p['preco'] * 1.1, 2)}
#     #for p in copy.deepcopy(produtos)
# #]

# print('Produtos com aumento de 10%')
# novos_produtos = []
# for produto in lista_produtos:
#     preco = produto['preco']
#     preco_aumentado = (preco * 0.1) + preco
#     produto['preco'] = f'{preco_aumentado:.2f}'
#     novos_produtos.append(produto)
# exibir_produtos(novos_produtos)

# print('Produtos organizados por nome decrescente')
# lista_ordenada_nome = sorted(copy.deepcopy(produtos), key=ordenar('nome'), reverse=True)
# exibir_produtos(lista_ordenada_nome)

# print('Produtos organizados por preço crescente')
# lista_ordenada_preco = sorted(copy.deepcopy(produtos), key=ordenar('preco'))
# exibir_produtos(lista_ordenada_preco)

# Exercício - Adiando execução de funções
# Closure é uma função aninhada (nested function) que permite acessar variáveis da função externa
# mesmo depois que a função externa é fechada
# def soma(x, y):
#     return x + y
# def multiplica(x, y):
#     return x * y
# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x, y)    
#     return interna

# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)
# print(soma_com_cinco(10))
# print(multiplica_por_dez(2))

# Variável livre
# def concatenar(valor):
#     minha_string = valor
#     def interna(string_concatena):
#         nonlocal minha_string
#         minha_string += string_concatena
#         return minha_string
#     return interna

# concatena = concatenar('A')
# print(concatena('!'))

# Funções decoradoras e decoradores (syntax sugar)
# recebe uma função e cria uma função interna (closure)
# def criar_funcao(funcao):
#     def interna(*args, **kwargs):
#         for arg in args:
#             e_string(arg)
#         resultado = funcao(*args, **kwargs)
#         return resultado
#     return interna

# @criar_funcao # usar decorador automaticamente
# def inverte_string(string):
#     return string[::-1]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('O parâmetro deve ser string')

# # inverte_string_verifica_param = criar_funcao(inverte_string)
# # invertida = inverte_string_verifica_param('Fulano')
# # print(invertida)
# invertida = inverte_string('padaria')
# print(invertida)

# Unir Listas
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [
#         (l1[i], l2[i]) for i in range(intervalo)
#     ]

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(zipper(l1, l2))
# print(list(zip(l1, l2)))
# from itertools import zip_longest
# print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))

# Exercicio 2
# lista1 = [1, 2, 3, 4, 5, 6, 7]
# lista2 = [1, 2, 3, 4]
# lista_soma = [x + y for x, y in zip(lista1, lista2)]
# print(lista_soma)

# count é um iterator sem fim
# from itertools import count
# c1 = count(10, 2)
# r1 = range(10, 20, 2)
# for i in c1:
#     if i >= 20:
#         break
#     print(i)
# print('--------')
# for i in r1:
#     print(i)

# Combinations: não importa a ordem, iterável, tamanho do grupo
# Permutations: ordem importa
# Product: ordem importa e repete valores únicos
# from itertools import combinations, permutations, product, groupby

# def print_iter(iterator):
#     print(*list(iterator), sep='\n')

# pessoas = ['João', 'Maria', 'José', 'Cleide',]
# camisetas = [['preta', 'verde'],['p', 'm', 'g'],['masculino', 'feminino'],]

# print(*list(combinations(pessoas, 2)), sep='\n')
# print_iter(combinations(pessoas, 2))
# print()
# print_iter(permutations(pessoas, 2))
# print()
# print_iter(product(*camisetas))

# groupby - agrupar valores
# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]

# def ordena(aluno):
#     return aluno['nota']

# alunos_agrupados = sorted(alunos, key=ordena)
# grupos = groupby(alunos_agrupados, key=ordena)

# #print(*alunos_agrupados, sep='\n')
# for chave, grupo in grupos:
#     print(chave)
#     print(*aluno)

# map: executa uma função para cada item do iterável (faz o mesmo que list comprehension).
# partial: ajusta um certo número de argumentos de uma função e gera uma nova função. (parecido com closure)
# reduce: reduz um iterável em um valor

# from functools import partial, reduce

# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# print(*list(produtos), sep='\n')

# def aumentar_porcentagem(preco, porcentagem):
#     return round(preco * porcentagem, 2)

# # Partial
# aumentar_dez_porcento = partial(
#     aumentar_porcentagem,
#     porcentagem=1.1
# )

# # novos_produtos = [
# #     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# # ]

# # Map
# def muda_preco_produtos(produto):
#     return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

# novos_produtos = map(
#     muda_preco_produtos,
#     produtos
# )
# print(*list(novos_produtos), sep='\n')

# # Filter
# outros_produtos = filter(
#     lambda p : p['preco'] > 20,
#     produtos
# )
# print(*list(outros_produtos), sep='\n')
# print()

# # Exemplo 1 
# print(
#     list(map(
#         lambda x : x * 2, 
#         [10, 22, 31, 8]
#     ))
# )

# Exemplo map
# def tamanho(letra):
#     return len(letra)
# letras = ['AAAAAA', 'BBB', 'CCCC']
# tamanho_letras = map(tamanho, letras)
# print(*tamanho_letras)

# # Exemplo partial
# def funcao(a, b, c, x):
#     return 100*a + 10*b + 5*c + x
# somar = partial(
#     funcao,
#     3, 4, 10, 
# )
# print(somar(1))

# Reduce
# def funcao_reduce(acumulador, produto):
#     print(acumulador, produto)
#     return acumulador + produto['preco']
# total = reduce(
#     funcao_reduce,
#     #lambda a, p : a + p['preco'],
#     produtos,
#     0
# )
# print('Total: ', round(total, 2))
# def soma(a, b):
#     result = a + b
#     print(f'{a} + {b} = {result}')
#     return result

# numeros = [1, 2, 3, 4]
# total = reduce(soma, numeros)
# print(total)

# Função Recursiva
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# Arquivos
# Modos: r(leitura), w(escrita), x(criação)
# a(escreve no final), b(binário)
# t(modo texto), +(leitura e escrita), - with open(abre e fecha)
#
# Métodos: write, read, writelines (escrever várias linhas)
# seek (move o cursor), readline, readlines
# os.remove ou unlink (apaga um arquivo)
# os.rename (troca ou move um arquivo)
# json.dump (gera um arquivo json)
# json.load

# import os
# caminho = 'arquivo.txt'
# arquivo = open(caminho, 'w')
# arquivo.close

# with open(caminho, 'w+', encoding='utf-8') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Ler linha por linha')
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print('Li 2 linhas')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
#     print('Fim do for!!!')

# with open(caminho, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho, 'a+') as arquivo:
#     arquivo.write('Mais atenção\n')
#     arquivo.seek(0,0)
#     print(arquivo.read())

# #os.unlink(caminho) # apagar arquivo
# #os.remove(caminho)
# #os.rename(caminho, 'novo_arquivo.txt')

# JSON
#import json

# pessoa = {
#     'nome': 'Fulano',
#     'sobrenome': 'Aviação',
#     'enderecos': [
#         {'rua': 'Rua 1', 'numero': 32},
#         {'rua': 'Rua 2', 'numero': 55},
#     ],
#     'altura': 1.84,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'obs': None,
# }

# with open('arquivo.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

# with open('arquivo.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     print(pessoa)
#     print(pessoa['nome'])

# def soma(x, y):
#     return x + y

# def subtrai(x, y):
#     return x - y

# def criar_funcao(funcao, x, y):
#     def interna():
#         return funcao(x, y)
#     return interna  

# opcao = input('Escolha uma opção (somar, subtrair): ')
# x = input('Digite o primeiro número: ')
# y = input('Digite o segundo número: ')
# int_x = int(x)
# int_y = int(y)

# # opcoes = {
# #     'somar': lambda: soma(int_x, int_y),
# #     'subtrair': lambda: subtrai(int_x, int_y),
# # }

# opcoes = {
#     'somar': criar_funcao(soma, int_x, int_y),
#     'subtrair': criar_funcao(subtrai, int_x, int_y),
# }

# escolha = opcoes.get(opcao)
# print(escolha())

# Positional-only Parameters (/) - tudo antes da / deve ser posicional(não nomeado) 
# def soma(x, y, /, a, b):
#     print(x + y + a + b)
# soma(2, 3, 4, b=5)
# # Keyword-only Arguments(*) - tudo depois do * é nomeado
# def soma2(a, b, *, c):
#     print(a + b + c)
# soma2(2, 3, c=5)

# import json

# lista = []
# caminho_arquivo = 'lista.json'

# try:
#     with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#         lista = json.load(arquivo)
#         for l in lista:
#             print(l)
# except FileNotFoundError:
#     print('Arquivo não encontrado, o arquivo será criado')
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#         lista = json.dump(lista, arquivo, indent=2, ensure_ascii=False)

# lista = ['Fulano', 'Ciclano', 'Beltrano']

# with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#     lista = json.dump(lista, arquivo, indent=2, ensure_ascii=False)

# with open(caminho_arquivo, 'r', encoding='utf8' ) as arquivo:
#     lista = json.load(arquivo)
#     print(*lista)
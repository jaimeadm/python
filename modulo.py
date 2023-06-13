# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()

import meumodulo

meumodulo.saudacao('Fulano')
print('Este módulo é o', __name__)

# Recarregar módulo
import importlib

print('Qualquer coisa')

importlib.reload(meumodulo)

# Packages
from sys import path

from packages import *
# OU
import packages.modulo_novo
print(packages.modulo_novo.somar(1, 1))
# OU
from packages import modulo_novo
print(modulo_novo.somar(3, 3))
# OU
from packages.modulo_novo import somar
print(somar(2, 2))
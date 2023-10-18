import os
from itertools import count

caminho = os.path.join('/home', 'administrador', 'code', 'menu')
counter = count()

for root, dirs, files in os.walk(caminho):
    contador = next(counter)
    print(contador, root)

    for dir_ in dirs:
        print(' ', contador, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', contador, 'File:', caminho_completo_arquivo)

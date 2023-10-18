import os

# os.system('clear')
# os.system('Olá Mundo')

# print('#' * 300)

# caminho = os.path.join('/home', 'administrador', 'code', 'db-leitor.sql')
# print(caminho)

# diretorio, arquivo = os.path.split(caminho)
# nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# print(nome_arquivo, extensao_arquivo)

# print(os.path.exists('/home/fulano'))

# print(os.path.abspath('.'))

# print(os.path.basename(caminho))  # parte final do caminho
# print(os.path.basename(diretorio))
# print(os.path.dirname(caminho))


caminho = os.path.join('/home', 'administrador', 'code', 'vagas')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo):
        continue
    for arquivo in os.listdir(caminho_completo):
        print(' - ', arquivo)

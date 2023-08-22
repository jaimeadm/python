import os
# Modos:
# r (leitura), w (escrita), x (criação)
# a (append ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context Manager - with (abre e fecha)

# Escrever
f = open("demofile.txt", "a")
f.write("Mais conteúdo")
f.close

# Ler
f = open('demofile.txt', 'r')
print(f.read())

print()

caminho_arquivo = 'arquivo.txt'

#arquivo = open(caminho_arquivo, 'w')
#arquivo.close()

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write("1 - Olá Mundo\n")
    arquivo.write("2 - Atenção\n")
    arquivo.writelines(
        ('Nova linha\n', 'Final\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print('------------')
    for linha in arquivo.readlines():
        print(linha.strip())

print('##########')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

#os.rename(caminho_arquivo, 'arquivonovo.txt')
#os.remove()
os.unlink(caminho_arquivo)
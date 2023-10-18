from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# print(Path.home() / 'Desktop')

arquivo = Path.home() / 'code' / 'arquivo.txt'
arquivo.touch()
# arquivo.write_text('Bem Vindo')
# print(arquivo.read_text())

arquivo.write_text('')
with arquivo.open('a+') as file:
    file.write('Primeira linha\n')
    file.write('Segunda linha\n')

print(arquivo.read_text())

arquivo.unlink()

#####################

caminho_pasta = Path.home() / 'code' / 'diretorio1'
caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

caminho_arquivo = subpasta / 'file.json'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá Mundo')

##########################################

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)
for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo\n')
        text_file.write('Bem Vindo\n')

# rmtree(caminho_pasta)


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)

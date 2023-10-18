import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'arquivo.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    # leitor = csv.reader(arquivo)
    # for linha in leitor:
    #     print(linha)

    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'], linha['Idade'])
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'arquivo2.csv'

lista_clientes = [
    {'Nome': 'Fulano', 'Endereço': 'Rua XYZ, 10'},
    {'Nome': 'Ciclano', 'Endereço': 'Rua ABC, 20'},
]

with open(CAMINHO_CSV, 'w') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)


# with open(CAMINHO_CSV, 'w') as arquivo:
#     #nomes_colunas = ['Nome', 'Endereço']
#     colunas = lista_clientes[0].keys() # Nome,Endereço
#     escritor = csv.writer(arquivo)
#     escritor.writerow(colunas)

#     for clientes in lista_clientes:
#         escritor.writerow(clientes.values())
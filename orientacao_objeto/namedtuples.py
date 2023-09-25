# namedtuples são classes de objetos usados para agrupamento de atributos.
# são imutáveis como as tuplas.
# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'valor'
    naipe: str = 'naipe'

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )

# as_espadas = Carta('A', 'espadas')
# print(as_espadas)
# print(as_espadas[0])
# print(as_espadas.naipe)
# for valor in as_espadas:
#     print(valor)
# print()
# print(as_espadas._fields)
# print(as_espadas._field_defaults)


rei_copas = Carta('Rei')
print(rei_copas._asdict())

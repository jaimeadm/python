# 4 built-in data types in Python used to store collections of data
# Dicionário, Tupla, Lista e Set 

# Dictionaries are used to store data values in key:value pairs.
dicionario = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
# Tuples, Lists and Sets are used to store multiple items in a single variable.
tupla = ('Banana', 'Maçã', 'Laranja')
lista = ["Banana", "Maçã", "Kiwi"]
set = {"Banana", "Maçã", "Morango"}

for i in range(len(tupla)):
    print(tupla[i])

print()

for i, tup in enumerate(tupla):
    print(i, tup)

print()

for x, y in dicionario.items():
  print(x, y)

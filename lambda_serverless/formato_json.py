import json

dados = """
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
"""

pessoa = json.loads(dados)

print(dados)
print(pessoa)
print(type(dados))
print(type(pessoa))
print(pessoa['secretBase'])

print('---------------------------')

# Converter de dict para str
# (convert a subset of Python objects into a json string.)
info = {'qtde_ec2': 5, 'type_ec2': 't3a.micro', 'ligado': True}
info_str = json.dumps(info)
print(info)
print(info_str)
print(type(info))
print(type(info_str))

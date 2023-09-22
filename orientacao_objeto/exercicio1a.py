import json
CAMINHO_ARQUIVO = 'pessoas.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('Fulano', 21)
p2 = Pessoa('Ciclano', 33)
p3 = Pessoa('Beltrano', 57)
dados = [p1.__dict__, p2.__dict__, p3.__dict__]

def gerar_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    gerar_dump()
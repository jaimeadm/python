from exercicio1a import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)

    for chave, pessoa in enumerate(pessoas):
        print(chave, pessoa['nome'])

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(p1.nome)
    print(p2.nome)
    print(p3.nome)
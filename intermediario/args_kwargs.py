# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Santos',
}

a, b = pessoa.values()
#print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

dados_pessoal = {
    'idade': 10,
    'altura': 1.7,
}

pessoa_completa = {**pessoa, **dados_pessoal}
print(pessoa_completa)

# Exemplo
def mostrar_argumentos(*args, **kwargs):
    print('Argumentos nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#mostrar_argumentos(1, 2, nome='Fulano', idade=19)
mostrar_argumentos(**pessoa_completa)
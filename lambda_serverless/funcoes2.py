def calcular_idade(ano_nascimento, ano_atual=2024):
    idade = ano_atual - ano_nascimento
    print(f'Vc tem {idade} anos')


calcular_idade(2003, ano_atual=2020)


def nome_sobrenome(nome, sobrenome):
    nome_completo = f"{nome} {sobrenome}"
    return nome_completo


nome1 = nome_sobrenome("Fulano", "Ciclano")
print(nome1)

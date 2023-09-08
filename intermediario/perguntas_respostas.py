perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

total_perguntas = len(perguntas)
total_acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    print('\nOpções:')
    
    opcoes = pergunta['Opções']
    for key, opcao in enumerate(opcoes):
        print(f'{key}) {opcao}')

    escolha = input('Escolha uma opção: ')
 
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        total_acertos += 1
        print('Acertou')
    else:
        print('Errou')

    # escolha_int = int(escolha)

    # for chave, opcao in enumerate(pergunta['Opções']):
    #     if chave == escolha_int:
    #         if opcao == pergunta['Resposta']:
    #             total_acertos += 1
    #             print('Acertou')
    #         else:
    #             print('Errou')

print(f'Você acertou {total_acertos} de {total_perguntas} perguntas')
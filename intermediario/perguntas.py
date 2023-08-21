perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

total_acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    
    opcoes = pergunta['Opções']
    
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    escolha = input('Escolha uma opção: ')
    acertou = False
    qtd_opcoes = len(opcoes)

    while True:

        if escolha.isdigit():
            escolha_int = int(escolha)
            
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                
                if opcoes[escolha_int] == pergunta['Resposta']:
                    acertou = True
                    
                    if acertou:
                        total_acertos += 1
                        print('Acertou!')
                else:
                    print('Errou!')
            break
        else:
            escolha = input('Escolha uma opção válida: ')
            continue

print('\nVocê acertou', total_acertos, 'de', len(perguntas), 'perguntas')
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic',
                    help='Mostrar Olá Mundo na tela',
                    # type=str, # Tipo de argumento
                    metavar='STRING',
                    # default='Olá Mundo', # Valor padrão
                    required=False,
                    # action='store_true' # retorna TRUE or FALSE
                    action='append',  # recebe o argumento mais de 1x
                    # nargs=+, # recebe mais de um valor
                    )
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
else:
    print('O valor de b é:', args.basic)

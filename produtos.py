from datetime import datetime
import json

def listar(produtos):
    if not produtos:
        print('Não há produtos para listar')
        return
    for chave, produto in enumerate(produtos):
        print(f'{chave}) {produto}')
    print()

def cadastrar(produto, produtos):
    produtos.append(produto.upper())
    listar(produtos)

def alterar(produto, produto_alterado, produtos):
    if produtos[produto]:
        produtos[produto] = produto_alterado.upper()
    else:
        print('Código Inválido')
    listar(produtos)

def deletar(produto, produtos):
    if produtos[produto]:
        del produtos[produto]
    else:
        print('Código inválido')
    listar(produtos)

def ler(produtos, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        salvar(produtos, caminho_arquivo)
    return dados

def salvar(produtos, caminho_arquivo):
    dados = produtos
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(produtos, arquivo, indent=2, ensure_ascii=False)
    return dados

def gerar_log(data_atual, caminho_log, opcao):
    with open(caminho_log, 'a+', encoding='utf8') as arquivo:
        arquivo.write(f'{data_atual} - {opcao}\n')

# Definições
CAMINHO_ARQUIVO = 'produtos.json'
CAMINHO_LOG = 'produtos.log'
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
produtos = ler([], CAMINHO_ARQUIVO)

while True:
    print('+', '------------------------', '+')
    print('|', '  CADASTRO DE PRODUTOS  ', '|')
    print('+', '------------------------', '+')
    print(f'- listar\n- cadastrar\n- alterar\n- deletar\n- sair')
    opcao = input('Escolha uma opção: ')

    menu = {
        'listar': lambda : listar(produtos),
        'cadastrar': lambda : cadastrar(produto, produtos),
        'alterar': lambda : alterar(produto, produto_alterado, produtos),
        'deletar': lambda : deletar(produto, produtos),
        'sair': lambda : True
    }

    try:
        escolha = menu.get(opcao)
        if opcao == 'cadastrar':
            produto = input('Digite o nome do produto: ')
        elif opcao == 'deletar':
            produto = input('Digite o código do produto: ')
            if produto.isdigit():
                produto = int(produto)
            else:
                continue
        elif opcao == 'alterar':
            produto = input('Digite o código do produto: ')
            if produto.isdigit():
                produto = int(produto)
                produto_alterado = input('Digite o novo nome do produto: ')
            else:
                continue
        elif opcao == 'sair':
            break
        escolha()
        salvar(produtos, CAMINHO_ARQUIVO)
        gerar_log(data_atual, CAMINHO_LOG, opcao)
    except TypeError:
        print('Opção inválida\n')
        continue
    
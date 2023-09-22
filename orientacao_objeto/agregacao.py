# Agragação é uma forma de associação em 2 ou mais objetos
# Geralmente é uma relação de 1 > n

class Carrinho:
    def __init__(self):
        self._produtos = []
        #self.preco_total = 0

    def total(self):
        return f'Total: {sum([p.preco for p in self._produtos])}'
        # for produto in self._produtos:
        #     self.preco_total += produto.preco
        # return self.preco_total
        ...
    def inserir_produto(self, *produtos):
            #self._produtos.extend(produtos)
            #self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print('LISTA DE PRODUTOS')
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print('-' * 10)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Lápis', 1.20), Produto('Tesoura', 3.30)
carrinho.inserir_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
class MyOpen:
    
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('Abrindo arquivo...')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo...')
        self._arquivo.close()
        #raise class_exception(*exception_.args).with_traceback(traceback_)
        #print(class_exception, exception_, traceback_)
        #exception_.add_note('Minha Nota')


with MyOpen('meuarquivo.txt', 'w') as arquivo:
    arquivo.write('Linha 1 \n')
    #arquivo.write('Linha 2 \n', 123) # error
    print('COM', arquivo)

# Novo Exemplo
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu um erro: ', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('newarquivo.txt', 'w') as arquivo:
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n', 123)
    print('WITH', arquivo)
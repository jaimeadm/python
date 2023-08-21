try:
    a = 10
    b = 0
    c = a / b
    #print(b[0])
except ZeroDivisionError as e:
    print('Dividiu por 0')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Msg:', error)
    print('Nome', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')
finally:
    print('Terminou as exceptions')


x = -1
if x < 0:
    raise Exception("Desculpe, números não podem ser abaixo de zero")
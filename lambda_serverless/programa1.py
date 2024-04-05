msg = "Ola, tudo bem"

testa_msg = "bem" in msg

print(testa_msg)

print(msg[1])

print(msg.find('a'))

print(msg.replace('O', 'Ho'))

# IF

temperatura = 30
esta_chovendo = False

if temperatura > 29 and esta_chovendo is False:
    print("Está ficando quente")
else:
    print("Não está ficando quente")

print('---------------------------')

# Exceção

try:
    carros = ['gol', 'fiat', 'bmw', 'fusca']
    print(carros[0])
    print(carros[4])
    print('Não serei mostrado')
except Exception as erro:
    print(f'Erro: {erro}')

print("Fim da exceção")

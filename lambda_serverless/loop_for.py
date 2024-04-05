datas = [3, 14, 33, 9, 10]
animais = ["gato", "cachorro", "passaro"]
dados = {
    'nome': "Fulano",
    'idade': 22,
    'cidade': "São Paulo",
    'cadastro': True
}

for i in animais:
    print(i)


for key in dados:
    print(f'O valor do {key} é {dados[key]}')


# for num in range(10, 15):
#     print(num)

print('---------------------------')

print(f'Antes: {datas}')

for key, data in enumerate(datas):
    datas[key] = data * 2
    print(f'Key: {key} - data: {data}')

print(f'Depois: {datas}')

print('---------------------------')

for i in range(10):
    # if i == 5:
    #     break
    if i == 5:
        continue
    print(i)

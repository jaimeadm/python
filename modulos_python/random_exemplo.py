import random

# random.seed(0)  # nenhum valor muda mais

r_range = random.randrange(1, 10, 1)
print(r_range)

r_int = random.randint(10, 20)
print(r_int)

r_uniform = random.uniform(10, 20)
print(r_uniform)

nomes = ['Fulano', 'Ciclano', 'Beltrano', 'Elano']
random.shuffle(nomes)  # embaralha a lista
print(nomes)

novos_nomes = random.sample(nomes, k=2)  # não repete valor
print(novos_nomes)

novos_nomes2 = random.choices(nomes, k=3)  # repete valor eventualmente
print(novos_nomes2)

novos_nomes3 = random.choice(nomes)  # escolhe um valor
print(novos_nomes3)

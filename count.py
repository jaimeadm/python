# count é um iterator sem fim
from itertools import count

c1 = count(50) # count(step=8, start=8) com argumentos nomeados
r1 = range(10, 100, 5) # step de 5 em 5

# verificar se o c1 tem um iterator
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)
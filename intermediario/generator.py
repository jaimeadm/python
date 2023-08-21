def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
    

gen = generator(n=0, maximum=20)

for i in gen:
    print(i)

print()
# Yield from
def gen1():
    yield 1
    yield 2

def gen2(gen=None):
    yield from gen1()
    yield 3
    yield 4

g = gen2(gen1)
for numero in g:
    print(numero)
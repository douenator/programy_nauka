def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

for i in gen():
    print(i)

print(list(gen()))

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

for i in parzyste(16):
    print(i)

print(list(parzyste(30)))

def testowe(y):
    i = 0
    while i <= y:
        if i % 3 == 1:
            yield i
        i += 1

for i in testowe(100):
    print(i)
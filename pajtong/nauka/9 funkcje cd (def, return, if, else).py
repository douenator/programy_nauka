#def func(x):
#    return x * x #funkcja ktora zwroci kwadrat liczby

#zmienna = func
#print(zmienna(5))

#def func2(f1, x): #funkcja jako argument innej funkcji
#    return f1(x) * x

#print(func2(func, 5))

def silnia(x): #funkcja rekurencyjna (funkcja wywoluje sama siebie wewnatrz ciala)
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(5))
print(silnia(4))
print(silnia(3))
print(silnia(1))
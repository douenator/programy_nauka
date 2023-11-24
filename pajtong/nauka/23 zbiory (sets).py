liczby1 = {0, 1, 2, 3, 4,}
slowa = set(['b', 'c', 'd', 'e'])

print(liczby1)
print(slowa)

liczby1.add(9)
print(liczby1)
liczby1.remove(0)
print(liczby1)
print(1 in liczby1)
print("a" in liczby1)

liczby1 = {0, 1, 2, 3, 4,}
liczby2 = {3, 4, 5, 6, 9,}

print(liczby1 | liczby2) # | to lub ew. logiczna suma
print(liczby1 & liczby2) # & to iloczyn dwoch zbiorow
print(liczby1 - liczby2) # - to odejmowanie drugiego zbioru od pierwszego
print(liczby2 - liczby1) # - to odejmowanie pierwszego zbioru od drugiego
print(liczby2 ^ liczby1) # to różnica symetryczna (oba zbiory są do siebie dodawane, po czym powtarzajace sie liczby zostana wyrzucone i zostana tylko niepowtarzajace sie)
print(liczby1 ^ liczby2) # to samo co wyzej
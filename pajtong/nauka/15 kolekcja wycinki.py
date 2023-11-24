krotka = (2, 4, 8, 16, 32, 64, 128) #kolekcja (krotka)
print(krotka[0])
print(krotka[6])
print(krotka)

print("Elementów:", krotka.count(2))
print("Index:", krotka.index(64)) #zwraca index klucza 64 czyli jego pozycje w kolekcji

print("\nWycinki:")
print(krotka[0:3]) #zwraca kolekcje z przedzialu 0 do 3 (bez trzeciego)
print(krotka[-4:-2]) #zwraca indexy liczac od konca przedziału
print(krotka[0:7:2]) #2 to element skoku, sprawia, ze zwroci co drugi index
print(krotka[::-1]) #odwraca kolekcje
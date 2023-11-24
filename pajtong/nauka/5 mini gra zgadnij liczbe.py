from random import randint

los = randint(1, 10)
odp = -1
i = 0
print("Zgadnij liczbe z przedzialu 1 - 10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbe: "))
    if odp > los:
        print("wylosowana liczba jest mniejsza od twojej")
    elif odp < los:
        print("wylosowana liczba jest wieksza od twojej")
print("Brawo, Odgadles za", i, "razem.")
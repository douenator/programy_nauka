lista = list(range(10))

print(lista)
#wyrazenia listowe pozwalają operowac na zadeklarowanym zbiorze - przeprowadzac modyfikacje na kazdym argumencie

nowa = [i * 2 for i in lista] #wez liste, kazdy argument potraktuj jako zmienna "i" i kazdy ten argument pomnoz przez 2
nowa2 = [i + 2 for i in lista if i % 2 == 0] #dodaj 2 do argumentu, pod warunkiem, ze reszta z dzielenia przez 2 rowna sie 0
print("Nowa:", nowa)
print("Nowa 2:", nowa2)
nowa3 = [i + 1 for i in lista if i % 2 == 0] #operacja dodawania zachodzi po sprawdzeniu czy dana wartosc spelnia warunek "if", dlatego zwraca wartosc 1, 3, 5 (nieparzyste)
print("Nowa 3:", nowa3)
nowa4 = [i + 1 for i in lista if i % 2 == 1] #tutaj najpierw zostana wziete liczby nieparzyste (spelnienie warunku "if), potem do argumentow zostanie dodane 1 (parzyste)
print("Nowa 4:", nowa4)

#formatowanie ciągów string

argumenty = ["Maciek", 31]
tekst = "Cześć mam na imię {0} i mam {1} lat.".format(argumenty[0], argumenty[1])
print(tekst)

tekst = (f'Cześć mam na imię {argumenty[0]} i mam {argumenty[1]} lat.')
print(tekst)
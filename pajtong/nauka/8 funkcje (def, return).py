def funkcja_testowa(): #naglowek funkcji, funkcja konczy sie nawiasami oraz dwukropkiem
    print("funkcja...") #cialo funkcji

funkcja_testowa()

def dodaj(x):
    print(x + 1)

zmienna = dodaj(2)
print(zmienna)

#def dodaj(x, y = 1, z = 0):
#    return x + y + z #zwracanie wartosci z funkcji poza ramy funkcji, returnem konczymy, kod napisany w return nigdy sie nie pojawi

#print(dodaj(2, 3))
#print(dodaj(2))
#wynik = dodaj(2, 3, 5)
#print(wynik)
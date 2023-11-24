slownik = {1: "poniedzialek", 2: "wtorek", 7: "niedziela"} #dictionary otwieramy i zamykamy klamrami, tutaj nie podajemy samych wartosci, tylko pary wartosci (klucz i wartosc)

print(slownik[1])
print(slownik[7])
slownik[3] = "sroda" #dodajemy wartosc slownik[3] do slownik
slownik[4] = False
slownik[5] = 5 #w slowniku mozemy przechowywac rozne typy danych (mix typu danych wartosci)
print(slownik)
slownik["a"] = 1
print(slownik["a"]) #aby odwolac sie do indexu trzeba go przepisac jako string
print(slownik)

#print(slownik[8])
print(slownik.get(8, "inny dzien")) #jezeli w slowniku nie ma danego indexu, zwraca "inny dzien"

print("\nLista:")
for l in slownik.values(): #iteracja po wartosciach, bez values mamy iteracje po kluczach czyli key
    print(l)

print("\----------")
print(slownik.pop(1)) #pierwsza wartosc zostanie tutaj wpisana oddzielnie
print(slownik)
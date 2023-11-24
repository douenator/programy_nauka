plik = open("test.txt", "a", encoding="utf-8")
#wynik funkcji open, otwiera plik, txt zostanie wygenerowany. domyslnie otwiera jako plik tylko dla odczytu, dlatego na koncu trzeba dodac parament "w", "r" to tylko dla odczytu
print(plik.writable())
#true jesli plik jest w trybie do zapisu, false jesli tylko do odczytu
if plik.writable():
    plik.write(input("Wprowadz tekst: ") + "\n") # zapisywanie tekstu do pliku, tutaj tekst jest pobierny od uzytkownika, \n to znacznik nowej linii
plik.close() #tzw. zwolnienie pamieci, plik zostanie zamkniety

plik = open("test.txt", "r")

#if plik.readable():
#    print("Zawartosc pliku:")
#    tekst = plik.read()
#    print(tekst)

#if plik.readable():
#    print("Zawartosc pliku:")
#    tekst = plik.readlines() 
#    print(tekst)
#    for l in tekst: #wyswietlenie linijka po linijce
#        print(l)

if plik.readable():
    print("Zawartosc pliku:")
    for l in plik:
        print(l)
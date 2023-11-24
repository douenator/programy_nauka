def przywitanie():
    print("Witaj użytkowniku")

print("Góra")
przywitanie()
print("Dół")

#w tym kodzie na poczatku definiujemy funkcje o nazwie przywitanie():, która ma wywoływać tekst "Witaj użytkowniku", po czym wywolujemy trzy rozne zadania, gdzie jedno jest nasza funkcja

def przywitanie2(imie):
    print("Witaj " + imie)

#modyfikacja funkcji o parametr (imie): ktore zostanie wywolane tylko przy podaniu odpowiedniego imienia 

przywitanie2("Jacek")
przywitanie2("Arek")
przywitanie2("Tomek")

def przywitanie3(imie, wiek):
    print("Witaj " + imie + " masz " + wiek)

przywitanie3("Agata", "18")
przywitanie3("Ola", "23")
przywitanie3("Barbara", "12")



###################################################
#deklaracja zwrotu 

def szescian(numer):
    return numer*numer*numer

#definiujemy funkcje ktora ma zwracac szescian danej liczby

print(szescian(4))

#wynik otrzymujemy poprzez wywolanie funkcji szescian

def szescian2(numer):
    return numer*numer*numer

wynik = szescian2(4)
print(wynik)

#wynik otrzymujemy poprzez wywolanie zmiennej wynik









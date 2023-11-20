lista = []

def dodaj_do_listy():
    print("Co chcesz dodać do listy?")
    dodaj = str(input(""))
    lista.append(dodaj)

def usun_z_listy():
    print("Co chcesz usuńąć z listy?")
    usun = str(input(""))
    lista.append(usun)

def pokaz_liste():
    print(lista)

def wyczysc_liste():
    lista.clear()

while True:
    print("Witaj w liście rzeczy do zrobienia. Wybierz czynność, którą chcesz wykonać:")
    print("1. Dodaj do listy.\n2. Usuń z listy.\n3. Pokaż liste.\n4. Wyczyść liste.\n5. Wyjdź.\n")
    
    wybor = input("Opcja:")
    if wybor == "1":
        dodaj_do_listy()
    elif wybor == "2":
        usun_z_listy()
    elif wybor == "3":
        pokaz_liste()
    elif wybor == "4":
        wyczysc_liste()
    elif wybor == "5":
        print("Dzięki za skorzystanie z programu.")
        break
    else:
        print("Niepoprawny wybór")

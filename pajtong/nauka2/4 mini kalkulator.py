pierwsza = input("Podaj liczbę: ")
druga = input("Podaj liczbę: ")

wynik = pierwsza + druga
print(wynik)

#przy inputach program defaultowo ustawia wszystko jako string, dlatego wynik jest "zlepiony" zamiast normalnego dodawania

wynik = int(pierwsza) + int(druga) #zamieniamy defaultowe stringi na integery, dzieki czemu zostana potraktowane jako liczby calkowite i zajdzie dodawanie
print(wynik)

wynik = float(pierwsza) + float(druga)
print(wynik)

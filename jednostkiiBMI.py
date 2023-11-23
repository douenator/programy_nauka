from math import *
from fractions import Fraction
import string
import random

def licznikBMI():
    print("Licznik BMI")
    waga = float(input("Podaj wage w kilogramach: "))
    wzrost = float(input("Podaj wzrost w metrach: "))
    wynik = waga / pow(wzrost, 2)
    print(wynik)

def zamianaJednostek():
poprawkiheh
    print("Zamiana jednostek: Wybierz opcje:\n1. Kilometry na mile\n2. Mile na kilometry\n3. Celsjusze na fahrenheity\n4. Celsjusze na kelwiny\n5. Fahrenheity na celsjusze\n6. Fahrenheity na kelwiny\n7. Kelwiny na celsjusze\n8. Kelwiny na fahrenheity\n9. Wróć do menu wyboru.")

    wybor = input("Opcja: ")
    if wybor == "1":
        x = float(input("Podaj wartość: "))
        wynik = x * 0.621371192
        print(round(wynik, 2))
    elif wybor == "2":
        x = float(input("Podaj wartość: "))
        wynik = x * 1.609344
        print(round(wynik, 2))
    elif wybor == "3":
        x = float(input("Podaj wartość: "))
        wynik = Fraction(9, 5) * x + 32
        print(round(wynik, 2))
    elif wybor == "4":
        x = float(input("Podaj wartość: "))
        wynik = x + 273.15
        print(round(wynik, 2))
    elif wybor == "5":
        x = float(input("Podaj wartość: "))
        wynik = (x - 32) * Fraction(5, 9)
        print(round(wynik, 2))
    elif wybor == "6":
        x = float(input("Podaj wartość: "))
        wynik = ((x - 32) / 1.8) + 273.15
        print(round(wynik, 2))
    elif wybor == "7":
        x = float(input("Podaj wartość: "))
        wynik = x - 273.15
        print(round(wynik, 2))
    elif wybor == "8":
        x = float(input("Podaj wartość: "))
        wynik = ((x - 273.15) * 1.8) + 32
        print(round(wynik, 2))

    elif wybor == "9":
        return
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")
        return zamianaJednostek()

def konwersjaWalut():
    print("Konwersja walut: Wybierz opcje:\n 1. PLN\n 2. EURO\n 3. USD\n 4. Wróć do menu wyboru.")
    wyborPierwotnejWaluty = input("Opcja: ")
    if wyborPierwotnejWaluty == "1":
        print("Wybierz docelową walute:\n 1. EURO\n 2. USD")
        wyborDocelowejWaluty = input("Opcja: ")
        if wyborDocelowejWaluty == "1":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 0.23
            print(f'{wynikZamiany} EURO')
        elif wyborDocelowejWaluty == "2":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 0.25
            print(f'{wynikZamiany} USD')            
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            return konwersjaWalut()
    elif wyborPierwotnejWaluty == "2":
        print("Wybierz docelową walute:\n 1. USD\n 2. PLN")
        wyborDocelowejWaluty = input("Opcja: ")        
        if wyborDocelowejWaluty == "1":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 1.09
            print(f'{wynikZamiany} USD')
        if wyborDocelowejWaluty == "2":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 4.37
            print(f'{wynikZamiany} PLN')
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            return konwersjaWalut()
    elif wyborPierwotnejWaluty == "3":
        print("Wybierz docelową walute:\n 1. EURO\n 2. PLN")
        wyborDocelowejWaluty = input("Opcja: ")         
        if wyborDocelowejWaluty == "1":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 0.92
            print(f'{wynikZamiany} EURO')
        if wyborDocelowejWaluty == "3":
            print("Podaj kwote: ")
            kwota = float(input(""))
            wynikZamiany = kwota * 4.00
            print(f'{wynikZamiany} PLN')
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            return konwersjaWalut()
    elif wyborPierwotnejWaluty == "4":
        return

def generatorHasel():
    print("Podaj długość hasła które chcesz wygenerować.")
    dlugosc = int(input(""))
    listaZnakow = string.ascii_letters + string.digits + string.punctuation
    haslo = "".join(random.choice(listaZnakow) for x in range(dlugosc))
    print(f"Twoje hasło to: {haslo}")

while True:
    print("Profesjonalny program douena.\nWybierz program z którego chcesz skorzystać.")
    print("1. Licznik BMI.\n2. Zamiana jednostek.\n3. Konwersja walut.\n4. Generator haseł.\n5. Wyjdź.\n")
    
    wybor = input("Opcja: ")
    if wybor == "1":
        licznikBMI()
    elif wybor == "2":
        zamianaJednostek()
    elif wybor == "3":
        konwersjaWalut()
    elif wybor == "4":
        generatorHasel()
    elif wybor == "5":
        print("Dzięki za skorzystanie z programu.")
        break
    else:
        print("Niepoprawny wybór")
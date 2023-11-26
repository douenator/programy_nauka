from math import *
from fractions import Fraction
from forex_python.converter import CurrencyRates
import string
import random

def licznikBMI():
    print("Licznik BMI")
    waga = float(input("Podaj wage w kilogramach: "))
    wzrost = float(input("Podaj wzrost w metrach: "))
    wynik = waga / pow(wzrost, 2)
    print(f"Twoje BMI to: {round(wynik, 2)}")
    if wynik < 16:
        print("Wygłodzenie")
    elif wynik > 16 and wynik < 16.99:
        print("Wychudzenie")
    elif wynik > 17 and wynik < 18.49:
        print("Niedowaga")
    elif wynik > 18.5 and wynik < 24.99:
        print("Wartość prawidłowa")
    elif wynik > 25 and wynik < 29.99:
        print("Nadwaga")
    elif wynik > 30:
        print("Otyłość")

def zamianaJednostek():
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
    def konwersja(ilosc, pierwotnaWaluta, docelowaWaluta):
        k = CurrencyRates()
        wynik = k.convert(pierwotnaWaluta, docelowaWaluta, ilosc)
        return wynik

    kwota = float(input("Podaj kwotę: "))
    pierwotnaWaluta = input("Podaj pierwotną walutę: ")
    docelowaWaluta = input("Podaj docelową walutę: ")

    kwotaPoKonwersji = konwersja(kwota, pierwotnaWaluta, docelowaWaluta)
    print(f"{kwota} {pierwotnaWaluta} = {round(kwotaPoKonwersji, 2)} {docelowaWaluta}")

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
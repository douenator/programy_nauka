from math import *
from fractions import Fraction

def licznikBMI():
    print("Licznik BMI")
    waga = float(input("Podaj wage w kilogramach: "))
    wzrost = float(input("Podaj wzrost w metrach: "))
    wynik = waga / pow(wzrost, 2)
    print(wynik)

def zamianaJednostek():
    print("Zamiana jednostek: Wybierz opcje:\n1. Kilometry na mile\n2. Mile na kilometry\n3. Celsjusz na fahrenheit\n4. Celsjusz na kelwin\n5. Fahrenheit na celsjusz\n6. Fahrenheit na kelwin\n7. Kelwin na celsjusz\n8. Kelwin na fahrenheit")
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

def konwersjaWalut():
    return

def generatorHasel():
    return

zamianaJednostek()
from math import *

def licznikBMI():
    print("Licznik BMI")
    waga = float(input("Podaj wage: "))
    wzrost = float(input("Podaj wzrost w metrach: "))
    wynik = waga / pow(wzrost, 2)
    print(wynik)

licznikBMI()
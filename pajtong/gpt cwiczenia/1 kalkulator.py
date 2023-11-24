from math import *

lista = ["dodawanie", "odejmowanie", "mnożenie", "dzielenie", "potęgowanie", "pierwiastek", "procent", "wyjście"]

try:
    num1 = input("Podaj pierwszą liczbę: ")
    numer1 = float(num1)
except ValueError:
    print("Wystąpił błąd. Podana wartość nie jest liczbą.")

print(str(lista))
x = input("Wybierz działanie z listy: ")

if x not in lista:
    print("Wystąwił błąd, złe działanie")
else:
    (...)

if x == "pierwiastek":
    print(sqrt(numer1))

else:    
    try:
        num2 = input("Podaj drugą liczbę: ")
        numer2 = float(num2)
    except ValueError:
        print("Wystąpił błąd. Podana wartość nie jest liczbą.")
    if x == "dodawanie":
        print(numer1 + numer2)
    elif x == "odejmowanie":
        print(numer1 - numer2)
    elif x == "mnożenie":
        print(numer1 * numer2)
    elif x == "dzielenie":
        try:
            print(numer1 / numer2)
        except ZeroDivisionError:
            print("Nie można dzielić przez 0")
    elif x == "potęga":
        print(numer1 ** numer2)
    elif x == "procent":
        print(numer2 / numer1 * 1000)
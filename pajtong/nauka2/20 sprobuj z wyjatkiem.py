try:
    x = 10/0
    number = int(input("Podaj cyfre: "))
    print(number)
except ValueError:
    print("Błąd")
except ZeroDivisionError as dupa:
    print(dupa)
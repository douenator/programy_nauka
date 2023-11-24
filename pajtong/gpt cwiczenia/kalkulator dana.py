import math

def licz(num1):
    if num1 == None:
        num1 = wez_liczbe("Podaj pierwsza liczbe: ")

    operacja = wez_operacje()
    
    if operacja == "sqrt":
        if num1 < 0:
            obsluz_blad("Nie mozna wyciagnac pierwiastka z liczby ujemnej")
        sqrt = math.sqrt(num1)
        print(f"Wynik: {round(sqrt, 2)}")
        licz(sqrt)

    num2 = wez_liczbe("Podaj druga liczbe: ")

    if operacja == "%":
        if num1 == 0:
            obsluz_blad("Nie mozna wyciagnac procent z zera")
        procent = num2 / num1 * 100
        print(f"Wynik: {round(procent, 2)}")
        licz(procent)

    try:
        wynik = eval(f"{num1} {operacja} {num2}")
    except ZeroDivisionError:
        obsluz_blad("Nie mozna dzielic przez zero")
    
    print(f"Wynik: {round(wynik, 2)}")
    licz(wynik)

def wez_liczbe(wiadomosc):
    wartosc = input(wiadomosc)
    if wartosc.lower() == "koniec":
        print("Dzieki za krozystanie z kalkulatora")
        exit()
    try:
        wartosc = float(wartosc)
    except ValueError:
        obsluz_blad("Zly argument")
    return wartosc

def wez_operacje():
    lista_operacji = ["+", "-", "*", "/", "**", "%", "sqrt", "koniec"]
    while True:
        operacja = input(f"Wybierz operacje z listy: ({', '.join(lista_operacji)}): ")
        if operacja.lower() == "koniec":
            print("Dzieki za krozystanie z kalkulatora")
            exit()
        if operacja.lower() in lista_operacji:
            return operacja.lower()
        obsluz_blad("Nieprawidlowa operacja")

def obsluz_blad(wiadomosc):
    print(wiadomosc)
    licz(None)

if __name__ == "__main__":
    licz(None)
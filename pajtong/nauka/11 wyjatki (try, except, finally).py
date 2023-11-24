#na błedy w pythonie mówimy wyjątki (informacja nie python nie wie co z tym zrobic, wyrzucenie wyjatku)
x = 12
y = 0

try: #proba obslugi wyjatku ()
    lista = [3] #pusta lista
    print(lista[0])
    print(x + 4) #string z intiger nie zadziala
    print(x / y)
    print("linijka po") #flaga mowiaca ze wykonano robote (ta linijka sie nie wyswietli poniewaz linijke wyzej nastapil blad)
except ZeroDivisionError: #za try zawsze musi pojawic sie except
    print("Nastapilo dzielenie przez 0")
except TypeError:
    print("Błąd typów danych")
#except (ZeroDivisionError, TypeError): #do except mozna dac kilka wyjatkow
#    print("Wystapil 1 z 2 bledow")
except: #wychwyca kazdy inny, niewymieniony wyjatek i zastepuje inne except
    print("Inny blad")
finally: #niezaleznie czy byly problemy w kodzie czy nie, wykona sie
    print("FINALLY: Wykonam się i tak")

print("Dalsze instrukcje...")

############################

try: #proba obslugi wyjatku - input bedzie dzialal tylko jako float, str wyrzuci blad except
    num1 = input("Podaj pierwszą liczbę: ")
    numer1 = float(num1)
except ValueError:
    print("Wystąpił błąd. Podana wartość nie jest liczbą.")
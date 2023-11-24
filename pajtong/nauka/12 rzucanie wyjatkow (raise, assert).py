#umyslne wyrzucanie bledow
def dzielenie(x, y):
    assert y != 0, "Y == 0" # warunek logiczny prawda albo falsz, bedzie zwracal wartosc prawdy dla wszystkich argumentow roznych od wartosci 0 dla zmiennej y
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0") #moj blad
    print(x / y)
try: #sprawi to, ze nie wyskoczy czerwony blad z kodu wyzej
    dzielenie(2, 1)
except ZeroDivisionError:
    print("Blad")
    raise #wykona pierwszy bledny wyjatek + wyjatek try
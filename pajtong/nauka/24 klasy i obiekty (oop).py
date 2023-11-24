class Czlowiek:  #klasy pozwalaja nam na przechowywanie w sobie zbioru zmiennych, na funkcje wewnatrz klasy mowimy "metoda", klasa pozwoli na stworzenie szablonu ktorym pozniej sie posluzymy do stworzenia obiektu
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
    
    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imie " + self.imie + " lat " + str(self.wiek) + ". "

obiekt = Czlowiek("Maciek", 31)
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))
obiekt2 = Czlowiek("Janusz", 50)
obiekt2.imie = "Andrzej"
print(obiekt2.przedstawSie())
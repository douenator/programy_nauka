class Poldek:
    def __init__(self, kolor):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.spalanie_na_100 = 12
#    kolor = "czerwony" #zmienna statyczna

    def zasieg(self):
        zasieg = self.ilosc_paliwa * 100 / self.spalanie_na_100
        return zasieg

    def hamuj(self):
        pass

poldek = Poldek("czerwony")
poldek2 = Poldek("czarny")

#poldek.bagaznik.append("czapka")
#poldek.bagaznik.append("hulajnoga")

print(poldek.kolor)
print(poldek2.kolor)

print(poldek.zasieg())
print(poldek2.zasieg())
poldek.ilosc_paliwa += 10
print(poldek.zasieg())
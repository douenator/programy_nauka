class Czlowiek:
    def __init__(self, imie):
        self.imie = imie
    
    def przedstawSie(self):
        print(f'Nazywam się ' + self.imie)
    
    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)
    
    @staticmethod
    def przywitaj(arg):
        print(f'Cześć ' + arg)

cz1 = Czlowiek.nowy_czlowiek("Janusz")
cz1.przedstawSie()
cz2 = cz1.nowy_czlowiek("Adrianek")
cz2.przedstawSie()
Czlowiek.przywitaj("przyjacielu.")
cz2.przywitaj("skurwisynu.")
class Polonez:
    def __init__(self):
        print("Polonez jest spoko")
        self.hamuj()
        
    def hamuj(self):
        print("ojoj hamuje oczami")
        self.skrecaj("prawo")
    
    def skrecaj(self, strona):
        print(f'skrecam w {strona}')
    
    def ilosc_paliwa(self):
        return "10 litrow"
    
    def into(self):
        print(self)
    
    def dodaj(self, a, b):
        return a + b
    
    def __str__(self):
        return "Dupsko"

#moj_polonez = Polonez()
#moj_polonez.hamuj()
#moj_polonez.skrecaj("lewo")
#ilosc_paliwa = moj_polonez.ilosc_paliwa()
#print(ilosc_paliwa)
class Auto:
    def __init__(self, waga):
        self.waga = waga
    
    def jedz(self):
        print("Jade")

class AutoSpalinowe(Auto):
    def __init__(self, ilosc_cylindrow, waga):
        self.ilosc_cylindrow = ilosc_cylindrow
        super().__init__(waga)
        
    def sprawdz_olej(self):
        return "Olej jest ok"

class Polonez(AutoSpalinowe):
    def __init__(self, model, ilosc_cylindrow, waga):
        self.model = model
        super().__init__(ilosc_cylindrow, waga)
    
    def jazda_bokiem(self):
        print("Jade bokiem")


auto_spalinowe = Polonez("caro plus", 6, 1500)
print(auto_spalinowe.ilosc_cylindrow)
print(auto_spalinowe.waga)
print(auto_spalinowe.sprawdz_olej())

#auto_spalinowe = AutoSpalinowe(6, 1750)
#print(auto_spalinowe.sprawdz_olej())
#auto_spalinowe.jedz()
#print(auto_spalinowe.waga)
#auto = Auto(1800)
#auto.jedz()

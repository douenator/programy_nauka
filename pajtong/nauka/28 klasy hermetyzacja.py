class Test:
    lista = []
    def dodaj(self, arg):
        self.lista.append(arg)
    
    def zdejmij(self):
        if len(self.lista) > 0:
            return self.lista.pop(len(self.lista) - 1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
#obj.lista.append("X")
print(obj.zdejmij())
#print(obj.lista)
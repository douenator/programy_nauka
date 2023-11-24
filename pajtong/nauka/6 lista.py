zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "d", "e", ]
print(lista)
print(lista[0]) #funkcja podaje pierwszy element z listy
lista[2] = 3 #funkcja zmienia trzeci element "c" na 3
print(lista)
tekst = "no elo"
print(tekst[0])
print(lista + ["f", "g"])
print(lista * 3)
print("Ilosc elementow: ", len(lista))
lista.append("f") #dodanie elementu do listy
print(lista)
lista.append(["g", "h"])
print(lista)
print(lista[6][0])
lista.insert(3, 3) #wskazanie na ktorym miejscu dodac cyfre 3
print(lista)
print("Ilosc: ", lista.count(3)) #wskazanie ile razy wystepuje 3
print("Index:", lista.index("f")) #wskazanie na ktorym miejscu znajduje sie literka f
lista.remove("f") #usuniecie pewnego elementu
print(lista)
lista2 = [1, 20, 35, -5, 0]
print("Min: ", min(lista2)) #funkcja zwraca minimalna wartosc z listy
print("Max: ", max(lista2)) #funkcja zwraca maksymalna wartosc z listy
lista2.sort() #sortowanie od najmniejszego do najwiekszego
print(lista2)
lista2.reverse() #odwrocenie listy
print(lista2)
lista2.clear() #wyczyszczenie listy
print(lista2)
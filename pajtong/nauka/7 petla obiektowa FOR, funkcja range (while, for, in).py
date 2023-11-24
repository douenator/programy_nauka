lista = ["Subskrybuj", "Kanal", "o", "Wszystkim", ] #elementy przechowywane przez liste

i = 0 #zmienna pomocniczna ktora odwoluje sie konkretnie do indexu (iterowanie po indexach listy)
while i < len(lista): #petla nieobiektowa
    print(lista[i])
    i += 1

print("-----------")

for x in lista: #petla obiektowa
    print(x)

print(list(range(10))) #pokazanie listy z wartosciami od 0 do 9

print("-----------")

for y in range(1, 11): #lista z wartosciami od 1 do 10
    print(y)

print("-----------")

for y in range(1, 11, 2): #wylistowanie wartosci od 1 do 10 co druga cyfre
    print(y)
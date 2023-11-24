print(" , ".join(["a", "b", "c"])) #Ten kod Pythonowy wykorzystuje funkcję join() do połączenia elementów listy w jedną łańcuch znaków, gdzie każdy element jest oddzielony przecinkiem i spacją.
print("witaj swiecie".replace("witaj", "cześć")) #witaj zostanie zmieniona na cześć
print("to jest zdanie".startswith("to")) #sprawdzamy czy to zdanie zaczyna sie danym ciagiem znakow
print("to jest zdanie".endswith("zdanie")) #sprawdzamy czy to zdanie konczy sie danym ciagiem znakow
print("j" in "to jest zdanie") #sprawdzamy, czy dana wartosc "j" jest w tym zdaniu
print("to jest zdanie".upper()) #konwersja na wielkie znaki
print("to jest zdanie".lower()) #konwersja na male znaki

print("----------")
lista = [10, 20, 25, 35, 40]

if all([i % 2 == 0 for i in lista]):
    print("wszystkie parzyste")
else:
    print("wszystkie nieparzyste")

if any([i % 2 == 0 for i in lista]):
    print("chociaz jedna parzysta")
else:
    print("brak liczb parzystych")

for i in enumerate(lista): #funkcja enumerate() zwraca indeks i wartości - numeruje argumenty
    print(i[0] +1, "-", i[1])
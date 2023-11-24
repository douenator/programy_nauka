import re

if re.match("ko.", "kotttt"): # kropka oznacza tutaj dowolny znak, ktory python sobie dopasuje, wiec zawsze bedzie sie zgadzalo
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^ko.$", "kot"): # ^ oznacza, ze od tego musi rozpoczynac sie dany wzor, natomiast $ oznacza, ze na tym ma sie konczyc
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[Kk]o.$", "kot"): # znaki w nawiasie kwadratowym oznaczaja, ze program dopasuje sobie albo wielka albo mala litere
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[aA-zZ]o.$", "pot"): #program bedzie dopasowywal znak ze wszystkich wielkich jak i malych liter
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[^aA-zZ]o.$", "pot"): #symbol ^ w zbiorze oznacza, ze zadne litery ze zbioru nie moga wystepowac na 1 pozycji wzoru
    print("Dopasowano")
else:
    print("Nie dopasowano")
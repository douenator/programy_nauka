#print("Prawda") if 5 > 5 else print("Nieprawda")

#a = "Parzysta" if 10 % 2 == 0 else "Nieparzysta"
#print(a)

#for i in range(10):
#    if i > 5:
#        continue
#else:
#    print("Koniec")

try:
    a = 5/0
except ZeroDivisionError:
    print("Błąd")
else:
    print("Koniec")
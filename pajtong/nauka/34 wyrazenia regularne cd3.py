import re

wynik = re.match(r"^((?:He)(?P<first>ll)o) (Wor(ld))$", "Hello World")

if wynik:
    print("Dopasowano")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.groups())
    print(wynik.group('first'))
else:
    print("Nie dopasowano")
import re

wzor = r"banan"
tekst = r"gruszkabananjabłko"

print(re.match(wzor,tekst)) #sprawdza czy tekst zaczyna sie od danego wzoru

if re.match(wzor, tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match(r".*" + wzor + r".*", tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.search(wzor, tekst):
    print("Dopasowano")
else:
    print("Nie dopasowano")

print(re.findall(wzor, tekst))

dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    print(dopasowanie.group()) #wskazuje wszystkie grupy, ktore udalo sie dopasowac
    print(dopasowanie.start()) #wskazuje na ktorym indexie zaczyna sie wzor
    print(dopasowanie.end()) #wskazuje na ktorym indexie konczy sie wzor
    print(dopasowanie.span()) #wskazuje na ktorym indexie zaczyna oraz konczy sie wzor

tekst2 = re.sub(wzor, r"kaszanka", tekst) #zamieni wzor na podany string w tekscie
print(tekst2)
import re

if re.match("^[A-Z][a-z]*$", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[A-Z][a-z]+$", "Ala"):
    print("Dopasowano")
else:
    print("Nie dopasowano")
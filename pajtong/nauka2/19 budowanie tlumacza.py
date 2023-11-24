def tlumacz(zdanie):
    tlumaczenie = ""
    for litera in zdanie:
        if litera.lower() in "aeiou":
            if litera.isupper():
                tlumaczenie = tlumaczenie + "G"
            else:
                tlumaczenie = tlumaczenie + "g"
        else:
            tlumaczenie = tlumaczenie + litera
    return tlumaczenie

print(tlumacz(input("Podaj zdanie: ")))
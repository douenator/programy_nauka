import random

def wybierz_liczby():
    losy = set()
    print("Podaj sześć różnych liczb z przedziału 1-49.")
    while len(losy) < 6:
        try:
            los = int(input(f"Podaj liczbę {len(losy) + 1}: "))
            if los < 1 or los > 49:
                print("Liczba spoza przedziału 1-49")
                continue
        except ValueError:
            print("Niepoprawna wartość.")
        else:
            losy.add(los)
    return (losy)
    
def losuj_liczby():
    return set(random.sample(range(1, 50), 6))

def symulator_lotto():
    losy = wybierz_liczby()
    losy_maszyny = losuj_liczby()
    proby = 1
    
    while losy != losy_maszyny:
        proby += 1
        losy_maszyny = losuj_liczby()
        if proby % 100000 == 0:
            print(f"Wykonano {proby} symulacji.")
    
    print(f"Komputer wylosował takie same liczby: {losy_maszyny}")
    print(f"Liczba prób potrzebnych do trafienia wszystkich liczb: {proby}")

def chybiltrafil():
    losy = wybierz_liczby()
    losy_maszyny = losuj_liczby()
    trafione = set(losy_maszyny) & set(losy)
    ilosc_trafien = len(trafione)
    print(f"Twoje losy to: {losy}")
    print(f"Losy maszyny to: {losy_maszyny}")
    print(f"Trafiłeś {ilosc_trafien} liczby.")

print("Witaj samuraju.")
print("Wybierz opcje: Symulator Lotto, Symulator Chybił Trafił")

wybor =  input("Opcja: ")
if wybor == "Symulator Lotto":
    symulator_lotto()
elif wybor == "Symulator Chybił Trafił":
    chybiltrafil()

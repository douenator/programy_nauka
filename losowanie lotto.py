import random

def wybierz_liczby():
    losy = []
    print("Podaj sześć różnych liczb z przedziału 1-49")
    for i in range(6):
        los = int(input(f"Podaj liczbę {i + 1}: "))
        losy.append(los)
    return sorted(losy)
    
def losuj_liczby():
    return sorted(random.sample(range(1, 50), 6))

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

symulator_lotto()
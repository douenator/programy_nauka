print(2**3)

def raise_to_power(base_num, power_num): #Funkcja raise_to_power przyjmuje dwie argumenty: base_num i power_num, które określają odpowiednio liczbę, którą chcemy podnieść do potęgi, oraz samą potęgę.
    result = 1 #Wewnątrz funkcji tworzona jest zmienna result i inicjalizowana wartością 1. Ta zmienna będzie przechowywać wynik obliczeń.
    for index in range(power_num): #Następnie uruchamiana jest pętla for, która iteruje od 0 do power_num - 1. Zakres pętli jest określany przez range(power_num). To oznacza, że pętla będzie wykonywana power_num razy.
        result = result * base_num #W każdej iteracji pętli wartość zmiennej result jest mnożona przez base_num. Początkowo result wynosi 1, więc w pierwszej iteracji obliczenia to result = 1 * base_num. W kolejnych iteracjach wartość result jest aktualizowana na podstawie wyniku poprzednich obliczeń.
    return result #Po zakończeniu pętli, zmienna result zawiera wynik podniesienia liczby base_num do potęgi power_num.

print(raise_to_power(2, 3))
smallest = None #Na początku tworzona jest zmienna smallest i przypisywana jej wartość None. None jest specjalnym obiektem w Pythonie, który oznacza brak wartości.

#Następnie uruchamiana jest pętla for, która iteruje przez listę [3, 41, 12, 2, 11, 9, 74, 15].
#W każdej iteracji pętli, zmienna itervar przyjmuje wartość kolejnego elementu z listy.
#Wewnątrz pętli sprawdzane jest, czy zmienna smallest ma wartość None (czyli jest to pierwsza iteracja), lub czy bieżący element itervar jest mniejszy niż obecna najmniejsza znaleziona wartość smallest. Jeśli tak, to przypisywana jest nowa najmniejsza wartość do zmiennej smallest.
#Pętla kontynuuje iterację przez całą listę, porównując każdy element z dotychczas znalezioną najmniejszą wartością i aktualizując smallest, jeśli znajdzie mniejszą wartość.
#Po zakończeniu pętli, smallest zawiera najmniejszą znalezioną wartość w liście.
#Ostatecznie, wartość smallest jest wydrukowana na konsoli za pomocą funkcji print().

for itervar in [3, 41, 12, 2, 11,  9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar

print(smallest)
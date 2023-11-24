number_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0]
]
#print(number_grid[1][0]) #wyswietla liczbe z listy pierwsza wspolrzedna [] okresla rzad druga [] okresla kolumne

#Ten kod Python jest pętlą, która służy do iteracji przez dwuwymiarową listę lub macierz (często nazywaną siatką). Oto, jak działa ten kod:
#number_grid to dwuwymiarowa lista (lub macierz), która zawiera liczby lub inne wartości. Ta lista jest prawdopodobnie zdefiniowana wcześniej w kodzie.

for row in number_grid: #Pętla zewnętrzna for row in number_grid: iteruje przez elementy listy number_grid. W każdej iteracji row przyjmuje wartość jednego wiersza z listy number_grid.
    for col in row: #Wewnętrzna pętla for col in row: jest zagnieżdżona w pętli zewnętrznej. Iteruje ona przez elementy w danym wierszu, który jest przechowywany w zmiennej row.
        print(col) #Wewnątrz pętli wewnętrznej print(col) drukuje zawartość zmiennej col, która przechowuje aktualnie rozważany element w macierzy. Może to być liczba, tekst lub dowolna inna wartość, którą zawiera macierz.
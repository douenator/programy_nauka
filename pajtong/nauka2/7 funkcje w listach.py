cyferki = [3, 5, 8, 11, 16, 65, 70, 99]
mordeczki = ["Sylwia", "Laura", "Jotes", "Meyszyk", "Sandra", "Edyta", "Michał"]
mordeczki2 = mordeczki.copy() #skopiuje liste mordeczki
#mordeczki.extend(cyferki) #przedłuzenie funkcji mordeczki o druga liste
#mordeczki.append("Janusz") #przedłuzenie funkcji mordeczki o dodatkowy string
#mordeczki.insert(1, "Andrzej") #wstawienie dodatkowego stringa na drugim indexie listy
#mordeczki.remove("Edyta") #usuniecie wybranego stringa z listy
#mordeczki.clear() #wyczysci liste mordeczki
#mordeczki.pop() #usuniecie ostatniego stringa z listy
#mordeczki.sort() #ulozy liste alfabetycznie
cyferki.reverse() #ulozy liste od tylu do przodu
print(cyferki)
print(mordeczki)
print(mordeczki.index("Jotes")) #wskazanie indexu danego stringa
print(mordeczki.count("Sylwia")) #liczba zawierających elementów
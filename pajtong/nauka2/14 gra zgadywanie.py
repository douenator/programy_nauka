secret_word = "kupsztal" #tworzymy zmienna hasło
guess = "" #tworzymy zmienna zgadywania
guess_count = 0 #tworzymy zmienna licznik zgadywania
guess_limit = 3 #tworzymy zmienna limitu prób
out_of_guesses = False #tworzymy zmienna sprawdzającą czy mamy jeszcze mozliwosc zgadywać

while guess != secret_word and not (out_of_guesses): #pętla sprawdza czy podane przez nas slowo jest hasłem i czy mamy jeszcze próby
    if guess_count < guess_limit: #jeśli mamy jeszcze mozliwosc zgadywania, przechodzimy niżej
        guess = input("Enter your guess: ") #wprowadzenie zgadywanego hasła
        guess_count += 1 #na koniec pętli nasza próba zostaje dodana do licznika
    else: #jeśli nie mamy możliwości zgadywania, koniec gry
        out_of_guesses = True

if out_of_guesses:
    print("You lost!")
else:
    print("You won!")











#while guess!= secret_word:
#    guess = input("Enter your guess: ")

#print("You won!")

#while guess != secret_word:
#    guess = input("Enter your guess: ")
#    if guess == secret_word:
#        print("You won!")
#        break
#    else:
#        print("Wrong guess")
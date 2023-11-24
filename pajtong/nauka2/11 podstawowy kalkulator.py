
num1 = float(input("Enter first number: ")) #funkcja prosi o wprowadzenie pierwszej cyfry
op = input("Enter operator: ") #funkcja prosi o podanie znaku matematycznego
num2 = float(input("Enter second number: ")) #funkcja prosi o wprowadzenie drugiej cyfry

if op == "+": #jesli podany znak to plus
    print(num1 + num2) #wynik dodawania
elif op == "-": #jesli podany znak to minus
    print(num1 - num2) #wynik odejmowania
elif op == "*": #jesli podany znak to mnozenie
    print(num1 * num2) #wynik mnozenia
elif op == "/": #jesli podany znak to dzielenie
    print(num1 / num2) #wynik dzielenia
else: #jesli zostanie podany niepoprawny znak
    print("Invalid operator") #wynik niepoprawny
#is_male = False

#if is_male:
    #print("You are a male")

#jesli warunek is_male nie jest spelniony, nic sie nie wyswietli

#is_male = True

#if is_male:
    #print("You are a male")

#jesli warunek is_male jest spelniony, wyswietli sie napis

is_male = True
if is_male:
    print("You are a male")
else:
    print("You are not a male")
    


is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither are a male nor tall")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall woman")
elif not(is_male) and not(is_tall):
    print("You are a short woman")






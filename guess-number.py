from random import randint


random_number = randint(1,5)

user_number = int(input("Gæt et tal:   "))

while True:
    if user_number < random_number:
        print("For lavt")
    elif user_number > random_number:
        print("For højt")
    else:
        print("Yes you guessed it!")
        break
    user_number = int(input("Prøv igen:     "))
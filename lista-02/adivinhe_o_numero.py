from random import randint

random_number = int(randint(1, 100))

number = -1
while number != random_number:
    number = int(input("Digite um número: "))
    print()

    if number > random_number:
        print("O valor é menor.")
        print()
    elif number < random_number:
        print("O valor é maior.")
        print()
    elif number == random_number:
        print("Acertou!")
        print()

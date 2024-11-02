year = float(input("Digite um ano: "))
print()

(
    print("O ano é bissexto.")
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    else print("O ano não é bissexto.")
)

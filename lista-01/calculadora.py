number01 = float(input("Digite um número: "))
print()

number02 = float(input("Digite um número: "))
print()

operation = str(
    input(
        "Digite uma operação (SO - Soma, SU - Subtracao, MU - Multiplicação, DI - Divisão): "
    )
)
print()

if operation == "SO":
    print(f"{number01} + {number02} = {number01 + number02}")

elif operation == "SU":
    print(f"{number01} - {number02} = {number01 - number02}")

elif operation == "MU":
    print(f"{number01} x {number02} = {number01 * number02}")

elif operation == "DI":
    print(f"{number01} ÷ {number02} = {number01 / number02}")

else:
    print("Erro! A operação digitada é invalida.")

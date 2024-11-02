weight = float(input("Digite seu peso: "))
print()

height = float(input("Digite sua altura: "))
print()

imc = weight / (height * height)

print(f"IMC: {imc}")

if imc < 18.5:
    print("Baixo Peso.")
elif imc < 25:
    print("Peso Normal.")
elif imc < 30:
    print("Excesso de Peso.")
elif imc < 35:
    print("Obesidade Grau I.")
elif imc < 40:
    print("Obesidade Grau II.")
else:
    print("Obesidade Mórbida.")

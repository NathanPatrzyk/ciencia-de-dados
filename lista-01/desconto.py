value = float(input("Digite o valor de um produto: "))
print()

discount = float(
    input(
        "Digite o percentual de desconto (apenas o valor entre 0 e 100, sem o sinal de %): "
    )
)
print()

print(f"Valor sem desconto: {value}")

value_with_discount = value * ((100 - discount) / 100)

value_saved = value - value_with_discount

print(f"Valor com o desconto: {value_with_discount}")

print(f"Valor economizado: {value_saved}")

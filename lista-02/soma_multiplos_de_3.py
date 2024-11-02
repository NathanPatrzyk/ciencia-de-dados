min = int(input("Digite um número mínimo: "))
print()

max = int(input("Digite um número máximo: "))
print()

sum = int(0)
i = min

while i <= max:
    if i % 3 == 0:
        sum += i
    i += 1

print(f"Soma dos Múltiplos de 3: {sum}")

list = list([])
for i in range(10):
    list.append(int(input("Digite um número: ")))
    print()

min = list[0]
max = list[0]
for element in list:
    if element < min:
        min = element
    if element > max:
        max = element

print(f"Menor número: {min}")
print(f"Maior número: {max}")

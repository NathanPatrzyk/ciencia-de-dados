list = list([])
for i in range(5):
    list.append(int(input("Digite um número: ")))
    print()

sum = 0
for element in list:
    sum += element

print(f"Soma dos elementos: {sum}")

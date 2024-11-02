# Armazenar as notas de cada bimestre em uma lista para calcular a média final do estudante:
lista = list([])
for i in range(4):
    lista.append(float(input(f"Nota do {i+1}º Bimestre: ")))

soma = 0
for elemento in lista:
    soma += elemento

print(f"Média Final: {soma/(len(lista))}")

dicionario = {"name": "Nome", "cidade": "São Paulo", "pesos": [1.6, 1.7, 1, 8]}

print(dicionario)
print()
print(dicionario["name"])
print()

dicionario["name"] = "João"
print(dicionario)
print()

pesos = dicionario.pop("pesos")
print(pesos)
print()

for chave, valor in dicionario.items():
    print(chave)
    print()

    print(valor)
    print()

tupla = (1, 2, 3, 4, 5)
print(tupla)
print()

print(tupla[0])
print()

print(tupla[1])
print()

print(tupla[2])
print()

conjunto = {1, 2, 3, 4}
conjunto.add(5)
conjunto.remove(5)


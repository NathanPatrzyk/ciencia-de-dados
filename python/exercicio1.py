name = str(input("Digite seu nome: "))
age = int(input("Digite sua idade: "))
height = float(input("Digite sua altura: "))

print(f"Nome: {name}")

if age < 18:
    print(f"Idade: {age} | Criança")
elif age >= 18 and age < 60:
    print(f"Idade: {age} | Adulto")
elif age >= 60:
    print(f"Idade: {age} | Idoso")

print(f"Altura: {height}")

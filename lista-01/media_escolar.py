notes = list()

notes.append(float(input("Digite a primeira nota (entre 0 e 100): ")))
print()

notes.append(float(input("Digite a segunda nota (entre 0 e 100): ")))
print()

notes.append(float(input("Digite a terceira nota (entre 0 e 100): ")))
print()

sum = float(0)

for note in notes:
    sum += note

print(f"Média: {sum / len(notes)}")

if sum < (0.5 * 280):
    print("Reprovado.")
elif sum < (0.66 * 280):
    print("Em recuperação.")
elif sum > (0.65 * 280):
    print("Aprovado.")

phrase = str(input("Digite uma frase: "))
print()

a = 0
e = 0
i = 0
o = 0
u = 0

for letter in phrase:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1

print(f"a: {a}")
print(f"e: {e}")
print(f"i: {i}")
print(f"o: {o}")
print(f"u: {u}")

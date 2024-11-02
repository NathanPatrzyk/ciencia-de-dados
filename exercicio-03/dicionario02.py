# Usando dicionário para listar os filmes que a pessoa assistiu e qual nota deu para cada um deles (como a pessoa só pode dar uma nota para cada filme, usamos o nome do filme como índice)

filmes_assistimos_por_ana = dict(
    {"Filme B": 1, "Filme A": 4, "Filme G": 2, "Filme C": 5}
)

filmes_assistimos_por_joao = dict(
    {"Filme E": 4, "Filme F": 3, "Filme D": 4, "Filme H": 5}
)

print("Notas do filmes assistidos por Ana: ")
for chave, valor in filmes_assistimos_por_ana.items():
    print(f"{chave}: {valor}")

print("Notas do filmes assistidos por João: ")
for chave, valor in filmes_assistimos_por_joao.items():
    print(f"{chave}: {valor}")

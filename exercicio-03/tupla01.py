# Usando uma tupla de dicionários para exibir um catálogo de produtos de uma empresa:

catalogoDeProdutos = tuple(
    (
        dict({"nome": "Mesa", "preco": 80, "material": "Madeira"}),
        dict({"nome": "Cadeira", "preco": 50, "material": "Metal"}),
        dict({"nome": "Sofá", "preco": 120, "material": "Tecido"}),
        dict({"nome": "Panela", "preco": 40, "material": "Aço"}),
        dict({"nome": "Mouse", "preco": 30, "material": "Plástico"}),
    )
)

print(catalogoDeProdutos)

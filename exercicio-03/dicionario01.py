# Utilizando um dicionario para armazenar os nomes dos passageiros de um voo com o número do assento como chave:
dicionario = dict(
    {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
    }
)

assentoEscolhido = int(
    input(f"{dicionario} \nEscolha um assento (0 - Sair e exibir a lista): ")
)
while assentoEscolhido != 0:
    nomeDoPassageiro = str(input(f"Nome do Passageiro: "))
    dicionario[assentoEscolhido] = nomeDoPassageiro
    assentoEscolhido = int(
        input(f"{dicionario} \nEscolha um assento (0 - Sair e exibir a lista): ")
    )

print(dicionario)

# Usando tuplas para armazenar localização de cidades:

localizacaoCuritiba = tuple(("25º S", "49º O"))
localizacaoFlorianopolis = tuple(("27º S", "48º O"))
localizacaoPortoAlegre = tuple(("30º S", "51º O"))
localizacaoSaoPaulo = tuple(("23º S", "46º O"))
localizacaoRioDeJaneiro = tuple(("22º S", "43º O"))

localizacaoSelecionada = input(
    "Digite qual cidade deseja saber a localização:\n1 - Curitiba,\n2 - Florianópolis,\n3 - Porto Alegre,\n4 - São Paulo,\n5 - Rio de Janeiro.\n"
)

match localizacaoSelecionada:
    case "1":
        print(f"Curitiba: {localizacaoCuritiba}")
    case "2":
        print(f"Florianópolis: {localizacaoFlorianopolis}")
    case "3":
        print(f"Porto Alegre: {localizacaoPortoAlegre}")
    case "4":
        print(f"São Paulo: {localizacaoSaoPaulo}")
    case "5":
        print(f"Rio de Janeiro: {localizacaoRioDeJaneiro}")
    case _:
        print("Código inválido.")

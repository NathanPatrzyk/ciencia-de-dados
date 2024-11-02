# Armazenar valores de operações possíveis para serem utilizados por uma calculadora:
listaDeOperacoes = list(["Soma", "Subtração", "Multiplicação", "Divisão"])

print("Escolha uma operação: ")
i = 1
for operacao in listaDeOperacoes:
    print(f"{i} - {operacao}")
    i += 1

operacaoSelecionada = input() 

print(f"Operação selecionada: {operacaoSelecionada}")

import random

from lottery import Lottery
from bet import Bet


def main():
    mega_sena = Lottery("Mega-Sena", 60, 6)
    quina = Lottery("Quina", 80, 5)
    lotofacil = Lottery("Lotofacil", 15, 25)

    lotteries = list([mega_sena, quina, lotofacil])

    while True:
        print()
        print("Escolha uma opcao:")
        for lottery in lotteries:
            print(lottery.get_name()[0] + " - " + lottery.get_name())

        selected = str(input("Opção selecionada: "))
        selected = selected[0]

        if selected == "M" or selected == "Q" or selected == "L":
            break

    if selected == "M":
        selected_lottery = mega_sena
    elif selected == "Q":
        selected_lottery = quina
    elif selected == "L":
        selected_lottery = lotofacil

    bets = list([])
    while True:
        print()
        user_name = str(input("Digite o nome do apostador: "))

        if user_name == "":
            print()
            print("Erro: Nome do apostador não pode ser nulo.")
            continue
        else:
            print()
            betting_numbers = str(
                input(
                    f"Digite {selected_lottery.get_sorted_numbers_quantity()} números entre 1 e {selected_lottery.get_numbers_quantity()} (divididos por vírgula): "
                )
            )

            betting_numbers = betting_numbers.replace(" ", "").split(",")
            unique_betting_numbers = list(set(betting_numbers))
            unique_betting_numbers = [int(number) for number in unique_betting_numbers]

            if len(betting_numbers) < selected_lottery.get_sorted_numbers_quantity():
                print()
                print(
                    f"Erro: Quantidade de números insuficientes, faltam {selected_lottery.get_sorted_numbers_quantity() - len(betting_numbers)} números. Digite os números novamente."
                )
                continue
            if len(unique_betting_numbers) != len(betting_numbers):
                print()
                print("Erro: Há números repetidos. Digite os números novamente.")
                continue

            errors = 0
            for unique_betting_number in unique_betting_numbers:
                if unique_betting_number < 1:
                    errors += 1
                    print(f"Erro: {unique_betting_number} menor que 1")
                elif unique_betting_number > selected_lottery.get_numbers_quantity():
                    errors += 1
                    print(
                        f"Erro: {unique_betting_number} maior que {selected_lottery.get_numbers_quantity()}"
                    )

            if errors > 0:
                continue

            else:
                bet = Bet(user_name, selected_lottery, unique_betting_numbers)
                bets.append(bet)

                print()
                print("Escolha uma opção:")
                print("N - Nova Aposta")
                print("F - Finalizar Recebimento de Apostas")

                selected_action = str(input("Opção selecionada: "))
                selected_action = selected_action[0]

                if selected_action == "N":
                    continue
                if selected_action == "F":
                    break

    sorted_numbers = random.sample(
        range(1, selected_lottery.get_numbers_quantity()),
        selected_lottery.get_sorted_numbers_quantity(),
    )

    print()
    print(f"Resultado da {selected_lottery.get_name()}: {str(sorted_numbers)}")

    statistics = dict({})
    for bet in bets:
        hits = set(bet.get_betting_numbers()) & set(sorted_numbers)
        hits = len(hits)

        if bet.get_user_name() not in statistics:
            statistics[bet.get_user_name()] = []

        statistics[bet.get_user_name()].append(
            {"betting_numbers": bet.get_betting_numbers(), "hits": hits}
        )

    for user, user_bets in statistics.items():

        sorted_bets = sorted(user_bets, key=lambda bet: bet["hits"], reverse=True)

        print()
        print(f"Usuário: {user}")
        print(f"  Total de apostas: {len(user_bets)}")

        for id_bet, bet in enumerate(sorted_bets, start=1):
            print(
                f"  Aposta {id_bet}: {bet["betting_numbers"]} - {bet["hits"]} acertos"
            )


main()

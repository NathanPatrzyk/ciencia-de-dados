from lottery import Lottery


class Bet:
    def __init__(self, user_name: str, loterry: Lottery, betting_numbers: list):
        self.__user_name = user_name
        self.__lottery = loterry
        self.__betting_numbers = betting_numbers

    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name

    def set_lottery(self, lottery: Lottery):
        self.__lottery = lottery

    def get_lottery(self):
        return self.__lottery

    def set_betting_numbers(self, betting_numbers: list):
        self.__betting_numbers = betting_numbers

    def get_betting_numbers(self):
        return self.__betting_numbers

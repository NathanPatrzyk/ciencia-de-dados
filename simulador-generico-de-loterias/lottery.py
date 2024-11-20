class Lottery:
    def __init__(self, name: str, numbers_quantity: int, sorted_numbers_quantity: int):
        self.__name = name
        self.__numbers_quantity = numbers_quantity
        self.__sorted_numbers_quantity = sorted_numbers_quantity

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_numbers_quantity(self, numbers_quantity: int):
        self.__numbers_quantity = numbers_quantity

    def get_numbers_quantity(self):
        return self.__numbers_quantity

    def set_sorted_numbers_quantity(self, sorted_numbers_quantity: int):
        self.__sorted_numbers_quantity = sorted_numbers_quantity

    def get_sorted_numbers_quantity(self):
        return self.__sorted_numbers_quantity

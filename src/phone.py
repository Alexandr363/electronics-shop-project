from src.item import Item


class Phone(Item):
    """
    Класс для конкретного вида товара в магазине
    """
    def __init__(self, name: str, price: float, quantity: int,
                 number_of_sim: int) -> None:
        """
        Переопределение родительского метода init
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, " \
               f"{self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер атрибута number_of_sim, возвращает значение number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        """
        Сеттер атрибута number_of_sim, проверят, что значение не равно 0
        """
        if number_of_sim == 0:
            raise ValueError('Количество физических SIM-карт должно быть '
                             'целым числом больше нуля')
        self.__number_of_sim = number_of_sim

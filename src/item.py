import csv


class Item:
    """
    Класс для представления товара в магазине
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        """
        Создание экземпляра класса item
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, " \
               f"{self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и '
                             'дочерние от них.')
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, filename) -> None:
        """
        Открывает файл csv, создаёт экземпляры классы Item на основании данных
        из открытого файла
        """
        Item.all = []
        with open(filename, newline='',
                  encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = str(row['name'])
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @property
    def name(self):
        """
        Геттер атрибута __name, возвращает значение __name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Сеттер атрибута __name, проверяет длину переданного имени экземпляра
        и обрезает её до 10 символов (если она больше)
        """
        if len(name) <= 10:
            self.__name = name
        if len(name) >= 10:
            name = name[:10]
            self.__name = name

    @staticmethod
    def string_to_number(data: str) -> int:
        """
        Принимает строку и возвращает значение int
        """
        if len(data) > 1:
            return int(data.split('.')[0])
        return int(data)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара
        """
        self.price *= self.pay_rate

from src.item import Item


class MixinKeyboard:
    """
    Миксин, добавляет функцию смены языка классу Keyboard
    """
    LANGUAGE = 'EN'

    def __init__(self):
        self.__language = 'EN'
        MixinKeyboard.__language = self.__language

    def change_lang(self):
        """
        Функция меняет язык
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinKeyboard):
    """
    Класс для клавиатуры в магазине
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

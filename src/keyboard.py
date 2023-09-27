from src.item import Item


class MixinKeyboard:
    """
    Миксин, добавляет функцию смены языка классу Keyboard
    """
    _LANGUAGE = 'EN'

    def change_lang(self):
        """
        Меняет язык
        """
        if self._LANGUAGE == 'EN':
            self._LANGUAGE = 'RU'
        elif self._LANGUAGE == 'RU':
            self._LANGUAGE = 'EN'

    @property
    def language(self):
        return self._LANGUAGE


class Keyboard(Item, MixinKeyboard):
    """
    Класс для клавиатуры в магазине
    """
    pass

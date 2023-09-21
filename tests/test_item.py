"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


phone = Item('tel', 10, 5)
Item.pay_rate = 5


def test_calculate_total_price():
    assert phone.calculate_total_price() == 50


def test_apply_discount():
    phone.apply_discount()
    assert phone.price == 50


def test_string_to_number():
    assert Item.string_to_number('357.19') == 357
    assert Item.string_to_number('9') == 9


def test_name_setter():
    test = Item('Пылесос', 500, 1)
    test.name = 'Утюг'
    assert test.name == 'Утюг'
    test.name = 'Мультиварка'
    assert test.name == 'Мультиварк'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('/Users/mac/Dev/electronics-shop-project'
                              '/src/items.csv')
    assert len(Item.all) == 5


def test_repr():
    phone = Item('Телефон', 5, 2)
    assert repr(phone) == "Item('Телефон', 5, 2)"


def test_str():
    phone = Item('Телефон', 5, 2)
    assert str(phone) == 'Телефон'


def test_add():
    tv = Item("tv", 35000, 1)
    smart = Phone("smart", 95000, 2, 1)
    assert tv + smart == 3

"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


phone = Item('tel', 10, 5)
Item.pay_rate = 5


def test_calculate_total_price():
    assert phone.calculate_total_price() == 50


def test_apply_discount():
    phone.apply_discount()
    assert phone.price == 50
